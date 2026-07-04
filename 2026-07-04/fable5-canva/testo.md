# Carosello Fable 5 — versione estesa, divulgativa e coinvolgente

- **Cover (slide 1):** fatta dall'utente in Canva. **Slide generate:** 2-7.
- **Sfondi:** griglia pulita `grid_slide-2.png` su TUTTE le slide di contenuto (2-7), nessuna variante "nebbia" — uniformato su richiesta esplicita dell'utente.
- **Regola video:** si anima SOLO il contenuto dentro la cornice (l'immagine/video), non la slide intera — testo e UI restano fermi.

## Visual per slide
- **2** — immagine AI (concetto server/sparizione, rigenerata senza "schermo dentro lo schermo") + video fal.ai (kling-video, image-to-video) composito nella cornice
- **3** — immagine AI (sfera d'energia dietro le sbarre) + video fal.ai (kling-video, image-to-video) composito nella cornice
- **4** — scroll-through reale della pagina VentureBeat (16:9, cookie-safe, max 6s) composito nella cornice
- **5** — diagramma HTML "Fable 5 → Opus 4.8" (nessun asset esterno)
- **6** — scroll-through reale della pagina ufficiale Anthropic (16:9, cookie-safe, max 6s) composito nella cornice
- **7** — CTA statica con founder

## Copy esteso (per non tecnici, con gancio)

**2 · Fable 5 è tornato online**
C'è un'intelligenza artificiale sparita per una settimana dalla faccia della terra, e quasi nessuno sa perché. Si chiama Fable 5, è il modello più potente costruito da Anthropic, l'azienda dietro Claude, ed è tornato disponibile da pochi giorni. Ma la storia di come è sparito e ricomparso vale la pena conoscerla: dice molto su come funziona davvero l'IA oggi.

**3 · Prima lo bloccano**
Immagina di lanciare un prodotto e vedertelo sequestrare pochi giorni dopo. È successo davvero: alcuni ricercatori avevano scoperto come aggirare i suoi sistemi di sicurezza, e il governo americano ha imposto lo stop in tutto il mondo, non solo in USA. Da un giorno all'altro, un'IA usata da migliaia di aziende si è spenta.

**4 · E poi lo riaccendono**
Poi il colpo di scena: il primo luglio il governo fa marcia indietro e toglie il blocco. Anthropic non se lo fa ripetere due volte: in appena 24 ore rimette tutto online, su Claude, Claude Code e Cowork. Una velocità di reazione quasi senza precedenti.

**5 · Non è più quello di prima**
Qui arriva la parte che in pochi hanno notato. Per essere più sicuro, ora Fable 5 filtra molte più richieste, e quando ne blocca una non te lo dice: la gira in silenzio a un modello più semplice. Pensi di parlare col top di gamma, ma a volte è il fratello minore a risponderti.

**6 · Conviene provarlo adesso**
C'è una finestra comoda per provarlo: fino al 7 luglio è incluso gratis nei piani Pro, Max e Team di Claude, fino a metà del tuo utilizzo settimanale. Dopo quella data si paga extra a consumo. Se sei curioso, questi sono i giorni giusti per farci un giro senza spendere di più.

**7 · CTA**
Vuoi provarlo senza perderci un pomeriggio? Scrivi FABLE nei commenti: ti mando in DM il link diretto e due indicazioni per iniziare, in due minuti.

## Fonti / crediti
- Slide 4: scroll-through reale della pagina VentureBeat. Slide 6: scroll-through reale della pagina ufficiale Anthropic (redeploying-fable-5). Uso editoriale-divulgativo, fonti citate nel copy.
- Notizia: NBC News, MacRumors (blocco/riattivazione governativa), pagina ufficiale Anthropic (riattivazione, finestra gratuita 7 luglio).
- Immagini slide 2/3 generate via OpenArt (Seedream 5 Lite 2K) — generazione avvenuta prima dell'istruzione standing dell'utente di usare sempre fal.ai per le generazioni; i caroselli successivi a questa istruzione usano fal.ai anche per le immagini (vedi skill `carosello-produzione`).
- Video slide 2/3: generati via **fal.ai** (`fal-ai/kling-video/v1.6/standard/image-to-video`), animazione dell'immagine statica corrispondente, composito nella cornice via mask-probe+ffmpeg (nessun altro modello ha completato con successo in questa produzione: un primo tentativo con `fast-svd-lcm` è rimasto bloccato in coda indefinitamente ed è stato abbandonato).
