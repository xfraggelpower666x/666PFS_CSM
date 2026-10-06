# CYBERINTROHQ-39001 Rehydration

1. Read SYSTEM_IDENTITY.md.
2. Read SOURCE_MANIFEST.md.
3. Read DASHBOARD_CARD.md.
4. Resolve runtime only when CYBERINTROHQ-39001 is explicitly selected.
5. Treat CYBERINTROHQ-39001 as a separate child and separate version line from CYBERINTRO-38001.
6. Do not merge, downgrade, upgrade, or compare versions across those two children.
7. Preserve transparent PNG assets and the Clean-Eyes replacement.
8. Keep Phase 1 and Phase 2 logically separate.
9. Phase 1 terminates visibly with READY.
10. No automatic redirect.
11. Missing repository binary payload produces PARTIAL / READBACK_PENDING rather than invented verification.

FOUND != VERIFIED
SEARCH_RESULT != READBACK
READ != REHYDRATED
NEWER_VALID_EVOLUTION_APPLIES_WITHIN_NATIVE_LINEAGE_ONLY=TRUE
