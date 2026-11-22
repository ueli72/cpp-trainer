# Vektoren 02 — Statistik mit Vektoren

## Ziel

Mit einem Vektor arbeiten, **nachdem** er gefüllt ist: Minimum, Maximum
und Durchschnitt berechnen — das Skelett gibt die Struktur vor.

## Aufgabe

Lies beliebig viele ganze Zahlen ein (Ende durch Dateiende/Strg+D) und gib
aus:
- **Anzahl:** wie viele Zahlen
- **Minimum:** die kleinste Zahl
- **Maximum:** die größte Zahl
- **Durchschnitt:** der Durchschnitt mit genau zwei Nachkommastellen

Es garantiert mindestens eine Zahl.

## SOLL-Verhalten (Beispiel)

```
2 9 4
```

```
Anzahl: 3
Minimum: 2
Maximum: 9
Durchschnitt: 5.00
```

## Hinweise

- Das Skelett hat die Struktur: `zahlen` wird eingelesen, du ergänzt die
  drei TODO-Blöcke.
- Minimum/Maximum: mit dem **ersten Element** starten und jedes weitere
  vergleichen.
- Der Durchschnitt: Summe durch Anzahl — beachte die Ganzzahldivision.

## Testen

`./trainer test struct/07vektoren/02` — die Testfälle liegen sichtbar in `tests/`
