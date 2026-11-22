# Eingabe 04 — Vektorprodukte

## Ziel

Strukturierte Eingaben verarbeiten: Werte, die nicht durch Leerzeichen, sondern durch **Kommas** getrennt sind — und dabei zwei klassische Vektorberechnungen kennenlernen.

## Aufgabe

Lies zwei dreidimensionale Vektoren ein — **jeweils in einer eigenen Zeile**, im Format `x,y,z` (ganze Zahlen, durch Kommas getrennt).

Berechne daraus das **Skalarprodukt** (eine einzige Zahl) und das **Kreuzprodukt** (wieder ein Vektor) und gib beides aus — jede Zeile beginnt genau mit dem Wort, dann Doppelpunkt, dann Leerzeichen; die Vektorkomponenten sind durch Kommas ohne Leerzeichen getrennt:

**Eingabe** (Beispiel):

```
1,2,3
4,5,6
```

**Ausgabe** (Beispiel):

```
Skalarprodukt: 32
Kreuzprodukt: -3,6,-3
```

## Hintergrund

- **Skalarprodukt:** `a·b = ax*bx + ay*by + az*bz` — das Ergebnis ist eine **Zahl**.
- **Kreuzprodukt:** Das Ergebnis ist wieder ein **Vektor**:
  - `cx = ay*bz - az*by`
  - `cy = az*bx - ax*bz`
  - `cz = ax*by - ay*bx`

Interessant: Stehen beide Vektoren **parallel**, ist das Kreuzprodukt der Nullvektor — das zeigt dir Testfall `06-parallel`.

## Hinweise

- `std::cin >> x` liest eine Zahl bis zum nächsten Trennzeichen — das Komma wird **nicht** automatisch übersprungen und blockiert sonst das nächste Einlesen.
- Trick: Ein einzelnes `char` „schluckt“ das Komma:
  `std::cin >> x >> komma >> y >> komma >> z;`
- Bonus: `>>` überspringt Leerzeichen automatisch — deshalb funktioniert auch `1, 2, 3` als Eingabe (siehe Testfall `04-mit-leerzeichen`).
- Ausgabe des Vektors: `std::cout << cx << "," << cy << "," << cz;` — ohne Leerzeichen, genau wie in der Eingabe.

## So testest du

- `./trainer test eingabe/04` (oder in VSCodium Strg+Shift-B bzw. der 🧪-Button) — die Testfälle liegen sichtbar in `tests/`
- `./trainer run eingabe/04` — das Programm selbst ausprobieren
- Bei roten Tests: OpenCode fragen, z. B. „Warum schlägt mein Test fehl?“
