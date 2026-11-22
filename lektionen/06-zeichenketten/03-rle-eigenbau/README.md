# Zeichenketten 03 — Run-Length-Encoding (Eigenbau)

## Ziel

Alles selbst bauen: Zeichenketten durchlaufen, Runs gleicher Buchstaben
zählen und kompakt ausgeben — die klassische **Run-Length-Encoding**-Aufgabe.

## Aufgabe

Lies ein Wort ein (nur Buchstaben, keine Leerzeichen) und gib es
**laufzeitkomprimiert** aus: jeder Buchstabe gefolgt von der Anzahl,
wie oft er hintereinander vorkommt.

## SOLL-Verhalten (Beispiele)

```
AAABBC
```

```
A3B2C1
```

Weitere Beispiele: `AAAA` → `A4` · `ABC` → `A1B1C1`

## Hinweise

- Merke dir das **vorherige Zeichen** und einen **Zähler**.
- Wechselt das Zeichen (oder das Wort endet), hänge
  `<buchstabe><anzahl>` an das Ergebnis an und setze den Zähler auf 1.
- Der letzte Lauf endet **am Wortende** — daran denken, ihn auch
  auszugeben!

## Testen

`./trainer test zeichenketten/03` — die Testfälle liegen sichtbar in `tests/`
