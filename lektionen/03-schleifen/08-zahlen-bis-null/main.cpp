#include <iostream>

// do-while: erst handeln, dann prüfen — der Block läuft MINDESTENS einmal.
// Beim Einlesen genau richtig: den ersten Wert MUSST du lesen, bevor
// du prüfen kannst, ob er das Stoppsignal (0) war.
int main() {
    int summe = 0;
    int anzahl = 0;

    // TODO: Bau hier die do-while-Schleife:
    //   do {
    //       int x einlesen (std::cin >> x)
    //       wenn x nicht 0 ist: zur summe addieren und anzahl um 1 erhöhen
    //   } while (x != 0);        // das Semikolon am Ende nicht vergessen!
    // Tipp: zu x != 0 addieren kannst du einfach mit summe = summe + x.

    std::cout << "Summe: " << summe << "\n";
    std::cout << "Anzahl: " << anzahl << "\n";

    return 0;
}
