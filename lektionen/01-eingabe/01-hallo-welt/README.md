# Eingabe 01 — Hallo, du!

## Ziel

Erstes Programm mit Eingabe: die Konsole mit `cout`/`cin` kennenlernen — und verstehen, wie eine Zeile in deinem Programm aufgebaut ist. Der komplette Ablauf steht kommentiert in `main.cpp`.

## Aufgabe

Das Gerüst in `main.cpp` gibt bereits `Hallo, Welt!` aus. Baue es zu einer persönlichen Begrüßung aus:

Lies einen **Namen** ein (ein Wort) und gib genau **eine** Zeile aus:

**Eingabe** (Beispiel):

```
Ada
```

**Ausgabe** (Beispiel):

```
Hallo, Ada!
```

## Hinweise

- Werkzeuge stehen als Kommentare im Gerüst: `std::string name;` und `std::cin >> name;`
- Texte klebt man mit `+` aneinander: `"Hallo, " + name + "!"`
- Die alte feste `Hallo, Welt!`-Ausgabe verschwindet dabei — übrig bleibt genau eine Zeile.

## So testest du

- `./trainer test eingabe/01` (oder in VSCodium Strg+Shift-B bzw. der 🧪-Button) — die Testfälle liegen sichtbar in `tests/`
- `./trainer run eingabe/01` — das Programm selbst ausprobieren
- Bei roten Tests: OpenCode fragen, z. B. „Warum schlägt mein Test fehl?“
