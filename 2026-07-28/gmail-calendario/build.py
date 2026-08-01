#!/usr/bin/env python3
"""Carosello TUTORIAL 2/3: "Gmail e Calendario dentro Claude" — template T2 SFUMATURA.
- METODO OGGETTO FUSO: ogni oggetto e' GENERATO DENTRO la sfumatura del brand (scene su fondo che fa
  contrasto -> paste-feather -> img2img), con riflesso e ombra veri, niente quadrato. I file `*_fused.png`
  sono la SLIDE INTERA (sfondo + oggetto): si passano a slide_grad come bg_image, sopra vanno solo i testi.
- coppia SEAMLESS animata da 2 SOLE slide (4-5), soggetto UNICO che le attraversa (kling.py)
- CTA con azione principale CONDIVIDI (si alterna: Excel usava SALVA)
"""
import sys, os
SK = os.path.dirname(os.path.abspath(__file__)) + "/../../../../.claude/skills/carosello-produzione/scripts"
sys.path.insert(0, SK)
import slide_kit as sk

HERE = os.path.dirname(os.path.abspath(__file__)); A = f"{HERE}/assets"
G, O, Wt, GD = "#5CFC6E", "#FF7A1A", "#F5F7F5", "#0B7A38"
TOT = 8

def fused(name):
    return sk.b64(f"{A}/{name}_fused.png")

def hi(t, dark=True):
    return f'<b style="color:{G if dark else GD};font-weight:600">{t}</b>'

S = {}

# 2 HOOK (scuro)
S[2] = sk.slide_grad(None, "Gmail &middot; Il collegamento", "Claude legge", "la tua posta",
    f'Cerca nelle mail, ti prepara le risposte e ti riempie il calendario. {hi("Gratis anche sul piano base")}, e si attiva in due minuti.',
    0, total=TOT, variant="dark", l1_size=84, l2_size=80, l2_indent=0, bg_image=fused('s2-inbox'))

# 3 COME SI ATTIVA (scuro)
S[3] = sk.slide_grad(None, "Si fa una volta", "Due minuti", "e basta",
    f'Apri Claude, vai su Customize e poi Connectors, scegli Google e autorizzi. {hi("Non si installa niente")}: &egrave; solo un permesso che dai tu.',
    1, total=TOT, variant="dark", l2_indent=60, bg_image=fused('s3-plug'))

# 4 (chiaro) — la posta si fa evento. Oggetti singoli nitidi (la banda larga usciva sfocata da FLUX).
S[4] = sk.slide_grad(None, "Come lavora", "La posta", "si fa evento",
    f'Claude legge la mail, capisce che c\'&egrave; un appuntamento e {hi("te lo mette in agenda",0)} da solo, senza che tu apra il calendario.',
    2, total=TOT, variant="light", l1_size=88, l2_size=80, l2_indent=30, bg_image=fused('g4-mailcal'))

# 5 (chiaro) — tu leggi, lui organizza
S[5] = sk.slide_grad(None, "Senza copia-incolla", "Tu la leggi,", "lui la organizza",
    f'Niente pi&ugrave; passaggio a mano dalla posta all\'agenda: {hi("lo fa mentre tu fai altro",0)} e tu ritrovi tutto in ordine.',
    3, total=TOT, variant="light", l1_size=84, l2_size=78, l2_indent=50, bg_image=fused('g5-calfull'))

# 6 L'ESEMPIO (scuro)
S[6] = sk.slide_grad(None, "L'esempio vero", "Una frase,", "e ha gi&agrave; fatto",
    f'&laquo;Trova le mail di questo cliente degli ultimi tre mesi, riassumimi dove siamo e mettimi in agenda la chiamata di verifica.&raquo; {hi("Lo fa in un colpo solo")}.',
    4, total=TOT, variant="dark", l1_size=80, l2_size=74, l2_indent=90, bg_image=fused('s6-slot'))

# 7 COSA NON FA (chiaro)
S[7] = sk.slide_grad(None, "La cosa importante", "Le mail", "non le manda",
    f'Le scrive e te le lascia in bozza, ma {hi("l\'invio resta tuo",0)}. Non &egrave; un limite: &egrave; la protezione che ti evita la figuraccia mandata in automatico.',
    5, total=TOT, variant="light", l2_indent=40, bg_image=fused('s7-draft'))

# 8 LA PARTE ONESTA (scuro)
S[8] = sk.slide_grad(None, "La parte onesta", "Occhio a cosa", "gli fai leggere",
    f'Lo dice Anthropic stessa: un file ricevuto da uno sconosciuto pu&ograve; contenere istruzioni nascoste. {hi("Collega solo quello che ti serve")} e non far analizzare allegati sospetti.',
    6, total=TOT, variant="dark", l1_size=76, l2_size=70, l2_indent=110, bg_image=fused('s8-shield'))

# 9 CTA (scuro) — azione principale CONDIVIDI; oggetto FUSO in basso di lato (full-bleed bg)
b9 = fused('s9-key')
def riga(verbo, testo):
    return (f'<div style="margin-top:22px">'
            f'<span style="font-family:\'Space Grotesk\';font-weight:700;font-size:32px;color:{G};letter-spacing:.03em">{verbo}</span>'
            f'<span style="font-family:\'Inter\';font-weight:400;font-size:26px;line-height:1.35;color:#C9D8CE"> {testo}</span></div>')
_cta = ('<div style="position:absolute;left:82px;top:150px;width:640px;z-index:4">'
    f'<div style="font-family:\'Space Grotesk\';font-weight:600;font-size:27px;letter-spacing:.16em;text-transform:uppercase;color:{O};margin-bottom:16px">Chi vive nelle mail</div>'
    f'<div style="font-family:\'Space Grotesk\';font-weight:700;font-size:64px;line-height:1.0;letter-spacing:-.03em;color:{Wt};text-shadow:0 2px 20px rgba(0,0,0,.55)">Conosci uno cos&igrave;?</div>'
    f'<div style="margin-top:30px"><span style="font-family:\'Space Grotesk\';font-weight:700;font-size:48px;color:{G};text-shadow:0 0 22px rgba(92,252,110,.5)">CONDIVIDI</span></div>'
    f'<div style="font-family:\'Inter\';font-weight:400;font-size:27px;line-height:1.35;color:#C9D8CE;margin-top:8px;max-width:470px">mandalo a chi passa la giornata dentro la casella di posta.</div>'
    '<div style="display:flex;align-items:center;gap:12px;margin-top:26px">'
      f'<span style="font-family:\'Space Grotesk\';font-weight:700;font-size:34px;color:{Wt}">Commenta</span>'
      f'<span style="display:inline-block;background:{G};color:#06240f;font-family:\'Space Grotesk\';font-weight:700;'
      f'font-size:34px;padding:6px 20px;border-radius:12px;box-shadow:0 0 30px rgba(92,252,110,.55)">MAIL</span></div>'
    f'<div style="font-family:\'Inter\';font-weight:400;font-size:25px;line-height:1.35;color:#C9D8CE;margin-top:8px;max-width:470px">e ti mando le 5 richieste che uso ogni giorno.</div>'
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
