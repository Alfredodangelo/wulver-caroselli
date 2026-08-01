#!/usr/bin/env python3
"""Carosello "Opus 5" — template GRADIENTE (slide_grad), alternanza scuro/chiaro.
Fonti dei fatti: annuncio Anthropic 24/07/2026 + docs (pricing, migration guide) + system card.
"""
import sys, os
SK = os.path.dirname(os.path.abspath(__file__)) + "/../../../../.claude/skills/carosello-produzione/scripts"
sys.path.insert(0, SK)
import slide_kit as sk
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__)); A = f"{HERE}/assets"
G, O, Wt = "#5CFC6E", "#FF7A1A", "#F5F7F5"
GD = "#0B7A38"  # verde scuro leggibile sulle slide chiare

def obj(name, target_h=540):
    """Ritaglia al bbox l'oggetto scontornato e lo scala ad altezza fissa: ritorna (b64, w, h)."""
    im = Image.open(f"{A}/{name}_cut.png").convert("RGBA")
    bb = im.split()[3].getbbox()
    if bb: im = im.crop(bb)
    w, h = im.size; sw = int(target_h * w / h)
    out = f"{A}/{name}_fit.png"; im.save(out)
    return sk.b64(out), sw, target_h

def hi(t, dark=True):  # evidenziazione nel corpo, leggibile su entrambe le varianti
    return f'<b style="color:{G if dark else GD};font-weight:600">{t}</b>'

S = {}
# 2 HOOK (scuro) — il "5"
b, w, h = obj('s2-five', 520)
S[2] = sk.slide_grad(b, "Novit&agrave; &middot; 24 luglio 2026", "&Egrave; uscito", "Opus 5",
    f'Anthropic ha rilasciato il suo nuovo modello. Costa come quello di prima, ma rende molto di pi&ugrave;. Ecco {hi("cosa cambia davvero")} per la tua azienda.',
    0, variant="dark", subj_w=w, subj_h=h, subj_top=520, l2_indent=0)
# 3 STESSO PREZZO, IL DOPPIO (chiaro)
b, w, h = obj('s3-scale', 500)
S[3] = sk.slide_grad(b, "Il salto", "Stesso prezzo,", "il doppio",
    f'Anthropic dichiara il doppio delle prestazioni rispetto al modello precedente, {hi("allo stesso costo",0)}. Pi&ugrave; lavoro fatto, stessa spesa.',
    1, variant="light", subj_w=w, subj_h=h, subj_top=540, l2_indent=60)
# 4 DECIDI QUANTO SPENDERE (scuro)
b, w, h = obj('s4-dial', 520)
S[4] = sk.slide_grad(b, "Il controllo", "Decidi tu", "quanto spendere",
    f'Cinque livelli di sforzo. Sui compiti semplici tieni basso e paghi poco, su quelli difficili alzi la leva. {hi("Stesso modello")}, costo che scegli tu.',
    2, variant="dark", subj_w=w, subj_h=h, subj_top=530, l1_size=88, l2_size=78, l2_indent=30)
# 5 ARRIVA IN FONDO (chiaro)
b, w, h = obj('s5-puzzle', 470)
S[5] = sk.slide_grad(b, "Il cambio vero", "Arriva in fondo", "al lavoro",
    f'Su un test di automazione aziendale fa 1,5 volte il secondo modello migliore. Non &laquo;sa usare gli strumenti&raquo;: {hi("porta a termine la catena",0)} senza mollarla a met&agrave;.',
    3, variant="light", subj_w=w, subj_h=h, subj_top=560, l1_size=84, l2_indent=90)
# 6 I GESTIONALI VECCHI (scuro)
b, w, h = obj('s6-monitor', 480)
S[6] = sk.slide_grad(b, "I gestionali vecchi", "Usa i programmi", "al posto tuo",
    f'Sa muoversi dentro un software a schermo, anche quello vecchio senza collegamenti. Per tante PMI italiane &egrave; la differenza tra {hi("&laquo;si pu&ograve; fare&raquo;")} e &laquo;lascia perdere&raquo;.',
    4, variant="dark", subj_w=w, subj_h=h, subj_top=560, l1_size=84, l2_size=94, l2_indent=120)
