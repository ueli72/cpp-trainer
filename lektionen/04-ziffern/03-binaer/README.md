# Ziffern 03 — Binärdarstellung

## Ziel

Bits und Schiebeoperatoren — der Vorgeschmack auf die Klausuraufgabe „Binary Expansion“.

## Aufgabe

Lies **eine ganze Zahl zwischen 0 und 255** ein.

Gib ihre Binärdarstellung aus — immer mit **genau 8 Stellen** (mit führenden Nullen):

**Eingabe** (Beispiel):

```
5
```

**Ausgabe** (Beispiel):

```
00000101
```

> **Skelett:** In `main.cpp` steht schon ein Teil — den Rest ergänzt du an den `TODO`-Stellen.

## Hinweise

- Bit `i` einer Zahl ist `(zahl >> i) % 2`.
- Geh in einer Schleife von Bit 7 runter bis Bit 0 und gib jedes Bit aus — ohne Zeilenumbruch dazwischen.
- Erst am Ende ein `\n` ausgeben.

## So testest du

- `./trainer test ziffern/03` (oder in VSCodium Strg+Shift-B bzw. der 🧪-Button) — die Testfälle liegen sichtbar in `tests/`
- `./trainer run ziffern/03` — das Programm selbst ausprobieren
- Bei roten Tests: OpenCode fragen, z. B. „Warum schlägt mein Test fehl?“
