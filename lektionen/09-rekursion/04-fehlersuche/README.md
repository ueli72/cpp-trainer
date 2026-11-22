# Rekursion 04 — Fehlersuche: Fakultät

## Ziel

Rekursion debuggen: Basisfall und rekursiver Schritt — typische Fehler
finden, bevor sie problematisch werden.

## Aufgabe

Das Programm soll die **Fakultät** n! = 1 · 2 · … · n rekursiv berechnen
(0! = 1). Es enthält **2 eingebaute Fehler** (beide Logik — das Programm
kompiliert und terminiert, rechnet aber falsch).

## SOLL-Verhalten (Beispiele)

```
5   →  Fakultaet: 120
0   →  Fakultaet: 1
10  →  Fakultaet: 3628800
```

## Hinweise

- Der Basisfall: Was ist 0! wirklich? Und was liefert der Code?
- Der rekursive Schritt: Fakultät multipliziert — was steht im Code?
- Teste mit n = 0 zuerst: Der kleinste Fall verrät den ersten Fehler.

## Testen
- **In der App:** Lektion im Baum wählen → 💾 Speichern (bei Änderungen) → 🧪 Testen — die Ausgabe erscheint in der Konsole, die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test rekursion/04`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run rekursion/04`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?“) oder OpenCode im Terminal fragen

