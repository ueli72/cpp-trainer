#include <iostream>
#include <string>

// Skelett: die Struktur steht — du ergaenzst die TODO-Bloecke.
int main() {
    std::string wort;
    std::cin >> wort;

    int vokale = 0;
    std::string rueckwaerts = "";

    // TODO 1: Das Wort durchlaufen und die Vokale zaehlen:
    //   Vokale sind a, e, i, o und u (Kleinbuchstaben).

    // TODO 2: Das Wort rueckwaerts aufbauen — jedes Zeichen VORN anfuegen.

    std::cout << "Vokale: " << vokale << "\n";
    std::cout << "Rueckwaerts: " << rueckwaerts << "\n";

    return 0;
}
