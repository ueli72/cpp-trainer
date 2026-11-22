// ============================================================
// Schleifen 04 — Zahlenreihe auswerten (Eigenbau)
// ============================================================
// Kein Gerüst — nur dein Bauplan. Du brauchst: while-Schleife
// und if — beides hast du in dieser Reihe bereits benutzt.
//
// Deine Schritte:
//
// 1. Lies beliebig viele ganze Zahlen ein (EINE pro Zeile).
//    Eine negative Zahl beendet die Eingabe — sie selbst zählt
//    nicht mehr mit. Lesen funktioniert so:
//      while (std::cin >> x) { … }      (läuft, solange Zahlen kommen)
//    Innen entscheidest du mit if: negativ → fertig (break), sonst …
//
// 2. Halte beim Lesen drei Variablen aktuell:
//      anzahl   — eins mehr pro gelesener Zahl
//      summe    — alle Zahlen aufaddiert
//      maximum  — die bislang größte Zahl (beim ERSTEN Wert setzen!
//                 Tipp: erstes Mal: maximum = x, danach: if (x > maximum) …)
//
// 3. Drei Ausgabezeilen (es ist garantiert mindestens eine
//    nicht-negative Zahl dabei):
//      Anzahl: 4
//      Summe: 100
//      Maximum: 42
//
// Beispiel: Eingabe 42, 7, 13, 38, -1  →  Anzahl: 4, Summe: 100,
//                                          Maximum: 42

// ============================================================
// Dein main: Programmstart — hier baust du die Schritte ein.
// ============================================================
int main() {
    // Schritt 1 + 2: Schleife mit Stoppsignal, drei Variablen aktuell halten
    // Schritt 3: drei Ausgabezeilen

    return 0;
}
