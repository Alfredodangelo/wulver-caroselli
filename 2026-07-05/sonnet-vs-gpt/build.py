#!/usr/bin/env python3
import sys, os
SKILL = os.path.dirname(os.path.abspath(__file__)) + "/../../../../.claude/skills/carosello-produzione/scripts"
sys.path.insert(0, SKILL)
from slide_kit import b64, stage, slide, card, dots, render, GRID_CLEAN

HERE = os.path.dirname(os.path.abspath(__file__))
FIN = "/Users/alfredo/Desktop/Progetti/Wulver/wulver-social/05-asset/foto/cover-reel"
grid = b64(GRID_CLEAN)
FND = b64(f"{FIN}/reveal-5.png")
EYE = "Wulver &middot; Confronti AI"

# chip neutro (opzione non consigliata per quel caso): grigio, NON barrato
def neutro(txt):
    return (f'<span style="padding:14px 24px;border-radius:14px;font-family:\'Space Grotesk\';font-weight:700;'
            f'font-size:33px;background:rgba(255,255,255,.06);color:#9DB6A6">{txt}</span>')
def orb(txt):
    return f'<span class="chip orb">{txt}</span>'
def vs():
    return '<span style="color:#9DB6A6;font-size:26px;font-family:\'Space Grotesk\';padding:0 4px">vs</span>'

# card confronto: caso in etichetta, i due chip (consigliato arancione + altro neutro), criterio in sub
def cmp_card(caso, consigliato, altro, criterio):
    flow = orb(consigliato) + vs() + neutro(altro)
    return card(caso, flow, criterio)

B2 = ("Prima una cosa onesta: non esiste un vincitore assoluto. Claude e ChatGPT sono entrambi ottimi, ma danno il meglio in "
      "situazioni diverse. Ti mostro quando conviene l'uno e quando l'altro per il lavoro vero di una piccola azienda. "
      "(Nota: la famiglia GPT pi&ugrave; nuova, la 5.6, &egrave; ancora in test riservato, quindi oggi usare GPT significa il ChatGPT normale.)")
B3 = ("Se devi gestire tante richieste al giorno, penso ad assistenza clienti, analisi di documenti, automazioni che girano in "
      "continuazione, il costo di ogni richiesta conta. Sull'API Claude Sonnet&nbsp;5 costa <span class=\"or\">circa la met&agrave;</span> "
      "del ChatGPT standard: a parit&agrave; di lavoro, spendi meno.")
B4 = ("Se non hai un tecnico e vuoi solo un'app pronta da usare, ChatGPT ha <span class=\"or\">pi&ugrave; fasce di abbonamento economiche</span> "
      "e un'interfaccia che gran parte delle persone gi&agrave; conosce. Per mettere l'AI in mano al team senza toccare codice, "
      "&egrave; la strada pi&ugrave; semplice per partire.")
B5 = ("Se vuoi che l'AI lavori sui tuoi dati e sui tuoi software, Google Drive, Slack, il gestionale, Notion, in modo controllato, "
      "Claude ha <span class=\"or\">centinaia di connettori pronti</span>. &Egrave; Anthropic ad aver inventato lo standard con cui oggi "
      "questi strumenti si collegano all'AI.")
B6 = ("Se ti serve cercare informazioni aggiornate con le fonti citate, o creare contenuti come immagini e messaggi vocali, ChatGPT lo "
      "fa dentro l'app. Claude legge e capisce benissimo immagini e PDF, ma <span class=\"or\">non genera immagini n&eacute; parla a voce</span>: "
      "per creare quel tipo di contenuti serve ChatGPT.")
B7 = ("Se sogni un assistente che porti a termine un lavoro intero al posto tuo, sistemare file, preparare un documento, mettere insieme "
      "dati da pi&ugrave; fonti, Claude ha uno strumento pensato <span class=\"or\">apposta per chi non programma</span>, che lavora sul tuo "
      "computer e ti restituisce il risultato pronto.")
