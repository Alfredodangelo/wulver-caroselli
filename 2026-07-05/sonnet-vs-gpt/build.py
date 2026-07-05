#!/usr/bin/env python3
import sys, os
SKILL = os.path.dirname(os.path.abspath(__file__)) + "/../../../../.claude/skills/carosello-produzione/scripts"
sys.path.insert(0, SKILL)
from slide_kit import b64, stage, dots, render, GRID_CLEAN, CSS
from composite_video_in_frame import probe_rect, composite, verify_confined
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
A = f"{HERE}/assets"
FIN = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/05-asset/foto/cover-reel"
grid = b64(GRID_CLEAN)
FND = b64(f"{FIN}/reveal-5.png")
LC = b64(f"{A}/logo-claude.png")
LG = b64(f"{A}/logo-chatgpt.png")
EYE = "Wulver &middot; Confronti AI"
ORANGE, GREEN = "#FF7A1A", "#5CFC6E"

def badge(logo_b64, nome, colore):
    return (f'<div style="align-self:center;margin-top:20px;display:flex;align-items:center;gap:14px;'
            f'background:rgba(9,13,14,.9);border:2px solid {colore};border-radius:999px;padding:12px 26px 12px 18px">'
            f'<span style="font-family:\'Space Grotesk\';font-weight:500;font-size:22px;letter-spacing:.08em;text-transform:uppercase;color:#9DB6A6">Meglio con</span>'
            f'<img src="data:image/png;base64,{logo_b64}" style="height:38px;width:38px;object-fit:contain">'
            f'<span style="font-family:\'Space Grotesk\';font-weight:700;font-size:30px;color:{colore}">{nome}</span></div>')

def img_html(data_b64, is_video=False):
    tag = (f'<video src="data:video/mp4;base64,{data_b64}" autoplay muted loop></video>' if is_video
           else f'<img src="data:image/png;base64,{data_b64}">')
    return f'<div class="imgframe">{tag}</div>'

def usecase(bg, titolo, badge_html, visual_html, body, idx, total=9):
    inner = (f'<div class="eyebrow"><span class="d"></span>{EYE}</div>'
             f'<div class="content"><div class="beat">{titolo}</div>{badge_html}{visual_html}'
             f'<div class="body" style="margin-top:22px">{body}</div></div>'
             f'<div class="foot">{dots(idx, total)}<div class="handle">@wulver.ai</div></div>')
    return stage(bg, inner)

# --- slide 2: contesto, i due loghi affiancati ---
def contesto():
    vs = (f'<div style="align-self:center;margin-top:30px;display:flex;align-items:center;gap:40px">'
          f'<div style="display:flex;flex-direction:column;align-items:center;gap:12px">'
          f'<img src="data:image/png;base64,{LC}" style="height:150px;width:150px;object-fit:contain">'
          f'<span style="font-family:\'Space Grotesk\';font-weight:700;font-size:30px;color:{ORANGE}">Claude</span></div>'
          f'<span style="font-family:\'Space Grotesk\';font-weight:700;font-size:44px;color:#9DB6A6">vs</span>'
          f'<div style="display:flex;flex-direction:column;align-items:center;gap:12px">'
          f'<img src="data:image/png;base64,{LG}" style="height:150px;width:150px;object-fit:contain">'
          f'<span style="font-family:\'Space Grotesk\';font-weight:700;font-size:30px;color:{GREEN}">ChatGPT</span></div></div>')
    body = ("Non esiste un vincitore assoluto: sono entrambi ottimi, ma danno il meglio in situazioni diverse. Ti mostro quando "
            "conviene l'uno e quando l'altro. (La famiglia GPT pi&ugrave; nuova, la 5.6, &egrave; ancora in test riservato: oggi usare GPT "
            "significa il ChatGPT normale.)")
    inner = (f'<div class="eyebrow"><span class="d"></span>{EYE}</div>'
             f'<div class="content"><div class="beat">Claude o ChatGPT? Dipende</div>{vs}'
             f'<div class="body" style="margin-top:30px">{body}</div></div>'
             f'<div class="foot">{dots(1, 9)}<div class="handle">@wulver.ai</div></div>')
    return stage(grid, inner)

