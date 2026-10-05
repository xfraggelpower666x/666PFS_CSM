# 666PFS Live-Circle Current

DATE=2026-10-05
SYSTEM_ID=666PFS-CORE-001
NAMESPACE=666PFS
MODE=REPO_FIRST_CONTINUITY

## Rehydrate in this order
1. README.md
2. governance/SYSTEM_IDENTITY.md
3. governance/REHYDRATION_CONTRACT.md
4. csm/COORDINATION_CONTRACT.md
5. registry/README.md
6. registry/REHYDRATION_MATRIX.md
7. registry/CURRENT_STATE.md
8. handoff/LYVRA_PLUGIN_BACKUP_HANDOFF_CURRENT.md when PENDING_EXTERNAL_HANDOFF=LYVRA_PLUGIN_BACKUP_REFRESH
9. dashboard/DASHBOARD_CONTRACT.md
10. dashboard/CURRENT_DASHBOARD.md
11. children/CHILD_INVENTORY.md
12. children/FUNCTIONAL_MIGRATION_QUEUE.md
13. registry/CURRENT_POINTER.md

## Resume state
SELECTED_CHILD=NONE
FUNCTIONAL_CHILD_PAYLOAD_MIGRATION=OPEN
IDENTITY_CONFLICT_QUARANTINE=ACTIVE
REPO_ROLE=PRIMARY_RUNTIME_CONTROL_SURFACE
DRIVE_ROLE=HISTORY_BACKUP_RECOVERY
PENDING_EXTERNAL_HANDOFF=LYVRA_PLUGIN_BACKUP_REFRESH
PENDING_EXTERNAL_HANDOFF_PATH=handoff/LYVRA_PLUGIN_BACKUP_HANDOFF_CURRENT.md
PENDING_HANDOFF_ACTION=READ_AND_VALIDATE_ONLY_UNTIL_EXPLICIT_666PFS_UPDATE

## Continuity rule
On 666PFS SYSTEMSTART or 666PFS WEITER, rehydrate from repository current state and pointer first.
Do not promote history, backups, old handoffs or Drive material over a newer valid repository state.
Do not auto-load children. Resolve only an explicitly selected PFS target.
A pending external handoff may be read automatically as evidence, but it must not activate a child, mutate PFS state, or transfer foreign authority without an explicit 666PFS UPDATE.

## Evidence rule
FOUND != VERIFIED
SEARCH_RESULT != READBACK
READ != REHYDRATED
NEWER_VALID_EVOLUTION > OLDER_VALID_STATE
