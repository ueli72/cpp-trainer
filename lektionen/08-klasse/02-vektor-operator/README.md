# Klasse 02 — Skalarprodukt als Operator

## Ziel

Operatoren überladen: Der eigene Typ bekommt dasselbe `*`-Zeichen wie `int` und `double` — `a * b` liefert fortan das Skalarprodukt.

## Aufgabe

Definiere eine `class Vector` mit drei `double`-Membern `x`, `y`, `z` und einem **`operator*`**, der das Skalarprodukt liefert.

Lies zwei Vektoren ein — jeweils in einer eigenen Zeile im Format `x,y,z` — und gib das Skalarprodukt mit **genau zwei Nachkommastellen** aus:

**Eingabe** (Beispiel):

```
1,2,3
4,5,6
```

**Ausgabe** (Beispiel):

```
Skalarprodukt: 32.00
```

## Hintergrund (aus Klasse 01)

- Eine Methode mit besonderem Namen: Der Aufruf `a * b` ist exakt dasselbe wie `a.operator*(b)`.
- Der Operator **liefert** sein Ergebnis (`return`, Typ `double`) — er gibt nichts selbst aus. Das Drucken passiert in `main`.
- C++ erlaubt nur das Überladen **vorhandener** Symbole — neue Zeichen (wie das „×“ aus der Mathematik) kann man nicht erfinden.

> **Skelett:** In `main.cpp` steht schon ein Teil — den Rest ergänzt du an den `TODO`-Stellen.

## Hinweise

- Formel: `x*other.x + y*other.y + z*other.z` — `other` ist der zweite Vector, der beim Aufruf übergeben wird.
- Einlesen wie gewohnt mit dem Komma-Trick: `std::cin >> v.x >> komma >> v.y >> komma >> v.z;`
- Zwei Nachkommastellen: `std::cout << std::fixed << std::setprecision(2);` (aus `<iomanip>`), einmal in `main` gesetzt gilt es für alle folgenden Ausgaben.

## So testest du

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test rekursion/09klasse/02`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run klasse/02klasse/02`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?“) oder OpenCode im Terminal fragen
