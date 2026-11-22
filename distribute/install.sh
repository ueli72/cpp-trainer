#!/usr/bin/env bash
#
# install.sh — richtet die C++-Lernumgebung auf Linux Mint (Ubuntu/Debian) ein
#
# Aufruf:   ./install.sh
# Wirkung:  installiert bei Bedarf g++/make/curl, VSCodium und OpenCode,
#           richtet die VSCodium-Erweiterungen ein, prüft die Umgebung und
#           startet OpenCode mit einer Einführung.
#           Alles ist idempotent — das Skript kann beliebig oft gelaufen werden.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

if [ -t 1 ]; then
  C_FETT=$'\033[1m'; C_GRUEN=$'\033[1;32m'; C_GELB=$'\033[33m'; C_GRAU=$'\033[90m'; C_RESET=$'\033[0m'
else
  C_FETT=""; C_GRUEN=""; C_GELB=""; C_GRAU=""; C_RESET=""
fi

schritt() { printf '\n%s== %s ==%s\n' "$C_FETT" "$1" "$C_RESET"; }
ok()      { printf '%s✔%s %s\n' "$C_GRUEN" "$C_RESET" "$1"; }
info()    { printf '%s%s%s\n' "$C_GRAU" "$1" "$C_RESET"; }

SUDO=""
if [ "$(id -u)" -ne 0 ] && command -v sudo >/dev/null 2>&1; then
  SUDO="sudo"
fi

# ---------- 1. Systempakete ----------
schritt "1/6 Systempakete (g++, make, curl)"
if command -v g++ >/dev/null 2>&1 && command -v make >/dev/null 2>&1 && command -v curl >/dev/null 2>&1; then
  ok "g++, make und curl sind bereits installiert."
else
  if ! command -v apt-get >/dev/null 2>&1; then
    echo "Kein apt-get gefunden — bitte g++, make und curl von Hand installieren." >&2
    exit 1
  fi
  if [ -z "$SUDO" ] && [ "$(id -u)" -ne 0 ]; then
    echo "Weder Root-Rechte noch sudo verfügbar — bitte als Nutzer mit sudo ausführen." >&2
    exit 1
  fi
  info "Installiere build-essential und curl (sudo-Afrage kann kommen) …"
  $SUDO apt-get update
  $SUDO apt-get install -y build-essential curl
fi

# ---------- 2. VSCodium ----------
schritt "2/6 VSCodium (Editor)"
if command -v codium >/dev/null 2>&1 || command -v vscodium >/dev/null 2>&1; then
  ok "VSCodium ist bereits installiert."
else
  if ! command -v apt-get >/dev/null 2>&1; then
    info "Kein apt-get gefunden — bitte VSCodium von https://vscodium.com von Hand installieren."
  elif [ -z "$SUDO" ] && [ "$(id -u)" -ne 0 ]; then
    info "Ohne sudo kann VSCodium nicht installiert werden — bitte nachholen (siehe vscodium.com)."
  else
    info "Richte das offizielle VSCodium-Repository ein und installiere …"
    curl -fsSL https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/raw/master/pub.gpg \
      | gpg --dearmor \
      | $SUDO dd of=/usr/share/keyrings/vscodium-archive-keyring.gpg
    echo 'deb [ signed-by=/usr/share/keyrings/vscodium-archive-keyring.gpg ] https://paulcarroty.gitlab.io/vscodium-deb-rpm-repo/deb vscodium main' \
      | $SUDO tee /etc/apt/sources.list.d/vscodium.list > /dev/null
    $SUDO apt-get update
    $SUDO apt-get install -y codium
  fi
fi

# ---------- 3. OpenCode ----------
schritt "3/6 OpenCode (KI-Unterstützung)"
if command -v opencode >/dev/null 2>&1; then
  ok "OpenCode ist bereits installiert ($(opencode --version 2>/dev/null || echo 'Version unbekannt'))."
else
  info "Installiere OpenCode über das offizielle Skript …"
  curl -fsSL https://opencode.ai/install | bash
  export PATH="$HOME/.opencode/bin:$PATH"
fi
if ! command -v opencode >/dev/null 2>&1; then
  echo "OpenCode wurde nicht gefunden. Terminal neu öffnen oder ausführen:" >&2
  echo '  export PATH="$HOME/.opencode/bin:$PATH"' >&2
  exit 1
fi

# ---------- 4. VSCodium-Erweiterungen ----------
schritt "4/6 VSCodium-Erweiterungen (Markdown-Vorschau, Statusleisten-Buttons)"
VSCODIUM_BIN=""
if command -v codium >/dev/null 2>&1; then
  VSCODIUM_BIN="codium"
elif command -v vscodium >/dev/null 2>&1; then
  VSCODIUM_BIN="vscodium"
