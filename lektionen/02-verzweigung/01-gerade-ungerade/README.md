# Verzweigung 01 — Gerade oder ungerade

## Ziel

Den Modulo-Operator kennen lernen und mit `if/else` Entscheidungen treffen.

## Aufgabe

Lies **eine ganze Zahl** ein.

Gib danach genau eines der beiden Wörter aus:

- `gerade` — wenn die Zahl durch 2 teilbar ist
- `ungerade` — wenn nicht

Das gilt auch für negative Zahlen und für die 0: Die 0 ist gerade, `-3` ist ungerade.

**Eingabe** (Beispiel):

```
7
```

**Ausgabe** (Beispiel):

```
ungerade
```

## Hinweise

- `n % 2` ergibt den Rest der Division durch 2 — bei geraden Zahlen ist er `0`.
- Ein einfaches `if / else` reicht: zwei Zweige, zwei Ausgaben.

## So testest du

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test verzweigung/01`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run verzweigung/01`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?“) oder OpenCode im Terminal fragen
