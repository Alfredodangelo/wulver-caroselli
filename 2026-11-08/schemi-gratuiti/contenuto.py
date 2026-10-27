# -*- coding: utf-8 -*-
"""Carosello: cinque degli schemi gratuiti di wulver.it/risorse (su dodici), uno per slide.

I titoli delle slide in basso sono quelli veri della pagina (Sito/Main/lib/resources.ts).
CTA: link nel profilo, nessuna parola da commentare."""
import os
NOME = "Gli schemi gratuiti di wulver.it"
SEED = 530944

APERTURA = dict(
    scena="standing at a tidy home office desk next to a laptop, one hand open as if presenting "
          "a few printed sheets laid out on the desk, a friendly relaxed smile at the camera, "
          "warm daylight from a window.",
    kicker="Gratis, senza registrarsi",
    titolo="Dodici schemi gratis,<br>{in un posto solo}",
    sotto="Prompt già scritti e schemi da copiare. Te ne faccio vedere cinque, gli altri sette li trovi sulla pagina.",
)

COPPIE = [
    (("at a desk frowning at a laptop showing a messy spreadsheet with misaligned columns, "
      "one hand pressed on his forehead. Dim office, late afternoon.",
      "L'export del gestionale è {un disastro}"),
     ("at the same desk looking at a tidy clean spreadsheet on the laptop with a satisfied nod, "
      "arms relaxed. Bright office, morning light.",
      "{Pulisci l'export Excel} in un colpo")),

    (("at a kitchen table surrounded by crumpled paper receipts and phone photos of receipts, "
      "overwhelmed, rubbing his eyes. Evening, warm lamp.",
      "Ricevute {sparse} dappertutto"),
     ("at the same table with a single neat stack of papers and a phone, relaxed, a small smile. "
      "Morning light, tidy table.",
      "{Ricevute e scansioni} in un PDF")),

    (("at a laptop, shrugging with open hands while reading a vague generic answer on the "
      "screen, unimpressed. Evening desk lamp.",
      "Chiedi all'AI e {risponde a caso}"),
     ("at the same laptop reading a precise answer on the screen with a nod, one finger "
      "raised as if making a point. Morning light.",
      "Lo schema del {prompt perfetto}")),

    (("at a desk in the morning with a phone full of notifications in one hand and a laptop "
      "with a crowded inbox open, stressed expression. Cool morning light.",
      "Posta e agenda {ti mangiano la mattina}"),
     ("at the same desk calmly reviewing a short draft email on the laptop with a coffee in "
      "hand, relaxed. Warm morning light.",
      "{Email e agenda}: le mail restano in bozza")),

    (("at a desk repeating the same task for the umpteenth time, staring at the clock on the "
      "wall with a tired face, a pile of small tasks on a notepad. Late afternoon, flat light.",
      "Sempre {gli stessi giri} ripetitivi"),
     ("leaning back in a chair with arms behind the head, a crossed-off checklist on the desk, "
      "relaxed smile. Bright office, daylight.",
      "{5 task} da toglierti di dosso")),
]

CHIUSURA = dict(
    scena="sitting on a sofa at home in the evening with a phone resting on his knee, looking at "
          "the camera with a relaxed half smile and one hand pointing upward, warm lamp light. "
          "Medium shot.",
    kicker="Link nel profilo",
    titolo="Tutti gratis su<br>{wulver.it/risorse}",
    sotto="Si scaricano senza registrarsi. Salvalo, così lo ritrovi quando ti serve.",
)

DIDASCALIA = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               "_didascalia.txt"), encoding="utf-8").read()
