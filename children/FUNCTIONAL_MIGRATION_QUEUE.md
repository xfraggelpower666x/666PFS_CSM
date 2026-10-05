# Functional Child Migration Queue

Goal: each eligible child becomes a repository-native, rehydratable child system rather than a registry-only entry.

## Required child package contract
Each migrated child must provide, as evidence permits:
- SYSTEM_IDENTITY.md
- CURRENT_STATE.md
- REHYDRATION.md
- TRIGGERS.md
- runtime/ or an explicit external-runtime binding
- config/ where applicable
- docs/
- recovery / provenance metadata
- dashboard card metadata

## Migration rules
1. Read the latest verified child state from canonical evidence.
2. Preserve ENTRY_ID and SYSTEM_ID.
3. Do not invent missing runtime files.
4. Copy or bind only verified functional material.
5. Re-audit after migration.
6. Mark runtime as READY only after direct readback / source verification.
7. Preserve backup-only children as backup-only unless their runtime becomes independently verified.
8. Quarantine identity conflicts instead of guessing.

## Current migration state
- Registry normalization: VERIFIED
- Repo-native child inventory: CREATED
- Functional child payload migration: OPEN
- Backup-only class separation: VERIFIED
- Identity-conflict quarantine: ACTIVE
