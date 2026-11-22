# C++ Lernskript – die ausführliche Version zum Cheatsheet
> **So benutzt du dieses Dokument:** Der Aufbau und die Nummerierung (1–15) sind identisch mit dem Cheatsheet. Hier steht, **warum** etwas so ist, mit mehr Beispielen und erklärten Ausgaben. Lies einen Abschnitt, löse die Übungen dazu und schau dann im Cheatsheet, wie derselbe Stoff in Kurzform aussieht. So gewöhnst du dich an das Cheatsheet, das du in der Prüfung benutzen darfst.
> Alle Beispiele mit `main` sind kompiliert und getestet. Die Zeilen `// Ausgabe:` zeigen, was das Programm wirklich ausgibt.

**Inhalt:** 1 Programmgerüst, Typen · 2 Ausdrücke & Operatoren · 3 Kontrollfluss · 4 Funktionen & PRE/POST · 5 Parameter, Referenzen, const · 6 Vector & Matrix · 7 Ein-/Ausgabe · 8 struct & class · 9 Operatoren überladen · 10 Gleitkomma · 11 Ganzzahl-Tricks · 12 Iterative Algorithmen · 13 Rekursion · 14 Vorgehen nach Aufgabentyp · 15 Checkliste

## 1 Programmgerüst, Typen, Konversion
> Cheatsheet: Abschnitt 1

### Das kleinste Programm
Jedes C++-Programm beginnt in der Funktion `main`. Mit `#include` holt man Bibliotheken, `std::cin` liest von der Tastatur, `std::cout` schreibt auf den Bildschirm. `<<` und `>>` zeigen die Richtung, in die die Daten fliessen.
```run
#include <iostream>

int main() {
  int a, b;                      // zwei Variablen (noch ohne Wert!)
  std::cin >> a >> b;            // liest zwei Zahlen, getrennt durch Leerzeichen/Zeilenumbruch
  std::cout << a << " + " << b << " = " << a + b << '\n';
  return 0;                      // 0 = alles in Ordnung
}
// Eingabe: 3 4
// Ausgabe: 3 + 4 = 7
```
- `'\n'` ist ein Zeilenumbruch. `std::endl` macht dasselbe und leert zusätzlich den Ausgabepuffer (langsamer, aber manchmal verlangt).
- Kompilieren auf der Konsole: `g++ -std=c++20 -Wall main.cpp -o main`, danach `./main`. `-Wall` schaltet nützliche Warnungen ein, z. B. für nicht initialisierte Variablen.
- Wichtige Bibliotheken: `<iostream>` (Ein-/Ausgabe), `<vector>`, `<string>`, `<cassert>` (`assert`), `<cmath>` (`sqrt`, `pow`, `abs`), `<climits>` (`INT_MAX`), `<algorithm>` (`sort`, `swap`), `<sstream>`, `<iomanip>`.

### Die wichtigsten Datentypen
| Typ | Bedeutung | Wertebereich / Eigenschaft |
|---|---|---|
| `int` | ganze Zahl | 32 Bit: −2 147 483 648 … 2 147 483 647 (`INT_MIN`…`INT_MAX`) |
| `unsigned` | ganze Zahl ≥ 0 | 0 … 4 294 967 295 |
| `long long` | grosse ganze Zahl | 64 Bit, ca. ±9·10¹⁸ |
| `double` | Kommazahl | ca. 15–16 gültige Dezimalstellen |
| `bool` | Wahrheitswert | `true` (=1) oder `false` (=0) |
| `char` | ein Zeichen | `'a'` ist die Zahl 97, `'0'` ist 48 |
| `std::string` | Text | `"Hallo"` |

> **Overflow bei `int`:** Rechnet man über `INT_MAX` hinaus, ist das Verhalten **undefiniert** (undefined behavior). Das Programm kann alles Mögliche tun. In Prüfungsaufgaben heisst das: Prüfe vorher, ob das Ergebnis noch in den Bereich passt (siehe Abschnitt 11).
> **`unsigned` dagegen läuft über** (rechnet modulo 2³²), das ist fest definiert, aber trotzdem tückisch:

```run
#include <iostream>

int main() {
  unsigned u = 0;
  --u;                            // 0 - 1 ergibt nicht -1, sondern ...
  std::cout << u << '\n';
  std::cout << (3u - 5u > 0) << '\n';   // "negative" unsigned-Differenz ist riesig => true (1)
}
// Ausgabe: 4294967295
// Ausgabe: 1
```

### Variablen deklarieren und initialisieren
```frag
int a = 5;          // Deklaration mit Anfangswert
int b{5};           // gleichwertig (Brace-Initialisierung); verbietet Verlust: int c{3.7}; ist ein Fehler
int d{};            // d == 0
const int N = 10;   // Konstante: N kann nicht mehr geändert werden
auto z = 2.5;       // Compiler leitet den Typ ab (hier double)
double e = 1e-3;    // 0.001 (Exponentschreibweise)
int x;              // ACHTUNG: x hat keinen definierten Wert (Müll), bis man es zuweist
```
> **Merke:** Lokale Variablen werden **nicht** automatisch auf 0 gesetzt. Eine nicht initialisierte Variable zu lesen ist ein klassischer Fehler (Abschnitt 4).

### Ganzzahldivision, Rest und Konversionen
Teilt man zwei `int`, wird das Ergebnis **abgeschnitten** (Richtung 0). `%` liefert den Rest. Das Vorzeichen des Rests ist das des Dividenden (linker Operand).
```run
#include <iostream>

int main() {
  std::cout << 7 / 2 << '\n';         // Ganzzahldivision
  std::cout << -7 / 2 << '\n';        // Richtung 0, nicht Richtung -unendlich
  std::cout << 7 % 3 << '\n';
  std::cout << -7 % 3 << '\n';        // Rest hat das Vorzeichen von -7
  std::cout << 7 / 2.0 << '\n';       // ein double im Spiel => Fliesskommadivision
  int a = 7, b = 2;
  std::cout << static_cast<double>(a) / b << '\n';   // Typ erzwingen, VOR dem Teilen
  std::cout << static_cast<double>(a / b) << '\n';   // zu spät: a/b ist schon 3
  std::cout << int(3.9) << ' ' << int(-3.9) << '\n'; // schneidet ab, rundet nicht
}
// Ausgabe: 3
// Ausgabe: -3
// Ausgabe: 1
// Ausgabe: -1
// Ausgabe: 3.5
// Ausgabe: 3.5
// Ausgabe: 3
// Ausgabe: 3 -3
```
Regeln für gemischte Typen: `int` ⊕ `double` ergibt `double`. `bool` wird zu 0/1. `double` nach `int` verliert die Nachkommastellen.

### Zeichen und Ziffern
Ein `char` ist eine kleine Zahl (ASCII). Die Ziffern `'0'`…`'9'` stehen hintereinander, darum rechnet man eine Ziffer in ihren Wert um mit `c - '0'`.
```run
#include <iostream>

int main() {
  char c = '7';
  int wert = c - '0';                       // '7' (55) - '0' (48) = 7
  std::cout << wert + 1 << '\n';
  std::cout << char('a' + 2) << '\n';       // 'a' + 2 ist 99 => 'c'
  std::cout << int('A') << '\n';
}
// Ausgabe: 8
// Ausgabe: c
// Ausgabe: 65
```

### Grösse von Containern und Strings
`v.size()` liefert einen **vorzeichenlosen** Typ. Das führt bei `v.size() - 1` für einen leeren Vektor zum Überlauf auf eine riesige Zahl. Darum nimmt man `std::ssize(v)`, das vorzeichenbehaftet ist (C++20).
```run
#include <iostream>
#include <vector>
#include <string>

int main() {
  std::vector<int> leer;
  std::cout << (leer.size() - 1 > 0) << '\n';        // riesige Zahl! (true)
  std::cout << (std::ssize(leer) - 1) << '\n';       // -1, wie erwartet
  std::string s = "abc";
  std::cout << s.size() << ' ' << s[1] << ' ' << s + "def" << ' ' << s.substr(1, 2) << '\n';
  s.erase(0, 1);                                     // löscht 1 Zeichen ab Index 0
  std::cout << s << '\n';
}
// Ausgabe: 1
// Ausgabe: -1
// Ausgabe: 3 b abcdef bc
// Ausgabe: bc
```
> **Übung 1:** Was gibt `std::cout << 5 / 2 * 2.0;` aus? (Lösung: `4`, weil zuerst `5/2 == 2` gerechnet wird.) Und `std::cout << 5 / 2.0 * 2;`? (Lösung: `5`.)

## 2 Ausdrücke & Operatoren
> Cheatsheet: Abschnitt 2

Ein **Ausdruck** hat immer einen **Typ** und einen **Wert**, zum Beispiel `3 + 4` (Typ `int`, Wert 7) oder `x < 3` (Typ `bool`).

### Präzedenz und Assoziativität
Die Präzedenz sagt, welcher Operator zuerst zugreift (wie „Punkt vor Strich“). Bei gleicher Präzedenz entscheidet die Assoziativität (meist von links nach rechts).
| Prio | Operatoren | Assoziativität |
|---|---|---|
| 1 | `a++  a--  ()  []` | links → rechts |
| 2 | `++a  --a  !a  -a` (unär) | rechts → links |
| 3 | `*  /  %` | links → rechts |
| 4 | `+  -` | links → rechts |
| 5 | `<<  >>` | links → rechts |
| 6 | `<  <=  >  >=` | links → rechts |
| 7 | `==  !=` | links → rechts |
| 8 | `&&` | links → rechts |
| 9 | `\|\|` | links → rechts |
| 10 | `=  +=  -=  *=  /=  %=` | rechts → links |

Im Zweifel setzt man Klammern. Zum Auswerten klammert man erst gedanklich komplett:
- `1 + 2 * 3 % 4` wird zu `1 + ((2 * 3) % 4)` = `1 + (6 % 4)` = 3.
- `a < b == c < d` wird zu `(a < b) == (c < d)`.
- `x = y = 5` wird zu `x = (y = 5)` (rechts-assoziativ).

### l-value und r-value
- Ein **l-value** hat eine Speicheradresse und darf links von `=` stehen: eine Variable `a`, ein Element `v[i]`, und auch `++a` oder `a = b`.
- Ein **r-value** ist ein temporärer Wert ohne Adresse: `5`, `a + b`, `a++`. Er darf nur rechts stehen.

```skip
int a = 1, b = 2, c = 3, d = 4;
a = b = 5;        // gültig: a = (b = 5). Wert des Ausdrucks 5, Typ int, ein l-value
1 = a;            // FEHLER: 1 ist ein r-value
a + b = c + d;    // FEHLER: a + b ist ein r-value
a = 2 b;          // FEHLER: Syntax, Operator fehlt
```
### Prä- und Postinkrement
`++a` erhöht `a` und liefert den **neuen** Wert (ein l-value). `a++` erhöht ebenfalls, liefert aber den **alten** Wert (ein r-value).
```run
#include <iostream>

int main() {
  int a = 1, b = 10;
  int x = ++a;            // a wird 2, x bekommt 2
  int y = b++;            // y bekommt 10, danach wird b 11
  std::cout << a << ' ' << x << ' ' << b << ' ' << y << '\n';

  int p = 3, q = 4;
  int r = ++p + q++;      // (p+1) + q = 4 + 4; danach q = 5
  std::cout << r << ' ' << p << ' ' << q << '\n';
}
// Ausgabe: 2 2 11 10
// Ausgabe: 8 4 5
```
> **Nie** dieselbe Variable in einem Ausdruck zweimal verändern oder lesen und verändern, zum Beispiel `i + i++` oder `a[i] = i++`. Die Reihenfolge der Auswertung ist nicht festgelegt, das Ergebnis ist undefiniert.

### Short-circuit-Auswertung
`&&` und `||` werten von links nach rechts aus und **hören auf**, sobald das Ergebnis feststeht. Die rechte Seite wird dann gar nicht berechnet.
```run
#include <iostream>

int aufrufe = 0;
bool f() { ++aufrufe; return true; }

int main() {
  bool r1 = true || f();      // links schon true => f() wird NICHT aufgerufen
  bool r2 = false && f();     // links false => f() wird NICHT aufgerufen
  std::cout << r1 << r2 << " Aufrufe: " << aufrufe << '\n';
  bool r3 = false || f();     // links false => rechts nötig
  std::cout << r3 << " Aufrufe: " << aufrufe << '\n';
}
// Ausgabe: 10 Aufrufe: 0
// Ausgabe: 1 Aufrufe: 1
```
Praktischer Nutzen: Schutz vor ungültigem Zugriff. In `i < n && v[i] == x` wird `v[i]` nur geprüft, wenn `i` gültig ist.

`&&` bindet stärker als `||`. Darum ist `true || false && false` dasselbe wie `true || (false && false)`, also `true`, und die rechte Seite wird nicht einmal berechnet.

### Vergleichsketten sind eine Falle
`8 > 4 > 2 > 1` bedeutet **nicht** „8 grösser als 4 grösser als 2 …“. Wegen der Links-Assoziativität wird `((8 > 4) > 2) > 1` gerechnet. `8 > 4` ist `true` (also 1), `1 > 2` ist `false` (0), und `0 > 1` ist `false`.
```run
#include <iostream>

int main() {
  std::cout << std::boolalpha;
  std::cout << (8 > 4 > 2 > 1) << '\n';             // ((8>4)>2)>1 = (1>2)>1 = 0>1
  int a = 100;
  std::cout << (2 < a < 4) << '\n';                 // (2<a)=1, 1<4 => IMMER true
  std::cout << (2 < a && a < 4) << '\n';            // so schreibt man es richtig
  std::cout << (3 > (1 < true)) << '\n';            // (1<true)=false=0, 3>0
  std::cout << (3 >= 3 == true) << '\n';            // (3>=3)==1
}
// Ausgabe: false
// Ausgabe: true
// Ausgabe: false
// Ausgabe: true
// Ausgabe: true
```
> Ebenso tückisch: `if (a = 0)` ist **Zuweisung**, kein Vergleich (Wert 0 = false). Mit `-Wall` warnt der Compiler oft davor.

