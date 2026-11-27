"""Read-only Git object parity check for R07, run in a full PFS checkout."""
import subprocess
import sys
BASE = "08989d5dc71259cbebf108c71d2e315aa9ac28a1"
SOURCES = (
    ("2d96b328b539c011a114cb30802e12703e20b3a6", "children/CURES-16001/", 66),
    ("7ce8d2df0869c13879f57ebfa6d6545df37dc129", "children/CYBERINTRO-38001/", 24),
)
def git(*args):
    return subprocess.check_output(["git", *args])
def tree(ref, prefix):
    result = {}
    for entry in git("ls-tree", "-r", "-z", ref, "--", prefix).split(b"\0"):
        if entry:
            meta, path = entry.split(b"\t", 1)
            result[path] = meta
    return result
def verify(target):
    total = 0
    for source, prefix, expected in SOURCES:
        baseline = tree(BASE, prefix)
        original = tree(source, prefix)
        merged = tree(target, prefix)
        changed = {p: m for p, m in original.items() if baseline.get(p) != m}
        if len(changed) != expected or any(p in baseline for p in changed):
            raise RuntimeError("SOURCE_SCOPE_MISMATCH " + prefix)
        if any(merged.get(p) != m for p, m in changed.items()):
            raise RuntimeError("BLOB_OR_MODE_MISMATCH " + prefix)
        if any(merged.get(p) != m for p, m in baseline.items()):
            raise RuntimeError("BASELINE_CHANGED " + prefix)
        print(prefix, len(changed), "PASS")
        total += len(changed)
    if total != 90:
        raise RuntimeError("COUNT_MISMATCH")
    print("R07 GIT BLOB AND MODE PARITY:", total, "PASS")
if __name__ == "__main__":
    verify(sys.argv[1] if len(sys.argv) > 1 else "HEAD")
