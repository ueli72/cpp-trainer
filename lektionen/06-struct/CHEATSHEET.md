# Cheatsheet — Structs

## Deklaration — außerhalb von `main`, ganz oben
```cpp
struct Posten {
    double preis;
    int anzahl;
};      // ← dieses Semikolon nicht vergessen!
```

## Benutzen: der Punkt
```cpp
Posten p1, p2;                        // zwei Objekte des neuen Typs
p1.preis = 3.5;                       // Member setzen
std::cin >> p1.preis >> p1.anzahl;    // direkt einlesen
Posten summe = p1;                    // kopieren/zuweisen geht auch
```
Zusammengehörige Werte reisen als **ein Paket** — statt sechs losen
Variablen hast du zwei klare Objekte (`a.x, a.y, …`).

## Vektor-Struct einlesen (Format x,y,z)
```cpp
struct Vector { double x; double y; double z; };
Vector a, b;
char komma;
std::cin >> a.x >> komma >> a.y >> komma >> a.z;
std::cin >> b.x >> komma >> b.y >> komma >> b.z;
```

## Formeln (Struct 01)
```
Skalarprodukt = a.x*b.x + a.y*b.y + a.z*b.z
cx = a.y*b.z - a.z*b.y      cy = a.z*b.x - a.x*b.z
cz = a.x*b.y - a.y*b.x      → Ausgabe: cx,cy,cz
```

## Brüche (Struct 03)
```cpp
struct Bruch { int zaehler; int nenner; };
char slash;
std::cin >> b.zaehler >> slash >> b.nenner;   // liest 3/4
```
Produkt = `z1*z2 / n1*n2` — **nicht kürzen**, Nenner 1 erlaubt.

## Nachkommastellen (Kassenbon)
```cpp
std::cout << std::fixed << std::setprecision(2) << gesamt;   // 19.75
```

## Formate der Lektionen (genau so ausgeben!)
```
Gesamt: 19.75        Produkt: 15/24
Skalarprodukt: 32.00        Kreuzprodukt: -3.00,6.00,-3.00
```

## Testen
`./trainer test struct/01` … `./trainer run struct/02` — sichtbar in `tests/`
