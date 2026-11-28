# Cheatsheet — Prüfungsfragen

## Die 4 Klausuraufgaben in dieser Gruppe

| Lektion | Prüfung | Thema | Vorstufe |
|---|---|---|---|
| 02 | Exam 2022-02 (MAVT/ITET) | Dezimal → beliebige Basis | 01 |
| 04 | Exam 2019-02 (RW) | Number Pairs with Sum (Iteratoren) | 03 |
| 06 | Exam 2022-08 (ITET MATH PHYS RW) | max_difference (Iteratoren) | 05 |
| 08 | Exam 2023-01 (MAVT) | Binary Tree Depth (Rekursion) | 07 |

## Prüfungs-Strategie

1. **PRE/POST genau lesen** — was ist garantiert (musst du nicht prüfen),
   was wird verlangt (Randfälle!).
2. **Harness ignorieren**: „You most likely don't need to read and
   understand this file" — nur die eigene Funktion schreiben.
3. **Markierungen `|…|`**: dein Ergebnis wird zwischen Markern gedruckt —
   bei Fehlern in den automatischen Tests lohnt der Blick auf die
   exakte Ausgabe (Groß-/Kleinschreibung, Leerzeichen).
4. **Erst die Vorstufe**: wenn eine Prüfungslektion klemmt, die zugehörige
   Vorstufe davor wiederholen.

## Zahlensysteme (Prüfung 2022-02)

```cpp
int convert_base(int n, int b) {
  int result = 0, stellenwert = 1;
  while (n != 0) {
    result += stellenwert * (n % b);   // letzte Ziffer an die richtige Stelle
    n /= b;
    stellenwert *= 10;
  }
  return result;
}
```

## Iteratoren (Prüfung 2019-02 / 2022-08)

```cpp
using iterator = std::vector<int>::const_iterator;
// iterator ~ Zeiger: *it = Wert, ++it / it + 1 = weiter, it != end = Ende
for (iterator it = begin; it != end; ++it) { /* *it */ }
// benachbart: *it und *(it + 1) — es gilt it + 1 != end
```

## Binärbäume (Prüfung 2023-01)

```cpp
// Knoten zaehlen:        1 + f(links) + f(rechts)
// Tiefe bestimmen:       1 + max(f(links), f(rechts))
int f(TreeNode* node) {
  if (node == nullptr) return 0;   // leerer Teilbaum — IMMER zuerst
  return 1 + std::max(f(node->left), f(node->right));
}
```
Klammer-Notation: `Wurzel(links)(rechts)`, leerer Teilbaum `()`,
einzelner Knoten `3`.

## Denk-Fallen

- `i < j` beim Paare-Zählen: die innere Schleife startet bei `i + 1`.
- Absolutbetrag bei Differenzen (`std::abs` oder manuell negieren).
- Rekursionsabbruch zuerst — sonst Absturz (segfault).
- `assert` in Vorbedingungen: für den **ersten** Aufruf; in der Rekursion
  selbst auf `nullptr` prüfen.

## Testen
`./trainer test pruefung/01` … `./trainer run pruefung/08` — Testfälle sichtbar in `tests/`
