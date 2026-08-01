#!/usr/bin/env python3
"""Gmail seamless 4-5 NITIDO e UNITO: FLUX non rende nitida la banda larga, ma rende nitidi gli oggetti
singoli. Quindi genero UNA busta nitida e la compongo IN FILA (conveyor) lungo le 2 slide fino al
calendario: continua attraverso il taglio, e nitida perche' ogni pezzo e' un oggetto singolo."""
import sys, os, urllib.request
import numpy as np
from PIL import Image
SK = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/.claude/skills/carosello-produzione/scripts"
sys.path.insert(0, SK)
import slide_kit as sk, fal_client as fc

HERE = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/03-contenuti/caroselli/2026-07-28/gmail-calendario"
A = f"{HERE}/assets"; W, H, TOT = 2160, 1350, 8
def hi(t): return f'<b style="color:#0B7A38;font-weight:600">{t}</b>'
def sharp(im):
    a = np.array(im.convert("L")).astype(float)
    return round((np.abs(np.diff(a,axis=0)[:,:-1])+np.abs(np.diff(a,axis=1)[:-1,:])).var(), 1)

# 1) UNA busta nitida (obsidiana su bianco, pavimento riflettente) + calendario (riuso g5-calfull_scene)
if not os.path.exists(f"{A}/env_scene.png"):
    p = ("A single dark obsidian black closed envelope, glossy, seen three-quarter from slightly above, a thin "
         "emerald green hex #5CFC6E glow along its top flap edge, standing on a white glossy reflective floor with a "
         "soft reflection and grey contact shadow, pure clean white background, tack sharp, deep focus, crisp micro "
         "bevels, physically based rendering, 100mm lens. No text, no letters, no numbers, no logo, no watermark.")
    rid, surl, rurl = fc.submit("fal-ai/flux/dev", {"prompt": p, "image_size": "square_hd", "num_images": 1})
    fc.poll(surl, interval=6, timeout=500, log=lambda m: None)
    u = (fc._req(rurl or f"{fc.QUEUE_BASE}/fal-ai/flux/dev/requests/{rid}").get("images") or [{}])[0].get("url")
    urllib.request.urlretrieve(u, f"{A}/env_scene.png")
print("busta nitidezza:", sharp(Image.open(f"{A}/env_scene.png")), flush=True)

# 2) sfumatura menta + composizione IN FILA (multiply + feather per ogni pezzo)
sk.render(sk.CSS + f'<div class="stage" style="background:{sk.GRAD_LIGHT}"></div>', f"{A}/_wgrad.png")
bg = np.array(Image.open(f"{A}/_wgrad.png").resize((W, H)).convert("RGB")).astype(float)
def place(scene_path, cx, cyt, tw, fx=0.22, fy=0.20):
    s = Image.open(scene_path).convert("RGB")
    bbw = int(tw); bbh = int(tw * s.size[1] / s.size[0]); s = s.resize((bbw, bbh))
    x0 = int(cx - bbw/2); y0 = int(cyt)
    x1, y1 = max(0, x0), max(0, y0); x2, y2 = min(W, x0+bbw), min(H, y0+bbh)
    if x2 <= x1 or y2 <= y1: return
    sb = np.array(s).astype(float)[y1-y0:y2-y0, x1-x0:x2-x0]
    reg = bg[y1:y2, x1:x2]; o = reg * sb / 255.0
    ww, hh = x2-x1, y2-y1
    xs = np.minimum(np.clip(np.arange(ww)/(bbw*fx), 0, 1), np.clip((bbw-1-(np.arange(ww)+(x1-x0)))/(bbw*fx), 0, 1))
    ys = np.minimum(np.clip((np.arange(hh)+(y1-y0))/(bbh*fy), 0, 1), np.clip((bbh-1-(np.arange(hh)+(y1-y0)))/(bbh*fy), 0, 1))
    m = np.clip(np.outer(ys, xs), 0, 1)[:, :, None]
    bg[y1:y2, x1:x2] = o*m + reg*(1-m)
# fila di buste da sinistra, attraversa il taglio (x=1080), poi il calendario a destra
for k, cx in enumerate(range(150, 1550, 205)):
    place(f"{A}/env_scene.png", cx, 640 + (k % 2) * 18, 520)
place(f"{A}/g5-calfull_scene.png", 1880, 560, 620)
scene = Image.fromarray(bg.astype("uint8"))
scene.save(f"{A}/_wscene.png"); print("fila composta nitidezza:", sharp(scene), flush=True)

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
