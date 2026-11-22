#include <iostream>

// Skelett: Die äußere Schleife (Zeilen) steht — die Sterne sind deine.
int main() {
    int n;
    std::cin >> n;

    // Zeile i bekommt GENAU i Sternchen — Zeile 1: "*", Zeile 4: "****"
    for (int i = 1; i <= n; i = i + 1) {
        // TODO 1: Innere Schleife: gib i-mal "*" aus (ohne Zeilenumbruch)
        // TODO 2: Danach "\n" für das Zeilenende
    }

    return 0;
}
