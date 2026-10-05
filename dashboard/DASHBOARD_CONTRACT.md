# 666PFS / 666CSM Dashboard Contract

The dashboard is a required system surface, not a separate authority.

## Whole-System Dashboard
Render from canonical repository state only:
- PFS core identity and version
- current repository HEAD / branch
- authority and rehydration state
- registry state
- lock / queue / recovery state when available
- current lifecycle stage
- open / blocked / partial work
- 666CSM coordination state
- child-system overview

## Status vocabulary
- VERIFIED
- DERIVED
- PROPOSED
- OPEN
- BLOCKED
- PARTIAL
- WRITE_BLOCKED
- READBACK_PENDING
- CONFLICT_QUARANTINE

## Hard rules
- dashboard data must be derived from canonical repository files
- no parallel dashboard database
- no child autoload
- no cross-child merge
- no foreign-system mutation
- unknown state is displayed as unknown / hold, never invented
