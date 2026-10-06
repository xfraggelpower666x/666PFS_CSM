# CYBERINTRO-38001 Rehydration

1. Read SYSTEM_IDENTITY.md.
2. Read SOURCE_MANIFEST.md.
3. Read DASHBOARD_CARD.md.
4. Resolve runtime payload only when CYBERINTRO-38001 is explicitly selected.
5. Do not autoload into 666STREAM, WEBLYVRA, LYVRA, or another child.
6. Keep Phase 1 and Phase 2 logically separate.
7. Preserve Phase-1 background through the transition into Phase 2.
8. Phase 1 must terminate visibly with READY.
9. In Phase 2, keep the center emblem static/effect-free.
10. SYSTEM ONLINE must appear below the center emblem.
11. SYSTEM ONLINE fades/blinks exactly 3 times over ~5.4 seconds.
12. After the third fade, SYSTEM ONLINE remains visible for 2 seconds.
13. Only after that hold may the host system start via lyvra:system-start or optional window.startProjectSystem().
14. No automatic Phase-2 loop/restart may be introduced.
15. No automatic redirect may be introduced without explicit user instruction.
16. Missing repo binary payload produces PARTIAL / HOLD; never silently replace it.

FOUND != VERIFIED
SEARCH_RESULT != READBACK
READ != REHYDRATED