### De Morgan und XOR
- `!(a && b)` ist gleich `!a || !b`.
- `!(a || b)` ist gleich `!a && !b`.
- „Entweder A oder B, aber nicht beide“ (XOR) schreibt man für `bool` als `A != B`.

### Natürliche Sprache nach C++
Übersetze Satzstück für Satzstück, verbinde sie dann mit `&&` oder `||`. Teste mit ein, zwei Zahlen, besonders an den Grenzen.
| Text | C++ | Erklärung |
|---|---|---|
| a ist eine gerade Zahl grösser 3 | `a % 2 == 0 && a > 3` | beide Bedingungen müssen gelten |
| a > b und der Abstand ist < 15 | `a > b && a - b < 15` | `a - b` ist wegen `a > b` positiv |
| a ist höchstens 5-mal so gross wie b, aber mindestens 5-mal so gross wie c | `a <= 5 * b && a >= 5 * c` | „höchstens“ ist `<=`, „mindestens“ ist `>=` |
| entweder A oder B, nicht beide | `A != B` | XOR für `bool` |
| a und b sind beide false, oder c ist true, aber nicht beides | `(!a && !b) != c` | XOR zwischen zwei Teilbedingungen |
| x liegt im Intervall [lo, hi] | `lo <= x && x <= hi` | nie `lo <= x <= hi`! |
| a ist false und b ist 0 | `!a && b == 0` | `!` bindet stärker als `==` |
| n durch 3 oder 5 teilbar, aber nicht durch beide | `(n % 3 == 0) != (n % 5 == 0)` | XOR |
| Schaltjahr | `y % 4 == 0 && (y % 100 != 0 \|\| y % 400 == 0)` | durch 4, ausser Jahrhunderte, ausser durch 400 |

> **Übung 2:** Gib an, ob gültig, und den Wert/Typ: `a = b + 1`, `a + 1 = b`, `++a + a++`, `(a > b) > c`. (Lösung: gültig/l-value; ungültig; gültig aber undefiniert, da `a` doppelt verändert wird; gültig, Typ `bool`.)

## 3 Kontrollfluss
> Cheatsheet: Abschnitt 3

### if / else und switch
```run
#include <iostream>

int main() {
  int n;
  std::cin >> n;
  if (n < 0) {
    std::cout << "negativ\n";
  } else if (n == 0) {
    std::cout << "null\n";
  } else {
    std::cout << "positiv\n";
  }
}
// Eingabe: 5
// Ausgabe: positiv
```
`switch` wählt je nach ganzzahligem Wert (`int`, `char`, `enum`) einen Einsprungpunkt. Ohne `break` läuft die Ausführung in den nächsten `case` weiter (**Fall-through**). Das nutzt man bewusst, um Fälle zusammenzufassen.
```run
#include <iostream>
#include <cassert>

int tage_im_monat(int monat, bool schaltjahr) {
  int tage;
  switch (monat) {
    case 4: case 6: case 9: case 11:   // vier Monate teilen sich diesen Code
      tage = 30;
      break;
    case 2:
      tage = schaltjahr ? 29 : 28;
      break;
    case 1: case 3: case 5: case 7: case 8: case 10: case 12:
      tage = 31;
      break;
    default:
      assert(false);                   // Monat ausserhalb 1..12 ist ein Programmfehler
  }
  return tage;
}

int main() {
  std::cout << tage_im_monat(2, true) << ' ' << tage_im_monat(6, false) << ' ' << tage_im_monat(12, false) << '\n';
}
// Ausgabe: 29 30 31
```
### Die drei Schleifen
```run
#include <iostream>

int main() {
  for (int i = 0; i < 3; ++i) std::cout << i << ' ';    // Zählschleife
  std::cout << '\n';

  int n = 3;
  while (n > 0) { std::cout << n << ' '; --n; }         // prüft VOR jedem Durchlauf
  std::cout << '\n';

  int k = 10;
  do { std::cout << k << ' '; ++k; } while (k < 5);     // Körper läuft mindestens 1x
  std::cout << '\n';
}
// Ausgabe: 0 1 2
// Ausgabe: 3 2 1
// Ausgabe: 10
```
**Welche Schleife passt?**
- `for`: es gibt eine Zählvariable und man weiss vorher, wie oft (oder bis wohin) gezählt wird.
- `while`: die Bedingung wird vor dem ersten Durchlauf geprüft. Null Durchläufe sind möglich.
- `do-while`: der Körper muss mindestens einmal laufen, typisch bei Eingaben („Nochmal? 0/1“).
- `while (true)` mit `break`: nur, wenn man mitten im Körper entscheidet (etwa nach dem Einlesen eines Werts).

```run
#include <iostream>

int main() {
  int summe = 0;
  while (true) {
    int x;
    std::cin >> x;
    if (x < 0) break;          // Abbruch mitten im Körper
    if (x % 2 == 0) continue;  // gerade Zahl überspringen, nächste Runde
    summe += x;
  }
  std::cout << summe << '\n';  // Summe der ungeraden Zahlen
}
// Eingabe: 1 2 3 4 5 -1
// Ausgabe: 9
```
`break` verlässt die (innerste) Schleife, `continue` springt zum nächsten Durchlauf, `return` beendet die ganze Funktion.

### Schleife ohne Körper: der kleinste Teiler
```run
#include <iostream>

int main() {
  int n;
  std::cin >> n;                       // PRE: n >= 2
  int d;
  for (d = 2; n % d != 0; ++d);        // leerer Körper (nur ';'): suche den kleinsten Teiler
  std::cout << (d == n ? "prim" : "nicht prim") << " (kleinster Teiler " << d << ")\n";
}
// Eingabe: 91
// Ausgabe: nicht prim (kleinster Teiler 7)
```
Die Schleife endet spätestens bei `d == n`, weil `n % n == 0`. Ist der kleinste Teiler `n` selbst, ist `n` prim.

### Eine Schleife analysieren (typische Prüfungsaufgabe)
Aufgabe: Was berechnet das Programm, für welche `n` ist die Ausgabe korrekt, und warum hält es an?
```run
#include <iostream>

int main() {
  int n;
  std::cin >> n;
  int x = 1;
  while (n > 0) {
    x *= 2;
    --n;
  }
  std::cout << x << '\n';
}
// Eingabe: 5
// Ausgabe: 32
```
**1. Von Hand durchrechnen** (Tabelle für n = 3):
| Zeitpunkt | n | x |
|---|---|---|
| vor der Schleife | 3 | 1 |
| nach Durchlauf 1 | 2 | 2 |
| nach Durchlauf 2 | 1 | 4 |
| nach Durchlauf 3 | 0 | 8 |

Das Muster zeigt `x = 2ⁿ`. Die **Schleifeninvariante** (gilt vor und nach jedem Durchlauf) lautet: `x · 2ⁿ = 2^(n₀)`, wobei `n₀` der Startwert von `n` ist.

**2. Wertebereich:** `x` ist ein `int` mit Maximum 2³¹−1. Für `n ≥ 31` läuft `x` über, die Ausgabe stimmt also nur für `n ∈ {0, …, 30}`.

**3. Terminierung:** `n` ist ganzzahlig, wird in jedem Durchlauf um 1 kleiner (strikt fallend) und die Schleife läuft nur, solange `n > 0`. Nach höchstens `n₀` Durchläufen ist `n = 0` und die Schleife endet. Für `n₀ ≤ 0` wird der Körper gar nicht ausgeführt.

### Schleifen umschreiben
Jede Schleife lässt sich in jede andere Form bringen: Initialisierung vor die Schleife, Bedingung in `while(...)`, Update ans Ende des Körpers.
```run
#include <iostream>

int main() {
  int n = 5;

  int f = 1;                              // Fakultät als for-Schleife
  for (int i = n; i > 0; --i) f *= i;

  int g = 1, m = n;                       // dasselbe mit while
  while (m > 0) { g *= m; --m; }

  std::cout << f << ' ' << g << '\n';
}
// Ausgabe: 120 120
```
Potenz mit Schleife: `for (r = 1; x > 0; --x) r *= n;` berechnet `nˣ`. Ein `do-while` ist die natürliche Form für „Summe zweier Eingaben, danach fragen, ob nochmal“:
```run
#include <iostream>

int main() {
  int nochmal;
  do {
    int a, b;
    std::cin >> a >> b;
    std::cout << a + b << '\n';
    std::cin >> nochmal;               // 0 beendet die Schleife
  } while (nochmal != 0);
}
// Eingabe: 1 2 1
// Eingabe: 10 20 0
// Ausgabe: 3
// Ausgabe: 30
```
> **Übung 3:** Was gibt `for (int i = 1; i <= 10; i += 3) std::cout << i << ' ';` aus? (Lösung: `1 4 7 10`.) Wie oft läuft `do { ... } while (false);`? (Lösung: einmal.)

## 4 Funktionen, PRE/POST, Fehlersuche
> Cheatsheet: Abschnitt 4

### Aufbau einer Funktion
Eine Funktion hat einen **Rückgabetyp**, einen **Namen**, **Parameter** und einen **Körper**. `void` heisst: kein Rückgabewert. Funktionen müssen vor ihrer Verwendung **deklariert** sein.
```run
#include <iostream>

int quadrat(int x);                // Deklaration (Prototyp): "es gibt so eine Funktion"

int main() {
  std::cout << quadrat(5) << '\n';
}

int quadrat(int x) {               // Definition: der eigentliche Code
  return x * x;
}
// Ausgabe: 25
```
### Vor- und Nachbedingungen (PRE / POST)
Ein **Vertrag** zwischen Aufrufer und Funktion:
- **PRE** (Vorbedingung): Was muss der Aufrufer garantieren, damit die Funktion korrekt arbeitet? Hält er sich nicht daran, ist alles erlaubt.
- **POST** (Nachbedingung): Was garantiert die Funktion danach? Dazu zählen der Rückgabewert **und alle Seiteneffekte**, also Ausgaben und geänderte Referenzparameter.

PRE sollte so **schwach** wie möglich sein (nicht mehr verlangen als nötig), POST so **vollständig** wie möglich. Mit `assert` prüft man die PRE zur Laufzeit.
```run
#include <iostream>
#include <cassert>

// PRE:  b != 0
// POST: gibt die ganzzahlige Division a / b zurück
int teile(int a, int b) {
  assert(b != 0);                  // bricht mit Fehlermeldung ab, wenn die PRE verletzt ist
  return a / b;
}

int main() {
  std::cout << teile(7, 2) << '\n';
}
// Ausgabe: 3
```
Beispiele, wie man PRE/POST aus Code herausliest:
| Code | PRE | POST |
|---|---|---|
| `int res = 1; for (; x > 0; x--) res *= n; return res;` | `x >= 0 && (n != 0 \|\| x != 0)` (0⁰ ausschliessen) | gibt nˣ zurück |
| `int i = 0; while (n > 0) { n /= 10; ++i; } return i;` | `n > 0` | gibt die Anzahl Dezimalstellen von n zurück |
| `int i = 0; while (i*i != n) ++i; return i;` | `n` ist eine positive Quadratzahl | gibt √n zurück |
| `int i = 2; for (; n % i != 0; ++i); return n == i;` | `n >= 2` | gibt `true` zurück, genau wenn n prim ist |

Die Vorbedingung bei der Wurzel ist nötig, weil die Schleife sonst nie endet (`i*i` springt über `n`, oder Overflow).

### Fehler in Funktionen finden
Prüfe immer: (1) Gibt **jeder Pfad** einen Wert zurück? (2) Ist alles initialisiert? (3) Genügt die PRE (Division durch 0, ungültiger Index)? (4) Stimmen die Grenzen (`<` oder `<=`)?
```skip
bool is_even(int i) {
  if (i % 2 == 0) return true;
  // Fehler: für ungerade i wird nichts zurückgegeben => undefiniertes Verhalten
}

double invert(int x) {
  double result;               // Fehler: nicht initialisiert
  if (x != 0) result = 1.0 / x;
  return result;               // für x == 0 wird Müll gelesen
}
```
Korrekturen:
```decl
// POST: gibt true zurück, genau wenn i gerade ist
bool is_even(int i) {
  return i % 2 == 0;           // jeder Pfad liefert einen Wert, keine PRE nötig
}

// Variante 1: PRE verschärfen
// PRE:  x != 0
// POST: gibt 1/x zurück
double invert1(int x) {
  assert(x != 0);
  return 1.0 / x;
}

// Variante 2: Sonderwert für den Problemfall
// POST: gibt 1/x zurück, oder 0, falls x == 0
double invert2(int x) {
  double result = 0;
  if (x != 0) result = 1.0 / x;
  return result;
}
```
### Header und Source trennen
Bei grösseren Programmen steht die **Deklaration** in einer Header-Datei (`.h`) und die **Definition** in einer `.cpp`. So kann `main.cpp` die Funktionen benutzen, ohne den Code zu kennen.
```skip
// ---- calendar.h ----
#pragma once                       // verhindert doppeltes Einbinden
bool is_leap_year(int year);

// ---- calendar.cpp ----
#include "calendar.h"              // eigene Header in Anführungszeichen
bool is_leap_year(int year) {
  return year % 4 == 0 && (year % 100 != 0 || year % 400 == 0);
}

// ---- main.cpp ----
#include <iostream>
#include "calendar.h"
int main() { std::cout << is_leap_year(2024) << '\n'; }
```
### Überladen
Mehrere Funktionen dürfen gleich heissen, wenn sich die Parametertypen unterscheiden. Der Compiler wählt nach den Argumenten.
```run
#include <iostream>

int betrag(int x) { return x < 0 ? -x : x; }
double betrag(double x) { return x < 0 ? -x : x; }

int main() {
  std::cout << betrag(-3) << ' ' << betrag(-2.5) << '\n';   // erste bzw. zweite Version
}
// Ausgabe: 3 2.5
```
(Genau dieser Mechanismus steckt hinter den überladenen Operatoren in Abschnitt 9.)

