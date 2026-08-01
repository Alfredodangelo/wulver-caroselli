#!/usr/bin/env python3
"""Fonde i 12 oggetti statici (6 Gmail + 6 PDF) dentro le sfumature del brand.
Oggetto al centro-basso; CTA (s9) in basso di lato. Salta i 2 seamless (animati a parte)."""
import sys, os
SK = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/.claude/skills/carosello-produzione/scripts"
sys.path.insert(0, SK)
import fuse_object as fo

B = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/03-contenuti/caroselli/2026-07-28"
G = f"{B}/gmail-calendario/assets"; P = f"{B}/pdf-scansioni/assets"
SC = "/tmp/claude-501/-Users-alfredo-Desktop-Progetti-Wulver/43804b13-b255-47f2-8d18-9a2cd642dfa1/scratchpad"

# sfumature vergini (una scura, una chiara) a misura slide
fo.virgin_grad("dark", f"{SC}/grad_dark.png")
fo.virgin_grad("light", f"{SC}/grad_light.png")
GD, GL = f"{SC}/grad_dark.png", f"{SC}/grad_light.png"

CEN = dict(W=780, cx=540, top=360)          # centro un po' piu' in basso
CTA = dict(W=540, cx=720, top=720)          # basso di lato (slide finale)

# (cartella, nome, variante, descrizione oggetto, posizione)
jobs = [
 (G, "s2-inbox",  "dark",  "a deep mail tray holding a stack of pale pearl-grey sealed envelopes, the top envelope glowing emerald green hex #5CFC6E along its flap", CEN),
 (G, "s3-plug",   "dark",  "two chunky pale pearl-grey connector plugs clicking together with a glowing emerald green hex #5CFC6E ring where they meet", CEN),
 (G, "s6-slot",   "dark",  "a pale pearl-grey calendar day block, one time-slot filled with a glowing emerald green hex #5CFC6E bar", CEN),
 (G, "s7-draft",  "light", "an open dark obsidian black envelope with a folded letter and a slim stylus, the letter edge glowing emerald green hex #5CFC6E", CEN),
 (G, "s8-shield", "dark",  "a pale pearl-grey shield standing in front of an envelope, a glowing warm orange hex #FF7A1A exclamation mark on the shield", CEN),
 (G, "s9-key",    "dark",  "a single chunky pale pearl-grey key with glowing emerald green hex #5CFC6E teeth", CTA),
 (P, "s2-scans",  "dark",  "a loose pile of pale scanned photo prints and sheets overlapping at careless angles, one sheet dog-eared", CEN),
 (P, "s3-pdfdoc", "dark",  "a single thick pale bound document with a glowing emerald green hex #5CFC6E spine", CEN),
 (P, "s6-find",   "dark",  "a pale magnifying glass enlarging one line of a document page which glows emerald green hex #5CFC6E", CEN),
 (P, "s7-form",   "light", "a dark obsidian black form sheet with recessed boxes, three filled with glowing emerald green hex #5CFC6E blocks and a slim stylus", CEN),
 (P, "s8-warn",   "dark",  "a single pale sheet standing upright with a glowing warm orange hex #FF7A1A exclamation triangle in front of it", CEN),
 (P, "s9-folder", "dark",  "a single pale closed document folder with a glowing emerald green hex #5CFC6E check mark on its cover", CTA),
]

done = 0
for d, name, var, desc, pos in jobs:
    out = f"{d}/{name}_fused.png"
    if os.path.exists(out):
        print("skip", name, flush=True); done += 1; continue
    grad = GD if var == "dark" else GL
    fo.fuse(grad, f"{d}/{name}_scene.png", out, var, desc, **pos)
    done += 1
    print(f"[{done}/{len(jobs)}] fuso {name}", flush=True)
print("FINE")
