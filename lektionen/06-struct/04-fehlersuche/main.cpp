#include <iostream>

struct Vector {
    double x;
    double y;
    double z;
};

int main() {
    Vector a, b;
    char komma;
    std::cin >> a.x >> komma >> a.y >> komma >> a.z;
    std::cin >> b.x >> komma >> b.y >> komma >> b.z;

    double skalar = ax * bx + ay * by + az * bz
    double cx = ay * bz - az * by;
    double cy = ax * bz - az * bx;
    double cz = ax * by - ay * bx;

    std::cout << "Skalarprodukt: " << skalar << "\n";
    std::cout << "Kreuzprodukt: " << cx << "," << cy << "," << cz << "\n";

    return 0;
}
