#include <iostream>

// Zwei Werkzeuge für Ziffern — dieses Beispiel läuft schon:
int main() {
    int zahl;
    std::cin >> zahl;

    // zahl % 10  →  die LETZTE Ziffer (Rest bei Division durch 10)
    // zahl / 10  →  die Zahl OHNE die letzte Ziffer (Ganzzahldivision:
    //               123 / 10 ist 12 — die .3 fällt weg)
    std::cout << "Letzte Ziffer: " << zahl % 10 << "\n";
    std::cout << "Ohne letzte:   " << zahl / 10 << "\n";

    // TODO 1: Kombiniere beide Werkzeuge in einer while-Schleife:
    //   while (zahl > 0) { … nimm die letzte Ziffer, schneide sie ab … }
    //   Die Schleife läuft, SOLANGE noch Ziffern da sind.
    //
    // TODO 2: Summiere die Ziffern in einer Variable (z. B. int summe = 0;)
    //   auf und gib am Ende aus:   Quersumme: <summe>

    return 0;
}
