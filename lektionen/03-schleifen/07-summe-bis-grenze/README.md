# Schleifen 07 — Summe bis zur Grenze

## Ziel

`while`, wenn **vorher niemand weiß**, wie viele Runden es werden — die Schleife endet, weil ein Wert im Inneren eine Grenze überschreitet.

## Aufgabe

Lies eine Zahl `n` zwischen 1 und 1.000.000 ein.

Addiere der Reihe nach `1 + 2 + 3 + …` — **genau so lange, bis die Summe mindestens `n` ist**. Gib aus, wie viele Summanden dafür nötig waren (nur die Zahl, sonst nichts):

**Eingabe** (Beispiel):

```
10
```

**Ausgabe** (Beispiel):

```
4
```

(weil `1 + 2 + 3 + 4 = 10` — nach 4 Summanden ist die Grenze erreicht)

## Hinweise

- Zwei Variablen: `summe = 0` und `k = 0` (der nächste Summand).
- Solange `summe < n`: zuerst `k` um 1 erhöhen (das ist der nächste Summand), dann `summe = summe + k`.
- Die Schleife stoppt **mitten im Aufaddieren** — deshalb `while` und kein `for` mit fester Grenze.
- Grenzfall: bei `n = 1` reicht schon der erste Summand → Ausgabe `1`.
- Achte darauf, dass du genau die **kleinste** Anzahl nimmst, die `n` erreicht oder übersteigt (`>=` zählt als „erreicht“).

## So testest du

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test schleifen/07`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run schleifen/07`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?“) oder OpenCode im Terminal fragen
