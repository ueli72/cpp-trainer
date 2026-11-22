# Struct 01 — Vektoren als struct

## Ziel

Zusammengehörige Werte bündeln: Mit einem eigenen Datentyp (`struct`) hörst du auf, lose Einzelvariablen zu verwalten — und die Stream-Eingabe landet direkt in den struct-Membern.

## Aufgabe

Definiere einen `struct Vector` mit drei `double`-Werten `x`, `y`, `z`.

Lies zwei Vektoren ein — **jeweils in einer eigenen Zeile**, im Format `x,y,z` (Kommazahlen, durch Kommas getrennt).

Berechne daraus das **Skalarprodukt** (eine Zahl) und das **Kreuzprodukt** (wieder ein Vektor) und gib beides mit **genau zwei Nachkommastellen** aus:

**Eingabe** (Beispiel):

```
1,2,3
4,5,6
```

**Ausgabe** (Beispiel):

```
Skalarprodukt: 32.00
Kreuzprodukt: -3.00,6.00,-3.00
```

## Hintergrund

Ein eigener Datentyp wird außerhalb von `main` deklariert (meist oben in der Datei):

```cpp
struct Vector {
    double x;
    double y;
    double z;
};
```

Auf die Werte greifst du mit dem Punkt zu: `a.x`, `a.y`, `a.z`.

Die Formeln kennst du aus Eingabe 04:

- **Skalarprodukt:** `a.x*b.x + a.y*b.y + a.z*b.z`
- **Kreuzprodukt:**
  - `c.x = a.y*b.z - a.z*b.y`
  - `c.y = a.z*b.x - a.x*b.z`
  - `c.z = a.x*b.y - a.y*b.x`

## Hinweise

- **Eingabe in den struct:** Erst Variablen anlegen (`Vector a, b;`), dann liest du direkt in die Member:
  ```cpp
  char komma;
  std::cin >> a.x >> komma >> a.y >> komma >> a.z;
  std::cin >> b.x >> komma >> b.y >> komma >> b.z;
  ```
  `>>` liest die Zahl bis zum nächsten Trennzeichen, das `char` „schluckt“ das Komma. Weil `>>` Leerzeichen automatisch überspringt, funktioniert auch `1.5, 2.5, -3` (siehe Testfall `04-mit-leerzeichen`).
- **Zwei Nachkommastellen:** `std::cout << std::fixed << std::setprecision(2) << wert;` — `std::setprecision` braucht `#include <iomanip>`. Einmal gesetzt, gilt die Formatierung für alle folgenden Ausgaben.
- **Vektor ausgeben:** `std::cout << c.x << "," << c.y << "," << c.z;` — Kommas ohne Leerzeichen, wie in der Eingabe.

## So testest du

- `./trainer test struct/01` (in der App: 🧪-Button) — die Testfälle liegen sichtbar in `tests/`
- `./trainer run struct/01` — das Programm selbst ausprobieren
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?“) oder OpenCode im Terminal fragen
