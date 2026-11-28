# Schleifen 09 — Zahlen raten

## Ziel

`do while` als „wiederhole, **bis** es klappt“: mindestens ein Versuch, danach so lange weitere, bis die Bedingung erfüllt ist.

## Aufgabe

Das Programm hält eine **geheime Zahl fest: 42** — lege sie dir als `const int GEHEIM = 42;` an (Tipp steht im Skelett).

Lies solange Tipps ein (**eine Zahl pro Zeile**), bis jemand die `42` rät. Jede Eingabe ist ein Versuch — **auch die richtige**. Gib aus, wie viele Versuche gebraucht wurden:

**Eingabe** (Beispiel):

```
10
100
41
42
```

**Ausgabe** (Beispiel):

```
Versuche: 4
```

## Hinweise

- Struktur wie in Lektion 08 — nur ist das Stoppsignal hier der **Treffer** statt der `0`:
  ```cpp
  do {
      // Tipp einlesen, Versuch mitzählen
  } while (tipp != GEHEIM);
  ```
- `!=` heißt „ungleich“ — die Schleife läuft also, **solange noch nicht geraten** wurde.
- `const int GEHEIM = 42;` — `const` macht die Variable unveränderlich (gute Angewohnheit für feste Werte).
- Grenzfall: gleich der erste Tipp ist richtig → `Versuche: 1`.

## So testest du

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test schleifen/09`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run schleifen/09`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?“) oder OpenCode im Terminal fragen
