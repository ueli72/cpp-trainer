# Cheatsheet — Zeiger

## Die zwei Operatoren

```cpp
int x = 42;
int* p = &x;    // p speichert die ADRESSE von x  (& = Adresse von)
std::cout << *p;   // 42  (* = Wert an der Adresse, "Dereferenzieren")
*p = 7;            // schreibt 7 in x — über die Adresse!
```

## Zeiger als Funktionsparameter

```cpp
void add(int* res, const int* a, const int* b) {
    *res = *a + *b;      // Ergebnis landet beim AUFRUFER
}
// Aufruf:
add(&res, &a, &b);       // & übergibt die Adressen
```

Normale Parameter sind **Kopien** — Änderungen kommen nicht zurück.
Zeiger-Parameter erlauben „Call by Reference": nur so können Funktionen
mehrere Ergebnisse liefern oder Werte des Aufrufers ändern (vertauschen!).

## Zeiger auf Vektor-Elemente

```cpp
const int* p = &vec[i];       // Adresse des i-ten Elements
const int* q = vec.data() + i; // identisch: Zeiger-Arithmetik
```

## Verkettete Liste / Dynamische Queue

```cpp
struct Node {
    Node(const int _value, Node* _next) : value(_value), next(_next) { }
    const int value;
    Node* next;
};
```

- **enqueue** (hinten anhängen): `Node* n = new Node(value, nullptr);`
  bei leerer Queue `first` und `last` beide auf `n`, sonst
  `last->next = n; last = n;`
- **dequeue** (vorne entnehmen): Wert merken, `first = first->next;`,
  alten Knoten `delete`n — am Schluss: `last = nullptr` nicht vergessen.
- **Invariante:** `first == nullptr` genau dann, wenn `last == nullptr`.
- **Rückwärts drucken** (Rekursions-Trick wie bei Zahlensystemen):
  ```cpp
  void print_node_reverse(Node* n) {
      if (n != nullptr) {
          print_node_reverse(n->next);   // ERST weiterlaufen …
          std::cout << " " << n->value;  // … DANN ausgeben
      }
  }
  ```

## Denk-Fallen

- `p` ist die **Adresse**, `*p` der **Wert** — `std::cout << p` gibt keine Zahl aus.
- Zeiger in Funktionen sind lokale **Kopien**: `a = b;` im Funktionskörper
  ändert nur die Kopie — `*a = *b;` ändert den Wert draußen.
- `new` ohne `delete` = Speicherleck; Zeiger auf lokale Variablen
  zurückgeben = undefiniertes Verhalten.

## Testen
`./trainer test zeiger/01` … `./trainer run zeiger/05` — Testfälle sichtbar in `tests/`
