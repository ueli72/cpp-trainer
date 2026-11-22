#include <iostream>
#include <iomanip>
#include <vector>

// Skelett: die Struktur steht — du ergaenzst die TODO-Bloecke.
int main() {
    std::vector<int> zahlen;
    int x;
    while (std::cin >> x) {
        zahlen.push_back(x);
    }

    // TODO 1: Minimum berechnen — mit dem ersten Element starten und
    //   jedes weitere vergleichen. Ausgabe:  Minimum: <wert>
    int minimum = 0;

    // TODO 2: Maximum berechnen — analog. Ausgabe:  Maximum: <wert>
    int maximum = 0;

    // TODO 3: Durchschnitt berechnen (Summe / Anzahl, als double!)
    //   Ausgabe mit 2 Nachkommastellen:  Durchschnitt: <wert>
    double durchschnitt = 0;

    std::cout << "Anzahl: " << zahlen.size() << "\n";
    std::cout << "Minimum: " << minimum << "\n";
    std::cout << "Maximum: " << maximum << "\n";
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "Durchschnitt: " << durchschnitt << "\n";

    return 0;
}
