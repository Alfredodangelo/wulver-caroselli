#!/usr/bin/env python3
"""Coppia SEAMLESS animata (slide 4-5) del carosello Gmail — soggetto UNICO che attraversa 2 slide.
Metodo: banda larga (nastro di buste -> calendario) fusa sulla sfumatura CHIARA -> Kling anima tutta la
tela 2160x1350 in un solo video -> testi trasparenti sopra -> taglio in 2 pannelli. Video = max 2 slide."""
import sys, os, urllib.request
import numpy as np
from PIL import Image
SK = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/.claude/skills/carosello-produzione/scripts"
sys.path.insert(0, SK)
import slide_kit as sk, seam_video as sv, fal_client as fc

HERE = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/03-contenuti/caroselli/2026-07-28/gmail-calendario"
A = f"{HERE}/assets"; W, H = 2160, 1350; TOT = 8; G, GD = "#5CFC6E", "#0B7A38"

def hi(t): return f'<b style="color:{GD};font-weight:600">{t}</b>'

# --- 1) TELA LARGA fusa (sfumatura chiara 2160x1350 + banda dark-on-white in multiply, feather) ---
sk.render(sk.CSS + f'<div class="stage" style="background:{sk.GRAD_LIGHT}"></div>', f"{A}/_wgrad.png")
Image.open(f"{A}/_wgrad.png").resize((W, H)).save(f"{A}/_wgrad.png")
bg = Image.open(f"{A}/_wgrad.png").convert("RGB")
band = Image.open(f"{A}/wide-flow_scene.png").convert("RGB")
bw = W; bh = int(bw * band.size[1] / band.size[0]); band = band.resize((bw, bh))
top = 470
a = np.array(bg).astype(float)
reg = a[top:top+bh, 0:bw].copy(); b = np.array(band).astype(float)
o = reg * b / 255.0  # multiply: il bianco della scena sparisce, l'oggetto scuro resta
fy = 0.28; ys = np.minimum(np.clip(np.arange(bh)/(bh*fy), 0, 1), np.clip((bh-1-np.arange(bh))/(bh*fy), 0, 1))
m = ys[:, None, None]
a[top:top+bh, 0:bw] = o*m + reg*(1-m)
Image.fromarray(a.astype("uint8")).save(f"{A}/_wscene.png")

# --- 2) TESTI trasparenti 2160x1350 (pannello 0 = slide4, pannello 1 = slide5), variante light ---
texts = [
 ("Come lavora", "La posta scorre", "e si fa evento",
  f'Claude legge la mail, capisce che c\'&egrave; un appuntamento e {hi("te lo mette in agenda")} da solo.'),
 ("Senza copia-incolla", "Tu la leggi,", "lui la organizza",
  f'Niente pi&ugrave; passaggio a mano dalla posta al calendario: {hi("lo fa mentre tu fai altro")}.'),
]
wtext = Image.new("RGBA", (W, H), (0, 0, 0, 0))
for i, (k, l1, l2, body) in enumerate(texts):
    L = sk.slide_grad(None, k, l1, l2, body, 2+i, total=TOT, variant="light",
                      l1_size=84, l2_size=78, l2_indent=30+i*40, layers=True)
    sk.render(L["fg"], f"{A}/_wt{i}.png", transparent=True)
    wtext.alpha_composite(Image.open(f"{A}/_wt{i}.png").convert("RGBA"), (i*1080, 0))
wtext.save(f"{A}/_wtext.png")

# --- 3) KLING anima tutta la tela in UN video ---
url = fc.upload_file(f"{A}/_wscene.png")
prompt = ("the long ribbon of linked envelopes gently flows from left to right along its path toward the calendar "
          "on the right, a slow continuous conveyor motion, the calendar day slots softly light up one after another "
          "in emerald green, the overall layout stays the same, very slow steady elegant cinematic motion, "
          "no camera shake, no warping, everything stable and clean")
r = fc.submit_and_wait("fal-ai/kling-video/v2.5-turbo/pro/image-to-video",
                       {"prompt": prompt, "image_url": url, "duration": "5"},
                       interval=10, timeout=900, log=lambda s: print(" ", s, flush=True))
v = (r.get("video") or {}).get("url"); urllib.request.urlretrieve(v, f"{A}/_wkling.mp4")
print("video:", sv.probe(f"{A}/_wkling.mp4"), flush=True)

# --- 4) testi sopra + taglio in 2 pannelli ---
outs = [f"{HERE}/slide-4.mp4", f"{HERE}/slide-5.mp4"]
sv.cut_panels(f"{A}/_wkling.mp4", f"{A}/_wtext.png", outs, canvas=(W, H))
for n in (4, 5): sv.poster(f"{HERE}/slide-{n}.mp4", f"{HERE}/slide-{n}.png", t=2.0)
print("DONE")
