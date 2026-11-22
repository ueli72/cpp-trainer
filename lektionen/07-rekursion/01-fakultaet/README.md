# Rekursion 01 — Fakultät

## Ziel

Rekursion verstehen: eine Funktion, die sich selbst aufruft. Jede Rekursion hat zwei Teile — **Abbruchbedingung** (das kleinste Problem, direkt beantwortbar) und **rekursiven Schritt** (das Problem etwas kleiner machen).

## Aufgabe

Lies eine ganze Zahl `n` (0 bis 12) ein und gib ihre **Fakultät** aus: `n! = 1 · 2 · … · n`, mit `0! = 1`.

**Eingabe** (Beispiel):

```
5
```

**Ausgabe** (Beispiel):

```
Fakultaet: 120
```

## Wie du vorgehst

In `main.cpp` steht ein **komplettes Beispiel** — `potenz(b, e)` ist bereits rekursiv gelöst und erklärt. Deine Arbeit: `fakultaet(n)` nach demselben Muster bauen (zwei kleine TODOs).

Das Muster:

```
potenz(b, e):
    wenn e == 0:  liefere 1            ← Abbruchbedingung
    sonst:        liefere b * potenz(b, e - 1)   ← rekursiver Schritt
```

Für die Fakultät gilt dasselbe mit anderen Zahlen:

```
fakultaet(n):
    wenn n == 0:  liefere 1
    sonst:        liefere n * fakultaet(n - 1)
```

## Hinweise

- Der rekursive Aufruf arbeitet immer mit einem **kleineren** Problem (`n - 1`) — deshalb kommt die Rekursion irgendwann beim Abbruch an.
- Probier in Gedanken `fakultaet(3)`: 3 · fakultaet(2) → 3 · 2 · fakultaet(1) → 3 · 2 · 1 · fakultaet(0) → 3 · 2 · 1 · 1 = 6.
- `12!` ist die größte Fakultät, die in ein `int` passt — daher die Eingabegrenze.

## So testest du

- `./trainer test rekursion/01rekursion/01` (in der App: 🧪-Button) — die Testfälle liegen sichtbar in `tests/`
- `./trainer run rekursion/01rekursion/01` — das Programm selbst ausprobieren
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?“) oder OpenCode im Terminal fragen
