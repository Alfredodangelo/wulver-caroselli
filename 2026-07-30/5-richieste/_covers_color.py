#!/usr/bin/env python3
"""Cover A COLORI per "5 richieste": mazzo di carte colorate + sveglia colorata. Scontorno + aura arancione."""
import sys, os, urllib.request, time
sys.path.insert(0, "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/.claude/skills/carosello-produzione/scripts")
import fal_client as fc, slide_kit as sk
from PIL import Image, ImageFilter
CO = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/03-contenuti/caroselli/2026-07-30/5-richieste/assets/cover-options"
SC = "/tmp/claude-501/-Users-alfredo-Desktop-Progetti-Wulver/43804b13-b255-47f2-8d18-9a2cd642dfa1/scratchpad"
ORANGE = (255, 122, 26); AURA = (255, 140, 45)
TAIL = ("glossy colorful premium photorealistic 3D product icon, vivid saturated colors, soft studio key light from "
        "upper left, soft contact shadow, three quarter view slightly above, 100mm lens, crisp micro bevels, on a "
        "plain seamless neutral light grey studio background. No text, no letters, no numbers, no logo, no watermark.")
jobs = {
 "cov-cards-color": f"A neat deck of rounded cards fanned out in a smooth arc, each card a different vivid glossy colour: mint green, warm orange, teal, coral pink and soft yellow, the top card lifted, {TAIL}",
 "cov-clock-color": f"A playful modern round desk clock, mint green glossy body with warm orange hands and rim and a small orange bell on top, cheerful and colourful, {TAIL}",
}
def retry(fn, n=4, wait=6):
    for i in range(n):
        try: return fn()
        except Exception as e:
            if i == n-1: raise
            time.sleep(wait)
def rembg(p):
    u = retry(lambda: fc.upload_file(p))
    try: r = fc.submit_and_wait("fal-ai/imageutils/rembg", {"image_url": u}, interval=5, timeout=200, log=lambda m: None)
    except Exception: r = fc.submit_and_wait("fal-ai/birefnet/v2", {"image_url": u}, interval=5, timeout=200, log=lambda m: None)
    url = (r.get("image") or {}).get("url") or (r.get("images") or [{}])[0].get("url")
    o = p.replace(".png", "_cut.png"); urllib.request.urlretrieve(url, o); return o
def aura(cut, out, pad=110, stroke=9, blur=46):
    im = Image.open(cut).convert("RGBA"); bb = im.split()[3].getbbox()
    if bb: im = im.crop(bb)
    W, H = im.size; cv = Image.new("RGBA", (W+2*pad, H+2*pad), (0,0,0,0)); cv.alpha_composite(im, (pad, pad))
    a = cv.split()[3]; dil = a.filter(ImageFilter.MaxFilter(stroke*2+1))
    ct = Image.new("RGBA", cv.size, (0,0,0,0)); ct.paste(Image.new("RGBA", cv.size, ORANGE+(255,)), (0,0), dil)
    au = Image.new("RGBA", cv.size, (0,0,0,0)); au.paste(Image.new("RGBA", cv.size, AURA+(255,)), (0,0), dil.filter(ImageFilter.GaussianBlur(blur)))
    res = Image.new("RGBA", cv.size, (0,0,0,0))
    for L in (au, au, ct, cv): res = Image.alpha_composite(res, L)
    res.save(out); return out
subs = {k: retry(lambda p=p: fc.submit("fal-ai/flux/dev", {"prompt": p, "image_size": "portrait_4_3", "num_images": 1})) for k, p in jobs.items()}
grid = Image.open(sk.GRID_CLEAN).convert("RGBA").resize((1080, 1350)); tiles = []
for k, (rid, surl, rurl) in subs.items():
    fc.poll(surl, interval=6, timeout=400, log=lambda m: None)
    r = rurl or f"{fc.QUEUE_BASE}/fal-ai/flux/dev/requests/{rid}"
    u = (fc._req(r).get("images") or [{}])[0].get("url"); raw = f"{CO}/{k}.png"; urllib.request.urlretrieve(u, raw)
    fin = aura(rembg(raw), f"{CO}/{k}_aura.png"); print("cover", k, flush=True)
    fg = Image.open(fin).convert("RGBA"); t = grid.copy(); f = fg.copy(); f.thumbnail((760, 980))
    t.alpha_composite(f, ((1080-f.size[0])//2, (1350-f.size[1])//2)); tiles.append(t.convert("RGB"))
cw = 460; sheet = Image.new("RGB", (cw*2, 590), (8, 10, 10))
for i, t in enumerate(tiles): t.thumbnail((cw-8, 590-8)); sheet.paste(t, (i*cw+4, 4))
sheet.save(f"{SC}/cover5_color.png"); print("SHEET OK")
