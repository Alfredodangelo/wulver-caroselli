#!/usr/bin/env python3
"""Gmail 4-5 come due OGGETTI SINGOLI nitidi (la banda larga usciva sfocata da FLUX).
Genera 2 scene (light = obsidiana su bianco) e le fonde sulla sfumatura chiara."""
import sys, os, time, urllib.request
SK = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/.claude/skills/carosello-produzione/scripts"
sys.path.insert(0, SK)
import fal_client as fc, fuse_object as fo

A = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/03-contenuti/caroselli/2026-07-28/gmail-calendario/assets"
SC = "/tmp/claude-501/-Users-alfredo-Desktop-Progetti-Wulver/43804b13-b255-47f2-8d18-9a2cd642dfa1/scratchpad"
LIGHT = ("The object is polished obsidian black with a chamfered edge and emerald green hex #5CFC6E glowing accents. "
         "It sits on a white glossy reflective floor that mirrors it softly below, plus a soft grey contact shadow. "
         "Pure clean white seamless studio background, bright soft lighting, large soft key from upper left, deep "
         "focus, tack sharp, crisp micro bevels, physically based rendering, three quarter view slightly above, "
         "100mm lens. No text, no letters, no numbers, no logo, no watermark.")
objs = {
 "g4-mailcal": "An open envelope tilting forward, pouring a single glowing emerald green event card down into an open calendar block below it",
 "g5-calfull": "A calendar day block with three time-slots filled by glowing emerald green event bars and a small emerald check mark in the corner",
}
def retry(fn, n=4, wait=6):
    for i in range(n):
        try: return fn()
        except Exception as e:
            if i == n-1: raise
            time.sleep(wait)
for name, desc in objs.items():
    if not os.path.exists(f"{A}/{name}_scene.png"):
        def gen(d=desc, nm=name):
            rid, surl, rurl = fc.submit("fal-ai/flux/dev", {"prompt": f"A premium 3D product render. {d}. {LIGHT}", "image_size": "square_hd", "num_images": 1})
            fc.poll(surl, interval=6, timeout=500, log=lambda m: None)
            u = (fc._req(rurl or f"{fc.QUEUE_BASE}/fal-ai/flux/dev/requests/{rid}").get("images") or [{}])[0].get("url")
            urllib.request.urlretrieve(u, f"{A}/{nm}_scene.png")
        retry(gen); print("scene", name, flush=True)
fo.virgin_grad("light", f"{SC}/grad_light.png")
for name in objs:
    fo.fuse(f"{SC}/grad_light.png", f"{A}/{name}_scene.png", f"{A}/{name}_fused.png",
            "light", objs[name].lower(), W=780, cx=540, top=360)
    print("fuso", name, flush=True)
print("FINE")
