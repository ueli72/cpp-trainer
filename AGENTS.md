# Projekt: C++ Trainer (Lernumgebung)

Lernumgebung für C++: Der Nutzer schreibt Übungslösungen in
`lektionen/<thema>/<lektion>/main.cpp` (in VSCodium) und arbeitet nur mit der Konsole.

## Regeln

- Immer auf Deutsch antworten.
- Bauen und Testen ausschließlich über das Skript `./trainer` im Projektordner:
  - `./trainer list` — Lektionen anzeigen
  - `./trainer build <lektion>` — nur kompilieren
  - `./trainer run <lektion>` — manuell ausführen
  - `./trainer test <lektion>` — automatische Tests ausführen
  - `./trainer all` — Tests aller Lektionen
  - `./trainer new <thema>/<name>` — neue Lektion aus `vorlage/` anlegen
- Lektionen leben in `lektionen/<thema>/<lektion>/` (Themen-Ordner, eine Lektion = ein Ordner), Testfälle in deren `tests/`-Ordner.
- `build/`-Ordner sind Wegwerfartefakte (kompilierte Programme, Testausgaben) — nicht aufräumen, nicht löschen.
- `main.cpp` des Nutzers niemals ohne ausdrückliche Aufforderung ändern — der Nutzer soll selbst lernen.
- Wird eine Lösung getestet, geprüft oder bewertet: den Skill `cpp-trainer` laden und dessen Ablauf verwenden.
