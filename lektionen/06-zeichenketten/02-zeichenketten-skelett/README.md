# Zeichenketten 02 — Vokale und Rueckwaerts (Skelett)

## Ziel

Zeichenketten durchlaufen und Zeichen prüfen — das Skelett gibt die
Struktur vor, du ergänzt die TODO-Blöcke.

## Aufgabe

Lies ein Wort ein (Kleinbuchstaben) und gib aus:
- **Vokale:** wie viele der Buchstaben a, e, i, o oder u sind
- **Rueckwaerts:** das Wort rückwärts

## SOLL-Verhalten (Beispiel)

```
hallo
```

```
Vokale: 2
Rueckwaerts: ollah
```

## Hinweise

- Ein Zeichen ist ein Vokal: `c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'`
- Rückwärts: jedes gelesene Zeichen **vorne** anfügen —
  `rueckwaerts = c + rueckwaerts;` (einzelnes `char` + `std::string`)

## Testen

`./trainer test zeichenketten/02` — die Testfälle liegen sichtbar in `tests/`
