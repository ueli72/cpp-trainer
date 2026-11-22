# Vektoren 04 — Fehlersuche: Skalarprodukt

## Ziel

Vektoren debuggen: Der Compiler zeigt dir die erste Stelle, die Testfälle
zeigen dir, was das Ergebnis noch falsch macht.

## Aufgabe

Das Programm liest **zwei Vektoren** (wie in Vektoren 03: zuerst die
Größe n1, dann n1 Werte; dann die Größe n2, dann n2 Werte) und gibt das
**Skalarprodukt** aus — oder `error`, wenn die Größen nicht passen.

Es enthält **3 eingebaute Fehler** (1 Compiler, 2 Logik).

## SOLL-Verhalten (Beispiele)

```
3
1 2 3
4 5 6
```

```
32
```

Unterschiedliche Längen (`2` und `3` Werte): → `error`

## Hinweise

- Der Compiler-Fehler zeigt die Zeile — lies die Meldung und zähle die
  Semikolons.
- Danach: zwei Logik-Fehler im Skalarprodukt — der Startwert der Summe und
  die Schleifengrenze (der letzte Wert fehlt im Ergebnis!).
- Die Größenprüfung selbst ist korrekt — unterschiedliche Längen geben
  `error` aus.

## Testen

`./trainer test vektoren/04` — die Testfälle liegen sichtbar in `tests/`
