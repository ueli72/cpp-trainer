# Klasse 01 — Vektoren als class

## Ziel

Klassen verstehen: Eine `class` verbindet Daten mit den Funktionen, die dazugehören. Der Vector bringt jetzt alles selbst mit — er kann sich einlesen und seine Produkte ausgeben.

## Aufgabe

Wie in Struct 01, nur diesmal mit einer **`class Vector`** und zwei **Methoden**:

- `skalarprodukt(...)` — gibt das Skalarprodukt (eine Zahl) aus
- `vektorprodukt(...)` — gibt das Vektorprodukt, auch **Kreuzprodukt** genannt (Format `x,y,z`) aus

Beide Methoden geben ihr Ergebnis **direkt auf der Konsole aus** — sie liefern nichts zurück.

**Wichtig:** In `main.cpp` liegt ein **Gerüst**. Alles ist fertig — du ergänzt nur die beiden mit `TODO 1` und `TODO 2` markierten Methodenrümpfe, bis das Programm läuft:

**Eingabe** (Beispiel):

```
1,2,3
4,5,6
```

**Ausgabe** (Beispiel):

```
Skalarprodukt: 32.00
Kreuzprodukt: -3.00,6.00,-3.00
```

## Wie das Gerüst aufgebaut ist (learning by example)

- `class Vector { public: … };` — wie ein struct, mit einem Unterschied: In einer `class` ist alles **privat** (von außen unsichtbar), bis du mit `public:` den Zugang freigibst.
- **Methoden** sind Funktionen innerhalb der class. In ihnen greifst du **direkt** auf die Member zu: `x` statt `a.x` — sie gehören immer zu dem Objekt, mit dem die Methode aufgerufen wurde.
- **Aufruf:** `a.skalarprodukt(b);` — `a` ist das Objekt, das rechnet; `b` landet im Parameter `other`.
- `liesVonEingabe()` füllt das Objekt von allein: `a.liesVonEingabe();` schreibt direkt in `a.x`, `a.y`, `a.z`.

## Hinweise

- **TODO 1:** `std::cout << "Skalarprodukt: " << … << "\n";`
- **TODO 2:** Drei Komponenten berechnen (Formeln stehen im Kommentar), dann `std::cout << "Kreuzprodukt: " << cx << "," << cy << "," << cz << "\n";`
- Die Formatierung (2 Nachkommastellen) setzt `main` einmal vorab — in den Methoden brauchst du sie nicht mehr.
- **Beim ersten Kompilieren eine Warnung?** `unused parameter 'other'` ist solange normal, wie die Methoden noch leer sind — sie verschwindet, sobald du `other` benutzt.

## So testest du

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test rekursion/09klasse/01`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run klasse/01klasse/01`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?“) oder OpenCode im Terminal fragen
