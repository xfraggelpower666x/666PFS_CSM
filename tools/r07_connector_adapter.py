"""Bind the R07 guard to an authorized GitHub connector, without force.

The host supplies the two tool callables. No credentials are stored here.
"""
from r07_writer import REPO, BRANCH, publish

class GitHubConnectorAdapter:
    def __init__(self, fetch_commit, update_ref):
        self.fetch_commit = fetch_commit
        self.update_ref = update_ref

    @staticmethod
    def scope(repo, branch):
        if (repo, branch) != (REPO, BRANCH):
            raise ValueError("OUTSIDE_SCOPE")

    def head(self, repo, branch):
        self.scope(repo, branch)
        return self.fetch_commit(repo_full_name=repo,
                                 commit_sha=branch)["result"]["commit"]["sha"]

    def compare_and_swap(self, repo, branch, expected, commit, force=False):
        self.scope(repo, branch)
        if force:
            raise ValueError("FORCE_FORBIDDEN")
        response = self.update_ref(repository_full_name=repo, branch_name=branch,
                                   sha=commit, expected_sha=expected, force=False)
        return response["result"]["success"] is True

def publish_with_connector(fetch_commit, update_ref, expected, commit):
    return publish(GitHubConnectorAdapter(fetch_commit, update_ref), expected, commit)
