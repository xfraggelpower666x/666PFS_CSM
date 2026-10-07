---
name: 666pfs-scope-map
description: "Resolve requested task-local PFS scope from the current verified Scope Map without creating routing authority."
---

Read [authority](../../references/authority.md) before execution. Current repository contracts outrank this workflow.

Purpose:

Resolve task-local foreground scope.

Scope Map fields:

ID
ALIASES
FUNCTIONAL_IDENTITY
AUTHORITY_CLASS
SOURCE_REPO
SOURCE_ROOT
PFS_ROLE
REHYDRATION_CARRIER
RECOVERY_ROOT
FOREGROUND_ELIGIBILITY

Rules:

SCOPE_MAP_NE_ROUTER=TRUE
SCOPE_MAP_NE_AUTHORITY=TRUE

Scope selection is causal and task-local.

Do not convert the Scope Map into a global dispatcher.

---
