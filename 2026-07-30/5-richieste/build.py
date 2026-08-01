#!/usr/bin/env python3
"""Carosello LISTA: "Le 5 richieste che valgono un'ora al giorno" — template T2 SFUMATURA, oggetti fusi.
Statico. CTA: azione principale SALVA (formato lista), secondaria COMMENTA PROMPT (pacchetto pronto)."""
import sys, os
SK = os.path.dirname(os.path.abspath(__file__)) + "/../../../../.claude/skills/carosello-produzione/scripts"
sys.path.insert(0, SK)
import slide_kit as sk

HERE = os.path.dirname(os.path.abspath(__file__)); A = f"{HERE}/assets"
G, O, Wt, GD = "#5CFC6E", "#FF7A1A", "#F5F7F5", "#0B7A38"
TOT = 8

def fused(name): return sk.b64(f"{A}/{name}_fused.png")
def hi(t, dark=True): return f'<b style="color:{G if dark else GD};font-weight:600">{t}</b>'
def prompt(txt, dark=True):
    col = "#DCEBE1" if dark else "#25402F"
    return f'<span style="color:{col}">&laquo;{txt}&raquo;</span>'

S = {}

# 2 HOOK (scuro) — clessidra
S[2] = sk.slide_grad(None, "5 richieste pronte", "Un'ora al giorno", "te la riprendi",
    f'Email, preventivi, riassunti: le cose che ti mangiano il tempo le deleghi con una frase. {hi("Queste sono le 5 che uso ogni giorno")}.',
    0, total=TOT, variant="dark", l1_size=80, l2_size=76, l2_indent=30, bg_image=fused('s2-hourglass'))

# 3 P1 (chiaro) — riassumi thread
S[3] = sk.slide_grad(None, "1 &middot; Riassumi", "Il thread", "infinito",
    f'{prompt("Da questo scambio di email dimmi in 5 punti dove siamo e cosa devo decidere io", 0)} {hi("Venti mail in cinque righe",0)}.',
    1, total=TOT, variant="light", l1_size=84, l2_size=86, l2_indent=40, bg_image=fused('s3-funnel'))

# 4 P2 (scuro) — preventivo
S[4] = sk.slide_grad(None, "2 &middot; Trasforma", "Appunti sparsi,", "preventivo pronto",
    f'{prompt("Da questi appunti scrivimi un preventivo ordinato con voci, prezzi e totale, tono professionale")} {hi("Le tue note diventano un documento")}.',
    2, total=TOT, variant="dark", l1_size=80, l2_size=72, l2_indent=30, bg_image=fused('s4-quote'))

# 5 P3 (chiaro) — email difficile
S[5] = sk.slide_grad(None, "3 &middot; Scrivi", "L'email", "difficile",
    f'{prompt("Devo dire a un cliente che [la situazione]: scrivimi un\'email cortese ma ferma, breve, che chiude bene", 0)} {hi("Il no, il sollecito, senza sudare",0)}.',
    3, total=TOT, variant="light", l1_size=84, l2_size=88, l2_indent=50, bg_image=fused('s5-plane'))

# 6 P4 (scuro) — riunione -> cose da fare
S[6] = sk.slide_grad(None, "4 &middot; Estrai", "La riunione,", "in cose da fare",
    f'{prompt("Da questi appunti della riunione tira fuori le cose da fare, chi le fa e le scadenze")} {hi("Chiacchiere in una lista chiara")}.',
    4, total=TOT, variant="dark", l1_size=80, l2_size=74, l2_indent=40, bg_image=fused('s6-clipboard'))

# 7 P5 (chiaro) — reclamo
S[7] = sk.slide_grad(None, "5 &middot; Rispondi", "Il reclamo,", "gestito con calma",
    f'{prompt("Un cliente si lamenta cos&igrave; [incolla]: rispondi con calma, prenditi la responsabilit&agrave; dove serve e proponi una soluzione", 0)}',
    5, total=TOT, variant="light", l1_size=84, l2_size=72, l2_indent=30, bg_image=fused('s7-bubble'))

# 8 NOTA ONESTA (scuro) — penna
S[8] = sk.slide_grad(None, "La parte onesta", "Cambia le [ ]", "e rileggi",
    f'Sono punti di partenza, non da mandare a occhi chiusi. Metti la tua parte tra parentesi e ricontrolla: {hi("il tempo lo risparmi, la firma resta tua")}.',
    6, total=TOT, variant="dark", l1_size=82, l2_size=78, l2_indent=60, bg_image=fused('s8-pen'))

# 9 CTA (scuro) — SALVA primaria, COMMENTA PROMPT secondaria; carte fuse in basso di lato
b9 = fused('s9-cards')
def riga(verbo, testo):
    return (f'<div style="margin-top:22px">'
            f'<span style="font-family:\'Space Grotesk\';font-weight:700;font-size:32px;color:{G};letter-spacing:.03em">{verbo}</span>'
            f'<span style="font-family:\'Inter\';font-weight:400;font-size:26px;line-height:1.35;color:#C9D8CE"> {testo}</span></div>')
_cta = ('<div style="position:absolute;left:82px;top:150px;width:660px;z-index:4">'
    f'<div style="font-family:\'Space Grotesk\';font-weight:600;font-size:27px;letter-spacing:.16em;text-transform:uppercase;color:{O};margin-bottom:16px">Le vuoi tutte e 5</div>'
    f'<div style="font-family:\'Space Grotesk\';font-weight:700;font-size:76px;line-height:.96;letter-spacing:-.03em;color:{Wt};text-shadow:0 2px 20px rgba(0,0,0,.55)">Pronte da<br>incollare?</div>'
    '<div style="display:flex;align-items:center;gap:16px;margin-top:30px">'
      f'<span style="display:inline-block;background:{G};color:#06240f;font-family:\'Space Grotesk\';font-weight:700;'
      f'font-size:46px;padding:9px 30px;border-radius:14px;box-shadow:0 0 34px rgba(92,252,110,.55)">SALVA</span>'
      f'<span style="font-family:\'Space Grotesk\';font-weight:700;font-size:40px;color:{Wt}">il post</span></div>'
    f'<div style="font-family:\'Inter\';font-weight:400;font-size:27px;line-height:1.35;color:#C9D8CE;margin-top:14px;max-width:470px">questa lista la riapri ogni volta che ti serve.</div>'
    '<div style="display:flex;align-items:center;gap:12px;margin-top:26px">'
      f'<span style="font-family:\'Space Grotesk\';font-weight:700;font-size:34px;color:{Wt}">Commenta</span>'
      f'<span style="display:inline-block;background:{G};color:#06240f;font-family:\'Space Grotesk\';font-weight:700;'
      f'font-size:34px;padding:6px 20px;border-radius:12px;box-shadow:0 0 30px rgba(92,252,110,.55)">PROMPT</span></div>'
    f'<div style="font-family:\'Inter\';font-weight:400;font-size:25px;line-height:1.35;color:#C9D8CE;margin-top:8px;max-width:470px">e ti mando le 5 gi&agrave; scritte, con le varianti.</div>'
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
