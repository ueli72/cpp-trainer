# Zeichenketten 01 — Erste Zeichenketten

## Ziel

`std::string` kennenlernen: der Typ für **Text** ("Zeichenketten") — mit
Länge, einzelnem Zeichen und Verkettung.

## Aufgabe

Lies ein Wort ein und gib aus:
- **Laenge:** wie viele Zeichen das Wort hat
- **Erster:** der erste Buchstabe
- **Letzter:** der letzte Buchstabe

## SOLL-Verhalten (Beispiel)

```
Hallo
```

```
Laenge: 5
Erster: H
Letzter: o
```

## Hinweise

- `wort.length()` liefert die **Länge**, `wort[i]` das i-te Zeichen
  (ab 0 gezählt!), `wort[0]` den ersten und `wort[wort.length() - 1]`
  den letzten Buchstaben.
- Ein einzelnes Zeichen ist der Typ `char` — in **einfachen Anführungszeichen**: `'H'`

## Testen

`./trainer test zeichenketten/01` — die Testfälle liegen sichtbar in `tests/`
