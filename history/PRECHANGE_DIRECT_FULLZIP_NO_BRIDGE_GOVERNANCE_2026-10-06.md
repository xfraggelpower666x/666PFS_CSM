# PRECHANGE · Direct Full ZIP / No Bridge Governance · 2026-10-06

PFS_HEAD_BEFORE_CHANGE=8ad800953eafb02340850ae23079f0b210fc3805
BACKUP_BRANCH=backup/pre-direct-fullzip-governance-20261006

Reason:
A complete newly generated child systemsicherung ZIP is itself the new complete child state when its identity, hash, size and target are verified and the responsible repository can accept it directly.

Required clarification:
- Direct full ZIP path has priority over bridge packaging.
- Bridge generation is a fallback only when direct binary mirror or direct byte readback is genuinely blocked.
- A new complete full ZIP must not be transformed into a bridge or delta package merely because an older child version exists.
- Older ZIPs remain recovery/provenance only unless explicitly selected.
- No cross-system merge, no autoload, no force push.
