# Prüfungsfragen 02 — Prüfung 2022-02: Dezimal → beliebige Basis

## Ziel

Die echte Prüfungsaufgabe: **„Decimal to arbitrary base" (Exam 2022-02,
MAVT/ITET)** — im Original-Harness der Prüfung. Vorstufe war
Prüfungsfragen 01; die Technik ist genau dieselbe.

## Aufgabe

In `functions.h` steht die Funktion `convert_base(n, b)` mit PRE/POST —
implementiere sie: Sie gibt die Zahl `n` zur Basis `b` zurück, und zwar
als **eine Zahl, deren Dezimalziffern die Ziffern der Zielbasis sind**:

- `10 2` → `1010`
- `14 9` → `15`

`main.cpp` (fertig — musst du nicht lesen) liest `value` und `base` und
gibt aus: `convert_base = <wert>`.

**Eingabe** (Beispiel):

```
14 9
```

**Ausgabe** (Beispiel):

```
Enter a number to convert, followed by the base to convert it to
convert_base = 15
```

> Die erste Zeile ist der Eingabe-Prompt des Prüfungsprogramms — gehört
> mit zur Ausgabe! Genau daran siehst du in der Prüfung, wo dein Ergebnis
> steht (Markierung `|` in anderen Aufgaben).

## Hinweise

- Der Prüfungs-Trick aus Vorstufe 01: `ergebnis += stellenwert * (n % b);`
  `n /= b; stellenwert *= 10;` — solange `n > 0`.
- Sonderfall `n = 0` → `0`.
- PRE lesen: `n >= 0`, `1 < b < 10` — das ist in der Prüfung garantiert,
  du musst es nicht prüfen.

## Testen

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test pruefung/02`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run pruefung/02`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?") oder OpenCode im Terminal fragen
