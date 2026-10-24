#!/usr/bin/env python3
"""Compose le livre « Le Sprint d'après » en PDF à partir des fichiers Markdown.

Usage :  ./outils/build.sh            (crée le venv si besoin, produit build/le-sprint-d-apres.pdf)
         ./outils/build.sh --html     (écrit aussi build/livre.html, pratique pour déboguer la mise en page)
"""
import html
import re
import sys
from pathlib import Path

import markdown

REPO = Path(__file__).resolve().parent.parent
ROOT = REPO / "le-sprint-d-apres"  # sources Markdown
OUT = REPO / "build"
TITLE = "Le Sprint d'après"
SUBTITLE = "Agilité, agents et spécifications"
TAGLINE = "Un roman d'entreprise et un manuel pour travailler avec Claude Code et BMAD"
AUTHOR = "Patrick Lecocq"
PARTS = [
    ("Partie I", "Le roman", "1-roman"),
    ("Partie II", "Le manuel de référence", "2-manuel"),
    ("Annexes", "Les outils du quotidien", "3-annexes"),
]

CSS = """
@font-face { font-family: Livre; src: local('Iowan Old Style'), local('Palatino'), local('P052'), local('Georgia'); }
@page { size: 148mm 210mm; margin: 20mm 18mm 24mm 18mm; }
@page :left  { margin-left: 20mm; margin-right: 16mm;
  @bottom-left  { content: counter(page); font: 9pt Livre; color: #444; }
  @top-left     { content: string(booktitle, start); font: italic 8.5pt Livre; color: #666; } }
@page :right { margin-left: 16mm; margin-right: 20mm;
  @bottom-right { content: counter(page); font: 9pt Livre; color: #444; }
  @top-right    { content: string(chaptertitle, start); font: italic 8.5pt Livre; color: #666; } }

@page cover { margin: 0; @top-left{content:none} @top-right{content:none}
  @bottom-left{content:none} @bottom-right{content:none} }
@page blank { @top-left{content:none} @top-right{content:none}
  @bottom-left{content:none} @bottom-right{content:none} }
@page front:left  { @bottom-left{content:none} @top-left{content:none} }
@page front:right { @bottom-right{content:none} @top-right{content:none} }
@page chapter:left  { margin-left: 20mm; margin-right: 16mm;
  @bottom-left  { content: counter(page); font: 9pt Livre; color: #444; }
  @top-left     { content: string(booktitle, start); font: italic 8.5pt Livre; color: #666; } }
@page chapter:right { margin-left: 16mm; margin-right: 20mm;
  @bottom-right { content: counter(page); font: 9pt Livre; color: #444; }
  @top-right    { content: string(chaptertitle, start); font: italic 8.5pt Livre; color: #666; } }
@page part { @top-left{content:none} @top-right{content:none}
  @bottom-left{content:none} @bottom-right{content:none} }

html { font: 10.4pt/1.5 Livre, 'Iowan Old Style', Palatino, P052, serif; color: #1c1c1c;
       hyphens: auto; -weasy-hyphens: auto; }
html, body { lang: fr; }
body { margin: 0; text-align: justify; orphans: 3; widows: 3; }
p { margin: 0; text-indent: 1.3em; }
h1 + p, h2 + p, h3 + p, hr + p, blockquote + p, table + p, pre + p, ul + p, ol + p, .nofirst { text-indent: 0; }
h1, h2, h3, h4 { text-align: left; hyphens: manual; break-after: avoid; }

/* --- couverture --- */
section.cover { page: cover; break-after: page; background: #14213d; color: #f4efe6;
  width: 148mm; height: 210mm; position: relative; text-align: center; }
.cover .rule { position:absolute; left:24mm; right:24mm; height:0.6mm; background:#c9a24b; }
.cover .rule.top { top: 34mm; } .cover .rule.bottom { bottom: 34mm; }
.cover .author { position:absolute; top: 18mm; left:0; right:0; font: 10pt Livre; letter-spacing: .35em;
  text-transform: uppercase; color:#c9a24b; }
.cover h1 { position:absolute; top: 62mm; left:14mm; right:14mm; margin:0; font: 400 38pt/1.1 Livre;
  text-align:center; color:#f4efe6; }
.cover .sub { position:absolute; top: 108mm; left:20mm; right:20mm; font: italic 14pt/1.35 Livre; color:#e6d9bd; text-align:center; }
.cover .tag { position:absolute; bottom: 44mm; left:22mm; right:22mm; font: 9.5pt/1.5 Livre; letter-spacing:.04em; color:#bfb8a8; text-align:center; }

/* --- pages liminaires --- */
section.front { page: front; }
section.halftitle { page: blank; break-after: page; text-align:center; padding-top: 70mm; }
.halftitle h1 { font: 400 24pt Livre; text-align:center; margin:0; }
section.titlepage { page: blank; break-after: page; text-align:center; padding-top: 38mm; }
.titlepage .a { font: 11pt Livre; letter-spacing:.3em; text-transform:uppercase; }
.titlepage h1 { font: 400 34pt/1.1 Livre; margin: 32mm 0 6mm; text-align:center; }
.titlepage .s { font: italic 13pt/1.4 Livre; text-align:center; }
.titlepage .o { width: 18mm; margin: 14mm auto; border-top: .4mm solid #c9a24b; }
.titlepage .t { font: 9.5pt/1.5 Livre; color:#555; text-align:center; padding: 0 14mm; }
section.colophon { page: blank; break-before: left; break-after: page; font-size: 8.5pt; line-height:1.5; color:#444;
  padding-top: 120mm; text-align:left; }
.colophon p { text-indent:0; margin-bottom: 2mm; }

nav#toc { page: front; break-before: right; }
nav#toc h1 { font: 400 20pt Livre; margin: 0 0 8mm; text-align:center; }
nav#toc .part { font: small-caps 600 11pt Livre; letter-spacing:.08em; margin: 6mm 0 2mm; break-after: avoid; }
nav#toc a { display:block; color: inherit; text-decoration:none; font-size: 9.2pt; line-height:1.55; text-align:left; }
nav#toc a::after { content: leader('.') target-counter(attr(href), page); }
nav#toc a.part { font: small-caps 600 10.5pt Livre; letter-spacing:.06em; margin-top:4mm; }

/* --- parties --- */
section.part { page: part; break-before: right; break-after: page;   text-align:center; padding-top: 62mm; }
section.part .n { font: small-caps 12pt Livre; letter-spacing:.3em; color:#8a6d1f; }
section.part h1 { font: 400 30pt/1.15 Livre; text-align:center; margin: 8mm 0 6mm; string-set: chaptertitle none; }
section.part .o { width: 18mm; margin: 6mm auto; border-top: .4mm solid #c9a24b; }
section.part .d { font: italic 10.5pt/1.5 Livre; padding: 0 12mm; text-align:center; color:#444; }

/* --- chapitres --- */
section.chapter { page: chapter; break-before: right; string-set: booktitle "@@TITLE@@"; }
.endmark { height: 0; string-set: booktitle "" chaptertitle ""; }
section.chapter > h1 { string-set: chaptertitle content(); }
.chapter > header { text-align:center; margin: 26mm 0 14mm; }
.chapter > header .lbl { font: small-caps 11pt Livre; letter-spacing:.3em; color:#8a6d1f; }
.chapter > header h1 { font: 400 22pt/1.2 Livre; text-align:center; margin: 4mm 0 0; string-set: chaptertitle content(); }
.chapter > header .o { width: 14mm; margin: 6mm auto 0; border-top: .4mm solid #c9a24b; }
.chapter > header + p { text-indent: 0; }

h2 { font: 600 11.5pt/1.3 Livre; margin: 7mm 0 3mm; text-align:left; }
.roman h2 { font: italic 400 11pt/1.3 Livre; text-align:center; margin: 8mm 0 4mm; letter-spacing:.02em; }
h3 { font: italic 600 10.5pt/1.3 Livre; margin: 5mm 0 2mm; }
h4 { font: 600 10pt Livre; margin: 4mm 0 1.5mm; }
hr { border: 0; margin: 5mm auto; text-align:center; height: 4mm; }
hr::after { content: "\\2766"; display:block; color:#8a6d1f; font-size: 11pt; }

blockquote { margin: 3mm 0 3mm 4mm; padding: 1mm 0 1mm 4mm; border-left: .5mm solid #c9a24b; font-size: 9.8pt; color:#333; }
blockquote p { text-indent: 0; margin: 0 0 1.5mm; }
ul, ol { margin: 2mm 0 2mm 0; padding-left: 6mm; }
li { margin: 0 0 1mm; text-align: left; } li p { text-indent:0; }
a { color: inherit; text-decoration: none; }
strong { font-weight: bold; }

code { font: 8.4pt Menlo, 'DejaVu Sans Mono', monospace; background: #f1ede4; padding: 0 .8mm; border-radius: .6mm; hyphens: none; word-break: break-word; }
pre { font: 7.6pt/1.4 Menlo, 'DejaVu Sans Mono', monospace; background: #f4f1ea; border-left: .8mm solid #c9a24b; padding: 2.5mm 3mm;
  margin: 3mm 0; white-space: pre-wrap; word-break: break-all; text-align:left; break-inside: auto; hyphens: none; }
pre code { background: none; padding: 0; font: inherit; word-break: break-all; }

table { width: 100%; border-collapse: collapse; margin: 3.5mm 0; font-size: 8.4pt; line-height:1.35; text-align:left; }
th { font-weight: 600; background: #ebe5d6; border-bottom: .3mm solid #8a6d1f; }
th, td { padding: 1.2mm 1.8mm; vertical-align: top; hyphens: manual; }
td { border-bottom: .15mm solid #cfc8b5; }
tr { break-inside: avoid; }

/* --- le carnet de Thomas --- */
section.carnet { margin-top: 9mm; padding: 4mm 5mm 3mm; background: #f6f1e3; border-top: .6mm solid #c9a24b;
  border-bottom: .2mm solid #c9a24b; font-size: 9.6pt; line-height: 1.45; }
section.carnet h2 { font: small-caps 600 12pt Livre; letter-spacing:.08em; text-align:center; margin: 0 0 3mm; color:#8a6d1f; }
section.carnet h3 { font: italic 600 10pt Livre; margin: 3mm 0 1mm; }
section.carnet p { text-indent: 0; margin-bottom: 1.5mm; }
section.carnet li { text-align:left; }
"""

