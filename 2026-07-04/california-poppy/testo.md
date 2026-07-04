# Carosello "La California assume l'IA" (Poppy / Anthropic)

- **Cover (slide 1):** fatta dall'utente in Canva. **Slide generate:** 2-8.
- **Sfondo:** griglia pulita `grid_slide-2.png` su tutte le slide di contenuto.
- **Angolo:** News AI (news-jacking), variante estesa a 8 slide per dare spazio ai tanti numeri concreti della notizia.

## Visual per slide
- **2** — foto reale del Campidoglio della California di notte (Wikimedia Commons, CC BY-SA 4.0, Frank Schulenburg)
- **3** — scroll-through reale della pagina ufficiale del Governatore (gov.ca.gov), composito nella cornice
- **4** — scroll-through reale della pagina ufficiale CDT su Poppy (cdt.ca.gov/poppy), composito nella cornice
- **5** — card/diagramma: pilota &rarr; rollout statale
- **6** — card/diagramma: "solo Claude" &rarr; "Claude, Gemini, GPT, Nova" (vendor-agnostic)
- **7** — nessuna immagine, solo testo
- **8** — CTA con founder

## Copy

**2 · Uno stato ha assunto l'IA**
Non parliamo di un'azienda che sperimenta un nuovo tool. Parliamo della California, uno stato con quasi 40 milioni di abitanti, che ha appena deciso di usare l'intelligenza artificiale nel lavoro quotidiano dei suoi dipendenti pubblici. L'accordo è vero, è firmato, e i numeri dietro sono più concreti di quanto sembri.

**3 · L'accordo, in breve**
Il 29 giugno il governatore Gavin Newsom ha annunciato una partnership con Anthropic. Agenzie statali, città e contee possono usare Claude con uno sconto del 50%, con in più formazione gratuita per il personale e assistenza tecnica diretta dai team di Anthropic.

**4 · Il primo risultato: Poppy**
Poppy è l'assistente digitale costruito dallo stato per i propri dipendenti, pensato per rispondere alle domande e ai compiti più comuni del lavoro d'ufficio. Il pilota è partito a settembre 2025 con oltre 2.800 dipendenti in 67 dipartimenti diversi, e ora si prepara al rollout su tutto lo stato.

**5 · Non è più un esperimento**
Il rollout completo è già previsto per questo mese. E non è l'unico caso reale: il DMV della California usa Claude per abbassare i tempi di attesa agli sportelli, mentre il dipartimento della sanità, la più grande agenzia Medicaid del paese, lo usa per i flussi di lavoro interni e assistere meglio i beneficiari.

**6 · Un dettaglio poco notato**
Poppy non è un prodotto esclusivo di Anthropic. È stato progettato per funzionare con più modelli AI insieme, non legato a un solo fornitore. Claude ha contribuito al suo sviluppo, ma la scelta dello stato è stata quella di non dipendere da un'azienda sola.

**7 · Cosa significa per te**
Se uno stato con migliaia di dipendenti e procedure complesse è riuscito a passare da pilota a rollout in meno di un anno, una piccola azienda può fare lo stesso molto più in fretta. Non serve un reparto IT dedicato: serve iniziare con lo strumento giusto e una richiesta scritta bene.

**8 · CTA**
Vuoi il tuo assistente interno, senza reparto IT? Scrivi POPPY nei commenti: ti mando in DM un prompt pronto per creare un assistente AI interno con Claude, pensato per una piccola azienda.

## Analisi neuromarketing

| Slide | Leva |
|---|---|
| 2 | Curiosity gap + autorità (uno stato intero, non un'azienda qualunque) |
| 3 | Concretezza (data, nome, percentuale esatti) + prova (screenshot reale della fonte ufficiale) |
| 4 | Concretezza (numeri: 2.800 dipendenti, 67 dipartimenti) + prova (screenshot reale) |
| 5 | Scarsità/recency (rollout "questo mese") + prova sociale (casi d'uso reali DMV, Sanità) |
| 6 | Contrarian-trust (il dettaglio che "in pochi hanno notato": non è un prodotto a marchio unico) |
| 7 | Self-relevance diretta (PMI, non serve reparto IT) |
| 8 | Micro-commitment (commenta una parola, non un'azione complessa) |

## Prompt pronto per la CTA (risorsa da mandare in DM a chi commenta POPPY)

```
Sei l'assistente interno di [nome azienda], un'attività che si occupa di [cosa fa la tua azienda].
Il tuo compito è rispondere alle domande più comuni che ricevono i dipendenti su: orari, procedure
interne, politiche aziendali, contatti utili, e passaggi operativi ricorrenti (es. come richiedere
ferie, come compilare una nota spese, a chi rivolgersi per un problema tecnico).

Regole:
- Rispondi in modo diretto e pratico, senza girarci intorno.
- Se non conosci la risposta esatta o l'informazione richiesta non ti e' stata fornita, dillo
  chiaramente e indica a chi rivolgersi internamente, invece di inventare una risposta.
- Usa un tono professionale ma colloquiale, come un collega esperto che aiuta velocemente.

Ecco le informazioni di base sulla mia azienda che devi conoscere:
[incolla qui: orari, contatti, 5-10 procedure interne piu' comuni, politiche principali]

Da ora in poi, rispondi alle domande dei dipendenti usando SOLO queste informazioni.
```

## Fonti / crediti
- [Governor Newsom announces a first-of-its-kind partnership](https://www.gov.ca.gov/2026/06/29/governor-newsom-announces-a-first-of-its-kind-partnership-providing-anthropic-tools-to-state-agencies-and-improving-services-for-californians/) — comunicato ufficiale, 29 giugno 2026 (screenshot reale in slide 3)
- [Poppy: California's Digital Assistant](https://www.cdt.ca.gov/poppy/) — pagina ufficiale California Department of Technology, conferma 2.800+ dipendenti/67 dipartimenti, pilota dal 29 settembre 2025, rollout luglio 2026, natura vendor-agnostic (screenshot reale in slide 4)
- Foto Campidoglio della California: [California State Capitol during blue hour](https://commons.wikimedia.org/wiki/File:California_State_Capitol_during_blue_hour-3982.jpg), Frank Schulenburg, CC BY-SA 4.0
- Nota su discrepanza minore: StateScoop riporta "2.600+ utenti/66 dipartimenti" invece di "2.800+/67" — usato il dato della fonte ufficiale CDT come primario.
