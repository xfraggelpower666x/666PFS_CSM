"""PFS-only additive Git tree writer. No force, no production promotion."""
import re

REPO = "xfraggelpower666x/666PFS_CSM"
BRANCH = "integration/pfs-r07-writer-20261127"
PREFIXES = ("children/CURES-16001/", "children/CYBERINTRO-38001/")

def plan(entries, lookup):
    """lookup(path) returns existing blob SHA or None; errors must propagate."""
    result = []
    seen = set()
    for path, sha in entries:
        if not path.startswith(PREFIXES) or any(p in ("", ".", "..") for p in path.split("/")):
            raise ValueError("OUTSIDE_SCOPE")
        if not re.fullmatch(r"[0-9a-f]{40}", sha) or path in seen:
            raise ValueError("INVALID_OR_DUPLICATE_ENTRY")
        seen.add(path)
        old = lookup(path)
        if old is not None and old != sha:
            raise ValueError("EXISTING_SOURCE_CONFLICT: " + path)
        if old is None:
            result.append(dict(path=path, sha=sha, mode="100644", type="blob"))
    return result

def publish(api, expected, commit):
    """Adapter must enforce expected SHA atomically; never fall back to force."""
    if not all(re.fullmatch(r"[0-9a-f]{40}", s) for s in (expected, commit)):
        raise ValueError("INVALID_HEAD")
    if api.head(REPO, BRANCH) != expected:
        raise ValueError("HEAD_DRIFT")
    if not api.compare_and_swap(REPO, BRANCH, expected, commit, force=False):
        raise ValueError("CAS_REJECTED")
    if api.head(REPO, BRANCH) != commit:
        raise ValueError("READBACK_PENDING")
    return commit
