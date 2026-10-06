# CYBERINTRO-38001 Rehydration

1. Read SYSTEM_IDENTITY.md.
2. Read SOURCE_MANIFEST.md.
3. Read DASHBOARD_CARD.md.
4. Treat the latest verified Systemsicherung as the current source authority.
5. Older backups are history/recovery/provenance only and must not downgrade the current source authority.
6. Resolve runtime payload only when CYBERINTRO-38001 is explicitly selected.
7. Do not autoload into 666STREAM, WEBLYVRA, LYVRA, or another child.
8. Keep Phase 1 and Phase 2 logically separate.
9. Preserve Phase-1 background through the transition into Phase 2.
10. Phase 1 must terminate visibly with READY.
11. In Phase 2, keep the center emblem static/effect-free.
12. SYSTEM ONLINE must appear below the center emblem.
13. SYSTEM ONLINE fades/blinks exactly 3 times over ~5.4 seconds.
14. After the third fade, SYSTEM ONLINE remains visible for 2 seconds.
15. Only after that hold may the host system start via lyvra:system-start or optional window.startProjectSystem().
16. No automatic Phase-2 loop/restart may be introduced.
17. No automatic redirect may be introduced without explicit user instruction.
18. Missing repository binary readback keeps runtime promotion pending; it does not restore an older backup as authority.

LATEST_VERIFIED_SYSTEMSICHERUNG_WINS=TRUE
OLDER_BACKUPS=HISTORY_RECOVERY_PROVENANCE
NO_DOWNGRADE=TRUE
CHILD_AUTOLOAD=FORBIDDEN
CROSS_SYSTEM_MERGE=FORBIDDEN

FOUND != VERIFIED
SEARCH_RESULT != READBACK
READ != REHYDRATED
