# AGENT INSTRUKTIONER

## Målgrupp & ton
Målgruppen för presentationerna och workshoparna vi skapar här är 10-åriga killar som spelar ishockey. Språket måste vara lätt att följa, positivt och gärna med emoji.

## Grundfilosofi
Detta genomsyrar allt vi skapar: vi jobbar tillsammans för att UPPTÄCKA och LÄRA - vi ska inte bara lyssna på teori. Varje workshop ska vara interaktiv (smågrupper, diskussion, rit-övningar, QR-filmer) istället för en lång envägsgenomgång.

## Webbsidans struktur - en enda källa att redigera
- `README.md` är den enda källan för webbsidans innehåll (rubriker, pitch, listan över workshops med länkar).
- Root-`index.html` hämtar och renderar `README.md` automatiskt vid sidladdning (via `fetch()` + `marked.js`). Den filen ska ALDRIG innehålla hårdkodat listinnehåll, bara den gemensamma stilmallen/headern - annars får vi två ställen att hålla i synk igen.
- `workshops/index.md` är en parallell, mer detaljerad översikt för den som bläddrar i källkoden på GitHub.
- Se till att `README.md` och `workshops/index.md` hålls uppdaterade när vi skapar en ny workshop eller en presentation till en workshop.
- Mappen heter `workshops/` (inte `teoripass/`).
- Testa `index.html`-ändringar med en lokal webbserver (`python3 -m http.server`), inte `file://` direkt - `fetch()` av lokala filer blockeras annars av webbläsaren.

## Presentationer (grafisk-profil/templates)
- Kopiera `presentation-template.html`, följ `grafisk-profil/templates/README.md`.
- Max en rubrik + 1-3 korta rader/punkter per bild, gärna emoji.
- Första och sista bilden röd (`slide-red`), men undvik två röda bilder i följd (bryter flödet).
- `.card-grid` för korta saker (2-4 kort funkar, designat för tre), `.steps` för numrerad instruktion.
- Verifiera alltid visuellt med en skärmdump (headless Chrome) innan en presentation eller ändring anses klar - gissa inte att layouten ser bra ut.

## Utskrivbart material (situationskort, uppdragskort, etc.)
- Bygg som HTML + spara ett Python-script (`build_html.py`) i samma mapp som genererar det - inte bara den färdiga filen. Då går det snabbt att iterera på text/innehåll senare.
- Generera PDF från HTML med headless Chrome: `--headless --print-to-pdf`.
- QR-koder: generera med `qrcode`-biblioteket via ett sparat `build_qr.py`, och länka till GitHub Pages-URL:er (inte `raw`/`blob`-länkar på GitHub) - de går att öppna direkt i webbläsaren/telefonen.
- Isbane-diagram: enkla symboler - röd `X` för eget lag, svart `O` för motståndare, svart prick för puck, inringad `M` i rätt lagfärg för målvakter. Bygg med Pillow (`build_rink.py`), definiera varje scen som data (positioner i en lista) så det är lätt att lägga till/ändra scener. Håll koll på spelarantal (var explicit, t.ex. alltid 3 mot 3 utespelare om inget annat sägs) och kontrollera avstånd mellan markörer så inget överlappar.

## Workshop-upplägg
- Smågrupper om 4-5 spelare är standardstorleken.
- Situationskort med diskussionsfrågor - ibland kompletterat med en rit-uppgift.
- "Bli experter"-modellen fungerar bra: varje grupp blir expert på en del och lär sedan ut till resten av laget.
- Avsluta gärna med att laget gemensamt väljer EN konkret, positiv grej att testa framåt.

## Språk och text
- Dubbelkolla syftningar så det är entydigt vem som gör vad (t.ex. "en försvarare är mellan dig och pucken" - inte "mellan pucken och en försvarare", som är tvetydigt om perspektivet inte är glasklart).
- Undvik löpande numrering i listor som kräver manuellt underhåll varje gång något läggs till/tas bort - använd punktlistor om den exakta ordningen inte har betydelse.

## Git
- Committa eller pusha ALDRIG själv - lämna ändringar redo för användaren att granska och committa. Detta gäller alltid, oavsett vad som verkar bekvämt för stunden.
- Repot är publikt och GitHub Pages är aktiverat (deploy från `main`, root).
