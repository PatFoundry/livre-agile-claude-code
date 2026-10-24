#!/usr/bin/env python3
"""Génère un site statique (une page par chapitre) dans site/ à partir des fichiers Markdown.

Usage :  python outils/build_site.py [--version v1.2.3]   (nécessite seulement le paquet « markdown »)

Sans --version, le site est écrit dans site/ (version « dev »).
Avec --version, il est écrit deux fois : à la racine de site/ (= dernière version affichée par défaut)
et dans site/v1.2.3/ (= version archivée, accessible par le sélecteur de version).
Le fichier versions.json est produit séparément par le workflow (voir .github/workflows/pages.yml).
"""
import html
import re
import shutil
import sys
from pathlib import Path

from build_pdf import (AUTHOR, PARTS, ROOT, SUBTITLE, TAGLINE, TITLE, REPO, render_md, slug,
                       split_title, typo_fr)

OUT = REPO / "site"

CSS = """
:root { --fg:#1c1c1c; --bg:#fbf9f4; --muted:#6b665b; --gold:#8a6d1f; --rule:#e2dccb; --code:#f1ede4; }
@media (prefers-color-scheme: dark) { :root { --fg:#e8e3d6; --bg:#16181d; --muted:#9a958a; --gold:#d3ab52; --rule:#2b2e36; --code:#20232b; } }
* { box-sizing: border-box; }
body { margin:0; background:var(--bg); color:var(--fg); font:18px/1.65 'Iowan Old Style',Palatino,'Palatino Linotype',Georgia,serif; }
main, header.site, footer.site, nav.pager { max-width: 40rem; margin: 0 auto; padding: 0 1.25rem; }
header.site { padding-top: 1rem; display:flex; justify-content:space-between; font-size:.85rem; color:var(--muted); }
a { color: var(--gold); } header.site a { color: inherit; text-decoration:none; }
h1 { font-weight:400; font-size:2.1rem; line-height:1.2; margin:3rem 0 1.5rem; }
.lbl { font-variant:small-caps; letter-spacing:.2em; color:var(--gold); margin-top:3rem; }
.lbl + h1 { margin-top:.3rem; }
h2 { font-size:1.25rem; margin:2.2rem 0 .6rem; } .roman h2 { font-style:italic; font-weight:400; text-align:center; }
h3 { font-size:1.05rem; font-style:italic; margin:1.6rem 0 .4rem; }
p { margin:0 0 1rem; } hr { border:0; text-align:center; margin:2rem 0; } hr::after { content:"\\2766"; color:var(--gold); }
blockquote { margin:1.2rem 0; padding:.1rem 0 .1rem 1rem; border-left:3px solid var(--gold); color:var(--muted); }
code { font:.82em Menlo,'DejaVu Sans Mono',monospace; background:var(--code); padding:.1em .3em; border-radius:3px; }
pre { background:var(--code); border-left:3px solid var(--gold); padding:.8rem 1rem; overflow-x:auto; font-size:.8rem; line-height:1.45; }
pre code { background:none; padding:0; font-size:inherit; }
table { border-collapse:collapse; width:100%; font-size:.85rem; line-height:1.4; display:block; overflow-x:auto; }
th, td { border-bottom:1px solid var(--rule); padding:.4rem .6rem; text-align:left; vertical-align:top; }
th { background:var(--code); }
section.carnet { margin:2.5rem 0 1rem; padding:.2rem 1.2rem 0; background:var(--code); border-top:3px solid var(--gold); }
nav.pager { display:flex; justify-content:space-between; gap:1rem; padding-top:1.5rem; padding-bottom:3rem; margin-top:2rem; border-top:1px solid var(--rule); font-size:.95rem; }
nav.pager span:last-child { text-align:right; }
.home { text-align:center; } .home h1 { font-size:2.8rem; margin-top:4rem; } .home .sub { font-style:italic; font-size:1.2rem; }
.home .tag { color:var(--muted); } nav.toc h2 { font-variant:small-caps; letter-spacing:.1em; border-bottom:1px solid var(--rule); padding-bottom:.3rem; }
nav.toc ul { list-style:none; padding:0; } nav.toc li { margin:.25rem 0; }
header.site select { font: inherit; color: inherit; background: var(--code); border: 1px solid var(--rule); border-radius: 4px; padding: .1rem .3rem; }
.home .ver { text-align:center; font-size:.85rem; color:var(--muted); margin-bottom: 1rem; }
.credit { font-size:.8rem; color:var(--muted); text-align:center; padding-bottom:3rem; }
"""


SELECTOR_JS = """
<script>
(function () {
  var sel = document.getElementById('ver'); if (!sel) return;
  var root = sel.dataset.root, current = sel.dataset.current;
  fetch(root + 'versions.json').then(function (r) { return r.json(); }).then(function (d) {
    var opts = [['latest', 'Dernière version (' + d.latest + ')']].concat(d.versions.map(function (v) { return [v, v]; }));
    sel.innerHTML = opts.map(function (o) {
      return '<option value="' + o[0] + '"' + (o[0] === current ? ' selected' : '') + '>' + o[1] + '</option>';
    }).join('');
    sel.hidden = false;
    sel.onchange = function () {
      var file = location.pathname.split('/').pop() || 'index.html';
      location.href = root + (sel.value === 'latest' ? '' : sel.value + '/') + file;
    };
  }).catch(function () {});
})();
</script>"""


