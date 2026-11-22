#include <iostream>

int fakultaet(int n) {
    if (n == 0) {
        return 0;
    }
    return n + fakultaet(n - 1);
}

int main() {
    int n;
    std::cin >> n;
    std::cout << "Fakultaet: " << fakultaet(n) << "\n";
    return 0;
}
