# Ziffern 05 — Fehlersuche: Ziffernanalyse

## Ziel

Ziffern-Rechnen debuggen: % und / und ihre Rollen.

## Aufgabe

Das Programm soll eine nicht-negative Zahl einlesen und
- die **Quersumme** (Summe aller Ziffern)
- die Zahl **mit umgedrehten Ziffern**
ausgeben.

Es enthält **2 eingebaute Fehler** (1 Compiler, 1 Logik/vertauscht).

## SOLL-Verhalten (Beispiel, 123)

```
Quersumme: 6
Gedreht: 321
```

## Hinweise

- Was liefert `123 % 10` und was `123 / 10`? Und was steht im Code?
- Achte darauf, welche der beiden Operationen wo verwendet wird — eine
  davon ist an einer Stelle vertauscht.

## Testen

`./trainer test ziffern/05` — die Testfälle liegen sichtbar in `tests/`
