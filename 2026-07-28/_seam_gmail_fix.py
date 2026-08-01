#!/usr/bin/env python3
"""Rifa' il seamless 4-5 di Gmail NITIDO: rigenera il soggetto lardo senza sfocatura, lo fonde, taglia."""
import sys, os, urllib.request
import numpy as np
from PIL import Image
SK = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/.claude/skills/carosello-produzione/scripts"
sys.path.insert(0, SK)
import slide_kit as sk, fal_client as fc

HERE = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/03-contenuti/caroselli/2026-07-28/gmail-calendario"
A = f"{HERE}/assets"; W, H, TOT = 2160, 1350, 8
def hi(t): return f'<b style="color:#0B7A38;font-weight:600">{t}</b>'

# 1) rigenera il soggetto NITIDO (dark-on-white, deep focus)
p = ("A premium wide 3D product render on a pure clean white studio background, one single continuous subject "
     "spanning the whole ultra wide frame from left to right: a long ribbon of dark obsidian black envelopes joined "
     "edge to edge like one unbroken conveyor belt, each envelope crisp and clearly an envelope, travelling from the "
     "far left and feeding on the right into a large obsidian calendar block whose day-slots glow emerald green hex "
     "#5CFC6E one after another. It is ONE unbroken chain, not separate items. Sharp deep focus, everything in "
     "perfect focus, no depth of field blur, no bokeh, crisp micro bevels, physically based rendering, soft even "
     "studio light. No text, no letters, no numbers, no logo, no watermark.")
rid, surl, rurl = fc.submit("fal-ai/flux/dev", {"prompt": p, "image_size": {"width":1920,"height":640}, "num_images":1})
fc.poll(surl, interval=6, timeout=500, log=lambda m: None)
u = (fc._req(rurl or f"{fc.QUEUE_BASE}/fal-ai/flux/dev/requests/{rid}").get("images") or [{}])[0].get("url")
urllib.request.urlretrieve(u, f"{A}/wide-flow_scene.png"); print("soggetto nitido rigenerato", flush=True)

# 2) fondi sulla sfumatura chiara (multiply + feather verticale), poi img2img nitido
sk.render(sk.CSS + f'<div class="stage" style="background:{sk.GRAD_LIGHT}"></div>', f"{A}/_wgrad.png")
Image.open(f"{A}/_wgrad.png").resize((W, H)).save(f"{A}/_wgrad.png")
bg = np.array(Image.open(f"{A}/_wgrad.png").convert("RGB")).astype(float)
band = Image.open(f"{A}/wide-flow_scene.png").convert("RGB"); bh = int(W*band.size[1]/band.size[0]); band = band.resize((W, bh))
top = 430; reg = bg[top:top+bh, 0:W].copy(); b = np.array(band).astype(float); o = reg*b/255.0
fy = 0.30; ys = np.minimum(np.clip(np.arange(bh)/(bh*fy),0,1), np.clip((bh-1-np.arange(bh))/(bh*fy),0,1)); m = ys[:,None,None]
bg[top:top+bh, 0:W] = o*m + reg*(1-m)
Image.fromarray(bg.astype("uint8")).resize((1728,1080)).save(f"{A}/_winit_s.png")
u0 = fc.upload_file(f"{A}/_winit_s.png")
prompt = ("A premium wide 3D render fully fused into a soft pale mint-green gradient background: one single continuous "
          "chain of dark obsidian envelopes flowing left to right into a calendar block on the right with emerald "
          "green hex #5CFC6E glowing slots, standing on a subtly reflective light floor with soft reflection, "
          "seamless, no panel, no rectangle, no border. Sharp deep focus, everything in focus, no depth of field "
          "blur, crisp micro bevels, physically based rendering. No text, no letters, no numbers, no logo.")
r = fc.submit_and_wait("fal-ai/flux/dev/image-to-image",
    {"image_url": u0, "prompt": prompt, "strength": 0.78, "num_inference_steps": 42, "guidance_scale": 3.5},
    interval=6, timeout=500, log=lambda m: None)
uu = (r.get("images") or [{}])[0].get("url"); urllib.request.urlretrieve(uu, f"{A}/_wfused_s.png")
Image.open(f"{A}/_wfused_s.png").resize((W, H)).save(f"{A}/_wscene.png"); print("banda fusa nitida", flush=True)

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
