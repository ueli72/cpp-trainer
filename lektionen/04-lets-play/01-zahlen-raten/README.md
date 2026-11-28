# Let's Play 01 — Zahlen raten

## Ziel

Alles aus den Schleifen-Kapiteln in einem echten Spiel: zwei ineinander verschachtelte Schleifen (Raten + Nochmal-Spielen), Verzweigungen und ein Zähler. Der Zufall steht schon im Code — du baust das Spiel drumherum.

## Aufgabe

Das Spiel läuft so:

1. Der Computer denkt sich eine **Zufallszahl zwischen 0 und 100** aus. Das ist im Skelett schon implementiert (`geheim`).
2. Bei jedem Spiel beginnt er mit **zwei Zeilen**:
   ```
   Ich habe mir eine Zahl zwischen 0 und 100 ausgedacht
   Errate sie!
   ```
3. Dann rät der Spieler: Es erscheint **`Versuch 1: `** und der Spieler tippt eine Zahl ein. Danach `Versuch 2: ` usw.
4. Nach jedem Tipp vergleicht der Computer:
   - Tipp zu klein → `Meine Zahl ist grösser`
   - Tipp zu gross → `Meine Zahl ist kleiner`
   - Tipp richtig → `Du hast sie in x Versuchen erraten` (x = Anzahl der Versuche dieses Spiels)
5. Dann fragt er: **`Noch ein Spiel? (j/n)`** — bei `j` beginnt ein komplettes neues Spiel (neue Zufallszahl, Versuche wieder bei 1), sonst endet das Programm.

Ein kompletter Spielzug (Eingaben nach den Aufforderungen: `50`, `75`, `63`):

```
Ich habe mir eine Zahl zwischen 0 und 100 ausgedacht
Errate sie!
Versuch 1: Meine Zahl ist grösser
Versuch 2: Meine Zahl ist kleiner
Versuch 3: Du hast sie in 3 Versuchen erraten
Noch ein Spiel? (j/n) 
```

> Im Testprotokoll steht die Ausgabe direkt hinter der Aufforderung — genau so erscheint es auch in der Konsole, denn die Eingabe selbst wird nicht mitgeschrieben.

## Hinweise

- **Zwei Schleifen:** Außen eine Schleife für „noch ein Spiel", innen eine fürs Raten. Beides bietet sich als `do while` an — beim Raten musst du mindestens einmal fragen!
- **Der Versuchszähler** startet bei jedem neuen Spiel wieder bei 0 und wird **vor** der Ausgabe der Aufforderung erhöht.
- **Der Zufall ist fertig** — das Wichtigste aus dem Skelett:
  ```cpp
  std::uniform_int_distribution<int> verteilung(0, 100);
  int geheim = verteilung(generator);   // jede Spielrunde würfelt NEU
  ```
- **Für die Tests:** Das Programm kann beim Start einen Startwert für den Zufallsgenerator mitbekommen (Kommandozeilenargument) — dann ist die „ausgedachte" Zahl immer dieselbe. Deshalb kennen die Testfälle die Geheimzahl. Beim normalen Start (per ▶ Starten) bleibt es echter Zufall.
- Es werden immer gültige Zahlen von 0 bis 100 eingegeben — Prüfungen auf Falscheingaben brauchst du nicht.

## So testest du

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/` (`.args` = Startwert für den Zufall)
- **Im Terminal:** `./trainer test lets-play/01`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run lets-play/01` — hier ist der Zufall echt!
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?“) oder OpenCode im Terminal fragen
