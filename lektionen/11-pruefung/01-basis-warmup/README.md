# Prüfungsfragen 01 — Zahlensysteme: Vorstufe zur Prüfung 2022-02

## Ziel

Die Prüfungsaufgabe **„Decimal to arbitrary base" (Exam 2022-02, MAVT/ITET)**
in zwei kleinen Schritten vorbereitet — erst die Ziffern, dann das
Zusammenbauen. Wie du Zahlensysteme generell umrechnest, kennst du aus
Ziffern 04 und Rekursion 03 — hier lernst du den **Prüfungs-Trick**: die
Ziffern als **eine einzige Zahl** zurückgeben.

## Aufgabe

Lies zwei ganze Zahlen ein: `n` (≥ 0) und `b` (2–9), getrennt durch
Leerzeichen. Das Skelett hat zwei TODOs:

1. **TODO 1:** Gib die Ziffern von `n` zur Basis `b` in der Reihenfolge
   aus, in der man sie ableitet: immer `n % b` (letzte Ziffer), dann
   `n /= b` — solange `n > 0`.
2. **TODO 2:** Baue die Ziffern zu **einer Zahl** zusammen — mit zwei
   Hilfsvariablen `ergebnis` (Start 0) und `stellenwert` (Start 1):
   `ergebnis += stellenwert * (n % b); n /= b; stellenwert *= 10;`

**Eingabe** (Beispiel):

```
14 9
```

**Ausgabe** (Beispiel):

```
Ziffern (von hinten): 5 1
Als Zahl: 15
```

## Hinweise

- `14 % 9 = 5`, `14 / 9 = 1`, `1 % 9 = 1` — deshalb `5 1`.
- „Als Zahl": `5 + 1·10 = 15` — der `stellenwert` wandert 1, 10, 100, …
- **Achtung:** TODO 1 verkleinert `n` schon — für TODO 2 nimm eine
  **Kopie** von `n`.
- Sonderfall `n = 0`: keine Ziffer — die Schleifen laufen nie, „Als Zahl: 0".
- Genau diese Technik verlangt die Prüfungsaufgabe in **Prüfungsfragen 02**.

## Testen

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test pruefung/01`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run pruefung/01`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?") oder OpenCode im Terminal fragen
