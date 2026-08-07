"""
Bygger rinkmallar.html - varje grupp far ALLA scenarier utskrivna (inte
bara en station), 3 scenarier per A4-sida. Med 9 scenarier totalt blir
det exakt 3 sidor per grupp-paket. Kör build_rink.py forst om du andrar
nagon rit-scen, sa bilderna ar uppdaterade, kor sedan om detta skript.
"""

STATIONS = [
    {
        "title": "Bästa passningen",
        "instruction": "✏️ Rita en pil dit du skulle passa pucken",
        "scenarios": [
            ("Lätt", "passning-latt.png"),
            ("Medel", "passning-medel.png"),
            ("Svår", "passning-svar.png"),
        ],
    },
    {
        "title": "Anfall",
        "instruction": "✏️ Rita var alla anfallare borde åka",
        "scenarios": [
            ("Lätt", "anfall-forsvar-latt.png"),
            ("Medel", "anfall-forsvar-medel.png"),
            ("Svår", "anfall-forsvar-svar.png"),
        ],
    },
    {
        "title": "Försvar",
        "instruction": "✏️ Rita var försvararna borde stå",
        # Samma bilder som del 2 - nu ritar gruppen försvararnas positioner istället
        "scenarios": [
            ("Lätt", "anfall-forsvar-latt.png"),
            ("Medel", "anfall-forsvar-medel.png"),
            ("Svår", "anfall-forsvar-svar.png"),
        ],
    },
]

LEGEND = "⭕ = Försvarare&nbsp;&nbsp;&nbsp;✖️ = Anfallare"


def render_card(number, station, difficulty, image):
    return f"""
    <div class="card">
      <div class="card-top">
        <span class="station-label">#{number} {station['title']}</span>
        <span class="difficulty-label">{difficulty}</span>
      </div>
      <div class="legend">{LEGEND}</div>
      <img class="rink" src="{image}" alt="Isbane-diagram" />
      <p class="instruction">{station['instruction']}</p>
    </div>
    """


def render_page(cards):
    return f"""
  <div class="page">
    {''.join(cards)}
  </div>
    """


cards = []
number = 1
for station in STATIONS:
    for difficulty, image in station["scenarios"]:
        cards.append(render_card(number, station, difficulty, image))
        number += 1

PER_PAGE = 3
pages_html = []
for i in range(0, len(cards), PER_PAGE):
    pages_html.append(render_page(cards[i:i + PER_PAGE]))

html = f"""<!DOCTYPE html>
<html lang="sv">
<head>
<meta charset="UTF-8" />
<title>Rita taktik - rinkmallar</title>
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
    display: flex;
    flex-direction: column;
    page-break-after: always;
  }}
  .page:last-child {{ page-break-after: auto; }}
  .card {{
    position: relative;
    flex: 1;
    min-height: 0;
    border-bottom: 1px dashed #bbb;
    padding: 6mm 12mm;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    overflow: hidden;
  }}
  .card:last-child {{ border-bottom: none; }}
  .card-top {{
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    flex: none;
  }}
  .station-label {{
    font-size: 4mm;
    font-weight: 700;
    color: #AF2924;
  }}
  .difficulty-label {{
    font-size: 3.2mm;
    font-weight: 600;
    color: #999;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }}
  .legend {{
    flex: none;
    font-size: 3mm;
    color: #555;
    margin: 1mm 0;
  }}
  .rink {{
    flex: 1;
    min-height: 0;
    max-width: 92%;
    max-height: 100%;
    object-fit: contain;
    margin: 1.5mm 0;
  }}
  .instruction {{
    flex: none;
    font-size: 3.8mm;
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

with open("rinkmallar.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Skrev rinkmallar.html med", len(cards), "scenarier pa", len(pages_html), "sidor (ett grupp-paket)")
