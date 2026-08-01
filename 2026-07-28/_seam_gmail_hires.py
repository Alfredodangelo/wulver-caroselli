#!/usr/bin/env python3
"""Gmail seamless 4-5 NITIDO davvero: genero l'intera scena a risoluzione NATIVA alta (1472x920, ~1.35MP,
formato 1.6 = 2 slide) invece che larga-e-bassa; poi ingrandisco con LANCZOS (o esrgan se serve) a 2160x1350.
Fondo verde-menta gia' nell'immagine, soggetto continuo. Poi testi + taglio in 2."""
import sys, os, urllib.request
import numpy as np
from PIL import Image
SK = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/.claude/skills/carosello-produzione/scripts"
sys.path.insert(0, SK)
import slide_kit as sk, fal_client as fc

HERE = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/03-contenuti/caroselli/2026-07-28/gmail-calendario"
A = f"{HERE}/assets"; W, H, TOT = 2160, 1350, 8
def hi(t): return f'<b style="color:#0B7A38;font-weight:600">{t}</b>'
def sharp(path):
    a = np.array(Image.open(path).convert("L")).astype(float)
    lap = np.abs(np.diff(a, axis=0)[:, :-1]) + np.abs(np.diff(a, axis=1)[:-1, :])
    return round(lap.var(), 1)

# 1) scena intera a risoluzione nativa alta, fondo menta + soggetto continuo, TACK SHARP
p = ("A wide premium 3D render on a soft pale mint-green radial gradient background (white-mint centre fading to "
     "light green edges): one single continuous subject spanning the whole frame left to right, a horizontal strip "
     "of dark obsidian black envelopes standing side by side and joined edge to edge like one unbroken conveyor, "
     "flowing from the left into a dark obsidian calendar block on the right whose day-slots glow emerald green hex "
     "#5CFC6E. The strip sits in the lower-middle on a subtly reflective light floor with a soft reflection and "
     "shadow fading into the gradient, empty gradient space above. Flat near side-on view, everything on one plane, "
     "tack sharp edge to edge, deep focus, absolutely no depth of field, no bokeh, crisp micro bevels, physically "
     "based rendering. No text, no letters, no numbers, no logo, no watermark.")
rid, surl, rurl = fc.submit("fal-ai/flux/dev", {"prompt": p, "image_size": {"width": 1472, "height": 920}, "num_images": 1})
fc.poll(surl, interval=6, timeout=500, log=lambda m: None)
u = (fc._req(rurl or f"{fc.QUEUE_BASE}/fal-ai/flux/dev/requests/{rid}").get("images") or [{}])[0].get("url")
urllib.request.urlretrieve(u, f"{A}/_whires.png")
print("nativa 1472x920 nitidezza:", sharp(f"{A}/_whires.png"), flush=True)

# 2) prova esrgan (2x) per ingrandire mantenendo la nitidezza; fallback LANCZOS
scene = None
try:
    uu = fc.upload_file(f"{A}/_whires.png")
    r = fc.submit_and_wait("fal-ai/esrgan", {"image_url": uu, "scale": 2}, interval=5, timeout=300, log=lambda m: None)
    us = (r.get("image") or {}).get("url") or (r.get("images") or [{}])[0].get("url")
    urllib.request.urlretrieve(us, f"{A}/_whires2x.png")
    scene = Image.open(f"{A}/_whires2x.png").convert("RGB").resize((W, H), Image.LANCZOS)
    print("esrgan ok", flush=True)
except Exception as e:
    print("esrgan non disponibile, uso LANCZOS:", str(e)[:60], flush=True)
    scene = Image.open(f"{A}/_whires.png").convert("RGB").resize((W, H), Image.LANCZOS)
scene.save(f"{A}/_wscene.png")
print("scene finale nitidezza:", sharp(f"{A}/_wscene.png"), flush=True)

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