# 7 LEGGE TUTTO IN UNA VOLTA (chiaro)
b, w, h = obj('s7-docs', 540)
S[7] = sk.slide_grad(b, "La memoria", "Legge tutto", "in una volta",
    f'Un milione di token, circa 550.000 parole: un fascicolo intero, anni di bilanci, un contratto con tutti gli allegati. {hi("Senza spezzettare niente",0)}.',
    5, variant="light", subj_w=w, subj_h=h, subj_top=520, l2_indent=40)
# 8 LA PARTE ONESTA (scuro)
b, w, h = obj('s8-magnify', 470)
S[8] = sk.slide_grad(b, "La parte onesta", "Ma i numeri", "controllali",
    f'Lo dice Anthropic stessa: su certe affermazioni sbaglia un po&apos; pi&ugrave; di prima, e lo fa con la faccia sicura. Su dati e riferimenti {hi("la verifica resta tua")}.',
    6, variant="dark", subj_w=w, subj_h=h, subj_top=560, l2_indent=150)

# 9 CTA (scuro) — founder di lato + parola OPUS
FND = sk.b64(f"{A}/f-cover_cut.png")
_txt = (
  '<div style="position:absolute;left:82px;top:172px;width:600px;z-index:4">'
    f'<div style="font-family:\'Space Grotesk\';font-weight:600;font-size:27px;letter-spacing:.16em;text-transform:uppercase;color:{O};margin-bottom:16px">Da dove parti</div>'
    f'<div style="font-family:\'Space Grotesk\';font-weight:700;font-size:84px;line-height:.94;letter-spacing:-.03em;color:{Wt};text-shadow:0 2px 20px rgba(0,0,0,.55)">Cosa gli fai<br>fare per primo?</div>'
    '<div style="display:flex;align-items:center;gap:18px;margin-top:32px">'
      f'<span style="font-family:\'Space Grotesk\';font-weight:700;font-size:46px;color:{Wt}">Scrivi</span>'
      f'<span style="display:inline-block;background:{G};color:#06240f;font-family:\'Space Grotesk\';font-weight:700;font-size:48px;letter-spacing:.02em;padding:9px 26px;border-radius:15px;box-shadow:0 0 36px rgba(92,252,110,.55)">OPUS</span>'
    '</div>'
    f'<div style="font-family:\'Inter\';font-weight:400;font-size:30px;line-height:1.4;color:#C9D8CE;margin-top:24px;max-width:520px">nei commenti e ti mando <b style="color:{G};font-weight:600">3 modi concreti</b> per metterlo al lavoro nella tua azienda gi&agrave; questa settimana.</div>'
  '</div>')
_dots = ''.join(f'<span style="width:14px;height:14px;border-radius:50%;'
                f'{"background:"+G+";box-shadow:0 0 12px rgba(92,252,110,.6)" if i==7 else "border:2px solid rgba(157,182,166,.5)"};box-sizing:border-box"></span>'
                for i in range(8))
S[9] = (sk.CSS + f'<div class="stage" style="background:{sk.GRAD_DARK}">'
    f'<div style="position:absolute;inset:0;z-index:0;background:radial-gradient(ellipse 110% 75% at 84% 90%,rgba(92,252,110,.14),transparent 55%)"></div>'
    f'<img src="data:image/png;base64,{FND}" style="position:absolute;right:-60px;bottom:0;height:880px;z-index:2;filter:drop-shadow(0 20px 40px rgba(0,0,0,.6))">'
    f'<div style="position:absolute;top:82px;left:90px;display:flex;align-items:center;gap:12px;font-family:\'Space Grotesk\';font-size:22px;letter-spacing:.2em;text-transform:uppercase;color:#9DB6A6;z-index:5">'
    f'<span style="width:11px;height:11px;border-radius:50%;background:{G};box-shadow:0 0 14px {G}"></span>Wulver &middot; News AI</div>'
    f'{_txt}'
    f'<div style="position:absolute;left:90px;right:90px;bottom:74px;display:flex;justify-content:space-between;align-items:center;z-index:5">'
    f'<div style="display:flex;gap:13px">{_dots}</div></div></div>')

for n, html in S.items():
    sk.render(html, f"{HERE}/slide-{n}.png"); print("rendered", n)
print("DONE")
