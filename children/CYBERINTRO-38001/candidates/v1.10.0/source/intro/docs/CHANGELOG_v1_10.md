# CHANGELOG v1.10

- Fixed hidden Phase-2 animation pre-run bug.
- Added explicit `phase2-armed` gate.
- Phase-2 animations now start at transition start, not at document load.
- Corrected SYSTEM ONLINE inline documentation.
- Added deterministic HUD reset handling.
- Added tracked/clearable failsafe timer.
- Added `defer` to both JavaScript includes.
- Preserved v1.9 timing:
  - Phase-2 entrance ~4.6–5.2 s
  - SYSTEM ONLINE triple fade 5.4 s
  - final visible hold 2.0 s
- Preserved static center emblem and no redirect.
