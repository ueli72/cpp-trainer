#include <iostream>

int main() {
    int zahl;
    std::cin >> zahl;

    int quersumme = 0;
    int gedreht = 0;
    while (zahl > 0) {
        quersumme = quersumme + zahl / 10
        gedreht = gedreht * 10 + zahl % 10;
        zahl = zahl / 10;
    }

    std::cout << "Quersumme: " << quersumme << "\n";
    std::cout << "Gedreht: " << gedreht << "\n";

    return 0;
}
