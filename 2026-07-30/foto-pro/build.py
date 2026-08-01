#!/usr/bin/env python3
"""Carosello TUTORIAL: "Trasforma un selfie in una foto professionale" — T2 SFUMATURA, oggetti fusi.
Audience LARGA. Tool onesto: ChatGPT / Gemini (non Claude: non genera immagini).
Slide 4-5 = SEAMLESS ANIMATA (il prima->dopo), fatte da _seam.py. CTA: commenta FOTO + salva."""
import sys, os
SK = os.path.dirname(os.path.abspath(__file__)) + "/../../../../.claude/skills/carosello-produzione/scripts"
sys.path.insert(0, SK)
import slide_kit as sk

HERE = os.path.dirname(os.path.abspath(__file__)); A = f"{HERE}/assets"
G, O, Wt, GD = "#5CFC6E", "#FF7A1A", "#F5F7F5", "#0B7A38"
TOT = 8

def fused(name): return sk.b64(f"{A}/{name}_fused.png")
def hi(t, dark=True): return f'<b style="color:{G if dark else GD};font-weight:600">{t}</b>'
def prompt(txt, dark=True):
    col = "#DCEBE1" if dark else "#25402F"
    return f'<span style="color:{col}">&laquo;{txt}&raquo;</span>'

S = {}

# 2 HOOK (scuro) — smartphone
S[2] = sk.slide_grad(None, "Foto pro &middot; Senza fotografo", "Il selfie che diventa", "foto da CV",
    f'Da una tua foto normale a un ritratto professionale in due minuti, con un\'AI che hai gi&agrave; sul telefono. {hi("Gratis o quasi")}.',
    0, total=TOT, variant="dark", l1_size=80, l2_size=84, l2_indent=30, bg_image=fused('s2-phone'))

# 3 STEP 1 (chiaro) — upload
S[3] = sk.slide_grad(None, "Passo 1 &middot; Carica", "Una tua foto", "ben illuminata",
    f'Apri ChatGPT o Gemini e carica una foto dove {hi("si vede bene il viso",0)}. Anche un selfie va bene, basta che sia a fuoco e non troppo scuro.',
    1, total=TOT, variant="light", l1_size=82, l2_size=80, l2_indent=30, bg_image=fused('s3-upload'))

# 6 STEP 2 / IL PROMPT (scuro) — il prompt vero nella slide
S[6] = sk.slide_grad(None, "Passo 2 &middot; Il prompt", "Copia questo,", "incollalo",
    f'{prompt("Trasforma questa foto in un ritratto professionale: giacca scura, sfondo neutro sfocato, luce soft frontale, sguardo in camera. Mantieni identici il mio viso e i miei tratti")}',
    4, total=TOT, variant="dark", l1_size=78, l2_size=74, l2_indent=40, bg_image=fused('s6-wand'))

# 7 LA PARTE ONESTA (chiaro) — id card
S[7] = sk.slide_grad(None, "La parte onesta", "&Egrave; un ritratto,", "non un documento",
    f'L\'AI a volte ti ritocca i tratti. Va benissimo per {hi("social e LinkedIn",0)}, ma non usarla per foto tessera, documenti o per spacciarla come foto vera.',
    5, total=TOT, variant="light", l1_size=80, l2_size=74, l2_indent=30, bg_image=fused('s7-idcard'))

# 8 IN PIU' (scuro) — frames
S[8] = sk.slide_grad(None, "Il trucco in pi&ugrave;", "Chiedine tre,", "poi scegli",
    f'Fattene fare {hi("tre versioni")} con sfondo e giacca diversi, e tieni quella che ti somiglia di pi&ugrave;. Se cambia troppo il viso, riscrivi: mantieni i miei tratti.',
    6, total=TOT, variant="dark", l1_size=84, l2_size=80, l2_indent=50, bg_image=fused('s8-frames'))

# 9 CTA (scuro) — commenta FOTO + salva; cornice fusa in basso di lato
b9 = fused('s9-camera')
_cta = ('<div style="position:absolute;left:82px;top:150px;width:680px;z-index:4">'
    f'<div style="font-family:\'Space Grotesk\';font-weight:600;font-size:27px;letter-spacing:.16em;text-transform:uppercase;color:{O};margin-bottom:16px">Il prompt pronto</div>'
    f'<div style="font-family:\'Space Grotesk\';font-weight:700;font-size:80px;line-height:.96;letter-spacing:-.03em;color:{Wt};text-shadow:0 2px 20px rgba(0,0,0,.55)">Lo vuoi<br>gi&agrave; scritto?</div>'
    '<div style="display:flex;align-items:center;gap:16px;margin-top:30px">'
      f'<span style="font-family:\'Space Grotesk\';font-weight:700;font-size:42px;color:{Wt}">Commenta</span>'
      f'<span style="display:inline-block;background:{G};color:#06240f;font-family:\'Space Grotesk\';font-weight:700;'
      f'font-size:42px;padding:9px 26px;border-radius:14px;box-shadow:0 0 34px rgba(92,252,110,.55)">FOTO</span></div>'
    f'<div style="font-family:\'Inter\';font-weight:400;font-size:27px;line-height:1.35;color:#C9D8CE;margin-top:14px;max-width:480px">e ti mando il prompt esatto da incollare.</div>'
    '<div style="margin-top:22px">'
      f'<span style="font-family:\'Space Grotesk\';font-weight:700;font-size:32px;color:{G};letter-spacing:.03em">SALVA</span>'
      f'<span style="font-family:\'Inter\';font-weight:400;font-size:26px;line-height:1.35;color:#C9D8CE"> cos&igrave; lo ritrovi quando ti serve una foto decente</span></div>'
    '</div>')
_dots = ''.join(f'<span style="width:14px;height:14px;border-radius:50%;'
                f'{"background:"+G+";box-shadow:0 0 12px rgba(92,252,110,.6)" if i==TOT-1 else "border:2px solid rgba(157,182,166,.5)"};box-sizing:border-box"></span>'
                for i in range(TOT))
S[9] = (sk.CSS + '<div class="stage">'
    f'<img src="data:image/png;base64,{b9}" style="position:absolute;inset:0;width:1080px;height:1350px;object-fit:cover;z-index:0">'
    f'<div style="position:absolute;top:82px;left:90px;display:flex;align-items:center;gap:12px;font-family:\'Space Grotesk\';font-size:22px;letter-spacing:.2em;text-transform:uppercase;color:#9DB6A6;z-index:5">'
    f'<span style="width:11px;height:11px;border-radius:50%;background:{G};box-shadow:0 0 14px {G}"></span>Wulver &middot; Tutorial</div>'
    f'{_cta}'
    f'<div style="position:absolute;left:90px;right:90px;bottom:74px;display:flex;justify-content:space-between;align-items:center;z-index:5">'
    f'<div style="display:flex;gap:13px">{_dots}</div>'
    f'<div style="font-family:\'Space Grotesk\';font-weight:600;font-size:21px;letter-spacing:.08em;color:{G};border:2px solid {G};border-radius:999px;padding:8px 22px">wulver.it</div></div></div>')

for n, html in S.items():
    sk.render(html, f"{HERE}/slide-{n}.png"); print("statica", n)
print("STATICHE OK (4-5 le fa _seam.py)")
