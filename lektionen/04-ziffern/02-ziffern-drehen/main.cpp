#include <iostream>

// Skelett: Ziel-Variable und Ausgabe stehen — die Dreh-Maschine ist deine.
int main() {
    int zahl;
    std::cin >> zahl;

    int gedreht = 0;

    // TODO: while (zahl > 0) — in jeder Runde:
    //   letzte Ziffer holen:        zahl % 10
    //   gedreht aufbauen:           gedreht = gedreht * 10 + ziffer
    //   Zahl verkürzen:             zahl = zahl / 10
    // (1200 → 0, 0, 2, 1 → gedreht: 0 → 0 → 2 → 21 — führende Nullen
    //  verschwinden von selbst.)

    std::cout << gedreht << "\n";

    return 0;
}
