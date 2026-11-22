# Rekursion 03 — Zahlensysteme (rekursiv, Eigenbau)

## Ziel

Die Klausuraufgabe vom Januar 2022 — diesmal **rekursiv**. Die Rekursion löst nebenbei das eleganteste Problem der iterativen Version: die Ziffern fallen nicht mehr umgekehrt an, weil der rekursive Aufruf **vor** der eigenen Ausgabe passiert.

## Aufgabe

Lies zwei ganze Zahlen ein: `value` (größer oder gleich 0) und `base` (zwischen 2 und 9), getrennt durch Leerzeichen.

Gib `value` **zur Basis `base`** als Ziffernfolge aus — die Umrechnung läuft **rekursiv**, ohne Schleife:

**Eingabe** (Beispiel):

```
10 2
```

**Ausgabe** (Beispiel):

```
1010
```

Weitere Beispiele: `255 9` → `313`, `7 8` → `7`, `0 2` → `0`.

## Wie du vorgehst

Der **Bauplan steht als Kommentare in `main.cpp`**. Das Herzstück:

```
gibZiffernAus(value, base):
    wenn value == 0:  return                    ← Abbruch
    gibZiffernAus(value / base, base)           ← ERST weiter reichen …
    gib die letzte Ziffer (value % base) aus    ← … DANN eigene Ziffer
```

Beispiel `10 2`: gibZiffernAus(10) → ruft gibZiffernAus(5) → ruft gibZiffernAus(2) → ruft gibZiffernAus(1) → ruft gibZiffernAus(0) [Abbruch] → gibt 1 aus → 0 → 1 → 0 → 0: **1010**.

## Hinweise

- Der Sonderfall `value = 0` wird **in main** abgefangen (direkt `0` ausgeben) — die Rekursion selbst würde bei 0 nichts ausgeben.
- Keine führenden Nullen — die höchste Ziffer ist immer ungleich 0.
- Vergleiche mit deiner Lösung aus Ziffern 04: dort brauchtest du Tricks für die Reihenfolge — hier erledigt die Rekursion das allein.

## So testest du
- **In der App:** Lektion im Baum wählen → 💾 Speichern (bei Änderungen) → 🧪 Testen — die Ausgabe erscheint in der Konsole, die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test rekursion/03`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run rekursion/03`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?“) oder OpenCode im Terminal fragen

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?“) oder OpenCode im Terminal fragen
