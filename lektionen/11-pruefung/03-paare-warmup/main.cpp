#include <iostream>
#include <vector>

// Vorstufe zur Pruefungsaufgabe "Number Pairs with Sum" (Exam 2019-02):
// Paare von Indizes i < j zaehlen, deren Summe die Zielsumme ergibt.
int main() {
    int zielsumme;
    std::cin >> zielsumme;

    std::vector<int> zahlen;
    int x;
    while (std::cin >> x) {
        zahlen.push_back(x);
    }

    // TODO: Zaehle die Paare von INDIZES i < j mit
    //   zahlen[i] + zahlen[j] == zielsumme
    //   (zwei verschachtelte Schleifen — j startet immer bei i + 1).
    //   Beachte: gleiche Werte an verschiedenen Positionen zaehlen mehrfach!
    int anzahl = 0;
    std::cout << "Paare: " << anzahl << "\n";

    return 0;
}
