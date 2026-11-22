# Struct 04 — Fehlersuche: Vektor-Debug

## Ziel

Structs debuggen: Member-Zugriff, Formeln und Semikolons.

## Aufgabe

Das Programm liest zwei Vektoren (x,y,z, Komma-getrennt) und gibt
**Skalarprodukt** und **Kreuzprodukt** aus.

Es enthält **3 eingebaute Fehler** (2 Compiler, 1 Logik/vertauscht).

## SOLL-Verhalten (Beispiel)

```
1,2,3
4,5,6
```

```
Skalarprodukt: 32
Kreuzprodukt: -3,6,-3
```

## Hinweise

- `ax`, `ay`, `bx` — wo sind diese Variablen deklariert? Was heißt der
  Member-Zugriff richtig?
- Kreuzprodukt: Vergleiche die drei Formeln Zeichen für Zeichen — zwei
  Komponenten sind vertauscht.

## Testen
- **In der App:** Lektion im Baum wählen → 💾 Speichern (bei Änderungen) → 🧪 Testen — die Ausgabe erscheint in der Konsole, die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test struct/04`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run struct/04`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?“) oder OpenCode im Terminal fragen

