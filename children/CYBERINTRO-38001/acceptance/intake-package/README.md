# CYBERINTRO-38001 – isolierter Source Intake v1.10.0

Keine produktive Freigabe. Alle 20 Dateien des Python-Start-Backups sind unverändert unter `children/CYBERINTRO-38001/candidates/v1.10.0/source/` entpackt. Das Originalarchiv liegt zusätzlich unter `recovery/original/`. Keine HQ-Dateien. Bestehende native Registry-Dateien werden nicht ersetzt.

## Prüfung
14/14 nicht selbstreferenzielle Freeze-Dateien stimmen nach Größe und SHA-256 überein. Die Selbstreferenz des Freeze-Manifests ist veraltet; der zusätzliche Freeze-Receipt ist nicht gelistet. Beide bleiben unverändert. Drei Bilder sind vollständig dekodierbar. Lokale HTML/CSS-Referenzen existieren. Beide JS-Dateien bestehen `node --check`; Python besteht die Syntaxkompilierung. WebRadio: vier direkt gelesene Base64-Fragmente, 15.803 dekodierte Bytes, neun zentrale ZIP-Einträge stimmen nach CRC32 und Größe überein. Keine kryptografische Remote-Dateiparität behauptet.

## Python-Integration
Das Originalbeispiel lädt `intro/index.html` in QWebEngineView und wechselt nach 12.700 ms zur Beispieloberfläche. PySide6 ist in der Prüfumgebung nicht installiert. QWebChannel ist nur empfohlen, nicht implementiert. Der Timer beginnt beim Laden, nicht beim bestätigten Abschluss; Ladezeiten, verzögerte Frames und der 250-ms-Failsafe können zu vorzeitigem Wechsel führen. Das JavaScript dispatcht das Start-Ereignis sowohl am Root (bubbling) als auch am Window; Host-Listener sollten idempotent sein. Manuelles Reset/Replay ist nicht abgenommen (once-Listener). Keine Reparaturen in diesem Intake.

## Grenzen
Das historische v1.10-Original-ZIP (797.163 Bytes) fehlt weiterhin. Dieses neue Paket ist kein Ersatz für dessen exakten Archivhash. Kein Browser-/Qt-Laufzeittest, kein Repository-Write, keine Promotion. Details im INTAKE_RECEIPT.json.