NBSP = " "
NNBSP = " "


def typo_fr(fragment: str) -> str:
    """Espaces insécables françaises dans le texte courant (hors code et balises)."""
    out, depth_code = [], 0
    for tok in re.split(r"(<[^>]+>)", fragment):
        if tok.startswith("<"):
            if re.match(r"<(pre|code)\b", tok):
                depth_code += 1
            elif re.match(r"</(pre|code)>", tok):
                depth_code -= 1
            out.append(tok)
            continue
        if depth_code > 0:
            out.append(tok)
            continue
        tok = re.sub(r"[  ]+([;!?»:])", lambda m: (NNBSP if m.group(1) in ";!?»" else NBSP) + m.group(1), tok)
        tok = re.sub(r"«[  ]*", "«" + NNBSP, tok)
        tok = re.sub(r"(\d) (?=\d{3}\b)", r"\1" + NNBSP, tok)
        tok = re.sub(r"\b(\d+) (h|min|s|%|€|Mo|Go|ko|k€|M€)\b", r"\1" + NBSP + r"\2", tok)
        out.append(tok)
    return "".join(out)


def slug(path: Path) -> str:
    return "f-" + re.sub(r"[^a-z0-9]+", "-", path.stem.lower()).strip("-")


def split_title(h1: str) -> tuple[str, str]:
    """« Chapitre 1 — Quatorze semaines » -> ('Chapitre 1', 'Quatorze semaines')."""
    m = re.match(r"^(.*?)\s+[—–]\s+(.*)$", h1)
    if not m:
        return "", h1
    label, title = m.groups()
    if re.fullmatch(r"M\d+", label):
        label = f"Chapitre {label}"
    return label, title