## 5 Parameterübergabe: Wert, Referenz, const
> Cheatsheet: Abschnitt 5

### Call by value
Standardmässig bekommt die Funktion eine **Kopie** des Arguments. Änderungen daran wirken nicht auf das Original.
### Referenzen
`int&` ist ein **Alias**: ein zweiter Name für dieselbe Variable. Ändert die Funktion ihn, ändert sie das Original.
```run
#include <iostream>

void erhoehe_kopie(int i)     { ++i; }
void erhoehe_referenz(int& i) { ++i; }

void tausche(int& a, int& b) {          // klassisches Beispiel für Referenzparameter
  int t = a;
  a = b;
  b = t;
}

int main() {
  int x = 5;
  erhoehe_kopie(x);
  std::cout << x << '\n';               // unverändert
  erhoehe_referenz(x);
  std::cout << x << '\n';               // verändert
  int a = 1, b = 2;
  tausche(a, b);
  std::cout << a << ' ' << b << '\n';
}
// Ausgabe: 5
// Ausgabe: 6
// Ausgabe: 2 1
```
- Eine `int&` braucht einen **l-value**: `erhoehe_referenz(5)` ist ein Fehler, `5` hat keine Adresse.
- Bei `const int&` darf auch ein r-value übergeben werden, dafür darf die Funktion nichts ändern.

### const
`const` verbietet Änderungen. Das gilt für Variablen und Parameter: `int f(const int i) { return ++i; }` lässt sich nicht kompilieren.

**`const&` für grosse Objekte:** Ein `std::vector` per Wert zu übergeben kopiert alle Elemente. Mit `const std::vector<int>&` gibt es keine Kopie, und die Funktion kann das Original trotzdem nicht verändern. So übergibt man Vektoren, die nur gelesen werden.
```run
#include <iostream>
#include <vector>

int summe(const std::vector<int>& v) {      // nur lesen, nicht kopieren
  int s = 0;
  for (int i = 0; i < std::ssize(v); ++i) s += v[i];
  return s;
}

void verdopple(std::vector<int>& v) {       // soll ändern => Referenz ohne const
  for (int i = 0; i < std::ssize(v); ++i) v[i] *= 2;
}

int main() {
  std::vector<int> v = {1, 2, 3};
  verdopple(v);
  std::cout << summe(v) << '\n';
}
// Ausgabe: 12
```
### Die fünf `foo`-Varianten (Prüfungsklassiker)
Alle fünf Funktionen versuchen `++i` zurückzugeben. Beurteile: Gibt es einen Compilerfehler? Ist das Verhalten wohldefiniert? Wie lautet die POST?
| Funktion | Beurteilung |
|---|---|
| `int foo(int i) { return ++i; }` | Kein Fehler. `i` ist eine Kopie. POST: gibt `i+1` zurück, das Original bleibt unverändert. |
| `int foo(const int i) { return ++i; }` | **Compilerfehler**: `++i` ändert einen `const`-Parameter. |
| `int foo(int& i) { return ++i; }` | Kein Fehler. POST: erhöht das Original um 1 und gibt den neuen Wert (als Kopie) zurück. |
| `int& foo(int i) { return ++i; }` | Kompiliert, ist aber **undefiniert**: Es wird eine Referenz auf die lokale Kopie `i` zurückgegeben, die nach dem Ende der Funktion nicht mehr existiert (*dangling reference*). |
| `const int& foo(int& i) { return ++i; }` | Kein Fehler. Erhöht das Original und gibt eine nur lesbare Referenz darauf zurück. Das Original lebt weiter, also wohldefiniert. |

> **Regel:** Gib nie eine Referenz auf eine **lokale** Variable oder einen Parameter zurück, der per Wert übernommen wurde. Das Objekt wird beim Verlassen der Funktion zerstört. (Referenz auf einen Referenzparameter ist dagegen in Ordnung, siehe vierte und fünfte Zeile.)

## 6 std::vector, Matrix, Iteratoren
> Cheatsheet: Abschnitt 6

Ein `std::vector<T>` ist ein Array, das mitwächst. Man braucht `#include <vector>`.

### Anlegen und benutzen
```run
#include <iostream>
#include <vector>

int main() {
  std::vector<int> v;                 // leer
  std::vector<int> a(3);              // 3 Elemente, alle 0
  std::vector<int> b(3, 7);           // 3 Elemente, alle 7
  std::vector<int> c = {4, 5, 6};     // Liste

  v.push_back(10);                    // hinten anfügen
  v.push_back(20);
  v.push_back(30);
  std::cout << v.size() << ' ' << v[0] << ' ' << v.back() << '\n';
  v.pop_back();                       // letztes Element entfernen
  v[0] = 99;                          // Zugriff mit []: Index 0 .. size-1
  std::cout << v[0] << ' ' << v.size() << ' ' << a[2] << ' ' << b[1] << ' ' << c[2] << '\n';
}
// Ausgabe: 3 10 30
// Ausgabe: 99 2 0 7 6
```
> **Achtung:** `v[i]` prüft den Index **nicht**. Ein Zugriff ausserhalb von `0 … size-1` ist undefiniertes Verhalten (oft ein Absturz, oft stilles Falschrechnen).

### Durchlaufen
```run
#include <iostream>
#include <vector>

int main() {
  std::vector<int> v = {1, 2, 3};

  for (int i = 0; i < std::ssize(v); ++i)    // klassisch mit Index
    v[i] *= 2;

  for (int x : v) std::cout << x << ' ';      // x ist eine KOPIE des Elements
  std::cout << '\n';

  for (int& x : v) x += 1;                    // x ist eine REFERENZ => ändert den Vektor
  for (const int& x : v) std::cout << x << ' ';   // nur lesen, ohne zu kopieren
  std::cout << '\n';
}
// Ausgabe: 2 4 6
// Ausgabe: 3 5 7
```
### Vektoren in Funktionen
Übergib Vektoren **immer** als Referenz: `const std::vector<int>&`, wenn die Funktion nur liest, `std::vector<int>&`, wenn sie ändert. Per Wert würde der ganze Vektor kopiert, und Änderungen gingen verloren.
```run
#include <iostream>
#include <vector>

// POST: gibt die Anzahl Vorkommen von t in v zurück
int vorkommen(const std::vector<int>& v, int t) {
  int c = 0;
  for (int i = 0; i < std::ssize(v); ++i)
    if (v[i] == t) ++c;
  return c;
}

// POST: hängt alle Zahlen bis zur ersten negativen Eingabe an v an
void lies(std::vector<int>& v) {
  int x;
  while (std::cin >> x && x >= 0) v.push_back(x);
}

int main() {
  std::vector<int> v;
  lies(v);
  int gesucht;
  std::cin >> gesucht;
  std::cout << vorkommen(v, gesucht) << '\n';
}
// Eingabe: 3 5 3 3 7 -1
// Eingabe: 3
// Ausgabe: 3
```
Weitere Eigenschaften: `v2 = v1` kopiert den ganzen Vektor, `v1 == v2` vergleicht elementweise, `v.clear()` leert, `v.resize(n)` ändert die Grösse, `v.empty()` fragt nach Leere.

### Matrizen: Vektor von Vektoren
Eine Matrix mit `rows` Zeilen und `cols` Spalten ist ein `std::vector<std::vector<int>>`. Mit `using` gibt man dem Typ einen kurzen Namen.
```run
#include <iostream>
#include <vector>

using vec = std::vector<int>;
using mat = std::vector<vec>;

int main() {
  mat m(2, vec(3, 0));            // 2 Zeilen, 3 Spalten, alles 0
  m[0][1] = 5;                    // Zeile 0, Spalte 1
  m[1][2] = 7;
  std::cout << m.size() << " Zeilen, " << m[0].size() << " Spalten\n";
  for (int r = 0; r < std::ssize(m); ++r) {
    for (int c = 0; c < std::ssize(m[r]); ++c) std::cout << m[r][c] << ' ';
    std::cout << '\n';
  }
}
// Ausgabe: 2 Zeilen, 3 Spalten
// Ausgabe: 0 5 0
// Ausgabe: 0 0 7
```
### Matrixprodukt
Für `A` (n×k) und `B` (k×p) ist `R = A·B` eine n×p-Matrix mit `R[r][c] = Σ_i A[r][i]·B[i][c]`. Voraussetzung: Spaltenzahl von `A` = Zeilenzahl von `B`.
```run
#include <iostream>
#include <vector>

using vec = std::vector<int>;
using mat = std::vector<vec>;

// PRE: A und B nicht leer, A[0].size() == B.size()
// POST: gibt A * B zurück
mat produkt(const mat& A, const mat& B) {
  mat R(std::ssize(A), vec(std::ssize(B[0]), 0));
  for (int r = 0; r < std::ssize(A); ++r)
    for (int c = 0; c < std::ssize(B[0]); ++c)
      for (int k = 0; k < std::ssize(B); ++k)
        R[r][c] += A[r][k] * B[k][c];
  return R;
}

int main() {
  mat A = {{1, 2, 3}, {4, 5, 6}};      // 2x3
  mat B = {{1, 0}, {0, 1}, {2, 2}};    // 3x2
  mat R = produkt(A, B);               // 2x2
  for (const vec& zeile : R) {
    for (int x : zeile) std::cout << x << ' ';
    std::cout << '\n';
  }
}
// Ausgabe: 7 8
// Ausgabe: 16 17
```
Nachrechnen: `R[0][0] = 1·1 + 2·0 + 3·2 = 7`. Matrix mal Vektor geht gleich: `res[r] += m[r][c] * v[c]`. Transponieren: `T[c][r] = m[r][c]`.

### Iteratoren
Ein Iterator ist ein „Zeiger“ auf ein Element. `v.begin()` zeigt auf das erste, `v.end()` **hinter** das letzte Element (halboffener Bereich `[begin, end)`). `*it` ist das Element, `++it` rückt weiter, `end - begin` ist die Anzahl.
```run
#include <iostream>
#include <vector>

using iterator = std::vector<int>::const_iterator;

// POST: Summe aller Elemente im Bereich [b, e)
int summe(iterator b, iterator e) {
  int s = 0;
  for (iterator it = b; it != e; ++it) s += *it;
  return s;
}

int main() {
  std::vector<int> v = {1, 2, 3, 4};
  std::cout << summe(v.begin(), v.end()) << '\n';          // alles
  std::cout << summe(v.begin() + 1, v.begin() + 3) << '\n'; // Elemente 1 und 2 => 2 + 3
}
// Ausgabe: 10
// Ausgabe: 5
```
### Nützliche Funktionen aus `<algorithm>`
```run
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
  std::vector<int> v = {5, 2, 9, 1};
  std::sort(v.begin(), v.end());                    // aufsteigend sortieren
  for (int x : v) std::cout << x << ' ';
  std::cout << '\n';
  std::swap(v[0], v[3]);                            // zwei Elemente vertauschen
  std::reverse(v.begin(), v.end());
  for (int x : v) std::cout << x << ' ';
  std::cout << '\n' << *std::max_element(v.begin(), v.end()) << '\n';
}
// Ausgabe: 1 2 5 9
// Ausgabe: 1 5 2 9
// Ausgabe: 9
```
> **Typische Fehler:** `v.size() - 1` bei leerem Vektor (riesige Zahl, siehe Abschnitt 1) · `v[v.size()]` (ein Element zu weit) · Vektor per Wert statt per Referenz übergeben (Änderung geht verloren) · Matrix-Dimensionen nicht vor dem Rechnen prüfen.

## 7 Ein-/Ausgabe
> Cheatsheet: Abschnitt 7

### Einlesen mit cin
`std::cin >> x` liest das nächste „Wort“ und wandelt es in den Typ von `x` um. Leerzeichen und Zeilenumbrüche werden übersprungen. Der Ausdruck `std::cin >> x` ist selbst in einer Bedingung nutzbar: er ist `true`, solange das Lesen geklappt hat.
```run
#include <iostream>

int main() {
  int x, summe = 0;
  while (std::cin >> x) summe += x;     // liest bis zum Ende der Eingabe (EOF) oder bis ein Fehler auftritt
  std::cout << "Summe " << summe << '\n';
}
// Eingabe: 4 5
// Eingabe: 6
// Ausgabe: Summe 15
```
Drei übliche Eingabeformate:
- **Anzahl zuerst:** `int n; std::cin >> n; for (int i = 0; i < n; ++i) { ... }`
- **Endmarke:** lies, bis ein bestimmter Wert (z. B. −1 oder eine negative Zahl) kommt.
- **Bis zum Ende:** `while (std::cin >> x)`.

