# 666CSM Coordination Contract

666CSM is the internal coordination service of 666PFS.

Responsibilities:
- registry coordination
- child lifecycle governance
- continuity and recovery routing
- write-order enforcement
- post-write readback enforcement

Boundaries:
- no child autoload
- no cross-child merge
- no foreign-system mutation
- no authority invention
- pointer-style publication is always the last mutation of a governed update

## Child storage/authority classification
At UPDATE and NEW CHILD, coordinate evidence-first EXTERNAL_BACKUP_CHILD / PFS_LOCAL_LIVE_CHILD / SYSTEM_ARTIFACT_CHILD classification using governance/CHILD_AUTHORITY_STORAGE_POLICY_V1.md. CSM is not an independent owner or child. On ambiguity HOLD. Never reclassify existing children automatically or infer runtime authority from a backup ZIP.
