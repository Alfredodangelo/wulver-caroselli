#!/usr/bin/env python3
"""Genera + fonde gli 8 oggetti del carosello "5 richieste": scena su fondo che fa contrasto -> fuse()."""
import sys, os, time, urllib.request
SK = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/.claude/skills/carosello-produzione/scripts"
sys.path.insert(0, SK)
import fal_client as fc
import fuse_object as fo

A = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/03-contenuti/caroselli/2026-07-30/5-richieste/assets"
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

# (nome, variante, prompt-scena, descrizione-per-fuse, posizione)
jobs = [
 ("s2-hourglass", "dark",  "a sleek modern hourglass with glowing emerald green sand falling through it",
                            "a sleek hourglass with glowing emerald green sand", CEN),
 ("s3-funnel",    "light", "a wide funnel with several sheets of paper being drawn down into it and condensing into one small card below",
                            "a funnel with sheets of paper condensing into one small card", CEN),
 ("s4-quote",     "dark",  "a clean single-page quotation document with neat line items and a total line at the bottom glowing emerald green",
                            "a clean quotation document with a glowing green total line", CEN),
 ("s5-plane",     "light", "a crisp paper airplane folded from a letter, caught mid-flight at a three quarter angle",
                            "a paper airplane folded from a letter, mid-flight", CEN),
 ("s6-clipboard", "dark",  "a clipboard holding a checklist with several glowing emerald green checkmarks",
                            "a clipboard with a checklist and glowing green checkmarks", CEN),
 ("s7-bubble",    "light", "a single rounded speech bubble with a small exclamation mark inside turning into a glowing emerald green check",
                            "a rounded speech bubble with a glowing green check inside", CEN),
 ("s8-pen",       "dark",  "a sleek pen nib drawing a single glowing emerald green underline stroke",
                            "a sleek pen nib drawing a glowing green underline", CEN),
 ("s9-cards",     "dark",  "a small neat fanned stack of rounded cards, the top one glowing emerald green along its edge",
                            "a small fanned stack of rounded cards with a glowing green edge", CTA),
]
def retry(fn, n=4, wait=6):
    for i in range(n):
        try: return fn()
        except Exception as e:
            if i == n-1: raise
            print("   retry", str(e)[:50], flush=True); time.sleep(wait)
# 1) scene
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
# 2) fuse
for name, var, _, desc, pos in jobs:
    out = f"{A}/{name}_fused.png"
    if os.path.exists(out): continue
    grad = GD if var == "dark" else GL
    fo.fuse(grad, f"{A}/{name}_scene.png", out, var, desc, **pos)
    print("fused", name, flush=True)
print("FINE")