### Zeilen lesen und zerlegen
```run
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

int main() {
  std::string zeile;
  std::getline(std::cin, zeile);        // ganze Zeile inkl. Leerzeichen
  std::stringstream ss(zeile);          // wie ein cin, das aus dem String liest
  int ziel;
  ss >> ziel;                           // erstes Wort
  std::vector<int> v;
  int x;
  while (ss >> x) v.push_back(x);       // alle restlichen Zahlen der Zeile
  std::cout << "ziel " << ziel << ", " << v.size() << " Werte\n";
}
// Eingabe: 8 1 7 2 6 6
// Ausgabe: ziel 8, 5 Werte
```
### Ausgabeformatierung
```run
#include <iostream>
#include <iomanip>

int main() {
  std::cout << true << ' ' << std::boolalpha << true << '\n';      // 1 true
  std::cout << 3.14159 << '\n';                                    // Standard: 6 Stellen insgesamt
  std::cout << std::fixed << std::setprecision(2) << 3.14159 << '\n';  // 2 Nachkommastellen
  std::cerr << "nur für Fehlermeldungen\n";                        // anderer Kanal (nicht in cout)
}
// Ausgabe: 1 true
// Ausgabe: 3.14159
// Ausgabe: 3.14
```
> Bei Prüfungsaufgaben mit Ausgabevergleich muss das Format **exakt** stimmen: Leerzeichen, Zeilenumbruch am Schluss, keine zusätzlichen Hinweise wie „Bitte Zahl eingeben“ in `std::cout` (die kommen in `std::cerr` oder entfallen).

## 8 struct & class
> Cheatsheet: Abschnitt 8

Mit `struct` oder `class` fasst man Daten und die dazugehörigen Funktionen (**Methoden**) zu einem neuen Typ zusammen. Ein konkretes Exemplar heisst **Objekt**.

### Beispiel: ein Mittelwert-Zähler
```run
#include <iostream>

class Averager {
  double sum = 0;                  // Daten-Member, private (Standard bei class)
  int count = 0;                   // mit Standardwerten initialisiert
public:                            // ab hier von aussen benutzbar
  void add_value(double value) {
    sum += value;
    ++count;
  }
  double get_average() const {     // const: verändert das Objekt nicht
    return count == 0 ? 0 : sum / count;     // Bedingungsoperator: Bedingung ? wenn_wahr : wenn_falsch
  }
  void reset() {
    sum = 0;
    count = 0;
  }
};

int main() {
  Averager a;                      // Objekt anlegen (Standardwerte sum=0, count=0)
  std::cout << a.get_average() << '\n';
  a.add_value(2);
  a.add_value(4);
  a.add_value(9);
  std::cout << a.get_average() << '\n';
  a.reset();
  std::cout << a.get_average() << '\n';
}
// Ausgabe: 0
// Ausgabe: 5
// Ausgabe: 0
```
### Wichtige Begriffe
- **Member:** Daten (`sum`, `count`) und Methoden (`add_value`, …). Zugriff von aussen mit dem Punkt: `a.add_value(2)`.
- **private / public:** `private` ist nur innerhalb der Klasse zugänglich. `a.sum` von `main` aus gibt einen Compilerfehler. Bei `class` ist alles zunächst `private`, bei `struct` zunächst `public`. Sonst sind beide gleich.
- **Konstruktor:** eine Methode ohne Rückgabetyp, die genau den Namen der Klasse trägt. Sie läuft beim Anlegen des Objekts.
- **const-Methode:** ein `const` hinter der Parameterliste verspricht, dass das Objekt nicht verändert wird. Nur solche Methoden darf man auf einem `const`-Objekt oder über eine `const&` aufrufen.
- **Klasseninvariante:** eine Aussage über die Member, die nach jedem Konstruktor und jeder Methode gilt (z. B. `count >= 0`, `sum` ist die Summe der `count` hinzugefügten Werte).

### Konstruktoren und Initialisierungsliste
```run
#include <iostream>

struct Punkt {
  int x = 0, y = 0;                 // Standardwerte
  Punkt() {}                        // Standardkonstruktor: Punkt p;
  Punkt(int x_, int y_) : x(x_), y(y_) {}   // Initialisierungsliste: initialisiert die Member direkt
  int manhattan() const { return (x < 0 ? -x : x) + (y < 0 ? -y : y); }
};

int main() {
  Punkt a;                          // (0, 0)
  Punkt b(3, -4);                   // ruft den zweiten Konstruktor
  std::cout << a.x << ' ' << b.x << ' ' << b.y << ' ' << b.manhattan() << '\n';
}
// Ausgabe: 0 3 -4 7
```
Ohne Standardwert (`= 0`) und ohne Konstruktor enthalten `int`-/`double`-Member **Müll**.

### Deklaration in der .h, Definition in der .cpp
Bei getrennten Dateien steht in der Klasse nur die Deklaration, die Methode wird mit `Klasse::name` ausserhalb definiert:
```skip
// averager.h
class Averager {
  double sum = 0;
  int count = 0;
public:
  void add_value(double value);
  double get_average() const;
};

// averager.cpp
#include "averager.h"
void Averager::add_value(double value) { sum += value; ++count; }
double Averager::get_average() const { return count == 0 ? 0 : sum / count; }
```
### PRE/POST bei Methoden, Typ und Wert von Ausdrücken
Die **PRE** bezieht sich auf die Parameter *und* auf den Zustand des Objekts davor, die **POST** beschreibt Rückgabewert und neuen Zustand. Beispiel: `void add(const char c);` hat POST „der Zähler für das Zeichen `c` wurde um 1 erhöht“.

Bei Aufgaben „Welchen Typ und Wert hat der Ausdruck?“ geht man Schritt für Schritt von innen nach aussen vor. Mit dem `Averager` oben:
| Ausdruck | Typ | Wert / Bemerkung |
|---|---|---|
| `a.get_average()` (nach 2, 4, 9) | `double` | 5 |
| `std::vector<Averager> avs(3);  avs[1]` | `Averager` | ein Objekt mit sum=0, count=0 |
| `a.count` | – | **Fehler**: `count` ist `private` |

> **Übung 4:** Schreibe eine Klasse `Zaehler` mit Methoden `erhoehe()`, `hole() const` und `zuruecksetzen()`. Der Zählerstand darf nie negativ sein (Invariante). Teste sie, indem du `erhoehe()` dreimal aufrufst und dann `hole()` ausgibst (Ergebnis: 3).

## 9 Operatoren überladen
> Cheatsheet: Abschnitt 9. Das ist ein Schwerpunktthema: **So definiert man Operatoren für eigene Typen.**

### Die Grundidee
Für `int` und `double` kennt der Compiler `+`, `==`, `<<` usw. Für eigene Typen (`struct`/`class`) nicht. Du bringst es ihm bei, indem du eine **Funktion mit dem besonderen Namen `operator` + Symbol** schreibst, zum Beispiel `operator+` oder `operator==`. Der Ausdruck `a + b` ist dann nur eine bequeme Schreibweise für den Aufruf `operator+(a, b)`.
```run
#include <iostream>

struct Punkt { int x, y; };

Punkt operator+(const Punkt& a, const Punkt& b) {
  return Punkt{a.x + b.x, a.y + b.y};
}

int main() {
  Punkt p{1, 2}, q{10, 20};
  Punkt r = p + q;                    // Kurzschreibweise
  Punkt s = operator+(p, q);          // dasselbe, ausgeschrieben
  std::cout << r.x << ' ' << r.y << ' ' << s.x << ' ' << s.y << '\n';
}
// Ausgabe: 11 22 11 22
```
Wie bei normalen Funktionen wählt der Compiler nach den Parametertypen (Überladen, Abschnitt 4). Du kannst nur Operatoren umdefinieren, an denen mindestens ein **eigener Typ** beteiligt ist. `int + int` lässt sich nicht ändern, und neue Symbole wie `**` kann man nicht erfinden. Nicht überladbar sind `::`, `.`, `?:` und `sizeof`.

### Zwei Möglichkeiten: freie Funktion oder Member
Ein Operator lässt sich auf zwei Arten schreiben. Pro Operator wählt man **eine**:
| Form | Aussehen | Der Ausdruck `a + b` bedeutet |
|---|---|---|
| **freie Funktion** | `T operator+(const T& a, const T& b)` | `operator+(a, b)` |
| **Member** | `T operator+(const T& b) const` in der Klasse | `a.operator+(b)`; linker Operand ist das Objekt selbst (`*this`) |

```run
#include <iostream>

struct Wert {
  int v;
  Wert operator+(const Wert& b) const {         // Member-Version: der linke Operand ist *this
    return Wert{v + b.v};
  }
};

int main() {
  Wert a{3}, b{4};
  std::cout << (a + b).v << ' ' << a.operator+(b).v << '\n';
}
// Ausgabe: 7 7
```
**Faustregeln, welche Form man nimmt:**
| Operator | Form | Grund |
|---|---|---|
| `+ - * /` (binär), `== != <` | frei | symmetrisch, beide Operanden gleichwertig |
| `+=`, `++`, `--`, `=`, `[]` | Member | verändern das linke Objekt bzw. brauchen direkten Zugriff |
| unäres `-` (und `!`) | Member (oder frei mit einem Parameter) | nur ein Operand |
| `<<` (Ausgabe), `>>` (Eingabe) | **nur frei** | der linke Operand ist `std::ostream`/`std::istream`, nicht dein Typ |
| `2.0 * a` | **nur frei** | der linke Operand ist ein `double`, kein Objekt, also kein Member-Aufruf möglich |

### Schritt für Schritt: die Klasse Complex
Schritt 1: Daten und Konstruktoren.
```decl
struct Complex {
  double re = 0, im = 0;
  Complex() {}
  Complex(double r, double i) : re(r), im(i) {}
};
```
Schritt 2: arithmetische Operatoren als freie Funktionen. Sie ändern ihre Operanden nicht (darum `const&`) und liefern ein **neues Objekt per Wert** zurück.
```decl
struct Complex {
  double re = 0, im = 0;
  Complex() {}
  Complex(double r, double i) : re(r), im(i) {}
};

Complex operator+(const Complex& a, const Complex& b) {
  return Complex(a.re + b.re, a.im + b.im);
}
Complex operator-(const Complex& a, const Complex& b) {
  return Complex(a.re - b.re, a.im - b.im);
}
Complex operator*(const Complex& a, const Complex& b) {
  // (a+bi)(c+di) = (ac - bd) + (ad + bc)i
  return Complex(a.re * b.re - a.im * b.im, a.re * b.im + a.im * b.re);
}
Complex operator/(const Complex& a, const Complex& b) {
  // (a+bi)/(c+di) = ((ac + bd) + (bc - ad)i) / (c^2 + d^2);  PRE: b != 0
  double n = b.re * b.re + b.im * b.im;
  return Complex((a.re * b.re + a.im * b.im) / n, (a.im * b.re - a.re * b.im) / n);
}
```
Schritt 3: Vergleiche. Sie liefern `bool`. Man definiert `==` und baut `!=` daraus.
```decl
struct Complex {
  double re = 0, im = 0;
};

bool operator==(const Complex& a, const Complex& b) {
  return a.re == b.re && a.im == b.im;
}
bool operator!=(const Complex& a, const Complex& b) {
  return !(a == b);                  // wiederverwenden statt neu schreiben
}
```
Schritt 4: Ausgabe `<<` und Eingabe `>>`. Der **Stream** wird per Referenz übergeben und **zurückgegeben**. Das macht Ketten wie `std::cout << a << " " << b` möglich, denn `(std::cout << a)` liefert wieder `std::cout`.
```decl
struct Complex {
  double re = 0, im = 0;
};

// Ausgabeformat: [re,im]
std::ostream& operator<<(std::ostream& out, const Complex& a) {
  return out << "[" << a.re << "," << a.im << "]";
}

// Eingabeformat: [re,im]   z.B.  [1.5,-2]
std::istream& operator>>(std::istream& in, Complex& a) {   // Complex& OHNE const: wir schreiben hinein
  char c;                            // fängt die Trennzeichen '[' ',' ']' ab
  return in >> c >> a.re >> c >> a.im >> c;
}
```
Schritt 5: Operatoren als **Member**: unäres Minus, `+=`, `[]`, `++`.
```decl
struct Complex {
  double re = 0, im = 0;
  Complex() {}
  Complex(double r, double i) : re(r), im(i) {}

  Complex operator-() const {                // unäres Minus:  -a   (const: ändert a nicht)
    return Complex(-re, -im);
  }
  Complex& operator+=(const Complex& o) {    // a += b   (ändert a!)
    re += o.re;
    im += o.im;
    return *this;                            // gibt das Objekt selbst zurück (als Referenz)
  }
  double& operator[](int i) {                // c[0] ist re, c[1] ist im; Referenz => auch beschreibbar
    return i == 0 ? re : im;
  }
  double operator[](int i) const {           // Version für const-Objekte: nur lesen
    return i == 0 ? re : im;
  }
  Complex& operator++() {                    // Präfix ++c: erst erhöhen, dann neuen Wert liefern
    ++re;
    return *this;
  }
  Complex operator++(int) {                  // Postfix c++ (Dummy-int markiert die Postfix-Form)
    Complex alt = *this;                     // alten Wert merken
    ++re;
    return alt;                              // ... und den liefern
  }
};
```
Wichtig dabei:
- **`*this`** ist das Objekt, auf dem die Methode gerade aufgerufen wird (`a` bei `a += b`). `return *this;` gibt es als Referenz zurück, damit man `(a += b) += c` schreiben kann und kein unnötiges Objekt entsteht.
- **Rückgabe-Konvention:** `+ - * /` und Postfix-`++` liefern ein **neues Objekt per Wert**; `+=`, `-=` und Präfix-`++` liefern eine **Referenz auf `*this`**; Vergleiche liefern `bool`; `<<`/`>>` liefern den **Stream**.
- **`const`:** Alles, was das Objekt nicht verändert (`operator-()`, lesendes `operator[]`), wird `const` markiert.
- **Wiederverwenden:** Hat man `+=`, baut man `+` daraus: `Complex r = a; r += b; return r;`.

