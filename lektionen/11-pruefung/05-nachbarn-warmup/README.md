# Prüfungsfragen 05 — Iteratoren & Nachbarn: Vorstufe zur Prüfung 2022-08

## Ziel

Die Prüfungsaufgabe **„max_difference" (Exam 2022-08, ITET MATH PHYS RW)**
vorbereitet: gleiches Einlese-Format wie in der Prüfung (Zahlen bis `-1`),
zuerst mit **Iteratoren** umgehen, dann benachbarte Werte vergleichen.

## Aufgabe

Lies ganze Zahlen ein, bis `-1` kommt (die `-1` gehört **nicht** zu den
Daten — genau wie in der Prüfung). Mindestens zwei Zahlen sind garantiert.

Das Skelett hat drei TODOs:

1. **Anzahl** der Zahlen ausgeben
2. **Erste und letzte Zahl** — aber mit **Iteratoren**:
   `*zahlen.begin()` bzw. `*(zahlen.end() - 1)`
3. **Größte Differenz** zweier benachbarter Zahlen (Absolutbetrag!)

**Eingabe** (Beispiel):

```
1 5 2 5 7 6 -1
```

**Ausgabe** (Beispiel):

```
Anzahl: 6
Erste: 1, Letzte: 6
Groesste Differenz: 4
```

## Hinweise

- Benachbarte Paare sind `zahlen[i]` und `zahlen[i + 1]` — die Schleife
  stoppt beim vorletzten Index. In der Prüfung steht das Paar als
  Iterator-Paar `[begin, end)` im Raum — die Idee ist dieselbe.
- Differenz mit Vorzeichen beachten: `|2 - 5| = 3` — negiere im
  Fehlerfall oder nutze `std::abs` (Header `<cstdlib>`).
- In **Prüfungsfragen 06** ist die Aufgabe die Original-Prüfungsfunktion
  mit Iteratoren-Parametern.

## Testen

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test pruefung/05`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run pruefung/05`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?") oder OpenCode im Terminal fragen
