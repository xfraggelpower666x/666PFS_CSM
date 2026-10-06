# CYBERINTRO-38001 Rehydration

1. Read SYSTEM_IDENTITY.md.
2. Read SOURCE_MANIFEST.md.
3. Read DASHBOARD_CARD.md.
4. Resolve runtime payload only when CYBERINTRO-38001 is explicitly selected.
5. Do not autoload into 666STREAM, WEBLYVRA, LYVRA, or another child.
6. Keep Phase 1 and Phase 2 logically separate.
7. Preserve Phase-1 background through the transition into Phase 2.
8. Phase 1 must terminate visibly with READY.
9. No automatic redirect may be introduced without explicit user instruction.
10. Missing binary assets produce PARTIAL / HOLD; never silently replace them.

FOUND != VERIFIED
SEARCH_RESULT != READBACK
READ != REHYDRATED
