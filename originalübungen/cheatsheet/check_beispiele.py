#!/usr/bin/env python3
"""Prüft die Codebeispiele in lernskript.md (und cheatsheet.md, soweit möglich).

Info-Wort hinter den drei Backticks bestimmt die Prüfung:
  run   vollständiges Programm: kompilieren, ausführen, '// Eingabe:' füttern,
        '// Ausgabe:'-Zeilen mit der echten Ausgabe vergleichen
  decl  nur Deklarationen/Funktionen: Syntaxcheck
  frag  Anweisungen: in main() verpackt, Syntaxcheck
  skip  wird nicht geprüft (Fehlerbeispiele, Dateiausschnitte)
"""
import re, subprocess, sys, tempfile, pathlib

here = pathlib.Path(__file__).parent
name = sys.argv[1] if len(sys.argv) > 1 else "lernskript"
text = (here / f"{name}.md").read_text(encoding="utf-8")
PRE = ("#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n"
       "#include <cassert>\n#include <cmath>\n#include <climits>\n#include <algorithm>\n#include <iomanip>\n")
blocks = re.findall(r"```(\w*)\n(.*?)```", text, re.S)
bad = 0
tmp = pathlib.Path(tempfile.mkdtemp(prefix="chk_", dir="/tmp/opencode" if pathlib.Path("/tmp/opencode").exists() else None))
for n, (kind, code) in enumerate(blocks, 1):
    if kind in ("", "skip"): continue
    first = code.strip().split("\n")[0][:60]
    if kind == "run":
        src = code if "#include" in code else PRE + code
    elif kind == "decl":
        src = PRE + code + "\nint main() {}\n"
    elif kind == "frag":
        src = PRE + "int main() {\n" + code + "\n}\n"
    else:
        print(f"Block {n}: unbekannter Typ {kind}"); bad += 1; continue
    f = tmp / f"b{n}.cpp"; f.write_text(src, encoding="utf-8")
    cmd = ["g++", "-std=c++20", "-Wall", "-o", str(tmp / f"b{n}")] if kind == "run" else ["g++", "-std=c++20", "-fsyntax-only", "-Wall"]
    r = subprocess.run(cmd + [str(f)], capture_output=True, text=True)
    if r.returncode != 0:
        print(f"[FEHLER] Block {n} ({kind}): {first}\n{r.stderr[:600]}"); bad += 1; continue
    if kind == "run":
        inp = "\n".join(re.findall(r"^\s*// Eingabe: ?(.*)$", code, re.M)) + "\n"
        exp = [l.rstrip() for l in re.findall(r"^\s*// Ausgabe: ?(.*)$", code, re.M)]
        run = subprocess.run([str(tmp / f"b{n}")], input=inp, capture_output=True, text=True, timeout=10)
        got = [l.rstrip() for l in run.stdout.split("\n")]
        while got and got[-1] == "": got.pop()
        if exp and got != exp:
            print(f"[AUSGABE] Block {n}: {first}\n  erwartet: {exp}\n  erhalten: {got}"); bad += 1
print("Geprüft:", sum(1 for k, _ in blocks if k not in ("", "skip")), "Blöcke, Probleme:", bad)
sys.exit(1 if bad else 0)
