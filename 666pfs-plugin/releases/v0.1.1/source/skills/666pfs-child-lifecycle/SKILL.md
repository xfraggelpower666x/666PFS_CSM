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
