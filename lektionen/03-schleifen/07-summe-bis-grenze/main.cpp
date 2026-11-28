#include <iostream>

// Die Anzahl der Runden kennt vorher niemand — genau dafür ist while da:
// die Schleife läuft, BIS die Bedingung umkippt.
int main() {
    int n;
    std::cin >> n;

    int k = 0;   // der jeweils nächste Summand

    // TODO 1: Lege die Summe an:  int summe = 0;
    // TODO 2: Solange summe kleiner als n ist:
    //   - erhöhe k um 1  (k ist dann der nächste Summand: 1, 2, 3, …)
    //   - addiere k zur summe
    // TODO 2: Gib danach NUR k aus (die Anzahl der Summanden).
    //   Platz für die Ausgabe hast du unten — das std::cout steht schon da.

    std::cout << k << "\n";

    return 0;
}
