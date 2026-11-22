# Eingabe 03 — Durchschnitt

## Ziel

Mit Gleitkommazahlen rechnen und die Ausgabe auf eine feste Anzahl Nachkommastellen formatieren.

## Aufgabe

Lies drei ganze Zahlen ein (in einer Zeile, durch Leerzeichen getrennt).

Gib ihren **Durchschnitt** mit **genau zwei Nachkommastellen** aus:

**Eingabe** (Beispiel):

```
1 2 3
```

**Ausgabe** (Beispiel):

```
Durchschnitt: 2.00
```

> **Skelett:** In `main.cpp` steht schon ein Teil — den Rest ergänzt du an den `TODO`-Stellen.

## Hinweise

- Ganze Zahlen geteilt durch ganze Zahlen ergibt wieder eine ganze Zahl: `9 / 4` ist `2`. Rechne daher mit `double` weiter, z. B. durch Division durch `3.0`.
- Formatierung: `std::cout << std::fixed << std::setprecision(2) << durchschnitt;` aus `<iomanip>`.
- Der Punkt ist das Dezimaltrennzeichen (`2.00`, nicht `2,00`).

## So testest du

- `./trainer test eingabe/03` (oder in VSCodium Strg+Shift-B bzw. der 🧪-Button) — die Testfälle liegen sichtbar in `tests/`
- `./trainer run eingabe/03` — das Programm selbst ausprobieren
- Bei roten Tests: OpenCode fragen, z. B. „Warum schlägt mein Test fehl?“
