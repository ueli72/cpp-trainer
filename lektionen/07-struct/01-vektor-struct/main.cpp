#include <iostream>
#include <iomanip>

// Ein struct bündelt zusammengehörige Werte zu EINEM eigenen Typ.
// Statt sechs losen Variablen (ax, ay, az, bx, …) hast du zwei
// klare Objekte: a und b. Zugreifen tust du mit dem Punkt: a.x
struct Vector {
    double x;
    double y;
    double z;
};

int main() {
    Vector a, b;
    char komma;

    // Einlesen — der Trennzeichen-Trick aus der Eingabe-Reihe:
    // >> liest die Zahl bis zum Komma, das char "schluckt" es.
    // Weil a.x zum Objekt a gehört, landet alles ordentlich sortiert.
    std::cin >> a.x >> komma >> a.y >> komma >> a.z;
    std::cin >> b.x >> komma >> b.y >> komma >> b.z;

    std::cout << std::fixed << std::setprecision(2);

    // TODO 1: Skalarprodukt — eine EINZIGE Zahl:
    //   a.x*b.x + a.y*b.y + a.z*b.z
    //   Ausgabe:   Skalarprodukt: <wert>
    //
    // TODO 2: Kreuzprodukt — wieder ein Vektor, drei Formeln:
    //   cx = a.y*b.z - a.z*b.y
    //   cy = a.z*b.x - a.x*b.z
    //   cz = a.x*b.y - a.y*b.x
    //   Ausgabe:   Kreuzprodukt: <cx>,<cy>,<cz>

    return 0;
}
