#!/usr/bin/env python3
"""Genera oggetti fusi + le 2 foto (casual/pro) del carosello "Trasforma un selfie in foto professionale"."""
import sys, os, time, urllib.request
SK = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/.claude/skills/carosello-produzione/scripts"
sys.path.insert(0, SK)
import fal_client as fc
import fuse_object as fo

A = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/03-contenuti/caroselli/2026-07-30/foto-pro/assets"
os.makedirs(A, exist_ok=True)
SC = "/tmp/claude-501/-Users-alfredo-Desktop-Progetti-Wulver/43804b13-b255-47f2-8d18-9a2cd642dfa1/scratchpad"
fo.virgin_grad("dark", f"{SC}/grad_dark.png"); fo.virgin_grad("light", f"{SC}/grad_light.png")
GD, GL = f"{SC}/grad_dark.png", f"{SC}/grad_light.png"

DARK = ("The object is a pale material: light pearl grey and frosted milk-white with soft chrome, glowing bright "
        "against the dark, with emerald green hex #5CFC6E glowing accents. It sits on a black glossy reflective floor "
        "that mirrors it clearly below, plus a soft contact shadow. Pure solid black background, dark studio, soft key "
        "light from upper left, deep focus, crisp micro bevels, physically based rendering, three quarter view "
        "slightly above, 100mm lens. No text, no letters, no numbers, no logo, no watermark.")
LIGHT = ("The object is polished obsidian black with a chamfered edge and emerald green hex #5CFC6E glowing accents. "
         "It sits on a white glossy reflective floor that mirrors it softly below, plus a soft grey contact shadow. "
         "Pure clean white seamless studio background, bright soft lighting, soft key from upper left, deep focus, "
         "crisp micro bevels, physically based rendering, three quarter view slightly above, 100mm lens. No text, "
         "no letters, no numbers, no logo, no watermark.")
CEN = dict(W=780, cx=540, top=360); CTA = dict(W=540, cx=720, top=720)

objs = [
 ("s2-phone",  "dark",  "a modern smartphone standing upright, its screen glowing softly emerald green, clean bold geometry",
                        "a modern smartphone with a softly glowing green screen", CEN),
 ("s3-upload", "light", "a rounded photo picture frame with a bold upward arrow floating above it, an upload symbol",
                        "a photo frame with an upward upload arrow above it", CEN),
 ("s6-wand",   "dark",  "a rounded chat speech bubble with a small magic wand and a sparkle beside it",
                        "a chat speech bubble with a small magic wand and a sparkle", CEN),
 ("s7-idcard", "light", "an ID badge card with a small rounded warning triangle floating in front of it",
                        "an ID badge card with a small warning triangle in front", CEN),
 ("s8-frames", "dark",  "three overlapping rounded portrait photo frames fanned out in a small stack",
                        "three overlapping rounded portrait photo frames fanned out", CEN),
 ("s9-camera", "dark",  "a framed portrait photo standing on a small stand, the frame glowing emerald green",
                        "a framed portrait photo on a stand, frame glowing green", CTA),
]
def retry(fn, n=4, wait=6):
    for i in range(n):
        try: return fn()
        except Exception as e:
            if i == n-1: raise
            print("   retry", str(e)[:50], flush=True); time.sleep(wait)
# scene + fuse per gli oggetti
for name, var, sp, _, _ in objs:
    out = f"{A}/{name}_scene.png"
    if os.path.exists(out): continue
    tail = DARK if var == "dark" else LIGHT
    def gen(p=f"A premium 3D product render. {sp} {tail}", o=out):
        rid, surl, rurl = fc.submit("fal-ai/flux/dev", {"prompt": p, "image_size": "square_hd", "num_images": 1})
        fc.poll(surl, interval=6, timeout=500, log=lambda m: None)
        r = rurl or f"{fc.QUEUE_BASE}/fal-ai/flux/dev/requests/{rid}"
        u = (fc._req(r).get("images") or [{}])[0].get("url"); urllib.request.urlretrieve(u, o)
    retry(gen); print("scene", name, flush=True)
for name, var, _, desc, pos in objs:
    out = f"{A}/{name}_fused.png"
    if os.path.exists(out): continue
    grad = GD if var == "dark" else GL
    fo.fuse(grad, f"{A}/{name}_scene.png", out, var, desc, **pos)
    print("fused", name, flush=True)

# le 2 FOTO (persona coerente) con flux-pro ultra
PERSON = "a woman in her early thirties, shoulder length wavy brown hair, warm friendly face, light natural makeup"
photos = {
 "photo-casual": (f"An ordinary casual phone mirror selfie of {PERSON}, hair slightly messy, plain grey t-shirt, "
                  "cluttered home bedroom in the background, flat harsh phone-camera flash lighting, mediocre amateur "
                  "snapshot, realistic. No text, no watermark."),
 "photo-pro":    (f"A polished professional corporate LinkedIn headshot of {PERSON}, neat hair, dark tailored blazer "
                  "over a light blouse, confident natural micro-smile, soft studio key light plus subtle rim light, "
                  "clean neutral softly blurred office gradient background, shot on 85mm f2.2, sharp, magazine quality "
                  "colour photograph. No text, no watermark."),
}
for k, p in photos.items():
    out = f"{A}/{k}.png"
    if os.path.exists(out): continue
    def go(p=p, o=out):
        r = fc.submit_and_wait("fal-ai/flux-pro/v1.1-ultra", {"prompt": p, "aspect_ratio": "3:4", "num_images": 1}, interval=6, timeout=400, log=lambda m: None)
        u = (r.get("images") or [{}])[0].get("url"); urllib.request.urlretrieve(u, o)
    retry(go); print("photo", k, flush=True)
print("FINE")
