#include <iostream>

// So sieht eine Verzweigung aus — dieses Beispiel läuft schon:
int main() {
    int zahl;
    std::cin >> zahl;

    // if (Bedingung) { … } else { … } — GENAU EIN Zweig läuft.
    // Die Bedingung ist entweder wahr oder falsch.
    if (zahl > 10) {
        std::cout << "gross" << "\n";
    } else {
        std::cout << "klein" << "\n";
    }

    // TODO 1: Ersetze die Bedingung durch den Gerade-Test:
    //   zahl % 2 == 0    ("Rest bei Division durch 2 ist 0")
    // TODO 2: Passe die beiden Ausgaben an: "gerade" und "ungerade".
    //   (Der Vergleich == hat ZWEI Gleichheitszeichen — eines = wäre
    //   eine Zuweisung, kein Vergleich!)

    return 0;
}