def page(title: str, body: str, prefix: str, current: str, home: bool = False) -> str:
    sel = f'<select id="ver" data-root="{prefix}" data-current="{current}" hidden aria-label="Version du livre"></select>'
    nav = (f'<div class="ver">{sel}</div>' if home else
           f'<header class="site"><a href="index.html">{TITLE}</a><span>{sel}</span></header>')
    if home:
        body = nav + body
        nav = ""
    doc = (f'<!doctype html><html lang="fr"><head><meta charset="utf-8">'
           f'<meta name="viewport" content="width=device-width,initial-scale=1">'
           f'<title>{html.escape(title)}</title><link rel="stylesheet" href="style.css"></head>'
           f'<body>{nav}<main>{body}</main>{SELECTOR_JS}</body></html>')
    return typo_fr(doc)


def build(dest: Path, prefix: str, current: str, version: str) -> int:
    files = {d: sorted((ROOT / d).glob("*.md")) for _, _, d in PARTS}
    files["1-roman"].sort(key=lambda p: (p.stem.startswith("epilogue"), p.name))
    ids = {p.stem: slug(p) for v in files.values() for p in v}
    order = [(num, name, d, p) for num, name, d in PARTS for p in files[d]]

    dest.mkdir(parents=True, exist_ok=True)
    (dest / "style.css").write_text(CSS, encoding="utf-8")

    meta = []
    for _, _, d, p in order:
        raw = p.read_text(encoding="utf-8")
        h1 = next(l[2:].strip() for l in raw.splitlines() if l.startswith("# "))
        meta.append((split_title(h1), ids[p.stem]))

    for i, (num, name, d, p) in enumerate(order):
        (label, title), sid = meta[i]
        body = p.read_text(encoding="utf-8").split("\n", 1)[1]
        body = re.sub(r"\A\s*\*(Partie|Annexes)[^*\n]*\*\s*\n", "\n", body)
        body = body.replace("> *Schéma non reproduit dans cette version Markdown :", "> *Schéma (version numérique) :")
        h = render_md(body)
        h = re.sub(r'href="(?!https?:)[^"#]*?([^/"#]+)\.md(#[^"]*)?"',
                   lambda m: f'href="{ids[m.group(1)]}.html{m.group(2) or ""}"' if m.group(1) in ids else m.group(0), h)
        m = re.search(r"<h2>Le carnet de Thomas</h2>", h)
        if m:
            h = h[:m.start()] + '<section class="carnet">' + h[m.start():] + "</section>"
        head = (f'<div class="lbl">{html.escape(label)}</div>' if label else "") + f"<h1>{html.escape(title)}</h1>"
        prev = (f'<a href="{meta[i-1][1]}.html">← {html.escape(meta[i-1][0][1])}</a>' if i else "")
        nxt = (f'<a href="{meta[i+1][1]}.html">{html.escape(meta[i+1][0][1])} →</a>' if i + 1 < len(meta) else "")
        body_html = (f'<article class="{"roman" if d == "1-roman" else "other"}">{head}{h}</article>'
                     f'<nav class="pager"><span>{prev}</span><span>{nxt}</span></nav>')
        (dest / f"{sid}.html").write_text(page(f"{title} — {TITLE}", body_html, prefix, current), encoding="utf-8")

    toc, k = [], 0
    for num, name, d in PARTS:
        items = []
        for _ in files[d]:
            (label, title), sid = meta[k]
            k += 1
            items.append(f'<li><a href="{sid}.html">{html.escape((label + " — ") if label else "")}{html.escape(title)}</a></li>')
        toc.append(f'<nav class="toc"><h2>{num} — {name}</h2><ul>{"".join(items)}</ul></nav>')
    home = (f'<div class="home"><h1>{TITLE}</h1><p class="sub">{SUBTITLE}</p><p class="tag">{TAGLINE}</p>'
            f'<p><em>{AUTHOR}</em> · {html.escape(version)}</p></div>{"".join(toc)}'
            f'<p class="credit">Licence <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.fr">CC BY-NC-SA 4.0</a></p>')
    (dest / "index.html").write_text(page(TITLE, home, prefix, current, home=True), encoding="utf-8")
    return len(order) + 1


def main() -> None:
    version = sys.argv[sys.argv.index("--version") + 1] if "--version" in sys.argv else None
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    (OUT / ".nojekyll").write_text("")
    if version:
        n = build(OUT, "", "latest", version)
        build(OUT / version, "../", version, version)
    else:
        n = build(OUT, "", "latest", "dev")
    print(f"OK -> {OUT} ({n} pages{', version ' + version if version else ''})")


if __name__ == "__main__":
    main()
