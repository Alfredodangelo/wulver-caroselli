#!/usr/bin/env python3
"""Cover concettuale del confronto: un bivio stilizzato (due percorsi che divergono),
Claude arancione a sinistra, ChatGPT verde a destra. Renderizzata e incorniciata."""
import sys, os
HERE = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, HERE + "/../../../../.claude/skills/carosello-produzione/scripts")
import slide_kit as sk

W, Hc = 1080, 1350
svg = f'''
<svg width="{W}" height="{Hc}" viewBox="0 0 {W} {Hc}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="glowO" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="14" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="glowG" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="14" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <rect width="{W}" height="{Hc}" fill="#0a0e0f"/>
  <!-- nodo di partenza (la scelta) -->
  <circle cx="540" cy="1150" r="20" fill="#F5F7F5"/>
  <circle cx="540" cy="1150" r="40" fill="none" stroke="#F5F7F5" stroke-opacity="0.25" stroke-width="3"/>
  <!-- percorso Claude (sinistra, arancione) -->
  <path d="M540 1150 C 420 910, 280 730, 215 500" fill="none" stroke="#FF7A1A" stroke-width="16"
        stroke-linecap="round" filter="url(#glowO)"/>
  <circle cx="215" cy="470" r="26" fill="#FF7A1A" filter="url(#glowO)"/>
  <!-- percorso ChatGPT (destra, verde) -->
  <path d="M540 1150 C 660 910, 800 730, 865 500" fill="none" stroke="#5CFC6E" stroke-width="16"
        stroke-linecap="round" filter="url(#glowG)"/>
  <circle cx="865" cy="470" r="26" fill="#5CFC6E" filter="url(#glowG)"/>
  <!-- etichette -->
  <text x="215" y="405" text-anchor="middle" font-family="Space Grotesk" font-weight="700"
        font-size="48" fill="#FF7A1A">Claude</text>
  <text x="215" y="355" text-anchor="middle" font-family="Space Grotesk" font-weight="500"
        font-size="27" fill="#9DB6A6">Sonnet 5</text>
  <text x="865" y="405" text-anchor="middle" font-family="Space Grotesk" font-weight="700"
        font-size="48" fill="#5CFC6E">ChatGPT</text>
</svg>
'''
html = sk.CSS + f'<div style="width:{W}px;height:{Hc}px;background:#0a0e0f">{svg}</div>'
raw = f"{HERE}/assets/_cover_bivio_raw.png"
sk.render(html, raw)

# ritaglia al canvas e incornicia con l'app cornici
sys.path.insert(0, "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/05-asset/tool/cornici")
from server import rounded_frame, hex2rgb
from PIL import Image
im = Image.open(raw).convert("RGBA").crop((0, 0, W, Hc))
res = rounded_frame(im, hex2rgb("#FF7A1A"), bw=12, aura=45, radius=48, gap=0)
os.makedirs(f"{HERE}/assets/cover-options", exist_ok=True)
res.save(f"{HERE}/assets/cover-options/cover_bivio.png")
os.remove(raw)
print("cover salvata:", res.size)
