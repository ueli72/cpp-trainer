#include <iostream>
#include <vector>

int main() {
    // std::vector<int> ist eine wachsende Liste fuer ganze Zahlen:
    //   zahlen.push_back(x) haengt x hinten an,
    //   zahlen.size() liefert die Anzahl der Elemente,
    //   zahlen[i] greift auf das i-te Element zu (ab 0 gezaehlt!).
    std::vector<int> zahlen;
    int x;
    while (std::cin >> x) {
        zahlen.push_back(x);
    }

    // TODO 1: Gib aus, wie viele Zahlen gelesen wurden:
    //   Anzahl: N
    //
    // TODO 2: Berechne die Summe aller Zahlen (Schleife ueber den Vektor)
    //   und gib sie aus:
    //   Summe: S

    return 0;
}
