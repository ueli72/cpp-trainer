#include <iostream>

void add(int* res, const int* a, const int* b) {
    *res = *a + *b;
}

void tauschen(int* a, int* b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

int main() {
    int a, b, summe = 0;
    std::cin >> a >> b;
    add(&summe, &a, &b);
    std::cout << "Summe: " << summe << "\n";
    tauschen(&a, &b);
    std::cout << "Getauscht: " << a << " " << b << "\n";
}
