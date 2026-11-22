# Cheatsheet — Eingabe & Ausgabe

## Grundgerüst
```cpp
#include <iostream>
int main() {
    // dein Code
    return 0;
}
```

## Ausgabe mit `cout`
| Code | Wirkung |
|---|---|
| `std::cout << "Text";` | gibt Text aus |
| `std::cout << zahl;` | gibt den Wert einer Variable aus |
| `"\n"` | Zeilenumbruch am Zeilenende |
| Mehreres: einfach mehrfach `<<` verketten |

## Variablen
`int` Ganzzahl · `double` Kommazahl · `std::string` Text (aus `<string>`)

## Eingabe mit `cin`
```cpp
std::cin >> zahl;      // liest bis Leerzeichen/Enter
std::cin >> a >> b;    // zwei Werte in einer Zeile (2 5)
std::cin >> name;      // liest EIN Wort (kein Leerzeichen im Namen!)
```

## Trennzeichen-Trick
Bei `1,2,3`, `3/4`, `13:45` stoppt `>>` am Trennzeichen — ein `char` schluckt es:
```cpp
char komma;
std::cin >> x >> komma >> y;    // liest 1,2
```
`>>` überspringt Leerzeichen automatisch → `1, 2, 3` funktioniert auch.

## Rechnen
- `+ - * /` — **Achtung Ganzzahldivision:** `7 / 2` ist `3`, aber `7 / 2.0` ist `3.5`
- `%` = Rest der Division: `7 % 2` ist `1`

## Nachkommastellen (aus `<iomanip>`)
```cpp
std::cout << std::fixed << std::setprecision(2) << wert;   // 2 Stellen
```

## Text verketten
`"Hallo, " + name + "!"` — Texte mit `+` zusammensetzen.

## Formate der Lektionen (genau so ausgeben!)
```
Summe: 30          Produkt: 200        Durchschnitt: 2.00
Skalarprodukt: 32  Kreuzprodukt: -3,6,-3
```

## Formeln für Eingabe 04 (Vektorprodukte)
```
Skalarprodukt = ax*bx + ay*by + az*bz        (eine Zahl)
cx = ay*bz - az*by    cy = az*bx - ax*bz    cz = ax*by - ay*bx
```

## Testen
`./trainer test eingabe/01` … `./trainer run eingabe/04` — Testfälle stehen sichtbar in `tests/`
