#!/usr/bin/env python3
"""Carosello "Dal 2 agosto cambia una cosa sola" (AI Act) — template T2 SFUMATURA.
- alternanza scuro/chiaro
- gruppo SEAMLESS da 3 slide (6-7-8) sulle slide CHIARE: la linea del tempo che le attraversa
- ANIMAZIONI: la linea del tempo (seamless, luce che avanza) + il b-roll UE nella cornice (slide 3)
- CTA con TRE azioni: salva, condividi, commenta
"""
import sys, os
SK = os.path.dirname(os.path.abspath(__file__)) + "/../../../../.claude/skills/carosello-produzione/scripts"
sys.path.insert(0, SK)
import slide_kit as sk, seam_video as sv
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__)); A = f"{HERE}/assets"
G, O, Wt = "#5CFC6E", "#FF7A1A", "#F5F7F5"
GD = "#0B7A38"          # verde scuro leggibile sulle slide chiare
TOT = 9                 # slide di contenuto 2-10

def obj(name, target_h=520):
    im = Image.open(f"{A}/{name}_cut.png").convert("RGBA")
    bb = im.split()[3].getbbox()
    if bb: im = im.crop(bb)
    w, h = im.size; sw = int(target_h * w / h)
    out = f"{A}/{name}_fit.png"; im.save(out)
    return sk.b64(out), sw, target_h

def hi(t, dark=True):
    return f'<b style="color:{G if dark else GD};font-weight:600">{t}</b>'

S = {}   # slide statiche (PNG)

# 2 HOOK (scuro) — calendario
b, w, h = obj('s2-calendar', 500)
S[2] = sk.slide_grad(b, "AI Act &middot; 2 agosto 2026", "Cambia", "una cosa sola",
    f'Tra pochi giorni scattano gli obblighi di trasparenza dell\'AI Act. In giro leggi di multe milionarie e certificazioni. {hi("La verit&agrave; &egrave; pi&ugrave; semplice")}, e pi&ugrave; utile da sapere.',
    0, total=TOT, variant="dark", subj_w=w, subj_h=h, subj_top=540, l2_indent=0)

# 4 OBBLIGO 1 (chiaro) — fumetto
b, w, h = obj('s3-chat', 470)
S[4] = sk.slide_grad(b, "Obbligo 1 &middot; Il chatbot", "Se risponde", "un'AI, dillo",
    f'Chi ti scrive deve capire che dall\'altra parte non c\'&egrave; una persona. {hi("Basta una riga chiara",0)} al primo messaggio, non serve altro.',
    2, total=TOT, variant="light", subj_w=w, subj_h=h, subj_top=560, l2_indent=60)

# 5 OBBLIGO 2 (scuro) — cornice con sigillo
b, w, h = obj('s4-frame', 480)
S[5] = sk.slide_grad(b, "Obbligo 2 &middot; I contenuti", "Se l'hai fatto", "con l'AI, si vede",
    f'Immagini, video, audio e testi generati vanno resi riconoscibili. Vale soprattutto per i deepfake e per i testi di attualit&agrave; {hi("pubblicati senza rilettura")}.',
    3, total=TOT, variant="dark", subj_w=w, subj_h=h, subj_top=560, l1_size=84, l2_size=76, l2_indent=40)

# 9 LA PARTE ONESTA (scuro) — martelletto
b, w, h = obj('s8-gavel', 470)
S[9] = sk.slide_grad(b, "La parte onesta", "Non rischi", "15 milioni",
    f'Il tetto &egrave; alto, ma per le piccole imprese la legge prende {hi("l\'importo minore")} tra la cifra fissa e la percentuale, non il maggiore. E le sanzioni pesanti riguardano le pratiche vietate, non la trasparenza.',
    7, total=TOT, variant="dark", subj_w=w, subj_h=h, subj_top=560, l2_indent=110)

# 10 CTA (scuro) — founder + TRE azioni
FND = sk.b64(f"{A}/f-calm_cut.png")
def azione(verbo, testo):
    """Riga azione secondaria: verbo verde in evidenza + motivo pratico."""
    return (f'<div style="margin-top:26px">'
            f'<span style="font-family:\'Space Grotesk\';font-weight:700;font-size:36px;color:{G};letter-spacing:.03em">{verbo}</span>'
            f'<span style="font-family:\'Inter\';font-weight:400;font-size:28px;line-height:1.35;color:#C9D8CE"> {testo}</span></div>')
