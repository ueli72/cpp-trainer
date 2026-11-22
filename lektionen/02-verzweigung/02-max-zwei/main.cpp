#include <iostream>

// Skelett: Der erste Fall steht — die anderen zwei sind deine.
int main() {
    int a, b;
    std::cin >> a >> b;

    if (a > b) {
        std::cout << "Groessere: " << a << "\n";
    }
    // TODO 1: Fall b größer als a → "Groessere: <b>"
    // TODO 2: Fall gleich → "Gleich"

    return 0;
}
