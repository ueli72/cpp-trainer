#include <iostream>

// Raten ist do-while pur: mindestens EIN Versuch, dann so lange
// weitere, bis der Treffer da ist.
int main() {
    int versuche = 0;

    // TODO: Lege die geheime Zahl an:  const int GEHEIM = 42;  (const = unveränderlich)
    // TODO: Bau hier die do-while-Schleife:
    //   do {
    //       int tipp einlesen (std::cin >> tipp)
    //       versuche um 1 erhöhen
    //   } while (tipp != GEHEIM);   // läuft, SOLANGE noch nicht geraten
    // Die Ausgabe unten gibst dann die Anzahl der Versuche aus.

    std::cout << "Versuche: " << versuche << "\n";

    return 0;
}
