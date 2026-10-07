---
name: 666pfs-backup-governance
description: "Govern coordinated PFS managed-plugin backup rounds, native approvals, private-repo integration notices, real bytes, backup children and readback."
---

Read [authority](../../references/authority.md) before execution. Current repository contracts outrank this workflow.

Purpose:

Manage PFS-owned backup/recovery orchestration and coordinated managed-plugin backup rounds.

On every PFS UPDATE:
- inventory all PFS-managed plugin backups
- verify current live version, release ID and runtime fingerprint
- verify repo source parity and binary parity where applicable
- classify whether each plugin evolved
- classify backup need and approval freshness

If plugin evolution is detected:
- complete all PFS-owned plugin evolution first
- freeze one stable managed-plugin set
- inform LYVRA once for that stable set
- inform CLIC once for that stable set
- request LYVRA's native backup authorization for its own leg
- request CLIC's native backup authorization for its own leg
- explicitly notify LYVRA that the round targets private-repository plugin-backup integration

ONE_COORDINATED_NOTICE_PER_STABLE_ROUND=TRUE
NEW_RELEVANT_PLUGIN_CHANGE_AFTER_ROUND_FREEZE=NEW_ROUND_REQUIRED
FINGERPRINT_OR_RELEASE_CHANGE_BREAKS_STABLE_SET=TRUE

For foreign-native systems such as LYVRA or CLIC:
- read approval from their native authority
- never self-approve
- never mutate foreign live systems
- fail closed on stale/mismatched approval
- preserve old backup provenance
- direct readback required after backup write
- verify actual bytes before claiming SHA-256
- never infer binary parity from text parity

LYVRA_LIVE_REPOSITORY_REMAINS_APPROVAL_AUTHORITY=TRUE
LYVRA_PRIVATE_REPOSITORY_ROLE=PLUGIN_BACKUP_STORAGE_ONLY
LYVRA_AUTHORIZES_ONLY_LYVRA_LEG=TRUE
CLIC_AUTHORIZES_ONLY_CLIC_LEG=TRUE
PFS_SELF_APPROVAL_OF_FOREIGN_LEGS=FORBIDDEN
FOREIGN_NATIVE_APPROVAL_REMAINS_PER_SYSTEM=TRUE

PFS may authorize and back up its own plugin under native PFS governance after real live/readback/parity checks.

Read [plugin lifecycle](../../references/plugin-lifecycle.md) for native plugin-current inspection, impact, stable-set coordination, parity and backup requirements.
