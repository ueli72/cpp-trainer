#include <iostream>

class Vector {
    double x;
    double y;
    double z;
};

int main() {
    Vector a, b;
    char komma;
    std::cin >> a.x >> komma >> a.y >> komma >> a.z;
    std::cin >> b.x >> komma >> b.y >> komma >> b.z;

    double skalar = a.skalarprodukt(b);

    std::cout << "Skalarprodukt: " << skalar << "\n";

    return 0;
}
