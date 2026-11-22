# Cheatsheet — Rekursion

## Das Prinzip
Eine Funktion ruft sich **selbst** — mit einem etwas kleineren Problem.
Zwei Teile sind Pflicht:

1. **Abbruchbedingung** (base case): das kleinste Problem — direkte Antwort
2. **Rekursiver Schritt**: Problem verkleinern und sich selbst aufrufen

Ohne Abbruchbedingung läuft die Rekursion endlos → Absturz.

## Fakultät
```cpp
int fakultaet(int n) {
    if (n == 0) return 1;              // Abbruch
    return n * fakultaet(n - 1);       // Schritt
}
```
In Gedanken: `f(3)` = 3·f(2) = 3·2·f(1) = 3·2·1·f(0) = 3·2·1·1 = 6

## Quersumme
```cpp
int quersumme(int n) {
    if (n == 0) return 0;
    return n % 10 + quersumme(n / 10);
}
```
Der Abbruch ist **natürlich**: `/10` macht `n` irgendwann zu 0.

## Zahlensysteme — der Reihenfolgen-Trick
```cpp
void gibZiffernAus(int value, int base) {
    if (value == 0) return;
    gibZiffernAus(value / base, base);   // ERST aufrufen …
    std::cout << value % base;           // … DANN ausgeben
}
```
Die Aufrufe stapeln sich bis zur höchsten Ziffer; beim Zurücklaufen
erscheinen die Ziffern in **richtiger** Reihenfolge — ohne Umkehr-Trick.
Sonderfall `value = 0`: in `main` direkt `"0"` ausgeben.

## Grenzen
`12!` passt noch in ein `int` (479001600) — `13!` nicht.

## Denk-Falle
Jeder Aufruf bekommt **seine eigenen** Kopien der Parameter —
das `n` im inneren Aufruf verändert das `n` des äußeren nicht.

## Formate der Lektionen (genau so ausgeben!)
```
Fakultaet: 120        Quersumme: 6        1010
```

## Testen
`./trainer test rekursion/01` … `./trainer run rekursion/03` — sichtbar in `tests/`
