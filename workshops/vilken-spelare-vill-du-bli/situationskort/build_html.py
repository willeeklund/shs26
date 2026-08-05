"""
Bygger situationskort.html (8 kort per A4-sida) utifrån listan
`situations` nedan. Kör om (python3 build_html.py) efter att du ändrat
text eller lagt till/tagit bort situationer. Kör build_rink.py forst
om du andrar nagon rit-scen, sa bilderna ar uppdaterade.
"""

situations = [
    # --- På isen ---
    {"category": "isen", "text": "Din lagkompis missar ett öppet mål i en match. Vad gör du?"},
    {"category": "isen", "text": "Ni ligger under i en match och det börjar kännas tungt i laget. Vad kan du säga eller göra?"},
    {"category": "isen", "text": "En ny spelare är med på träningen för första gången och verkar osäker. Vad gör du?"},
    {"category": "isen", "text": "Domaren blåser en straff mot dig som du tycker är helt fel. Hur reagerar du?"},
    {"category": "isen", "text": "Du har inte fått spela så mycket i matchen som du hoppats på. Vad gör du?"},
    {"category": "isen", "text": "Du har precis passat pucken till en lagkompis. Vad gör du direkt efteråt?"},
    {"category": "isen", "text": "Motståndarna tar pucken från er. Vad gör du på en gång?"},
    {"category": "isen", "text": "Du gör ett misstag som leder till att motståndarna gör mål. Vad gör du direkt efteråt?"},
    {"category": "isen", "text": "En lagkompis blir arg och skäller på en annan lagkompis efter ett misstag. Vad gör du?"},
    {"category": "isen", "text": "Ni vinner stort och matchen är i praktiken redan avgjord. Hur väljer du att spela sista minuterna?"},
    {"category": "isen", "text": "Du blir hårt tacklad (helt inom reglerna) och det gör ont. Hur reagerar du?"},
    {"category": "isen", "text": "Tränaren byter ut dig mitt i en period du kände dig riktigt bra. Vad gör du på bänken?"},
    {"category": "isen", "text": "En motståndare retas eller är taskig mot dig. Hur reagerar du?"},
    # --- Rita-situationer (på isen) ---
    {
        "category": "isen",
        "text": "Motståndarna har precis tagit pucken vid mittlinjen och är på väg mot ert mål.",
        "draw": True,
        "draw_instruction": "✏️ Rita: vart åker DU i försvar?",
        "image": "rink-jobba-hem.png",
    },
    {
        "category": "isen",
        "text": "En lagkompis har pucken vid kanten, men ingen är riktigt öppen för passning.",
        "draw": True,
        "draw_instruction": "✏️ Rita: vart åker DU för att bli spelbar?",
        "image": "rink-bli-spelbar.png",
    },
    {
        "category": "isen",
        "text": "En lagkompis pressar puckbäraren i er egen zon - en motståndare blir öppen framför mål.",
        "draw": True,
        "draw_instruction": "✏️ Rita: vart åker DU för att täcka?",
        "image": "rink-hjalp-forsvar.png",
    },
    {
        "category": "isen",
        "text": "Laget har pucken djupt i anfallszonen, men DU står för högt för att stötta.",
        "draw": True,
        "draw_instruction": "✏️ Rita: vart åker DU för att stötta?",
        "image": "rink-stotta-anfall.png",
    },
    {
        "category": "isen",
        "text": "Din medback pinchar längs kanten i anfallszon - om motståndarna får pucken kan det bli kontring.",
        "draw": True,
        "draw_instruction": "✏️ Rita: vart åker DU för att täcka mitten?",
        "image": "rink-tacka-pinch.png",
    },
    # --- Utanför isen ---
    {"category": "utanfor", "text": "I omklädningsrummet har någon glömt en del av sin utrustning hemma. Vad gör laget?"},
    {"category": "utanfor", "text": "Ni åker buss eller bil till en bortamatch och en spelare sitter ensam. Vad gör du?"},
    {"category": "utanfor", "text": "Du ser att en lagkompis blir retad av någon annan i skolan. Vad gör du?"},
    {"category": "utanfor", "text": "En förälder ropar väldigt högt från läktaren och det känns jobbigt för spelaren det gäller. Hur pratar ni om det i laget?"},
    {"category": "utanfor", "text": "Du är inte alls sugen på att göra styrke- eller konditionsövningar (off-ice) en viss dag. Hur märks det på dig?"},
    {"category": "utanfor", "text": "Ni kör landträning och övningen känns tråkig eller för lätt. Hur visar du att du ändå är med fullt ut?"},
]

CATEGORY_LABEL = {
    "isen": "🏒 På isen",
    "utanfor": "🏠 Utanför isen",
}


def render_card(s):
    label = CATEGORY_LABEL[s["category"]]
    if s.get("draw"):
        body = f"""
      <p class="situation-text">{s['text']}</p>
      <img class="rink" src="{s['image']}" alt="Diagram av isbanan för rit-uppgiften" />
      <p class="draw-instruction">{s['draw_instruction']}</p>
        """
    else:
        body = f"""
      <p class="situation-text">{s['text']}</p>
        """
    return f"""
    <div class="card">
      <div class="card-top">
        <span class="category-label">{label}</span>
      </div>
      <div class="card-body">
        {body}
      </div>
    </div>
    """


def render_page(cards):
    return f"""
  <div class="page">
    {''.join(render_card(c) for c in cards)}
  </div>
    """


PER_PAGE = 8
pages_html = []
for i in range(0, len(situations), PER_PAGE):
    pages_html.append(render_page(situations[i:i + PER_PAGE]))

html = f"""<!DOCTYPE html>
<html lang="sv">
<head>
<meta charset="UTF-8" />
<title>Vilken spelare vill du bli? - situationskort</title>
<style>
  @page {{ size: A4; margin: 0; }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    font-family: -apple-system, "Helvetica Neue", Arial, sans-serif;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}
  .page {{
    width: 210mm;
    height: 297mm;
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: repeat(4, 1fr);
    page-break-after: always;
  }}
  .page:last-child {{ page-break-after: auto; }}
  .card {{
    position: relative;
    border: 1px dashed #bbb;
    padding: 4mm 6mm;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    overflow: hidden;
  }}
  .card-top {{
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    flex: none;
  }}
  .category-label {{
    font-size: 3mm;
    color: #999;
    letter-spacing: 0.02em;
  }}
  .card-body {{
    flex: 1;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 0;
  }}
  .situation-text {{
    font-size: 3.6mm;
    line-height: 1.35;
    color: #111;
    margin: 0;
    max-width: 40ch;
  }}
  .rink {{
    width: 50mm;
    height: auto;
    margin: 1.5mm 0;
  }}
  .draw-instruction {{
    font-size: 3.2mm;
    font-weight: 700;
    color: #AF2924;
    margin: 0;
  }}
</style>
</head>
<body>
  {''.join(pages_html)}
</body>
</html>
"""

with open("situationskort.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Skrev situationskort.html med", len(situations), "kort pa", len(pages_html), "sidor")
