# Ziffern 04 — Zahlensysteme (Klausurniveau)

## Ziel

Die Klausuraufgabe vom Januar 2022: eine Dezimalzahl in eine beliebige Basis umrechnen — alles aus Ziffern 01 und 02 kommt hier zusammen.

## Aufgabe

Lies zwei ganze Zahlen ein: `value` (größer oder gleich 0) und `base` (zwischen 2 und 9), getrennt durch Leerzeichen.

Gib `value` **zur Basis `base`** als Ziffernfolge aus. Beispiele:

- `10 2` → `1010` (denn 10 = 8 + 2 = 1·8 + 0·4 + 1·2 + 0·1)
- `255 9` → `313` (denn 255 = 3·81 + 1·9 + 3)

Hinweis zur Technik wie im Original: Wiederholt `value % base` (letzte Ziffer) und `value /= base` — die Ziffern fallen in umgekehrter Reihenfolge an.

**Eingabe** (Beispiel):

```
10 2
```

**Ausgabe** (Beispiel):

```
1010
```

## Hinweise

- Das ist exakt die Technik aus Ziffern 02 — nur dass du mit `% base` statt `% 10` arbeitest.
- Sonderfall `value = 0` → Ausgabe `0` (die Schleife läuft sonst kein einziges Mal).
- Führende Nullen gibt es bei dieser Umrechnung nicht — die höchste Ziffer ist immer ungleich 0.

## So testest du

- `./trainer test ziffern/04` (oder in VSCodium Strg+Shift-B bzw. der 🧪-Button) — die Testfälle liegen sichtbar in `tests/`
- `./trainer run ziffern/04` — das Programm selbst ausprobieren
- Bei roten Tests: OpenCode fragen, z. B. „Warum schlägt mein Test fehl?“
