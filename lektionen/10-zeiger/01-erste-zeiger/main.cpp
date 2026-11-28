#include <iostream>

// PRE:  a und b zeigen auf gueltige int-Werte.
// POST: Liefert einen Zeiger auf den groessten der beiden Werte.
int* max_ptr(int* a, int* b) {
    // TODO 1: vergleiche *a und *b und gib den passenden Zeiger zurueck
    return a;
}

// PRE:  a und b zeigen auf gueltige int-Werte.
// POST: Die Werte, auf die a und b zeigen, sind vertauscht.
void tauschen(int* a, int* b) {
    // TODO 2: die WERTS vertauschen (Zwischenvariable fuer *a nicht vergessen)
}

int main() {
    int a, b;
    std::cin >> a >> b;

    int* p = max_ptr(&a, &b);
    std::cout << "Max: " << *p << "\n";

    tauschen(&a, &b);
    std::cout << "Getauscht: " << a << " " << b << "\n";

    return 0;
}
