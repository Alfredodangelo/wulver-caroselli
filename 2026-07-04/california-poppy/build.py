#!/usr/bin/env python3
import sys, os, base64, subprocess
SKILL_SCRIPTS = os.path.dirname(os.path.abspath(__file__)) + "/../../../../.claude/skills/carosello-produzione/scripts"
sys.path.insert(0, SKILL_SCRIPTS)
from slide_kit import b64, stage, slide, img_frame, card, dots, render, GRID_CLEAN
from composite_video_in_frame import probe_rect, composite, verify_confined
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = f"{HERE}/assets"
FIN = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/05-asset/copertine/studio/finite"

grid = b64(GRID_CLEAN)
# Posa founder CTA: variare tra i caroselli (non sempre la stessa). Qui 'aha' (indice alzato = "ecco il punto/la risorsa").
FND = b64(f"{FIN}/aha.png")
CAPITOL = b64(f"{ASSETS}/slide2_capitol.jpg")
POSTER_GOV = b64(f"{ASSETS}/poster_gov.png")
POSTER_CDT = b64(f"{ASSETS}/poster_cdt.png")

BODY2 = ("Non parliamo di un'azienda che sperimenta un nuovo tool. Parliamo della California, uno stato con quasi 40 milioni di abitanti, "
         "che ha appena deciso di usare l'intelligenza artificiale nel lavoro quotidiano dei suoi dipendenti pubblici. "
         "L'accordo è vero, è firmato, e i numeri dietro sono più concreti di quanto sembri.")
BODY3 = ("Il 29 giugno il governatore Gavin Newsom ha annunciato una partnership con Anthropic. Agenzie statali, città e contee possono usare "
         "Claude con uno sconto del <span class=\"or\">50%</span>, con in più formazione gratuita per il personale e assistenza tecnica diretta "
         "dai team di Anthropic.")
BODY4 = ("Poppy è l'assistente digitale costruito dallo stato per i propri dipendenti, pensato per rispondere alle domande e ai compiti più "
         "comuni del lavoro d'ufficio. Il pilota è partito a settembre 2025 con oltre <span class=\"gr\">2.800 dipendenti</span> in "
         "<span class=\"gr\">67 dipartimenti</span> diversi, e ora si prepara al rollout su tutto lo stato.")
BODY5 = ("Il rollout completo è già previsto per <span class=\"or\">questo mese</span>. E non è l'unico caso reale: il DMV della California usa "
         "Claude per abbassare i tempi di attesa agli sportelli, mentre il dipartimento della sanità, la più grande agenzia Medicaid del paese, "
         "lo usa per i flussi di lavoro interni e assistere meglio i beneficiari.")
BODY6 = ("Poppy non è un prodotto esclusivo di Anthropic. È stato progettato per funzionare con più modelli AI insieme, non legato a un solo "
         "fornitore. Claude ha contribuito al suo sviluppo, ma la scelta dello stato è stata quella di <span class=\"or\">non dipendere da "
         "un'azienda sola</span>.")
BODY7 = ("Se uno stato con migliaia di dipendenti e procedure complesse è riuscito a passare da pilota a rollout in meno di un anno, una piccola "
         "azienda può fare lo stesso molto più in fretta. Non serve un reparto IT dedicato: serve <span class=\"gr\">iniziare con lo strumento "
         "giusto e una richiesta scritta bene</span>.")

S = {}
S[2] = slide(grid, "Uno stato ha assunto l'IA", img_frame(CAPITOL), BODY2, 1)
S[3] = slide(grid, "L'accordo, in breve", img_frame(POSTER_GOV), BODY3, 2)
S[4] = slide(grid, "Il primo risultato: Poppy", img_frame(POSTER_CDT), BODY4, 3)
S[5] = slide(grid, "Non &egrave; pi&ugrave; un esperimento",
             card("Dal pilota al rollout statale",
                  '<span class="chip dim">Pilota: 2.800 dipendenti</span><span class="arrow">&rarr;</span><span class="chip orb">Rollout: tutto lo stato</span>',
                  "67 dipartimenti coinvolti, rollout completo previsto per luglio 2026"),
             BODY5, 4)
S[6] = slide(grid, "Un dettaglio poco notato",
             card("Non &egrave; un prodotto a marchio unico",
                  '<span class="chip dim">Solo Claude</span><span class="arrow">&rarr;</span><span class="chip orb">Claude, Gemini, GPT, Nova</span>',
                  "Poppy &egrave; costruito per funzionare con pi&ugrave; modelli, non da un unico fornitore"),
             BODY6, 5)
S[7] = slide(grid, "Cosa significa per te", "", BODY7, 6)
S[8] = stage(grid,
    f'<img class="founder" src="data:image/png;base64,{FND}">'
    f'<div class="eyebrow"><span class="d"></span>Wulver &middot; News AI</div>'
    f'<div class="cta-c"><div class="beat wh">Vuoi il tuo assistente interno, senza reparto IT?</div>'
    f'<div class="sub" style="margin-top:20px">Scrivi POPPY nei commenti: ti mando in DM un prompt pronto per creare un assistente AI interno con Claude, pensato per una piccola azienda.</div>'
    f'<div class="pill">Commenta POPPY</div></div>'
    f'<div class="foot" style="right:auto">{dots(6, 7)}</div>')

for n, html in S.items():
    out = f"{HERE}/slide-{n}.png"
    render(html, out)
    print("rendered", out)

# --- mask-probe per le slide video (3 = scroll-gov, 4 = scroll-cdt) ---
BLACK = Image.new("RGB", (1080, 1350), (0, 0, 0))
black_path = f"{ASSETS}/_probe_black.png"
BLACK.save(black_path)
black_b64 = b64(black_path)

for n, poster_path, real_video, out_name, beat, body in (
    (3, f"{ASSETS}/poster_gov.png", f"{ASSETS}/scroll-gov-6s.mp4", "slide-3-VIDEO.mp4", "L'accordo, in breve", BODY3),
    (4, f"{ASSETS}/poster_cdt.png", f"{ASSETS}/scroll-cdt-6s.mp4", "slide-4-VIDEO.mp4", "Il primo risultato si chiama Poppy", BODY4),
):
    w, h = Image.open(poster_path).size
    white_path = f"{ASSETS}/_probe_white_{n}.png"
    Image.new("RGB", (w, h), (255, 255, 255)).save(white_path)
    neutralize = ('<style>.eyebrow,.eyebrow *,.beat,.body,.body *,.handle,.dot,.dot.on,.d'
                  '{color:#000 !important;background:#000 !important;box-shadow:none !important;'
                  'border-color:#000 !important;text-shadow:none !important}</style>')
    probe_html = slide(black_b64, beat, img_frame(b64(white_path)), body, n - 1) + neutralize
    probe_png = f"{ASSETS}/_probe_{n}.png"
    render(probe_html, probe_png)
    x, y, pw, ph = probe_rect(probe_png)
    print(f"slide {n} rect:", x, y, pw, ph)
    static_png = f"{HERE}/slide-{n}.png"
    out_mp4 = f"{HERE}/{out_name}"
    composite(static_png, real_video, x, y, pw, ph, 6.0, out_mp4, radius=18)
    result = verify_confined(out_mp4, (x, y, pw, ph))
    print(f"slide {n} verify:", result)

print("DONE")