fi
if [ -n "$VSCODIUM_BIN" ]; then
  # Schönere Markdown-Vorschau + Statusleisten-Buttons der Lernumgebung
  ERWEITERUNGEN=(
    "shd101wyy.markdown-preview-enhanced"   # Markdown Preview Enhanced
    "spencerwmiles.vscode-task-buttons"     # Task Buttons (🧪 ▶ 🔧 ☑ 📖)
  )
  for ext in "${ERWEITERUNGEN[@]}"; do
    if "$VSCODIUM_BIN" --list-extensions 2>/dev/null | grep -qi "^${ext}\$"; then
      ok "bereits installiert: $ext"
    else
      info "Installiere: $ext …"
      if "$VSCODIUM_BIN" --install-extension "$ext" > /dev/null 2>&1; then
        ok "$ext installiert."
      else
        info "$ext konnte nicht installiert werden — bitte von Hand im Erweiterungen-Panel installieren."
      fi
    fi
  done

  # Markdown-Vorschau als Standard: Strg+Shift+V und Strg+K V öffnen
  # Markdown Preview Enhanced statt der eingebauten Vorschau.
  # Nur anlegen, wenn noch keine Benutzertastenkürzel existieren.
  KEYB="$HOME/.config/VSCodium/User/keybindings.json"
  mkdir -p "$(dirname "$KEYB")"
  if [ -f "$KEYB" ]; then
    info "Vorhandene Tastenkürzel wurden nicht verändert ($KEYB)."
  else
    cat > "$KEYB" <<'JSON'
[
  {
    "key": "ctrl+shift+v",
    "command": "-markdown.showPreview",
    "when": "editorLangId == markdown"
  },
  {
    "key": "ctrl+k v",
    "command": "-markdown.showPreviewToSide",
    "when": "editorLangId == markdown"
  },
  {
    "key": "ctrl+shift+v",
    "command": "markdown-preview-enhanced.openPreview",
    "when": "editorLangId == markdown"
  },
  {
    "key": "ctrl+k v",
    "command": "markdown-preview-enhanced.openPreviewToTheSide",
    "when": "editorLangId == markdown"
  }
]
JSON
    ok "Standard-Vorschau: Strg+Shift+V / Strg+K V öffnen jetzt Markdown Preview Enhanced."
  fi
else
  info "VSCodium nicht gefunden — Erweiterungen werden übersprungen."
  info "(Ohne VSCodium: Erweiterung 'Markdown Preview Enhanced' im Erweiterungsmarkt deines Editors suchen.)"
fi

# ---------- 5. Lernumgebung prüfen ----------
schritt "5/6 Lernumgebung prüfen"
# Ausführungsrechte können z. B. beim Kopieren per FAT-USB-Stick verloren gehen
chmod +x trainer lernen 2>/dev/null || chmod +x trainer
echo "g++:       $(g++ --version | head -1)"
echo "opencode:  $(opencode --version)"
./trainer list

# ---------- 6. Start ----------
schritt "6/6 Start"
cat <<EOF
${C_FETT}Willkommen beim C++-Trainer!${C_RESET}

So lernst du:
  1. Aufgabe lesen:    lektionen/<lektion>/README.md  (im VSCodium-Editor)
  2. Code schreiben:   lektionen/<lektion>/main.cpp
  3. Testen:           ./trainer test <lektion>  (oder Strg+Shift-B / 🧪-Button)
  4. Ausprobieren:     ./trainer run <lektion>
  5. Hilfe von der KI: hier im OpenCode-Chat fragen, z. B.
                         „Teste meine Lösung“
                         „Warum schlägt mein Test fehl?“

Nützliches:
  ./trainer list                 Lektionen anzeigen
  ./trainer new 02-variablen     neue Lektion anlegen
  /lernen (im OpenCode-Chat)     geführte Einführung durch die KI
EOF

# Nur in einem interaktiven Terminal automatisch starten
if [ ! -t 0 ] || [ ! -t 1 ]; then
  info ""
  info "Kein interaktives Terminal — OpenCode wird nicht automatisch gestartet."
  info "Starten:  cd $ROOT && opencode   (dann /lernen eintippen)"
  exit 0
fi

printf '\n%sOpenCode begrüßt dich mit einer Einführung …%s\n' "$C_FETT" "$C_RESET"
if ! timeout 180 opencode run "Stelle dich in einem bis zwei Sätzen auf Deutsch vor und erkläre dem Nutzer knapp, wie das Lernen mit diesem C++-Trainer abläuft: (1) Aufgabe in lektionen/<lektion>/README.md lesen, (2) main.cpp in VSCodium bearbeiten, (3) im Terminal ./trainer test <lektion> ausführen oder Strg+Shift+B bzw. den Tests-Button in VSCodium nutzen, (4) bei roten Tests hier im Chat um Hilfe fragen (z. B. „Teste meine Lösung“). Führe ./trainer list aus und nenne die vorhandenen Lektionen. Beende damit, dass man für die geführte Einführung /lernen tippen kann."; then
  printf '%sHinweis:%s Die KI-Begrüßung war nicht möglich — vermutlich ist OpenCode auf\n' "$C_GELB" "$C_RESET"
  info "diesem Rechner noch nicht eingerichtet. Die OpenCode-Oberfläche hilft beim ersten Start."
  info "Danach im Chat: /lernen"
fi

printf '\n%sOpenCode wird gestartet …%s\n' "$C_FETT" "$C_RESET"
exec opencode
