#include <iostream>
#include <vector>

using vec = std::vector<int>;

void lies_vector(vec& v) {
    int size;
    std::cin >> size;
    v = vec(size);
    for (int i = 0; i < int(v.size()); ++i) {
        std::cin >> v[i];
    }
}

// SOLL: das Skalarprodukt von v1 und v2 ausgeben — oder "error",
// wenn die Groessen nicht uebereinstimmen.
void skalarprodukt(const vec& v1, const vec& v2) {
    if (int(v1.size()) != int(v2.size())) {
        std::cout << "error\n";
        return;
    }
    int res = 1;                                    // BUG: Startwert einer Summe
    for (int i = 0; i < int(v1.size()) - 1; ++i) {  // BUG: letzter Wert fehlt
        res += v1[i] * v2[i]
    }
    std::cout << res << "\n";
}

int main() {
    vec v1, v2;
    lies_vector(v1);
    lies_vector(v2);
    skalarprodukt(v1, v2);
}
