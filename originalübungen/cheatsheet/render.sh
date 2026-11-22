#!/bin/bash
# Baut Cheatsheet und Lernskript neu (HTML -> PDF via Chrome headless)
# Aufruf: ./render.sh [cheatsheet|lernskript]   (ohne Argument: beide)
cd "$(dirname "$0")"
for n in ${1:-cheatsheet lernskript}; do
  [ -f "$n.md" ] || continue
  python3 build.py "$n" || exit 1
  google-chrome --headless=new --no-sandbox --disable-gpu --no-pdf-header-footer --print-to-pdf="$n.pdf" "file://$PWD/$n.html" 2>&1 | tail -1
  python3 -c "
import re;d=open('$n.pdf','rb').read();print('$n: Seiten:',len(re.findall(rb'/Type\s*/Page[^s]',d)))"
done
