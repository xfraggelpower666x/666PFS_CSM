---
name: 666pfs-lifecircle
description: "Handle requested PFS daemon and temporal LifeCircle continuity using current repository contracts."
---

Read [authority](../../references/authority.md) before execution. Current repository contracts outrank this workflow.

Purpose:

Operate PFS native continuity architecture.

Current native carriers include:

governance/PFS_DAEMON_LIFECIRCLE_CONTRACT.md
governance/CHILD_LIFECIRCLE_STANDARD.md
csm/LIFECIRCLE_REHYDRATION.md
registry/PFS_SCOPE_MAP.md
handoff/TEMPORAL_LIVE_CIRCLE_MODEL.md

PFS Shared Daemon:

ROLE=
PROCESS_GUIDANCE
STATE_STEWARDSHIP
CONTINUITY_SUPPORT

The daemon has:

DECISION_AUTHORITY=NONE

DAEMON_NE_CSM=TRUE
DAEMON_NE_ROUTER=TRUE
DAEMON_NE_CONTROLLER=TRUE

Daemon LifeCircle:

LOAD_CORE
→ LOAD_PROCESS_STATE
→ RESOLVE_SCOPE
→ LOAD_RELEVANT_ADAPTER
→ LOAD_OPEN_PROBLEMS
→ LOAD_PENDING_NATIVE_APPROVALS
→ SURFACE_NEXT_CAUSAL_STEP
→ TRACK_RESULT
→ UPDATE_LOCAL_PROCESS_STATE

---
