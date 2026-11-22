# C++ Trainer

Lerne C++ direkt an der Konsole: **Aufgabe lesen → Code schreiben → Tests laufen
lassen.** OpenCode hilft dir dabei als KI-Tutor — mit Testreihen, Fehleranalyse
und Hinweisen, ohne dir die Lösung vorwegzunehmen.

---

## 🚀 Sofort loslegen

So startest du deine erste Lektion (dauert keine Minute):

1. **Editor öffnen:** VSCodium → *Datei → Ordner öffnen* → diesen Ordner (`c++Trainer`)
2. **Aufgabe lesen:** `lektionen/01-eingabe/01-hallo-welt/README.md` — dort steht, was zu tun ist
3. **Lösung schreiben:** dieselbe Datei `main.cpp` öffnen und den Code eintragen
4. **Testen:** **Strg+Shift+B** drücken (oder unten links den 🧪-Button „Tests")
   - 🟢 **grün** = alle Tests bestanden → Glückwunsch, weiter zur nächsten Lektion!
   - 🔴 **rot** = es klemmt noch → siehe „Hilfe von der KI" unten
5. **Ausprobieren:** zwischendurch das Programm selbst starten —
   ▶-Button „Ausführen" oder im Terminal `./trainer run 01`

> Die Tests prüfen, ob dein Programm **exakt** die geforderte Ausgabe liefert.
> Schau also genau hin: Groß-/Kleinschreibung, Kommas, Leerzeichen.

## 🔁 Der Lernkreislauf

Jede Lektion funktioniert immer gleich:

```text
README.md der Lektion lesen          (die Aufgabe)
        ↓
main.cpp bearbeiten                  (dein Code, in VSCodium)
        ↓
./trainer test <lektion>             (oder Strg+Shift-B / 🧪-Button)
        ↓                        ↓
      🟢 fertig              🔴 verbessern → hinweise holen → nochmal
```

Tipp: Erst selbst knobeln, dann Hilfe holen. Genau so lernt man am meisten. 😉

> Die Lektionen 02–12 bilden eine Übungsreihe mit wachsender Schwierigkeit:
> Ein-/Ausgabe → Schleifen → Ziffern zerlegen → Bits → Zahlensysteme
> (Klausurniveau). `./trainer list` zeigt sie alle — die Aufgabenstellungen
> stehen in der jeweiligen `README.md` der Lektion.

## ⌨️ Die wichtigsten Befehle

Alle Lektionsangaben dürfen abgekürzt werden — `./trainer test hello` findet
die Lektion `01-eingabe/01-hallo-welt` genauso wie `./trainer test eingabe/01`.

| Befehl | Wirkung |
|---|---|
| `./trainer list` | Alle Lektionen anzeigen |
| `./trainer test eingabe/01` | Kompilieren + automatische Tests |
| `./trainer run 01` | Kompilieren + Programm selbst ausprobieren (Eingaben tippen, Ende mit Strg+D) |
| `./trainer build 01` | Nur kompilieren |
| `./trainer all` | Tests aller Lektionen |
| `./trainer new 02-verzweigung/03-namen` | Neue Lektion anlegen |

## 🤖 Hilfe von der KI (OpenCode)

OpenCode läuft direkt im Projektordner und kennt dein System:

1. **Täglicher Start:** `./lernen` (oder `opencode` im Projektordner)
2. **Geführte Einführung:** tippe im Chat **`/lernen`** — die KI zeigt dir Lektionen und Ablauf
3. **Hilfe beim Lernen** — sag einfach, was du brauchst:
   - „**Teste meine Lösung**" — die KI schreibt passende Testfälle (Normalfälle,
     Randfälle, Sonderfälle), legt sie unter `tests/` ab, führt sie aus und
     meldet dir, was lief
   - „**Warum schlägt mein Test fehl?**" — konkreter Hinweis statt fertiger Lösung
   - „Erkläre mir Zeile X" oder „Erkläre mir Zeiger" — dein persönlicher Tutor

Dein Code wird dabei nie heimlich geändert — das Lernen bleibt bei dir.

### Buttons in der Statusleiste

Unten links in VSCodium — die Erweiterung **Task Buttons** bringt sie mit und
wird von `install.sh` automatisch mitinstalliert (sonst einmalig über Open VSX:
`spencerwmiles.vscode-task-buttons`):

| Button | Wirkung |
|---|---|
| 🧪 **Tests** | Tests der Lektion, in der die offene Datei liegt (= Strg+Shift+B) |
| ▶ **Ausführen** | Programm manuell starten |
| 🔧 **Kompilieren** | Nur kompilieren |
| ☑ **Alle Tests** | Alle Lektionen testen |
| 📖 **Hilfe** | Öffnet diese Anleitung — **direkt schön gerendert** |

