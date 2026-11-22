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

`./trainer test klasse/05` — die Testfälle liegen sichtbar in `tests/`
