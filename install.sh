#!/usr/bin/env bash
#
# install.sh — richtet die C++-Lernumgebung auf Linux Mint (Ubuntu/Debian) ein
#
# Aufruf:   ./install.sh [--app|--vscodium|--beides]
# Wirkung:  fragt, welche Variante installiert werden soll
#             1) Python-App   (GUI: Aufgabenbaum, Editor, Tests, KI-Agent)
#             2) VSCodium     (klassischer Workflow im Editor)
#             3) Beides
#           und installiert alles Nötige (Systempakete, OpenCode, ggf.
#           VSCodium, Python-Umgebung). Idempotent — beliebig oft lauffähig.

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

# ---------- Variante bestimmen ----------
MODUS=""
case "${1:-}" in
  --app)      MODUS="app" ;;
  --vscodium) MODUS="vscodium" ;;
  --beides)   MODUS="beides" ;;
  "") ;;
  *) echo "Unbekannte Option: $1" >&2
     echo "Aufruf: ./install.sh [--app|--vscodium|--beides]" >&2
     exit 1 ;;
esac

if [ -z "$MODUS" ]; then
  if [ -t 0 ]; then
    cat <<EOF
${C_FETT}Was soll installiert werden?${C_RESET}
  1) Nur Python-App   (GUI: Aufgabenbaum, Editor, Tests, KI-Agent)
  2) Nur VSCodium     (klassischer Workflow im Editor)
  3) Beides
EOF
    read -r -p "Auswahl [1/2/3, Enter = 3]: " wahl
    case "$wahl" in
      1) MODUS="app" ;;
      2) MODUS="vscodium" ;;
      *) MODUS="beides" ;;
    esac
  else
    MODUS="beides"
    info "Kein interaktives Terminal — es wird alles installiert (beides)."
  fi
fi

WANT_APP=false
WANT_VSCODIUM=false
case "$MODUS" in
  app)      WANT_APP=true ;;
  vscodium) WANT_VSCODIUM=true ;;
  beides)   WANT_APP=true; WANT_VSCODIUM=true ;;
esac

# ---------- 1. Systempakete ----------
schritt "1/6 Systempakete"
FEHLEND=""
command -v g++ >/dev/null 2>&1 || FEHLEND="$FEHLEND build-essential"
command -v curl >/dev/null 2>&1 || FEHLEND="$FEHLEND curl"
if [ "$WANT_APP" = true ]; then
  command -v python3 >/dev/null 2>&1 || FEHLEND="$FEHLEND python3"
  if ! python3 -c "import ensurepip" 2>/dev/null; then
    FEHLEND="$FEHLEND python3-venv python3-pip"
  fi
fi
if [ -z "${FEHLEND# }" ]; then
  ok "Alle benötigten Systempakete sind bereits installiert."
else
  if ! command -v apt-get >/dev/null 2>&1; then
    echo "Kein apt-get gefunden — bitte von Hand installieren:$FEHLEND" >&2
    exit 1
  fi
  if [ -z "$SUDO" ] && [ "$(id -u)" -ne 0 ]; then
    echo "Weder Root-Rechte noch sudo verfügbar — bitte als Nutzer mit sudo ausführen." >&2
    exit 1
  fi
  info "Installiere:$FEHLEND (sudo-Afrage kann kommen) …"
  $SUDO apt-get update
  # shellcheck disable=SC2086
  $SUDO apt-get install -y $FEHLEND
fi

# ---------- 2. VSCodium ----------
if [ "$WANT_VSCODIUM" = true ]; then
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
else
  schritt "2/6 VSCodium (Editor)"
  info "übersprungen — Variante ohne VSCodium gewählt."
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
if [ "$WANT_VSCODIUM" = true ]; then
  schritt "4/6 VSCodium-Erweiterungen (Markdown-Vorschau, Statusleisten-Buttons)"
  VSCODIUM_BIN=""
  if command -v codium >/dev/null 2>&1; then
    VSCODIUM_BIN="codium"
  elif command -v vscodium >/dev/null 2>&1; then
    VSCODIUM_BIN="vscodium"
  fi
  if [ -n "$VSCODIUM_BIN" ]; then
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
  else
    info "VSCodium nicht gefunden — Erweiterungen werden übersprungen."
  fi
else
  schritt "4/6 VSCodium-Erweiterungen"
  info "übersprungen — Variante ohne VSCodium gewählt."
fi

# ---------- 5. Lernumgebung prüfen ----------
schritt "5/6 Lernumgebung prüfen"
chmod +x trainer lernen 2>/dev/null || chmod +x trainer
if [ "$WANT_APP" = true ]; then
  chmod +x app/start.sh 2>/dev/null || true
fi
echo "g++:       $(g++ --version | head -1)"
echo "opencode:  $(opencode --version)"
./trainer list

# ---------- 6. Start ----------
schritt "6/6 Start"
cat <<EOF
${C_FETT}Willkommen beim C++-Trainer!${C_RESET}

So lernst du:
  1. Aufgabe lesen:   lektionen/<thema>/<lektion>/README.md
  2. Code schreiben:  main.cpp (App-Editor oder VSCodium)
  3. Testen:          App: 🧪-Button  |  Terminal: ./trainer test <lektion>
  4. Hilfe:           Agent-Tab (App) oder OpenCode-Chat
     z. B. „Teste meine Lösung“ oder „Warum schlägt mein Test fehl?“
EOF

START_APP=false
if [ "$WANT_APP" = true ] && [ -t 0 ] && [ -t 1 ]; then
  START_APP=true
fi

if [ "$START_APP" = true ]; then
  printf '\n%sDie App wird gestartet …%s\n' "$C_FETT" "$C_RESET"
  (cd app && ./start.sh)
  info "(Später starten: cd app && ./start.sh — oder ./install.sh erneut laufen lassen.)"
elif [ "$WANT_VSCODIUM" = true ] && [ -t 0 ] && [ -t 1 ]; then
  printf '\n%sOpenCode wird gestartet …%s\n' "$C_FETT" "$C_RESET"
  exec opencode
else
  info ""
  info "Kein interaktives Terminal — später starten:"
  [ "$WANT_APP" = true ] && info "  App:        cd app && ./start.sh"
  [ "$WANT_VSCODIUM" = true ] && info "  VSCodium:   opencode  (dann /lernen eintippen)"
  exit 0
fi
