# Cheatsheet — Let's Play 01: Zahlen raten

## Flussdiagramm des Spiels

```
   +-------------------------+
   |          Start          |
   +------------+------------+
                |
                v
   +-------------------------+
   | 1  geheim = Zufall      |<----------------+
   |    (0 - 100)            |                 |
   |    Versuche = 0         |                 |
   +------------+------------+                 |
                |                              |
                v                              |  (j) -> neues Spiel
   +-------------------------+                 |
   | 2  Banner:              |                 |
   |    "Ich habe mir eine   |                 |
   |    Zahl zwischen 0 und  |                 |
   |    100 ausgedacht"      |                 |
   |    "Errate sie!"        |                 |
   +------------+------------+                 |
                |                              |
                v                              |
   +-------------------------+                 |
+-->| 3  Versuche += 1        |                 |
|  |    "Versuch <n>: "      |                 |
|  |    Tipp einlesen        |                 |
|  +------------+------------+                 |
|               |                              |
|               v                              |
|       <Tipp == geheim?>                      |
|            |         |                       |
|          nein      ja                      |
|            |         |                       |
|            |         v                       |
|            | +-------------------------+     |
|            | | 4  "Du hast sie in      |     |
|            | |    <n> Versuchen        |     |
|            | +------------+------------+     |
|            |              |                  |
|            |              v                  |
|            | +-------------------------+     |
|            | | 5  "Noch ein Spiel?     |     |
|            | |    (j/n)" + Antwort     |     |
|            | +------------+------------+     |
|            |              |                  |
|            |              v                  |
|            |      <Antwort == 'j'?>----------+  (j) -> nach oben (neues Spiel)
|            |              |
|            |         nein
|            |              |
|            |              v
|            |     +-----------------+
|            |     |         Ende    |
|            |     +-----------------+
|            |
|            v
|  +-------------------------+
|  | 6  Vergleich:           |
+--|    tipp < geheim?       |
   |    ja:  "Meine Zahl     |
   |        ist grösser"     |
   |    nein: "Meine Zahl    |
   |        ist kleiner"     |
   +-------------------------+
      (nächster Versuch — zurück zu „3“)
```

Die linke Bahn ist die **Rat-Schleife** (falscher Tipp → zurück zu „Versuche += 1“),
die rechte Bahn die **Spiel-Schleife** („j“ → neues Spiel mit neuer Geheimzahl).

## Die zwei Schleifen-Ebenen

| Ebene | Schleife | läuft … |
|---|---|---|
| außen: ganze Spiele | `do { … } while (antwort == 'j');` | nochmal, solange „j“ |
| innen: Raten | `do { … } while (tipp != geheim);` | mindestens einmal, bis richtig |

Beide als `do while`: Das Einlesen muss **vor** der ersten Prüfung laufen.

## Der Zufall (steht schon im Skelett)

```cpp
std::uniform_int_distribution<int> verteilung(0, 100);
int geheim = verteilung(generator);   // jede Spielrunde NEU würfeln!
```
- `std::mt19937 generator` = Würfelmaschine, `verteilung` = Bereich 0–100
- Gleicher Startwert (Seed) → gleiche „Zufalls“-Reihe: Deshalb bekommen die
  Tests per `.args`-Datei einen Seed mit — sonst echter Zufall (`random_device`)
- Der Versuchzähler beginnt **pro Spiel** wieder bei 0

## Die Ausgaben (genau so!)

```
Ich habe mir eine Zahl zwischen 0 und 100 ausgedacht
Errate sie!
Versuch 1:      ← ohne Zeilenumbruch, danach vergleichen:
Meine Zahl ist grösser    /    Meine Zahl ist kleiner
Du hast sie in x Versuchen erraten
Noch ein Spiel? (j/n)
```

## Testen
`./trainer test lets-play/01` — Starten mit echtem Zufall: `./trainer run lets-play/01`
