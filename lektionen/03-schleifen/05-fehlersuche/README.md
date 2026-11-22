# Schleifen 05 — Fehlersuche: Treppen-Statistik

## Ziel

Schleifen debuggen: Off-by-one-Fehler und fehlende Zuweisungen finden.

## Aufgabe

Das Programm soll eine Zahl n einlesen und
- eine **Sterntreppe** ausgeben (n Zeilen, Zeile i hat i Sterne)
- die **Summe** 1 + 2 + … + n ausgeben

Es enthält **2 eingebaute Fehler** (1 Compiler, 1 Off-by-one/Logik).

## SOLL-Verhalten (Beispiel, n = 3)

```
*
**
***
Summe: 6
```

## Hinweise

- Zähle die Sterne der Treppen-Zeilen nach: Zeile 1, 2, 3 — wie oft läuft
  die äußere Schleife wirklich?
- Die Summen-Schleife: Was wird da eigentlich aufsummiert?

## Testen

`./trainer test schleifen/05` — die Testfälle liegen sichtbar in `tests/`
