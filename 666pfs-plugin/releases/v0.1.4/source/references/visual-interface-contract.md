# PFS / CSM Visual Interface Contract

Purpose: evidence-first visual presentation of verified runtime state.

Hard guards:
- VISUAL_NE_AUTHORITY
- VISUAL_NE_ROUTER
- VISUAL_NE_ACTIVATION
- VISUAL_NE_WRITE_APPROVAL
- BACKUP_NE_CURRENT
- HISTORY_NE_CURRENT
- FOUND_NE_VERIFIED
- SEARCH_RESULT_NE_READBACK
- READ_NE_REHYDRATED
- POINTER_LAST_REQUIRED_FOR_PUBLISHED_CURRENT

Recommended structure: header identity card, authority/current card, lifecycle card, child/scope card, evidence/status matrix, blockers/readbacks, handoff card, next-action card.

Visual Standstill / Freeze card:
- reason for stop
- last verified checkpoint
- current lock/write state
- unresolved obligations
- exact return anchor
- whether mutation is forbidden, pending or complete

The view is descriptive only. Repository evidence remains authoritative.
