# Klasse 04 — Uhrzeit-Eigenbau

## Ziel

Alles zusammenbringen: Du baust eine Klasse **komplett selbst** — mit eigener Header-Datei, eigenem Operator und eigener Eingabelogik. Kein Gerüst mehr, nur noch der Bauplan als Kommentare in `main.cpp`.

## Aufgabe

Lies zwei Uhrzeiten ein — **jeweils in einer eigenen Zeile**, im Format `HH:MM` (z. B. `13:45` und `2:50`).

Addiere sie mit einem selbst überladenen **`operator+`** und gib die Summe aus — **immer zweistellig**, auch `00:20`. Die Uhr läuft dabei **über Mitternacht** weiter (`23:50 + 0:30` ist `00:20` am nächsten Tag).

**Eingabe** (Beispiel):

```
13:45
2:50
```

**Ausgabe** (Beispiel):

```
Summe: 16:35
```

## Wie du vorgehst

Der **Bauplan steht als Kommentare in `main.cpp`** — öffne sie und arbeite die 5 Schritte ab. `Zeit.h` und `Zeit.cpp` existieren bereits, enthalten aber selbst nur Kommentar-Erinnerungen.

Nach jedem Schritt ein `./trainer build 08` bzw. `./trainer run klasse/04` — die Bauplan-Kommentare nennen dir nach jedem Schritt einen Meilenstein.

## Wo du was wiederverwendest

| Konzept | Gelernt in |
|---|---|
| Trennzeichen mit `char` „wegschlucken“ | 03–07 (jetzt: `:` statt `,`) |
| class mit Methoden | 05 |
| Operator, der sein Ergebnis `return`t | 06/07 |
| Header + Implementierung trennen (`Zeit::`) | 07 |
| `%` als Rest-Operator (neu, klein) | Bauplan, Schritt 3 |
| `setw`/`setfill` für führende Nullen (neu, klein) | Bauplan, Schritt 5 |

## Hinweise

- Denk an die **Ganzzahl-Division**: `995 / 60` ist `16` — und `995 % 60` ist `35`.
- Das `% 24` in der Stundenberechnung sorgt dafür, dass die Uhr über Mitternacht weiterläuft.
- **setw-Falle:** `std::setw(2)` gilt nur für die **nächste** Ausgabe — vor jeder Komponente wiederholen (genaue Zeile im Bauplan, Schritt 5).

## So testest du

- `./trainer test klasse/04` (oder in VSCodium Strg+Shift-B bzw. der 🧪-Button) — die Testfälle liegen sichtbar in `tests/`
- `./trainer run klasse/04` — das Programm selbst ausprobieren
- Bei roten Tests: OpenCode fragen, z. B. „Warum schlägt mein Test fehl?“
