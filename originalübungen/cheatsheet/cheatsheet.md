# C++ Cheatsheet – Syntax, Prüfungsaufgaben, Algorithmen
## 1 Programmgerüst, Typen, Konversion
```
#include <iostream>   // cin, cout
#include <vector>     // std::vector
#include <string>     // std::string
#include <cassert>    // assert
#include <cmath>      // sqrt, pow, abs
#include <climits>    // INT_MAX, INT_MIN
int main() {
  int x; std::cin >> x;
  std::cout << "x = " << x << '\n';   // oder std::endl (flush)
  return 0;
}
// Kompilieren:  g++ -std=c++20 -Wall main.cpp -o main
```
| Typ | Merkmale |
|---|---|
| `int` | 32 Bit, −2³¹ … 2³¹−1 (`INT_MAX` = 2147483647). **Signed-Overflow = undefined behavior** |
| `unsigned` | 0 … 2³²−1, Überlauf = modulo 2³². `0u − 1` = 4294967295! |
| `double` | 64 Bit IEEE 754, ≈15–16 Dezimalstellen (`float`: 32 Bit, ≈7) |
| `bool` | `true`=1 / `false`=0. `char`: `'a'`=97, `'0'`=48 → Ziffer: `c - '0'` |
- Deklarieren: `int a = 5; int b{5}; const int N = 10; auto z = 2.5; double d = 1e-3;`
- **Ganzzahldivision**: `7/2 == 3`, `-7/2 == -3` (Richtung 0), `-7 % 3 == -1` (Vorzeichen des Dividenden), `7/2.0 == 3.5`.
- `int(3.9) == 3`, `int(-3.9) == -3` (abschneiden, nicht runden). `static_cast<double>(a) / b` erzwingt Fliesskomma-Division.
- Mischen: `int` op `double` → `double`; `bool` → 0/1; `double` → `int` verliert Nachkommastellen.
- `v.size()` ist **unsigned**; `std::ssize(v)` ist signed (C++20) → in Schleifen `i < std::ssize(v)` benutzen.
- Strings: `std::string s = "abc"; s.size(); s[i]; s + "x"; s.substr(pos, len); s == t; s.empty(); s.erase(i, 1);`
## 2 Ausdrücke & Operatoren
| Prio | Operatoren | Prio | Operatoren |
|---|---|---|---|
| 1 | `a++ a-- () []` | 6 | `< <= > >=` |
| 2 | `++a --a !a -a` (rechts→links) | 7 | `== !=` |
| 3 | `* / %` | 8 | `&&` |
| 4 | `+ -` | 9 | `\|\|` |
| 5 | `<< >>` | 10 | `= += -= *= /=` (rechts→links) |
- **l-value**: hat Adresse, darf links von `=` stehen (`a`, `v[i]`, `++a`, `a = b`). **r-value**: temporärer Wert (`1`, `a+b`, `a++`) → `1 = a` und `a + b = c` ungültig, `a = 2 b` Syntaxfehler.
- `a = b = 5` ≡ `a = (b = 5)`: gültig, l-value, Wert 5. `++a + b++` ≡ `(a+1) + b` (r-value). `++a` liefert den neuen, `a++` den alten Wert.
- **Short-circuit**: `&&` / `||` werten links→rechts aus und stoppen, sobald das Ergebnis feststeht. `true || f()` ruft `f` nie auf. Schutz: `i < n && v[i] == x`. `&&` bindet stärker als `||`: `true || false && false` = `true || (false && false)`.
- **Vergleichsketten** sind links-assoziativ mit bool→int: `8 > 4 > 2 > 1` ≡ `((8>4)>2)>1` = `(1>2)>1` = **false**. `2 < a < 4` ist **immer true**. Richtig: `2 < a && a < 4`.
- `3 > (1 < true)`: `(1<true)` = false = 0 → `3 > 0` = true. `3 >= 3 == true` → `(3>=3) == 1` = true.
- Nie: `if (a = 0)` (Zuweisung!), `i + i++`, `a[i] = i++` (Auswertungsreihenfolge unspezifiziert → UB).
- De Morgan: `!(a && b) == (!a || !b)` und `!(a || b) == (!a && !b)`. XOR für bool: `a != b`.
### Natürliche Sprache → C++
| Text | C++ |
|---|---|
| a gerade und > 3 | `a % 2 == 0 && a > 3` |
| a > b und Differenz < 15 | `a > b && a - b < 15` |
| a höchstens 5-mal so gross wie b, mind. 5-mal so gross wie c | `a <= 5 * b && a >= 5 * c` |
| entweder A oder B (nicht beide) | `A != B` (bool) |
| (a und b beide false) oder c, aber nicht beides | `(!a && !b) != c` |
| x im Intervall [lo, hi] | `lo <= x && x <= hi` |
| a ist false und b gleich 0 | `!a && b == 0` |
| n durch 3 oder durch 5 teilbar, aber nicht durch beide | `(n%3 == 0) != (n%5 == 0)` |
| Schaltjahr | `y%4==0 && (y%100!=0 \|\| y%400==0)` |
## 3 Kontrollfluss
```
if (c) { ... } else if (d) { ... } else { ... }
switch (month) {                     // nur int / char / enum
  case 4: case 6: days = 30; break;  // ohne break: Fall-through!
  case 2:  days = 28; break;
  default: assert(false);            // ungültiger Wert
}
for (int i = 0; i < n; ++i) { ... }  // Zählschleife
while (cond) { ... }                 // Prüfung vor dem Körper
do { ... } while (cond);             // Körper min. 1x, Semikolon!
for (d = 2; n % d != 0; ++d);        // leerer Körper: kleinster
                                     // Teiler (n prim <=> d == n)
while (true) {                       // Abbruch mitten im Körper
  std::cin >> x;  if (x < 0) break;  ...
}
```
- `break`: Schleife/switch verlassen. `continue`: nächste Iteration. `return`: Funktion beenden.
- **Welche Schleife?** `for`: Zählvariable / bekannte Anzahl. `while`: Bedingung vorab (evtl. 0 Durchläufe). `do-while`: mind. einmal (Eingabe, „nochmal?“). `while(true)`+`break` nur wenn der Abbruch mitten im Körper liegt.
- **Schleife analysieren**: (1) Variablen für n = 0,1,2,3 in Tabelle durchrechnen → Formel erkennen (`x *= 2; --n` ⇒ x = 2ⁿ; `f *= n; --n` ⇒ n!). (2) Wertebereich: ab wann Overflow? (2ⁿ: n ≤ 30). (3) **Terminierung**: ein Wert (z.B. `n`), der in jedem Durchlauf strikt kleiner wird und nach unten beschränkt ist. (4) **Invariante**: Aussage, die vor und nach jedem Durchlauf gilt (z.B. `x == 2^(n0−n)`).
- Fakultät: `for (f = 1; n > 0; --n) f *= n;` · Potenz: `for (r = 1; x > 0; --x) r *= n;`
- **Schleife umschreiben** (for ↔ while ↔ do-while): Initialisierung vor die Schleife, Bedingung in `while(...)`, Update ans Ende des Körpers. Bei `do-while` Bedingung am Ende (Körper läuft 1x gratis).
```
// Beispiel: Summe zweier Eingaben, solange der Nutzer "1" antwortet
int again;
do { int i1, i2; std::cin >> i1 >> i2; std::cout << i1 + i2 << "\n";
     std::cin >> again; } while (again != 0);
```
---PAGE---
## 4 Funktionen, PRE/POST, Fehlersuche
```
// PRE:  b != 0           (Garantie, die der AUFRUFER geben muss)
// POST: returns a / b    (Garantie der FUNKTION: Rückgabe,
//                        Ausgaben, geänderte Referenzen)
int divide(int a, int b) {
  assert(b != 0);         // prüft PRE zur Laufzeit
  return a / b;
}
void print_twice(int n) { std::cout << n << n; }  // void: kein Wert
```
- **Header/Source**: `.h`: `#pragma once` + Deklaration `int divide(int a, int b);` · `.cpp`: `#include "f.h"` + Definition. Funktion muss vor Verwendung deklariert sein.
- **PRE** so schwach wie möglich, **POST** vollständig (auch Ausgaben und geänderte Referenzparameter!). Beispiele: `f(n,x)` mit Schleife `res *= n` (x-mal): PRE `x >= 0 && (n != 0 || x != 0)` (kein 0⁰), POST „returns nˣ“. Stellenzahl: PRE `n > 0`, POST „Anzahl Dezimalstellen von n“. `while (i*i != n) ++i;`: PRE „n ist Quadratzahl“, POST „returns √n“. Primzahltest mit `for (; n % i != 0; ++i);`: PRE `n ≥ 2` (bzw. `n != ±1`).
- **Typische Fehler**: Pfad ohne `return` (UB, z.B. nur `if (i%2==0) return true;`) → `return i % 2 == 0;`. Nicht initialisierte Variable (`double r; if (x != 0) r = 1.0/x; return r;`) → `double r = 0;`. Fehlende PRE (Division durch 0) → PRE + `assert` oder Sonderwert zurückgeben.
- Lokale Variablen existieren nur im Block `{}`. Parameter sind lokale Kopien (ausser Referenzen).
- **Überladen**: gleicher Name, verschiedene Parametertypen: `int abs2(int)`, `double abs2(double)`.
## 5 Parameterübergabe: Wert, Referenz, const
```
int  f(int i)          // Call by value: Kopie, Original unverändert
void g(int& i)         // Referenz = Alias: ändert das Original
int  h(const std::vector<int>& v)  // keine Kopie, nicht änderbar
void swap_ints(int& a, int& b) { int t = a; a = b; b = t; }
```
- `int&` verlangt einen l-value (`g(5)` Fehler); `const int&` darf auch r-value binden. `const`-Variablen/-Parameter nicht änderbar (`++i` bei `const int i` → Compilerfehler).
- **Nie** eine Referenz auf eine lokale Variable zurückgeben (dangling reference → undefiniert).
| Funktion | Analyse |
|---|---|
| `int foo(int i){ return ++i; }` | ok. POST: gibt i+1 zurück (Kopie), Original unverändert |
| `int foo(const int i){ return ++i; }` | **Fehler**: ändert const-Parameter |
| `int foo(int& i){ return ++i; }` | ok. POST: erhöht i um 1, gibt neuen Wert (Kopie) zurück |
| `int& foo(int i){ return ++i; }` | **undefiniert**: Referenz auf lokale Kopie |
| `const int& foo(int& i){ return ++i; }` | ok. Erhöht i, gibt const-Referenz auf i zurück |
## 6 std::vector, Matrix, Iteratoren
```
std::vector<int> v;               // leer
std::vector<int> a(5);            // 5x 0
std::vector<int> b(5, 7);         // 5x 7
std::vector<int> c = {1, 2, 3};
v.push_back(4);  v.pop_back();  v.back();  v.front();
v.empty();  v.clear();  v.resize(n);
v[i]                  // KEIN Bereichscheck! gültig: 0 .. size-1
for (int i = 0; i < std::ssize(v); ++i) v[i] *= 2;
for (int x : v) { ... }  // x = Kopie; `int& x` ändert direkt
using mat = std::vector<std::vector<int>>;
mat m(rows, std::vector<int>(cols, 0));   // rows x cols, alles 0
// m.size() = Zeilen, m[0].size() = Spalten, m[r][c] = Element
// Matrixprodukt A(n x k) * B(k x p);  Check: A[0].size() == B.size()
mat R(std::ssize(A), std::vector<int>(std::ssize(B[0]), 0));
for (int r = 0; r < std::ssize(A); ++r)
  for (int c = 0; c < std::ssize(B[0]); ++c)
    for (int k = 0; k < std::ssize(B); ++k)
      R[r][c] += A[r][k] * B[k][c];
// Iteratoren: Bereich [begin, end) halboffen
using iterator = std::vector<int>::const_iterator;
for (iterator it = v.begin(); it != v.end(); ++it) sum += *it;
// #include <algorithm>
std::swap(v[i], v[j]);  std::sort(v.begin(), v.end());
```
- Vektor immer als `&` / `const&` übergeben (sonst Kopie). `v2 = v1` kopiert, `v1 == v2` vergleicht elementweise. `end - begin` = Anzahl Elemente, `it + 1` = nächstes.
- Falle: `v.size() - 1` bei leerem Vektor = riesig (unsigned)! Zugriff `v[size]` ist UB.
- Matrix-Vektor: `res[r] += m[r][c] * v[c]`. Transponieren: `T[c][r] = m[r][c]`. Dimensionen vorher prüfen (sonst „error“).
## 7 Ein-/Ausgabe
```
std::cin >> a >> d;                     // überspringt Whitespace
while (std::cin >> x) { ... }           // bis EOF / Fehler
void read_vector(std::vector<int>& v) {  // bis negativ
  int x;
  while (std::cin >> x && x >= 0) v.push_back(x);
}
std::string line;  std::getline(std::cin, line);   // ganze Zeile
std::stringstream ss(line);  int y;     // #include <sstream>
while (ss >> y) v.push_back(y);         // Zahlen aus der Zeile lesen
std::cout << std::boolalpha << true;    // "true" statt 1
std::cout << std::fixed << std::setprecision(2) << 3.14159;  // 3.14
//                                         #include <iomanip>
std::cerr << "Fehler\n";                // Fehlerkanal
```
- Eingabeformat beachten: Zahl zuerst (`n`, dann `n` Werte) oder Endmarke (`-1`) oder bis EOF. `std::cout << x << " "` mit Leerzeichen, `"\n"` am Ende, exakt wie in der Aufgabe verlangt.
### Nützliche Standardfunktionen
- `std::min(a,b)`, `std::max(a,b)`, `std::abs(x)`, `std::sqrt(x)`, `std::pow(x,y)` (double!), `std::floor/ceil(x)`, `std::swap(a,b)`.
- `#include <algorithm>`: `std::sort(v.begin(), v.end())`, `std::reverse(v.begin(), v.end())`, `*std::max_element(v.begin(), v.end())`.
- Typ-Tipp: `size_t` ist unsigned; `long long` (64 Bit) für grosse Zwischenwerte: `long long f = 1; f *= n;`.
---PAGE---
## 8 struct & class
```
class Averager {
  double sum = 0;        // private (Standard bei class), Default-Wert
  int count = 0;
public:                  // von aussen zugänglich
  Averager() {}                         // Konstruktor (hier optional)
  Averager(double s, int c)             // Initialisierungsliste
    : sum(s), count(c) {}
  void add_value(double v) { sum += v; ++count; }
  double get_average() const {          // const: ändert Objekt nicht
    return count == 0 ? 0 : sum / count;   // a ? b : c
  }
  void reset();                         // Deklaration (in .h) ...
};
void Averager::reset() { sum = 0; count = 0; }  // ... (.cpp)

Averager a;  a.add_value(2.5);
std::vector<Averager> avs(3);  avs[1].reset();
```
- `struct` = `class`, aber Standardzugriff **public**; `class`: **private**. Zugriff auf private von aussen → Compilerfehler.
- Auf `const`-Objekten / `const&`-Parametern nur `const`-Methoden aufrufbar. Elementzugriff `obj.member`.
- PRE/POST einer Methode: PRE über Parameter **und** Objektzustand; POST beschreibt Rückgabe und neuen Zustand (z.B. `add(c)`: „Zähler von c um 1 erhöht“). **Klasseninvariante**: gilt nach jedem Konstruktor / jeder Methode (z.B. `count >= 0`).
- Nicht initialisierte `int`/`double`-Member sind Müll → Defaults (`= 0`) oder Konstruktor.
- Aufgabe „Typ/Wert eines Ausdrucks“: `a.get_average()` → `double`; `avs[1]` → `Averager`; `a.count` → Fehler, da private.
## 9 Operatoren überladen (Beispiel Complex)
- `a + b` ist nur Kurzschreibweise für `operator+(a, b)` (freie Funktion) **oder** `a.operator+(b)` (Member, linker Operand = `*this`). Name = `operator` + Symbol. Pro Operator genau eine Form wählen.
| Ausdruck | Definition |
|---|---|
| `a + b`, `a * b` | frei: `T operator+(const T& a, const T& b)` → **neues** Objekt, Rückgabe per Wert |
| `a == b`, `a < b` | frei: `bool operator==(const T& a, const T& b)`; `!=` aus `==` bauen |
| `-a` (unär) | Member: `T operator-() const` oder frei mit **einem** Parameter |
| `a += b` | Member: `T& operator+=(const T& o)`: ändert `*this`, `return *this;` |
| `a[i]` | Member: `X& operator[](int i)` (+ `const`-Version, die `X` zurückgibt) |
| `++a` / `a++` | Member: `T& operator++()` / `T operator++(int)` (Dummy-`int` = Postfix) |
| `2.0 * a` | frei (linker Operand ist kein `T`): `T operator*(double k, const T& a)` |
| `cout << a` | frei (linker Operand ist der Stream): `std::ostream& operator<<(std::ostream&, const T&)` |
| `cin >> a` | frei: `std::istream& operator>>(std::istream&, T&)` (Objekt non-const!) |
```
struct Complex {
  double re = 0, im = 0;
  Complex() {}
  Complex(double r, double i) : re(r), im(i) {}
  Complex& operator+=(const Complex& o) {      // a += b
    re += o.re;  im += o.im;
    return *this;              // *this = das Objekt selbst (Referenz)
  }
  Complex operator-() const {                  // -a
    return Complex(-re, -im);
  }
  double& operator[](int i) { return i == 0 ? re : im; }  // c[0]
  Complex& operator++() { ++re; return *this; }            // ++c
  Complex operator++(int) {                                // c++
    Complex alt = *this;  ++re;  return alt;   // alter Wert
  }
};
Complex operator+(const Complex& a, const Complex& b) {
  Complex r = a;  r += b;  return r;           // += wiederverwenden
}
Complex operator*(const Complex& a, const Complex& b) {
  return Complex(a.re*b.re - a.im*b.im, a.re*b.im + a.im*b.re);
}
Complex operator*(double k, const Complex& a) {  // 2.0 * c
  return Complex(k * a.re, k * a.im);
}
bool operator==(const Complex& a, const Complex& b) {
  return a.re == b.re && a.im == b.im;
}
bool operator!=(const Complex& a, const Complex& b) {
  return !(a == b);
}
bool operator<(const Complex& a, const Complex& b) {  // Betrag
  return a.re*a.re + a.im*a.im < b.re*b.re + b.im*b.im;
}
std::ostream& operator<<(std::ostream& out, const Complex& a) {
  return out << "[" << a.re << "," << a.im << "]";
}
std::istream& operator>>(std::istream& in, Complex& a) {  // [re,im]
  char c;                       // fängt '[' ',' ']' ab
  return in >> c >> a.re >> c >> a.im >> c;
}
```
- `<<` / `>>`: Stream **per Referenz** übernehmen und **zurückgeben** (Verkettung `cout << a << b`).
- Rückgabe: `+ - * /` neues Objekt **per Wert**; `+= ++a` und `=` **Referenz** auf `*this`; Vergleiche `bool`.
- Member `const` machen, wenn sie das Objekt nicht ändern. Sind die Member `private`, braucht `operator<<` Zugriff: `friend`-Deklaration in der Klasse oder öffentliche Getter.
- Division: (a+bi)/(c+di) = ((ac+bd) + (bc−ad)i) / (c²+d²). Betrag: `std::sqrt(re*re + im*im)`.
- Header: nur Deklarationen (`Complex operator+(const Complex&, const Complex&);`), Definitionen in `.cpp`. Nicht überladbar: `::`, `.`, `?:`, `sizeof`.
## 10 Gleitkomma & Zahlendarstellung
- `double` = ±1.m × 2ᵉ (1 Bit Vorzeichen, 11 Exponent, 52 Mantisse). Übungsmodell: normalisiert **1.b₁b₂b₃ × 2ᵉ** (3 Nachkommabits).
- Dezimal → Binär: Vorkomma durch ÷2 (Reste), Nachkomma wiederholt ×2 (Vorkommastelle ablesen). `0.75 = 0.11₂ = 1.100×2⁻¹`, `7 = 111₂ = 1.110×2²`, `3.1416 = 11.001001…₂` → `1.101×2¹` (=3.25, gerundet, Fehler 0.1084), `2.718` → `1.011×2¹` (=2.75). Exponentenbereich des Modells beachten (Aufgabe: 0.11 → `1.000×2⁻³`).
- Zurück: `1.101×2¹` = (1 + ½ + ⅛)·2 = 3.25. Fehler = |exakt − Darstellung|.
- **Absorption**: grosse + kleine Zahl → kleine geht verloren (`6.0 + 0.11` bleibt `1.100×2²`; `1e16 + 1 == 1e16`).
- Nie `==` auf `double`: `0.1 + 0.2 != 0.3` → `std::abs(a - b) < 1e-9`. Zu grosse Zwischenwerte (Fakultät) → `inf` / `nan`.
```
// 0 <= x < 2: Binärentwicklung b0.b1b2...b15
int b = x >= 1;  std::cout << b << ".";
for (int i = 1; i < 16; ++i) {
  x -= b;  x *= 2;  b = x >= 1;  std::cout << b;
}
// Pi (Leibniz): pi = 4 (1 - 1/3 + 1/5 - ...), m Terme
double pi = 0;
for (int j = 0; j < m; ++j)
  pi += (j % 2 == 0 ? 4.0 : -4.0) / (2*j + 1);
// Pi = 2 * Summe j!/(3*5*...*(2j+1)), inkrementell (schneller)
double pi2 = 2, nu = 2, de = 1;           // j = 0: Term 2
for (int j = 1; j < m; ++j) {
  nu *= j;  de *= 2*j + 1;  pi2 += nu / de;
}
// Rundung double -> int, .5 weg von 0 (Ergebnis im int-Bereich)
int round_number(double x) {
  int t = x;  double d = x - t;           // d ist exakt
  if (d >= 0.5)  return t + 1;
  if (d <= -0.5) return t - 1;
  return t;
}
```
## 11 Ganzzahl-Tricks
- Ziffern: letzte `n % 10`, abschneiden `n / 10`. Stellenzahl: `do { ++c; n /= 10; } while (n > 0);` · Ziffernsumme: `for (; n > 0; n /= 10) s += n % 10;`
- Basiswechsel (b<10): `for (pos = 1; n != 0; n /= b, pos *= 10) r += pos * (n % b);` (10 → Basis 2 = 1010; 14 → Basis 9 = 15).
- **Rundung a/b (a,b > 0)**: `(a + b/2) / b` (kaufmännisch). Gerundeter Parallelwiderstand: `R = (R12*R34 + (R12+R34)/2) / (R12+R34);`
- **Overflow vor dem Rechnen prüfen**: `a + b` überläuft ⇔ `a > INT_MAX - b` (b ≥ 0); `a * b` ⇔ `a > INT_MAX / b`.
- Multiplikation nur mit `+`: 29a = 16a+8a+4a+a: `b=a+a; c=b+b; d=c+c; e=d+d;` → `e+d+c+a`.
- Parität: `n % 2 != 0` (nicht `== 1`: falsch bei n<0). Teilbar: `n % k == 0`. Wochentag: `Tage_seit_1900 % 7` (0 = Montag).
- Datum: `Tage(Jahr) = 365 + Schaltjahr`. Tage seit 1900 = Tage der vollen Jahre + Tage der vollen Monate + (Tag−1).
---PAGE---
## 12 Typische iterative Algorithmen
```
bool is_prime(int n) {                    // O(sqrt n)
  if (n < 2) return false;
  for (int d = 2; d * d <= n; ++d)
    if (n % d == 0) return false;
  return true;
}
int gcd(int a, int b) {                   // Euklid
  while (b != 0) { int t = a % b;  a = b;  b = t; }
  return a;
}
// Fibonacci (a = F_i, b = F_i+1), Overflow vor dem Addieren prüfen
int a = 0, b = 1;
for (int i = 0; i < n; ++i) {
  if (a > INT_MAX - b) break;
  int nx = a + b;  a = b;  b = nx;
}
int max_of(const std::vector<int>& v) {   // PRE: !v.empty()
  int m = v[0];
  for (int x : v) if (x > m) m = x;
  return m;
}
int count_of(const std::vector<int>& v, int t) {
  int c = 0;
  for (int i = 0; i < std::ssize(v); ++i) if (v[i] == t) ++c;
  return c;
}
void bubble_sort(std::vector<int>& v) {   // O(n²)
  bool swapped;                           // Inv: grösste k fix
  do {
    swapped = false;
    for (int i = 1; i < std::ssize(v); ++i)
      if (v[i] < v[i-1]) { std::swap(v[i], v[i-1]); swapped = true; }
  } while (swapped);                      // terminiert: <= n Runden
}
void selection_sort(std::vector<int>& v) {  // O(n²)
  for (int i = 0; i + 1 < std::ssize(v); ++i) {
    int m = i;
    for (int j = i + 1; j < std::ssize(v); ++j)
      if (v[j] < v[m]) m = j;
    std::swap(v[i], v[m]);
  }
}
int binary_search(const std::vector<int>& v, int x) {
  // PRE: v aufsteigend sortiert; O(log n)
  int lo = 0, hi = std::ssize(v) - 1;
  while (lo <= hi) {
    int mid = lo + (hi - lo) / 2;         // kein Overflow von lo+hi
    if (v[mid] == x) return mid;
    else if (v[mid] < x) lo = mid + 1;
    else hi = mid - 1;
  }
  return -1;                              // nicht gefunden
}
// Paare i<j mit v[i]+v[j] == sum (Iteratoren), O(n²)
int pairs_with_sum(int sum, iterator b, iterator e) {
  int c = 0;
  for (iterator i = b; i != e; ++i)
    for (iterator j = i + 1; j != e; ++j)
      if (*i + *j == sum) ++c;
  return c;
}
// Run-length-Encoding: Folge -> (Länge, Wert)-Paare, Länge max. 255
int prev, len = 1;  std::cin >> prev;
while (std::cin >> x && x != -1) {
  if (x != prev || len == 255) {
    std::cout << len << " " << prev << " ";
    len = 1;  prev = x;
  } else ++len;
}
std::cout << len << " " << prev;          // letzten Lauf!
// Decode: Paar (len, val) lesen; len-mal val ausgeben
void reverse_vec(std::vector<int>& v) {   // zwei Zeiger von aussen
  for (int i = 0, j = std::ssize(v) - 1; i < j; ++i, --j)
    std::swap(v[i], v[j]);
}
bool is_sorted(const std::vector<int>& v) {
  for (int i = 1; i < std::ssize(v); ++i)
    if (v[i] < v[i-1]) return false;      // Gegenbeispiel
  return true;
}
std::vector<bool> sieve(int n) {          // Sieb des Eratosthenes
  std::vector<bool> p(n + 1, true);       // PRE: n >= 1
  p[0] = p[1] = false;
  for (int i = 2; i * i <= n; ++i)
    if (p[i]) for (int j = i * i; j <= n; j += i) p[j] = false;
  return p;                               // p[k] == true <=> k prim
}
int collatz(int n) {                  // Schritte bis 1; PRE n>=1
  int steps = 0;
  while (n != 1) { n = n % 2 == 0 ? n / 2 : 3 * n + 1; ++steps; }
  return steps;
}
```
- **Muster**: Akkumulieren (`s += ...`), Zählen (`if (...) ++c`), Suchen (früh `return`), Min/Max (Start mit `v[0]`!), Flag (`bool found = false`), zwei Zeiger / zwei Iteratoren, Laufindex mit Vorgänger (`v[i-1]`, Start bei 1).
- **Laufzeit**: eine Schleife O(n), verschachtelt O(n²), Halbieren O(log n), alle Teiler bis √n O(√n).
## 13 Rekursion
```
R f(Parameter) {
  if (Basisfall) return ...;    // terminiert OHNE weiteren Aufruf
  ... f(kleineres Problem) ...  // Argument nähert sich dem Basisfall
}
```
- **Rezept**: (1) Basisfall(e) festlegen. (2) Rekursionsschritt: Problem auf kleineres zurückführen. (3) **Terminierung**: Argument wird bei jedem Aufruf strikt kleiner (`n-1`, `n/2`, Intervall `lo..hi` schrumpft) und erreicht den Basisfall (in **jedem** Zweig!). (4) PRE/POST gelten auch für den rekursiven Aufruf (Induktion) → daraus POST der Funktion folgern.
```
int fact(int n) { return n <= 1 ? 1 : n * fact(n - 1); } // n>=0
int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }
int fib(int n) {                          // exponentiell!
  return n < 2 ? n : fib(n-1) + fib(n-2);
}
int power(int b, int e) {                 // b^e in O(log e)
  if (e == 0) return 1;
  int h = power(b, e / 2);
  return e % 2 == 0 ? h * h : h * h * b;
}
bool is_odd(int n) {   // PRE n>=0, POST: true gdw n ungerade
  return n == 0 ? false : !is_odd(n - 1);
}
int digit_sum(int n) {
  return n < 10 ? n : n % 10 + digit_sum(n / 10);
}
void reverse_digits(int n) {  // PRE n>=0; POST Ziffern rückwärts
  if (n < 10) std::cout << n;
  else { std::cout << n % 10; reverse_digits(n / 10); }
}
void print_bin(int n) {       // 10 -> 1010 (Ausgabe NACH Aufruf)
  if (n > 1) print_bin(n / 2);
  std::cout << n % 2;
}
void print_bin_rev(int n) {   // 10 -> 0101 (Ausgabe VOR Aufruf)
  std::cout << n % 2;
  if (n > 1) print_bin_rev(n / 2);
}
bool is_pal(const std::string& s, int l, int r) {
  return l >= r || (s[l] == s[r] && is_pal(s, l + 1, r - 1));
}
int rsum(const std::vector<int>& v, int i) {   // Summe ab Index i
  return i == std::ssize(v) ? 0 : v[i] + rsum(v, i + 1);
}
void stars(int n) {           // gibt 2^n Sterne aus
  if (n == 0) { std::cout << '*'; return; }
  stars(n - 1);  stars(n - 1);
}
int bsearch_rec(const std::vector<int>& v, int x, int lo, int hi) {
  if (lo > hi) return -1;
  int m = lo + (hi - lo) / 2;
  if (v[m] == x) return m;
  return v[m] < x ? bsearch_rec(v, x, m + 1, hi)
                  : bsearch_rec(v, x, lo, m - 1);
}
void hanoi(int n, char from, char via, char to, int& moves) {
  if (n == 0) return;                     // 2^n - 1 Züge
  hanoi(n - 1, from, to, via, moves);
  ++moves;                                // Scheibe from -> to
  hanoi(n - 1, via, from, to, moves);
}
void perms(std::string rest, std::string pre) { // alle n!
  if (rest.empty()) { std::cout << pre << ' '; return; }
  for (int i = 0; i < std::ssize(rest); ++i) {
    std::string r = rest;  r.erase(i, 1);
    perms(r, pre + rest[i]);
  }
}
void subsets(const std::vector<int>& v, int i,
             std::vector<int>& cur) {          // alle 2^n
  if (i == std::ssize(v)) { /* cur verarbeiten */ return; }
  subsets(v, i + 1, cur);                 // v[i] weglassen
  cur.push_back(v[i]);
  subsets(v, i + 1, cur);                 // v[i] nehmen
  cur.pop_back();
}
```
```
std::string rev(const std::string& s) {       // "abc" -> "cba"
  return s.empty() ? "" : rev(s.substr(1)) + s[0];
}
int rmax(const std::vector<int>& v, int i) {  // PRE: i < size
  if (i == std::ssize(v) - 1) return v[i];
  return std::max(v[i], rmax(v, i + 1));
}
long long memo[90];               // Memoization: Aufruf 2x = O(1)
long long fibm(int n) {
  if (n < 2) return n;
  if (memo[n] != 0) return memo[n];
  return memo[n] = fibm(n - 1) + fibm(n - 2);
}
bool od(int n);                               // Vorwärtsdeklaration
bool ev(int n) { return n == 0 ? true : od(n - 1); }
bool od(int n) { return n == 0 ? false : ev(n - 1); }
int binom(int n, int k) {                     // Pascal: n über k
  if (k == 0 || k == n) return 1;
  return binom(n - 1, k - 1) + binom(n - 1, k);
}
void triangle(int n) {                        // n=3: * / ** / ***
  if (n == 0) return;
  triangle(n - 1);                       // erst kleinere Zeilen
  for (int i = 0; i < n; ++i) std::cout << '*';
  std::cout << '\n';
}
```
- **Aufruf von Hand verfolgen** (Beispiel `stars(2)`): `stars(2)` → 2x `stars(1)` → je 2x `stars(0)` → 4 Basisfälle=Sterne; Baumtiefe n, Blätter 2ⁿ, Knoten insgesamt 2ⁿ⁺¹−1. Bei `fib`: Calls(n) = 2·F(n+1) − 1 (`fib(5)`: 15 Aufrufe) – Memoization reduziert auf O(n).
- **Reihenfolge der Ausgabe**: Ausgabe **vor** dem Aufruf → Reihenfolge der Aufrufe (`reverse_digits`: 4321); **nach** dem Aufruf → umgekehrt (`print_bin`: höchstes Bit zuerst).
- **Anzahl Aufrufe** (inkl. erstem): `f(n-1)` einmal → **n+1**. Zweimal (`g(n-1); g(n-1);`) → Σ2ⁱ = **2ⁿ⁺¹−1**. `fib(n)` ≈ 1.6ⁿ. Halbierung `f(n/2)` → **⌊log₂ n⌋+1**. Aufrufbaum zeichnen, Ebenen zählen.
- Jede Ebene belegt Stack → zu tiefe Rekursion (≈10⁵–10⁶) = Stack Overflow. Rekursion ↔ Schleife: gcd / Fakultät lassen sich iterativ schreiben.
## 14 Vorgehen nach Aufgabentyp
- **Ausdruck bewerten/gültig?** Klammern nach Präzedenz setzen, Typ jedes Teilausdrucks (int/bool/double) notieren, l-value/r-value prüfen, bei `&&`/`||` Short-circuit beachten, bool↔int (true=1).
- **Text → Bedingung**: jedes Satzstück einzeln übersetzen, mit `&&`/`||` verbinden, Grenzfälle (`<` vs `<=`) an Beispielzahlen testen.
- **Funktion reparieren**: (1) Gibt jeder Pfad einen Wert zurück? (2) Alles initialisiert? (3) Passt PRE (Division durch 0, Index, negative Zahl)? (4) Grenzen/Off-by-one?
- **PRE/POST formulieren**: Beispiele durchrechnen (kleine Eingaben, Randfälle 0, 1, negativ), dann allgemein: PRE = wann definiert/terminiert, POST = Rückgabewert + Seiteneffekte (Ausgabe, geänderte Referenzen).
- **Programm schreiben**: Eingabe lesen → Teilprobleme in Funktionen mit PRE/POST → Hauptprogramm; Eingabeformat und Ausgabeformat **exakt** einhalten (Leerzeichen, Zeilenumbruch, Text).
- **Klasse implementieren**: Members privat, Defaults setzen, Methoden `const` wenn sie nichts ändern, Methoden in `.cpp` mit `Klasse::name`.
- **Rekursive Funktion analysieren**: PRE/POST angeben → Terminierung (Argument schrumpft, Basisfall erreicht) → Aufrufanzahl als Formel (Baum zeichnen, Ebenen aufsummieren).
## 15 Prüfungs-Checkliste
- Overflow: `int` ab 2³¹ (Schleife: n ≤ 30 bei 2ⁿ). `int/int` schneidet ab. `%` bei negativen Zahlen.
- `=` vs `==`; Vergleichsketten; `&&` vor `||`; Short-circuit schützt Zugriffe; `switch` ohne `break`.
- `v.size()` unsigned (`size()-1`!); Index `0..size-1`; Vektor als `&` übergeben; nie Referenz auf Lokales zurückgeben.
- Jeden Pfad mit `return` abschliessen; Variablen initialisieren; PRE ⇒ `assert`.
- Rekursion: Basisfall zuerst, Argument schrumpft, **alle** Zweige terminieren; Ausgabe-Reihenfolge beachten.
- Letzter Lauf/Rest nach der Schleife (RLE!); `<` vs `<=`; `lo + (hi-lo)/2`.
