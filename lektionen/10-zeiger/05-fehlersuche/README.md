# Zeiger 05 — Fehlersuche: Zeiger

## Ziel

Zeiger-Code debuggen: Der Compiler zeigt dir die erste Stelle, die
Testfälle zeigen dir, was das Ergebnis noch falsch macht.

## Aufgabe

Das Programm liest **zwei ganze Zahlen** `a` und `b` und gibt die Summe
(unter Verwendung von `add`) sowie die beiden Werte **nach dem Tausch**
(unter Verwendung von `tauschen`) aus:

**SOLL-Ausgabe** (Eingabe `3 7`):

```
Summe: 10
Getauscht: 7 3
```

Es enthält **3 eingebaute Fehler** (1 Compiler, 2 Logik).

## Hinweise

- Der Compiler-Fehler steht im `main` — eine Zeile, ein Semikolon.
- Danach: `add` berechnet die Summe, aber in eine **lokale** Variable —
  das Ergebnis erreicht `main` nie. Schreibe es an die Adresse `res`.
- `tauschen` vertauscht nur die **Zeiger** (lokale Kopien!) statt der
  **Werte** — außen kommt nichts an. Tausche `*a` und `*b`.

## Testen

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test zeiger/05`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run zeiger/05`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?") oder OpenCode im Terminal fragen
