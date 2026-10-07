---
name: 666pfs-csm
description: "Handle requested coordination through CSM as an internal PFS service with its own sub-LifeCircle."
---

Read [authority](../../references/authority.md) before execution. Current repository contracts outrank this workflow.

Purpose:

Operate 666CSM strictly as an internal 666PFS service.

Rules:

PFS_NE_CSM=TRUE
CSM_NE_SECOND_SYSTEM=TRUE
CSM_NE_CHILD=TRUE

CSM Sub-LifeCircle:

VERIFY_ROOT_PFS_CURRENT
→ LOAD_REGISTRY
→ LOAD_CHILD_LIFECYCLE_RELATIONS
→ LOAD_WRITE_ORDER_STATE
→ LOAD_LOCKS_AND_CONFLICTS
→ LOAD_PENDING_READBACKS
→ LOAD_RECOVERY_ANCHORS
→ EXECUTE_COORDINATION
→ VERIFY_RESULTS
→ RETURN_TO_WHOLE_PFS

CSM must never acquire independent system authority.

---
