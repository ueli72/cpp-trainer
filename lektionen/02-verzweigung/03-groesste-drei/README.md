# Verzweigung 03 — Die größte von dreien (Eigenbau)

## Ziel

Verzweigungen kombinieren, ohne Vorlage: drei Werte vergleichen und das Maximum finden — der Bauplan steht nur als Kommentare in `main.cpp`.

## Aufgabe

Lies drei ganze Zahlen `a`, `b`, `c` ein (in einer Zeile, durch Leerzeichen getrennt) und gib die **größte** der drei aus:

**Eingabe** (Beispiel):

```
4 9 2
```

**Ausgabe** (Beispiel):

```
Groesste: 9
```

Bei gleichen Werten zählt die Zahl einmal (`7 7 7` → `Groesste: 7`).

## Wie du vorgehst

Der **Bauplan steht als Kommentare in `main.cpp`** — zwei Lösungswege sind dort skizziert (drei Verzweigungen oder schrittweise mit einer `maximum`-Variable). Beide sind richtig.

## Hinweise

- negative Zahlen sind erlaubt — „am größten“ heißt nicht „positiv“.
- Denk an den doppelten Gleichheits-Vergleich `==`, falls du ihn brauchst.
- Es gibt genau eine Ausgabezeile: `Groesste: <wert>`.

## So testest du

- `./trainer test verzweigung/03verzweigung/03` (in der App: 🧪-Button) — die Testfälle liegen sichtbar in `tests/`
- `./trainer run verzweigung/03verzweigung/03` — das Programm selbst ausprobieren
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?“) oder OpenCode im Terminal fragen