_cta = (
  '<div style="position:absolute;left:82px;top:150px;width:660px;z-index:4">'
    f'<div style="font-family:\'Space Grotesk\';font-weight:600;font-size:27px;letter-spacing:.16em;text-transform:uppercase;color:{O};margin-bottom:16px">La checklist &middot; gratis</div>'
    f'<div style="font-family:\'Space Grotesk\';font-weight:700;font-size:82px;line-height:.94;letter-spacing:-.03em;color:{Wt};text-shadow:0 2px 20px rgba(0,0,0,.55)">Sei a posto<br>o no?</div>'
    + azione("SALVA", "questo post, ti serve prima del 2 agosto")
    + azione("CONDIVIDI", "con chi ha un\'attivit&agrave; e usa l\'AI")
    + '<div style="display:flex;align-items:center;gap:16px;margin-top:34px">'
      f'<span style="font-family:\'Space Grotesk\';font-weight:700;font-size:44px;color:{Wt}">Commenta</span>'
      f'<span style="display:inline-block;background:{G};color:#06240f;font-family:\'Space Grotesk\';font-weight:700;'
      f'font-size:46px;letter-spacing:.02em;padding:8px 26px;border-radius:14px;box-shadow:0 0 34px rgba(92,252,110,.55)">AGOSTO</span></div>'
    + f'<div style="font-family:\'Inter\';font-weight:400;font-size:28px;line-height:1.35;color:#C9D8CE;margin-top:16px;max-width:470px">e ti mando la checklist in 5 punti per capire in due minuti se ti riguarda.</div>'
  + '</div>')
_dots = ''.join(f'<span style="width:14px;height:14px;border-radius:50%;'
                f'{"background:"+G+";box-shadow:0 0 12px rgba(92,252,110,.6)" if i==TOT-1 else "border:2px solid rgba(157,182,166,.5)"};box-sizing:border-box"></span>'
                for i in range(TOT))
S[10] = (sk.CSS + f'<div class="stage" style="background:{sk.GRAD_DARK}">'
    f'<div style="position:absolute;inset:0;z-index:0;background:radial-gradient(ellipse 110% 75% at 86% 92%,rgba(92,252,110,.13),transparent 55%)"></div>'
    f'<img src="data:image/png;base64,{FND}" style="position:absolute;right:-70px;bottom:0;height:840px;z-index:2;filter:drop-shadow(0 20px 40px rgba(0,0,0,.6))">'
    f'<div style="position:absolute;top:82px;left:90px;display:flex;align-items:center;gap:12px;font-family:\'Space Grotesk\';font-size:22px;letter-spacing:.2em;text-transform:uppercase;color:#9DB6A6;z-index:5">'
    f'<span style="width:11px;height:11px;border-radius:50%;background:{G};box-shadow:0 0 14px {G}"></span>Wulver &middot; AI Act</div>'
    f'{_cta}'
    f'<div style="position:absolute;left:90px;right:90px;bottom:74px;display:flex;justify-content:space-between;align-items:center;z-index:5">'
    f'<div style="display:flex;gap:13px">{_dots}</div>'
    f'<div style="font-family:\'Space Grotesk\';font-weight:600;font-size:21px;letter-spacing:.08em;color:{G};border:2px solid {G};border-radius:999px;padding:8px 22px">wulver.it</div></div></div>')

for n, html in S.items():
    sk.render(html, f"{HERE}/slide-{n}.png"); print("statica", n)

# ---------------------------------------------------------------- 3: B-ROLL UE in cornice (video)
BOX = (95, 545, 890, 500)      # riquadro interno della cornice arancione
_frame = (f'<div style="position:absolute;left:90px;top:540px;width:900px;height:510px;border:5px solid {O};'
          f'border-radius:18px;box-shadow:0 0 40px rgba(255,122,26,.4);z-index:3"></div>')
_txt3 = (f'<div style="position:absolute;left:90px;right:90px;top:172px;z-index:4">'
    f'<div style="font-family:\'Space Grotesk\';font-weight:600;font-size:27px;letter-spacing:.16em;text-transform:uppercase;color:{O};margin-bottom:16px">Il dettaglio che nessuno dice</div>'
    f'<div style="font-family:\'Space Grotesk\';font-weight:700;font-size:88px;line-height:.94;letter-spacing:-.03em;color:{Wt};text-shadow:0 2px 20px rgba(0,0,0,.55)">Le regole sono</div>'
    f'<div style="font-family:\'Space Grotesk\';font-weight:700;font-size:96px;line-height:.94;letter-spacing:-.03em;text-transform:uppercase;color:{G};margin-left:50px;text-shadow:0 0 26px rgba(92,252,110,.45)">uscite il 20 luglio</div></div>')
_body3 = (f'<div style="position:absolute;left:90px;right:90px;bottom:150px;z-index:4;font-family:\'Inter\';font-weight:400;'
          f'font-size:31px;line-height:1.42;color:#C9D8CE;max-width:920px">La Commissione ha pubblicato le linee guida {hi("13 giorni prima")} della scadenza. Se sei in ritardo, non &egrave; colpa tua.</div>')
_eb3 = (f'<div style="position:absolute;top:82px;left:90px;display:flex;align-items:center;gap:12px;font-family:\'Space Grotesk\';'
        f'font-size:22px;letter-spacing:.2em;text-transform:uppercase;color:#9DB6A6;z-index:5">'
        f'<span style="width:11px;height:11px;border-radius:50%;background:{G};box-shadow:0 0 14px {G}"></span>Wulver &middot; AI Act</div>')
_d3 = ''.join(f'<span style="width:14px;height:14px;border-radius:50%;'
              f'{"background:"+G+";box-shadow:0 0 12px rgba(92,252,110,.6)" if i==1 else "border:2px solid rgba(157,182,166,.5)"};box-sizing:border-box"></span>'
              for i in range(TOT))
