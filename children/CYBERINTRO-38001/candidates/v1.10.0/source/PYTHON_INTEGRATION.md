# Python Integration

## Empfohlene Projektstruktur

```text
your_python_app/
├── main.py
├── app/
│   └── ...
└── assets/
    └── startup_intro/
        ├── index.html
        ├── assets/
        ├── docs/
        └── FREEZE_MANIFEST.json
```

Kopiere den kompletten Ordner `intro/` aus dieser Sicherung nach:

`assets/startup_intro/`

Wichtig: `index.html` und der zugehörige `assets/`-Ordner müssen zusammenbleiben.

## Start-Handoff

Das Intro löst nach vollständigem Ablauf dieses JavaScript-Ereignis aus:

```javascript
window.dispatchEvent(new CustomEvent('lyvra:system-start', {
  detail: { root }
}));
```

Die Python-App sollte dieses Ereignis über die WebView-Bridge abfangen und danach auf die eigentliche App-Oberfläche wechseln.

## Zeit-Fallback

Nur falls noch keine Event-Bridge eingebaut ist:

- Phase 1: 4,2 s
- Transition: 1,1 s
- SYSTEM ONLINE: 5,4 s
- finaler sichtbarer Hold: 2,0 s

Gesamt: ca. 12,7 s.

Event-basiert ist besser als ein fixer Timer.

## Source Authority

Originale eingefrorene Systemsicherung:

`666_CYBER_INTRO_HUD_TEMPLATE_v1_10_AUDIT_REPAIR_FREEZE_SYSTEMSICHERUNG.zip`

SHA-256:

`3ec3326bcf514dd7783c9099b47c21360d59afb62b717cf60c3466cd462abc6f`
