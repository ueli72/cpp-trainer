# Klasse 03 — Klasse in eigene Dateien

## Ziel

Projektstruktur wie in der Praxis: **Deklaration** (Vector.h) und **Implementierung** (Vector.cpp) trennen — `main.cpp` wird dünn und macht nur noch Eingabe, Operator-Aufruf und Ausgabe.

## Aufgabe

Wie in Klasse 02, nur diesmal wohnt die Klasse in **zwei eigenen Dateien**, die du komplett selbst baust — `Vector.h` und `Vector.cpp` liegen als Kommentar-Stubs bereit:

- `Vector.h` — nur *was* die Klasse kann: Include-Guard, `class Vector` mit den Membern und den Deklarationen (jede endet mit `;`)
- `Vector.cpp` — *wie* sie es tut: `#include "Vector.h"` und die Implementierungen mit dem Scope-Operator (`double Vector::operator*(Vector other) { … }`)
- `main.cpp` — dünn bleiben lassen: Eingabe, ein `a * b`, eine Ausgabezeile

**Eingabe** (Beispiel):

```
1,2,3
4,5,6
```

**Ausgabe** (Beispiel):

```
Skalarprodukt: 32.00
```

## Hintergrund (aus Klasse 01/02)

- `#include "Vector.h"` fügt den Inhalt an dieser Stelle ein — eigene Dateien in `"…"`, die Standardbibliothek in `<…>`.
- **Include-Guard:** `#ifndef VECTOR_H` / `#define VECTOR_H` / `#endif` verhindert doppeltes Einfügen.
- **Deklaration vs. Definition:** die `.h` sagt *was*, die `.cpp` sagt *wie*.
- **Der Scope-Operator `::`:** `double Vector::operator*(Vector other)` heißt „`operator*` **der** Klasse Vector“.
- Der `trainer` kompiliert automatisch **alle** `.cpp`-Dateien einer Lektion und linkt sie zusammen.

## Hinweise

- Formel: `x*other.x + y*other.y + z*other.z`
- **Beim ersten Kompilieren eine Warnung?** `unused parameter 'other'` ist solange normal, wie die Methode noch leer ist — sie verschwindet, sobald du `other` benutzt.

## So testest du

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test klasse/03`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run klasse/03`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?“) oder OpenCode im Terminal fragen
