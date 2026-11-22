# Verzweigung 02 — Die größere Zahl

## Ziel

Verzweigungen sicher einsetzen: zwei Werte vergleichen und passend dazu ausgeben — inklusive des Sonderfalls „gleich“.

## Aufgabe

Lies zwei ganze Zahlen `a` und `b` ein (in einer Zeile, durch Leerzeichen getrennt).

Gib die **größere** der beiden Zahlen aus. Sind beide gleich, gib `Gleich` aus:

**Eingabe** (Beispiel):

```
3 7
```

**Ausgabe** (Beispiel):

```
Groessere: 7
```

Bei gleicher Eingabe (z. B. `5 5`):

```
Gleich
```

> **Skelett:** In `main.cpp` steht schon ein Teil — den Rest ergänzt du an den `TODO`-Stellen.

## Hinweise

- Du brauchst zwei Vergleiche: `a > b` und `a == b` (der Rest ist der andere Fall).
- Der Vergleich auf Gleichheit hat **zwei** Gleichheitszeichen: `a == b` — ein einzelnes `=` wäre eine Zuweisung.
- Genau dieses Muster baust du in der nächsten Lektion ohne Vorlage aus.

## So testest du

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test verzweigung/02`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run verzweigung/02`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?“) oder OpenCode im Terminal fragen
