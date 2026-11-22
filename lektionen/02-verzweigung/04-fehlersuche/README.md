# Verzweigung 04 — Fehlersuche: Zahlendiagnose

## Ziel

Verzweigungen debuggen: Der Compiler und die Testfälle zeigen dir, wo ein
Programm klemmt.

## Aufgabe

Das Programm soll eine Zahl einlesen und **zwei Zeilen** ausgeben:
- gerade / ungerade
- positiv / negativ / null

Es enthält **3 eingebaute Fehler** (2 Compiler, 1 Logik/Grenzfall).

## SOLL-Verhalten (Beispiele)

```
4      →  gerade   +   positiv
-3     →  ungerade +   negativ
0      →  gerade   +   null
```

## Hinweise

- Achtung auf den Unterschied zwischen **Zuweisung (=)** und
  **Vergleich (==)** — der Compiler meckert, wenn die linke Seite eines
  = kein Speicherplatz ist.
- Der Grenzfall **0** wird im zweiten Vergleich gerne falsch einsortiert.

## Testen

`./trainer test verzweigung/04` — die Testfälle liegen sichtbar in `tests/`
