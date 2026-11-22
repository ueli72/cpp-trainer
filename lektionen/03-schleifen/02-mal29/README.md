# Schleifen 02 — Mal 29 — nur mit Addition

## Ziel

Werte in Variablen zwischenspeichern und gezielt kombinieren — wie in der Originalübung „Multiply with 29“.

## Aufgabe

Lies **eine ganze Zahl** `a` ein.

Berechne `29 * a`, aber **ohne den Multiplikationsoperator `*`** — nur mit Additionen.

Gib dann aus:

**Eingabe** (Beispiel):

```
12
```

**Ausgabe** (Beispiel):

```
29 * 12 = 348
```

> **Skelett:** In `main.cpp` steht schon ein Teil — den Rest ergänzt du an den `TODO`-Stellen.

## Hinweise

- Verdopple `a` Schritt für Schritt: `2a`, `4a`, `8a`, `16a` — das sind lauter Additionen.
- Und `29 = 16 + 8 + 4 + 1`. Addiere also `16a + 8a + 4a + a`.
- Funktioniert auch mit negativen `a` — da änderst du nichts.

## So testest du

- `./trainer test schleifen/02` (oder in VSCodium Strg+Shift-B bzw. der 🧪-Button) — die Testfälle liegen sichtbar in `tests/`
- `./trainer run schleifen/02` — das Programm selbst ausprobieren
- Bei roten Tests: OpenCode fragen, z. B. „Warum schlägt mein Test fehl?“
