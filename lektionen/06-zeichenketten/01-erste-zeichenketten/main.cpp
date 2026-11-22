#include <iostream>
#include <string>

int main() {
    // std::string ist der Typ fuer Text ("Zeichenketten"):
    //   wort.length()   liefert die Laenge,
    //   wort[i]         das i-te Zeichen (ab 0 gezaehlt!),
    //   wort += "..."   haengt Text an.
    std::string wort;
    std::cin >> wort;

    // TODO 1: Laenge ausgeben:
    //   Laenge: N
    int laenge = 0;

    // TODO 2: Ersten und letzten Buchstaben ausgeben:
    //   Erster: <c>    Letzter: <c>
    //   (Werkzeug: wort[0] und wort[wort.length() - 1])

    return 0;
}
