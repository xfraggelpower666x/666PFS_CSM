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
