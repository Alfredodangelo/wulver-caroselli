#!/usr/bin/env python3
"""Carosello CLASSIFICA: "5 AI gratis che battono quelle a pagamento" — T2 SFUMATURA, oggetti fusi. Statico.
Audience LARGA (per tutti, non solo PMI). CTA: commenta GRATIS (lista coi link) + salva."""
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

# 2 HOOK (scuro) — regalo
S[2] = sk.slide_grad(None, "Gratis sul serio", "Cinque AI gratis", "che valgono di pi&ugrave;",
    f'Il 90% paga per cose che ha gi&agrave; gratis. {hi("Queste cinque le uso ogni giorno")}: ecco per cosa e con che limiti.',
    0, total=TOT, variant="dark", l1_size=82, l2_size=76, l2_indent=30, bg_image=fused('s2-gift'))

# 3 NotebookLM (chiaro)
S[3] = sk.slide_grad(None, "1 &middot; NotebookLM &middot; Google", "I tuoi documenti", "diventano un'AI",
    f'Carichi PDF, appunti, anche video YouTube e gli fai domande: risponde citando dove l\'ha letto, e te lo riassume in audio. {hi("Gratis: 50 domande e 3 audio al giorno",0)}.',
    1, total=TOT, variant="light", l1_size=82, l2_size=80, l2_indent=30, bg_image=fused('s3-notebook'))

# 4 Perplexity (scuro)
S[4] = sk.slide_grad(None, "2 &middot; Perplexity", "La ricerca", "con le fonti",
    f'Come Google, ma ti d&agrave; la risposta con i link da cui l\'ha presa, cos&igrave; verifichi. {hi("Gratis col modello pieno")}, circa 10 domande ogni 5 ore.',
    2, total=TOT, variant="dark", l1_size=88, l2_size=84, l2_indent=40, bg_image=fused('s4-search'))

# 5 DeepSeek (chiaro)
S[5] = sk.slide_grad(None, "3 &middot; DeepSeek", "Come ChatGPT,", "senza limiti",
    f'Chat, testi, conti, ragionamenti: {hi("nessun tetto giornaliero",0)}, tutto gratis. Onesto: i dati stanno su server in Cina, non dargli roba sensibile.',
    3, total=TOT, variant="light", l1_size=86, l2_size=80, l2_indent=50, bg_image=fused('s5-infinity'))

# 6 Gemini (scuro)
S[6] = sk.slide_grad(None, "4 &middot; Gemini &middot; Google", "Il tuttofare,", "con Google dentro",
    f'Ci butti dentro interi documenti (un milione di parole di contesto), cerca sul web e vive dentro Gmail e Documenti. {hi("Il piano gratis &egrave; molto generoso")}.',
    4, total=TOT, variant="dark", l1_size=80, l2_size=72, l2_indent=30, bg_image=fused('s6-spark'))

# 7 Claude (chiaro)
S[7] = sk.slide_grad(None, "5 &middot; Claude &middot; Anthropic", "La scrittura", "fatta meglio",
    f'Per email, testi e documenti lunghi &egrave; quello che scrive pi&ugrave; naturale e umano. {hi("Gratis circa 20 messaggi al giorno",0)}, bastano per le cose che contano.',
    5, total=TOT, variant="light", l1_size=86, l2_size=82, l2_indent=40, bg_image=fused('s7-pen'))

# 8 LA PARTE ONESTA (scuro) — gauge
S[8] = sk.slide_grad(None, "La parte onesta", "Il gratis", "ha dei tetti",
    f'Limiti di messaggi, code nelle ore di punta, niente memoria infinita. {hi("Paghi solo se sbatti contro quei tetti ogni giorno")}: per quasi tutti, il gratis basta.',
    6, total=TOT, variant="dark", l1_size=88, l2_size=84, l2_indent=70, bg_image=fused('s8-gauge'))

# 9 CTA (scuro) — commenta GRATIS (lista coi link) + salva; busta fusa in basso di lato
b9 = fused('s9-list')
_cta = ('<div style="position:absolute;left:82px;top:150px;width:680px;z-index:4">'
    f'<div style="font-family:\'Space Grotesk\';font-weight:600;font-size:27px;letter-spacing:.16em;text-transform:uppercase;color:{O};margin-bottom:16px">La lista pronta</div>'
    f'<div style="font-family:\'Space Grotesk\';font-weight:700;font-size:78px;line-height:.96;letter-spacing:-.03em;color:{Wt};text-shadow:0 2px 20px rgba(0,0,0,.55)">Li vuoi tutti<br>con i link?</div>'
    '<div style="display:flex;align-items:center;gap:16px;margin-top:30px">'
      f'<span style="font-family:\'Space Grotesk\';font-weight:700;font-size:42px;color:{Wt}">Commenta</span>'
      f'<span style="display:inline-block;background:{G};color:#06240f;font-family:\'Space Grotesk\';font-weight:700;'
      f'font-size:42px;padding:9px 26px;border-radius:14px;box-shadow:0 0 34px rgba(92,252,110,.55)">GRATIS</span></div>'
    f'<div style="font-family:\'Inter\';font-weight:400;font-size:27px;line-height:1.35;color:#C9D8CE;margin-top:14px;max-width:480px">e ti mando la lista dei 5 con i link diretti.</div>'
    '<div style="margin-top:22px">'
      f'<span style="font-family:\'Space Grotesk\';font-weight:700;font-size:32px;color:{G};letter-spacing:.03em">SALVA</span>'
      f'<span style="font-family:\'Inter\';font-weight:400;font-size:26px;line-height:1.35;color:#C9D8CE"> cos&igrave; te li ricordi quando ti servono</span></div>'
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
print("DONE")