# --- slide 8: sintesi due colonne con loghi ---
def sintesi():
    col = (f'<div style="display:flex;gap:26px;margin-top:4px">'
           f'<div style="flex:1"><div style="display:flex;align-items:center;gap:10px;margin-bottom:12px">'
           f'<img src="data:image/png;base64,{LC}" style="height:40px;width:40px"><span style="font-family:\'Space Grotesk\';font-weight:700;font-size:29px;color:{ORANGE}">Claude</span></div>'
           f'<div style="font-family:\'Inter\';font-size:25px;line-height:1.5;color:#EAF0EC">volumi e costi<br>codice pulito<br>collegare i tuoi dati<br>capire documenti</div></div>'
           f'<div style="width:2px;background:rgba(255,122,26,.4)"></div>'
           f'<div style="flex:1"><div style="display:flex;align-items:center;gap:10px;margin-bottom:12px">'
           f'<img src="data:image/png;base64,{LG}" style="height:40px;width:40px"><span style="font-family:\'Space Grotesk\';font-weight:700;font-size:29px;color:{GREEN}">ChatGPT</span></div>'
           f'<div style="font-family:\'Inter\';font-size:25px;line-height:1.5;color:#EAF0EC">partire senza tecnici<br>cercare sul web<br>creare immagini e voce</div></div></div>')
    card = f'<div class="card">{col}</div>'
    body = ("Non &egrave; una gara, &egrave; una cassetta degli attrezzi: molte aziende li usano <span class=\"gr\">entrambi</span>. "
            "E nessun test li confronta davvero testa a testa, quindi la prova migliore resta il tuo caso reale.")
    inner = (f'<div class="eyebrow"><span class="d"></span>{EYE}</div>'
             f'<div class="content"><div class="beat">In due parole</div>{card}'
             f'<div class="body" style="margin-top:22px">{body}</div></div>'
             f'<div class="foot">{dots(7, 9)}<div class="handle">@wulver.ai</div></div>')
    return stage(grid, inner)

BC = badge(LC, "Claude", ORANGE)
BG = badge(LG, "ChatGPT", GREEN)

B3 = ("Assistenza clienti, analisi documenti, automazioni che girano in continuazione: sull'API Claude Sonnet&nbsp;5 costa "
      "<span class=\"or\">circa la met&agrave;</span> del ChatGPT standard. Su grandi volumi, la differenza si vede a fine mese.")
B4 = ("Non hai un tecnico e vuoi solo un'app pronta da usare? ChatGPT ha <span class=\"gr\">pi&ugrave; fasce economiche</span> e "
      "un'interfaccia che gran parte delle persone gi&agrave; conosce. La strada pi&ugrave; semplice per partire.")
B5 = ("Vuoi far lavorare l'AI sui tuoi dati e software, Drive, Slack, il gestionale, in modo controllato? Claude ha "
      "<span class=\"or\">centinaia di connettori pronti</span>, ed &egrave; Anthropic ad aver inventato lo standard.")
B6 = ("Cercare informazioni aggiornate con le fonti, o creare immagini e messaggi vocali: ChatGPT lo fa dentro l'app. Claude "
      "capisce immagini e PDF, ma <span class=\"gr\">non li crea</span>.")
B7 = ("Un assistente che porta a termine un lavoro intero al posto tuo, sistemare file, preparare un documento: Claude ha uno "
      "strumento <span class=\"or\">pensato per chi non programma</span>, che lavora sui tuoi file e ti d&agrave; il risultato pronto.")

# poster frame per i video
import subprocess
def poster(mp4, out):
    subprocess.run(["ffmpeg","-y","-ss","2","-i",mp4,"-frames:v","1",out], check=True, capture_output=True)
    return out
