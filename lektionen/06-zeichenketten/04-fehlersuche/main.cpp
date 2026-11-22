#include <iostream>
#include <string>

int main() {
    std::string wort;
    std::cin >> wort;

    int vokale = 0;
    std::string rueckwaerts = "";
    for (int i = 0; i < wort.length(); i = i + 1) {
        char c = wort[i];
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            vokale = vokale + 1    // BUG: Semikolon fehlt
        }
        rueckwaerts = rueckwaerts + c;
    }

    std::cout << "Vokale: " << vokale << "\n";
    std::cout << "Rueckwaerts: " << rueckwaerts << "\n";
    return 0;
}
