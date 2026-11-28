# Prüfungsfragen 03 — Paare zählen: Vorstufe zur Prüfung 2019-02

## Ziel

Die Prüfungsaufgabe **„Number Pairs with Sum" (Exam 2019-02, RW)**
vorbereitet: Paare von **Indizes** `i < j` zählen, deren Summe genau
passt. Der Kern ist die doppelte Schleife — hier ohne Iteratoren.

## Aufgabe

Lies zuerst die **Zielsumme** ein, danach beliebig viele Zahlen
(Ende durch Dateiende/Strg+D) in einen Vektor.

Zähle alle Paare von Indizes `i < j` mit `zahlen[i] + zahlen[j] == zielsumme`.
Jedes Index-Paar zählt genau einmal — gleiche Werte an verschiedenen
Positionen sind verschiedene Paare!

**Eingabe** (Beispiel):

```
8 1 7 2 6 6
```

**Ausgabe** (Beispiel):

```
Paare: 3
```

(Die Paare: 1+7, 2+6, 2+6 — Indizes (0,1), (2,3), (2,4).)

## Hinweise

- Zwei verschachtelte Schleifen: `i` läuft über alle Positionen,
  `j` startet immer bei `i + 1` — so gilt automatisch `i < j`.
- Genau diese Doppel-Schleife baust du in **Prüfungsfragen 04** wieder
  ein — dort zusätzlich über **Iteratoren**.

## Testen

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test pruefung/03`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run pruefung/03`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?") oder OpenCode im Terminal fragen
