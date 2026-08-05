# Rita taktik

🎥 **Presentation:** [Öppna presentationen](https://willeeklund.github.io/shs26/workshops/rita-taktik/presentation/)

Laget ritar taktiska lösningar tillsammans - passningsvägar, anfall och försvar.

## Mål med passet
Vi ska se vanliga situationer och rita upp sina lösningar - var är den säkraste passningsvägen, hur rör vi oss tillsammans i anfall och försvar.

Rita var pucken och spelarna borde vara för att det ska bli så bra som möjligt - vid passningar, anfall och försvar.

Cirkel = försvarare, Kryss = anfallare (samma hela passet, så alla hänger med).

## Material
- Skriv ut [rinkmallar](rinkmallar/rinkmallar.html) - varje grupp får ETT paket med alla 9 scenarier (3 per station: lätt/medel/svår), 3 scenarier per A4-sida = 3 sidor per grupp. Samma ritstil som ["Vilken spelare vill du bli?"](../vilken-spelare-vill-du-bli/situationskort/situationskort.html) använder för sina isbane-bilder. Varje scen har alltid 3 anfallare och 3 försvarare (vi spelar 3 mot 3) samt en målvakt i vardera målet, i rätt lagfärg
- Pennor
- Magneter i olika färger, en färg per lag (de som redan finns hemma räcker, se TODO)
- Laminera gärna rink-mallarna så man kan rita med whiteboard-penna och sudda - då kan samma papper användas om och om igen

### Bygga om rinkmallarna
Ändra positioner i `SCENES` i `rinkmallar/build_rink.py`, kör sedan om båda skripten:
```
cd rinkmallar
python3 build_rink.py
python3 build_html.py
```

## Upplägg (ca 20-25 min)
Dela in laget i grupper om 4-5 kompisar. Varje grupp får sitt eget utskrivna paket (alla 9 scenarier) och jobbar igenom passningen → anfall → försvar i sin egen takt, istället för att rotera mellan fysiska stationer i rummet.

### Del 1: Bästa passningen
1. Titta på bilden - var är dina lagkompisar och var är motståndarna?
2. Rita en pil dit du skulle passa pucken.
3. Jämför med de andra i gruppen. Valde ni samma väg? Varför/varför inte?

### Del 2: Anfall
1. Titta på bilden - ni är fler än motståndarna (t ex 2 mot 1).
2. Rita tillsammans var alla anfallare borde åka för att få ett bra skottläge.
3. Prata om: vem har pucken? Vem ropar efter en passning?

### Del 3: Försvar
1. Samma bild, men nu är ni försvarare istället.
2. Rita var försvararna borde stå för att stoppa anfallet.
3. Prata om: vem tar pucken? Vem håller koll på den farligaste motståndaren?

## Visa upp (frivilligt)
Efter stationerna: vill någon grupp visa sin ritning för resten av laget och berätta hur de tänkte? Frivilligt - ingen måste, men peppa den som vågar!

## Hur gör vi det roligt?
- Ge övningarna roliga namn, precis som i ["Syftet med övningen"](../syftet-med-träningen/index.md)
- Gör det till en tävling: vilken grupp hittar flest olika bra lösningar? Inte vem som har "rätt", utan vem som är mest påhittig
- Låt spelarna rita in sig själva med sitt eget tröjnummer istället för ett kryss - känns roligare och mer på riktigt
- Börja enkelt, gör det lite svårare för varje runda (fler motståndare, trängre yta) - som att klara en bana i ett spel

## TODO
[x] Förbered 2-3 färdiga scenarier per station (från lätt till svårare) - se [rinkmallar/rinkmallar.html](rinkmallar/rinkmallar.html)

[ ] Skriv ut/laminera rink-mallar - ett komplett 3-sidigt paket per grupp

[ ] Plocka med magneterna hemifrån i olika färger. Baserat på hur många magneter jag har avgör jag hur många grupper som blir lagom.
