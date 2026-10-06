# PRECHANGE · Repo-First / Child Backup-Only Authority · 2026-10-06

PFS_HEAD_BEFORE_CHANGE=804a93fa0d222bbcdde7665e7f1c499bbeadfc30
BACKUP_BRANCH=backup/pre-repo-first-child-backup-only-20261006

Clarification:
- The responsible external/native/source repository is the live/current functional authority.
- A PFS child representing that external system is backup/recovery/registry only.
- PFS metadata about the child remains governed by 666PFS_CSM.
- A PFS child must never override the live source repository, deployment, routing, runtime, or native authority.
- Drive remains history/backup/recovery only where applicable.
- No autoload, no cross-system merge, no downgrade.
