# Zeichenketten 04 — Fehlersuche: Vokale und Rueckwaerts

## Ziel

Zeichenketten-Code debuggen: Der Compiler zeigt Compiler-Fehler, die
Testfälle zeigen falsche Ergebnisse — beides zusammen führt zur Lösung.

## Aufgabe

Das Programm liest ein Wort ein (Kleinbuchstaben) und soll ausgeben:
- **Vokale:** wie viele der Buchstaben a, e, i, o oder u sind
- **Rueckwaerts:** das Wort rückwärts

Es enthält **3 eingebaute Fehler** (1 Compiler, 2 Logik).

## SOLL-Verhalten (Beispiel)

```
hallo
```

```
Vokale: 2
Rueckwaerts: ollah
```

## Hinweise

- Ein Compiler-Fehler: ein **Semikolon** fehlt — der Compiler zeigt die
  Zeile und schlägt meist direkt die Reparatur vor.
- Zwei Logik-Fehler: die **Vokal-Bedingung** (ein Zeichen kann nicht
  gleichzeitig a UND e sein — welches logische Zeichen gehört da hin?) und
  die **Rückwärts-Reihenfolge** (hänge jedes Zeichen vorne an).

## Testen

`./trainer test zeichenketten/04` — die Testfälle liegen sichtbar in `tests/`
