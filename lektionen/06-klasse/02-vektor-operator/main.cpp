#include <iostream>
#include <iomanip>

// Skelett: Klasse und Operator-Signatur stehen — die Logik ist deine.
class Vector {
public:
    double x;
    double y;
    double z;

    // a * b  ist dasselbe wie  a.operator*(b)
    double operator*(Vector other) {
        // TODO 1: Gib das Skalarprodukt zurück:
        //   x*other.x + y*other.y + z*other.z
        return 0;  // ← Platzhalter
    }
};

int main() {
    Vector a, b;
    char komma;

    // TODO 2: Beide Vektoren je Zeile im Format x,y,z einlesen —
    //   Komma-Trick:  std::cin >> a.x >> komma >> a.y >> komma >> a.z;

    std::cout << std::fixed << std::setprecision(2);

    // TODO 3: Ausgabe:   Skalarprodukt: <wert>
    //   (Der Operator liefert das Ergebnis — main gibt aus.)

    return 0;
}
