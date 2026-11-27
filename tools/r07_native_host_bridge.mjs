// Native host bridge for authorized GitHub connector callables.
export const REPO = "xfraggelpower666x/666PFS_CSM";
export const PROBE = "integration/pfs-r07-cas-probe-20261127";
const valid = s => typeof s === "string" && /^[0-9a-f]{40}$/.test(s);
export async function publishProbe(host, expected, target) {
  if (!valid(expected) || !valid(target)) throw Error("INVALID_HEAD");
  const head = async () => {
    const r = await host.fetch_commit({repo_full_name: REPO, commit_sha: PROBE});
    const sha = r.result.commit.sha;
    if (!valid(sha)) throw Error("INVALID_READBACK");
    return sha;
  };
  if (await head() !== expected) throw Error("HEAD_DRIFT");
  const result = await host.update_ref({repository_full_name: REPO,
    branch_name: PROBE, sha: target, expected_sha: expected, force: false});
  if (result.result.success !== true) throw Error("CAS_REJECTED");
  if (await head() !== target) throw Error("READBACK_PENDING");
  return target;
}
