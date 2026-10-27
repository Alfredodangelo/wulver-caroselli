# -*- coding: utf-8 -*-
"""Carosello: video vero o fatto con l'AI? Quattro segnali e un avviso onesto.

Per il pubblico largo, pensato per essere salvato e girato a chi condivide tutto.
Linea editoriale: nessun segnale da solo e' una prova, e i rilevatori online sbagliano. Quindi
niente trucchi da detective: domande da farsi prima di girare un video. Fatti generici e
verificabili, nessuna cifra inventata."""
import os
NOME = "Video vero o fatto con l'AI"
SEED = 311872

APERTURA = dict(
    scena="sitting on a sofa at home in the evening looking at a phone with a puzzled frown, one "
          "eyebrow raised, the screen light on his face, a half finished cup beside him. Warm lamp, "
          "dim living room.",
    kicker="Prima di girarlo",
    titolo="Quel video è {vero}<br>o l'ha fatto<br>un'AI?",
    sotto="Quattro domande da farti prima di mandarlo a tutti. E una cosa onesta alla fine.",
)

COPPIE = [
    (("standing in a kitchen holding a phone, thumb already hovering over the share button, "
      "reading a shocking video caption quickly, hurried posture. Morning light.",
      "Ti arriva in chat e {lo giri subito}"),
     ("sitting at a table with a laptop open, searching with a focused look to find who posted the "
      "video first, notes beside him. Calm afternoon light.",
      "Prima cerchi {chi l'ha pubblicato per primo}")),

    (("close up of him holding a phone at arm's length squinting at it, trying to spot something "
      "odd on the screen, tilted head. Cool daylight by a window.",
      "Controlli {mani e dettagli} e ti fidi"),
     ("at a desk pausing a video on a laptop and pointing at a corner of the screen, comparing "
      "two frames, careful expression. Evening lamp.",
      "Guardi anche {scritte e oggetti} fra un taglio e l'altro")),

    (("sitting on a train looking at a very short looping clip on his phone, headphones around "
      "the neck, a slightly bored look. Passing landscape, flat light.",
      "Dura {otto secondi} e non ha un prima"),
     ("sitting at a desk with two browser windows open, searching for a longer version of the "
      "same clip, leaning toward the screen. Neutral office light.",
      "Cerchi {la versione lunga} o l'altra inquadratura")),

    (("standing in the hallway reading a video on his phone with a clenched jaw, shoulders "
      "tense, clearly angry. Harsh overhead light.",
      "Ti fa {arrabbiare} in cinque secondi"),
     ("sitting by a window with the phone face down on the table, taking a slow breath with eyes "
      "closed, relaxed shoulders. Soft morning light.",
      "È proprio il momento di {aspettare}")),

    (("at a desk with a laptop, pointing at a single small detail on the screen with a triumphant "
      "look, a sticky note saying nothing readable. Warm lamp, evening.",
      "Trovi {un dettaglio strano} e decidi: è finto"),
     ("sitting back in the chair with arms crossed and a thoughtful half smile, looking at the "
      "camera, the screen behind him. Soft light.",
      "Un segnale {non è una prova}: contano insieme")),
]

CHIUSURA = dict(
    scena="sitting on the edge of a desk facing the camera holding a phone in one hand, calm and "
          "direct, a friendly half smile, tidy office in warm late light behind him. Medium shot.",
    kicker="Salvalo",
    titolo="Mandalo a chi {gira tutto}<br>senza controllare",
    sotto="Nessun rilevatore online è sicuro: se ti dice 90% finto, può sbagliare. Le domande valgono più del verdetto.",
)

DIDASCALIA = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               "_didascalia.txt"), encoding="utf-8").read()
