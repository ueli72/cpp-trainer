# Zeiger 02 — Lookup (Original: Understanding Pointers 1a)

## Ziel

Ein Zeiger auf ein Element im Vektor: `&vec[i]` ist die Adresse des
i-ten Elements. Genau so war es in der Originalübung
**„Understanding Pointers — Lookup"**.

## Aufgabe

Die Datei `main.cpp` (fertig — musst du nicht ändern) liest:

1. `length` — wie viele Zahlen folgen
2. `length` ganze Zahlen → werden in einen `std::vector<int>` gelegt
3. `index` — welcher Wert gesucht ist

Du schreibst in `lookup.cpp` die Funktion `lookup(vec, i)`, die die
**Adresse des i-ten Elements** zurückgibt. `main` gibt den Wert über
diesen Zeiger aus (`*lookup(vec, index)`).

**Eingabe** (Beispiel):

```
5
10 20 30 40 50
2
```

**Ausgabe** (Beispiel):

```
30
```

> **Skelett:** In `lookup.cpp` steht der Rumpf — vor der Lösung gibt
> `lookup` `nullptr` zurück und das Programm stürzt beim Dereferenzieren ab.

## Hinweise

- Zwei Möglichkeiten: `return &vec[i];` oder Zeiger-Arithmetik:
  `return vec.data() + i;`
- `lookup.h` enthält die Deklaration mit PRE/POST — die gehört zur
  Aufgabe dazu (in der Prüfung musst du PRE/POST genau lesen).
- Der Parameter ist `const std::vector<int>&` — deshalb kommt der
  Rückgabezeiger als `const int*` zurück (nur Lesen erlaubt).

## Testen

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test zeiger/02`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run zeiger/02`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?") oder OpenCode im Terminal fragen
