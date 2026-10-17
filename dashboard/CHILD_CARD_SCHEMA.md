# 666PFS Child Card Schema

Each registered child is represented visually by a card derived from canonical registry and child files.

Required fields when known:
- display name
- entry ID
- system ID
- version
- role / purpose
- status
- trigger summary
- repository path or external authority reference
- rehydration state
- readback state
- update state
- recovery state
- dependency / relation summary

A card is informational and navigational only. Rendering a card must never autoload or execute the child.

Suggested visual status mapping:
- VERIFIED -> green indicator
- PARTIAL / READBACK_PENDING -> amber indicator
- BLOCKED / CONFLICT_QUARANTINE / WRITE_BLOCKED -> red indicator
- OPEN / PROPOSED -> neutral indicator

## Storage authority fields
CLASSIFICATION=EXTERNAL_BACKUP_CHILD|PFS_LOCAL_LIVE_CHILD|SYSTEM_ARTIFACT_CHILD|UNKNOWN_HOLD
SOURCE_LIVE_AUTHORITY=VERIFIED_GITHUB_OR_DRIVE_OWNER
ORIGIN_NATIVE_BACKUP=SECONDARY_VERIFIED_OR_PENDING
PFS_BACKUP=TERTIARY_VERIFIED_OR_PENDING
PFS_ROLE=EVIDENCE_BOUND
STORAGE_MODE=EVIDENCE_BOUND
RESTORE_STATUS=INDEPENDENTLY_VERIFIED
UI_NE_AUTHORITY=TRUE
