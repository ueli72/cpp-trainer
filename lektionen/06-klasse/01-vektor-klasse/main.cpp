#include <iostream>
#include <iomanip>

// Eine class ist wie ein struct: Sie bündelt Daten mit den Funktionen,
// die dazugehören (Methoden). Der Unterschied: In einer class ist alles
// standardmäßig "privat" (von außen unsichtbar) — mit "public:" gibst
// du den Zugang von außen frei.
class Vector {
public:
    double x;
    double y;
    double z;

    // Liest DIESEN Vektor im Format x,y,z ein.
    // Innerhalb einer Methode greifst du direkt auf die Member zu
    // (x statt a.x) — sie gehören immer zu dem Objekt, mit dem die
    // Methode aufgerufen wurde: a.liesVonEingabe() füllt a.
    void liesVonEingabe() {
        char komma;
        std::cin >> x >> komma >> y >> komma >> z;
    }

    // Gibt das Skalarprodukt von DIESEM Vektor mit einem anderen aus (eine Zahl).
    // "other" ist der zweite Vector, der beim Aufruf übergeben wird:
    // a.skalarprodukt(b);  →  a rechnet, b landet in other.
    void skalarprodukt(Vector other) {
        // TODO 1: Berechne das Skalarprodukt
        //   x*other.x + y*other.y + z*other.z
        // und gib es aus:   Skalarprodukt: <wert>

    }

    // Gibt das Vektorprodukt (auch Kreuzprodukt genannt) von DIESEM
    // Vektor mit einem anderen aus (Format x,y,z).
    void vektorprodukt(Vector other) {
        // Die drei Formeln für die Komponenten des Ergebnisses:
        //   cx = y*other.z - z*other.y
        //   cy = z*other.x - x*other.z
        //   cz = x*other.y - y*other.x
        // TODO 2: Berechne die drei Komponenten und gib sie aus:
        //   Kreuzprodukt: <cx>,<cy>,<cz>

    }
};

int main() {
    Vector a, b;

    a.liesVonEingabe();   // Eingabe landet direkt in a.x, a.y, a.z
    b.liesVonEingabe();

    // Zwei Nachkommastellen — gilt für alle folgenden Ausgaben,
    // auch die aus den Methoden.
    std::cout << std::fixed << std::setprecision(2);

    a.skalarprodukt(b);   // beide Ergebnisse kommen aus den Methoden …
    a.vektorprodukt(b);   // … diese Zeilen stehen schon fertig hier

    return 0;
}
