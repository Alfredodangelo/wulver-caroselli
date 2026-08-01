#!/usr/bin/env python3
"""Carosello TUTORIAL 1/3: "Il foglio Excel incasinato che si sistema da solo" — template T2 SFUMATURA.
- gruppo SEAMLESS da 3 slide (4-5-6) sulle slide CHIARE: i 3 passi, con i dati che vanno dal caos all'ordine
- ANIMAZIONE multi-livello che attraversa i 3 tagli (onda + particelle a velocita' diverse + respiro)
- CTA con 3 azioni e OGGETTO al posto del founder (LoRA sospeso)
"""
import sys, os
SK = os.path.dirname(os.path.abspath(__file__)) + "/../../../../.claude/skills/carosello-produzione/scripts"
sys.path.insert(0, SK)
import slide_kit as sk, seam_video as sv
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__)); A = f"{HERE}/assets"
G, O, Wt = "#5CFC6E", "#FF7A1A", "#F5F7F5"
GD = "#0B7A38"
TOT = 8

def obj(name, target_h=500):
    im = Image.open(f"{A}/{name}_cut.png").convert("RGBA")
    bb = im.split()[3].getbbox()
    if bb: im = im.crop(bb)
    w, h = im.size; sw = int(target_h * w / h)
    out = f"{A}/{name}_fit.png"; im.save(out)
    return sk.b64(out), sw, target_h

def hi(t, dark=True):
    return f'<b style="color:{G if dark else GD};font-weight:600">{t}</b>'

S = {}

# 2 HOOK (scuro)
b, w, h = obj('s2-mess', 500)
S[2] = sk.slide_grad(b, "Excel &middot; Il trucco", "Il file sfasciato", "si sistema da solo",
    f'Quell\'export del gestionale con le intestazioni sballate e le celle sporche. {hi("Non serve installare niente")}, e funziona anche col piano gratuito.',
    0, total=TOT, variant="dark", subj_w=w, subj_h=h, subj_top=560, l1_size=80, l2_size=72, l2_indent=0)

# 3 LA SPUNTA (scuro)
b, w, h = obj('s3-check', 460)
S[3] = sk.slide_grad(b, "Prima di tutto", "Una spunta", "da attivare",
    f'Impostazioni, poi Capabilities, poi attivi {hi("&laquo;Code execution and file creation&raquo;")}. &Egrave; l\'interruttore che gli permette di aprire e scrivere file. Si fa una volta sola.',
    1, total=TOT, variant="dark", subj_w=w, subj_h=h, subj_top=590, l2_indent=60)

# 7 L'ESEMPIO (scuro)
b, w, h = obj('s7-chart', 470)
S[7] = sk.slide_grad(b, "L'esempio vero", "200 righe", "in due minuti",
    f'Un export con le date in tre formati diversi e gli importi salvati come testo. Risultato: date uniformi, {hi("importi sommabili")}, totale per cliente e grafico mensile.',
    5, total=TOT, variant="dark", subj_w=w, subj_h=h, subj_top=580, l2_indent=100)

# 8 IL LIMITE (chiaro)
b, w, h = obj('s8-magnify', 450)
S[8] = sk.slide_grad(b, "La parte onesta", "Ricontrolla", "i numeri",
    f'Su file molto grandi o con formule complicate pu&ograve; sbagliare, e {hi("non ti avvisa",0)}. Prima di mandare qualcosa al commercialista, verifica i totali.',
    6, total=TOT, variant="light", subj_w=w, subj_h=h, subj_top=600, l2_indent=40)

# 9 CTA (scuro) — oggetto al posto del founder + 3 azioni
b9, w9, h9 = obj('s9-doc', 660)
def azione(verbo, testo):
    return (f'<div style="margin-top:24px">'
            f'<span style="font-family:\'Space Grotesk\';font-weight:700;font-size:34px;color:{G};letter-spacing:.03em">{verbo}</span>'
            f'<span style="font-family:\'Inter\';font-weight:400;font-size:27px;line-height:1.35;color:#C9D8CE"> {testo}</span></div>')
