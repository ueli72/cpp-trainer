# Cheatsheet — Ziffern & Basen

## Die zwei Kern-Werkzeuge (bei `int`)
| Ausdruck | Bedeutung | Beispiel |
|---|---|---|
| `zahl % 10` | LETZTE Ziffer (Rest durch 10) | `123 % 10` → `3` |
| `zahl / 10` | Zahl ohne letzte Ziffer | `123 / 10` → `12` |

## Quersumme (Muster)
```cpp
int summe = 0;
while (zahl > 0) {
    summe += zahl % 10;   // letzte Ziffer aufaddieren
    zahl /= 10;           // sie abschneiden
}
```
`summe += x` ist Kurzform für `summe = summe + x` (gibt's auch für `-=`, `*=`, `/=`).

## Ziffern drehen (Muster)
```cpp
int gedreht = 0;
while (zahl > 0) {
    gedreht = gedreht * 10 + zahl % 10;   // Ziffer hinten anbauen
    zahl /= 10;
}
```
`1200` → `21` (führende Nullen fallen weg) · `0` → `0` (Sonderfall im Kopf behalten)

## Binär (8-stellig, 0–255)
```cpp
for (int stelle = 128; stelle >= 1; stelle /= 2) {   // 128,64,…,1
    if (zahl >= stelle) { std::cout << "1"; zahl -= stelle; }
    else                  { std::cout << "0"; }
}
```
Führende Nullen sind hier **gewollt** (immer 8 Zeichen).

## Beliebige Basis (value ≥ 0, base 2–9)
```cpp
while (value > 0) {
    std::cout << value % base;   // letzte Ziffer zur Basis
    value /= base;               // und abschneiden
}
```
Reihenfolge-Aufgabe: die Ziffern fallen **umgekehrt** an —
rekursiv löst sich das von selbst (siehe Rekursion-Cheatsheet).

## Sonderfall 0
`value = 0` → die Schleife läuft **nie** → vorher direkt `"0"` ausgeben.

## Formate der Lektionen (genau so ausgeben!)
```
Quersumme: 6      1010        00000101        54321
```

## Testen
`./trainer test ziffern/01` … `./trainer run ziffern/03` — sichtbar in `tests/`
