// ============================================================
// Klasse 04 — Uhrzeit-Eigenbau
// ============================================================
// Hier steht kein Code mehr — nur dein Bauplan. Alles, was du
// dafür brauchst, hast du in den bisherigen Lektionen bereits gebaut.
// Lege die Dateien Zeit.h und Zeit.cpp daneben an und baue
// Schritt für Schritt. Nach jedem Schritt: ./trainer build 08
//
// Deine Schritte:
//
// 1. Zeit.h: Include-Guard (#ifndef ZEIT_H / #define ZEIT_H /
//    #endif, wie in Klasse 03) und darin die class Zeit mit
//    public: zwei int-Membern stunde und minute.
//    → Meilenstein: ./trainer build 08 läuft durch.
//
// 2. liesVonEingabe(): Deklaration in Zeit.h (endet mit ;),
//    Definition in Zeit.cpp mit dem Scope-Operator:
//    void Zeit::liesVonEingabe() { … }
//    Einlesen wie gewohnt im Trennzeichen-Trick aus 03–07 —
//    nur schluckt diesmal ein char den Doppelpunkt:
//    std::cin >> stunde >> dp >> minute;
//    → Meilenstein: ./trainer run klasse/04 und selbst eintippen
//    (beenden mit Strg+D).
//
// 3. operator+(Zeit other): wieder Deklaration in Zeit.h,
//    Definition in Zeit.cpp: Zeit Zeit::operator+(Zeit other)
//    Er liefert einen ZEIT-WERT zurück (wie operator* in 06/07
//    eine Zahl lieferte — diesmal also der Rückgabetyp Zeit).
//    Rechenidee: alles in Minuten umrechnen
//    (stunde*60 + minute, plus das von other), zusammenzählen,
//    zurückrechnen mit Ganzzahl-Division und Rest:
//    der %-Operator gibt den Rest einer Division — 95 % 60 ist 35.
//        stunde = total / 60 % 24;   (das % 24 lässt die Uhr
//    über Mitternacht weiterlaufen)  minute = total % 60;
//
// 4. main(): zwei Zeit-Objekte einlesen, beide liegen je in
//    EINER Zeile im Format HH:MM (z. B. 13:45 und 2:50),
//    dann c = a + b und genau eine Ausgabezeile:
//
//    Summe: 16:35
//
// 5. Zweistellig ausgeben — führende Nullen:
//    Neu, aber klein: std::setw(2) (aus <iomanip>) macht das
//    nächste ausgegebene Stück 2 Zeichen breit, std::setfill('0')
//    füllt die Lücken mit '0' statt Leerzeichen.
//
//    ABER ACHTUNG (klassische Falle): setw gilt nur für das NÄCHSTE
//    Stück — setfill bleibt. Deshalb setw vor JEDER Komponente
//    wiederholen:
//
//    std::cout << std::setfill('0') << std::setw(2) << zeit.stunde
//              << ":" << std::setw(2) << zeit.minute << "\n";
//
//    (Die Eingabe braucht das übrigens nicht — std::cin >> stunde
//    frisst auch 9:5 problemlos. Nullen sind reines Ausgabe-Thema.)

// ============================================================
// Dein main: Programmstart — hier baust du Schritt 4 und 5 ein.
// ============================================================
int main() {
    // Schritt 4: zwei Zeit-Objekte, einlesen, c = a + b
    // Schritt 5: Ausgabe "Summe: HH:MM" (zweistellig!)

    return 0;
}
