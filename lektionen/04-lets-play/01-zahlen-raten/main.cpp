// =====================================================================
// Let's Play 01 — Zahlen raten
// =====================================================================
//
// RANDOM — so denkt sich der Computer eine Zufallszahl aus:
//
//   Zufall in C++ braucht drei Bausteine (alle in <random>):
//
//   1. Eine Zufallsquelle — liefert echte Zufallsdaten vom Betriebssystem:
//        std::random_device quellgeraet;
//
//   2. Einen Generator — eine Maschine, die aus einem Startwert eine
//      lange, chaotisch wirkende Zahlenreihe erzeugt. Der verbreitete
//      Standardgenerator heißt Mersenne-Twister:
//        std::mt19937 generator;
//      Dem Generator muss man einen STARTWERT (Seed) geben — von dort
//      arbeitet die Reihe weiter. Gleicher Startwert → gleiche Reihe!
//
//   3. Eine Verteilung — aus welchem Bereich soll die Zahl kommen,
//      und soll jede gleich wahrscheinlich sein:
//        std::uniform_int_distribution<int> verteilung(0, 100);
//      („gleichverteilt“ — jede Zahl von 0 bis 100 gleich wahrscheinlich)
//
//   Eine Zahl würfeln:      verteilung(generator)
//   Jeder Aufruf liefert die NÄCHSTE Zahl der Reihe — wer zweimal
//   würfelt, bekommt (fast sicher) zwei verschiedene Zahlen.
//
// Die if-Abfrage unten ist ein Test-Trick: Wird dem Programm beim Start
// ein Startwert mitgegeben (z. B.  ./app 7), nimmt es DIESSEN Seed —
// die „ausgedachte“ Zahl ist dann immer gleich und die Tests können
// sie kennen. Beim normalen Start entscheidet die Zufallsquelle.
//
// (main bekommt hier erstmals Argumente: argc = Anzahl, argv = die
// Texte hinter dem Programmnamen. argv[1] ist das erste Argument.)
// =====================================================================

#include <iostream>
#include <random>

int main(int argc, char* argv[]) {
    std::mt19937 generator;
    if (argc > 1) {
        generator.seed(std::stoul(argv[1]));   // Startwert von außen (Tests)
    } else {
        std::random_device quellgeraet;
        generator.seed(quellgeraet());         // echter Zufall
    }
    std::uniform_int_distribution<int> verteilung(0, 100);

    // =================================================================
    // AB HIER BIST DU — dein Spiel!
    //
    // Deine Bausteine (alles schon dagewesen in den Lektionen):
    //
    //   int geheim = verteilung(generator);  — die ausgedachte Zahl.
    //       Achtung: jede NEUE Spielrunde muss neu würfeln!
    //
    //   Zwei Schleifen ineinander:
    //     Außen: das komplette Spiel — läuft nochmal bei Antwort 'j'
    //     Innen: das Raten — läuft, bis der Tipp stimmt
    //
    //   Pro Spiel:
    //     1. Die zwei Bannerzeilen ausgeben (siehe README)
    //     2. Innen-Schleife (do while):
    //          - Versuchszähler erhöhen (startet jedes Spiel bei 0)
    //          - "Versuch i: " ausgeben — OHNE Zeilenumbruch am Ende,
    //            damit der Spieler hinter dem Doppelpunkt tippt
    //          - Tipp einlesen
    //          - kleiner/größer vergleichen und den Hinweis ausgeben
    //     3. Nach der Innen-Schleife: "Du hast sie in x Versuchen erraten"
    //     4. "Noch ein Spiel? (j/n) " ausgeben und die Antwort einlesen
    //        (ein char:  char antwort;  std::cin >> antwort;)
    // =================================================================

    return 0;
}
