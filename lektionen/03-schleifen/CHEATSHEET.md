# Cheatsheet — Schleifen

## for — wenn die Anzahl bekannt ist
```cpp
for (int i = 1; i <= 10; i = i + 1) {
    // läuft 10-mal: i = 1, 2, 3, …, 10
}
```
- Start (`i = 1`), Bedingung (`i <= 10`), Schritt (`i = i + 1`)
- `i = i + 1` ist dasselbe wie `i++`
- `i` ist nur **innerhalb** der Schleife sichtbar

## while — wenn das Ende von der Eingabe abhängt
```cpp
while (std::cin >> x) {          // läuft, solange Zahlen kommen
    if (x < 0) break;            // negatives x = Stoppsignal
    // … x verarbeiten …
}
```
`break` verlässt die Schleife sofort.

## while über einem schrumpfenden Wert
```cpp
while (zahl > 0) { … zahl = zahl / 10; … }   // stoppt, wenn zahl 0 ist
```

## do while — wenn er mindestens einmal laufen soll
```cpp
do {
    std::cin >> x;                 // erst handeln …
} while (x != 0);                  // … dann prüfen (Semikolon hinter while!)
```
- Die Prüfung kommt **nach** der ersten Runde — der Körper läuft garantiert mindestens einmal
- Typisch beim Einlesen: der erste Wert muss gelesen sein, BEVOR man ihn prüfen kann
- Während `while` vorher prüft (Eventuell 0 Runden), prüft `do while` hinterher (mindestens 1 Runde)

## Klassische Muster (immer dieselben drei Variablen)
| Zweck | Start | Je Runde |
|---|---|---|
| Summe | `int summe = 0;` | `summe = summe + x;` |
| Anzahl | `int anzahl = 0;` | `anzahl = anzahl + 1;` |
| Maximum | beim ersten Wert setzen | `if (x > maximum) maximum = x;` |

## Verschachtelte Schleifen (Sterntreppe)
```cpp
for (int i = 1; i <= n; i = i + 1) {   // Zeile i
    for (int j = 1; j <= i; j = j + 1) // i Sternchen
        std::cout << "*";
    std::cout << "\n";                 // Zeilenende
}
```
Die innere Schleife läuft **komplett durch** pro äußerer Runde.

## Formate der Lektionen (genau so ausgeben!)
```
3 * 7 = 21        29 * 12 = 348        * / ** / ***
Anzahl: 4         Summe: 100           Maximum: 42
```

## Testen
`./trainer test schleifen/01` … `./trainer test schleifen/09` — sichtbar in `tests/`
