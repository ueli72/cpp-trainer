# Zeiger 04 — Dynamische Queue (Original)

## Ziel

Die Prüfungsklassiker mit Zeigern: eine **verkettete Liste** als Queue
(Datenstruktur first-in-first-out) selbst bauen — Originalübung
**„Dynamic Queue"**.

## Aufgabe

Die Dateien `queue.h` (Klasse), `queue_invariant.cpp` (Invarianten-Prüfung)
und `main.cpp` (Test-Harness) sind fertig. Du schreibst in `queue.cpp`:

1. **Konstruktor** `Queue()` — leere Queue: beide Zeiger auf `nullptr`
2. `enqueue(value)` — neues Element **am Ende** anhängen
3. `dequeue()` — erstes Element entfernen und seinen Wert zurückgeben
4. `is_empty()` — `true`, wenn die Queue leer ist
5. `print_reverse()` — Werte in **umgekehrter** Reihenfolge ausgeben,
   jeweils mit einem Leerzeichen davor (so wie das gegebene `print_node`
   es vormacht) — also ohne Klammern

Gegeben ist `print()` — er zeigt die Idee: `[1 2 3]`. Die Ausgaben
erfolgen über den Harness in `main.cpp`: Befehle zeilenweise, z. B.
`enqueue 5`, `dequeue`, `is_empty`, `print`, `print_reverse`, `end`.

**Eingabe** (Beispiel):

```
enqueue 1
enqueue 2
enqueue 3
print
print_reverse
end
```

**Ausgabe** (Beispiel):

```
[1 2 3]
 3 2 1
```

> **Achtung:** `dequeue` auf einer leeren Queue ist verboten (siehe PRE
> in `queue.h`) — in den Tests passiert das nie. Die Invarianten-Prüfung
> `check_invariant()` läuft nach jedem Befehl mit.

## Hinweise

- Klasseninvariante (steht in `queue.h`): `first == nullptr` **genau dann**,
  wenn `last == nullptr` — beim enqueue/dequeue beide Zeiger sauber halten!
- `enqueue`: neuen Knoten mit `new Node(value, nullptr)` anlegen; bei
  leerer Queue zeigen `first` und `last` beide auf ihn, sonst hängt er
  hinter `last`.
- `dequeue`: Wert merken, `first` weiterziehen, alten Knoten mit
  `delete` freigeben, Invariante prüfen (war es das letzte Element?).
- `print_reverse`: Rekursion wie bei `print_node` — nur in der anderen
  Reihenfolge: **erst** rekursiv weiterlaufen, **dann** ausgeben
  (gleicher Trick wie bei den rekursiven Zahlensystemen).

## Testen

- **In der App:** 🧪 Testen — die Testfälle liegen sichtbar in `tests/`
- **Im Terminal:** `./trainer test zeiger/04`
- **Ausprobieren:** ▶ Starten (App) bzw. `./trainer run zeiger/04`
- Bei roten Tests: **Agent-Tab** („Warum schlägt mein Test fehl?") oder OpenCode im Terminal fragen
