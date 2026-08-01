#!/usr/bin/env python3
import sys, os
SK = os.path.dirname(os.path.abspath(__file__)) + "/../../../../.claude/skills/carosello-produzione/scripts"
sys.path.insert(0, SK)
import slide_kit as sk

HERE = os.path.dirname(os.path.abspath(__file__)); A = f"{HERE}/assets"
grid = sk.b64(sk.GRID_CLEAN)
O, G, Wt = "#FF7A1A", "#5CFC6E", "#F5F7F5"
FND = sk.b64(f"{A}/f-cta_cut.png")

def img(f): return f"{A}/{f}.png"
def deb(f, lo=6, hi=55, feather=0.0): return sk.b64(sk.de_black(img(f), f"{A}/{f}_nobg.png", lo, hi, feather))
def cut(f, **kw): return sk.b64(sk.cutout_halo(f"{A}/{f}_cut.png", f"{A}/{f}_halo.png", **kw))
def debw(f, feather=0.07): return sk.b64(sk.de_black(img(f), f"{A}/{f}_db.png", 6, 55, feather))  # seamless larga

seam_time = debw('seam-time')   # clessidra -> ingranaggi (slide 2-3)
seam_wheel = debw('seam-wheel')  # ruota -> uscita (slide 6-7)

S = {}
# 2-3 SEAMLESS: tempo -> falla lavorare (clessidra che versa negli ingranaggi)
S[2] = sk.slide_seam(grid, seam_time, "L", "Il metodo &middot; Il tempo", "Il tuo tempo", "non torna",
    'È l\'unico asset che non compri e non recuperi. Ogni ora nei task ripetitivi è persa <span class="gr">per sempre</span>.',
    0, subj_top=120, l2_indent=0)
S[3] = sk.slide_seam(grid, seam_time, "R", "Il metodo &middot; Il tempo", "Falla lavorare", "per te",
    'Ribalta la domanda: non «come lo faccio io», ma <span class="gr">«come lo fa l\'AI al posto mio»</span>. Tu la guidi, non la esegui.',
    1, subj_top=120, l2_indent=70)
# 4 STRATEGIA (grafico che sale)
S[4] = sk.slide_hero(grid, deb('s4-graph', feather=0.06), "La strategia", "Automatizzare", "è strategia",
    'Non è una spesa da tagliare. È la scelta che ti fa crescere <span class="gr">senza assumere</span> e senza bruciarti.',
    2, subj_w=1020, subj_top=260, mask_solid=(37, 84), l2_indent=120)
# 5 IL VERO FRENO (te, pensieroso)
S[5] = sk.slide_hero(grid, cut('f-pensive', halo_op=0.78, halo_blur=52), "Il vero freno", "Chi resta fermo", "ha paura",
    'Quasi mai è questione di soldi. È la paura di sbagliare. Ma restare fermi <span class="gr">costa più che provare</span>.',
    3, subj_w=760, subj_top=300, mask_solid=(8, 92), l2_indent=40)
# 6-7 SEAMLESS: la ruota del criceto -> l'uscita
S[6] = sk.slide_seam(grid, seam_wheel, "L", "La trappola", "Più clienti", "non bastano",
    'Se sei tu la ruota che gira, ogni cliente in più è solo un altro giro. Corri di più, <span class="gr">non arrivi più lontano</span>.',
    4, subj_top=120, l2_indent=96)
S[7] = sk.slide_seam(grid, seam_wheel, "R", "La trappola", "Esci dalla", "ruota",
    'Smetti di essere tu la ruota. Automatizza i giri ripetitivi e <span class="gr">la strada si apre</span>.',
    5, subj_top=120, l2_indent=64)
# 8 IL PUNTO (cervello: tu decidi)
S[8] = sk.slide_hero(grid, deb('s8-brain', feather=0.06), "Il punto", "Tu non esegui.", "decidi",
    'L\'AI fa i giri ripetitivi. Le <span class="gr">scelte, la strategia e la responsabilità</span> restano tue.',
    6, subj_w=1000, subj_top=250, mask_solid=(37, 84), l2_indent=130)

# 9 CTA
_cta_txt = (
  '<div style="position:absolute;left:78px;top:150px;width:600px;z-index:3">'
    f'<div style="font-family:\'Space Grotesk\';font-weight:600;font-size:27px;letter-spacing:.16em;text-transform:uppercase;color:{O};margin-bottom:16px">La lista &middot; gratis</div>'
    f'<div style="font-family:\'Space Grotesk\';font-weight:700;font-size:86px;line-height:.94;letter-spacing:-.03em;color:{Wt};text-shadow:0 2px 18px rgba(0,0,0,.85)">Cosa togli<br>per primo?</div>'
    '<div style="display:flex;align-items:center;gap:18px;margin-top:32px">'
      f'<span style="font-family:\'Space Grotesk\';font-weight:700;font-size:48px;color:{Wt}">Scrivi</span>'
      f'<span style="display:inline-block;background:{G};color:#06240f;font-family:\'Space Grotesk\';font-weight:700;font-size:50px;letter-spacing:.02em;padding:9px 28px;border-radius:15px;box-shadow:0 0 36px rgba(92,252,110,.55)">TEMPO</span>'
    '</div>'
    f'<div style="font-family:\'Inter\';font-weight:400;font-size:30px;line-height:1.4;color:#DCE4DE;margin-top:24px;max-width:540px">nei commenti e ti mando i <b style="color:{G};font-weight:600">5 task</b> che una PMI come la tua può togliersi subito.</div>'
  '</div>')
S[9] = sk.stage(grid,
    f'<div style="position:absolute;inset:0;z-index:0;background:radial-gradient(ellipse 120% 80% at 86% 96%,rgba(92,252,110,.12),transparent 55%)"></div>'
    f'<div style="position:absolute;left:0;right:0;bottom:0;height:560px;z-index:2;background:linear-gradient(to top,rgba(4,6,6,.8) 0%,transparent 100%)"></div>'
    f'<img src="data:image/png;base64,{FND}" style="position:absolute;right:-70px;bottom:0;height:900px;z-index:2">'
    f'<div class="eyebrow" style="z-index:4"><span class="d"></span>Wulver &middot; AI in azienda</div>'
    f'{_cta_txt}'
    f'<div class="foot" style="right:auto;z-index:4">{sk.dots(7,8)}</div>')

for n, html in S.items():
    sk.render(html, f"{HERE}/slide-{n}.png"); print("rendered", n)
print("DONE")
