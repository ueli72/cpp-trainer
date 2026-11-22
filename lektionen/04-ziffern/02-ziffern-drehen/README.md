# Ziffern 02 — Ziffern drehen

## Ziel

Ziffernzerlegung (Ziffern 01) gezielt anwenden — wie in der Originalübung „Reverse Digits“.

## Aufgabe

Lies **eine nicht-negative ganze Zahl** ein.

Gib die Zahl mit **umgedrehten Ziffernfolge** aus. Führende Nullen fallen dabei weg:

**Eingabe** (Beispiel):

```
12345
```

**Ausgabe** (Beispiel):

```
54321
```

> **Skelett:** In `main.cpp` steht schon ein Teil — den Rest ergänzt du an den `TODO`-Stellen.

## Hinweise

- Baue die neue Zahl in einer Schleife auf: `ergebnis = ergebnis * 10 + n % 10;`
- Danach Ziffer abschneiden: `n /= 10;` — solange `n > 0`.
- Bei der `1200` entsteht `0021` → ausgegeben wird `21`, weil führende Nullen bei einer Zahl wegfallen.

## So testest du

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test ziffern/02`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run ziffern/02`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?“) oder OpenCode im Terminal fragen
