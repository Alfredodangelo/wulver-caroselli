#!/usr/bin/env python3
"""Seamless STATICO (slide 4-5) per Gmail e PDF: banda continua FUSA sulla sfumatura chiara + testi.
Niente video (scelta utente per questi due). Banda fusa con img2img -> nitida come gli oggetti singoli."""
import sys, os, urllib.request
import numpy as np
from PIL import Image
SK = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/.claude/skills/carosello-produzione/scripts"
sys.path.insert(0, SK)
import slide_kit as sk, fal_client as fc

BASE = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/03-contenuti/caroselli/2026-07-28"
W, H, TOT = 2160, 1350, 8
def hi(t): return f'<b style="color:#0B7A38;font-weight:600">{t}</b>'

def fuse_band(cardir, band_name, subj_desc, top=430, fy=0.30, strength=0.68):
    A = f"{BASE}/{cardir}/assets"
    sk.render(sk.CSS + f'<div class="stage" style="background:{sk.GRAD_LIGHT}"></div>', f"{A}/_wgrad.png")
    Image.open(f"{A}/_wgrad.png").resize((W, H)).save(f"{A}/_wgrad.png")
    bg = np.array(Image.open(f"{A}/_wgrad.png").convert("RGB")).astype(float)
    band = Image.open(f"{A}/{band_name}_scene.png").convert("RGB")
    bh = int(W * band.size[1] / band.size[0]); band = band.resize((W, bh))
    reg = bg[top:top+bh, 0:W].copy(); b = np.array(band).astype(float)
    o = reg * b / 255.0
    ys = np.minimum(np.clip(np.arange(bh)/(bh*fy), 0, 1), np.clip((bh-1-np.arange(bh))/(bh*fy), 0, 1))
    m = ys[:, None, None]
    bg[top:top+bh, 0:W] = o*m + reg*(1-m)
    init = f"{A}/_winit.png"; Image.fromarray(bg.astype("uint8")).save(init)
    # img2img: fal accetta ~<=2MP comodamente -> fondo a 1728x1080 poi riscalo a 2160x1350
    small = f"{A}/_winit_s.png"; Image.open(init).resize((1728, 1080)).save(small)
    u0 = fc.upload_file(small)
    prompt = (f"A premium wide 3D render fully fused into a soft pale mint-green gradient background: {subj_desc}. "
              "It is ONE single continuous object flowing left to right across the whole wide frame, standing on a "
              "subtly reflective light floor with soft reflection and shadow that fade into the gradient, part of the "
              "same continuous scene, seamless, no panel, no rectangle, no border. Dark obsidian and graphite "
              "materials with emerald green hex #5CFC6E glowing accents, crisp micro bevels, physically based "
              "rendering, sharp focus. No text, no letters, no numbers, no logo, no watermark.")
    r = fc.submit_and_wait("fal-ai/flux/dev/image-to-image",
        {"image_url": u0, "prompt": prompt, "strength": strength, "num_inference_steps": 40, "guidance_scale": 3.5},
        interval=6, timeout=500, log=lambda m: None)
    u = (r.get("images") or [{}])[0].get("url"); urllib.request.urlretrieve(u, f"{A}/_wfused_s.png")
    Image.open(f"{A}/_wfused_s.png").resize((W, H)).save(f"{A}/_wscene.png")
    print("banda fusa", cardir, flush=True)

def texts_and_cut(cardir, texts, l2base=30):
    A = f"{BASE}/{cardir}/assets"; HERE = f"{BASE}/{cardir}"
    sc = Image.open(f"{A}/_wscene.png").convert("RGBA")
    for i, (k, l1, l2, body) in enumerate(texts):
        L = sk.slide_grad(None, k, l1, l2, body, 2+i, total=TOT, variant="light",
                          l1_size=84, l2_size=78, l2_indent=l2base+i*40, layers=True)
        fg = f"{A}/_wt{i}.png"; sk.render(L["fg"], fg, transparent=True)
        assert os.path.getsize(fg) > 8000, f"render fallito {fg}"
        sc.alpha_composite(Image.open(fg).convert("RGBA"), (i*1080, 0))
    for i in (0, 1):
        sc.convert("RGB").crop((i*1080, 0, (i+1)*1080, H)).save(f"{HERE}/slide-{4+i}.png")
        m = f"{HERE}/slide-{4+i}.mp4"
        if os.path.exists(m): os.remove(m)
    print("statiche 4-5 ok", cardir, flush=True)

fuse_band("gmail-calendario", "wide-flow",
    "a long ribbon of pale envelopes linked edge to edge like one conveyor belt, travelling from the far left and "
    "feeding into a calendar block on the right whose day-slots glow emerald green")
texts_and_cut("gmail-calendario", [
 ("Come lavora", "La posta scorre", "e si fa evento",
  f'Claude legge la mail, capisce che c\'&egrave; un appuntamento e {hi("te lo mette in agenda")} da solo.'),
 ("Senza copia-incolla", "Tu la leggi,", "lui la organizza",
  f'Niente pi&ugrave; passaggio a mano dalla posta al calendario: {hi("lo fa mentre tu fai altro")}.'),
])

fuse_band("pdf-scansioni", "wide-merge",
    "a long unbroken river of paper sheets overlapping like dominoes, scattered and crooked on the left and "
    "progressively straightening to the right where they merge into one single bound document whose spine glows "
    "emerald green")
texts_and_cut("pdf-scansioni", [
 ("La trasformazione", "Tante scansioni", "un solo file",
  f'Le pagine storte e sparse si raddrizzano e si impilano: {hi("da cartella di foto a PDF unico")}, in ordine.'),
 ("In un colpo", "Dal mucchio", "al documento",
  f'Quello che era una pila di ricevute diventa {hi("un file solo")}, pronto da archiviare e ritrovare.'),
])
print("FINE")
