#!/usr/bin/env python3
"""Gmail seamless 4-5 NITIDO: soggetto PIATTO di profilo (niente prospettiva = niente profondita' di campo),
composto SENZA img2img (che ingrandiva e ammorbidiva). Solo multiply + feather sulla sfumatura chiara."""
import sys, os, urllib.request
import numpy as np
from PIL import Image
SK = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/.claude/skills/carosello-produzione/scripts"
sys.path.insert(0, SK)
import slide_kit as sk, fal_client as fc

HERE = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/03-contenuti/caroselli/2026-07-28/gmail-calendario"
A = f"{HERE}/assets"; W, H, TOT = 2160, 1350, 8
def hi(t): return f'<b style="color:#0B7A38;font-weight:600">{t}</b>'

# 1) soggetto PIATTO, ortografico, tutto sullo stesso piano -> nessun bokeh
p = ("A flat side-on elevation, orthographic, camera perfectly straight on, every object lined up on ONE single "
     "plane at exactly the same distance from the camera, tack sharp from edge to edge, absolutely no depth of "
     "field, no blur, no bokeh, everything in crisp focus. The subject, on a pure clean white background: a long "
     "horizontal continuous strip of dark obsidian black envelopes standing side by side like a frieze, joined edge "
     "to edge, and at the right end a dark obsidian calendar block whose day-slots glow emerald green hex #5CFC6E. "
     "One unbroken strip spanning the whole ultra wide frame. Crisp micro bevels, physically based rendering, even "
     "flat studio light. No text, no letters, no numbers, no logo, no watermark.")
rid, surl, rurl = fc.submit("fal-ai/flux/dev", {"prompt": p, "image_size": {"width":1920,"height":576}, "num_images":1})
fc.poll(surl, interval=6, timeout=500, log=lambda m: None)
u = (fc._req(rurl or f"{fc.QUEUE_BASE}/fal-ai/flux/dev/requests/{rid}").get("images") or [{}])[0].get("url")
urllib.request.urlretrieve(u, f"{A}/wide-flow_scene.png"); print("soggetto piatto nitido", flush=True)

# 2) compose multiply + feather (NIENTE img2img)
sk.render(sk.CSS + f'<div class="stage" style="background:{sk.GRAD_LIGHT}"></div>', f"{A}/_wgrad.png")
Image.open(f"{A}/_wgrad.png").resize((W, H)).save(f"{A}/_wgrad.png")
bg = np.array(Image.open(f"{A}/_wgrad.png").convert("RGB")).astype(float)
band = Image.open(f"{A}/wide-flow_scene.png").convert("RGB"); bh = int(W*band.size[1]/band.size[0]); band = band.resize((W, bh))
top = 540; reg = bg[top:top+bh, 0:W].copy(); b = np.array(band).astype(float); o = reg*b/255.0
fy = 0.34; ys = np.minimum(np.clip(np.arange(bh)/(bh*fy),0,1), np.clip((bh-1-np.arange(bh))/(bh*fy),0,1)); m = ys[:,None,None]
bg[top:top+bh, 0:W] = o*m + reg*(1-m)
Image.fromarray(bg.astype("uint8")).save(f"{A}/_wscene.png"); print("banda composta nitida", flush=True)

# 3) testi + taglio
texts = [
 ("Come lavora", "La posta scorre", "e si fa evento",
  f'Claude legge la mail, capisce che c\'&egrave; un appuntamento e {hi("te lo mette in agenda")} da solo.'),
 ("Senza copia-incolla", "Tu la leggi,", "lui la organizza",
  f'Niente pi&ugrave; passaggio a mano dalla posta al calendario: {hi("lo fa mentre tu fai altro")}.'),
]
sc = Image.open(f"{A}/_wscene.png").convert("RGBA")
for i, (k, l1, l2, body) in enumerate(texts):
    L = sk.slide_grad(None, k, l1, l2, body, 2+i, total=TOT, variant="light", l1_size=84, l2_size=78, l2_indent=30+i*40, layers=True)
    fg = f"{A}/_wt{i}.png"; sk.render(L["fg"], fg, transparent=True)
    sc.alpha_composite(Image.open(fg).convert("RGBA"), (i*1080, 0))
for i in (0, 1):
    sc.convert("RGB").crop((i*1080, 0, (i+1)*1080, H)).save(f"{HERE}/slide-{4+i}.png")
print("DONE")
