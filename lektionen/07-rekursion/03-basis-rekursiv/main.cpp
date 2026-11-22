// ============================================================
// Rekursion 03 — Zahlensysteme (rekursiv, Eigenbau)
// ============================================================
// Kein Gerüst — nur dein Bauplan. Die Aufgabe kennst du aus
// Ziffern 04 (value zur Basis base) — diesmal LÖST du sie
// rekursiv, ganz ohne Schleife. Und das löst ein altes Problem:
// die Ziffern fielen umgekehrt an — Rekursion dreht gratis um!
//
// Deine Schritte:
//
// 1. Lies value (>= 0) und base (2 bis 9) ein — Leerzeichen
//    getrennt, normales >>.
//
// 2. Schreibe eine rekursive Funktion gibZiffernAus(value, base):
//      wenn value == 0:  return           (Abbruch — nichts ausgeben)
//      sonst:
//        gibZiffernAus(value / base, base)   ← ERST den Rest rekursiv
//        std::cout << value % base           ← DANN die letzte Ziffer
//
//    Der Clou: Der rekursive Aufruf passiert VOR der eigenen
//    Ausgabe — die Aufrufe stapeln sich bis zur höchsten Ziffer,
//    und beim Zurücklaufen werden die Ziffern in richtiger
//    Reihenfolge ausgegeben.
//
// 3. Sonderfall: value == 0 → die Rekursion würde nichts
//    ausgeben. Gib in main direkt "0" aus.
//
// 4. Eine Ausgabezeile — nur die Ziffernfolge:
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
    // Schritt 3 + 2: Sonderfall 0 abfangen, sonst die Rekursion starten
    // Zeilenumbruch "\n" am Ende nicht vergessen!

    return 0;
}
