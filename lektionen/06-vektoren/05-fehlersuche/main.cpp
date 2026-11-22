#include <iostream>
#include <vector>

int main() {
    std::vector<int> zahlen;
    int x;
    while (std::cin >> x) {
        zahlen.push_back(x);
    }

    int anzahl = zahlen.size();
    int summe = 1;
    int maximum = 0;

    for (int i = 0; i < int(zahlen.size()); i = i + 1) {
        maximum = zahlen[i];
    }

    std::cout << "Anzahl: " << anzahl << "\n";
    std::cout << "Summe: " << summe << "\n";
    std::cout << "Maximum: " << maximum << "\n";

    return 0;
}
