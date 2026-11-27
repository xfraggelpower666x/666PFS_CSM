// PFS-only publication guard. Host must supply authorized connector functions.
// No credentials, force push, child activation or foreign repository access.
const REPO = "xfraggelpower666x/666PFS_CSM";
const MAIN = "main";
const POINTER = "registry/CURRENT_POINTER.md";
const valid = s => typeof s === "string" && /^[0-9a-f]{40}$/.test(s);
const allowedBody = new Set([
  "tools/r07_writer.py", "tools/r07_connector_adapter.py",
  "tools/r07_native_host_bridge.mjs", "tools/test_r07_writer.py",
  "tools/test_r07_connector_adapter.py", "tools/test_r07_native_host_bridge.mjs",
  "tools/r07_production_publisher.mjs", "tools/test_r07_production_publisher.mjs",
  ".github/workflows/pfs-r07-production-acceptance.yml",
  "history/PFS_R07_PRODUCTION_ACCEPTANCE_20261127.md"
]);
export async function publishPfs(host, request) {
  const {expected, target, backup, phase, approvedTarget} = request;
  if (!valid(expected) || !valid(target) || expected === target ||
      approvedTarget !== target || !["body","pointer"].includes(phase))
    throw Error("INVALID_OR_UNAPPROVED_TARGET");
  if (typeof backup !== "string" || !/^backup\/pfs-r07-[a-z0-9-]+$/.test(backup))
    throw Error("INVALID_BACKUP_SCOPE");
  const read = async ref => {
    const r = await host.fetch_commit({repo_full_name:REPO,commit_sha:ref});
    const sha = r.result.commit.sha;
    if (!valid(sha)) throw Error("INVALID_READBACK");
    return sha;
  };
  if (await read(MAIN) !== expected) throw Error("HEAD_DRIFT");
  if (await read(backup) !== expected) throw Error("BACKUP_MISMATCH");
  const r = await host.compare_commits({repo_full_name:REPO,base:expected,head:target});
  const d = r.result;
  if (d.too_large || !Array.isArray(d.files) || d.files.length === 0)
    throw Error("DIFF_UNVERIFIED");
  if (phase === "pointer") {
    if (d.files.length !== 1 || d.files[0].filename !== POINTER ||
        d.files[0].status !== "modified") throw Error("POINTER_NOT_LAST");
  } else if (d.files.some(f => !allowedBody.has(f.filename) || f.status !== "added")) {
    throw Error("BODY_SCOPE_VIOLATION");
  }
  if (await read(MAIN) !== expected) throw Error("HEAD_DRIFT");
  const w = await host.update_ref({repository_full_name:REPO,branch_name:MAIN,
    sha:target,expected_sha:expected,force:false});
  if (w.result.success !== true) throw Error("CAS_REJECTED");
  if (await read(MAIN) !== target) throw Error("READBACK_PENDING");
  return target;
}
