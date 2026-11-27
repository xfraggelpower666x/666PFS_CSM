"""
Beispiel: Cyber Intro als Startscreen einer PySide6-App.

Benötigt:
    pip install PySide6 PySide6-Addons

Das Beispiel verwendet einen Timer-Fallback.
Für die endgültige App sollte `lyvra:system-start`
per QWebChannel an Python weitergegeben werden.
"""

from pathlib import Path
import sys

from PySide6.QtCore import QTimer, QUrl
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtWebEngineWidgets import QWebEngineView

INTRO_FALLBACK_MS = 12700


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python App")

        intro_html = Path(__file__).resolve().parent / "intro" / "index.html"

        self.web = QWebEngineView()
        self.web.load(QUrl.fromLocalFile(str(intro_html)))
        self.setCentralWidget(self.web)

        QTimer.singleShot(INTRO_FALLBACK_MS, self.start_real_app)

    def start_real_app(self):
        label = QLabel("HIER STARTET DIE EIGENTLICHE PYTHON APP")
        label.setStyleSheet("font-size: 28px; padding: 40px;")
        self.setCentralWidget(label)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.resize(1280, 720)
    win.show()
    sys.exit(app.exec())
