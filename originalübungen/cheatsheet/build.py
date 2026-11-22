#!/usr/bin/env python3
"""Wandelt cheatsheet.md (Markdown-light) in cheatsheet.html um; PDF via Chrome."""
import html, re, sys, pathlib

here = pathlib.Path(__file__).parent
name = sys.argv[1] if len(sys.argv) > 1 else "cheatsheet"
src = (here / f"{name}.md").read_text(encoding="utf-8").split("\n")

KW = r"\b(int|double|float|bool|char|void|const|auto|return|if|else|for|while|do|switch|case|default|break|continue|struct|class|public|private|using|true|false|operator|static_cast|namespace)\b"

def esc(s): return html.escape(s, quote=False)

def inline(s):
    out, parts = [], re.split(r"(`[^`]+`)", s)
    for p in parts:
        if p.startswith("`") and p.endswith("`") and len(p) > 1:
            out.append("<code>" + esc(p[1:-1].replace("\\|", "|")) + "</code>")
        else:
            t = esc(p)
            t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
            t = re.sub(r"(?<![\w*])_(.+?)_(?![\w*])", r"<i>\1</i>", t)
            out.append(t)
    return "".join(out)

def hl(line):
    code, _, com = line.partition("//")
    t = esc(code)
    t = re.sub(KW, r'<span class="k">\1</span>', t)
    t = re.sub(r"(#include|#pragma once)", r'<span class="p">\1</span>', t)
    if _:
        t += '<span class="c">//' + esc(com) + "</span>"
    return t

def split_row(r):
    cells, cur, tick = [], "", False
    for ch in r.strip().strip("|") if False else r.strip():
        if ch == "`": tick = not tick
        if ch == "|" and not tick:
            cells.append(cur); cur = ""
        else:
            cur += ch
    cells.append(cur)
    return [c.strip() for c in cells[1:-1]] if r.strip().endswith("|") else [c.strip() for c in cells[1:]]

out = ['<div class="cols">']
i = 0
first_page = True
while i < len(src):
    l = src[i]
    if l.startswith("---PAGE---"):
        pass  # Seitenumbrüche ergeben sich aus dem Spaltenfluss
    elif l.startswith("```"):
        i += 1; buf = []
        while not src[i].startswith("```"):
            buf.append(hl(src[i])); i += 1
        out.append("<pre>" + "\n".join(buf) + "</pre>")
    elif l.startswith("> "):
        buf = []
        while i < len(src) and src[i].startswith("> "):
            buf.append(inline(src[i][2:])); i += 1
        i -= 1
        out.append('<div class="box">' + "<br>".join(buf) + "</div>")
    elif l.startswith("# "):
        out.append("<h1>" + inline(l[2:]) + "</h1>")
    elif l.startswith("## "):
        out.append("<h2>" + inline(l[3:]) + "</h2>")
    elif l.startswith("### "):
        out.append("<h3>" + inline(l[4:]) + "</h3>")
    elif l.startswith("|"):
        rows = []
        while i < len(src) and src[i].startswith("|"):
            rows.append(src[i]); i += 1
        i -= 1
        head = None
        if len(rows) > 1 and re.match(r"^\|[-| ]+\|$", rows[1]):
            head = split_row(rows[0]); rows = rows[2:]
        t = ["<table>"]
        if head: t.append("<tr>" + "".join("<th>" + inline(c) + "</th>" for c in head) + "</tr>")
        for r in rows:
            t.append("<tr>" + "".join("<td>" + inline(c) + "</td>" for c in split_row(r)) + "</tr>")
        t.append("</table>")
        out.append("".join(t))
    elif l.startswith("- "):
        items = []
        while i < len(src) and src[i].startswith("- "):
            items.append("<li>" + inline(src[i][2:]) + "</li>"); i += 1
        i -= 1
        out.append("<ul>" + "".join(items) + "</ul>")
    elif l.strip():
        out.append("<p>" + inline(l) + "</p>")
    i += 1
out.append("</div>")

css = (here / f"{name}.css").read_text(encoding="utf-8")
doc = f"""<!doctype html><html lang="de"><head><meta charset="utf-8"><title>C++ {name}</title>
<style>{css}</style></head><body>{''.join(out)}
</body></html>"""
(here / f"{name}.html").write_text(doc, encoding="utf-8")
print("ok")
