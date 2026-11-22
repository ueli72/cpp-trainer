# C++ Trainer — App (PyQt6)

Eine kleine GUI-Hülle für das `trainer`-Skript: Aufgabenbaum, Editor,
Kompilieren/Testen/Starten, Konsole und die Aufgabe rechts — plus ein
interaktiver OpenCode-Agent als Chat.

## Starten

```bash
cd app
./start.sh
```

`start.sh` richtet bei Bedarf automatisch eine Python-Umgebung (`.venv`)
ein — nur beim ersten Mal, mit Internetverbindung.

### Voraussetzungen

- `python3` (≥ 3.9) und `python3 -m venv` (Debian/Ubuntu:
  `sudo apt install python3-venv python3-pip`)
- Für die Qt-Oberfläche ggf. Systembibliotheken (die PyQt6-Wheels bringen
  Qt mit, aber nicht die Grafik-Bibliotheken des Systems):
  `sudo apt install libgl1 libegl1 libxkbcommon-x11-0 libxcb-cursor0`

Der Tray erkennt das selbst: Wenn Qt die Plattform `xcb` nicht laden kann,
gibt `start.sh` den passenden Installationshinweis aus.

## Bedienung

| Element | Funktion |
|---|---|
| **Baum links** | Thema anklicken → aufklappen; Lektion anklicken → laden |
| **Tabs Mitte** | alle Dateien der Lektion (`main.cpp`, `Vector.h` …) — wird vor jeder Aktion automatisch gespeichert |
| **Kompilieren** | `./trainer build <lektion>` — Fehler landen rot in der Konsole |
| **Testen** | `./trainer test <lektion>` — ✔ grün / ✘ rot |
| **Starten** | kompiliert und startet das Programm mit dem im Dropdown gewählten Testfall als Eingabe |
| **🔄 Updates** | holt neue Aufgaben von GitHub (`./trainer update`) — danach wird der Baum automatisch aktualisiert |
| **❓ Cheatsheet** | öffnet das Cheatsheet des Themas in einem eigenen Fenster |
| **Konsole (unten)** | Ausgabe von Kompilieren/Testen/Starten |
| **Agent (unten)** | Chat mit OpenCode — siehe unten |

## Fortschritt

Läuft ein Testdurchlauf einer Lektion komplett durch, wird die Lektion im
Baum grün mit ✔ markiert und in `fortschritt.json` (Projektordner)
gespeichert — der Kopftext zeigt „Aufgaben — X/Y gelöst“. Nur echte
Testläufe (`🧪 Testen`) zählen; „Starten“ markiert nichts.

## Der Agent-Tab

- Pro Lektion wird eine eigene OpenCode-Sitzung geführt
  (`-s ses_trainer_<lektion>`) — der Kontext bleibt erhalten, auch über
  App-Neustarts hinweg.
- **Schnell-Buttons:**
  - *Testfehler erklären* — sendet die Frage plus die letzte Ausgabe
    aus der Konsole an den Agenten
  - *Hinweis geben* — bewusst „gestufter Hinweis statt Lösung"
  - *Code erklären*
- Die Eingabezeile schickt freie Fragen an den Agenten.
- Der Agent arbeitet im Projektordner und folgt den Regeln in
  `AGENTS.md` (cpp-trainer-Skill: Aufgaben lesen, Tests laufen lassen,
  gestufte Hinweise statt fertiger Lösungen).

### Modell & Konfiguration

- **⚙-Button** im Agent-Tab öffnet die Agent-Konfiguration:
  - OpenCode-Version, Anbieter mit gespeichertem API-Key
  - Modell-Auswahl aus der Liste von `opencode models` (59+ Modelle)
  - **Pre-Prompt** — eine Vorgabe, die jeder Agent-Antwort vorangestellt
    wird (z. B. „Halte dich sehr kurz.“ oder „Nur Hinweise, keine Lösungen.“)
  - „Verbindung testen" prüft Modell + Key sofort
- **API-Keys/Anbieter** konfigurierst du mit opencode-Bordmitteln im
  Terminal: `opencode auth login` — die App nutzt die dort gespeicherten
  Schlüssel automatisch (und baut das Key-Management nicht doppelt nach).
- Läuft das Standard-Modell in ein Usage-Limit, trägst du im Modell-Feld
  z. B. `opencode/glm-5.3-flash` ein (die Einstellung wird gemerkt).

### Wichtig: `--auto`

Der Agent wird mit `--auto` gestartet — Berechtigungen werden
automatisch genehmigt, damit `./trainer test` ohne Rückfragen läuft.
Das bedeutet: Der Agent darf Befehle im Projektordner ausführen.
Wenn du das nicht willst, entferne `"--auto"` in `main.py`
(Funktion `agent_send`).

## Portabilität

Der komplette Ordner `c++Trainer/` kann auf andere Linux-Rechner
kopiert werden. `app/.venv` ist maschinenspezifisch — `start.sh`
baut sie automatisch neu, falls sie fehlt oder nicht zur Python-Version
passt. Voraussetzungen auf dem Zielsystem: `python3` + venv/pip
(siehe oben) und die genannten Qt-Systembibliotheken.

## Test (ohne GUI)

```bash
./start.sh --smoke
```
prüft Kopflos: Import, Baum (7 Themen / 25 Lektionen), Laden einer
Lektion, Markdown-Konvertierung, Kompilier-Lauf.


## Fehlerbehebung

| Symptom | Ursache/Lösung |
|---|---|
| „Modelle werden geladen" endet nicht | Läuft `opencode models` im Terminal im Projektordner? Beim ersten Start lädt opencode die Modell-Liste aus dem Netz. |
| „opencode konnte nicht gestartet werden" | opencode nicht installiert → `./install.sh` (Schritt 3) oder `opencode` einmal im Terminal starten (Ersteinrichtung). |
| Agent antwortet mit Usage-Limit-Fehler | Modell-Feld füllen, z. B. `opencode/glm-5.3-flash` (⚙-Dialog). |
