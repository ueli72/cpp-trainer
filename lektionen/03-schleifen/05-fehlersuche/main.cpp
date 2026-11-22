#include <iostream>

int main() {
    int n;
    std::cin >> n;

    for (int i = 1; i < n; i = i + 1) {
        for (int j = 1; j <= i; j = j + 1) {
            std::cout << "*";
        }
        std::cout << "\n";
    }

    int summe = 0;
    for (int i = 1; i <= n; i = i + 1) {
        summe = summe + i
    }
    std::cout << "Summe: " << summe << "\n";

    return 0;
}
