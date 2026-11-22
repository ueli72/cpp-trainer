# Schleifen 03 — Sterntreppe

## Ziel

Verschachtelte Schleifen: eine äußere Schleife für die Zeilen, eine innere für die Zeichen.

## Aufgabe

Lies eine Zahl `n` zwischen 1 und 20 ein.

Gib eine „Treppe“ aus **n Zeilen** aus: In Zeile `i` stehen genau `i` Sternchen `*` (keine Leerzeichen):

**Eingabe** (Beispiel):

```
4
```

**Ausgabe** (Beispiel):

```
*
**
***
****
```

> **Skelett:** In `main.cpp` steht schon ein Teil — den Rest ergänzt du an den `TODO`-Stellen.

## Hinweise

- Äußere Schleife: `for (int i = 1; i <= n; ++i)`
- Innere Schleife: `for (int j = 1; j <= i; ++j)` — gibt jeweils ein `*` ohne Zeilenumbruch aus.
- Erst **nach** der inneren Schleife den Zeilenumbruch ausgeben.

## So testest du

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test schleifen/03`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run schleifen/03`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?“) oder OpenCode im Terminal fragen
