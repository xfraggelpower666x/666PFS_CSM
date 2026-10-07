# 666PFS Scope Map

STATUS=ACTIVE_V1
ROLE=NON_AUTHORITY_SCOPE_INDEX
SCOPE_MAP_NE_ROUTER=TRUE
SCOPE_MAP_NE_AUTHORITY=TRUE

## Required fields
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

## Resolution rules
Functional identity outranks name-only match.
Ambiguous identity => HOLD_AND_AUDIT.
External authority remains external.
Foreground selection is causal/task scoped only.
