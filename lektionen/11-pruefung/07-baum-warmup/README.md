# Prüfungsfragen 07 — Binärbäume: Vorstufe zur Prüfung 2023-01

## Ziel

Die Prüfungsaufgabe **„Binary Tree Depth" (Exam 2023-01, MAVT)**
vorbereitet: derselbe Prüfungs-Harness mit Binärbäumen in
Klammer-Notation — aber zuerst zählst du nur die **Knoten**. Das
Rekursionsmuster ist dasselbe.

## Aufgabe

In `binary_tree.h` steht:

```cpp
int count_nodes(TreeNode* node);
```

Implementiere sie: Sie zählt die **Knoten** im Baum ab `node` —
rekursiv über die zwei Kinder. `node` kann `nullptr` sein (leerer
Teilbaum) — dann ist die Antwort 0.

`main.cpp` (fertig — musst du nicht lesen) baut aus der Klammer-Notation
den Baum auf. Das Format: `Wurzel(linker Teilbaum)(rechter Teilbaum)`,
leere Teilbäume als `()`.

**Eingabe** (Beispiel):

```
7(5(2)(4))(9)
```

**Ausgabe** (Beispiel):

```
Enter a binary tree in bracket notation:
Number of nodes = |5|
```

Der Beispielbaum:

```
      7
     / \
    5   9
   / \
  2   4
```

## Hinweise

- Rekursionsmuster: `count(node) = 1 + count(node->left) + count(node->right)`
  — **vor** dem Zugriff prüfen: `if (node == nullptr) return 0;`
- Zugriff auf Kinder mit `node->left` und `node->right` (Pfeil-Operator,
  weil `node` ein Zeiger ist).
- In **Prüfungsfragen 08** zählst du statt der Knoten die **Tiefe** —
  mit `std::max` statt `+` beim Zusammenführen.

## Testen

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test pruefung/07`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run pruefung/07`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?") oder OpenCode im Terminal fragen
