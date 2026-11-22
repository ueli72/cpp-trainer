# Cheatsheet — Verzweigungen

## if / else if / else
```cpp
if (bedingung) {
    // läuft, wenn Bedingung WAHR ist
} else if (andereBedingung) {
    // läuft, wenn die erste falsch, diese wahr ist
} else {
    // läuft, wenn alles falsch war
}
```
Es läuft **genau ein** Zweig. Geschweifte Klammern um jeden Block.

## Vergleiche
| Operator | Bedeutung |
|---|---|
| `a == b` | gleich — **ZWEI** Gleichheitszeichen! |
| `a != b` | ungleich |
| `a < b` · `a > b` · `a <= b` · `a >= b` | kleiner/größer (gleich) |

**Achtung:** Ein einzelnes `=` ist eine Zuweisung, kein Vergleich —
`if (a = b)` ist fast immer ein Fehler.

## Logische Verknüpfungen
| Operator | Bedeutung | Beispiel |
|---|---|---|
| `&&` | UND (beide wahr) | `x > 0 && x < 100` |
| `\|\|` | ODER (mindestens einer) | `x < 0 \|\| x > 100` |
| `!` | NICHT (umdrehen) | `!(a == b)` |

## Gerade oder ungerade
```cpp
if (zahl % 2 == 0)   // Rest bei Division durch 2 ist 0 → gerade
```

## Muster: Größte von dreien
```cpp
int maximum = a;                    // mit dem ersten starten
if (b > maximum) maximum = b;       // jeden weiteren prüfen
if (c > maximum) maximum = c;       // danach ist maximum das größte
```
Zwei Wege sind ok: so schrittweise oder drei getrennte Verzweigungen.

## Formate der Lektionen (genau so ausgeben!)
```
gerade    ungerade
Groessere: 7    Gleich
Groesste: 9
```

## Testen
`./trainer test verzweigung/01` … `./trainer run verzweigung/02` — sichtbar in `tests/`
