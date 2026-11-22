#!/usr/bin/env bash
# Startet die C++-Trainer-App — portabel für verschiedene Linux-Systeme.
# Nutzt das System-Python, wenn PyQt6 + markdown vorhanden sind,
# sonst wird automatisch eine venv in app/.venv angelegt.
set -u
cd "$(dirname "$0")"

# opencode liegt oft in ~/.opencode/bin — bei Start per Desktop-Icon ist
# der PATH sonst zu kurz (kein Shell-Profil wird geladen).
export PATH="$HOME/.opencode/bin:$PATH"

OKAY() { "$1" -c "import PyQt6, markdown" 2>/dev/null; }

PY="python3"
if ! "$PY" -c "import PyQt6" 2>/dev/null; then
  # venv verwenden — oder erzeugen, falls sie fehlt/unbrauchbar ist
  if [ ! -x .venv/bin/python ] || ! .venv/bin/python -c "import PyQt6, markdown" 2>/dev/null; then
    echo "Richte Python-Umgebung ein (.venv) — einmalig, braucht Internet …"
    if [ ! -x .venv/bin/python ]; then
      "$PY" -m venv .venv || {
        echo "Fehler: python3 -m venv fehlgeschlagen."
        echo "Debian/Ubuntu:  sudo apt install python3-venv python3-pip"
        echo "Fedora:         sudo dnf install python3-pip"
        exit 1
      }
    fi
    ./.venv/bin/pip install --quiet --upgrade pip
    ./.venv/bin/pip install --quiet -r requirements.txt
  fi
  PY=".venv/bin/python"
fi

"$PY" main.py "$@"
rc=$?
if [ "$rc" -ne 0 ]; then
  echo ""
  echo "Hinweis: Wenn Qt die Plattform 'xcb' nicht laden konnte, fehlen Systembibliotheken:"
  echo "Debian/Ubuntu:  sudo apt install libgl1 libegl1 libxkbcommon-x11-0 libxcb-cursor0"
  echo "Fedora:         sudo dnf install mesa-libGL libxkbcommon-x11 xcb-util-cursor"
fi
exit "$rc"
