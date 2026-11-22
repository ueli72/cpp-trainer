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

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test struct/02`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run struct/02`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?“) oder OpenCode im Terminal fragen