B8 = ("Non &egrave; una gara da vincere, &egrave; una cassetta degli attrezzi. Molte aziende finiscono per usarli <span class=\"gr\">entrambi</span>, "
      "ognuno per quello che sa fare meglio. E nessun test li confronta davvero testa a testa: la prova migliore resta il tuo caso reale.")

# card sintesi a due colonne
def sintesi_card():
    col = ('<div style="display:flex;gap:26px;margin-top:4px">'
           '<div style="flex:1">'
           '<div style="font-family:\'Space Grotesk\';font-weight:700;font-size:30px;color:#FF7A1A;margin-bottom:10px">Claude per</div>'
           '<div style="font-family:\'Inter\';font-size:25px;line-height:1.5;color:#EAF0EC">volumi e costi<br>codice pulito<br>collegare i tuoi dati<br>capire documenti</div></div>'
           '<div style="width:2px;background:rgba(255,122,26,.4)"></div>'
           '<div style="flex:1">'
           '<div style="font-family:\'Space Grotesk\';font-weight:700;font-size:30px;color:#5CFC6E;margin-bottom:10px">ChatGPT per</div>'
           '<div style="font-family:\'Inter\';font-size:25px;line-height:1.5;color:#EAF0EC">partire senza tecnici<br>cercare sul web<br>creare immagini e voce</div></div>'
           '</div>')
    return f'<div class="card">{col}</div>'

S = {}
S[2] = slide(grid, "Claude o ChatGPT? Dipende", "", B2, 1, total=9, eyebrow=EYE)
S[3] = slide(grid, "Per far girare molto lavoro",
             cmp_card("COSTO SU GRANDI VOLUMI", "Claude Sonnet&nbsp;5", "ChatGPT", "Sonnet costa circa la met&agrave; via API"), B3, 2, total=9, eyebrow=EYE)
S[4] = slide(grid, "Per partire senza sviluppatori",
             cmp_card("APP PRONTA, PI&Ugrave; FASCE ECONOMICHE", "ChatGPT", "Claude", "Ambiente gi&agrave; conosciuto, piani a basso costo"), B4, 3, total=9, eyebrow=EYE)
S[5] = slide(grid, "Per collegare i tuoi strumenti",
             cmp_card("INTEGRARE I TUOI DATI AZIENDALI", "Claude Sonnet&nbsp;5", "ChatGPT", "Centinaia di connettori (Drive, Slack, CRM)"), B5, 4, total=9, eyebrow=EYE)
S[6] = slide(grid, "Per cercare sul web e creare",
             cmp_card("RICERCA CON FONTI + IMMAGINI E VOCE", "ChatGPT", "Claude", "Claude capisce immagini e PDF, ma non li crea"), B6, 5, total=9, eyebrow=EYE)
S[7] = slide(grid, "Per automazioni, anche senza essere tecnico",
             cmp_card("UN AGENTE CHE LAVORA PER TE", "Claude Sonnet&nbsp;5", "ChatGPT", "Lavora sui tuoi file e ti d&agrave; il risultato finito"), B7, 6, total=9, eyebrow=EYE)
S[8] = slide(grid, "In due parole", sintesi_card(), B8, 7, total=9, eyebrow=EYE)
S[9] = stage(grid,
    f'<img class="founder" src="data:image/png;base64,{FND}">'
    f'<div class="eyebrow"><span class="d"></span>{EYE}</div>'
    f'<div class="cta-c"><div class="beat wh">Quale usare per cosa?</div>'
    f'<div class="sub" style="margin-top:20px">Commenta SCEGLI e ti invio una checklist pratica: per ogni compito tipico di una piccola azienda, quale dei due conviene. Cos&igrave; scegli in un minuto, senza doverli provare tutti e due.</div>'
    f'<div class="pill">Commenta SCEGLI</div></div>'
    f'<div class="foot" style="right:auto">{dots(7, 9)}</div>')

for n, html in S.items():
    render(html, f"{HERE}/slide-{n}.png")
    print("rendered slide", n)
print("DONE")
