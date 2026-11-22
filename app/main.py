#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C++ Trainer — Lern-App (PyQt6).

GUI-Hülle für das trainer-Skript: Aufgabenbaum, Editor, Kompilieren/
Testen/Starten, Konsole, Aufgaben-Spalte, Cheatsheet-Fenster und ein
interaktiver OpenCode-Agent. Alle Aktionen laufen über ./trainer.
"""

import glob
import html
import json
import os
import re
import shlex
import subprocess
import sys
import shutil
import traceback

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEKTIONEN_DIR = os.path.join(ROOT, "lektionen")
TRAINER = os.path.join(ROOT, "trainer")
PROGRESS_FILE = os.path.join(ROOT, "fortschritt.json")

# opencode auch ohne Shell-Profil finden (z. B. bei Start per Desktop-Icon):
# ~/.opencode/bin vor den PATH stellen.
_opencode_bin = os.path.join(os.path.expanduser("~"), ".opencode", "bin")
if os.path.isdir(_opencode_bin):
    os.environ["PATH"] = _opencode_bin + os.pathsep + os.environ.get("PATH", "")
OPENCODE = shutil.which("opencode") or "opencode"

# ---------------------------------------------------------------- Markdown

try:
    import markdown

    _MD_EXT = ["fenced_code", "tables"]
    _MD_CFG_BASIS = {}
    try:
        import pygments  # noqa: F401
        _MD_EXT.append("codehilite")
        _MD_CFG_BASIS = {"guess_lang": False}
    except ImportError:
        pass

    def _md_cfg(mit_nl2br=False):
        cfg = dict(_MD_CFG_BASIS)
        if "codehilite" in _MD_EXT:
            cfg["codehilite"] = {"noclasses": True,
                                 "pygments_style": SCHEME["pygments"],
                                 "guess_lang": False}
        ext = _MD_EXT + ["nl2br"] if mit_nl2br else _MD_EXT
        return ext, cfg

    def md_html(text):
        """Klassisches Markdown (Aufgabe/Cheatsheet): Absätze über Leerzeilen."""
        ext, cfg = _md_cfg()
        return markdown.markdown(text, extensions=ext, extension_configs=cfg)

    def md_chat_html(text):
        """Chat-Variante: einzelne Zeilenumbrüche bleiben sichtbar (nl2br)."""
        ext, cfg = _md_cfg(mit_nl2br=True)
        return markdown.markdown(text, extensions=ext, extension_configs=cfg)
except ImportError:
    def md_html(text):
        return "<pre style=\"font-family:monospace\">" + html.escape(text) + "</pre>"

    def md_chat_html(text):
        return md_html(text)


def fail(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)


try:
    from PyQt6.QtCore import (QEvent, QPoint, QRect, Qt, QTimer, QProcess,
                              QRegularExpression, QSettings)
    from PyQt6.QtGui import (QBrush, QColor, QFont, QGuiApplication, QIcon,
                             QPalette, QSyntaxHighlighter, QTextCharFormat)
    from PyQt6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
                                 QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
                                 QPushButton, QSpinBox, QSplitter, QTabWidget,
                                 QTextBrowser, QTreeWidget, QTreeWidgetItem,
                                 QVBoxLayout, QWidget)
except ImportError:
    fail("PyQt6 ist nicht installiert.\n"
         "Bitte die App über ./start.sh starten (richtet alles ein).")


ANSI_RE = re.compile(r"\x1b\[[0-9;]*[A-Za-z]|\x1b\][^\x07]*(?:\x07|\x1b\\)")


def _gui_excepthook(etype, value, tb):
    """Fehler in Qt-Slots loggen, statt die App abzustürzen."""
    traceback.print_exception(etype, value, tb)


sys.excepthook = _gui_excepthook


# Farben ans System-Theme angepasst (hell/dunkel) — in main() gesetzt.
SCHEME = {
    "text": "#333333", "agent_text": "#0f4c5c", "user": "#1a4d8f",
    "system": "#666666", "header": "#666666", "error": "#c62828",
    "warn": "#b26a00", "success": "#2e7d32", "pygments": "friendly",
    "hl_keyword": "#0033b3", "hl_type": "#7d3fa3", "hl_string": "#a31515",
    "hl_number": "#098658", "hl_comment": "#6a9955", "hl_preproc": "#7d5d00",
}


def farbschema():
    app = QApplication.instance()
    if app is None:
        return SCHEME
    hell = app.palette().color(QPalette.ColorRole.Window).lightness() > 127
    if hell:
        SCHEME.update({
            "text": "#333333", "agent_text": "#0f4c5c", "user": "#1a4d8f",
            "system": "#666666", "header": "#666666", "error": "#c62828",
            "warn": "#b26a00", "success": "#2e7d32", "pygments": "friendly",
            "hl_keyword": "#0033b3", "hl_type": "#7d3fa3",
            "hl_string": "#a31515", "hl_number": "#098658",
            "hl_comment": "#6a9955", "hl_preproc": "#7d5d00",
        })
    else:
        SCHEME.update({
            "text": "#e8eaed", "agent_text": "#c9e3f5", "user": "#8ab4f8",
            "system": "#9aa0a6", "header": "#9aa0a6", "error": "#ff8a80",
            "warn": "#ffb74d", "success": "#81c784", "pygments": "monokai",
            "hl_keyword": "#569cd6", "hl_type": "#4ec9b0",
            "hl_string": "#ce9178", "hl_number": "#b5cea8",
            "hl_comment": "#6a9955", "hl_preproc": "#c586c0",
        })
    return SCHEME



def strip_ansi(text):
    """Farb-/Steuer-Codes aus Terminal-Ausgaben entfernen."""
    return ANSI_RE.sub("", text)


def auth_json_path():
    data_dir = os.environ.get("XDG_DATA_HOME",
                              os.path.expanduser("~/.local/share"))
    return os.path.join(data_dir, "opencode", "auth.json")


def saved_providers():
    """Anbieter mit gespeichertem API-Key (aus opencode auth login)."""
    try:
        with open(auth_json_path(), encoding="utf-8") as f:
            data = json.load(f)
        return {k for k, v in data.items()
                if isinstance(v, dict) and v.get("key")}
    except (OSError, ValueError):
        return set()


def monospace(size=10):
    f = QFont("Monospace")
    f.setStyleHint(QFont.StyleHint.TypeWriter)
    f.setFixedPitch(True)
    f.setPointSize(size)
    return f


def lesson_title(lesson_dir):
    """Titel aus der ersten README-Zeile, sonst Ordnername."""
    readme = os.path.join(lesson_dir, "README.md")
    try:
        with open(readme, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("# "):
                    return line[2:].strip()
    except OSError:
        pass
    return os.path.basename(lesson_dir)


def console_color(line):
    if "error:" in line or "FEHLGESCHLAGEN" in line or "✘" in line:
        return SCHEME["error"]
    if "warning:" in line:
        return SCHEME["warn"]
    if "✔" in line or "BESTANDEN" in line:
        return SCHEME["success"]
    return None


# --------------------------------------------------------- Syntax-Highlight

class CppHighlighter(QSyntaxHighlighter):
    KEYWORDS = (
        "if|else|for|while|do|return|break|continue|switch|case|default|"
        "new|delete|this|nullptr|true|false|operator"
    )
    TYPES = (
        "void|int|char|bool|float|double|long|short|unsigned|signed|auto|"
        "size_t|struct|class|enum|union|public|private|protected|const|"
        "constexpr|static|namespace|using|template|typename|typedef"
    )

    def __init__(self, document):
        super().__init__(document)
        def fmt(color, bold=False, italic=False):
            f = QTextCharFormat()
            f.setForeground(QColor(color))
            if bold:
                f.setFontWeight(QFont.Weight.Bold)
            if italic:
                f.setFontItalic(True)
            return f

        self.rules = [
            (QRegularExpression(r"^\s*#[^\n]*"), fmt(SCHEME["hl_preproc"])),
            (QRegularExpression(r"\b(?:%s)\b" % self.KEYWORDS),
             fmt(SCHEME["hl_keyword"], bold=True)),
            (QRegularExpression(r"\b(?:%s)\b" % self.TYPES), fmt(SCHEME["hl_type"])),
            (QRegularExpression(r'"(?:[^"\\]|\\.)*"'), fmt(SCHEME["hl_string"])),
            (QRegularExpression(r"'(?:[^'\\]|\\.)*'"), fmt(SCHEME["hl_string"])),
            (QRegularExpression(r"\b\d+(?:\.\d+)?f?\b"), fmt(SCHEME["hl_number"])),
            (QRegularExpression(r"//[^\n]*"), fmt(SCHEME["hl_comment"], italic=True)),
        ]
        self.comment_fmt = fmt(SCHEME["hl_comment"], italic=True)
        self.re_start = QRegularExpression(r"/\*")
        self.re_end = QRegularExpression(r"\*/")

    def highlightBlock(self, text):
        for pattern, fmt in self.rules:
            m = pattern.globalMatch(text)
            while m.hasNext():
                mm = m.next()
                self.setFormat(mm.capturedStart(), mm.capturedLength(), fmt)
        # mehrzeilige /* … */-Kommentare
        self.setCurrentBlockState(0)
        if self.previousBlockState() != 1:
            m = self.re_start.match(text)
            start = m.capturedStart() if m.hasMatch() else -1
        else:
            start = 0
        while start >= 0:
            m = self.re_end.match(text, start)
            if m.hasMatch():
                end = m.capturedEnd()
                self.setFormat(start, end - start, self.comment_fmt)
                nm = self.re_start.match(text, end)
                start = nm.capturedStart() if nm.hasMatch() else -1
            else:
                self.setFormat(start, len(text) - start, self.comment_fmt)
                self.setCurrentBlockState(1)
                start = -1


# ------------------------------------------------------------- Editor

class CodeEditor(QPlainTextEdit):
    """Editor mit Auto-Einrückung: Bei Enter bekommt die neue Zeile die
    Einrückung der vorherigen Zeile — endet diese mit {, eine Stufe extra."""

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            cursor = self.textCursor()
            zeile = cursor.block().text()
            einrueck = re.match(r"[ \t]*", zeile).group(0)
            extra = "    " if zeile.rstrip().endswith("{") else ""
            cursor.insertText("\n" + einrueck + extra)
            self.ensureCursorVisible()
            return
        super().keyPressEvent(event)


# ------------------------------------------------------------- Konsole

class Console(QPlainTextEdit):
    """Zeilenweise gepufferte, gefärbte Ausgabe."""

    def __init__(self):
        super().__init__()
        self.setReadOnly(True)
        self.setFont(monospace())
        self.setMaximumBlockCount(5000)
        self._buf = ""

    def clear_output(self):
        self.clear()
        self._buf = ""

    def write(self, text):
        self._buf += text
        while "\n" in self._buf:
            line, self._buf = self._buf.split("\n", 1)
            self._line(line)

    def write_line(self, text, color=None):
        """Sofortige eigene Zeile (z. B. für Überschriften)."""
        self._buf = ""
        self._line(text, color)

    def flush(self):
        if self._buf:
            self._line(self._buf)
            self._buf = ""

    def _line(self, line, color=None):
        color = color or console_color(line)
        esc = html.escape(line) if line else " "
        if color:
            self.appendHtml(f'<span style="color:{color}">{esc}</span>')
        else:
            self.appendPlainText(line)
        self.verticalScrollBar().setValue(self.verticalScrollBar().maximum())


# ------------------------------------------------------------- Chat-Ansicht

class Chat(QTextBrowser):
    """Chat-Ansicht: Einträge als Liste; die Agent-Antwort wird während
    des Laufens live gezeigt und am Ende als Markdown (mit Code-Highlighting)
    gerendert — ohne "Agent:"-Präfix pro Zeile."""

    def __init__(self):
        super().__init__()
        self.setFont(monospace())
        self.setOpenExternalLinks(False)
        self._entries = []

    def clear_chat(self):
        self._entries = [("system", "Verlauf gelöscht.")]
        self._render()

    def add_system(self, text):
        self._entries.append(("system", text))
        self._render()

    def add_error(self, text):
        self._entries.append(("error", text))
        self._render()

    def add_user(self, text):
        self._entries.append(("user", text))
        self._render()

    def begin_agent(self):
        self._entries.append(("agent_live", ""))
        self._render()

    def update_agent(self, text):
        for i in range(len(self._entries) - 1, -1, -1):
            if self._entries[i][0] in ("agent_live", "agent"):
                self._entries[i] = ("agent_live", text)
                break
        self._render()

    def finish_agent(self, text):
        for i in range(len(self._entries) - 1, -1, -1):
            if self._entries[i][0] in ("agent_live", "agent"):
                self._entries[i] = ("agent", text)
                break
        self._render()

    def _render(self):
        parts = []
        for kind, text in self._entries:
            if kind == "user":
                esc = html.escape(text).replace("\n", "<br>")
                parts.append(f'<div style="color:{SCHEME["user"]};'
                             f'margin:10px 0 2px 0"><b>Du:</b> {esc}</div>')
            elif kind == "agent_live":
                parts.append(f'<div style="color:{SCHEME["agent_text"]};'
                             f'margin:6px 0;white-space:pre-wrap">'
                             f'{html.escape(text)}</div>')
            elif kind == "agent":
                parts.append(f'<div style="color:{SCHEME["header"]};'
                             f'margin:10px 0 2px 0">🤖 Agent</div>')
                parts.append(f'<div style="color:{SCHEME["agent_text"]};'
                             f'margin:0 0 14px 0">{md_chat_html(text)}</div>')
            elif kind == "system":
                parts.append(f'<div style="color:{SCHEME["system"]};margin:2px 0">'
                             f'{html.escape(text)}</div>')
            elif kind == "error":
                parts.append(f'<div style="color:{SCHEME["error"]};margin:2px 0">'
                             f'{html.escape(text)}</div>')
        self.setHtml("".join(parts))
        sb = self.verticalScrollBar()
        sb.setValue(sb.maximum())


# ------------------------------------------------------------- Konfiguration

class ConfigDialog(QDialog):
    """Zeigt den Agent-Status und wählt das Modell.

    API-Keys/Anbieter konfiguriert man mit opencode-Bordmitteln
    (`opencode auth login`) — die App nutzt sie automatisch.
    """

    def __init__(self, parent, settings, current_model):
        super().__init__(parent)
        self.setWindowTitle("Agent-Konfiguration")
        self.settings = settings
        self.resize(640, 470)
        self.result_model = current_model

        v = QVBoxLayout(self)

        v.addWidget(QLabel("OpenCode-Version:"))
        self.version_label = QLabel("wird gelesen …")
        v.addWidget(self.version_label)

        v.addWidget(QLabel("Anbieter mit gespeichertem API-Key:"))
        providers = sorted(saved_providers())
        self.provider_label = QLabel(", ".join(providers) if providers
                                     else "keine — siehe Hinweis unten")
        v.addWidget(self.provider_label)

        v.addWidget(QLabel("Modell für den Agent-Tab (anbieter/modell):"))
        self.model = QComboBox()
        self.model.setEditable(True)
        self.model.setCurrentText(current_model)
        v.addWidget(self.model)
        self.models_status = QLabel("Modelle werden geladen …")
        v.addWidget(self.models_status)

        v.addWidget(QLabel("Pre-Prompt — Vorgabe für jede Agent-Antwort:"))
        self.preprompt_edit = QPlainTextEdit()
        self.preprompt_edit.setPlaceholderText(
            "z. B. „Halte dich sehr kurz.“ oder „Antworte auf Deutsch und "
            "nur mit Hinweisen.“")
        self.preprompt_edit.setPlainText(self.settings.value("preprompt", ""))
        self.preprompt_edit.setFixedHeight(
            int(3.4 * self.preprompt_edit.fontMetrics().height()))
        v.addWidget(self.preprompt_edit)

        self.status = QLabel("")
        self.status.setWordWrap(True)
        v.addWidget(self.status)

        self._test_proc = None
        self._test_cancelled = False
        self._test_seconds = 0
        self._test_timer = QTimer(self)
        self._test_timer.setInterval(1000)
        self._test_timer.timeout.connect(self._test_tick)

        row = QHBoxLayout()
        self.b_test = QPushButton("Verbindung testen")
        self.b_test.clicked.connect(self.test_connection)
        b_save = QPushButton("Übernehmen")
        b_save.clicked.connect(self.accept)
        b_cancel = QPushButton("Abbrechen")
        b_cancel.clicked.connect(self.reject)
        row.addWidget(self.b_test)
        row.addStretch(1)
        row.addWidget(b_save)
        row.addWidget(b_cancel)
        v.addLayout(row)

        hint = QLabel(
            "Hinweis: API-Keys und Anbieter konfigurierst du im Terminal mit\n"
            "`opencode auth login` — die App nutzt automatisch die dort\n"
            "gespeicherten Schlüssel. Modell-Liste kommt von `opencode models`.")
        hint.setWordWrap(True)
        hint.setStyleSheet("")
        v.addWidget(hint)

        self.fetch_models()
        self.fetch_version()

    def fetch_models(self):
        self._models_proc = QProcess(self)
        self._models_proc.setWorkingDirectory(ROOT)
        self._models_proc.finished.connect(self._models_done)
        self._models_proc.errorOccurred.connect(self._models_error)
        self._models_proc.start(OPENCODE, ["models"])
        QTimer.singleShot(60000, self._models_timeout)

    def _models_free(self):
        """Prozess freigeben — True, wenn dieser Handler zuständig war."""
        proc = getattr(self, "_models_proc", None)
        if proc is None:
            return False
        proc.kill()
        self._models_proc = None
        return True

    def _models_timeout(self):
        if self._models_free():
            self.models_status.setText(
                "Timeout — läuft `opencode models` im Projektordner im Terminal? "
                "(Beim ersten Start lädt opencode die Modell-Liste aus dem Netz.)")

    def _models_error(self, err):
        if err != QProcess.ProcessError.FailedToStart:
            return   # Absturz/Timeout behandelt _models_done
        if self._models_free():
            self.models_status.setText(
                "opencode konnte nicht gestartet werden — "
                "./install.sh ausführen oder `opencode` einmal im Terminal starten.")

    def _models_done(self, code, _status):
        proc = self._models_proc
        self._models_proc = None
        if proc is None:
            return
        if code != 0:
            self.models_status.setText("`opencode models` fehlgeschlagen — "
                                       "Modell bitte von Hand eintippen.")
            return
        data = bytes(proc.readAllStandardOutput()).decode("utf-8", "replace")
        models = sorted(line.strip() for line in data.splitlines()
                        if "/" in line.strip())
        current = self.model.currentText()
        self.model.clear()
        self.model.addItems(models)
        self.model.setCurrentText(current)
        self.models_status.setText(f"{len(models)} Modelle gefunden.")

    def fetch_version(self):
        self._version_proc = QProcess(self)
        self._version_proc.finished.connect(self._version_done)
        self._version_proc.errorOccurred.connect(self._version_error)
        self._version_proc.start(OPENCODE, ["--version"])
        QTimer.singleShot(15000, self._version_timeout)

    def _version_free(self):
        proc = getattr(self, "_version_proc", None)
        if proc is None:
            return False
        proc.kill()
        self._version_proc = None
        return True

    def _version_timeout(self):
        if self._version_free():
            self.version_label.setText("Timeout — läuft `opencode --version` im Terminal?")

    def _version_error(self, err):
        if err != QProcess.ProcessError.FailedToStart:
            return
        if self._version_free():
            self.version_label.setText("opencode nicht gefunden — ./install.sh ausführen.")

    def _version_done(self, code, _status):
        proc = self._version_proc
        self._version_proc = None
        if proc is None:
            return
        data = bytes(proc.readAllStandardOutput()).decode("utf-8", "replace").strip()
        self.version_label.setText(data if data else "opencode nicht gefunden!")

    def test_connection(self):
        if self._test_proc is not None:      # läuft schon → abbrechen
            self._test_cancelled = True
            self._test_proc.kill()
            return
        model = self.model.currentText().strip()
        if not model:
            self.status.setText("erst ein Modell wählen.")
            return
        self._test_cancelled = False
        self._test_seconds = 0
        self.status.setText("Test läuft … (Denk-Modelle können länger brauchen)")
        self.b_test.setText("Abbrechen")
        self._test_proc = QProcess(self)
        self._test_proc.setWorkingDirectory(ROOT)
        self._test_proc.finished.connect(self._test_done)
        self._test_proc.errorOccurred.connect(self._test_error)
        self._test_proc.start(OPENCODE, ["run", "--standalone", "-m", model,
                                           "-s", "ses_trainer_config_test",
                                           "--auto", "Antworte mit genau: OK"])
        self._test_proc.closeWriteChannel()   # stdin schließen — sonst wartet opencode
        self._test_timer.start()

    def _test_error(self, err):
        if err != QProcess.ProcessError.FailedToStart:
            return
        self._test_timer.stop()
        self.b_test.setText("Verbindung testen")
        self.status.setText("opencode konnte nicht gestartet werden - "
                            "./install.sh ausfuehren.")
        self._test_proc = None

    def _test_tick(self):
        self._test_seconds += 1
        self.status.setText(f"Test läuft … {self._test_seconds} s "
                            "(Denk-Modelle können länger brauchen)")

    def _test_done(self, code, _status):
        self._test_timer.stop()
        self.b_test.setText("Verbindung testen")
        proc = self._test_proc
        self._test_proc = None
        if proc is None:
            return
        data = bytes(proc.readAllStandardOutput()).decode("utf-8", "replace")
        err = bytes(proc.readAllStandardError()).decode("utf-8", "replace")
        text = strip_ansi(data + err).strip()
        self._test_proc = None
        if self._test_cancelled:
            self.status.setText("Test abgebrochen.")
        elif code == 0 and "OK" in text:
            self.status.setText(f"✓ Verbindung ok ({self._test_seconds} s).")
        else:
            tail = text[-200:] if text else f"Exit-Code {code}"
            self.status.setText("✘ fehlgeschlagen: " + tail)

    def done(self, result):
        if self._test_proc is not None:
            self._test_proc.kill()
        super().done(result)


# ------------------------------------------------------------- Schriftgrößen

class ZoomDialog(QDialog):
    """Schriftgröße je Fensterbereich — ändert sich live."""

    BEREICHE = [("baum", "Aufgabenbaum"), ("editor", "Editor"),
                ("konsole", "Konsole"), ("agent", "Agent-Chat"),
                ("aufgabe", "Aufgabe / Cheatsheet")]

    def __init__(self, parent, hauptfenster):
        super().__init__(parent)
        self.setWindowTitle("Schriftgrößen")
        self.hauptfenster = hauptfenster
        self.resize(420, 260)
        v = QVBoxLayout(self)
        v.addWidget(QLabel("Schriftgröße je Fensterbereich (Punkte):"))
        self.spins = {}
        for key, label in self.BEREICHE:
            zeile = QHBoxLayout()
            zeile.addWidget(QLabel(label + ":"))
            spin = QSpinBox()
            spin.setRange(7, 24)
            spin.setValue(int(hauptfenster.sizes[key]))
            spin.valueChanged.connect(
                lambda wert, k=key: hauptfenster.set_size(k, wert))
            zeile.addWidget(spin)
            self.spins[key] = spin
            v.addLayout(zeile)
        v.addWidget(QLabel(
            "Die Größe wird sofort angewendet und gespeichert."))
        row = QHBoxLayout()
        b_reset = QPushButton("Zurücksetzen (10)")
        b_reset.clicked.connect(self.zurueck)
        row.addWidget(b_reset)
        row.addStretch(1)
        b_close = QPushButton("Schließen")
        b_close.clicked.connect(self.accept)
        row.addWidget(b_close)
        v.addLayout(row)

    def zurueck(self):
        for spin in self.spins.values():
            spin.setValue(10)


# ------------------------------------------------------------- Hauptfenster

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("C++ Trainer")
        self.resize(1420, 860)

        self.current_lesson = None      # z. B. "01-eingabe/02-summe"
        self.proc = None                # laufender trainer-Prozess
        self.agent_proc = None          # laufender Agent-Prozess
        self.last_output = ""           # letzte Ausgabe (für den Agenten)
        self.progress = self._load_progress()

        self.settings = QSettings("cpp-trainer", "trainer-app")
        self.sizes = self._load_sizes()

        central = QWidget()
        self.setCentralWidget(central)
        layout = QHBoxLayout(central)
        layout.setContentsMargins(6, 6, 6, 6)

        # --- Baum (links)
        self.tree = QTreeWidget()
        self.tree.setHeaderLabel("Aufgaben")
        self.tree.setFont(monospace(self.sizes["baum"]))
        self.tree.itemClicked.connect(self.tree_clicked)
        self.reload_tree()

        # --- Mitte: Taskleiste + Editor + Konsole/Agent
        center = QWidget()
        center_layout = QVBoxLayout(center)
        center_layout.setContentsMargins(0, 0, 0, 0)

        bar = QHBoxLayout()
        self.btn_build = QPushButton("🛠 Kompilieren")
        self.btn_test = QPushButton("🧪 Testen")
        self.btn_run = QPushButton("▶ Starten")
        self.btn_update = QPushButton("🔄 Updates")
        self.btn_update.setToolTip("Neue Aufgaben von GitHub holen (./trainer update)")
        for w in (self.btn_build, self.btn_test, self.btn_run):
            w.setEnabled(False)
        self.btn_build.clicked.connect(self.do_build)
        self.btn_test.clicked.connect(self.do_test)
        self.btn_run.clicked.connect(self.do_run)
        self.btn_update.clicked.connect(self.do_update)
        bar.addWidget(self.btn_build)
        bar.addWidget(self.btn_run)
        bar.addWidget(self.btn_test)
        bar.addWidget(self.btn_update)
        bar.addStretch(1)
        self.btn_zoom = QPushButton("Aa")
        self.btn_zoom.setToolTip("Schriftgrößen einstellen")
        self.btn_zoom.clicked.connect(self.open_zoom)
        bar.addWidget(self.btn_zoom)
        self.btn_cheat = QPushButton("❓ Cheatsheet")
        self.btn_cheat.setEnabled(False)
        self.btn_cheat.clicked.connect(self.open_cheatsheet)
        bar.addWidget(self.btn_cheat)
        center_layout.addLayout(bar)

        self.tabs = QTabWidget()
        self.tabs.setFont(monospace(self.sizes["editor"]))
        self.tabs.setDocumentMode(True)
        center_layout.addWidget(self.tabs, 1)

        self.bottom = QTabWidget()
        self.console = Console()
        self.console_input = QLineEdit()
        self.console_input.setPlaceholderText(
            "Eingabe an das laufende Programm … (Enter = senden)")
        self.console_input.setEnabled(False)
        self.console_input.returnPressed.connect(self.send_console_input)
        console_page = QWidget()
        cl = QVBoxLayout(console_page)
        cl.setContentsMargins(0, 0, 0, 0)
        cl.addWidget(self.console, 1)
        cl.addWidget(self.console_input)
        self.bottom.addTab(console_page, "Konsole")
        self.bottom.addTab(self.build_agent_panel(), "Agent")
        btn_clear_view = QPushButton("🧹")
        btn_clear_view.setFixedWidth(34)
        btn_clear_view.setToolTip("Sichtbare Ansicht leeren (Konsole oder Agent-Chat)")
        btn_clear_view.clicked.connect(self.clear_current_view)
        self.bottom.setCornerWidget(btn_clear_view, Qt.Corner.TopRightCorner)
        center_layout.addWidget(self.bottom, 1)

        self.split_vert = QSplitter(Qt.Orientation.Vertical)
        self.split_vert.addWidget(self.tabs)
        self.split_vert.addWidget(self.bottom)
        self.split_vert.setSizes([560, 280])
        center_layout.addWidget(self.split_vert, 1)

        # --- Aufgabe (rechts)
        self.task_title = QLabel("")
        self.task_title.setFont(monospace(self.sizes["aufgabe"]))
        self.task_title.setStyleSheet("font-weight:bold; padding:2px;")
        self.task_browser = QTextBrowser()
        task_widget = QWidget()
        task_layout = QVBoxLayout(task_widget)
        task_layout.setContentsMargins(0, 0, 0, 0)
        task_layout.addWidget(self.task_title)
        task_layout.addWidget(self.task_browser, 1)

        self.split_main = QSplitter(Qt.Orientation.Horizontal)
        self.split_main.addWidget(self.tree)
        self.split_main.addWidget(center)
        self.split_main.addWidget(task_widget)
        self.split_main.setSizes([300, 800, 330])
        layout.addWidget(self.split_main)

        self.cheat_windows = []
        self._fenster_wiederherstellen()
        self.apply_all_sizes()

    # ------------------------------------------------------------ Fenster

    def _fenster_wiederherstellen(self):
        """Gespeicherte Größe/Position/Splitter laden — mit Fallback, wenn
        der aktuelle Bildschirm zu klein für die gespeicherte Konfig ist."""
        geo = self.settings.value("win/geometry")
        if geo:
            self.restoreGeometry(geo)
        splitter = self.settings.value("win/splitter")
        if splitter:
            self.split_main.restoreState(splitter)
        vsplitter = self.settings.value("win/vsplitter")
        if vsplitter:
            self.split_vert.restoreState(vsplitter)
        self._an_bildschirm_anpassen()

    def _an_bildschirm_anpassen(self):
        screen = self.screen() or QGuiApplication.primaryScreen()
        avail = screen.availableGeometry()
        # Zu groß für den Bildschirm → auf die verfügbare Fläche verkleinern
        if self.width() > avail.width() or self.height() > avail.height():
            self.resize(min(self.width(), avail.width()),
                        min(self.height(), avail.height()))
        # Position außerhalb (z. B. zweiter Bildschirm weggefallen) → zurückholen
        if not avail.contains(self.frameGeometry().topLeft()):
            self.move(avail.topLeft())

    def _fenster_speichern(self):
        self.settings.setValue("win/geometry", self.saveGeometry())
        self.settings.setValue("win/splitter", self.split_main.saveState())
        self.settings.setValue("win/vsplitter", self.split_vert.saveState())
        self.settings.setValue("win/maximized", self.isMaximized())

    def closeEvent(self, event):
        self._fenster_speichern()
        super().closeEvent(event)

    # ------------------------------------------------------------ Baum

    # ------------------------------------------------------------ Baum

    def reload_tree(self):
        self.tree.clear()
        for thema in sorted(os.listdir(LEKTIONEN_DIR)):
            tdir = os.path.join(LEKTIONEN_DIR, thema)
            if not os.path.isdir(tdir):
                continue
            titem = QTreeWidgetItem([thema])
            tf = titem.font(0)
            tf.setBold(True)
            titem.setFont(0, tf)
            titem.setFlags(Qt.ItemFlag.ItemIsEnabled)   # Thema nicht wählbar
            self.tree.addTopLevelItem(titem)
            for lesson in sorted(os.listdir(tdir)):
                ldir = os.path.join(tdir, lesson)
                if not os.path.isdir(ldir):
                    continue
                rel = f"{thema}/{lesson}"
                item = QTreeWidgetItem([lesson_title(ldir)])
                item.setData(0, Qt.ItemDataRole.UserRole, rel)
                titem.addChild(item)
            titem.setExpanded(True)
        self._apply_progress()

    def tree_clicked(self, item, _column):
        rel = item.data(0, Qt.ItemDataRole.UserRole)
        if rel:
            self.load_lesson(rel)

    def load_lesson(self, rel):
        self.current_lesson = rel
        ldir = os.path.join(LEKTIONEN_DIR, rel)

        # Tabs: main.cpp zuerst, dann Rest
        files = sorted(glob.glob(os.path.join(ldir, "*.cpp"))) + \
                sorted(glob.glob(os.path.join(ldir, "*.h")))
        files.sort(key=lambda p: (os.path.basename(p) != "main.cpp", p))
        self.tabs.clear()
        for path in files:
            editor = CodeEditor()
            editor.setFont(monospace(self.sizes["editor"]))
            try:
                with open(path, encoding="utf-8") as f:
                    editor.setPlainText(f.read())
            except OSError as e:
                editor.setPlainText(f"(Datei konnte nicht gelesen werden: {e})")
            editor.setProperty("path", path)
            editor.hl = CppHighlighter(editor.document())
            editor.document().setDefaultFont(monospace())
            fm = editor.fontMetrics()
            editor.setTabStopDistance(fm.horizontalAdvance(" ") * 4)
            self.tabs.addTab(editor, os.path.basename(path))

        # Aufgabe
        try:
            with open(os.path.join(ldir, "README.md"), encoding="utf-8") as f:
                readme = f.read()
        except OSError:
            readme = "(keine README.md gefunden)"
        self.task_title.setText(rel)
        self.task_browser.setHtml(md_html(readme))

        self.btn_run.setEnabled(True)
        self.btn_build.setEnabled(True)
        self.btn_test.setEnabled(True)
        self.btn_cheat.setEnabled(True)
        self.console.write_line(f"== Lektion geladen: {rel} ==")

    # ------------------------------------------------------------ Dateien

    def clear_current_view(self):
        if self.bottom.currentIndex() == 0:
            self.console.clear_output()
        else:
            self.agent_chat.clear_chat()

    def save_all(self):
        for i in range(self.tabs.count()):
            editor = self.tabs.widget(i)
            path = editor.property("path")
            if path:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(editor.toPlainText())

    # ------------------------------------------------------------ Fortschritt

    def _load_progress(self):
        try:
            with open(PROGRESS_FILE, encoding="utf-8") as f:
                data = json.load(f)
            return set(data.get("solved", []))
        except (OSError, ValueError):
            return set()

    def _save_progress(self):
        try:
            with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
                json.dump({"solved": sorted(self.progress)}, f, indent=2)
        except OSError as e:
            self.console.write_line(
                f"Fortschritt konnte nicht gespeichert werden: {e}", color="#c62828")

    def _apply_progress(self):
        total = 0
        solved = 0
        for i in range(self.tree.topLevelItemCount()):
            titem = self.tree.topLevelItem(i)
            for j in range(titem.childCount()):
                litem = titem.child(j)
                rel = litem.data(0, Qt.ItemDataRole.UserRole)
                if not rel:
                    continue
                total += 1
                title = lesson_title(os.path.join(LEKTIONEN_DIR, rel))
                if rel in self.progress:
                    solved += 1
                    litem.setText(0, "✔ " + title)
                    litem.setForeground(0, QBrush(QColor(SCHEME["success"])))
                else:
                    litem.setText(0, title)
                    litem.setForeground(0, QBrush(QColor(SCHEME["text"])))
        self.tree.setHeaderLabels([f"Aufgaben — {solved}/{total} gelöst"])

    # ------------------------------------------------------------ Schriftgrößen

    def _load_sizes(self):
        standard = {"baum": 10, "editor": 10, "konsole": 10, "agent": 10,
                    "aufgabe": 10}
        sizes = {}
        for k, v in standard.items():
            sizes[k] = int(self.settings.value(f"sizes/{k}", v))
        return sizes

    def _save_sizes(self):
        try:
            for k, v in self.sizes.items():
                self.settings.setValue(f"sizes/{k}", v)
        except OSError as e:
            self.console.write_line(
                f"Schriftgrößen konnten nicht gespeichert werden: {e}", color="#c62828")

    def set_size(self, key, value):
        self.sizes[key] = int(value)
        self._save_sizes()
        self.apply_all_sizes()

    def apply_all_sizes(self):
        s = self.sizes
        self.tree.setFont(monospace(s["baum"]))
        self.tabs.setFont(monospace(s["editor"]))
        for i in range(self.tabs.count()):
            ed = self.tabs.widget(i)
            if ed is None:
                continue
            ed.setFont(monospace(s["editor"]))
            ed.document().setDefaultFont(monospace(s["editor"]))
            fm = ed.fontMetrics()
            ed.setTabStopDistance(fm.horizontalAdvance(" ") * 4)
        self.console.setFont(monospace(s["konsole"]))
        self.console_input.setFont(monospace(s["konsole"]))
        self.agent_chat.setFont(monospace(s["agent"]))
        self.agent_input.setFont(monospace(s["agent"]))
        self.agent_input.setFixedHeight(
            int(3.4 * self.agent_input.fontMetrics().height()))
        self.task_title.setFont(monospace(s["aufgabe"]))
        self.task_browser.setFont(monospace(s["aufgabe"]))
        for win in self.cheat_windows:
            for tb in win.findChildren(QTextBrowser):
                tb.setFont(monospace(s["aufgabe"]))

    def open_zoom(self):
        dlg = ZoomDialog(self, self)
        dlg.exec()

    # ------------------------------------------------------------ Prozesse

    def set_busy(self, busy):
        for b in (self.btn_build, self.btn_test, self.btn_run, self.btn_update):
            b.setEnabled(not busy)
        self.console_input.setEnabled(busy)
        self.agent_send_btn.setEnabled(self.agent_proc is None and not busy)

    def run_process(self, cmd, kind="build", lesson=None, stdin_text=None,
                    header=None, interactive=False):
        if self.proc is not None:
            return
        self.save_all()
        if header:
            self.console.write_line(header)
        self.proc_kind = kind
        self.proc_lesson = lesson
        self.last_output = ""
        self.proc = QProcess(self)
        self.proc.setWorkingDirectory(ROOT)
        self.proc.readyReadStandardOutput.connect(self._proc_stdout)
        self.proc.readyReadStandardError.connect(self._proc_stderr)
        self.proc.finished.connect(self._proc_finished)
        self.set_busy(True)
        self.proc.start(cmd[0], cmd[1:])
        if interactive:
            pass   # stdin bleibt offen — die Eingabezeile unten füttert das Programm
        elif stdin_text is not None:
            self.proc.write(stdin_text.encode("utf-8"))
            self.proc.closeWriteChannel()
        else:
            self.proc.closeWriteChannel()

    def _proc_stdout(self):
        data = bytes(self.proc.readAllStandardOutput()).decode("utf-8", "replace")
        self.last_output += data
        self.console.write(data)

    def _proc_stderr(self):
        data = bytes(self.proc.readAllStandardError()).decode("utf-8", "replace")
        self.last_output += data
        self.console.write(data)

    def _proc_finished(self, code, _status):
        self.console.flush()
        color = "#2e7d32" if code == 0 else "#c62828"
        self.console.write_line(f"== beendet (Exit-Code {code}) ==", color=color)
        kind = getattr(self, "proc_kind", "")
        lesson = getattr(self, "proc_lesson", None)
        self.proc = None
        self.set_busy(False)

        if kind == "update":
            self.reload_tree()
            if (self.current_lesson
                    and os.path.isdir(os.path.join(LEKTIONEN_DIR, self.current_lesson))):
                self.load_lesson(self.current_lesson)

        # Fortschritt: Testlauf komplett bestanden → Aufgabe abgeschlossen
        if (kind == "test" and lesson and code == 0
                and "✔" in self.last_output and "✘" not in self.last_output
                and "FEHLGESCHLAGEN" not in self.last_output):
            if lesson not in self.progress:
                self.progress.add(lesson)
                self._save_progress()
                self._apply_progress()
                self.console.write_line(
                    "🎉 Alle Tests bestanden — Aufgabe als abgeschlossen markiert!",
                    color="#2e7d32")
            else:
                self.console.write_line("🎉 Alle Tests bestanden!",
                                        color="#2e7d32")

    def send_console_input(self):
        """Zeile aus der Eingabezeile an das laufende Programm weiterreichen."""
        line = self.console_input.text()
        self.console_input.clear()
        if self.proc is None or not line:
            return
        self.console.write_line("> " + line, color=SCHEME["user"])
        self.proc.write((line + "\n").encode("utf-8"))

    def do_build(self):
        self.run_process([TRAINER, "build", self.current_lesson], kind="build",
                         lesson=self.current_lesson,
                         header=f"\n== Kompilieren: {self.current_lesson} ==")

    def do_test(self):
        self.run_process([TRAINER, "test", self.current_lesson], kind="test",
                         lesson=self.current_lesson,
                         header=f"\n== Testen: {self.current_lesson} ==")

    def do_update(self):
        self.run_process([TRAINER, "update"], kind="update",
                         header="\n== Updates von GitHub holen ==")

    def do_run(self):
        bin_path = os.path.join(LEKTIONEN_DIR, self.current_lesson, "build", "app")
        cmd = ["/bin/bash", "-c", " ".join([
            shlex.quote(TRAINER), "build", shlex.quote(self.current_lesson),
            "&&", shlex.quote(bin_path)])]
        self.run_process(cmd, kind="run", lesson=self.current_lesson,
                         interactive=True,
                         header="\n== Starten (interaktiv — Eingaben unten tippen) ==")

    # ------------------------------------------------------------ Agent

    def build_agent_panel(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)

        self.agent_chat = Chat()
        layout.addWidget(self.agent_chat, 1)

        quick = QHBoxLayout()
        b1 = QPushButton("Testfehler erklären")
        b1.clicked.connect(lambda: self.agent_send(
            "Warum schlägt mein Test fehl? Erkläre mir den Fehler und gib "
            "mir einen Hinweis — keine vollständige Lösung.", attach_console=True))
        b2 = QPushButton("Hinweis geben")
        b2.clicked.connect(lambda: self.agent_send(
            "Gib mir einen gestuften Hinweis für die aktuelle Lektion — "
            "keine vollständige Lösung."))
        b3 = QPushButton("Code erklären")
        b3.clicked.connect(lambda: self.agent_send(
            "Erkläre mir kurz, was mein aktueller Code in dieser Lektion "
            "macht, und ob er zur Aufgabe passt."))
        for b in (b1, b2, b3):
            quick.addWidget(b)
        btn_config = QPushButton("⚙ Konfiguration")
        btn_config.setToolTip("Agent-Konfiguration: Modell wählen, Status prüfen")
        btn_config.clicked.connect(self.open_config)
        quick.addWidget(btn_config)
        btn_clear = QPushButton("🧹 Verlauf")
        btn_clear.setToolTip("Chat-Anzeige leeren — der Agent erinnert sich weiterhin an die Lektion")
        btn_clear.clicked.connect(self.agent_clear_chat)
        quick.addWidget(btn_clear)
        quick.addStretch(0)
        layout.addLayout(quick)

        self.model_label = QLabel("")
        self.update_model_label()
        layout.addWidget(self.model_label)

        input_row = QHBoxLayout()
        self.agent_input = QPlainTextEdit()
        self.agent_input.setPlaceholderText(
            "Frage an den Agenten …  (Strg+Return = senden)")
        self.agent_input.setFixedHeight(
            int(3.2 * self.agent_input.fontMetrics().height()))
        self.agent_input.installEventFilter(self)
        input_row.addWidget(self.agent_input, 1)

        btns = QVBoxLayout()
        self.agent_send_btn = QPushButton("Senden")
        self.agent_send_btn.clicked.connect(self.agent_send_from_input)
        self.agent_abort_btn = QPushButton("Abbrechen")
        self.agent_abort_btn.setEnabled(False)
        self.agent_abort_btn.clicked.connect(self.agent_abort)
        btns.addWidget(self.agent_send_btn)
        btns.addWidget(self.agent_abort_btn)
        input_row.addLayout(btns)
        layout.addLayout(input_row)

        self.agent_chat.add_system(
            "Agent bereit. Lektion laden und fragen — der Agent kennt die "
            "Projektregeln (AGENTS.md) und gibt gestufte Hinweise statt "
            "fertiger Lösungen.",
        )
        return widget

    def agent_clear_chat(self):
        self.agent_chat.clear_chat()

    def open_config(self):
        dlg = ConfigDialog(self, self.settings,
                           (self.settings.value("model", "") or "").strip())
        if dlg.exec():
            model = dlg.model.currentText().strip()
            self.settings.setValue("model", model)
            preprompt = dlg.preprompt_edit.toPlainText().strip()
            self.settings.setValue("preprompt", preprompt)
            self.update_model_label()

    def update_model_label(self):
        model = (self.settings.value("model", "") or "").strip()
        self.model_label.setText(
            "Modell: " + (model if model else "OpenCode-Standard (über ⚙ änderbar)"))

    def agent_send_from_input(self):
        text = self.agent_input.toPlainText().strip()
        if text:
            self.agent_input.setPlainText("")
            self.agent_send(text)

    def eventFilter(self, obj, event):
        if obj is self.agent_input and event.type() == QEvent.Type.KeyPress:
            if (event.modifiers() & Qt.KeyboardModifier.ControlModifier
                    and event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter)):
                self.agent_send_from_input()
                return True
        return super().eventFilter(obj, event)

    def agent_abort(self):
        if self.agent_proc is not None:
            self.agent_proc.kill()

    def agent_send(self, question, attach_console=False):
        if self.agent_proc is not None:
            return
        if not self.current_lesson:
            self.agent_chat.add_system("erst eine Lektion im Baum wählen.")
            return
        self.save_all()

        prompt = question
        preprompt = (self.settings.value("preprompt", "") or "").strip()
        if preprompt:
            prompt = ("[Vorgabe des Nutzers — gilt für alle deine Antworten: "
                      + preprompt + "]\n\n" + prompt)
        if attach_console and self.last_output.strip():
            tail = "\n".join(self.last_output.strip().splitlines()[-60:])
            prompt += "\n\n[Letzte Ausgabe des Trainer-Skripts]:\n" + tail
        lesson_abs = os.path.join(LEKTIONEN_DIR, self.current_lesson)
        prompt += f"\n\n[Aktuelle Lektion: {lesson_abs}]"

        slug = re.sub(r"[^a-z0-9]+", "_", self.current_lesson.lower()).strip("_")
        session_id = "ses_trainer_v2_" + slug

        args = [OPENCODE, "run", "--standalone", "-s", session_id]
        model = (self.settings.value("model", "") or "").strip()
        if model:
            args += ["-m", model]
        args += ["--auto", prompt]

        note = "  (+ letzte Testausgabe)" if attach_console else ""
        self.agent_chat.add_user(question + note)
        self.agent_chat.begin_agent()
        model_name = model if model else "OpenCode-Standard"
        self.agent_chat.update_agent(
            f"… denkt (Modell: {model_name}) — Abbrechen möglich …")

        self.agent_proc = QProcess(self)
        self.agent_proc.setWorkingDirectory(ROOT)
        self.agent_proc.readyReadStandardOutput.connect(self._agent_stdout)
        self.agent_proc.readyReadStandardError.connect(self._agent_stderr)
        self.agent_proc.finished.connect(self._agent_finished)
        self.agent_proc.errorOccurred.connect(self._agent_error)
        self.agent_send_btn.setEnabled(False)
        self.agent_abort_btn.setEnabled(True)
        self.agent_raw = ""
        self.agent_text = ""
        self.agent_proc.start(OPENCODE, args[1:])
        self.agent_proc.closeWriteChannel()   # stdin schließen — kein Warten

    def _agent_stdout(self):
        data = strip_ansi(bytes(self.agent_proc.readAllStandardOutput()).decode("utf-8", "replace"))
        self.agent_raw += data
        lines = self.agent_raw.split("\n")
        self.agent_raw = lines[-1]
        for line in lines[:-1]:
            s = line.strip()
            if s.startswith(">") or not s:
                continue
            self.agent_text += line + "\n"
            self.agent_chat.update_agent(self.agent_text)

    def _agent_stderr(self):
        data = strip_ansi(bytes(self.agent_proc.readAllStandardError()).decode("utf-8", "replace"))
        for line in data.splitlines():
            s = line.strip()
            if not s:
                continue
            if "Error" in s or "limit" in s.lower() or "fatal" in s.lower():
                self.agent_chat.add_error(s)

    def _agent_error(self, err):
        if err != QProcess.ProcessError.FailedToStart:
            return
        self.agent_chat.add_error(
            "opencode konnte nicht gestartet werden - ./install.sh ausfuehren "
            "oder opencode einmal im Terminal starten.")
        self.agent_proc = None
        self.agent_send_btn.setEnabled(True)
        self.agent_abort_btn.setEnabled(False)

    def _agent_finished(self, code, _status):
        if self.agent_text.strip():
            self.agent_chat.finish_agent(self.agent_text.rstrip())
        else:
            self.agent_chat.add_system(f"— Agent beendet (Exit-Code {code}) —")
        self.agent_proc = None
        self.agent_send_btn.setEnabled(True)
        self.agent_abort_btn.setEnabled(False)

    # ------------------------------------------------------------ Cheatsheet

    def open_cheatsheet(self):
        if not self.current_lesson:
            return
        thema = self.current_lesson.split("/")[0]
        path = os.path.join(LEKTIONEN_DIR, thema, "CHEATSHEET.md")
        try:
            with open(path, encoding="utf-8") as f:
                content = f.read()
        except OSError as e:
            self.console.write_line(f"Cheatsheet nicht gefunden: {e}", color="#c62828")
            return
        win = QMainWindow(self)
        win.setWindowTitle(f"Cheatsheet — {thema}")
        win.resize(760, 820)
        browser = QTextBrowser()
        browser.setFont(monospace(self.sizes["aufgabe"]))
        browser.setHtml(md_html(content))
        win.setCentralWidget(browser)
        win.show()
        self.cheat_windows.append(win)


OPENCODE = "opencode"


# ------------------------------------------------------------ Start

def smoke(w):
    themes = w.tree.topLevelItemCount()
    lessons = sum(w.tree.topLevelItem(i).childCount() for i in range(themes))
    print(f"Themen: {themes}, Lektionen: {lessons}")
    if themes != 7 or lessons != 25:
        return 1
    w.load_lesson("01-eingabe/02-summe")
    if w.tabs.count() != 1 or "Summe" not in w.task_browser.toPlainText():
        print("Laden fehlgeschlagen")
        return 1
    if "TODO" not in w.tabs.widget(0).toPlainText():
        print("Editor-Inhalt falsch")
        return 1
    r = subprocess.run([TRAINER, "build", "01-eingabe/01-hallo-welt"],
                       cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        print("build fehlgeschlagen:", r.stderr)
        return 1
    print("build: OK")
    print("SMOKE OK")
    return 0


def main():
    if "--smoke" in sys.argv:
        os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    app = QApplication(sys.argv)
    app.setApplicationName("C++ Trainer")
    app.setDesktopFileName("cpp-trainer")
    icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.png")
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))
    w = MainWindow()
    maximiert = w.settings.value("win/maximized", False, type=bool)
    if "--smoke" in sys.argv:
        return smoke(w)
    if maximiert:
        w.showMaximized()
    else:
        w.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
