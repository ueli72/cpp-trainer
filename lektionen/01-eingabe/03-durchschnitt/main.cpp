#include <iostream>
#include <iomanip>

// Skelett: Nur das Formatierungs-Werkzeug steht — der Rest ist deine.
int main() {
    int a, b, c;

    // TODO 1: Drei Zahlen einlesen (eine Zeile, Leerzeichen getrennt)
    std::cin >> a >> b >> c;

    std::cout << std::fixed << std::setprecision(2);

    // TODO 2: Durchschnitt = (a + b + c) / 3.0
    //   Achtung: / 3.0 statt / 3 — sonst ist das Ergebnis ganzzahlig!
    //   Ausgabe:   Durchschnitt: 2.00

    return 0;
}
