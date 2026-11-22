# Vektoren 05 — Fehlersuche: Zahlenstatistik

## Ziel

Vektoren debuggen: Der Compiler zeigt Compiler-Fehler, die Testfälle zeigen
falsche Ergebnisse — beides zusammen führt zur Lösung.

## Aufgabe

Das Programm liest beliebig viele Zahlen (Ende durch Dateiende/Strg+D) und
soll ausgeben:
- **Anzahl:** wie viele Zahlen gelesen wurden
- **Summe:** die Summe aller Zahlen
- **Maximum:** die größte Zahl

Es enthält **3 eingebaute Fehler** (1 Compiler, 2 Logik).

## SOLL-Verhalten (Beispiel)

```
2 9 4
```

```
Anzahl: 3
Summe: 15
Maximum: 9
```

## Hinweise

- Der Compiler-Fehler steckt im Rechnen — eine Variable wird benutzt, bevor
  sie einen Wert hat.
- Die Ausgaben Anzahl/Summe/Maximum: zwei der drei stimmen nicht — prüfe,
  was wirklich aufsummiert und verglichen wird.

## Testen

`./trainer test vektoren/05` — die Testfälle liegen sichtbar in `tests/`
