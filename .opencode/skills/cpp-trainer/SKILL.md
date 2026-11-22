---
name: C++ Trainer — Lösungen testen
description: Intelligente Testreihen für C++-Übungslösungen im c++Trainer-Projekt schreiben, ausführen und Rückmeldung geben. Use when the user wants their exercise solution tested, checked, reviewed or graded (e.g. "teste meine Lösung", "prüfe die Aufgabe", "schreibe Tests", "warum schlägt der Test fehl"), or asks for a new lesson.
---

# C++ Trainer — Lösungen testen

Diese Projektmappe ist eine Lernumgebung. Struktur:

- `lektionen/<thema>/<lektion>/README.md` — Aufgabenstellung
- `lektionen/<thema>/<lektion>/main.cpp` — Lösung des Nutzers (niemals ungenannt ändern!)
- `lektionen/<thema>/<lektion>/tests/` — Testfälle als Paare: `NN-name.in` (Eingabe für stdin, darf leer sein) und `NN-name.out` (erwartete Ausgabe), optional `NN-name.args` (Kommandozeilenargumente, eine Zeile)
- `./trainer test <lektion>` — kompiliert und führt alle Tests aus (Exit-Code 0 = alle bestanden)
- `./trainer list` — Lektionen anzeigen; `./trainer new <thema>/<name>` — neue Lektion aus `vorlage/`

## Ablauf, wenn der Nutzer seine Lösung testen lässt

1. **Lektion ermitteln.** Falls unklar, `./trainer list` ausführen und nachfragen. Die Angabe darf auch ein Teil des Ordnernamens sein (`01` genügt meist).
2. **Aufgabe lesen:** `lektionen/<thema>/<lektion>/README.md`.
3. **Lösung lesen:** `lektionen/<thema>/<lektion>/main.cpp` — um zu verstehen, welche Eingaben das Programm erwartet und was es (vermutlich) tut.
4. **Testfälle entwerfen und als Dateien in `tests/` ablegen.** Die erwartete Ausgabe leitest du aus der **Aufgabenstellung** ab — niemals einfach von der Ausgabe des Programms abschauen (das würde Fehler bestätigen statt aufdecken).
5. **Ausführen:** `./trainer test <lektion>` aus dem Projektordner. Exit-Code 0 = alle bestanden, 1 = mindestens einer fehlgeschlagen.
6. **Rückmeldung geben** (siehe unten) — kurz, auf Deutsch, mit konkreten Hinweisen.

## Testfälle entwerfen

Decke ab, soweit die Aufgabe es sinnvoll macht:

- **Normalfälle:** typische, repräsentative Eingaben.
- **Sonderfälle/Randfälle:** leere Eingabe, 0, negative Zahlen, sehr große Werte, mehrere Werte in einer Zeile, Werte über mehrere Zeilen, Minimal-/Maximalwerte laut Aufgabe.
- **Fehlereingaben**, wenn die Aufgabe ein Verhalten dafür vorschreibt.
- Ein Test pro Dateipaar, sprechende Namen mit Nummernpräfix: `01-standard`, `02-leere-eingabe`, `03-negativ`, …

Qualitätsregeln:

- Erwartete Ausgabe **exakt** formulieren (Groß-/Kleinschreibung, Leerzeichen, Zeilenumbrüche). Wenn die Aufgabe das Format offen lässt, einmal im README der Lektion festhalten und konsistent testen.
- Trainer vergleicht tolerant: Leerzeichen am Zeilenende und Leerzeilen am Schluss ignorieren er bereits — nicht selbst nachlässig werden bei allem anderen.
- Bei Programmen mit Eingabe: `.in`-Datei mit genau der Eingabe füllen, die das Programm laut Aufgabe erwartet (z. B. eine Zahl pro Zeile).
- Lieber 5–10 gute Tests als 20 fast identische.
- Fehlt zu einem `.in` die `.out`-Datei, ergänze sie — der Trainer meldet das als UNVOLLSTÄNDIG.

## Rückmeldung an den Nutzer

Struktur der Antwort:

1. **Zusammenfassung:** „X von Y Tests bestanden.“
2. **Für jeden fehlgeschlagenen Test:** Name, erwartete Ausgabe, tatsächliche Ausgabe, Exit-Code/stderr falls relevant, und **ein konkreter Verdacht** (z. B. „vermutlich fehlt der Zeilenumbruch“, „off-by-one bei der Schleifengrenze“, „ Division Integer vs. Gleitkomma“).
3. **Keine fertige Korrektur** des Codes liefern, solange nicht ausdrücklich darum gebeten wird — der Nutzer soll selbst lösen. Stattdessen gestufte Hinweise anbieten („Sag Bescheid, wenn du einen stärkeren Hinweis willst“).
4. Den Nutzer ermutigen, selbst anzupassen und `./trainer test <lektion>` erneut auszuführen.

Weitere Regeln:

- Kompiliert und getestet wird nur über `./trainer` (einheitliche Flags: `-std=c++17 -Wall -Wextra`). Kompilerwarnungen ernst nehmen und erwähnen.
- Neue Tests immer als Dateien im `tests/`-Ordner anlegen (kein Ad-hoc-Piping), damit sie reproduzierbar und beim Nutzer sichtbar bleiben.
- Fragt der Nutzer nach einer **neuen Lektion**: `./trainer new <thema>/<name>` ausführen, dann eine sinnvolle, altersgerecht formulierte Aufgabe in `README.md` schreiben (mit erwarteten Ein-/Ausgabebeispielen) und optional Start-Testfälle anlegen.
- Auf Deutsch antworten.
