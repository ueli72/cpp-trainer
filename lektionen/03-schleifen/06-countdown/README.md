# Schleifen 06 — Countdown

## Ziel

Die `while`-Schleife im Kleinen: eine Bedingung prüfen, **dann** eine Runde laufen — bis die Bedingung nicht mehr gilt.

## Aufgabe

Lies eine Zahl `n` zwischen 1 und 100 ein.

Gib einen Countdown aus: **eine Zeile pro Zahl**, von `n` abwärts bis `1`. Danach eine Zeile mit `Los!`:

**Eingabe** (Beispiel):

```
3
```

**Ausgabe** (Beispiel):

```
3
2
1
Los!
```

## Hinweise

- `while` läuft, **solange** die Bedingung gilt — hier: solange dein Zähler größer als 0 ist:
  ```cpp
  while (zaehler > 0) {
      // … eine Runde …
  }
  ```
- In jeder Runde: Zähler ausgeben und um 1 verkleinern (`zaehler = zaehler - 1;` — kurz: `zaehler--;`).
- Das `Los!` gibst du **nach** der Schleife aus — einmal, nicht pro Runde.
- Anders als bei `for` brauchst du keinen Start-/Schritt-Teil: Zähler vorher anlegen, selbst runterzählen.

## So testest du

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test schleifen/06`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run schleifen/06`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?“) oder OpenCode im Terminal fragen