Schritt 6: Weitere Operatoren: Skalarmultiplikation (beide Reihenfolgen!) und `<`, damit sich Objekte sortieren lassen.
```decl
struct Complex {
  double re = 0, im = 0;
  Complex() {}
  Complex(double r, double i) : re(r), im(i) {}
};

Complex operator*(double k, const Complex& a) {   // 2.0 * c  (muss frei sein)
  return Complex(k * a.re, k * a.im);
}
Complex operator*(const Complex& a, double k) {   // c * 2.0
  return k * a;                                   // die andere Version benutzen
}
bool operator<(const Complex& a, const Complex& b) {   // nach Betrag; erlaubt std::sort
  return a.re * a.re + a.im * a.im < b.re * b.re + b.im * b.im;
}
```
Schritt 7: Alles zusammen in einem lauffähigen Programm.
```run
#include <iostream>
#include <vector>
#include <algorithm>

struct Complex {
  double re = 0, im = 0;
  Complex() {}
  Complex(double r, double i) : re(r), im(i) {}
  Complex operator-() const { return Complex(-re, -im); }
  Complex& operator+=(const Complex& o) { re += o.re; im += o.im; return *this; }
  double& operator[](int i) { return i == 0 ? re : im; }
};

Complex operator+(const Complex& a, const Complex& b) { Complex r = a; r += b; return r; }
Complex operator*(const Complex& a, const Complex& b) {
  return Complex(a.re * b.re - a.im * b.im, a.re * b.im + a.im * b.re);
}
Complex operator/(const Complex& a, const Complex& b) {
  double n = b.re * b.re + b.im * b.im;
  return Complex((a.re * b.re + a.im * b.im) / n, (a.im * b.re - a.re * b.im) / n);
}
Complex operator*(double k, const Complex& a) { return Complex(k * a.re, k * a.im); }
bool operator==(const Complex& a, const Complex& b) { return a.re == b.re && a.im == b.im; }
bool operator!=(const Complex& a, const Complex& b) { return !(a == b); }
bool operator<(const Complex& a, const Complex& b) {
  return a.re * a.re + a.im * a.im < b.re * b.re + b.im * b.im;
}
std::ostream& operator<<(std::ostream& out, const Complex& a) {
  return out << "[" << a.re << "," << a.im << "]";
}
std::istream& operator>>(std::istream& in, Complex& a) {
  char c;
  return in >> c >> a.re >> c >> a.im >> c;
}

int main() {
  Complex a, b;
  std::cin >> a >> b;                          // liest zwei Zahlen im Format [re,im]
  std::cout << a << " + " << b << " = " << a + b << '\n';
  std::cout << a << " * " << b << " = " << a * b << '\n';
  std::cout << a << " / " << b << " = " << a / b << '\n';
  std::cout << "-a = " << -a << ", 2*b = " << 2.0 * b << '\n';
  std::cout << (a == b) << (a != b) << (a < b) << '\n';
  a += b;                                      // a ist jetzt [4,6]
  a[0] = 100;                                  // re direkt überschreiben
  std::cout << a << '\n';
  std::vector<Complex> v = {Complex(3, 4), Complex(1, 0), Complex(0, 2)};
  std::sort(v.begin(), v.end());               // benutzt operator<
  for (const Complex& c : v) std::cout << c;
  std::cout << '\n';
}
// Eingabe: [1,2] [3,4]
// Ausgabe: [1,2] + [3,4] = [4,6]
// Ausgabe: [1,2] * [3,4] = [-5,10]
// Ausgabe: [1,2] / [3,4] = [0.44,0.08]
// Ausgabe: -a = [-1,-2], 2*b = [6,8]
// Ausgabe: 011
// Ausgabe: [100,6]
// Ausgabe: [1,0][0,2][3,4]
```
### Ein zweites Beispiel: Brüche
Hier muss der Konstruktor mit dem ggT kürzen, damit `==` richtig funktioniert (Invariante: Nenner > 0, Bruch gekürzt).
```run
#include <iostream>

int ggt(int a, int b) { return b == 0 ? a : ggt(b, a % b); }

struct Bruch {
  int z, n;                                   // Zähler, Nenner
  Bruch(int zaehler, int nenner = 1) {        // PRE: nenner != 0
    int g = ggt(zaehler < 0 ? -zaehler : zaehler, nenner < 0 ? -nenner : nenner);
    if (g == 0) g = 1;
    if (nenner < 0) { zaehler = -zaehler; nenner = -nenner; }
    z = zaehler / g;
    n = nenner / g;
  }
};

Bruch operator+(const Bruch& a, const Bruch& b) { return Bruch(a.z * b.n + b.z * a.n, a.n * b.n); }
Bruch operator*(const Bruch& a, const Bruch& b) { return Bruch(a.z * b.z, a.n * b.n); }
bool operator==(const Bruch& a, const Bruch& b) { return a.z == b.z && a.n == b.n; }
bool operator<(const Bruch& a, const Bruch& b) { return a.z * b.n < b.z * a.n; }   // n > 0 vorausgesetzt
std::ostream& operator<<(std::ostream& o, const Bruch& b) { return o << b.z << "/" << b.n; }

int main() {
  Bruch a(1, 2), b(1, 3);
  std::cout << a + b << ' ' << a * b << ' ' << (a < b) << ' ' << (Bruch(2, 4) == a) << ' ' << Bruch(6, -4) << '\n';
}
// Ausgabe: 5/6 1/6 0 1 -3/2
```
### Private Member und `friend`
Sind die Member einer Klasse `private`, kann eine freie Funktion wie `operator<<` nicht darauf zugreifen. Zwei Lösungen: öffentliche Getter-Methoden, oder `friend`: die Klasse erlaubt dieser einen Funktion ausdrücklich den Zugriff.
```run
#include <iostream>

class Geld {
  int rappen = 0;
public:
  Geld(int r) : rappen(r) {}
  Geld operator+(const Geld& o) const { return Geld(rappen + o.rappen); }   // Member: sieht private Daten
  friend std::ostream& operator<<(std::ostream& out, const Geld& g);        // erlaubt Zugriff
};

std::ostream& operator<<(std::ostream& out, const Geld& g) {
  return out << g.rappen / 100 << "." << (g.rappen % 100 < 10 ? "0" : "") << g.rappen % 100;
}

int main() {
  std::cout << Geld(1234) + Geld(5) << '\n';
}
// Ausgabe: 12.39
```
### Fallstricke
- **Stream nicht zurückgeben:** `void operator<<(...)` kompiliert, aber `std::cout << a << b` geht nicht mehr.
- **`>>` mit `const T&`:** Man kann nicht in ein `const` Objekt hineinlesen. Der Parameter muss `T&` sein.
- **Referenz auf lokale Variable zurückgeben:** `Complex& operator+(...)` mit einer lokalen Variable `r` ist ein Dangling-Reference-Fehler (Abschnitt 5). Arithmetische Operatoren liefern **per Wert**.
- **Member-Operator vergessen `const`:** Sonst lässt er sich auf `const`-Objekten und `const&`-Parametern nicht aufrufen.
- **`==` auf `double`:** Gleichheit von Kommazahlen ist heikel (Abschnitt 10). In Übungen reicht oft der exakte Vergleich.
- **Nur Sinnvolles überladen:** Ein `+` sollte sich wie Addition anfühlen. Ein überladenes `operator<<` zum Beispiel kann sich an die Format-Vorgabe der Aufgabe halten müssen.
- **Zuweisung `=` und Kopieren:** Für einfache Klassen erzeugt der Compiler `operator=` und den Kopierkonstruktor selbst. Man muss sie nicht schreiben, `a = b;` kopiert alle Member.

### So gehst du bei einer Operator-Aufgabe vor
1. Aus `main.cpp` ablesen, **welche Ausdrücke** vorkommen (`c1 + c2`, `-c1`, `c1 == c2`, `std::cin >> c1`, `std::cout << c1`).
2. Pro Ausdruck die Signatur wählen (Tabelle oben) und im Header **deklarieren**, in der `.cpp` **definieren**.
3. Eingabe-/Ausgabeformat aus der Aufgabe genau übernehmen (Klammern, Kommas, Leerzeichen).
4. Mit einem kleinen Test jede Operation einmal aufrufen.

> **Übung 5:** Definiere für `struct Vec2 { double x, y; }` die Operatoren `+`, `-` (binär und unär), `*` (Skalar, beide Reihenfolgen), `==` und `<<`. Gib `[x,y]` aus. Teste: `Vec2{1,2} + Vec2{3,4}` ergibt `[4,6]`.

## 10 Gleitkomma & Zahlendarstellung
> Cheatsheet: Abschnitt 10

### Wie ein `double` aufgebaut ist
Eine Gleitkommazahl wird als **±1.m × 2ᵉ** gespeichert: ein Vorzeichen, eine **Mantisse** `m` (die Nachkommastellen nach der führenden 1) und ein **Exponent** `e`. Beim `double` sind es 1 + 11 + 52 Bit. Weil die Mantisse endlich viele Bits hat, lassen sich die meisten Zahlen nur **näherungsweise** darstellen. Selbst `0.1` ist im Binärsystem periodisch und wird gerundet.

### Dezimal in Binär umrechnen (Übungsmodell)
In den Übungen wird ein kleines Modell benutzt: **1.b₁b₂b₃ × 2ᵉ** mit nur 3 Nachkommabits. Vorgehen:
1. Vorkommateil durch fortgesetztes Teilen durch 2 in Binär (die Reste von unten nach oben lesen).
2. Nachkommateil durch fortgesetztes **Verdoppeln**: Ist das Ergebnis ≥ 1, ist das nächste Bit 1 (und man zieht 1 ab), sonst 0.
3. Normalisieren: das Komma so verschieben, dass genau eine 1 davor steht (Exponent anpassen).
4. Auf 3 Nachkommabits **runden** (ist der Rest grösser als die Hälfte der letzten Stelle, aufrunden).

| Zahl | Binär | Normalisiert | gerundet auf 3 Bit | dargestellter Wert | Fehler |
|---|---|---|---|---|---|
| 0.75 | 0.11 | 1.1 × 2⁻¹ | `1.100×2⁻¹` | 0.75 | 0 |
| 7 | 111 | 1.11 × 2² | `1.110×2²` | 7 | 0 |
| 3.1416 | 11.0010010… | 1.10010010 × 2¹ | `1.101×2¹` (der Rest 0.10010 ist > 0.5, also aufrunden) | 3.25 | 0.1084 |
| 2.718 | 10.10110… | 1.010110 × 2¹ | `1.011×2¹` (der Rest 0.110 ist > 0.5, also aufrunden) | 2.75 | 0.032 |

**Zurückrechnen:** `1.101×2¹` ist (1 + ½ + ⅛)·2 = 1.625·2 = 3.25. Der **Fehler** ist |exakter Wert − dargestellter Wert|.

> Im Übungsmodell kam auch `0.11 → 1.000×2⁻³` vor. Das passt zu einer Einschränkung des Exponenten (hier wohl auf −3 nach unten; das ist aus der Musterlösung abgeleitet, nicht aus dem Aufgabentext, prüfe das in deiner Aufgabe). Dann ist 0.125 (= `1.000×2⁻³`) die nächste darstellbare Zahl zu 0.11, mit Fehler 0.015.

### Absorption und Vergleiche
Addiert man eine sehr kleine zu einer grossen Zahl, geht die kleine **verloren**, weil die Mantisse nicht genug Stellen hat. Im Übungsmodell bleibt `6.0 + 0.11` gleich `1.100×2²`. Beim `double` gilt `1e16 + 1 == 1e16`.
```run
#include <iostream>
#include <cmath>

int main() {
  std::cout << std::boolalpha;
  std::cout << (1e16 + 1 == 1e16) << '\n';              // das +1 geht verloren
  std::cout << (0.1 + 0.2 == 0.3) << '\n';              // nicht exakt gleich!
  std::cout << (std::abs((0.1 + 0.2) - 0.3) < 1e-9) << '\n';   // so vergleicht man double
}
// Ausgabe: true
// Ausgabe: false
// Ausgabe: true
```
**Regeln:** Nie `==` auf `double` verwenden, sondern „Abstand kleiner als eine kleine Toleranz“. Sehr grosse Zwischenwerte (z. B. Fakultäten) laufen zu `inf` oder `nan` über.

### Binärentwicklung ausgeben
Algorithmus für 0 ≤ x < 2: das erste Bit ist 1, falls `x >= 1`. Dann zieht man das Bit ab und verdoppelt (das verschiebt das Komma), und wiederholt.
```run
#include <iostream>

int main() {
  double x;
  std::cin >> x;                       // PRE: 0 <= x < 2
  int b = x >= 1;                      // Vorkommabit
  std::cout << b << ".";
  for (int i = 1; i < 16; ++i) {       // 15 Nachkommabits
    x -= b;                            // gesetztes Bit entfernen
    x *= 2;                            // nächste Stelle nach vorne holen
    b = x >= 1;
    std::cout << b;
  }
  std::cout << '\n';
}
// Eingabe: 0.75
// Ausgabe: 0.110000000000000
```
Warum geht das genau? `0.75 → 1.5` (Bit 1) `→ 0.5·2 = 1.0` (Bit 1) `→ 0` (Bit 0 …). Das entspricht `0.11₂`.

