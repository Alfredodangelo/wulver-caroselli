#!/usr/bin/env python3
"""Impagina la copertina (slide-1) di Gmail e PDF: griglia scura + oggetto (aura arancione) in alto +
titolo corto in basso (label bianca + riga grande verde). Path assoluti."""
import sys, os
sys.path.insert(0, "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/.claude/skills/carosello-produzione/scripts")
import slide_kit as sk
from PIL import Image
B = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/03-contenuti/caroselli/2026-07-28"
G, Wt = "#5CFC6E", "#F5F7F5"

def cover(car, aura_png, label, big, out):
    grid_b64 = sk.b64(sk.GRID_CLEAN)
    # oggetto ridimensionato e messo in alto-centro
    im = Image.open(aura_png).convert("RGBA"); bb = im.split()[3].getbbox()
    if bb: im = im.crop(bb)
    im.thumbnail((760, 720)); tmp = aura_png.replace(".png", "_fit.png"); im.save(tmp)
    ob = sk.b64(tmp); ow = im.size[0]
    html = (sk.CSS + '<div class="stage">'
        f'<img src="data:image/png;base64,{grid_b64}" style="position:absolute;inset:0;width:1080px;height:1350px;object-fit:cover;z-index:0">'
        f'<img src="data:image/png;base64,{ob}" style="position:absolute;left:50%;top:250px;transform:translateX(-50%);width:{ow}px;z-index:2">'
        f'<div style="position:absolute;left:70px;right:70px;bottom:150px;z-index:3;text-align:center">'
        f'<div style="font-family:\'Space Grotesk\';font-weight:600;font-size:34px;letter-spacing:.14em;text-transform:uppercase;color:{Wt};margin-bottom:10px">{label}</div>'
        f'<div style="font-family:\'Space Grotesk\';font-weight:700;font-size:96px;line-height:.98;letter-spacing:-.02em;text-transform:uppercase;color:{G};text-shadow:0 0 28px rgba(92,252,110,.5)">{big}</div>'
        f'</div>'
        f'<div style="position:absolute;top:70px;left:0;right:0;text-align:center;z-index:3;font-family:\'Space Grotesk\';font-size:22px;letter-spacing:.22em;text-transform:uppercase;color:#9DB6A6">Wulver</div>'
        '</div>')
    sk.render(html, out); print("cover", car, flush=True)

cover("gmail", f"{B}/gmail-calendario/assets/cover-options/cov-mailcal2_aura.png",
      "Gmail + Calendario", "Dentro Claude", f"{B}/gmail-calendario/slide-1.png")
cover("pdf", f"{B}/pdf-scansioni/assets/cover-options/cov-mergepdf_aura.png",
      "Cinque scansioni", "Un PDF solo", f"{B}/pdf-scansioni/slide-1.png")
print("DONE")
