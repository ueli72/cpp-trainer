# Zeiger 03 — Add (Original: Understanding Pointers 1b)

## Ziel

**Ausgaben über Zeiger**: Eine Funktion, die ihr Ergebnis nicht mit
`return` liefert, sondern in einen Speicher schreibt, den der Aufrufer
per Zeiger übergibt. Genau so war es in der Originalübung
**„Understanding Pointers — Add"**.

## Aufgabe

`main.cpp` (fertig) liest zwei Zahlen `a` und `b` und ruft auf:

```cpp
add(&res, &a, &b);
```

Du schreibst in `add.cpp` die Funktion `add` — sie addiert den Wert an
der Adresse `a` und den Wert an der Adresse `b` und schreibt das
Ergebnis an die Adresse `res`.

**Eingabe** (Beispiel):

```
12 30
```

**Ausgabe** (Beispiel):

```
42
```

> **Skelett:** In `add.cpp` steht der leere Funktionsrumpf.

## Hinweise

- `*a` ist der Wert an der Adresse `a` — die Summe gehört in `*res`.
- Vergleiche: in Zeiger 01 hast du Werte über Zeiger **vertauscht** —
  hier schreibst du einen Wert über einen Zeiger **zurück**.
- Warum geht das nicht mit `return`? Geht schon — aber in der Prüfung
  wird genau dieses „Call by Reference per Zeiger" verlangt.

## Testen

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test zeiger/03`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run zeiger/03`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?") oder OpenCode im Terminal fragen
