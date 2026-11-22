# Schleifen 01 — Das Einmaleins

## Ziel

Die erste Schleife: dieselbe Ausgabe zehnmal mit fortlaufender Zahl wiederholen.

## Aufgabe

Lies eine Zahl `n` zwischen 1 und 10 ein.

Gib das kleine Einmaleins zu `n` aus — **10 Zeilen**, von `1` bis `10`. Jede Zeile hat das Format `i * n = i*n`:

**Eingabe** (Beispiel):

```
7
```

**Ausgabe** (Beispiel):

```
1 * 7 = 7
2 * 7 = 14
3 * 7 = 21
4 * 7 = 28
5 * 7 = 35
6 * 7 = 42
7 * 7 = 49
8 * 7 = 56
9 * 7 = 63
10 * 7 = 70
```

## Hinweise

- Eine `for`-Schleife von 1 bis 10: `for (int i = 1; i <= 10; ++i) { … }`
- In der Schleife einfach ausgeben: `i`, `" * "`, `n`, `" = "`, `i * n`, Zeilenumbruch.

## So testest du

- `./trainer test schleifen/01` (in der App: 🧪-Button) — die Testfälle liegen sichtbar in `tests/`
- `./trainer run schleifen/01` — das Programm selbst ausprobieren
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?“) oder OpenCode im Terminal fragen
