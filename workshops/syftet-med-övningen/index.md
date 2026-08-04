# Syftet med övningen

🎥 **Presentation:** [Öppna presentationen](https://willeeklund.github.io/shs26/workshops/syftet-med-övningen/presentation/)

Laget lär sig sätta ord på vad varje övning faktiskt tränar upp.

## Mål med passet
Barnen ska själva kunna förklara vad man tränar på i våra övningar - inte bara göra dem. Om de förstår syftet kommer de göra övningarna med rätt fokus även när ingen coachar dem för stunden.

Bilderna på övningarna som Alexandre har ritat och som vi kört under våren finns i mappen ["Enskilda övningar"](Enskilda%20övningar). Originalen (ospäckade helpass) ligger i ["Råmaterial"](Råmaterial).

## Material
- Skriv ut [övningskort](ovningskort/ovningskort.html) **dubbelsidigt** (long-edge-vändning) - 4 övningar per A4-sida i ett 2x2-rutnät, klipp isär i fyra kvadranter efter utskrift. Framsidan är Alexandres ritning utan pyssel runt om (bilden fyller kvadranten), baksidan har två korta fält: "Namn på övningen" och "Vad tränar vi?" (laminera gärna, de kan återanvändas varje år)
- Ge varje grupp 2-3 kort

### Bygga om övningskorten
Om bilderna i ["Enskilda övningar"](Enskilda%20övningar) uppdateras, kör om genereringsskriptet så plockas ändringarna upp automatiskt:
```
cd ovningskort
python3 build_html.py
```

## Upplägg (ca 20-25 min)
1. **Introduktion (2 min):** Samla laget. Förklara kort: "Ni har blivit övningsdetektiver! Varje övning vi kör har en hemlighet - vad den egentligen tränar upp. Idag gör vi om Alexandres ritningar till egna övningskort, som ett hockeykort fast för övningar. Framsidan är redan klar - ni ska lösa gåtan och skriva klart baksidan."
2. **Gruppindelning (2 min):** Dela in i smågrupper om 3-4 spelare. Ge varje grupp 2-3 bilder på övningar.
3. **Lös gåtan och skriv klart kortet (10 min):** Grupperna tittar på sina bilder och pratar ihop sig om vad man tränar. På baksidan av varje bild skriver de sedan:
   - **Vad man tränar** (kika på nyckelorden nedan om de kör fast)
   - **Ett eget häftigt namn** på övningen - ju roligare desto bättre
4. **Redovisning (8-10 min):** Varje grupp visar upp sitt övningskort och presenterar det för resten av laget: namnet de gett den, vad de kom fram till att man tränar - och numret (#NN) som står på kortet. Skriv in det numret i presentationen och tryck Enter så hoppar den direkt till bilden på just den övningen, så alla ser vad gruppen pratar om. Fyll på om de missat något syfte.

## Hjälpfrågor till grupperna
- Vad gör spelaren i bilden - steg för steg?
- Vilken sak blir du bäst på om du övar den här jättemycket?
- När i en match skulle du ha nytta av det du tränar här?
- Är det något som är svårast i övningen? Vad tror ni det tränar upp?

## Nyckelord om de kör fast
De flesta övningarna har flera syften samtidigt. Om grupperna har svårt att sätta ord på det, hjälp dem med enkla nyckelord:
- **Skridskoåkning** - åka snabbt, bromsa, byta riktning
- **Klubbhantering** - ha kvar pucken på klubban, dribbla
- **Passningar** - passa och ta emot pucken
- **Titta upp** - se var lagkompisar och motståndare är utan att titta ner i pucken
- **1 mot 1 anfall** - ta sig förbi en motståndare
- **1 mot 1 försvar** - ta pucken eller stänga vinkeln mot en anfallare
- **Avslut** - skjuta på mål
- **Samarbete** - hitta öppna ytor, spela med varandra (t ex "give and go")
- **Speluppfattning** - förstå vad som händer i ett litet spel (t ex 3 mot 3)

## Extrapoäng
- Kan de komma på "nästa nivå" av övningen? Vi gör ofta en enklare variant först som senare byggs på med ett till moment för att göra den svårare. Fråga muntligt vid redovisningen - det finns inget skrivfält för det på kortet (de är 10 år, korten är medvetet korta).
- Spara korten! Namnen laget kommer på blir sedan de riktiga namnen vi använder på träningarna - lätt att ropa ut utan att behöva visa varje gång.

## TODO
- [x] Skapa övningskort - se [ovningskort/ovningskort.html](ovningskort/ovningskort.html), dubbelsidigt, 4 övningar per A4-sida (7 sidpar / 14 sidor totalt för alla 25 övningarna).
- [ ] Skriv ut, klipp isär raderna och laminera övningskorten inför passet. Varje grupp ska ha 2-3 kort.
- [ ] Bestäm gruppindelning i förväg (blandade nivåer i varje grupp brukar fungera bra)
