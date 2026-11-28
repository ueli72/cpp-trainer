#include <iostream>

// Vorstufe zur Pruefungsaufgabe "Decimal to arbitrary base" (Exam 2022-02):
// dieselbe Idee in zwei Stufen — erst Ziffern ableiten, dann zu einer
// Zahl zusammenbauen.
int main() {
    int n = 0;
    int b = 0;
    std::cin >> n >> b;

    // TODO 1: Ziffern von n zur Basis b in ABLEIT-Reihenfolge ausgeben:
    //   wiederholt  n % b  (mit einem Leerzeichen davor) und  n /= b —
    //   solange n > 0.  Der Text steht schon da:
    std::cout << "Ziffern (von hinten):";

    // TODO 2: Das ist die Kerntechnik der Pruefungsaufgabe — die Ziffern
    //   zu EINER Zahl zusammenbauen. Zwei Hilfsvariablen fuehren:
    //   ergebnis (Start 0) und stellenwert (Start 1). Pro Ziffer:
    //     ergebnis += stellenwert * (n % b);  n /= b;  stellenwert *= 10;
    //   Achtung: TODO 1 hat n schon klein gemacht — nimm eine Kopie von n.
    int ergebnis = 0;
    std::cout << "\nAls Zahl: " << ergebnis << "\n";

    return 0;
}
