#!/usr/bin/env bash
# pack.sh — baut distribute/cpp-trainer.tar.gz: das Projekt ohne Laufzeit-Daten.
# Aufruf:  ./pack.sh   (aus diesem Ordner oder dem Projektordner)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

OUT="distribute/cpp-trainer.tar.gz"
mkdir -p distribute
rm -f "$OUT" "$OUT.tmp"

# Installations-Kopie immer aktuell halten
cp install.sh distribute/install.sh

tar -czf "$OUT.tmp" \
    --exclude="./distribute" \
    --exclude="./.git" \
    --exclude="./app/.venv" \
    --exclude="./fortschritt.json" \
    --exclude="__pycache__" \
    --exclude="*.pyc" \
    --exclude="*/build" \
    --exclude="build" \
    --transform "s,^\./,cpp-trainer/," \
    -C "$ROOT" \
    .

mv "$OUT.tmp" "$OUT"

echo "Paket erstellt: $OUT ($(du -h "$OUT" | cut -f1))"
echo "Inhalt prüfen:  tar -tzf $OUT | less"
