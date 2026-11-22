# Vektoren 03 — Skalarprodukt (Eigenbau)

## Ziel

Alles selbst bauen: Das Programm ist die Originalaufgabe „Vector and
matrix operations" — der **Skalarprodukt**-Teil mit Größenprüfung.

## Aufgabe

Lies **zwei Vektoren** ein — wie in der Originalaufgabe: zuerst die
**Größe n1**, dann n1 Werte; dann die **Größe n2**, dann n2 Werte.

Gib das **Skalarprodukt** aus (Summe der Produkte v1[i] * v2[i]).

Haben die beiden Vektoren unterschiedliche Längen, gib `error` aus.

## SOLL-Verhalten (Beispiele)

```
3
1 2 3
4 5 6
```

```
32
```

Bei unterschiedlichen Längen (`2` Werte und `3` Werte):

```
error
```

## Hinweise

- Lies zuerst `n`, dann die `n` Werte für `v1` (mit `push_back`), dann
  die `n` Werte für `v2`.
- Größenprüfung: sind die Vektoren unterschiedlich lang → `error`.
  Das ist der zweite Wert, den du mit `std::cin` einliest.
- Die Originalaufgabe (ETH) nutzt dafür eine eigene Funktion mit
  `const vec&`-Parametern — für hier reicht eine Lösung in `main`.

## Testen
- **In der App:** Lektion im Baum wählen → 💾 Speichern (bei Änderungen) → 🧪 Testen — die Ausgabe erscheint in der Konsole, die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test vektoren/03`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run vektoren/03`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?“) oder OpenCode im Terminal fragen