> **Tipp:** `.md`-Dateien in diesem Projekt öffnen sich standardmäßig **gerendert**
> mit der erweiterten Vorschau (**Markdown Preview Enhanced**, wird von
> `install.sh` mitinstalliert; die Tastenkürzel **Strg+Shift+V** / **Strg+K, V**
> nutzen sie ebenfalls). Zum Bearbeiten einer Markdown-Datei klickst du in der
> Vorschau oben auf das Stift-Symbol („Quelle öffnen") — Theme-Auswahl per
> Rechtsklick in der Vorschau.

---

Ab hier folgt Technik für später — zum Lernen brauchst du das nicht sofort.

## ✏️ Eigene Lektionen erstellen

Wenn du weiter bist, legst du eigene Lektionen an:

```bash
./trainer new 02-verzweigung/03-namen
```

Dann in `lektionen/02-verzweigung/03-namen/`:

- `README.md` — die Aufgabenstellung (was soll das Programm bei welcher Eingabe ausgeben?)
- `main.cpp` — dein Lösungscode
- `tests/` — Testfälle als Paare: `01-name.in` (Eingabe, darf leer sein) +
  `01-name.out` (erwartete Ausgabe), optional `01-name.args` (Kommandozeilenargumente)

Die erwarteten Ausgaben schreibst du selbst — oder du lässt sie OpenCode aus
der Aufgabenstellung ableiten („Schreibe Tests für Lektion 02").

## 📁 Aufbau des Projekts

```
c++Trainer/
├── trainer                      # alles-in-einem Skript (bauen / ausführen / testen)
├── install.sh                   # Einmal-Installation auf einem neuen Rechner
├── lernen                       # täglicher Start: OpenCode im Projektordner
├── lektionen/                   # Lektionen in Themen-Ordnern
│   ├── 01-eingabe/              # Thema: Eingabe
│   │   └── 01-hallo-welt/       # Beispiellektion
│   │       ├── README.md        # Aufgabenstellung
│   │       ├── main.cpp         # hier schreibst du deinen Code
│   │       └── tests/           # automatische Tests
│   │           ├── 01-standard.in   # Eingabe (stdin), kann leer sein
│   │           └── 01-standard.out  # erwartete Ausgabe
├── vorlage/                     # Kopiervorlage für neue Lektionen
├── .opencode/skills/cpp-trainer/
│   └── SKILL.md                 # KI-Skill: schreibt & läuft Tests, gibt Rückmeldung
├── .opencode/commands/lernen.md # /lernen: geführte Einführung durch die KI
└── .vscode/                     # VSCodium-Tasks + Statusleisten-Buttons
```

## 💻 Auf einen anderen Computer übertragen

Es gibt keine absoluten Pfade — den ganzen Ordner `c++Trainer` kopieren und
dort einmal `./install.sh` ausführen. Fertig.

**Ordner übertragen** — einer von drei Wegen:

```bash
# Variante A: USB-Stick — Ordner einfach draufziehen und am Zielrechner einstecken

# Variante B: im Netzwerk (von diesem Rechner aus; Ziel-IP anpassen)
rsync -av ~/Dokumente/c++Trainer  benutzer@ziel-pc:~/Dokumente/

# Variante C: per git (einmalig hochladen, überall klonen)
git init && git add -A && git commit -m "C++ Trainer"
# → auf einen Git-Anbieter pushen, am Zielrechner klonen
```

**Auf dem neuen Rechner** (Linux Mint / Ubuntu / Debian):

```bash
cd c++Trainer
./install.sh
```

Das Skript installiert bei Bedarf **alles**: `g++`/`make`/`curl` (per apt),
**VSCodium** selbst, **OpenCode** sowie die VSCodium-Erweiterungen
(**Markdown Preview Enhanced** für die schöne Markdown-Vorschau, **Task
Buttons** für die Statusleisten-Buttons). Danach prüft es die Lernumgebung,
zeigt die Kurzanleitung und startet OpenCode mit einer KI-Einführung.
Alles Weitere (KI-Skill, `/lernen`-Befehl, Buttons, gerenderte Vorschau)
reist im Projektordner mit. Der tägliche Start: `./lernen`.

**Beim allerersten Start vor Ort:**
1. OpenCode fragt beim ersten Start nach dem Login bzw. Modell — einmal durchklicken.
2. VSCodium: einmal „Fenster neu laden“ (Strg+Shift+P), damit Buttons und
   Markdown-Vorschau aktiv werden.

(Windows: am besten im WSL arbeiten; macOS: statt `apt` Homebrew nutzen.)

## ✅ Voraussetzungen

- **Linux** (Linux Mint/Ubuntu/Debian: alles per `install.sh`) mit `g++` und `bash`
- **VSCodium** als Editor (oder jeder andere Editor — nötig sind nur Terminal und Textdateien);
  `install.sh` installiert VSCodium bei Bedarf gleich mit — zusammen mit
  **Markdown Preview Enhanced** (schöne Markdown-Vorschau) und
  **Task Buttons** (Statusleisten-Buttons)
- **OpenCode** für die KI-Hilfe (https://opencode.ai) — optional, aber sehr zu empfehlen
