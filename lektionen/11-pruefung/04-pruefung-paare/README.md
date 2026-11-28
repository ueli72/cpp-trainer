# Prüfungsfragen 04 — Prüfung 2019-02: Number Pairs with Sum

## Ziel

Die echte Prüfungsaufgabe: **„Number Pairs with Sum" (Exam 2019-02, RW)**
— im Original-Harness der Prüfung, mit **Iteratoren** statt Indizes.
Vorstufe war Prüfungsfragen 03.

## Aufgabe

In `pair_sum.h`/`pair_sum.cpp` steht:

```cpp
int pairs_with_sum(int sum, iterator begin, iterator end);
```

`iterator` ist ein `std::vector<int>::const_iterator`. Implementiere die
Funktion: Sie zählt die Paare von **Indizes** `i < j` des Vektors, deren
Summe genau `sum` ergibt.

`main.cpp` (fertig) liest eine Zeile: zuerst die Zielsumme, dann die
Zahlen — und gibt aus: `number of pairs with sum <sum>: <anzahl>`.

**Eingabe** (Beispiel):

```
8 1 7 2 6 6
```

**Ausgabe** (Beispiel):

```
number of pairs with sum 8: 3
```

## Hinweise

- Iteratoren wie Zeiger behandeln: `*begin` ist der Wert, `begin + 1`
  oder `++it` geht weiter, zwei Iteratoren `it != end` vergleichen.
- Doppel-Schleife aus Vorstufe 03 — nur mit Iteratoren:
  für `it1` von `begin` bis `end`, für `it2` von `it1 + 1` bis `end`.
- Die Bedingung `i < j` steckt im Start von `it2` bei `it1 + 1`.
- PRE (steht in der Datei): die Summen passen in ein `int` — kein
  Überlauf nötig.

## Testen

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test pruefung/04`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run pruefung/04`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?") oder OpenCode im Terminal fragen
