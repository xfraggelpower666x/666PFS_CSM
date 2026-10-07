---
name: 666pfs-backup-governance
description: "Govern PFS plugin backup rounds, native approvals, real archive bytes, backup children and direct readback."
---

Read [authority](../../references/authority.md) before execution. Current repository contracts outrank this workflow.

Purpose:

Manage PFS-owned backup/recovery orchestration and coordinated managed-plugin backup rounds.

Before any private-repository or foreign-leg backup notice:

- inventory all PFS-managed plugin backups
- verify each current live plugin version/release/fingerprint
- verify repo source parity and binary parity
- classify development impact
- complete all PFS-owned plugin evolution first
- freeze one stable backup-round manifest
- inform LYVRA once for the stable round
- inform CLIC once for the stable round

ONE_COORDINATED_NOTICE_PER_STABLE_ROUND=TRUE
NEW_RELEVANT_PLUGIN_CHANGE_AFTER_ROUND_FREEZE=NEW_ROUND_REQUIRED

For foreign-native systems such as LYVRA or CLIC:

- read approval from their native authority
- never self-approve
- never mutate foreign live systems
- fail closed on stale/mismatched approval
- preserve old backup provenance
- direct readback required after backup write
- verify actual bytes before claiming SHA-256
- never infer binary parity from text parity

LYVRA_AUTHORIZES_ONLY_LYVRA_LEG=TRUE
CLIC_AUTHORIZES_ONLY_CLIC_LEG=TRUE
PFS_SELF_APPROVAL_OF_FOREIGN_LEGS=FORBIDDEN
FOREIGN_NATIVE_APPROVAL_REMAINS_PER_SYSTEM=TRUE

PFS may authorize and back up its own plugin under native PFS governance after real live/readback/parity checks.

Read [plugin lifecycle](../../references/plugin-lifecycle.md) for native plugin-current inspection, impact, coordinated round, parity and backup requirements.
