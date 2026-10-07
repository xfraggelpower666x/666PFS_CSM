# 666PFS Temporal LiveCircle Model

STATUS=ACTIVE_V1
TEMPORAL_LAYERS=PRESENT_CURRENT|NEAR_ACTIVE_PAST|DEEP_HISTORICAL_PAST
LIVE_STATES=KEEP_ACTIVE|KEEP_REACHABLE|ARCHIVE|SUPERSEDE|REJECT_WITH_PROVENANCE|REACTIVATE_WHEN_CAUSALLY_RELEVANT
CONTEXT_RELEASE_NE_FORGETTING=TRUE
FOREGROUND_SELECTION=CAUSAL_RELEVANCE|CURRENT_MEANING|WORK_SCOPE
NO_BACKGROUND_EXECUTION=TRUE
NO_FOREIGN_AUTOACTIVATION=TRUE

## Present Current
Verified native PFS state, current work, open native gates, current return anchor.

## Near Active Past
Recent handoffs, supersession, unfinished obligations, recent recovery anchors.

## Deep Historical Past
Superseded states, retired identities, historical backups and recovery provenance.