_foot3 = (f'<div style="position:absolute;left:90px;right:90px;bottom:74px;display:flex;justify-content:space-between;align-items:center;z-index:5">'
          f'<div style="display:flex;gap:13px">{_d3}</div>'
          f'<div style="font-family:\'Space Grotesk\';font-weight:600;font-size:21px;letter-spacing:.08em;color:{G};border:2px solid {G};border-radius:999px;padding:8px 22px">wulver.it</div></div>')
sk.render(sk.CSS + f'<div class="stage" style="background:{sk.GRAD_DARK}"></div>', f"{A}/_bg3.png")
sk.render(sk.CSS + f'<div class="stage">{_frame}{_eb3}{_txt3}{_body3}{_foot3}</div>', f"{A}/_fg3.png", transparent=True)
sv.build_box(f"{A}/_bg3.png", f"{A}/_fg3.png", f"{A}/broll-30156205.mp4", BOX, f"{HERE}/slide-3.mp4", dur=5.0, radius=16)
sv.poster(f"{HERE}/slide-3.mp4", f"{HERE}/slide-3.png", t=2.0)
print("video 3 (b-roll UE in cornice)")

# ------------------------------------------- 6-7-8: SEAMLESS chiaro animato (linea del tempo)
# La linea del tempo la compongo io: un marker generato, replicato 3 volte a scale crescenti sui
# centri dei 3 pannelli, uniti da una linea luminosa. Cosi' controllo esattamente proporzioni e
# posizioni (la generazione diretta dava marker giganti che coprivano il testo).
from PIL import ImageDraw, ImageFilter
BAND_W, BAND_H = 3240, 430
mk = Image.open(f"{A}/marker_cut.png").convert("RGBA")
bb = mk.split()[3].getbbox()
if bb: mk = mk.crop(bb)
band = Image.new("RGBA", (BAND_W, BAND_H), (0, 0, 0, 0))
BASE_Y = BAND_H - 70                                    # quota su cui poggiano tutti i marker
line = Image.new("RGBA", (BAND_W, BAND_H), (0, 0, 0, 0))
ld = ImageDraw.Draw(line)
ld.rounded_rectangle([120, BASE_Y - 9, BAND_W - 120, BASE_Y + 9], radius=9, fill=(92, 252, 110, 235))
glow = line.filter(ImageFilter.GaussianBlur(22))
band.alpha_composite(glow); band.alpha_composite(glow); band.alpha_composite(line)
for i, hgt in enumerate((250, 300, 355)):               # marker crescenti da sinistra a destra
    m = mk.copy(); m.thumbnail((10000, hgt))
    cx = 540 + i * 1080                                 # centro di ciascun pannello da 1080
    band.alpha_composite(m, (cx - m.size[0] // 2, BASE_Y - m.size[1] + 14))
band.save(f"{A}/wide-timeline_fit.png")
# Animazione IN TEMA: un impulso di luce che PERCORRE la linea del tempo da sinistra a destra,
# attraversando le 3 slide. Il movimento e' il messaggio: il tempo che avanza verso le scadenze.
sv.wide_pulse_alpha(f"{A}/wide-timeline_fit.png", f"{A}/timeline.mov", y=BASE_Y, dur=5.0, w=380, h=52, color=(220, 255, 232))
wide = sk.b64(f"{A}/wide-timeline_fit.png")
TL_TOP = 620
seam = [
 (0, 6, 2, "Ora &middot; 2 agosto 2026", "Adesso", "la trasparenza",
  f'Parte l\'obbligo di dichiarare l\'AI, e diventa operativo {hi("il sistema delle sanzioni",0)}.'),
 (1, 7, 3, "Poi &middot; 2 dicembre 2026", "Poi", "la marcatura",
  f'I sistemi gi&agrave; sul mercato dovranno marcare i contenuti generati: {hi("su quel fronte c\'&egrave; tempo",0)}.'),
 (2, 8, 4, "Dopo &middot; 2 dicembre 2027", "E il resto?", "rinviato",
  f'Gli obblighi pesanti sui sistemi ad alto rischio, quelli di cui hai sentito parlare, {hi("sono slittati di oltre un anno",0)}.'),
]
for panel, n, idx, kick, l1, l2, body in seam:
    L = sk.slide_grad(wide, kick, l1, l2, body, idx, total=TOT, variant="light",
                      seam_panel=panel, seam_wide_w=3240, subj_top=TL_TOP, l2_indent=40 + panel * 50, layers=True)
    sk.render(L["bg"], f"{A}/_bg{n}.png"); sk.render(L["fg"], f"{A}/_fg{n}.png", transparent=True)
    sv.build(f"{A}/_bg{n}.png", f"{A}/_fg{n}.png", f"{A}/timeline.mov", panel=panel, wide_w=3240,
             subj_top=TL_TOP, out=f"{HERE}/slide-{n}.mp4", mode="over")
    sv.poster(f"{HERE}/slide-{n}.mp4", f"{HERE}/slide-{n}.png", t=3.0)
    print("seamless animato", n)
print("DONE")
