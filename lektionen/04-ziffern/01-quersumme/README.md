# Ziffern 01 — Quersumme

## Ziel

Die wichtigste Technik der Klausur-Aufgaben: eine Zahl Ziffer für Ziffer mit `% 10` und `/ 10` zerlegen.

## Aufgabe

Lies **eine nicht-negative ganze Zahl** ein.

Gib ihre **Quersumme** aus — also die Summe aller Ziffern:

**Eingabe** (Beispiel):

```
12345
```

**Ausgabe** (Beispiel):

```
Quersumme: 15
```

## Hinweise

- Die letzte Ziffer einer Zahl ist `n % 10`.
- Die letzte Ziffer abschneiden geht mit `n /= 10;` (Ganzzahldivision).
- Wiederhole beides in einer `while`-Schleife, bis `n` gleich `0` ist. Die 0 hat die Quersumme 0.

## So testest du

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test ziffern/01`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run ziffern/01`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?“) oder OpenCode im Terminal fragen
