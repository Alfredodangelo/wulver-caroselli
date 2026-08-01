#!/usr/bin/env python3
import sys, os
SK = os.path.dirname(os.path.abspath(__file__)) + "/../../../../.claude/skills/carosello-produzione/scripts"
sys.path.insert(0, SK)
import slide_kit as sk

HERE = os.path.dirname(os.path.abspath(__file__)); A = f"{HERE}/assets"
FIN = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/05-asset/foto/cover-reel"
grid = sk.b64(sk.GRID_CLEAN)
O, G, Wt = "#FF7A1A", "#5CFC6E", "#F5F7F5"
FND = sk.b64(f"{FIN}/aha.png")

def img(f): return f"{A}/{f}.png"
def deb(f, lo=6, hi=55, feather=0.0): return sk.b64(sk.de_black(img(f), f"{A}/{f}_nobg.png", lo, hi, feather))
def fade(f, fx=0.14, fy=0.14): return sk.b64(sk.fade_edges(img(f), f"{A}/{f}_fade.png", fx, fy))
def debh(f, **kw): return sk.b64(sk.de_black_halo(img(f), f"{A}/{f}_halo.png", **kw))  # scuri: alone nero (ripiego)
def raw(f): return sk.b64(img(f))  # OSSIDIANA: immagine INTERA, niente de_black; si inserisce tutta, mask sfuma alto/basso

# LAYOUT: titolo + WULVER in ALTO a sinistra, IMMAGINE GRANDE al centro (riempie lo spazio, sfumata
# sopra/sotto), CORPO in BASSO. mix-case: neutra bianca + ACCENTO verde MAIUSCOLO. l2_indent varia.
S = {}
# 2 HOOK (blueprint persona al laptop)
S[2] = sk.slide_hero(grid, deb('s2-hook', feather=0.06), "Prompt &middot; Il metodo", "&egrave; il tuo", "prompt",
    'Quasi mai &egrave; colpa dell\'AI: &egrave; di come gliela chiedi. Ecco i <span class="gr">6 pezzi</span> che trasformano una richiesta vaga in una risposta precisa.',
    0, support="non &egrave; l\'AI a sbagliare,", subj_w=1180, subj_top=170, mask_solid=(40, 84), l2_indent=0)
# 3 RUOLO (ossidiana testa)
S[3] = sk.slide_hero(grid, raw('s3-ruolo'), "Step 1 &middot; Il ruolo", "Dai un", "ruolo",
    'Di\' all\'AI chi deve essere: <span class="gr">"Agisci come un commercialista"</span>, "Sei un copywriter di email". Le fai indossare i panni giusti.',
    1, subj_w=1120, subj_top=200, mask_solid=(30, 74), l2_indent=72)
# 4 SPECIFICO (particelle freccia -> bersaglio)
S[4] = sk.slide_hero(grid, deb('s4-compito', feather=0.14), "Step 2 &middot; Il compito", "Sii", "specifico",
    'Non "scrivimi un post", ma "un post IG da 100 parole per un ristorante, sul menu di Pasqua". <span class="gr">Pi&ugrave; sei preciso</span>, meno l\'AI indovina.',
    2, subj_w=1360, subj_top=160, mask_solid=(36, 84), l2_indent=120)
# 5 CONTESTO (blueprint cartella)
S[5] = sk.slide_hero(grid, deb('s5-contesto', feather=0.06), "Step 3 &middot; Il contesto", "Dai il", "contesto",
    'Incolla le info che servono: prodotto, cliente tipo, dati, come parli. L\'AI <span class="gr">non ti legge nel pensiero</span>, glielo dai tu.',
    3, subj_w=1080, subj_top=300, mask_solid=(39, 84), l2_indent=40)
# 6 FORMATO (ossidiana blocchi)
S[6] = sk.slide_hero(grid, raw('s6-formato'), "Step 4 &middot; Il formato", "Chiedi il", "formato",
    'Di\' come vuoi la risposta: "in elenco", "in tabella", "massimo 5 righe", "tono informale". Cos&igrave; <span class="gr">non riscrivi tutto dopo</span>.',
    4, subj_w=1160, subj_top=260, mask_solid=(26, 72), l2_indent=96)
