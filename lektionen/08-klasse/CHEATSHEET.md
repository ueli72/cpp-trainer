# Cheatsheet — Klassen, Operatoren, Header-Dateien

## class vs. struct
`struct`: alles ist öffentlich. `class`: alles ist **privat** (von außen
unsichtbar), bis du es mit `public:` freigibst.

## Methoden
```cpp
class Vector {
public:
    double x;  double y;  double z;
    void liesVonEingabe();           // Deklaration: WAS
    double operator*(Vector other);  // a * b
};
```
- **In einer Methode** greifst du direkt auf die Member zu: `x` statt `a.x`
  (sie gehören zum Objekt, mit dem die Methode aufgerufen wurde:
  `a.liesVonEingabe();` füllt `a`).
- Aufruf: `a.methode(b);` — `a` ist das Objekt, `b` der Parameter `other`.

## Operator überladen
`a * b` ist **exakt dasselbe** wie `a.operator*(b)`.
Der Operator **liefert** sein Ergebnis (`return`) — das Ausgeben
übernimmt `main`. Nur vorhandene Symbole überladbar (kein `×`).

## Header-Dateien: WAS / WIE trennen
| Datei | Inhalt |
|---|---|
| `Vector.h` | Deklarationen + **Include-Guard**: `#ifndef VECTOR_H` / `#define VECTOR_H` / `#endif` |
| `Vector.cpp` | Definitionen mit Scope-Operator: `double Vector::operator*(Vector other) { … }` |
| `main.cpp` | dünn: `#include "Vector.h"`, Eingabe, `a * b`, Ausgabe |

- `"…"` = eigene Dateien · `<…>` = Standardbibliothek
- Deklaration endet mit `;` — Definition hat den Körper `{ … }`
- Der `trainer` kompiliert **alle** `.cpp` einer Lektion und linkt sie.

## Formatierung
| Code | Wirkung |
|---|---|
| `std::fixed << std::setprecision(2)` | 2 Nachkommastellen (aus `<iomanip>`) |
| `std::setfill('0') << std::setw(2)` | 2-stellig mit führenden Nullen |

**Falle:** `setw` gilt nur für die **nächste** Ausgabe — vor jeder
Komponente wiederholen. `setfill` bleibt gesetzt.

## Der Rest-Operator `%`
`95 % 60` ist `35` — z. B. Minuten: `minuten % 60`, Mitternacht:
`stunde = total / 60 % 24`.

## Formate der Lektionen (genau so ausgeben!)
```
Skalarprodukt: 32.00        Summe: 16:35        00:20
```

## Testen
`./trainer test klasse/01` … `./trainer run klasse/04` — sichtbar in `tests/`
