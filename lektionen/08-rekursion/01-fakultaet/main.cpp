#include <iostream>

// Rekursion = eine Funktion ruft sich selbst.
// Jede Rekursion braucht zwei Dinge:
//   1. ABBRUCHBEDINGUNG: das einfachste Beispiel, direkt beantwortbar
//   2. REKURSIVER SCHRITT: das Problem etwas kleiner machen
//
// Lauffähiges Beispiel — potenz(b, e) = b^e:
//   b^0 = 1                 (Abbruch: nichts zu tun)
//   b^e = b * b^(e-1)       (Schritt: exponents um 1 verkleinern)
int potenz(int b, int e) {
    if (e == 0) {
        return 1;                    // Abbruchbedingung
    }
    return b * potenz(b, e - 1);     // rekursiver Schritt
}

// TODO 1: Baue fakultaet(n) nach demselben Muster:
//   wenn n == 0  →  gib 1 zurück           (Abbruchbedingung)
//   sonst        →  gib n * fakultaet(n - 1) zurück  (Schritt)
int fakultaet(int n) {
    return 0;  // ← Platzhalter: Ersetze mich!
}

int main() {
    int n;
    std::cin >> n;

    std::cout << "Fakultaet: " << fakultaet(n) << "\n";

    return 0;
}