def render_md(text: str) -> str:
    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "attr_list"])
    return md.convert(text)


def build_chapter(path: Path, part_cls: str, ids: dict[str, str], first: bool) -> tuple[str, str, str]:
    raw = path.read_text(encoding="utf-8")
    lines = raw.splitlines()
    h1 = next(l[2:].strip() for l in lines if l.startswith("# "))
    body = "\n".join(l for l in lines if not l.startswith("# ")) if False else raw.split("\n", 1)[1]
    # supprime la ligne d'étiquette en italique (« Partie II — … ») juste après le titre
    body = re.sub(r"\A\s*\*[^*\n]+\*\s*\n", "\n", body, count=1) if re.match(r"\A\s*\*(Partie|Annexes)", body) else body
    # le schéma interactif non reproduit : on garde la mention, discrètement
    body = body.replace("> *Schéma non reproduit dans cette version Markdown :", "> *Schéma (version numérique) :")
    h = render_md(body)
    h = re.sub(r'href="([^"#]*?)([^/"#]+)\.md(#[^"]*)?"',
               lambda m: f'href="#{ids[m.group(2)]}"' if m.group(2) in ids and not m.group(1).startswith("http") else m.group(0), h)
    # carnet de Thomas
    m = re.search(r"<h2>Le carnet de Thomas</h2>", h)
    if m:
        h = h[:m.start()] + '<section class="carnet">' + h[m.start():] + "</section>"
    label, title = split_title(h1)
    sid = ids[path.stem]
    head = (f'<header id="{sid}"><div class="lbl">{html.escape(label)}</div><h1>{html.escape(title)}</h1><div class="o"></div></header>'
            if label else f'<h1 id="{sid}">{html.escape(title)}</h1>')
    cls = f"chapter {part_cls}"
    sec = f'<section class="{cls}">{head}{h}<div class="endmark"></div></section>'
    toc_label = f"{label} — {title}" if label else title
    return sec, toc_label, sid


