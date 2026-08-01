#!/usr/bin/env python3
import sys, os
SK = os.path.dirname(os.path.abspath(__file__)) + "/../../../../.claude/skills/carosello-produzione/scripts"
sys.path.insert(0, SK)
import slide_kit as sk

HERE = os.path.dirname(os.path.abspath(__file__)); A = f"{HERE}/assets"
FIN = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/05-asset/foto/cover-reel"
grid = sk.b64(sk.GRID_CLEAN)
O, G, Wt = "#FF7A1A", "#5CFC6E", "#F5F7F5"
FND = sk.b64(f"{FIN}/reveal-4.png")  # posa variata: braccia conserte, autorevole

def img(f): return f"{A}/{f}.png"
def deb(f, lo=6, hi=55, feather=0.0): return sk.b64(sk.de_black(img(f), f"{A}/{f}_nobg.png", lo, hi, feather))
def raw(f): return sk.b64(img(f))  # ossidiana: immagine intera, no de_black
# ossidiana SCONTORNATA (rembg -> {f}_cut.png) + alone morbido che la fonde con la griglia (preferenza utente)
def cut(f, **kw): return sk.b64(sk.cutout_halo(f"{A}/{f}_cut.png", f"{A}/{f}_halo.png", **kw))

S = {}
# 2 HOOK (ossidiana: mano STOP)
S[2] = sk.slide_hero(grid, cut('s2-hook'), "AI in azienda &middot; I confini", "non deve fare", "tutto",
    'L\'AI ti fa risparmiare ore, ma se le lasci mano libera ti crea guai. Ci sono <span class="gr">6 cose</span> che non deve MAI fare da sola.',
    0, subj_w=720, subj_top=300, mask_solid=(8, 92), l2_indent=0)
# 3 CONFINE 1 clienti (blueprint chat)
S[3] = sk.slide_hero(grid, deb('s3-clienti', feather=0.06), "Confine 1 &middot; I clienti", "Non risponde", "da sola",
    'Falle scrivere la bozza, ma l\'invio al cliente lo controlli tu. Un tono sbagliato o <span class="gr">una promessa inventata</span> li paghi caro.',
    1, subj_w=1000, subj_top=140, mask_solid=(37, 84), l2_indent=70)
# 4 CONFINE 2 numeri (particelle, full-bleed)
S[4] = sk.slide_hero(grid, deb('s4-numeri', feather=0.14), "Confine 2 &middot; I numeri", "Occhio ai", "numeri",
    'L\'AI inventa dati e statistiche con la faccia sicura. Ogni numero <span class="gr">daglielo tu o verificalo</span>, mai copiarlo com\'&egrave;.',
    2, subj_w=1360, subj_top=130, mask_solid=(40, 82), l2_indent=120)
# 5 CONFINE 3 privacy (ossidiana lucchetto)
S[5] = sk.slide_hero(grid, cut('s5-privacy'), "Confine 3 &middot; La privacy", "Non tocca", "i dati",
    'Non incollare dati sensibili di clienti o dipendenti nei tool pubblici. Finiscono chiss&agrave; dove, e <span class="gr">per il GDPR la responsabilit&agrave; &egrave; tua</span>.',
    3, subj_w=810, subj_top=255, mask_solid=(8, 92), l2_indent=40)
# 6 CONFINE 4 esperti (blueprint bilancia)
S[6] = sk.slide_hero(grid, deb('s6-esperto', feather=0.06), "Confine 4 &middot; Gli esperti", "Non sostituisce", "l'esperto",
    'Su fisco, contratti e salute l\'AI ti orienta, <span class="gr">non decide</span>. Su cose regolamentate una risposta sbagliata costa cara: c\'&egrave; il professionista.',
    4, subj_w=860, subj_top=250, mask_solid=(37, 84), l2_indent=96)
# 7 CONFINE 5 contenuti (blueprint invio+occhio)
S[7] = sk.slide_hero(grid, deb('s7-online', feather=0.06), "Confine 5 &middot; I contenuti", "Non va", "online",
    'Niente post, email o pagine pubblicate senza che un umano le rilegga. L\'AI <span class="gr">sbaglia nomi, date e tono</span>, e online lo vedono tutti.',
    5, subj_w=980, subj_top=185, mask_solid=(37, 84), l2_indent=64)
# 8 CONFINE 6 scelte (ossidiana re scacchi)
S[8] = sk.slide_hero(grid, cut('s8-scelte'), "Confine 6 &middot; Le scelte", "Non decide", "per te",
    'L\'AI &egrave; un assistente velocissimo, non il capo. <span class="gr">Le decisioni e la responsabilit&agrave; restano tue</span>: lei prepara, tu scegli.',
    6, subj_w=430, subj_top=360, mask_solid=(8, 92), l2_indent=130)

# 9 CTA: guida generata + founder + parola REGOLE
chk = deb('cta-guida', feather=0.06)
_cta_txt = (
  '<div style="position:absolute;left:78px;top:150px;width:600px;z-index:3">'
    f'<div style="font-family:\'Space Grotesk\';font-weight:600;font-size:27px;letter-spacing:.16em;text-transform:uppercase;color:{O};margin-bottom:16px">La guida &middot; gratis</div>'
    f'<div style="font-family:\'Space Grotesk\';font-weight:700;font-size:84px;line-height:.94;letter-spacing:-.03em;color:{Wt};text-shadow:0 2px 18px rgba(0,0,0,.85)">Usala senza rischi</div>'
    '<div style="display:flex;align-items:center;gap:18px;margin-top:30px">'
      f'<span style="font-family:\'Space Grotesk\';font-weight:700;font-size:46px;color:{Wt}">Scrivi</span>'
      f'<span style="display:inline-block;background:{G};color:#06240f;font-family:\'Space Grotesk\';font-weight:700;font-size:48px;letter-spacing:.02em;padding:9px 26px;border-radius:15px;box-shadow:0 0 36px rgba(92,252,110,.55)">REGOLE</span>'
    '</div>'
    f'<div style="font-family:\'Inter\';font-weight:400;font-size:30px;line-height:1.4;color:#DCE4DE;margin-top:24px;max-width:540px">nei commenti e ti mando la mini-guida <b style="color:{G};font-weight:600">cosa s&igrave; / cosa no</b> dell\'AI in azienda.</div>'
  '</div>')
S[9] = sk.stage(grid,
    f'<div style="position:absolute;inset:0;z-index:0;background:radial-gradient(ellipse 120% 80% at 84% 92%,rgba(92,252,110,.10),transparent 55%)"></div>'
    f'<img src="data:image/png;base64,{chk}" style="position:absolute;left:33%;top:460px;transform:translateX(-50%);width:820px;z-index:1;-webkit-mask-image:linear-gradient(to bottom,#000 66%,transparent 96%);mask-image:linear-gradient(to bottom,#000 66%,transparent 96%)">'
    f'<div style="position:absolute;left:0;right:0;bottom:0;height:560px;z-index:2;background:linear-gradient(to top,rgba(4,6,6,.8) 0%,transparent 100%)"></div>'
    f'<img src="data:image/png;base64,{FND}" style="position:absolute;right:-80px;bottom:0;height:820px;z-index:2">'
    f'<div class="eyebrow" style="z-index:4"><span class="d"></span>Wulver &middot; AI in azienda</div>'
    f'{_cta_txt}'
    f'<div class="foot" style="right:auto;z-index:4">{sk.dots(7,8)}</div>')

for n, html in S.items():
    sk.render(html, f"{HERE}/slide-{n}.png"); print("rendered", n)
print("DONE")