### Näherung von π (zwei Reihen)
```run
#include <iostream>

int main() {
  int m = 30;                                          // Anzahl Terme

  double pi1 = 0;                                      // Leibniz: pi = 4 (1 - 1/3 + 1/5 - ...)
  for (int j = 0; j < m; ++j)
    pi1 += (j % 2 == 0 ? 4.0 : -4.0) / (2 * j + 1);    // Vorzeichen wechselt

  double pi2 = 2, zaehler = 2, nenner = 1;             // pi = 2 * Summe_j j!/(3*5*...*(2j+1))
  for (int j = 1; j < m; ++j) {
    zaehler *= j;                                      // wird j!
    nenner *= 2 * j + 1;                               // wird 3*5*...*(2j+1)
    pi2 += zaehler / nenner;                           // nächster Term
  }
  std::cout << pi1 << ' ' << pi2 << '\n';
}
// Ausgabe: 3.10827 3.14159
```
Die zweite Reihe konvergiert viel schneller. Zähler und Nenner wachsen aber schnell, bei sehr vielen Termen laufen sie über (`inf`/`nan`). Man rechnet die Terme **inkrementell** (jeden Term aus dem vorherigen), statt jeweils Fakultäten neu zu berechnen.

### Auf ganze Zahlen runden
Die Umwandlung `int(x)` schneidet nur ab. Für „richtiges“ Runden (.5 weg von 0):
```run
#include <iostream>

// PRE: x passt nach dem Runden in den Bereich von int
// POST: gibt die nächste ganze Zahl zurück; bei .5 die weiter von 0 entfernte
int round_number(double x) {
  int t = x;                // schneidet ab (Richtung 0)
  double d = x - t;         // verbleibender Rest, exakt berechenbar
  if (d >= 0.5)  return t + 1;
  if (d <= -0.5) return t - 1;
  return t;
}

int main() {
  std::cout << round_number(2.4) << ' ' << round_number(2.5) << ' ' << round_number(-2.5) << ' ' << round_number(-2.4) << '\n';
}
// Ausgabe: 2 3 -3 -2
```
## 11 Ganzzahl-Tricks
> Cheatsheet: Abschnitt 11

### Ziffern zerlegen
`n % 10` ist die letzte Ziffer, `n / 10` schneidet sie ab.
```run
#include <iostream>

int main() {
  int n = 4096;
  int stellen = 0, summe = 0;
  for (int m = n; m > 0; m /= 10) {      // PRE: n > 0
    ++stellen;
    summe += m % 10;
  }
  std::cout << stellen << ' ' << summe << '\n';
}
// Ausgabe: 4 19
```
(Für `n == 0` zählt diese `for`-Schleife 0 Stellen. Will man dafür 1, nimmt man `do { ... } while (m > 0);`.)

### Zahlensystem wechseln
Man teilt wiederholt durch die Basis `b`. Die Reste sind die Ziffern von hinten nach vorn. Hier werden sie als Dezimalziffern einer neuen Zahl zusammengesetzt (für Basen < 10).
```run
#include <iostream>

// PRE: n >= 0, 1 < b < 10
// POST: gibt die Ziffern von n zur Basis b als Dezimalzahl zurück (z.B. 10, 2 -> 1010)
int convert_base(int n, int b) {
  int result = 0, pos = 1;               // pos: aktuelle Stelle 1, 10, 100, ...
  while (n != 0) {
    result += pos * (n % b);             // Rest ist die nächste Ziffer von hinten
    n /= b;
    pos *= 10;
  }
  return result;
}

int main() {
  std::cout << convert_base(10, 2) << ' ' << convert_base(14, 9) << '\n';
}
// Ausgabe: 1010 15
```
### Ganzzahl kaufmännisch runden
Mit Ganzzahlen: `a / b` schneidet ab. Rundet man stattdessen „halbe aufwärts“, rechnet man `(a + b/2) / b` (für `a, b > 0`). Beispiel Parallelschaltung von Widerständen mit gerundetem Ergebnis `R = R12·R34 / (R12 + R34)`:
```run
#include <iostream>

int main() {
  int R1 = 10, R2 = 20, R3 = 30, R4 = 40;
  int R12 = R1 + R2;                   // Serienschaltung: addieren
  int R34 = R3 + R4;
  int R = (R12 * R34 + (R12 + R34) / 2) / (R12 + R34);     // Parallel, gerundet
  std::cout << R << '\n';              // exakt 30*70/100 = 21
}
// Ausgabe: 21
```
### Overflow vorher erkennen
Statt `a + b` zu rechnen und hinterher zu schauen (zu spät, da undefiniert), prüft man **vorher** ohne zu überlaufen:
```run
#include <iostream>
#include <climits>

// PRE: b >= 0
bool addition_laeuft_ueber(int a, int b) { return a > INT_MAX - b; }

int main() {
  std::cout << addition_laeuft_ueber(INT_MAX, 1) << addition_laeuft_ueber(5, 6) << '\n';
  // Fibonacci bis zum letzten darstellbaren Wert
  int a = 0, b = 1, n = 0;
  while (!addition_laeuft_ueber(a, b)) { int nx = a + b; a = b; b = nx; ++n; }
  std::cout << n << ' ' << a << '\n';
}
// Ausgabe: 10
// Ausgabe: 45 1134903170
```
Bei Multiplikation: `a * b` läuft über, genau wenn `a > INT_MAX / b` (für `a, b > 0`).

### Weitere Tricks
- **Multiplikation nur mit Addition:** `29a = 16a + 8a + 4a + a`. Man verdoppelt wiederholt: `b = a + a; c = b + b; d = c + c; e = d + d;` und rechnet `e + d + c + a`.
- **Parität:** `n % 2 != 0` prüft „ungerade“ (nicht `n % 2 == 1`: für negative `n` ist der Rest −1).
- **Teilbarkeit:** `n % k == 0`.
- **Wochentag aus Datum:** Tage seit einem Bezugsdatum (hier 1.1.1900 = Montag) zählen, dann `% 7`.
```run
#include <iostream>

bool schaltjahr(int y) { return y % 4 == 0 && (y % 100 != 0 || y % 400 == 0); }
int tage_im_jahr(int y) { return schaltjahr(y) ? 366 : 365; }
int tage_im_monat(int m, int y) {
  if (m == 2) return schaltjahr(y) ? 29 : 28;
  if (m == 4 || m == 6 || m == 9 || m == 11) return 30;
  return 31;
}

// PRE: gültiges Datum ab 1.1.1900. POST: Anzahl Tage seit dem 1.1.1900 (ausschliesslich des Datums)
int tage_seit_1900(int tag, int monat, int jahr) {
  int t = tag - 1;                                          // volle Tage im aktuellen Monat
  for (int m = 1; m < monat; ++m) t += tage_im_monat(m, jahr);   // volle Monate dieses Jahres
  for (int y = 1900; y < jahr; ++y) t += tage_im_jahr(y);        // volle Jahre davor
  return t;
}

int main() {
  const char* name[] = {"montag", "dienstag", "mittwoch", "donnerstag", "freitag", "samstag", "sonntag"};
  std::cout << name[tage_seit_1900(1, 1, 1900) % 7] << ' ' << name[tage_seit_1900(21, 11, 2026) % 7] << '\n';
}
// Ausgabe: montag samstag
```

## 12 Typische iterative Algorithmen
> Cheatsheet: Abschnitt 12

Viele Aufgaben sind Variationen weniger **Muster**. Die Muster:
- **Akkumulieren:** eine Variable sammelt (`s += x`, `p *= x`). Startwert: 0 bei Summe, 1 bei Produkt.
- **Zählen:** `if (Bedingung) ++c;`
- **Suchen:** früh mit `return` abbrechen, sobald gefunden. Erst nach der Schleife „nicht gefunden“ melden.
- **Minimum/Maximum:** mit dem **ersten Element** starten (nicht mit 0!) und mit dem Rest vergleichen.
- **Flag:** `bool gefunden = false;` wird in der Schleife auf `true` gesetzt.
- **Zwei Positionen:** zwei Indizes oder Iteratoren (z. B. `i < j`), oder Vorgänger/Nachfolger (`v[i-1]`, Start bei `i = 1`).
- **Zustand mitführen:** z. B. „vorheriger Wert“ und „Länge des aktuellen Laufs“ bei der Run-Length-Kodierung.

### Primzahlen und ggT
Eine Zahl `n ≥ 2` ist prim, wenn sie keinen Teiler `d` mit `2 ≤ d ≤ √n` hat. Statt `d <= sqrt(n)` schreibt man `d * d <= n` (ganzzahlig, schnell). Der **Euklidische Algorithmus** berechnet den ggT über `ggT(a, b) = ggT(b, a % b)`.
```run
#include <iostream>

// PRE: -
// POST: gibt true zurück, genau wenn n eine Primzahl ist
bool is_prime(int n) {
  if (n < 2) return false;
  for (int d = 2; d * d <= n; ++d)       // O(sqrt n)
    if (n % d == 0) return false;        // Teiler gefunden => nicht prim
  return true;
}

// PRE: a >= 0, b >= 0, nicht beide 0
// POST: gibt den grössten gemeinsamen Teiler zurück
int gcd(int a, int b) {
  while (b != 0) {
    int t = a % b;                       // (a, b) -> (b, a mod b)
    a = b;
    b = t;
  }
  return a;
}

int main() {
  for (int n = 1; n <= 20; ++n) if (is_prime(n)) std::cout << n << ' ';
  std::cout << '\n' << gcd(12, 18) << ' ' << gcd(17, 5) << '\n';
}
// Ausgabe: 2 3 5 7 11 13 17 19
// Ausgabe: 6 1
```
### Fibonacci mit Overflow-Schutz
Jede Zahl ist die Summe der beiden vorherigen: 0, 1, 1, 2, 3, 5, 8, … Man merkt sich nur die letzten beiden Werte. Bevor man addiert, prüft man, ob die Summe noch in einen `int` passt.
```run
#include <iostream>
#include <climits>

int main() {
  int max_count;
  std::cin >> max_count;                 // so viele Zahlen wollen wir ausgeben
  int a = 0, b = 1;                      // F(0), F(1)
  int count = 0;
  while (count < max_count) {
    std::cout << a << ' ';
    ++count;
    if (a > INT_MAX - b) break;          // a + b würde überlaufen => aufhören
    int next = a + b;
    a = b;
    b = next;
  }
  std::cout << "\nAusgegeben: " << count << '\n';
}
// Eingabe: 10
// Ausgabe: 0 1 1 2 3 5 8 13 21 34
// Ausgabe: Ausgegeben: 10
```
Variante „Fibonacci-Primzahlen bis `m`“: dieselbe Schleife, aber nur Zahlen ausgeben, die `is_prime` erfüllen.

### Maximum, Zählen, Prüfen
```run
#include <iostream>
#include <vector>

// PRE: v nicht leer
int max_of(const std::vector<int>& v) {
  int m = v[0];                          // Start mit dem ersten Element
  for (int x : v)
    if (x > m) m = x;
  return m;
}

// POST: true, genau wenn v aufsteigend sortiert ist
bool is_sorted(const std::vector<int>& v) {
  for (int i = 1; i < std::ssize(v); ++i)
    if (v[i] < v[i - 1]) return false;   // ein Gegenbeispiel genügt
  return true;                           // keins gefunden => sortiert
}

// POST: v ist umgekehrt
void reverse_vec(std::vector<int>& v) {
  for (int i = 0, j = std::ssize(v) - 1; i < j; ++i, --j)   // zwei Zeiger von aussen nach innen
    std::swap(v[i], v[j]);
}

int main() {
  std::vector<int> v = {3, 9, 2, 7};
  std::cout << max_of(v) << ' ' << is_sorted(v) << ' ' << is_sorted({1, 2, 2, 5}) << '\n';
  reverse_vec(v);
  for (int x : v) std::cout << x << ' ';
  std::cout << '\n';
}
// Ausgabe: 9 0 1
// Ausgabe: 7 2 9 3
```
### Sortieren
**Bubble Sort:** Vergleicht benachbarte Elemente und tauscht sie, wenn sie in der falschen Reihenfolge stehen. Das wiederholt man, bis ein ganzer Durchlauf nichts mehr getauscht hat. Nach `k` Durchläufen stehen die `k` grössten Elemente an ihrem Platz (Invariante). Terminierung: nach höchstens `n` Durchläufen. Laufzeit O(n²).

**Selection Sort:** Sucht in jedem Schritt das Minimum des Rests und tauscht es nach vorn.
```run
#include <iostream>
#include <vector>

// POST: v ist aufsteigend sortiert
void bubble_sort(std::vector<int>& v) {
  bool swapped;
  do {
    swapped = false;
    for (int i = 1; i < std::ssize(v); ++i) {
      if (v[i] < v[i - 1]) {
        std::swap(v[i], v[i - 1]);
        swapped = true;                  // es hat sich etwas geändert => noch ein Durchlauf
      }
    }
  } while (swapped);
}

void selection_sort(std::vector<int>& v) {
  for (int i = 0; i + 1 < std::ssize(v); ++i) {
    int m = i;                           // Index des kleinsten Elements im Rest [i, n)
    for (int j = i + 1; j < std::ssize(v); ++j)
      if (v[j] < v[m]) m = j;
    std::swap(v[i], v[m]);
  }
}

int main() {
  std::vector<int> a = {5, 2, 9, 1, 5}, b = a;
  bubble_sort(a);
  selection_sort(b);
  for (int x : a) std::cout << x << ' ';
  std::cout << '\n';
  for (int x : b) std::cout << x << ' ';
  std::cout << '\n';
}
// Ausgabe: 1 2 5 5 9
// Ausgabe: 1 2 5 5 9
```
Im Beispiel „Sorting by Swapping“ der Übungen wird absteigend sortiert: dasselbe Programm mit `>` statt `<`.

