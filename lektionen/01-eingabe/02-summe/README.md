# Eingabe 02 — Summe und Produkt

## Ziel

Zahlen sicher einlesen, berechnen und in einem exakten Format wieder ausgeben — der Grundschritt jeder Konsolenaufgabe.

## Aufgabe

Lies zwei ganze Zahlen `a` und `b` ein (in einer Zeile, durch Leerzeichen getrennt).

Gib anschließend ihre **Summe** und ihr **Produkt** aus — jede Zeile beginnt genau mit dem Wort, dann Doppelpunkt, dann Leerzeichen:

**Eingabe** (Beispiel):

```
10 20
```

**Ausgabe** (Beispiel):

```
Summe: 30
Produkt: 200
```

> **Skelett:** In `main.cpp` steht schon ein Teil — den Rest ergänzt du an den `TODO`-Stellen.

## Hinweise

- `std::cin >> a >> b;` liest beide Zahlen hintereinander ein.
- Achte auf das exakte Format: `Summe: 30` — mit Leerzeichen nach dem Doppelpunkt.
- Gib nach der letzten Zahl einen Zeilenumbruch (`\n`) aus.

## So testest du

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test eingabe/02`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run eingabe/02`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?“) oder OpenCode im Terminal fragen
