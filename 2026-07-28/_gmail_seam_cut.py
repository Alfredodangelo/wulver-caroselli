#!/usr/bin/env python3
"""Ricompone le slide 4-5 di Gmail: seamless nitida (clarity-upscaled) + testi, taglio in 2. Path assoluti."""
import sys, os
sys.path.insert(0, "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/.claude/skills/carosello-produzione/scripts")
import slide_kit as sk
from PIL import Image, ImageDraw
HERE = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/03-contenuti/caroselli/2026-07-28/gmail-calendario"
A = f"{HERE}/assets"; W, H, TOT = 2160, 1350, 8
O = "/tmp/claude-501/-Users-alfredo-Desktop-Progetti-Wulver/43804b13-b255-47f2-8d18-9a2cd642dfa1/scratchpad"
def hi(t): return f'<b style="color:#0B7A38;font-weight:600">{t}</b>'
texts = [("Come lavora", "La posta scorre", "e si fa evento",
          f'Claude legge la mail, capisce che c\'&egrave; un appuntamento e {hi("te lo mette in agenda")} da solo.'),
         ("Senza copia-incolla", "Tu la leggi,", "lui la organizza",
          f'Niente pi&ugrave; passaggio a mano dalla posta al calendario: {hi("lo fa mentre tu fai altro")}.')]
sc = Image.open(f"{A}/_wscene_up.png").convert("RGBA")
for i, (k, l1, l2, body) in enumerate(texts):
    L = sk.slide_grad(None, k, l1, l2, body, 2+i, total=TOT, variant="light", l1_size=84, l2_size=78, l2_indent=30+i*40, layers=True)
    fg = f"{A}/_wt{i}.png"; sk.render(L["fg"], fg, transparent=True)
    assert os.path.getsize(fg) > 8000, f"render fallito {fg}"
    sc.alpha_composite(Image.open(fg).convert("RGBA"), (i*1080, 0))
for i in (0, 1):
    sc.convert("RGB").crop((i*1080, 0, (i+1)*1080, H)).save(f"{HERE}/slide-{4+i}.png")
g = Image.new("RGB", (2160, 1350), (255, 255, 255))
for i in (0, 1): g.paste(Image.open(f"{HERE}/slide-{4+i}.png").convert("RGB"), (i*1080, 0))
ImageDraw.Draw(g).line([(1080, 0), (1080, 1350)], fill=(255, 120, 26), width=3); g.thumbnail((1500, 950)); g.save(f"{O}/gmail_seam_FINAL.png")
print("DONE nitide e unite")
