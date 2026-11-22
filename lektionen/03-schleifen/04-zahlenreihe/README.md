# Schleifen 04 — Zahlenreihe auswerten

## Ziel

Eingaben mit Stoppsignal verarbeiten — Anzahl, Summe und Maximum auf einmal verwalten, wie in der Originalübung „Number of Occurrences“.

## Aufgabe

Lies beliebig viele ganze Zahlen ein (**eine pro Zeile**). Eine **negative Zahl beendet** die Eingabe — sie selbst wird nicht mehr mitgezählt. Es ist garantiert mindestens eine nicht-negative Zahl dabei.

Gib anschließend **drei Zeilen** aus — Anzahl, Summe und Maximum der gelesenen (nicht-negativen) Zahlen:

**Eingabe** (Beispiel):

```
42
7
13
38
-1
```

**Ausgabe** (Beispiel):

```
Anzahl: 4
Summe: 100
Maximum: 42
```

## Hinweise

- Lesen in einer Schleife: `while (std::cin >> x) { if (x < 0) break; … }`
- Halte drei Variablen aktuell: `anzahl`, `summe` und `maximum` (beim ersten Wert setzen, danach mit if aktualisieren).
- Gib am Ende genau drei Zeilen aus: `Anzahl: …`, `Summe: …`, `Maximum: …`.

## So testest du

- `./trainer test schleifen/04` (in der App: 🧪-Button) — die Testfälle liegen sichtbar in `tests/`
- `./trainer run schleifen/04` — das Programm selbst ausprobieren
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?“) oder OpenCode im Terminal fragen
