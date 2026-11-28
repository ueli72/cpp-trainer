#include <iostream>
#include <vector>

// Vorstufe zur Pruefungsaufgabe "max_difference" (Exam 2022-08):
// gleiches EINLESE-Format wie in der Pruefung — Zahlen bis -1.
int main() {
    std::vector<int> zahlen;
    int x;
    std::cin >> x;
    while (x != -1) {
        zahlen.push_back(x);
        std::cin >> x;
    }

    // TODO 1: Anzahl der Zahlen ausgeben:  Anzahl: <n>
    std::cout << "Anzahl: " << 0 << "\n";

    // TODO 2: Erste und letzte Zahl — MIT ITERATOREN:
    //   *zahlen.begin()   ist das erste Element,
    //   *(zahlen.end()-1) das letzte.
    //   Ausgabe:  Erste: <a>, Letzte: <b>
    std::cout << "Erste: " << 0 << ", Letzte: " << 0 << "\n";

    // TODO 3: Groesste Differenz zweier BENACHBARTER Zahlen
    //   (Absolutbetrag!) — Paare zahlen[i], zahlen[i+1], Schleife
    //   stoppt beim vorletzten Index.
    int differenz = 0;
    std::cout << "Groesste Differenz: " << differenz << "\n";

    return 0;
}
