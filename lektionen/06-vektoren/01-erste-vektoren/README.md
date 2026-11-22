# Vektoren 01 — Erste Vektoren

## Ziel

`std::vector<int>` kennenlernen: eine **wachsende Liste** für ganze Zahlen —
im Gegensatz zu einzelnen Variablen beliebig viele Werte in einem Container.

## Aufgabe

Lies beliebig viele ganze Zahlen ein (Ende durch Dateiende/Strg+D) und
gib aus:
- **Anzahl:** wie viele Zahlen gelesen wurden
- **Summe:** die Summe aller Zahlen

## SOLL-Verhalten (Beispiel)

```
1 2 3 4 5
```

```
Anzahl: 5
Summe: 15
```

## Hinweise

- `zahlen.push_back(x)` hängt eine Zahl **hinten an** die Liste.
- `zahlen.size()` liefert die **Anzahl** der Elemente.
- `zahlen[i]` greift auf das i-te Element zu — **ab 0 gezählt!**
- Das Einlesen läuft wie gewohnt: `while (std::cin >> x)`

## Testen
- **In der App:** Lektion im Baum wählen → 💾 Speichern (bei Änderungen) → 🧪 Testen — die Ausgabe erscheint in der Konsole, die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test vektoren/01`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run vektoren/01`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?“) oder OpenCode im Terminal fragen

