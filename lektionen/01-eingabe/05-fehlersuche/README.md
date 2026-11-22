# Eingabe 05 — Fehlersuche: Zahlenreport

## Ziel

Debuggen lernen: Der Compiler und die Testfälle zeigen dir, wo ein Programm
klemmt. Du behebst die Fehler, bis alle Tests grün sind.

## Aufgabe

Das Programm soll zwei Zahlen einlesen (eine Zeile, durch Leerzeichen
getrennt) und **Summe**, **Produkt** und **Durchschnitt** (mit genau zwei
Nachkommastellen) ausgeben.

Es enthält **3 eingebaute Fehler** (2 Compiler, 1 Rechnen). Die Tests
zeigen das erwartete Ergebnis — der Compiler zeigt dir die Zeilen.

## SOLL-Verhalten (Beispiel)

```
10 20
```

```
Summe: 30
Produkt: 200
Durchschnitt: 15.00
```

## Hinweise

- Der Compiler meldet Compiler-Fehler mit **Zeile und Spalte** — lies die
  Meldung von oben nach unten und behebe die erste Stelle zuerst.
- Die Rechen-Fehler erkennt man am **Ergebnis**: Der Durchschnitt stimmt
  vorne, aber die Nachkommastellen fehlen. Stichwort: Ganzzahldivision.
- Nach jedem behobenen Fehler: `./trainer test eingabe/05` — zählt die
  Anzahl der grünen Tests, siehst du den Fortschritt.

## Testen

`./trainer test eingabe/05` — die Testfälle liegen sichtbar in `tests/`
