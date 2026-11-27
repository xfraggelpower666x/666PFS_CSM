# 666 / LYVRA CYBER INTRO HUD TEMPLATE v1.7 — AUDITED FREEZE

Status: FROZEN SYSTEM BACKUP

## Sequence
1. Phase 1: CYBER BOOTING + optimized intro brand + progress.
2. Final progress step: READY.
3. Cyan/pink transition sweep.
4. Phase 2: cyber HUD with static centered LYVRA emblem.
5. The same LYVRA background remains active across both phases.

## Web performance
- intro-brand.png: 1400×591, transparent, optimized palette PNG.
- center-emblem.png: 880×1100, transparent, optimized palette PNG.
- intro-background.jpg: 1672×941, optimized JPEG quality 85.
- all three visuals are preloaded from index.html.
- intrinsic width/height are set on PNGs to reduce layout shift.

## Safety / integration
- no redirect
- no meta refresh
- no fixed target URL
- no window.location.replace()
- center emblem has no beat reaction, filter, animation, glow, scale or glitch
- automatic demo beat pulse is disabled by default
- existing public `window.pulseCyberHudLogo()` API remains available for host-player integration

## Assets
assets/images/intro-background.jpg
assets/images/intro-brand.png
assets/images/center-emblem.png


## v1.8 – Phase 2 SYSTEM ONLINE sequence

- SYSTEM ONLINE sits centered below the Phase 2 center emblem.
- It fades/blinks exactly 3 times.
- The sequence is one-shot; there is no automatic loop or restart.
- After the third blink, `lyvra:system-start` is dispatched.
- Optional host hook: define `window.startProjectSystem()` to start the real project immediately after the intro.
- The center emblem remains static and effect-free.


## v1.9 – verlangsamte Phase 2 / finaler SYSTEM ONLINE Hold

- Phase-2-HUD baut sich langsamer auf.
- `SYSTEM ONLINE` blinkt/fadet genau 3-mal über ca. 5,4 Sekunden.
- Nach dem dritten Fade bleibt `SYSTEM ONLINE` sichtbar.
- Sichtbarer Endzustand wird weitere 2 Sekunden gehalten.
- Erst danach wird `lyvra:system-start` ausgelöst.
- Keine automatische Wiederholung / keine Schleife.


## v1.10 – Audit/Repair Freeze

Critical timing repair: Phase-2 animations are now armed only when the transition into Phase 2 begins.
This prevents the one-shot HUD animation from completing invisibly during Phase 1.

Final sequence:
1. Phase 1 reaches READY.
2. Phase-2 transition begins and arms the HUD animations.
3. Phase 2 builds in slowly.
4. SYSTEM ONLINE fades/blinks exactly 3 times over ~5.4 s.
5. SYSTEM ONLINE remains visible for 2 s.
6. `lyvra:system-start` is dispatched and the host project may start.
