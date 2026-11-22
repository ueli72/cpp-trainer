#include <iostream>
#include <iomanip>

// Skelett: Der Typ und der erste Posten stehen — der Rest ist deine.
struct Posten {
    double preis;
    int anzahl;
};

int main() {
    Posten p1, p2;

    std::cin >> p1.preis >> p1.anzahl;   // erster Posten — steht schon

    // TODO 1: Zweiten Posten einlesen (gleiches Muster mit p2)
    // TODO 2: Gesamt = p1.preis * p1.anzahl + p2.preis * p2.anzahl
    // TODO 3: Ausgabe mit 2 Nachkommastellen:   Gesamt: 19.75
    //   (std::fixed << std::setprecision(2) nicht vergessen)

    return 0;
}
