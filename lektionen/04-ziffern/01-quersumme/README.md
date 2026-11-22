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

- `./trainer test ziffern/01` (oder in VSCodium Strg+Shift-B bzw. der 🧪-Button) — die Testfälle liegen sichtbar in `tests/`
- `./trainer run ziffern/01` — das Programm selbst ausprobieren
- Bei roten Tests: OpenCode fragen, z. B. „Warum schlägt mein Test fehl?“
