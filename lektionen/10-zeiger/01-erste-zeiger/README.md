# Zeiger 01 — Erste Zeiger (Beispiele)

## Ziel

Zeiger verstehen: Ein Zeiger ist eine Variable, die eine **Adresse**
speichert. Mit `&x` holt man die Adresse von `x`, mit `*p` liest oder
schreibt man den Wert an der Adresse — auch über Funktionsgrenzen hinweg.

## Aufgabe

Lies **zwei ganze Zahlen** `a` und `b` ein. Das Skelett hat zwei Funktionen
als TODO:

1. `max_ptr(&a, &b)` liefert einen **Zeiger auf die größere** der beiden
   Zahlen — `main` gibt den Wert über diesen Zeiger aus.
2. `tauschen(&a, &b)` vertauscht die **Werte** von `a` und `b` — per
   Zeiger, damit die Änderung in `main` ankommt.

**Eingabe** (Beispiel):

```
3 7
```

**Ausgabe** (Beispiel):

```
Max: 7
Getauscht: 7 3
```

## Hinweise

- `max_ptr` vergleicht `*a` und `*b` (die **Werte**) und gibt `a` oder `b`
  zurück — nicht `*a` oder `*b`!
- Beim Tauschen brauchst du eine Zwischenvariable für den **Wert**:
  `int tmp = *a;`
- Klassische Falle: Zeiger vertauschen statt Werte — die beiden Zeiger in
  der Funktion sind nur **lokale Kopien**, außen ändert das nichts.

## Testen

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test zeiger/01`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run zeiger/01`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?") oder OpenCode im Terminal fragen
