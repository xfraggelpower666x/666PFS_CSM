---
name: 666pfs-child-lifecycle
description: "Handle explicitly selected PFS child lifecycle while preserving functional identity and native authority."
---

Read [authority](../../references/authority.md) before execution. Current repository contracts outrank this workflow.

Purpose:

Safely manage child identity/state without automatic activation.

Child foreground states:

FOREGROUND
REHYDRATED_IDLE
NOT_REHYDRATED

Rules:

CHILD_AUTOLOAD=FORBIDDEN

NO_GLOBAL_LAST_CHILD=TRUE

NO_CROSS_CHAT_CHILD_FOREGROUND_INHERITANCE=TRUE

REPOSITORY_HEAD_NE_CHILD_FOREGROUND=TRUE

Functional identity outranks name or ID similarity.

NAME_OR_ID_MATCH_NOT_EQUAL_FUNCTIONAL_IDENTITY_MATCH=TRUE

AMBIGUOUS_CHILD_MATCH=READ_CHILD_BEFORE_BINDING

UNVERIFIED_CHILD_REUSE=FORBIDDEN

FUNCTIONAL_IDENTITY_MISMATCH=KEEP_EXISTING_CHILD_UNCHANGED

CHILD_REDEFINITION_TO_FIT_NEW_REQUEST=FORBIDDEN

Retired identities must not be resurrected.

External native systems may be referenced without authority transfer.

---

## Policy V1.0 — classification at UPDATE / NEW CHILD
Resolve governance/CHILD_AUTHORITY_STORAGE_POLICY_V1.md from verified current. Before child registration or update classify functional identity and canonical owner: EXTERNAL_BACKUP_CHILD (origin Repo/Drive live; PFS backup only), PFS_LOCAL_LIVE_CHILD (PFS-owned runtime), SYSTEM_ARTIFACT_CHILD (PFS-owned verified package). Ordering: origin live current > origin-native repo/Drive backup > PFS backup. Unknown owner => HOLD. Do not bulk-reclassify, autoload, deploy or infer live state from ZIP. New children require an explicit user-directed child creation scope; no automatic authority transfer.
