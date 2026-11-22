#include <iostream>

// Skelett: Die Schleife über die 8 Bit-Stellen steht — die Bits sind deine.
int main() {
    int zahl;
    std::cin >> zahl;

    // stelle läuft 128, 64, 32, 16, 8, 4, 2, 1 — die Werte der 8 Bits.
    for (int stelle = 128; stelle >= 1; stelle = stelle / 2) {
        // TODO: Für jede Stelle genau EIN Zeichen ausgeben ("1" oder "0"),
        //   ohne Zeilenumbruch:
        //   passt die Stelle noch in zahl?  dann "1" und zahl -= stelle
        //   sonst                           dann "0"
    }

    std::cout << "\n";

    return 0;
}
