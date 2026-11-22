// ============================================================
// Ziffern 04 — Zahlensysteme (Eigenbau)
// ============================================================
// Kein Gerüst — nur dein Bauplan. Das ist die Klausuraufgabe
// vom Januar 2022 — du hast alle Bausteine schon gebaut:
// Ziffern abschneiden (Ziffern 01), while-Schleife (Schleifen 04).
//
// Deine Schritte:
//
// 1. Lies zwei ganze Zahlen ein: value (>= 0) und base
//    (zwischen 2 und 9), getrennt durch Leerzeichen —
//    normales >> reicht:  std::cin >> value >> base;
//
// 2. Rechne value zur Basis base um — Ziffer für Ziffer:
//      value % base   →  die LETZTE Ziffer (Rest)
//      value / base   →  der Rest der Zahl ohne diese Ziffer
//    Wiederhole beides in einer while-Schleife, bis value 0 ist.
//
// 3. ZWEI Fallen:
//    a) Die Ziffern fallen in UMGEKEHRTER Reihenfolge an.
//       Trick: gib jede Ziffer SOFORT aus — dann steht am Ende
//       die richtige Reihenfolge. (Du gibst also mitten im
//       Ablauf aus, nicht erst am Schluss.)
//    b) value = 0 → die Schleife läuft nie. Sonderfall:
//       gib direkt "0" aus.
//
// 4. Eine Ausgabezeile — nur die Ziffernfolge, sonst nichts:
//      10 2   →   1010
//      255 9  →   313
//      7 8    →   7
//
// (Keine führenden Nullen — die höchste Ziffer ist immer != 0.)

// ============================================================
// Dein main: Programmstart — hier baust du die Schritte ein.
// ============================================================
int main() {
    // Schritt 1: value und base einlesen
    // Schritt 2 + 3: Sonderfall 0 — sonst Schleife mit % und /
    // Schritt 4: Ziffern direkt in der Schleife ausgeben, "\n" am Ende

    return 0;
}
