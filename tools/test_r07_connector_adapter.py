import unittest
from r07_connector_adapter import GitHubConnectorAdapter, publish_with_connector
from r07_writer import REPO, BRANCH
A, B = "a"*40, "b"*40
class Host:
    def __init__(self):
        self.sha = A
        self.calls = []
    def fetch(self, **kw):
        assert kw == dict(repo_full_name=REPO, commit_sha=BRANCH)
        return {"result":{"commit":{"sha":self.sha}}}
    def update(self, **kw):
        self.calls.append(kw)
        assert kw["repository_full_name"] == REPO
        assert kw["branch_name"] == BRANCH
        assert kw["force"] is False
        if kw["expected_sha"] != self.sha:
            return {"result":{"success":False}}
        self.sha = kw["sha"]
        return {"result":{"success":True}}
class ConnectorTests(unittest.TestCase):
    def test_publish(self):
        h = Host()
        self.assertEqual(publish_with_connector(h.fetch,h.update,A,B),B)
        self.assertEqual(h.calls[0]["expected_sha"],A)
    def test_stale(self):
        h = Host()
        with self.assertRaisesRegex(ValueError,"HEAD_DRIFT"):
            publish_with_connector(h.fetch,h.update,B,A)
        self.assertEqual(h.calls,[])
    def test_force(self):
        h = Host()
        with self.assertRaisesRegex(ValueError,"FORCE_FORBIDDEN"):
            GitHubConnectorAdapter(h.fetch,h.update).compare_and_swap(REPO,BRANCH,A,B,True)
    def test_scope(self):
        h = Host()
        with self.assertRaisesRegex(ValueError,"OUTSIDE_SCOPE"):
            GitHubConnectorAdapter(h.fetch,h.update).head(REPO,"main")
    def test_transport_error(self):
        h = Host()
        def fail(**kw): raise OSError("transport")
        with self.assertRaises(OSError):
            publish_with_connector(h.fetch,fail,A,B)
    def test_rejected(self):
        h = Host()
        with self.assertRaisesRegex(ValueError,"CAS_REJECTED"):
            publish_with_connector(h.fetch,lambda **kw:{"result":{"success":False}},A,B)
if __name__ == "__main__": unittest.main()