for v in ("volumi","partenza","crea","agente"):
    poster(f"{A}/broll-{v}-6s.mp4", f"{A}/poster-{v}.png")

VOL = b64(f"{A}/poster-volumi.png"); PAR = b64(f"{A}/poster-partenza.png")
CRE = b64(f"{A}/poster-crea.png"); AGE = b64(f"{A}/poster-agente.png")
COL = b64(f"{A}/img-collega.jpg")

S = {}
S[2] = contesto()
S[3] = usecase(grid, "Per far girare molto lavoro", BC, img_html(VOL), B3, 2)
S[4] = usecase(grid, "Per partire senza sviluppatori", BG, img_html(PAR), B4, 3)
S[5] = usecase(grid, "Per collegare i tuoi strumenti", BC, img_html(COL), B5, 4)
S[6] = usecase(grid, "Per cercare sul web e creare", BG, img_html(CRE), B6, 5)
S[7] = usecase(grid, "Per automazioni, anche senza essere tecnico", BC, img_html(AGE), B7, 6)
S[8] = sintesi()
S[9] = stage(grid,
    f'<img class="founder" src="data:image/png;base64,{FND}">'
    f'<div class="eyebrow"><span class="d"></span>{EYE}</div>'
    f'<div class="cta-c"><div class="beat wh">Quale usare per cosa?</div>'
    f'<div class="sub" style="margin-top:20px">Commenta SCEGLI e ti invio una checklist pratica: per ogni compito tipico di una piccola azienda, quale dei due conviene. Cos&igrave; scegli in un minuto, senza doverli provare tutti e due.</div>'
    f'<div class="pill">Commenta SCEGLI</div></div>'
    f'<div class="foot" style="right:auto">{dots(8, 9)}</div>')

for n, html in S.items():
    render(html, f"{HERE}/slide-{n}.png")
    print("rendered slide", n)

# --- compositing video nelle slide 3,4,6,7 (b-roll) ---
BLACK = f"{A}/_black.png"; Image.new("RGB",(1080,1350),(0,0,0)).save(BLACK)
black_b64 = b64(BLACK)
NEU = ('<style>.eyebrow,.eyebrow *,.beat,.body,.body *,.handle,.dot,.dot.on,.d{color:#000 !important;'
       'background:#000 !important;box-shadow:none !important;border-color:#000 !important;text-shadow:none !important}</style>')

for n, mp4, titolo, bdg, body in (
    (3, f"{A}/broll-volumi-6s.mp4", "Per far girare molto lavoro", BC, B3),
    (4, f"{A}/broll-partenza-6s.mp4", "Per partire senza sviluppatori", BG, B4),
    (6, f"{A}/broll-crea-6s.mp4", "Per cercare sul web e creare", BG, B6),
    (7, f"{A}/broll-agente-6s.mp4", "Per automazioni, anche senza essere tecnico", BC, B7),
):
    w, h = 1280, 720
    white = f"{A}/_white.png"; Image.new("RGB",(w,h),(255,255,255)).save(white)
    # per il probe: il badge (logo incluso) va NASCOSTO ma con ingombro invariato, cosi' solo
    # l'immagine bianca contribuisce al bounding box; il logo bianco altrimenti falserebbe il rect
    probe_badge = f'<div style="visibility:hidden">{bdg}</div>'
    probe = usecase(black_b64, titolo, probe_badge, img_html(b64(white)), body, n) + NEU
    pp = f"{A}/_probe_{n}.png"; render(probe, pp)
    x, y, pw, ph = probe_rect(pp)
    print(f"slide {n} rect:", x, y, pw, ph)
    out = f"{HERE}/slide-{n}-VIDEO.mp4"
    composite(f"{HERE}/slide-{n}.png", mp4, x, y, pw, ph, 6.0, out, radius=18)
    print(f"slide {n} verify:", verify_confined(out, (x, y, pw, ph)))

print("DONE")
