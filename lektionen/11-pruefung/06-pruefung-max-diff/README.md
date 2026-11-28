# Prüfungsfragen 06 — Prüfung 2022-08: max_difference

## Ziel

Die echte Prüfungsaufgabe: **„max_difference" (Exam 2022-08,
ITET MATH PHYS RW)** — im Original-Harness der Prüfung, mit
**Iterator-Paar `[begin, end)`** als Parameter. Vorstufe war
Prüfungsfragen 05.

## Aufgabe

In `functions.h` steht:

```cpp
int largest_difference(iterator begin, iterator end);
```

mit `using iterator = std::vector<int>::const_iterator;`. Implementiere
die Funktion: Sie gibt die **größte absolute Differenz zwischen zwei
benachbarten Zahlen** im Bereich `[begin, end)` zurück.

`main.cpp` (fertig) liest Zahlen bis `-1` und gibt aus:
`largest difference between two neighbouring numbers = |<wert>|`

**Eingabe** (Beispiel):

```
1 5 2 5 7 6 -1
```

**Ausgabe** (Beispiel):

```
Enter a sequence of non-negative numbers terminating with '-1'
largest difference between two neighbouring numbers = |4|
```

## Hinweise

- Bereich `[begin, end)`: `begin` zeigt aufs erste Element, `end` **hinter**
  das letzte — die Schleife läuft, solange `it + 1 != end`.
- Benachbart: `*it` und `*(it + 1)` — Differenz mit Absolutbetrag.
- PRE lesen: Werte in `[0, 2147483647]`, mindestens zwei Elemente —
  das ist in der Prüfung garantiert.
- Beispiele aus der Aufgabe: `[1, 5, 2, 5, 7, 6] → 4`, `[2, 9, 1] → 8`.

## Testen

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test pruefung/06`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run pruefung/06`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?") oder OpenCode im Terminal fragen