_cta = (
  '<div style="position:absolute;left:82px;top:150px;width:640px;z-index:4">'
    f'<div style="font-family:\'Space Grotesk\';font-weight:600;font-size:27px;letter-spacing:.16em;text-transform:uppercase;color:{O};margin-bottom:16px">La richiesta pronta &middot; gratis</div>'
    f'<div style="font-family:\'Space Grotesk\';font-weight:700;font-size:80px;line-height:.94;letter-spacing:-.03em;color:{Wt};text-shadow:0 2px 20px rgba(0,0,0,.55)">Vuoi il testo<br>gi&agrave; scritto?</div>'
    + azione("SALVA", "ti serve la prossima volta che esporti")
    + azione("CONDIVIDI", "con chi passa le serate a sistemare fogli")
    + '<div style="display:flex;align-items:center;gap:16px;margin-top:32px">'
      f'<span style="font-family:\'Space Grotesk\';font-weight:700;font-size:44px;color:{Wt}">Commenta</span>'
      f'<span style="display:inline-block;background:{G};color:#06240f;font-family:\'Space Grotesk\';font-weight:700;'
      f'font-size:46px;padding:8px 26px;border-radius:14px;box-shadow:0 0 34px rgba(92,252,110,.55)">EXCEL</span></div>'
    + f'<div style="font-family:\'Inter\';font-weight:400;font-size:28px;line-height:1.35;color:#C9D8CE;margin-top:16px;max-width:470px">e ti mando la richiesta esatta da copiare e incollare.</div>'
  + '</div>')
_dots = ''.join(f'<span style="width:14px;height:14px;border-radius:50%;'
                f'{"background:"+G+";box-shadow:0 0 12px rgba(92,252,110,.6)" if i==TOT-1 else "border:2px solid rgba(157,182,166,.5)"};box-sizing:border-box"></span>'
                for i in range(TOT))
S[9] = (sk.CSS + f'<div class="stage" style="background:{sk.GRAD_DARK}">'
    f'<div style="position:absolute;inset:0;z-index:0;background:radial-gradient(ellipse 110% 75% at 84% 88%,rgba(92,252,110,.13),transparent 55%)"></div>'
    f'<img src="data:image/png;base64,{b9}" style="position:absolute;right:20px;bottom:150px;width:{w9}px;z-index:2;filter:drop-shadow(0 24px 40px rgba(0,0,0,.6))">'
    f'<div style="position:absolute;top:82px;left:90px;display:flex;align-items:center;gap:12px;font-family:\'Space Grotesk\';font-size:22px;letter-spacing:.2em;text-transform:uppercase;color:#9DB6A6;z-index:5">'
    f'<span style="width:11px;height:11px;border-radius:50%;background:{G};box-shadow:0 0 14px {G}"></span>Wulver &middot; Tutorial</div>'
    f'{_cta}'
    f'<div style="position:absolute;left:90px;right:90px;bottom:74px;display:flex;justify-content:space-between;align-items:center;z-index:5">'
    f'<div style="display:flex;gap:13px">{_dots}</div>'
    f'<div style="font-family:\'Space Grotesk\';font-weight:600;font-size:21px;letter-spacing:.08em;color:{G};border:2px solid {G};border-radius:999px;padding:8px 22px">wulver.it</div></div></div>')

for n, html in S.items():
    sk.render(html, f"{HERE}/slide-{n}.png"); print("statica", n)

# ------------------------------- 4-5-6: SEAMLESS chiaro animato (caos -> ordine, i 3 passi)
# La banda la compongo io da UNA tessera generata: a sinistra ammucchiate e ruotate a caso, al centro
# in rotazione e piu' distanziate, a destra righe complanari perfettamente allineate. Comporla a mano
# e' l'unico modo di avere una banda 3240 x ~500 (un'immagine generata a 2:1, scalata a 3240, verrebbe
# alta 1641px e uscirebbe dal canvas) e di controllare che nulla di importante cada sulle cuciture.
import random
from PIL import ImageDraw
random.seed(7)
BAND_W, BH = 3240, 520
TOP = 560
tile = Image.open(f"{A}/tile_cut.png").convert("RGBA")
bb = tile.split()[3].getbbox()
if bb: tile = tile.crop(bb)
tile.thumbnail((360, 360))
band = Image.new("RGBA", (BAND_W, BH), (0, 0, 0, 0))
def put(img, cx, cy, rot=0, scale=1.0, op=1.0):
    t = img.rotate(rot, expand=True, resample=Image.BICUBIC)
    if scale != 1.0:
        t = t.resize((max(int(t.size[0]*scale),1), max(int(t.size[1]*scale),1)), Image.LANCZOS)
    if op < 1.0:
        a = t.split()[3].point(lambda v: int(v*op)); t.putalpha(a)
    band.alpha_composite(t, (int(cx - t.size[0]/2), int(cy - t.size[1]/2)))