def main() -> None:
    import logging
    from weasyprint import HTML
    logging.getLogger("weasyprint").setLevel(logging.WARNING)
    want_html = "--html" in sys.argv
    OUT.mkdir(exist_ok=True)

    files = {key: sorted((ROOT / d).glob("*.md")) for _, _, d in PARTS for key in [d]}
    # ordre : chapitres numérotés, épilogue à la fin
    files["1-roman"].sort(key=lambda p: (p.stem.startswith("epilogue"), p.name))
    ids = {p.stem: slug(p) for v in files.values() for p in v}

    body, toc, first = [], [], True
    descs = {
        "1-roman": "Vingt-sept chapitres et un épilogue.",
        "2-manuel": "Installer, configurer et utiliser Claude Code et BMAD.",
        "3-annexes": "Modèles, grilles et glossaire.",
    }
    for i, (num, name, d) in enumerate(PARTS):
        pid = f"part-{i}"
        toc.append(f'<a class="part" href="#{pid}">{num} — {name}</a>')
        body.append(f'<section class="part{" firstbody" if i == 0 else ""}" id="{pid}"><div class="n">{num}</div><h1>{name}</h1>'
                    f'<div class="o"></div><div class="d">{descs[d]}</div></section>')
        cls = {"1-roman": "roman", "2-manuel": "manuel", "3-annexes": "annexe"}[d]
        for p in files[d]:
            sec, label, sid = build_chapter(p, cls, ids, first)
            first = False
            body.append(sec)
            toc.append(f'<a href="#{sid}">{html.escape(label)}</a>')

    css = CSS.replace("@@TITLE@@", TITLE)
    doc = f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>{TITLE}</title>
<meta name="author" content="{AUTHOR}"><style>{css}</style></head><body>
<section class="cover"><div class="author">{AUTHOR}</div><div class="rule top"></div>
<h1>{TITLE}</h1><div class="sub">{SUBTITLE}</div><div class="rule bottom"></div>
<div class="tag">{TAGLINE}</div></section>
<section class="halftitle"><h1>{TITLE}</h1></section>
<section class="titlepage"><div class="a">{AUTHOR}</div><h1>{TITLE}</h1><div class="s">{SUBTITLE}</div>
<div class="o"></div><div class="t">{TAGLINE}</div></section>
<section class="colophon"><p><em>{TITLE}</em> — {SUBTITLE}.</p>
<p>Version de travail. Composé automatiquement à partir des manuscrits Markdown.</p>
<p>© {AUTHOR}. Cette œuvre est mise à disposition selon les termes de la licence Creative Commons Attribution – Pas d'utilisation commerciale – Partage dans les mêmes conditions 4.0 International (CC BY-NC-SA 4.0) : creativecommons.org/licenses/by-nc-sa/4.0/deed.fr</p></section>
<nav id="toc"><h1>Table des matières</h1>{''.join(toc)}</nav>
{''.join(body)}
</body></html>"""
    doc = typo_fr(doc)
    if want_html:
        (OUT / "livre.html").write_text(doc, encoding="utf-8")
    pdf = OUT / "le-sprint-d-apres.pdf"
    HTML(string=doc, base_url=str(ROOT)).write_pdf(pdf)
    print(f"OK -> {pdf} ({pdf.stat().st_size // 1024} Ko)")


if __name__ == "__main__":
    main()
