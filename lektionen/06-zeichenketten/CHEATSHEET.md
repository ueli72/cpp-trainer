# Cheatsheet — Zeichenketten

## Grundlagen
```cpp
#include <string>
std::string wort;           // leerer Text
std::string wort = "Hallo";
std::cin >> wort;           // liest EIN Wort (bis Leerzeichen/Enter)
std::getline(std::cin, wort);   // liest eine GANZE Zeile (mit Leerzeichen)
```

## Länge und Zeichen
| Ausdruck | Bedeutung |
|---|---|
| `wort.length()` | Anzahl der Zeichen |
| `wort[0]` | das erste Zeichen (ab 0 gezählt!) |
| `wort[wort.length() - 1]` | das letzte Zeichen |
| `wort[i]` | das i-te Zeichen — Typ: `char` |

Einzelne Zeichen stehen in **einfachen** Anführungszeichen: `'H'` —
Text in **doppelten**: `"H"`.

## Zeichen prüfen
```cpp
if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
    // c ist ein Vokal
}
```
Kurzform: `if (c == 'a' \|\| c == 'e' \|\| …)` — jedes Zeichen einzeln verglichen.

## Verketten und umdrehen
```cpp
std::string gruss = "Hallo, " + name + "!";   // Texte mit + verketten
rueckwaerts = c + rueckwaerts;                // Zeichen VORN anfügen = umdrehen
rueckwaerts = rueckwaerts + c;                // hinten anfügen = in der Reihenfolge bleiben
```

## Formate der Lektionen (genau so ausgeben!)
```
Laenge: 5        Erster: H        Letzter: o
Vokale: 2        Rueckwaerts: ollah
A3B2C1
```

## Testen
`./trainer test zeichenketten/01` … — die Testfälle liegen sichtbar in `tests/`
