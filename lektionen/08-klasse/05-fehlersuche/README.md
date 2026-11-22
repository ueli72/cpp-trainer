# Klasse 05 — Fehlersuche: Vektor-Klasse

## Ziel

Klassen debuggen: Sichtbarkeit (public/private), Member-Zugriff und Methoden.

## Aufgabe

Die Klasse Vector soll zwei Vektoren (x,y,z, Komma-getrennt) einlesen und
das **Skalarprodukt** über eine Methode berechnen.

Es enthält **2 eingebaute Fehler** (beide Compiler — typische Klassen-Fehler).

## SOLL-Verhalten (Beispiel)

```
1,2,3
4,5,6
```

```
Skalarprodukt: 32
```

## Hinweise

- Warum kann `main` nicht auf `a.x` zugreifen? Stichwort: In einer class ist
  alles privat, bis du es freigibst.
- Die Methode soll die Member **des Objekts** mit denen des Parameters
  verrechnen — `this->x` und `other.x`.

## Testen
- **In der App:** Lektion im Baum wählen → 💾 Speichern (bei Änderungen) → 🧪 Testen — die Ausgabe erscheint in der Konsole, die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test klasse/05`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run klasse/05`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?“) oder OpenCode im Terminal fragen

