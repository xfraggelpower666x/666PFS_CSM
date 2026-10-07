---
name: 666pfs-backup-governance
description: "Govern requested PFS backup and recovery with exact native approvals, real archive bytes and direct readback."
---

Read [authority](../../references/authority.md) before execution. Current repository contracts outrank this workflow.

Purpose:

Manage PFS-owned backup/recovery orchestration and approval gates.

PFS may coordinate backups only within verified authority and approval scope.

For foreign-native systems such as LYVRA or CLIC:

- read approval from their native authority
- never self-approve
- never mutate foreign live systems
- fail closed on stale/mismatched approval
- preserve old backup provenance
- direct readback required after backup write
- verify actual bytes before claiming SHA-256
- never invent archive hashes or binary parity

Coupled backup rule currently used:

EVERY_LYVRA_PLUGIN_BACKUP_ROUND_REQUIRES_CLIC_BACKUP_LEG

Both native legs must independently be fresh where the current contract requires it.

---

Read [plugin lifecycle](../../references/plugin-lifecycle.md) for native plugin-current inspection, impact, parity and backup requirements.
