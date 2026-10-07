# 666PFS Child LifeCircle Standard

STATUS=ACTIVE_V1
CHILD_AUTOLOAD=FORBIDDEN
NO_GLOBAL_LAST_CHILD=TRUE
NO_CROSS_CHAT_CHILD_FOREGROUND_INHERITANCE=TRUE
REPOSITORY_HEAD_NE_CHILD_FOREGROUND=TRUE

## Foreground states
FOREGROUND
REHYDRATED_IDLE
NOT_REHYDRATED

## Rules
FOREGROUND requires direct current task relevance and verified identity binding.
REHYDRATED_IDLE may remain reachable without becoming active authority.
NOT_REHYDRATED remains unloaded.
Ambiguous identity => HOLD_AND_AUDIT.
Retired identity => DO_NOT_RESURRECT.
External native system => REFERENCE_WITHOUT_AUTHORITY_TRANSFER.
