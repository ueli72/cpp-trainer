# Prüfungsfragen 08 — Prüfung 2023-01: Binary Tree Depth

## Ziel

Die echte Prüfungsaufgabe: **„Binary Tree Depth" (Exam 2023-01, MAVT)**
— im Original-Harness der Prüfung. Vorstufe war Prüfungsfragen 07; das
Rekursionsmuster ist dasselbe, nur das Zusammenführen ist eine Maximum-
statt einer Summenbildung.

## Aufgabe

In `binary_tree.h` steht:

```cpp
int get_max_depth(TreeNode *node);
```

Implementiere sie: Sie gibt die **maximale Tiefe** des Baums ab `node`
zurück — die Anzahl Knoten des längsten Pfads von der Wurzel zu einem
Blatt.

`main.cpp` (fertig) baut den Baum aus der Klammer-Notation
`Wurzel(links)(rechts)` auf und gibt aus:
`Maximal depth of the binary tree = |<tiefe>|`

**Eingabe** (Beispiel):

```
7(5(2)(4))(9)
```

**Ausgabe** (Beispiel):

```
Enter a binary tree in bracket notation:
Maximal depth of the binary tree = |3|
```

Beispiele aus der Aufgabe: ein einzelner Knoten → Tiefe 1;

```
      5
     / \
    2   7     → Tiefe 3
       /
      4
```

(Notation: `5(2)(7(4))`)

## Hinweise

- Rekursionsmuster wie beim Knotenzählen — nur mit Maximum:
  `1 + max(tiefe(links), tiefe(rechts))` (Header `<algorithm>` oder
  eigenes max).
- **nullptr ist der Normalfall**: die Kinder eines Blatts sind immer
  `nullptr` — leere Teilbäume haben Tiefe 0.
- Das `assert(node != nullptr)` im Skelett prüft die **VORBEDINGUNG**
  für den ersten Aufruf. In der Rekursion musst du selbst auf `nullptr`
  prüfen — das assert darfst du dafür entfernen oder umbauen.
- Wurzel allein zählt als Tiefe **1** (nicht 0).

## Testen

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test pruefung/08`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run pruefung/08`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?") oder OpenCode im Terminal fragen
