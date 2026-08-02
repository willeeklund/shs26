# Presentationsmall – IK Göta

Delad mall för HTML-presentationer av workshoparna i `workshops/`.

## Filer
- `presentation-template.html` – kopiera denna för en ny presentation
- `presentation.css` – delad styling (röd/vit, se `grafisk profil/Grafisk profil IK Göta.md`). Ändra inte per presentation.
- `presentation.js` – navigering (piltangenter, klick, svep, prickar, progressbar). Ändra inte per presentation.

## Ny presentation, steg för steg
1. Kopiera `presentation-template.html` till `workshops/<mapp>/presentation/index.html`
2. Byt `<title>` och innehållet i varje `<section class="slide">`
3. Öppna filen i webbläsaren och bläddra med piltangenter, mellanslag eller prickarna längst ner

## Riktlinjer för innehåll
- Målgrupp: 10-åringar som spelar hockey – enkelt språk, gärna emoji
- Max en rubrik + 1-3 korta rader/punkter per bild
- Första och sista bilden: röd (`class="slide slide-red"`) med logga
- Använd `.card-grid` för tre korta saker, `.steps` för en numrerad instruktion
