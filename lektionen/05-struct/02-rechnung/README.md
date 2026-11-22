# Struct 02 — Kassenbon

## Ziel

Structs selbst aufbauen: zusammengehörige Werte eines Typs (Preis + Stückzahl) bündeln, zweimal einlesen und verrechnen.

## Aufgabe

Definiere ein `struct Posten` mit zwei Membern: `double preis` und `int anzahl`.

Lies zwei Posten ein — **jeweils in einer eigenen Zeile**: zuerst der Preis, dann die Stückzahl, getrennt durch Leerzeichen.

Gib die **Summe aller Posten** (Preis × Stückzahl, aufsummiert) mit **genau zwei Nachkommastellen** aus:

**Eingabe** (Beispiel):

```
3.50 2
4.25 3
```

**Ausgabe** (Beispiel):

```
Gesamt: 19.75
```

## Hintergrund (aus Struct 01)

- `struct Posten { double preis; int anzahl; };` — der Typ wird außerhalb von `main` deklariert.
- Zwei Objekte anlegen: `Posten p1, p2;` — zugreifen mit dem Punkt: `p1.preis`, `p1.anzahl`.
- Einlesen mit `>>`: `std::cin >> p1.preis >> p1.anzahl;` — Leerzeichen überspringt `>>` automatisch.

> **Skelett:** In `main.cpp` steht schon ein Teil — den Rest ergänzt du an den `TODO`-Stellen.

## Hinweise

- Gesamt = `p1.preis * p1.anzahl + p2.preis * p2.anzahl`
- Zwei Nachkommastellen: `std::cout << std::fixed << std::setprecision(2);` (aus `<iomanip>`)
- Stückzahl 0 ist erlaubt (der Posten kostet dann nichts).

## So testest du

- `./trainer test struct/02struct/02` (oder in VSCodium Strg+Shift-B bzw. der 🧪-Button) — die Testfälle liegen sichtbar in `tests/`
- `./trainer run struct/02struct/02` — das Programm selbst ausprobieren
- Bei roten Tests: OpenCode fragen, z. B. „Warum schlägt mein Test fehl?“
