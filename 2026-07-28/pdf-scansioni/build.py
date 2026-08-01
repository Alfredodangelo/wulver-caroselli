#!/usr/bin/env python3
"""Carosello TUTORIAL 3/3: "Cinque scansioni, un PDF unico e cercabile" — template T2 SFUMATURA.
- METODO OGGETTO FUSO (bg_image = *_fused.png, slide intera generata nella sfumatura)
- coppia SEAMLESS animata da 2 SOLE slide (4-5): il fiume di fogli che converge in un documento (kling.py)
- CTA con azione principale COMMENTA (si alterna: Excel=SALVA, Gmail=CONDIVIDI, PDF=COMMENTA per la risorsa)
"""
import sys, os
SK = os.path.dirname(os.path.abspath(__file__)) + "/../../../../.claude/skills/carosello-produzione/scripts"
sys.path.insert(0, SK)
import slide_kit as sk

HERE = os.path.dirname(os.path.abspath(__file__)); A = f"{HERE}/assets"
G, O, Wt, GD = "#5CFC6E", "#FF7A1A", "#F5F7F5", "#0B7A38"
TOT = 8

def fused(name): return sk.b64(f"{A}/{name}_fused.png")
def hi(t, dark=True): return f'<b style="color:{G if dark else GD};font-weight:600">{t}</b>'

S = {}

# 2 HOOK (scuro)
S[2] = sk.slide_grad(None, "PDF &middot; Il trucco", "Cinque scansioni", "un PDF solo",
    f'Foto storte, ricevute sparse, pagine in disordine. {hi("Le unisci in un file solo")}, dritto e ordinato, senza scanner e senza app a pagamento.',
    0, total=TOT, variant="dark", l1_size=84, l2_size=80, bg_image=fused('s2-scans'))

# 3 COME SI FA (scuro)
S[3] = sk.slide_grad(None, "Passo 1 &middot; Carica", "Buttale dentro", "tutte insieme",
    f'Trascini le foto o gli scan in Claude e dici: {hi("&laquo;Uniscile in un unico PDF, raddrizza le pagine e mettile in ordine&raquo;")}. Anche venti alla volta.',
    1, total=TOT, variant="dark", l1_size=80, l2_size=76, l2_indent=50, bg_image=fused('s3-pdfdoc'))

# 6 IL PAYOFF (scuro) — cercabile (OCR)
S[6] = sk.slide_grad(None, "Passo 2 &middot; Cerca", "Adesso", "&egrave; cercabile",
    f'Legge il testo dentro le immagini. Cerchi &laquo;fattura marzo&raquo; o un importo e {hi("te lo trova nel mucchio")}, anche se era una foto.',
    4, total=TOT, variant="dark", l1_size=88, l2_size=80, l2_indent=40, bg_image=fused('s6-find'))

# 7 IN PIU' (chiaro) — estrae i dati
S[7] = sk.slide_grad(None, "In pi&ugrave;", "Ti tira fuori", "i dati in tabella",
    f'&laquo;Fammi la lista di date e importi di tutte le fatture.&raquo; {hi("Da mucchio di scansioni a tabella",0)} pronta da incollare in un foglio.',
    5, total=TOT, variant="light", l1_size=82, l2_size=76, l2_indent=30, bg_image=fused('s7-form'))

# 8 LA PARTE ONESTA (scuro)
S[8] = sk.slide_grad(None, "La parte onesta", "L'OCR", "ogni tanto sbaglia",
    f'Su calligrafia storta o scansioni sbiadite pu&ograve; leggere male un numero, e {hi("non te lo segnala")}. Sugli importi che contano, ricontrolla a occhio.',
    6, total=TOT, variant="dark", l1_size=88, l2_size=78, l2_indent=60, bg_image=fused('s8-warn'))

# 9 CTA (scuro) — azione principale COMMENTA (risorsa: il prompt esatto)
b9 = fused('s9-folder')
def riga(verbo, testo):
    return (f'<div style="margin-top:22px">'
            f'<span style="font-family:\'Space Grotesk\';font-weight:700;font-size:32px;color:{G};letter-spacing:.03em">{verbo}</span>'
            f'<span style="font-family:\'Inter\';font-weight:400;font-size:26px;line-height:1.35;color:#C9D8CE"> {testo}</span></div>')
_cta = ('<div style="position:absolute;left:82px;top:150px;width:740px;z-index:4">'
    f'<div style="font-family:\'Space Grotesk\';font-weight:600;font-size:27px;letter-spacing:.16em;text-transform:uppercase;color:{O};margin-bottom:16px">La richiesta pronta</div>'
    f'<div style="font-family:\'Space Grotesk\';font-weight:700;font-size:58px;line-height:1.0;letter-spacing:-.03em;color:{Wt};text-shadow:0 2px 20px rgba(0,0,0,.55)">Vuoi il prompt esatto?</div>'
    '<div style="display:flex;align-items:center;gap:16px;margin-top:30px">'
      f'<span style="font-family:\'Space Grotesk\';font-weight:700;font-size:42px;color:{Wt}">Commenta</span>'
      f'<span style="display:inline-block;background:{G};color:#06240f;font-family:\'Space Grotesk\';font-weight:700;'
      f'font-size:42px;padding:9px 26px;border-radius:14px;box-shadow:0 0 34px rgba(92,252,110,.55)">PDF</span></div>'
    f'<div style="font-family:\'Inter\';font-weight:400;font-size:27px;line-height:1.35;color:#C9D8CE;margin-top:14px;max-width:480px">e ti mando la richiesta gi&agrave; scritta, da copiare e incollare.</div>'
    + riga("SALVA", "cos&igrave; ce l\'hai la prossima volta che ti serve")
    + '</div>')
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
print("STATICHE OK (le 4-5 le fa kling.py)")
