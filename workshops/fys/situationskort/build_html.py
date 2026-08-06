#!/usr/bin/env python3
"""
Genererar situationskort.html - dubbelsidiga situationskort for "Fystraning".
3 situationer per A4-sida i tre vagratta remsor (en remsa = ett kort till en
grupp). Framsidan visar EN bild per situation (fler bilder i samma remsa blir
suddiga/for smatt), baksidan har ifyllningsfalt for grupperna.

Eftersom varje remsa spanner HELA sidans bredd behovs ingen spegelvandning av
baksidan vid dubbelsidig utskrift - ordningen uppifran och ner blir ratt bade
fore och efter att pappret vants (till skillnad fran ett rutnat med flera
kolumner, dar vanster/hoger annars hade hamnat fel).

Kor: python3 build_html.py
"""

IMG_DIR = "../bilder"
OUTPUT = "situationskort.html"

situations = [
    {
        "num": 1,
        "name": "Skydda pucken i hörnet",
        "image": "situation1-hornet-1.jpg",
    },
    {
        "num": 2,
        "name": "Första tre skären mot en lös puck",
        "image": "situation2-losPuck-1.png",
    },
    {
        "num": 3,
        "name": "Orka spela i låg hockeyposition",
        "image": "situation3-lagPosition-3.jpg",
    },
    {
        "num": 4,
        "name": "Hårdare handledsskott",
        "image": "situation4-handledsskott-1.jpg",
    },
    {
        "num": 5,
        "name": "Komma upp snabbt efter ett fall",
        "image": "situation5-uppresning-1.jpg",
    },
    {
        "num": 6,
        "name": "Sidledsförflyttning när man dribblar",
        "image": "situation6-sidled-1.jpg",
    },
]

PER_PAGE = 3


def chunk(items, size):
    groups = []
    for i in range(0, len(items), size):
        group = items[i:i + size]
        while len(group) < size:
            group.append(None)
        groups.append(group)
    return groups


def front_strip(situation):
    if situation is None:
        return '<div class="strip front empty"></div>'
    return f"""<div class="strip front">
        <div class="situation-badge">{situation['num']} · {situation['name']}</div>
        <img src="{IMG_DIR}/{situation['image']}" alt="{situation['name']}" />
      </div>"""


def back_strip(situation):
    if situation is None:
        return '<div class="strip back empty"></div>'
    return f"""<div class="strip back">
        <div class="back-badge">{situation['num']} · {situation['name']}</div>
        <div class="back-fields">
          <div class="mini-field grow">
            <label>Vilka kroppsdelar och egenskaper hjälper?</label>
            <div class="mini-lines"></div>
          </div>
          <div class="mini-field grow">
            <label>Förslag på övning</label>
            <div class="mini-lines"></div>
          </div>
        </div>
      </div>"""


def front_page(group):
    strips = "\n      ".join(front_strip(s) for s in group)
    return f"""
  <div class="page">
      {strips}
  </div>"""


def back_page(group):
    strips = "\n      ".join(back_strip(s) for s in group)
    return f"""
  <div class="page">
      {strips}
  </div>"""


PAGE_TEMPLATE = """<!doctype html>
<html lang="sv">
<head>
<meta charset="UTF-8" />
<title>Fysträning – situationskort</title>
<style>
  @page {{ size: A4; margin: 0; }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    font-family: -apple-system, "Helvetica Neue", Arial, sans-serif;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
    background: #e5e5e5;
  }}

  .toolbar {{
    text-align: center;
    padding: 14px;
  }}
  .toolbar button {{
    font-size: 16px;
    padding: 10px 20px;
    border-radius: 8px;
    border: none;
    background: #1a1a1a;
    color: white;
    cursor: pointer;
  }}
  .toolbar p {{
    max-width: 62ch;
    margin: 8px auto 0;
    color: #444;
    font-size: 13px;
  }}

  .page {{
    width: 210mm;
    height: 297mm;
    margin: 0 auto 20px;
    padding: 4mm;
    background: white;
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: repeat(3, 1fr);
    gap: 0;
    page-break-after: always;
  }}
  .page:last-child {{ page-break-after: auto; }}

  .strip {{
    position: relative;
    overflow: hidden;
    border-bottom: 1px dashed #bbb;
  }}
  .strip:last-child {{ border-bottom: none; }}

  /* --- Framsida: EN bild per situation, fyller hela remsan --- */
  .strip.front {{
    padding: 2mm;
    display: flex;
  }}
  .strip.front img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 2mm;
    display: block;
  }}
  .situation-badge {{
    position: absolute;
    top: 4mm;
    left: 50%;
    transform: translateX(-50%);
    background: #AF2924;
    color: white;
    padding: 1.2mm 4mm;
    border-radius: 999px;
    font-weight: 700;
    font-size: 3.4mm;
    box-shadow: 0 1mm 2mm rgba(0, 0, 0, 0.35);
    z-index: 5;
    white-space: nowrap;
    max-width: 90%;
    overflow: hidden;
    text-overflow: ellipsis;
  }}

  /* --- Baksida: rubrik + tva ifyllningsfalt sida vid sida --- */
  .strip.back {{
    display: flex;
    flex-direction: column;
    padding: 5mm 8mm;
    gap: 3mm;
  }}
  .back-badge {{
    flex: none;
    font-weight: 700;
    font-size: 4.2mm;
    color: #AF2924;
  }}
  .back-fields {{
    flex: 1;
    display: flex;
    gap: 8mm;
    min-height: 0;
  }}
  .mini-field label {{
    display: block;
    font-size: 3.4mm;
    font-weight: 700;
    color: #221615;
    margin-bottom: 2mm;
  }}
  .mini-field.grow {{
    flex: 1;
    display: flex;
    flex-direction: column;
    min-height: 0;
  }}
  .mini-field.grow .mini-lines {{
    flex: 1;
    background-image: repeating-linear-gradient(
      to bottom,
      transparent,
      transparent 8.7mm,
      #999 8.7mm,
      #999 9mm
    );
  }}

  @media print {{
    body {{ background: white; }}
    .toolbar {{ display: none; }}
    .page {{ box-shadow: none; margin: 0; }}
  }}
</style>
</head>
<body>

  <div class="toolbar">
    <button onclick="window.print()">Skriv ut</button>
    <p>Skriv ut dubbelsidigt med "long-edge"-vändning (standard för stående dokument), klipp sedan
       isär i 3 remsor per sida - en situation per grupp.</p>
  </div>
{pages}
</body>
</html>
"""


def main():
    groups = chunk(situations, PER_PAGE)

    pages = []
    for group in groups:
        pages.append(front_page(group))
        pages.append(back_page(group))

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(PAGE_TEMPLATE.format(pages="\n".join(pages)))

    print(f"Skrev {OUTPUT}: {len(situations)} situationer på {len(groups)} sidpar "
          f"({len(groups) * 2} A4-sidor totalt, 3 remsor/sida)")


if __name__ == "__main__":
    main()
