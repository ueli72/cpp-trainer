# Schleifen 08 — Zahlen bis 0

## Ziel

Die `do while`-Schleife: sie läuft **garantiert mindestens einmal**, weil erst gehandelt und danach geprüft wird. Genau richtig beim Einlesen — den ersten Wert musst du lesen, **bevor** du weißt, ob er das Stoppsignal ist.

## Aufgabe

Lies beliebig viele ganze Zahlen ein (**eine pro Zeile**). Die Zahl **`0` beendet** die Eingabe — sie selbst zählt nicht mit. Es ist garantiert mindestens eine Zahl in der Eingabe (notfalls nur die `0`).

Gib anschließend **zwei Zeilen** aus — Summe und Anzahl der gelesenen (von der `0` verschiedenen) Zahlen:

**Eingabe** (Beispiel):

```
5
7
2
0
```

**Ausgabe** (Beispiel):

```
Summe: 14
Anzahl: 3
```

## Hinweise

- So sieht `do while` aus — beachte das **Semikolon hinter `while (…)`**:
  ```cpp
  do {
      // läuft mindestens einmal
  } while (x != 0);
  ```
- Im Block: `x` einlesen; wenn `x` nicht `0` ist, zur Summe addieren und die Anzahl um 1 erhöhen. Die Schleife wiederholt sich, solange `x != 0`.
- Warum `do while` und nicht `while`? Ein `while (x != 0)` würde **vor** der ersten Runde prüfen — aber `x` ist zu dem Zeitpunkt noch gar nicht eingelesen.
- Das Muster „Anzahl mitzählen“ kennst du aus Lektion 04.

## So testest du

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test schleifen/08`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run schleifen/08`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?“) oder OpenCode im Terminal fragen
