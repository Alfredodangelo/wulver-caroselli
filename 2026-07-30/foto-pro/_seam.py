#!/usr/bin/env python3
"""Seamless ANIMATA 4-5, TUTTA generata AI (niente composizione HTML): immagine larga prima->dopo (flux-pro
ultra) -> animata INTERAMENTE da Kling come trasformazione -> tagliata in 2 -> testi sopra."""
import sys, os, urllib.request, time
sys.path.insert(0, "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/.claude/skills/carosello-produzione/scripts")
import slide_kit as sk, seam_video as sv, fal_client as fc
from PIL import Image
HERE = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/03-contenuti/caroselli/2026-07-30/foto-pro"
A = f"{HERE}/assets"; W, H, TOT = 2160, 1350, 8; GD = "#0B7A38"

def retry(fn, n=4, wait=6):
    for i in range(n):
        try: return fn()
        except Exception as e:
            if i == n-1: raise
            print("  retry", str(e)[:50], flush=True); time.sleep(wait)

# --- 1) IMMAGINE LARGA prima->dopo, generata AI (una scena, stessa donna) ---
prompt = ("A cinematic wide before and after portrait of the same woman in her early thirties with wavy brown hair, "
          "one single continuous image: on the LEFT she is an ordinary casual amateur phone selfie in a plain grey "
          "t-shirt in a slightly messy home, flat dull lighting; on the RIGHT the exact same woman is a polished "
          "professional studio headshot in a dark tailored blazer, soft studio key light, clean softly blurred "
          "neutral background; in the CENTER a soft vertical band of glowing emerald green light and floating sparkles "
          "connects the two halves like a magical transformation. Photorealistic, the same face and identity on both "
          "sides, seamless single wide composition, high detail, sharp. No text, no watermark.")
raw = f"{A}/_wide_ba.png"
def genimg():
    r = fc.submit_and_wait("fal-ai/flux-pro/v1.1-ultra", {"prompt": prompt, "aspect_ratio": "16:9", "num_images": 1},
                           interval=6, timeout=400, log=lambda m: None)
    u = (r.get("images") or [{}])[0].get("url"); urllib.request.urlretrieve(u, raw)
retry(genimg)
im = Image.open(raw).convert("RGB")  # 16:9 -> crop centrale a 1.6 (2160x1350)
iw, ih = im.size; tr = W/H
if iw/ih > tr: nw = int(ih*tr); im = im.crop(((iw-nw)//2, 0, (iw-nw)//2+nw, ih))
else: nh = int(iw/tr); im = im.crop((0, (ih-nh)//2, iw, (ih-nh)//2+nh))
im.resize((W, H)).save(f"{A}/_wide_ba_fit.png"); print("immagine larga ok", flush=True)

# --- 2) KLING anima TUTTA la trasformazione ---
url = retry(lambda: fc.upload_file(f"{A}/_wide_ba_fit.png"))
r = fc.submit_and_wait("fal-ai/kling-video/v2.5-turbo/pro/image-to-video",
    {"prompt": "the central glowing green light band and sparkles gently sweep and pulse, the casual left side slowly "
     "refines and brightens toward the polished professional right side, a smooth elegant transformation reveal, the "
     "woman's face and identity stay consistent and natural, soft cinematic motion, stable camera, no warping, no "
     "distortion of the face", "image_url": url, "duration": "5"},
    interval=10, timeout=900, log=lambda s: print(" ", s, flush=True))
v = (r.get("video") or {}).get("url"); urllib.request.urlretrieve(v, f"{A}/_kling.mp4")
print("video:", sv.probe(f"{A}/_kling.mp4"), flush=True)

# --- 3) TESTI trasparenti (variante chiara) per pannello ---
def hi(t): return f'<b style="color:{GD};font-weight:600">{t}</b>'
texts = [("La trasformazione", "Da questa", "foto", f'Un selfie qualsiasi, come quello che hai nel rullino. {hi("Il tuo prima")}.'),
         ("In due minuti", "esce", "questa", f'Stesso viso, tutt\'altra foto: {hi("il tuo dopo")}, pronto per il profilo.')]
wtext = Image.new("RGBA", (W, H), (0, 0, 0, 0))
for i, (k, l1, l2, body) in enumerate(texts):
    L = sk.slide_grad(None, k, l1, l2, body, 2+i, total=TOT, variant="light", l1_size=76, l2_size=80, l2_indent=20+i*30, layers=True)
    sk.render(L["fg"], f"{A}/_wt{i}.png", transparent=True)
    wtext.alpha_composite(Image.open(f"{A}/_wt{i}.png").convert("RGBA"), (i*1080, 0))
wtext.save(f"{A}/_wtext.png")

# --- 4) taglio in 2 pannelli + testi ---
outs = [f"{HERE}/slide-4.mp4", f"{HERE}/slide-5.mp4"]
sv.cut_panels(f"{A}/_kling.mp4", f"{A}/_wtext.png", outs, canvas=(W, H))
for n in (4, 5): sv.poster(f"{HERE}/slide-{n}.mp4", f"{HERE}/slide-{n}.png", t=2.5)
print("DONE")
