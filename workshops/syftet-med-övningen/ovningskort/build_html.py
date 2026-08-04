#!/usr/bin/env python3
"""
Genererar ovningskort.html - dubbelsidiga övningskort för "Syftet med övningen".
4 övningar per A4-sida i ett 2x2-rutnät (kvadranter) - använder ytan bättre än
en kolumn med 4 rader, eftersom övningsbilderna har väldigt olika proportioner.

VIKTIGT om dubbelsidig utskrift: vid "long-edge"-vändning (standard för stående
dokument) speglas vänster/höger när man vänder pappret, medan upp/ner är kvar.
Baksidans rutnät är därför medvetet SPEGELVÄNT kolumnvis jämfört med framsidan
(vänster/höger byter plats inom varje rad) - annars hamnar fel baksida bakom
fel övning. Det är avsiktligt att sida 2 i förhandsgranskningen ser "omvänd" ut
jämfört med sida 1 - det är efter fysisk vändning det stämmer.

Kör: python3 build_html.py
"""
import os
import re
import shutil
import unicodedata

SRC_DIR = "../Enskilda övningar"
IMG_DIR = "img"
OUTPUT = "ovningskort.html"


def slugify(name):
    name = unicodedata.normalize("NFC", name.rsplit(".", 1)[0].lower())
    for a, b in {"å": "a", "ä": "a", "ö": "o", "é": "e"}.items():
        name = name.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", name).strip("-")


def collect_cards():
    files = sorted(f for f in os.listdir(SRC_DIR) if f.lower().endswith(".png"))
    os.makedirs(IMG_DIR, exist_ok=True)
    cards = []
    for i, fname in enumerate(files, start=1):
        ext = fname.rsplit(".", 1)[1]
        dest_name = f"{i:02d}-{slugify(fname)}.{ext}"
        shutil.copy(os.path.join(SRC_DIR, fname), os.path.join(IMG_DIR, dest_name))
        cards.append((i, dest_name))
    return cards


def chunk4(items):
    groups = []
    for i in range(0, len(items), 4):
        group = items[i:i + 4]
        while len(group) < 4:
            group.append(None)
        groups.append(group)
    return groups


def mirror_columns(group):
    # 2x2 grid, row-major: [TL, TR, BL, BR] -> swap left/right within each row
    return [group[1], group[0], group[3], group[2]]


def front_quad(card):
    if card is None:
        return '<div class="quad front empty"></div>'
    num, img = card
    return f"""<div class="quad front">
        <img class="quad-img" src="{IMG_DIR}/{img}" alt="Övningsritning" />
        <span class="quad-num">#{num:02d}</span>
      </div>"""


def back_quad(card):
    if card is None:
        return '<div class="quad back empty"></div>'
    num, _ = card
    return f"""<div class="quad back">
        <span class="quad-num">#{num:02d}</span>
        <div class="mini-field name">
          <label>Namn på övningen</label>
          <span class="mini-line"></span>
        </div>
        <div class="mini-field grow">
          <label>Vad tränar vi? (skriv flera saker!)</label>
          <div class="mini-lines"></div>
        </div>
      </div>"""


def front_page(group):
    quads = "\n      ".join(front_quad(c) for c in group)
    return f"""
  <div class="page">
      {quads}
  </div>"""


def back_page(group):
    quads = "\n      ".join(back_quad(c) for c in mirror_columns(group))
    return f"""
  <div class="page">
      {quads}
  </div>"""


PAGE_TEMPLATE = """<!doctype html>
<html lang="sv">
<head>
<meta charset="UTF-8" />
<title>Syftet med övningen – övningskort</title>
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
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr;
    gap: 0;
    page-break-after: always;
  }}
  .page:last-child {{ page-break-after: auto; }}

  /* En enda streckad klipplinje mellan kvadranterna (inget dubbellinje/mellanrum) */
  .quad {{
    position: relative;
    overflow: hidden;
  }}
  .quad:nth-child(1) {{ border-right: 1px dashed #bbb; border-bottom: 1px dashed #bbb; }}
  .quad:nth-child(2) {{ border-bottom: 1px dashed #bbb; }}
  .quad:nth-child(3) {{ border-right: 1px dashed #bbb; }}

  /* --- Framsida: bilden fyller kvadranten, inga extra marginaler --- */
  .quad.front {{
    display: flex;
    align-items: center;
    justify-content: center;
    background: #fff;
  }}
  .quad-img {{
    width: 100%;
    height: 100%;
    object-fit: contain;
  }}

  /* --- Baksida: namn (en rad) + vad vi tränar (flera rader, fyller ytan) --- */
  .quad.back {{
    display: flex;
    flex-direction: column;
    gap: 4mm;
    padding: 6mm;
  }}
  .mini-field label {{
    display: block;
    font-size: 3.6mm;
    font-weight: 700;
    color: #221615;
    margin-bottom: 2mm;
  }}
  .mini-field.name {{
    flex: none;
  }}
  .mini-field .mini-line {{
    display: block;
    border-bottom: 0.4mm solid #999;
    height: 10mm;
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
      transparent 9.7mm,
      #999 9.7mm,
      #999 10mm
    );
  }}

  /* --- Litet kortnummer, för att kunna para ihop lösa kvadranter --- */
  .quad-num {{
    position: absolute;
    top: 1.5mm;
    right: 2mm;
    background: rgba(255, 255, 255, 0.8);
    padding: 0.3mm 1.5mm;
    border-radius: 1mm;
    font-size: 2.6mm;
    color: #777;
  }}
  .quad.back .quad-num {{
    position: static;
    align-self: flex-end;
    background: none;
    padding: 0;
    margin-bottom: -2mm;
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
       isär i 4 kvadranter per sida. Baksidan är avsiktligt spegelvänd vänster/höger i förhandsgranskningen -
       det blir rätt först efter att pappret vänts fysiskt.</p>
  </div>
{pages}
</body>
</html>
"""


def main():
    cards = collect_cards()
    groups = chunk4(cards)

    pages = []
    for group in groups:
        pages.append(front_page(group))
        pages.append(back_page(group))

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(PAGE_TEMPLATE.format(pages="\n".join(pages)))

    print(f"Skrev {OUTPUT}: {len(cards)} övningar på {len(groups)} sidpar "
          f"({len(groups) * 2} A4-sidor totalt, 4 kvadranter/sida)")


if __name__ == "__main__":
    main()