# CAOS (pannello 1): tessere sovrapposte, ruotate a caso, quote diverse
for _ in range(14):
    put(tile, random.randint(120, 980), random.randint(100, BH-190),
        rot=random.uniform(-75, 75), scale=random.uniform(.55, .85), op=random.uniform(.75, 1))
# TRANSIZIONE (pannello 2): rotazioni che si raddrizzano, piu' spaziate
for i in range(6):
    put(tile, 1180 + i*160, BH - 150 - i*8, rot=38 - i*7, scale=.7, op=.9)
# ORDINE (pannello 3): righe complanari, bordi sinistri allineati, spaziatura uguale
for r in range(5):
    put(tile, 2560, 150 + r*88, rot=0, scale=.78)
band.save(f"{A}/wide-order_fit.png")
# Animazione multi-livello: l'onda di "riordino" percorre tutta la banda + 3 particelle a velocita'
# diverse + respiro. Tutti gli elementi attraversano i 3 tagli: la continuita' si vede.
sv.wide_motion_alpha(f"{A}/wide-order_fit.png", f"{A}/order.mov",
    sweep={"y": BH * 0.55, "w": 520, "h": 90, "color": (225, 255, 235), "op": .85, "from": -0.12, "to": 1.12},
    particles=[{"y": BH * 0.30, "w": 150, "h": 34, "color": (150, 252, 175), "op": .55, "delay": .18},
               {"y": BH * 0.72, "w": 190, "h": 40, "color": (200, 255, 215), "op": .5,  "delay": .40},
               {"y": BH * 0.45, "w": 110, "h": 26, "color": (255, 190, 130), "op": .45, "delay": .62}],
    dur=5.0, breathe=0.022)
wide = sk.b64(f"{A}/wide-order_fit.png")
seam = [
 (0, 4, 2, "Passo 1 &middot; Carica", "Trascina", "il file",
  f'Anche se &egrave; un disastro: righe doppie, intestazioni a met&agrave;, {hi("numeri salvati come testo",0)}. Fino a 30 MB per file.'),
 (1, 5, 3, "Passo 2 &middot; Chiedi", "Di' cosa", "non va",
  f'&laquo;Sistema le intestazioni, togli le righe vuote, converti in numeri la colonna importo e dammi il totale per cliente.&raquo; {hi("In italiano",0)}, come lo diresti a una persona.'),
 (2, 6, 4, "Passo 3 &middot; Riprendi", "Torna indietro", "il file pulito",
  f'Te lo restituisce in .xlsx con le formule dentro, e il grafico se glielo chiedi. {hi("Non &egrave; uno screenshot",0)}, &egrave; il file vero da riaprire.'),
]
for panel, n, idx, kick, l1, l2, body in seam:
    L = sk.slide_grad(wide, kick, l1, l2, body, idx, total=TOT, variant="light",
                      seam_panel=panel, seam_wide_w=BAND_W, subj_top=TOP,
                      l1_size=84, l2_size=90, l2_indent=30 + panel * 45, layers=True)
    sk.render(L["bg"], f"{A}/_bg{n}.png"); sk.render(L["fg"], f"{A}/_fg{n}.png", transparent=True)
    sv.build(f"{A}/_bg{n}.png", f"{A}/_fg{n}.png", f"{A}/order.mov", panel=panel, wide_w=BAND_W,
             subj_top=TOP, out=f"{HERE}/slide-{n}.mp4", mode="over")
    sv.poster(f"{HERE}/slide-{n}.mp4", f"{HERE}/slide-{n}.png", t=2.6)
    print("seamless animato", n)
print("DONE")