### Binärsuche
Auf einem **sortierten** Vektor halbiert man den Suchbereich `[lo, hi]` in jedem Schritt: Mittelwert prüfen, links oder rechts weitersuchen. Laufzeit O(log n).
```run
#include <iostream>
#include <vector>

// PRE: v aufsteigend sortiert
// POST: gibt einen Index i mit v[i] == x zurück, sonst -1
int binary_search(const std::vector<int>& v, int x) {
  int lo = 0, hi = std::ssize(v) - 1;
  while (lo <= hi) {
    int mid = lo + (hi - lo) / 2;        // vermeidet Overflow von lo + hi
    if (v[mid] == x) return mid;
    else if (v[mid] < x) lo = mid + 1;   // x kann nur rechts sein
    else hi = mid - 1;                   // x kann nur links sein
  }
  return -1;
}

int main() {
  std::vector<int> v = {1, 3, 5, 7, 9, 11};
  std::cout << binary_search(v, 7) << ' ' << binary_search(v, 4) << ' ' << binary_search(v, 1) << '\n';
}
// Ausgabe: 3 -1 0
```
### Paare mit gegebener Summe
Zähle alle Paare `(i, j)` mit `i < j` und `v[i] + v[j] == sum`. Mit Iteratoren: zwei verschachtelte Schleifen, die innere beginnt hinter der äusseren Position (so wird kein Paar doppelt gezählt). O(n²).
```run
#include <iostream>
#include <vector>

using iterator = std::vector<int>::const_iterator;

// PRE: für alle i, j gilt v[i] + v[j] <= INT_MAX
// POST: gibt die Anzahl Paare (i < j) im Bereich [begin, end) mit Summe sum zurück
int pairs_with_sum(int sum, iterator begin, iterator end) {
  int c = 0;
  for (iterator i = begin; i != end; ++i)
    for (iterator j = i + 1; j != end; ++j)
      if (*i + *j == sum) ++c;
  return c;
}

int main() {
  std::vector<int> v = {1, 7, 2, 6, 6};
  std::cout << pairs_with_sum(8, v.begin(), v.end()) << '\n';   // (1,7), (2,6), (2,6)
}
// Ausgabe: 3
```
### Run-Length-Kodierung
Eine Folge gleicher Werte wird durch (Länge, Wert) ersetzt: `1 1 1 2 2 3` → `3 1 2 2 1 3`. Man merkt sich den vorherigen Wert und die Länge des laufenden Laufs. Wechselt der Wert (oder ist die Maximallänge 255 erreicht), gibt man den Lauf aus und beginnt einen neuen. **Den letzten Lauf nicht vergessen:** er wird nach der Schleife ausgegeben.
```run
#include <iostream>

int main() {
  int prev;
  std::cin >> prev;
  if (prev == -1) return 0;                    // leere Folge
  int len = 1, x;
  while (std::cin >> x && x != -1) {           // -1 beendet die Eingabe
    if (x != prev || len == 255) {             // Lauf zu Ende
      std::cout << len << ' ' << prev << ' ';
      len = 1;
      prev = x;
    } else {
      ++len;                                   // Lauf wird länger
    }
  }
  std::cout << len << ' ' << prev << '\n';     // letzter Lauf
}
// Eingabe: 1 1 1 2 2 3 -1
// Ausgabe: 3 1 2 2 1 3
```
Dekodieren: lies Paare `(len, val)` und gib `len`-mal `val` aus (`for (int i = 0; i < len; ++i) std::cout << val << ' ';`).

### Sieb des Eratosthenes und Collatz
```run
#include <iostream>
#include <vector>

// POST: p[k] == true, genau wenn k prim ist (0 <= k <= n); PRE: n >= 1
std::vector<bool> sieve(int n) {
  std::vector<bool> p(n + 1, true);
  p[0] = p[1] = false;
  for (int i = 2; i * i <= n; ++i)
    if (p[i])
      for (int j = i * i; j <= n; j += i) p[j] = false;   // alle Vielfachen streichen
  return p;
}

// PRE: n >= 1; POST: Anzahl Schritte bis die Folge bei 1 ankommt
int collatz(int n) {
  int steps = 0;
  while (n != 1) {
    n = n % 2 == 0 ? n / 2 : 3 * n + 1;
    ++steps;
  }
  return steps;
}

int main() {
  std::vector<bool> p = sieve(30);
  for (int k = 0; k <= 30; ++k) if (p[k]) std::cout << k << ' ';
  std::cout << '\n' << collatz(6) << '\n';      // 6 3 10 5 16 8 4 2 1  => 8 Schritte
}
// Ausgabe: 2 3 5 7 11 13 17 19 23 29
// Ausgabe: 8
```
**Laufzeit-Faustregeln:** eine Schleife über `n` Elemente O(n) · zwei ineinander O(n²) · Halbieren (Binärsuche) O(log n) · Teilersuche bis √n O(√n).

## 13 Rekursion
> Cheatsheet: Abschnitt 13. Die meisten Prüfungsaufgaben zur Rekursion sind Variationen der Beispiele hier.

### Was passiert bei einem rekursiven Aufruf?
Eine **rekursive Funktion** ruft sich selbst mit einem **kleineren** Problem auf. Jeder Aufruf hat seine eigenen Parameter und lokalen Variablen. Die Aufrufe stapeln sich (*Call Stack*), bis ein Aufruf den **Basisfall** erreicht und ohne weiteren Selbstaufruf zurückkehrt. Danach werden die wartenden Aufrufe von innen nach aussen fertig berechnet.
```run
#include <iostream>
#include <string>

int fact(int n, int tiefe = 0) {                  // tiefe: nur für die eingerückte Ausgabe
  std::string einzug(2 * tiefe, ' ');
  std::cout << einzug << "fact(" << n << ")\n";
  if (n <= 1) return 1;                           // Basisfall
  int r = n * fact(n - 1, tiefe + 1);             // Rekursionsschritt
  std::cout << einzug << "= " << r << '\n';
  return r;
}

int main() { fact(3); }
// Ausgabe: fact(3)
// Ausgabe:   fact(2)
// Ausgabe:     fact(1)
// Ausgabe:   = 2
// Ausgabe: = 6
```
`fact(3)` wartet auf `fact(2)`, das auf `fact(1)` wartet. `fact(1)` liefert 1, `fact(2)` rechnet `2·1 = 2`, `fact(3)` rechnet `3·2 = 6`.

### Das Rezept
```skip
Ergebnis f(Parameter) {
  if (Basisfall)  return einfacher_Wert;     // 1. Wann ist das Problem trivial?
  ... f(kleineres_Problem) ...               // 2. Wie führe ich es auf ein kleineres zurück?
}
```
1. **Basisfall(e)** festlegen (z. B. `n == 0`, leerer Vektor, `lo > hi`).
2. **Rekursionsschritt:** das Problem auf ein kleineres zurückführen und die Teillösung nutzen.
3. **Terminierung** zeigen: Das Argument wird bei **jedem** Aufruf **strikt kleiner** (`n - 1`, `n / 2`, ein schrumpfendes Intervall) und erreicht damit den Basisfall, in **jedem** Zweig (auch bei zwei rekursiven Aufrufen).
4. **PRE/POST** formulieren und annehmen, dass der rekursive Aufruf sie erfüllt (Induktion). Daraus folgt die POST der ganzen Funktion.

### Zahlen: Fakultät, Potenz, ggT, Fibonacci
```run
#include <iostream>

// PRE: n >= 0;  POST: gibt n! zurück
int fact(int n) { return n <= 1 ? 1 : n * fact(n - 1); }

// PRE: b^e passt in int;  POST: gibt b^e zurück. Halbiert den Exponenten => O(log e) Aufrufe
int power(int b, int e) {
  if (e == 0) return 1;
  int h = power(b, e / 2);               // b^(e/2) EINMAL berechnen und wiederverwenden
  return e % 2 == 0 ? h * h : h * h * b;
}

// PRE: a, b >= 0, nicht beide 0;  POST: gibt den ggT zurück (Euklid)
int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }

// PRE: n >= 0;  POST: gibt die n-te Fibonacci-Zahl zurück (F0 = 0, F1 = 1)
int fib(int n) { return n < 2 ? n : fib(n - 1) + fib(n - 2); }

int main() {
  std::cout << fact(5) << ' ' << power(2, 10) << ' ' << power(3, 5) << ' ' << gcd(12, 18) << ' ' << fib(10) << '\n';
}
// Ausgabe: 120 1024 243 6 55
```
`power`: `2^10 = (2^5)²`, `2^5 = (2^2)²·2`, `2^2 = (2^1)²`, `2^1 = (2^0)²·2`: nur 5 Aufrufe statt 10.

### Ziffern und Ausgabe-Reihenfolge
Wann man etwas ausgibt, **vor** oder **nach** dem rekursiven Aufruf, bestimmt die Reihenfolge der Ausgabe.
```run
#include <iostream>

// PRE: n >= 0;  POST: gibt die Ziffern von n in umgekehrter Reihenfolge aus
void reverse_digits(int n) {
  if (n < 10) {
    std::cout << n;                      // Basisfall: eine Ziffer
  } else {
    std::cout << n % 10;                 // ZUERST die letzte Ziffer ausgeben ...
    reverse_digits(n / 10);              // ... dann den Rest (ohne letzte Ziffer)
  }
}

// PRE: n >= 1;  POST: gibt n im Binärsystem aus (höchstes Bit zuerst)
void print_bin(int n) {
  if (n > 1) print_bin(n / 2);           // ZUERST die höheren Bits ...
  std::cout << n % 2;                    // ... DANN das letzte Bit => richtige Reihenfolge
}

void print_bin_rev(int n) {              // dieselben Zeilen vertauscht: umgekehrte Reihenfolge
  std::cout << n % 2;
  if (n > 1) print_bin_rev(n / 2);
}

// PRE: n >= 0;  POST: gibt die Ziffernsumme zurück
int digit_sum(int n) { return n < 10 ? n : n % 10 + digit_sum(n / 10); }

int main() {
  reverse_digits(1234); std::cout << '\n';
  print_bin(10); std::cout << '\n';
  print_bin_rev(10); std::cout << '\n';
  std::cout << digit_sum(1234) << '\n';
}
// Ausgabe: 4321
// Ausgabe: 1010
// Ausgabe: 0101
// Ausgabe: 10
```
**Merke:** Ausgabe vor dem Aufruf: Reihenfolge wie die Aufrufe kommen. Ausgabe nach dem Aufruf: umgekehrt (der innerste Aufruf gibt zuerst aus).

### Vektoren und Strings rekursiv
Hier arbeitet man mit einem **Index**, der Richtung Ende läuft, oder mit einem schrumpfenden Bereich.
```run
#include <iostream>
#include <string>
#include <vector>

// PRE: i <= v.size();  POST: Summe von v[i], ..., v[size-1]
int rsum(const std::vector<int>& v, int i) {
  return i == std::ssize(v) ? 0 : v[i] + rsum(v, i + 1);
}

// PRE: i < v.size();  POST: grösstes Element ab Index i
int rmax(const std::vector<int>& v, int i) {
  if (i == std::ssize(v) - 1) return v[i];            // Basisfall: letztes Element
  return std::max(v[i], rmax(v, i + 1));
}

// POST: true, genau wenn s[l..r] ein Palindrom ist
bool is_pal(const std::string& s, int l, int r) {
  return l >= r || (s[l] == s[r] && is_pal(s, l + 1, r - 1));   // aussen vergleichen, dann innen
}

// POST: gibt s rückwärts zurück
std::string rev(const std::string& s) { return s.empty() ? "" : rev(s.substr(1)) + s[0]; }

int main() {
  std::vector<int> v = {3, 9, 2};
  std::cout << rsum(v, 0) << ' ' << rmax(v, 0) << ' ' << is_pal("anna", 0, 3) << is_pal("abc", 0, 2) << ' ' << rev("abc") << '\n';
}
// Ausgabe: 14 9 10 cba
```
### Binärsuche rekursiv
Der Suchbereich `[lo, hi]` wird kleiner, bis er leer ist (`lo > hi`, Basisfall „nicht gefunden“).
```run
#include <iostream>
#include <vector>

// PRE: v aufsteigend sortiert;  POST: Index von x in v[lo..hi] oder -1
int bsearch_rec(const std::vector<int>& v, int x, int lo, int hi) {
  if (lo > hi) return -1;                         // leerer Bereich
  int m = lo + (hi - lo) / 2;
  if (v[m] == x) return m;
  return v[m] < x ? bsearch_rec(v, x, m + 1, hi)  // rechts weitersuchen
                  : bsearch_rec(v, x, lo, m - 1); // links weitersuchen
}

int main() {
  std::vector<int> v = {1, 3, 5, 7, 9};
  std::cout << bsearch_rec(v, 7, 0, 4) << ' ' << bsearch_rec(v, 4, 0, 4) << '\n';
}
// Ausgabe: 3 -1
```
### Zwei rekursive Aufrufe: Türme von Hanoi, Teilmengen, Permutationen
Wenn eine Funktion sich mehrfach aufruft, entsteht ein **Aufrufbaum**. Typisch für Kombinatorik.

