# 666 Cyber Intro – Python App Start Backup

Dieses Paket bewahrt das vollständige verifizierte Cyber Intro v1.10 als eigenständiges Startmodul für eine Python-App.

Aktueller Ablauf:
- Phase 1 endet mit READY
- Phase 2 wird erst beim Übergang über `phase2-armed` gestartet
- SYSTEM ONLINE fadet/blinkt exakt 3-mal
- Dauer SYSTEM ONLINE: ca. 5,4 s
- danach 2,0 s sichtbar halten
- danach Event `lyvra:system-start`
- kein Redirect
- keine automatische Schleife
- Center-Emblem bleibt statisch/effektfrei

Einbau:
1. Den kompletten Ordner `intro/` in das Python-Projekt kopieren.
2. `intro/index.html` in einer eingebetteten WebView laden.
3. Nach `lyvra:system-start` zur eigentlichen App-Oberfläche wechseln.
4. Die eingefrorene Sicherung selbst nicht verändern; für Anpassungen immer eine Kopie verwenden.

Geeignet für:
- PySide6 / PyQt6 + QWebEngineView
- pywebview
- andere Python-GUI-Frameworks mit eingebetteter HTML/WebView
