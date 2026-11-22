#include <iostream>

// Skelett: Signatur und main stehen — die Rekursion ist deine.
// int quersumme(int n):
//   Abbruchbedingung: das kleinste Problem direkt beantworten
//   Rekursiver Schritt: etwas Kleineres aufrufen und daran etwas anhängen
// (Das Muster steht in Rekursion 01 — potenz — und erklärt README.md.)
int quersumme(int n) {
    // TODO: Abbruch + rekursiver Schritt — ohne Schleife!
    return 0;  // ← Platzhalter
}

int main() {
    int n;
    std::cin >> n;

    std::cout << "Quersumme: " << quersumme(n) << "\n";

    return 0;
}