# 7 REGOLE (particelle raggi, full-bleed largo)
S[7] = sk.slide_hero(grid, deb('s7-regole', feather=0.13), "Step 5 &middot; Le regole", "Metti dei", "paletti",
    'Aggiungi i limiti: <span class="gr">"se non sai, dimmelo"</span> invece di inventare. Le regole evitano le risposte sbagliate.',
    5, subj_w=1520, subj_top=-10, mask_solid=(43, 82), l2_indent=64)
# 8 ESEMPIO (blueprint due cubi)
S[8] = sk.slide_hero(grid, deb('s8-esempio', feather=0.08), "Step 6 &middot; L'esempio", "Mostra un", "esempio",
    'Il trucco pi&ugrave; potente: incolla un esempio del risultato che vuoi. <span class="gr">"Scrivilo come questo"</span> e l\'AI copia stile e struttura.',
    6, subj_w=1200, subj_top=165, mask_solid=(37, 84), l2_indent=130)

# 9 CTA: testo IN ALTO (come le altre slide) + checklist generata (fal) + founder che indica su
chk = deb('cta-checklist', feather=0.13)
_cta_txt = (
  '<div style="position:absolute;left:78px;top:150px;width:600px;z-index:3">'
    f'<div style="font-family:\'Space Grotesk\';font-weight:600;font-size:27px;letter-spacing:.16em;text-transform:uppercase;color:{O};margin-bottom:16px">La risorsa &middot; gratis</div>'
    f'<div style="font-family:\'Space Grotesk\';font-weight:700;font-size:88px;line-height:.94;letter-spacing:-.03em;color:{Wt};text-shadow:0 2px 18px rgba(0,0,0,.85)">Vuoi lo schema pronto?</div>'
    '<div style="display:flex;align-items:center;gap:18px;margin-top:30px">'
      f'<span style="font-family:\'Space Grotesk\';font-weight:700;font-size:48px;color:{Wt}">Scrivi</span>'
      f'<span style="display:inline-block;background:{G};color:#06240f;font-family:\'Space Grotesk\';font-weight:700;font-size:50px;letter-spacing:.02em;padding:9px 28px;border-radius:15px;box-shadow:0 0 36px rgba(92,252,110,.55)">PROMPT</span>'
    '</div>'
    f'<div style="font-family:\'Inter\';font-weight:400;font-size:30px;line-height:1.4;color:#DCE4DE;margin-top:24px;max-width:540px">nei commenti e ti mando in DM il <b style="color:{G};font-weight:600">template compilabile</b> con i 6 pezzi.</div>'
  '</div>')
S[9] = sk.stage(grid,
    f'<div style="position:absolute;inset:0;z-index:0;background:radial-gradient(ellipse 120% 80% at 84% 92%,rgba(92,252,110,.10),transparent 55%)"></div>'
    f'<img src="data:image/png;base64,{chk}" style="position:absolute;left:33%;top:520px;transform:translateX(-50%);width:1120px;z-index:1;-webkit-mask-image:linear-gradient(to bottom,#000 66%,transparent 96%);mask-image:linear-gradient(to bottom,#000 66%,transparent 96%)">'
    f'<div style="position:absolute;left:0;right:0;bottom:0;height:560px;z-index:2;background:linear-gradient(to top,rgba(4,6,6,.8) 0%,transparent 100%)"></div>'
    f'<img src="data:image/png;base64,{FND}" style="position:absolute;right:-80px;bottom:0;height:820px;z-index:2">'
    f'<div class="eyebrow" style="z-index:4"><span class="d"></span>Wulver &middot; Prompt</div>'
    f'{_cta_txt}'
    f'<div class="foot" style="right:auto;z-index:4">{sk.dots(7,8)}</div>')

for n, html in S.items():
    sk.render(html, f"{HERE}/slide-{n}.png"); print("rendered", n)
print("DONE")
