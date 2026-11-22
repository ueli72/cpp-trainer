# Cheatsheet — Vektoren

## Grundlagen
```cpp
#include <vector>
std::vector<int> zahlen;        // leere Liste
zahlen.push_back(x);            // hinten anfügen
zahlen.size();                  // Anzahl der Elemente
zahlen[i];                      // i-tes Element (ab 0 gezählt!)
zahlen.back();                  // letztes Element
```

## Mit Startwerten
```cpp
std::vector<int> zahlen = {1, 2, 3};
```

## Durchlaufen
```cpp
for (int i = 0; i < int(zahlen.size()); i = i + 1) {
    // zahlen[i]
}
```
Achtung: `size()` ist vorzeichenlos — mit `int(...)` umwandeln, wenn du
mit `int`-Schleifenvariablen vergleichst.

## Lesen bis Dateiende (Strg+D)
```cpp
std::vector<int> zahlen;
int x;
while (std::cin >> x) {
    zahlen.push_back(x);
}
```

## Typische Muster
| Zweck | Muster |
|---|---|
| Summe | `int summe = 0; summe += zahlen[i];` |
| Minimum | mit dem ersten Element starten, dann vergleichen |
| Vorkommen zählen | `if (zahlen[i] == gesucht) anzahl += 1;` |

## Formate der Lektionen (genau so ausgeben!)
```
Anzahl: 5        Summe: 15        Minimum: 2        Maximum: 9
```

## Testen
`./trainer test vektoren/01` … — die Testfälle liegen sichtbar in `tests/`
