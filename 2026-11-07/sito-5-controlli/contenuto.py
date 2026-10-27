# -*- coding: utf-8 -*-
"""Carosello: cinque controlli al sito di un'attività locale, da fare col telefono in mano.

Per chi ha un negozio, uno studio, un'officina: non tecnico. Niente numeri inventati, solo cose
che si vedono con gli occhi in due minuti. CTA: salvalo e mandalo a chi ha un'attività."""
import os
NOME = "Il tuo sito fa perdere clienti? Cinque controlli"
SEED = 418273

APERTURA = dict(
    scena="sitting at a small cafe table with a coffee, holding a phone in one hand and looking at "
          "the screen with a skeptical frown, as if checking a small local business website, "
          "morning light through the cafe window.",
    kicker="Fallo col telefono in mano",
    titolo="Il tuo sito fa<br>perdere {clienti}?",
    sotto="Cinque controlli da due minuti. Non serve installare niente, basta il cellulare.",
)

COPPIE = [
    (("standing on a sidewalk outdoors holding a phone, looking at a blank screen with a small "
      "loading spinner, impatient, one foot tapping. Overcast daylight, street background.",
      "Il sito ci mette {una vita} ad aprirsi"),
     ("standing on the same sidewalk holding the phone out and looking at a page that has fully "
      "loaded, a small satisfied nod. Overcast daylight, street background.",
      "Aprilo {col 4G}, non col wifi di casa")),

    (("at a desk squinting at a phone, one finger trying to select a tiny phone number on the "
      "screen while the other hand holds a pen over a paper notepad, annoyed. Warm lamp light.",
      "Il numero c'è, ma {non si tocca}"),
     ("holding a phone to the ear with a relaxed smile after tapping a call button, other hand "
      "in a pocket. Bright room, window behind.",
      "Un tocco e {parte la chiamata}")),

    (("standing at night in front of a closed shop with its metal shutter down, looking at his "
      "phone with a puzzled face, no one around. Cold street light, dark street.",
      "Aperto? Boh. Dove? {Boh}"),
     ("walking toward an open shop with warm light glowing from the door, phone in hand, "
      "looking relieved. Evening street, warm window light.",
      "Orari e indirizzo {subito in vista}")),

    (("on a sofa scrolling a phone with a doubtful expression, one eyebrow raised, empty "
      "screen glow on his face. Evening living room, lamp off.",
      "Nessuna recensione, {nessuna fiducia}"),
     ("on the same sofa reading a phone with a small nod and a half smile, lamp on, relaxed "
      "posture. Evening living room.",
      "Mostra {quelle vere}, anche poche")),

    (("overwhelmed, one hand in his hair, staring at a phone screen crowded with many different "
      "colorful buttons, head tilted. Bright office, daylight.",
      "Dieci bottoni e {nessuno chiaro}"),
     ("confidently pressing one big single button on the phone screen with one finger, calm "
      "expression. Bright office, daylight.",
      "{Un solo bottone}: chiama o prenota")),
]

CHIUSURA = dict(
    scena="sitting on a sofa at home in the evening with a phone resting on his knee, looking at "
          "the camera with a relaxed half smile, warm lamp light. Medium shot.",
    kicker="Salvalo",
    titolo="Mandalo a chi ha<br>{un'attività}",
    sotto="Sono cinque cose che si vedono in due minuti. Meglio scoprirle tu che un cliente che non richiama.",
)

DIDASCALIA = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               "_didascalia.txt"), encoding="utf-8").read()
