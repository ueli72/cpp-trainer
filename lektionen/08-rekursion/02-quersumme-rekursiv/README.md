# Rekursion 08 — Quersumme (rekursiv)

## Ziel

Rekursion selbst schreiben: Die Quersumme aus Ziffern-Reihe (Ziffern 01) als rekursive Funktion — ohne Schleife.

## Aufgabe

Lies eine nicht-negative ganze Zahl `n` ein und gib ihre **Quersumme** (Summe aller Ziffern) aus — diesmal **rekursiv**:

**Eingabe** (Beispiel):

```
123
```

**Ausgabe** (Beispiel):

```
Quersumme: 6
```

## Das Muster

```
quersumme(n):
    wenn n == 0:  liefere 0                      ← Abbruchbedingung
    sonst:        liefere n % 10 + quersumme(n / 10)   ← rekursiver Schritt
```

In Worten: die letzte Ziffer (`n % 10`) plus die Quersumme des Rests (`n / 10`). Bei `123`: 3 + quersumme(12) → 3 + 2 + quersumme(1) → 3 + 2 + 1 + quersumme(0) → 3 + 2 + 1 + 0 = 6.

> **Skelett:** In `main.cpp` steht schon ein Teil — den Rest ergänzt du an den `TODO`-Stellen.

## Hinweise

- Beide Werkzeuge kennst du aus Ziffern 01: `n % 10` ist die letzte Ziffer, `n / 10` der Rest.
- Der Abbruch ist hier **natürlich**: irgendwann ist `n` 0 — dann ist die Quersumme der leeren Zahl 0.
- Die Funktion braucht einen Namen und zwei feste Teile: `if` für den Abbruch, sonst der rekursive Aufruf. Keine Schleife nötig!

## So testest du

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test rekursion/08`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run rekursion/02`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?“) oder OpenCode im Terminal fragen
