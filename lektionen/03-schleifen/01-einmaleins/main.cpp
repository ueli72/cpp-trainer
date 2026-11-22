#include <iostream>

// So wiederholt man etwas — dieses Beispiel läuft schon:
int main() {
    int n;
    std::cin >> n;

    // for (Start; Bedingung; Schritt) { … }
    // i startet bei 1, die Schleife läuft, SOLANGE i <= 3 gilt,
    // und i wächst je Runde um 1 — der Block läuft also 3-mal:
    for (int i = 1; i <= 3; i = i + 1) {
        std::cout << "Zeile Nummer " << i << "\n";
    }

    // TODO 1: Lass i bis 10 laufen (Bedingung: i <= 10).
    // TODO 2: Gib stattdessen die Einmaleins-Zeile aus — pro Runde:
    //   "i * n = ergebnis"   also z. B.  "3 * 7 = 21"
    //   Alles mit << zusammensetzen: Texte in "...", Werte ohne.
    //   i * n rechnen und ausgeben kannst du direkt im <<.

    return 0;
}
