#!/usr/bin/env python3
"""Genera + fonde gli 8 oggetti del carosello "5 AI gratis" (metodo oggetto-fuso)."""
import sys, os, time, urllib.request
SK = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/.claude/skills/carosello-produzione/scripts"
sys.path.insert(0, SK)
import fal_client as fc
import fuse_object as fo

A = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/03-contenuti/caroselli/2026-07-30/5-ai-gratis/assets"
os.makedirs(A, exist_ok=True)
SC = "/tmp/claude-501/-Users-alfredo-Desktop-Progetti-Wulver/43804b13-b255-47f2-8d18-9a2cd642dfa1/scratchpad"
fo.virgin_grad("dark", f"{SC}/grad_dark.png"); fo.virgin_grad("light", f"{SC}/grad_light.png")
GD, GL = f"{SC}/grad_dark.png", f"{SC}/grad_light.png"

DARK = ("The object is a pale material: light pearl grey and frosted milk-white with soft chrome, glowing bright "
        "against the dark, with emerald green hex #5CFC6E glowing accents. It sits on a black glossy reflective floor "
        "that mirrors it clearly below, plus a soft contact shadow. Pure solid black background, dark studio, soft "
        "key light from upper left, deep focus, crisp micro bevels, physically based rendering, three quarter view "
        "slightly above, 100mm lens. No text, no letters, no numbers, no logo, no watermark.")
LIGHT = ("The object is polished obsidian black with a chamfered edge and emerald green hex #5CFC6E glowing accents. "
         "It sits on a white glossy reflective floor that mirrors it softly below, plus a soft grey contact shadow. "
         "Pure clean white seamless studio background, bright soft lighting, soft key from upper left, deep focus, "
         "crisp micro bevels, physically based rendering, three quarter view slightly above, 100mm lens. No text, "
         "no letters, no numbers, no logo, no watermark.")
CEN = dict(W=780, cx=540, top=360); CTA = dict(W=540, cx=720, top=720)

jobs = [
 ("s2-gift",     "dark",  "a wrapped gift box with a ribbon and bow, the lid slightly open with a soft emerald glow spilling out",
                          "a wrapped gift box with a bow glowing emerald green", CEN),
 ("s3-notebook", "light", "an open notebook with a glowing document page rising out of it and a small audio waveform beside it",
                          "an open notebook with a glowing page and a small audio waveform", CEN),
 ("s4-search",   "dark",  "a magnifying glass over a document page, with three small glowing dots connected by lines beside it like source links",
                          "a magnifying glass over a page with small glowing source-link dots", CEN),
 ("s5-infinity", "light", "a bold smooth glossy infinity symbol glowing emerald green",
                          "a bold glossy infinity symbol glowing emerald green", CEN),
 ("s6-spark",    "dark",  "a single four-pointed sparkle star, glossy and rounded, glowing emerald green, like an AI spark icon",
                          "a glossy four-pointed sparkle star glowing emerald green", CEN),
 ("s7-pen",      "light", "a fountain pen nib writing a single smooth glowing emerald green line across a sheet of paper",
                          "a fountain pen nib writing a glowing green line on paper", CEN),
 ("s8-gauge",    "dark",  "a round dashboard gauge meter with the needle pushed near the maximum, a small glowing emerald mark at the top",
                          "a round gauge meter with the needle near the maximum, glowing green mark", CEN),
 ("s9-list",     "dark",  "an open envelope with a list card sliding out, the card showing glowing emerald green lines and a small link icon",
                          "an open envelope with a glowing list card sliding out", CTA),
]
def retry(fn, n=4, wait=6):
    for i in range(n):
        try: return fn()
        except Exception as e:
            if i == n-1: raise
            print("   retry", str(e)[:50], flush=True); time.sleep(wait)
for name, var, sp, _, _ in jobs:
    out = f"{A}/{name}_scene.png"
    if os.path.exists(out): continue
    tail = DARK if var == "dark" else LIGHT
    def gen(p=f"A premium 3D product render. {sp} {tail}", o=out):
        rid, surl, rurl = fc.submit("fal-ai/flux/dev", {"prompt": p, "image_size": "square_hd", "num_images": 1})
        fc.poll(surl, interval=6, timeout=500, log=lambda m: None)
        r = rurl or f"{fc.QUEUE_BASE}/fal-ai/flux/dev/requests/{rid}"
        u = (fc._req(r).get("images") or [{}])[0].get("url"); urllib.request.urlretrieve(u, o)
    retry(gen); print("scene", name, flush=True)
for name, var, _, desc, pos in jobs:
    out = f"{A}/{name}_fused.png"
    if os.path.exists(out): continue
    grad = GD if var == "dark" else GL
    fo.fuse(grad, f"{A}/{name}_scene.png", out, var, desc, **pos)
    print("fused", name, flush=True)
print("FINE")
