#!/usr/bin/env bash
# Produit build/le-sprint-d-apres.pdf. Prérequis (macOS) : brew install pango
set -euo pipefail
cd "$(dirname "$0")/.."
export DYLD_FALLBACK_LIBRARY_PATH="/opt/homebrew/lib:/usr/local/lib:${DYLD_FALLBACK_LIBRARY_PATH:-}"
if [ ! -d .venv ]; then
  python3 -m venv .venv
  .venv/bin/pip install -q weasyprint markdown
fi
.venv/bin/python outils/build_pdf.py "$@"
