# Distribution — C++ Trainer auf einem anderen Rechner installieren

Dieser Ordner enthält alles, um die Lernumgebung auf einem neuen
Linux-Rechner (Mint/Ubuntu/Debian) einzurichten.

## Variante 1 — mit GitHub (empfohlen)

Auf dem Zielrechner (mit git):

```bash
git clone https://github.com/<BENUTZER>/cpp-trainer.git
cd cpp-trainer
./install.sh        # richtet g++, VSCodium, OpenCode ein (sudo-Afragen möglich)
```

Die App (optionale GUI) danach starten:

```bash
cd app
./start.sh          # richtet die Python-Umgebung (.venv) automatisch ein
```

## Variante 2 — ohne GitHub

`cpp-trainer.tar.gz` aus diesem Ordner herunterladen (auf GitHub über die
Datei → „Download raw file"), dann:

```bash
tar -xzf cpp-trainer.tar.gz
cd cpp-trainer
./install.sh
cd app && ./start.sh
```

## Was `install.sh` macht

1. Systempakete: g++, make, curl
2. VSCodium (Editor)
3. OpenCode (KI-Unterstützung)
4. VSCodium-Erweiterungen (Markdown-Vorschau, Task-Buttons)
5. Lernumgebung prüfen (`./trainer list`)
6. Start + Einführung

Das Skript ist idempotent — es kann beliebig oft laufen.

### Updates

Nach dem Klonen genügt im Projektordner:

```bash
./trainer update
```

Es holt neue Aufgaben von GitHub (eigene Lösungen bleiben erhalten) und
listet neue Lektionen auf. Die GUI hat dafür den 🔄-Button.

## Für Maintainer: Paket neu bauen

Nach Änderungen am Projekt im Projektordner:

```bash
distribute/pack.sh
```

erzeugt `distribute/cpp-trainer.tar.gz` neu — ohne `build/`-Ordner,
ohne Python-Umgebung, ohne persönlichen Fortschritt.
