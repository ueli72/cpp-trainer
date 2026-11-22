# Klasse 06 — Brüche multiplizieren (Eigenbau)

## Ziel

Structs frei anwenden, ohne Vorlage: einen eigenen Bruch-Typ definieren, das bekannte Trennzeichen-Trick-Muster auf den Bruchstrich `/` übertragen und zwei Brüche multiplizieren.

## Aufgabe

Definiere ein `struct Bruch` mit zwei `int`-Membern `zaehler` und `nenner`.

Lies zwei Brüche ein — **jeweils in einer eigenen Zeile**, im Format `z/n` (z. B. `3/4` und `5/6`).

Gib ihr **Produkt** aus — Zähler mal Zähler, Nenner mal Nenner, **nicht kürzt**:

**Eingabe** (Beispiel):

```
3/4
5/6
```

**Ausgabe** (Beispiel):

```
Produkt: 15/24
```

## Wie du vorgehst

Der **Bauplan steht als Kommentare in `main.cpp`** — vier Schritte, alles daraus schon einmal gebaut:

| Baustein | Gelernt in |
|---|---|
| `struct` mit Membern | Struct 01 |
| Trennzeichen per `char` wegschlucken | Eingabe-Reihe (jetzt: `/` statt `,`) |
| Werte verrechnen | Eingabe 02 |
| Ausgabe mit `<<` zusammensetzen | überall |

## Hinweise

- Vorzeichen wandern von selbst mit: `-1/3 * 2/5 = -2/15`.
- Nenner 1 ist erlaubt (`5/1 * 3/2 → Produkt: 15/2`) — nicht vereinfachen!
- Kein Kürzen, keine Dezimalzahl — exakt `Produkt: <z>/<n>`.

## So testest du

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test klasse/06`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run struct/03`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?“) oder OpenCode im Terminal fragen
