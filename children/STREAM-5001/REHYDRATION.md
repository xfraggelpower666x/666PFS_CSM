# STREAM-5001 Rehydration

1. Read SYSTEM_IDENTITY.md.
2. Read RUNTIME_BINDING.md.
3. Resolve the current live state from the origin repository xfraggelpower666x/WebRadio-666SOUNDsDESIGn on branch WebRadio-666SOUNDsDESIGn.
4. Treat any commit stored in this PFS child as backup/provenance evidence only, never as the live pointer.
5. PFS child content is backup/recovery/registry only and must not override the origin repository.
6. Do not mutate the origin repository during rehydration.
7. If origin identity or repository evidence conflicts, set HOLD and require controlled re-audit.
8. Child autoload remains forbidden; rehydrate only after explicit selection.

LIVE_AUTHORITY=ORIGIN_REPOSITORY
PFS_CHILD_ROLE=BACKUP_RECOVERY_REGISTRY_ONLY
PFS_CHILD_LIVE_AUTHORITY_OVERRIDE=FORBIDDEN
PFS_CHILD_RUNTIME_AUTHORITY=NONE
PFS_CHILD_DEPLOYMENT_AUTHORITY=NONE
PFS_CHILD_ROUTING_AUTHORITY=NONE
NO_DOWNGRADE=TRUE