**Türme von Hanoi:** n Scheiben von `from` nach `to`, mit Hilfsstab `via`. Um n Scheiben zu verschieben, schiebt man zuerst n−1 Scheiben auf den Hilfsstab, dann die grösste ans Ziel, dann die n−1 vom Hilfsstab ans Ziel. Das ergibt 2ⁿ−1 Züge.
```run
#include <iostream>
#include <string>
#include <vector>

void hanoi(int n, char from, char via, char to, int& moves) {
  if (n == 0) return;
  hanoi(n - 1, from, to, via, moves);             // n-1 Scheiben auf den Hilfsstab
  ++moves;                                        // grösste Scheibe: from -> to
  hanoi(n - 1, via, from, to, moves);             // n-1 Scheiben vom Hilfsstab ans Ziel
}

// POST: gibt alle Permutationen der Zeichen von rest aus, jeweils mit Präfix pre
void perms(std::string rest, std::string pre) {
  if (rest.empty()) { std::cout << pre << ' '; return; }
  for (int i = 0; i < std::ssize(rest); ++i) {
    std::string r = rest;
    r.erase(i, 1);                                // Zeichen i wählen ...
    perms(r, pre + rest[i]);                      // ... und mit dem Rest weitermachen
  }
}

// POST: gibt alle Teilmengen von v[i..] (zusammen mit den schon gewählten in cur) aus
void subsets(const std::vector<int>& v, int i, std::vector<int>& cur) {
  if (i == std::ssize(v)) {                       // alle Elemente entschieden
    std::cout << '{';
    for (int x : cur) std::cout << x;
    std::cout << "} ";
    return;
  }
  subsets(v, i + 1, cur);                         // v[i] weglassen
  cur.push_back(v[i]);
  subsets(v, i + 1, cur);                         // v[i] nehmen
  cur.pop_back();                                 // wieder rückgängig machen (Backtracking)
}

int main() {
  int moves = 0;
  hanoi(3, 'A', 'B', 'C', moves);
  std::cout << moves << '\n';
  perms("abc", "");
  std::cout << '\n';
  std::vector<int> cur;
  subsets({1, 2, 3}, 0, cur);
  std::cout << '\n';
}
// Ausgabe: 7
// Ausgabe: abc acb bac bca cab cba
// Ausgabe: {} {3} {2} {23} {1} {13} {12} {123}
```
### Aufrufe zählen (Analyse-Aufgabe)
Typische Frage: „Wie oft wird `f` aufgerufen, in Abhängigkeit von `n`?“ Man zählt inklusive des ersten (nicht rekursiven) Aufrufs. Hier wird zum Prüfen ein Zähler mitgeführt:
```run
#include <iostream>

int aufrufe = 0;

// PRE: n >= 0;  POST: gibt true zurück, genau wenn n ungerade ist
bool f(int n) {
  ++aufrufe;
  if (n == 0) return false;
  return !f(n - 1);                      // ein rekursiver Aufruf, n schrumpft um 1
}

// PRE: n >= 0;  POST: 2^n Sterne wurden ausgegeben
void g(int n) {
  ++aufrufe;
  if (n == 0) { std::cout << '*'; return; }
  g(n - 1);                              // ZWEI rekursive Aufrufe
  g(n - 1);
}

int main() {
  f(5);
  std::cout << aufrufe << '\n';          // n + 1 = 6
  aufrufe = 0;
  g(3);
  std::cout << ' ' << aufrufe << '\n';   // 2^(n+1) - 1 = 15
}
// Ausgabe: 6
// Ausgabe: ******** 15
```
Warum?
- **`f`:** `Calls(0) = 1` und `Calls(n) = 1 + Calls(n−1)`. Also `Calls(n) = n + 1`.
- **`g`:** `Calls(0) = 1` und `Calls(n) = 1 + 2·Calls(n−1)`. Aufgelöst: `1 + 2 + 4 + … + 2ⁿ = 2ⁿ⁺¹ − 1`. Im Aufrufbaum hat Ebene `i` genau 2ⁱ Knoten.
- **Terminierung von `f` und `g`:** Bei jedem Aufruf wird `n` um 1 kleiner und erreicht `0` (bei `g` in beiden Zweigen), dort enden die Aufrufe.
- **Halbierung** (`f(n/2)`): ⌊log₂ n⌋ + 1 Aufrufe.
- **`fib` naiv:** ruft zweimal mit fast gleichem Argument auf, daher exponentiell (ca. 1.6ⁿ): `Calls(n) = 2·F(n+1) − 1`.

### Memoization: wiederholte Arbeit sparen
Beim naiven `fib` wird dieselbe Teilaufgabe tausendfach neu berechnet. Merkt man sich bereits berechnete Werte (Memoization), reicht ein Aufruf pro Wert.
```run
#include <iostream>

long long calls_naive = 0, calls_memo = 0;
long long memo[100];                              // 0 = noch nicht berechnet

long long fib(int n) {
  ++calls_naive;
  return n < 2 ? n : fib(n - 1) + fib(n - 2);
}

long long fibm(int n) {
  ++calls_memo;
  if (n < 2) return n;
  if (memo[n] != 0) return memo[n];               // schon bekannt: sofort zurück
  return memo[n] = fibm(n - 1) + fibm(n - 2);     // berechnen und merken
}

int main() {
  std::cout << fib(30) << ' ' << calls_naive << '\n';
  std::cout << fibm(30) << ' ' << calls_memo << '\n';
}
// Ausgabe: 832040 2692537
// Ausgabe: 832040 59
```
### Gegenseitige Rekursion, Pascal-Dreieck, Dreieck zeichnen
```run
#include <iostream>

bool odd(int n);                                   // Vorwärtsdeklaration, weil sich beide brauchen
bool even(int n) { return n == 0 ? true : odd(n - 1); }
bool odd(int n)  { return n == 0 ? false : even(n - 1); }

// POST: gibt "n über k" zurück (Summe der beiden Einträge darüber im Pascal-Dreieck)
int binom(int n, int k) {
  if (k == 0 || k == n) return 1;
  return binom(n - 1, k - 1) + binom(n - 1, k);
}

// POST: gibt n Zeilen aus, Zeile i hat i Sterne
void triangle(int n) {
  if (n == 0) return;
  triangle(n - 1);                                 // zuerst die kleineren Zeilen
  for (int i = 0; i < n; ++i) std::cout << '*';
  std::cout << '\n';
}

int main() {
  std::cout << even(10) << odd(10) << ' ' << binom(5, 2) << '\n';
  triangle(3);
}
// Ausgabe: 10 10
// Ausgabe: *
// Ausgabe: **
// Ausgabe: ***
```
### Typische Fehler bei Rekursion
```skip
int bad(int n) {
  return n * bad(n - 1);          // FEHLER: kein Basisfall => endlose Rekursion => Stack Overflow
}
int bad2(int n) {
  if (n == 0) return 1;
  return bad2(n + 1);             // FEHLER: Argument nähert sich dem Basisfall nicht
}
int bad3(int n) {
  if (n == 0) return 1;
  return n * bad3(n - 1);         // FEHLER bei n < 0: Basisfall wird übersprungen (PRE n >= 0 fehlt)
}
```
Jede Rekursionsebene belegt Speicher auf dem Stack. Bei sehr tiefer Rekursion (grob 10⁵–10⁶ Ebenen) bricht das Programm ab (*Stack Overflow*). Jede Rekursion lässt sich auch mit einer Schleife schreiben (z. B. `gcd`, Fakultät). Umgekehrt ist Rekursion oft die einfachere Lösung (Hanoi, Permutationen).

## 14 Vorgehen nach Aufgabentyp
> Cheatsheet: Abschnitt 14

### Ausdruck bewerten, gültig?
Beispiel aus den Übungen. Bei `int a = 1, b = 2;` sei der Ausdruck `++a + b++`:
1. Klammern nach Präzedenz: `(++a) + (b++)` (Postfix und Präfix binden stärker als `+`).
2. Typen: beide Operanden sind `int`, das Ergebnis ist ein `int`. Es ist ein **r-value** (Ergebnis einer Addition).
3. Wert: `++a` ergibt 2, `b++` liefert den alten Wert 2, also `4`. Danach ist `b == 3`.

Bei „ist der Ausdruck gültig?“ prüft man: Syntax vollständig? Steht links von `=` ein l-value? Passen die Typen?

### Text in Bedingung übersetzen
Zerlege den Satz in Teile, übersetze jedes Teil, verbinde sie (siehe Tabelle in Abschnitt 2). Teste mit Zahlen an der Grenze: gilt „höchstens 5-mal“ für `a == 5 * b`? Ja, also `<=`.

### Funktion reparieren
Vorgehen mit den vier Fragen aus Abschnitt 4. Typische Auflösung: fehlendes `return` ergänzen, Variable initialisieren, PRE ergänzen oder einen Sonderwert zurückgeben.

### PRE/POST formulieren
Rechne kleine Beispiele durch (Eingaben 0, 1, 2, negativ). Beantworte dann: **Wann** ist die Funktion überhaupt sinnvoll definiert (PRE)? **Was** liefert sie, und was tut sie sonst noch (POST)? Beispiel: `int f(int n) { int i = 0; while (n > 0) { n /= 10; ++i; } return i; }`. Rechne `f(0) = 0` (nicht 1!), `f(5) = 1`, `f(123) = 3`. Für `n > 0` ist das die Stellenzahl. Eine PRE `n > 0` ist darum sinnvoll, POST: „gibt die Anzahl Dezimalstellen von `n` zurück“.

### Ein Programm schreiben
1. Aufgabe lesen: Welche **Eingabe** (Format!), welche **Ausgabe** (Format!)?
2. In kleine Funktionen mit PRE/POST zerlegen (Einlesen, Rechnen, Ausgeben).
3. `main` schreibt nur den Ablauf.
4. Mit den Beispielen aus der Aufgabe testen, danach mit Randfällen (leer, 0, 1, grosse Werte).

### Klasse implementieren
Member `private` und mit Standardwert, nur sinnvolle Methoden `public`, Methoden die nichts ändern `const`, bei getrennten Dateien `Klasse::methode` in der `.cpp`. Gefordert Operatoren: siehe Abschnitt 9.

### Rekursive Funktion analysieren (Muster einer Prüfungsaufgabe)
Gegeben: `bool f(int n) { if (n == 0) return false; return !f(n - 1); }`
- **i) PRE/POST:** PRE `n >= 0`. POST: gibt `true` zurück, genau wenn `n` ungerade ist.
- **ii) Terminierung:** Für `n == 0` endet die Funktion sofort. Bei jedem rekursiven Aufruf wird `n` um 1 kleiner, erreicht also nach `n` Schritten die 0.
- **iii) Aufrufe:** `Calls(n) = n + 1`, inklusive des ersten Aufrufs.

Bei zwei rekursiven Aufrufen (`g(n-1); g(n-1);`) ist es `Calls(n) = 2ⁿ⁺¹ − 1`.

## 15 Prüfungs-Checkliste
> Cheatsheet: Abschnitt 15

Die häufigsten Fehler, und warum sie passieren:
- **Overflow:** `int` fasst nur bis 2³¹−1. Bei Potenzen, Fakultäten und Fibonacci rechtzeitig prüfen oder den Wertebereich nennen (bei 2ⁿ: n ≤ 30).
- **Ganzzahldivision:** `1 / 2 == 0`. Wer ein `double` will, braucht ein `double` im Ausdruck (`1.0 / 2`). `%` mit negativen Zahlen beachten.
- **`=` statt `==`, Vergleichsketten, `&&` vor `||`:** Klammern setzen.
- **Short-circuit:** schützt `i < n && v[i] == x` vor ungültigem Zugriff, aber nur in dieser Reihenfolge.
- **`switch` ohne `break`:** Fall-through.
- **`v.size() - 1`:** bei leerem Vektor riesig. Index nur `0 … size-1`.
- **Vektoren als Referenz übergeben**, sonst gehen Änderungen verloren oder es wird kopiert.
- **Nie eine Referenz auf Lokales zurückgeben.**
- **Jeden Pfad mit `return` abschliessen, alles initialisieren, PRE mit `assert` prüfen.**
- **Rekursion:** Basisfall zuerst, Argument schrumpft, alle Zweige terminieren, Ausgabe-Reihenfolge (vor/nach dem Aufruf) beachten.
- **Letzter Lauf/Rest** nach der Schleife nicht vergessen (RLE!). `<` oder `<=` an den Grenzen prüfen. Mitte berechnen als `lo + (hi - lo) / 2`.
- **Operatoren:** Stream zurückgeben, `>>` mit `T&`, Arithmetik per Wert, Zugriff auf `private`-Member beachten (Abschnitt 9).

### Welche Übung trainiert welchen Abschnitt?
| Übung (Ordner `originalübungen`) | Abschnitt |
|---|---|
| Expressions, Expression Evaluation | 2 |
| From Natural Language to C++ | 2 |
| Multiply with 29, Equivalent Resistance, Rounding | 1, 11 |
| Loop mix-up (Snippets 1 und 2), Loop Analysis | 3 |
| Fixing Functions, Pre- and post-conditions | 4 |
| Const and reference types | 5 |
| Number of Occurrences, Vector and matrix operations, Sorting by Swapping, Number Pairs with Sum | 6, 7, 12 |
| Understanding struct & classes, Averager | 8 |
| Complex Numbers | 9 |
| Floating-Point Number Representation, Binary Expansion, Approximation of Pi | 10 |
| Fibonacci primes, Fibonacci overflow check, Perpetual calendar, Decimal to arbitrary base, Run-length encoding | 11, 12 |
| Recursive function analysis, Reverse Digits | 13 |

Zum Lernen: Abschnitt hier durcharbeiten, die Übungen dazu lösen (im Projekt `./trainer test <lektion>`), danach im Cheatsheet den gleichen Stoff in Kurzform wiederfinden.
