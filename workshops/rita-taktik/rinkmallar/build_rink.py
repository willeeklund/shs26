"""
Genererar isbane-bilder for rita-taktik-stationerna. Samma ritstil som
workshops/vilken-spelare-vill-du-bli/situationskort/build_rink.py.

Anfallare = röda X. Försvarare = svarta O (samma betydelse genom hela
passet, oavsett vilken station eller vilket lag spelarna representerar
just då - se index.md). Varje scen har alltid en målvakt i vardera målet,
i respektive lags färg (röd M till vänster för anfallarnas eget mål,
svart M till höger för försvararnas mål). Pucken = svart prick.

Vi spelar 3 mot 3, så varje scen har ALLTID exakt 3 anfallare och 3
försvarare totalt - även på "lätt"-scenerna. Svårighetsgraden styrs av
hur många av dem som är nära pucken/aktiva i just den situationen; de
andra är med på isen men placerade längre bort (t.ex. på väg tillbaka
eller inte hunnit med i rusningen än).

Byt positioner i SCENES och kör om (python3 build_rink.py) for att
uppdatera bilderna.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1400, 800
ICE = (235, 245, 250)
LINE = (60, 60, 70)
BLUE_LINE = (30, 80, 170)
RED_LINE = (175, 41, 36)
ATTACKER = (175, 41, 36)
DEFENDER = (30, 30, 30)
GOAL_COLOR = (90, 90, 90)

FONT_PATH_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_PATH = "/System/Library/Fonts/Supplemental/Arial.ttf"


def load_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


font_marker = load_font(FONT_PATH_BOLD, 64)
font_label = load_font(FONT_PATH_BOLD, 30)

MARGIN = 20
BLUE_LINE_1_X = int(W * 0.32)
BLUE_LINE_2_X = int(W * 0.68)
CENTER_X = W // 2
GOAL_W, GOAL_H = 22, 90
GOAL_LEFT_X = MARGIN + 25
GOAL_RIGHT_X = W - MARGIN - 25 - GOAL_W


def new_rink():
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)

    rink_box = [MARGIN, MARGIN, W - MARGIN, H - MARGIN]
    draw.rounded_rectangle(rink_box, radius=90, fill=ICE, outline=LINE, width=6)

    draw.line([(BLUE_LINE_1_X, MARGIN + 10), (BLUE_LINE_1_X, H - MARGIN - 10)], fill=BLUE_LINE, width=10)
    draw.line([(BLUE_LINE_2_X, MARGIN + 10), (BLUE_LINE_2_X, H - MARGIN - 10)], fill=BLUE_LINE, width=10)
    draw.line([(CENTER_X, MARGIN + 10), (CENTER_X, H - MARGIN - 10)], fill=RED_LINE, width=6)

    r = 70
    draw.ellipse([CENTER_X - r, H // 2 - r, CENTER_X + r, H // 2 + r], outline=RED_LINE, width=5)

    draw.rectangle(
        [GOAL_LEFT_X, H // 2 - GOAL_H // 2, GOAL_LEFT_X + GOAL_W, H // 2 + GOAL_H // 2],
        outline=GOAL_COLOR,
        width=6,
    )
    draw.rectangle(
        [GOAL_RIGHT_X, H // 2 - GOAL_H // 2, GOAL_RIGHT_X + GOAL_W, H // 2 + GOAL_H // 2],
        outline=GOAL_COLOR,
        width=6,
    )
    return img, draw


def draw_marker(draw, pos, text, color, label=None, label_offset=(0, 62)):
    x, y = pos
    r = 42
    draw.ellipse([x - r, y - r, x + r, y + r], fill="white", outline=color, width=6)
    bbox = draw.textbbox((0, 0), text, font=font_marker)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text((x - tw / 2 - bbox[0], y - th / 2 - bbox[1]), text, fill=color, font=font_marker)
    if label:
        bbox2 = draw.textbbox((0, 0), label, font=font_label)
        lw = bbox2[2] - bbox2[0]
        draw.text((x - lw / 2, y + label_offset[1]), label, fill=color, font=font_label)


def draw_puck(draw, pos):
    x, y = pos
    r = 14
    draw.ellipse([x - r, y - r, x + r, y + r], fill="black")


def render_scene(filename, attackers, defenders, puck=None):
    img, draw = new_rink()

    # Alltid en målvakt i vardera målet, i respektive lags färg
    draw_marker(draw, (GOAL_LEFT_X + 45, H // 2), "M", ATTACKER)
    draw_marker(draw, (GOAL_RIGHT_X - 45, H // 2), "M", DEFENDER)

    for d in defenders:
        draw_marker(draw, d["pos"], "O", DEFENDER, label=d.get("label"))
    for a in attackers:
        draw_marker(draw, a["pos"], "X", ATTACKER, label=a.get("label"))
    if puck:
        draw_puck(draw, puck)

    img.save(filename)
    print("Sparade", filename, img.size)


SCENES = [
    # --- Del 1: Bästa passningen ---
    dict(
        filename="passning-latt.png",
        # Lätt: en lagkompis helt öppen, en täckt - tydligt val.
        # De två andra försvararna är långt bort och påverkar inte läsningen.
        attackers=[
            {"pos": (480, 410), "label": "DU"},
            {"pos": (750, 200)},  # helt öppen
            {"pos": (750, 600)},  # täckt
        ],
        defenders=[
            {"pos": (615, 505)},  # i passningsvägen mot den nedre lagkompisen
            {"pos": (1050, 250)},  # långt bort, inte inblandad
            {"pos": (1050, 600)},  # långt bort, inte inblandad
        ],
        puck=(500, 400),
    ),
    dict(
        filename="passning-medel.png",
        # Medel: en försvarare tätt i passningsvägen mot en lagkompis (blockerad),
        # den andra lagkompisen är helt öppen. Den tredje försvararen är långt bort.
        attackers=[
            {"pos": (420, 460), "label": "DU"},
            {"pos": (680, 230)},
            {"pos": (760, 560)},
        ],
        defenders=[
            {"pos": (600, 320)},
            {"pos": (560, 610)},
            {"pos": (1050, 430)},  # långt bort, inte inblandad
        ],
        puck=(440, 450),
    ),
    dict(
        filename="passning-svar.png",
        # Svår: tre lagkompisar, tre försvarare tätt i passningsvägarna - alla inblandade
        attackers=[
            {"pos": (380, 480), "label": "DU"},
            {"pos": (650, 200)},
            {"pos": (650, 660)},
        ],
        defenders=[
            {"pos": (515, 340)},
            {"pos": (600, 470)},
            {"pos": (515, 570)},
        ],
        puck=(400, 470),
    ),
    # --- Station 2/3: Anfall (samma bild, olika roll beroende på station) ---
    dict(
        filename="anfall-forsvar-latt.png",
        # Lätt: 2 mot 1 i anfallszon. Tredje anfallaren och två försvarare
        # hänger fortfarande långt bak - inte hunnit med i rusningen.
        attackers=[
            {"pos": (1050, 300)},
            {"pos": (1050, 560)},
            {"pos": (800, 430)},  # långt bak, inte med i rusningen än
        ],
        defenders=[
            {"pos": (1130, 430)},
            {"pos": (650, 250)},  # långt bak, backchecking
            {"pos": (650, 620)},  # långt bak, backchecking
        ],
        puck=(1050, 300),
    ),
    dict(
        filename="anfall-forsvar-medel.png",
        # Medel: 3 mot 2 i anfallszon. Tredje försvararen hinner inte tillbaka i tid.
        attackers=[
            {"pos": (980, 220)},
            {"pos": (1000, 430)},
            {"pos": (980, 640)},
        ],
        defenders=[
            {"pos": (1120, 340)},
            {"pos": (1120, 520)},
            {"pos": (620, 430)},  # hinner inte tillbaka
        ],
        puck=(1000, 430),
    ),
    dict(
        filename="anfall-forsvar-svar.png",
        # Svår: 3 mot 3, men försvararna har klumpat ihop sig upptill (dubbelbevakar
        # de två översta anfallarna) - den nedersta anfallaren står helt fri med
        # öppet skottläge. Något MÅSTE rättas till här, både för anfalls- och
        # försvarsstationen (den tredje försvararen är för långt bort för att hinna).
        attackers=[
            {"pos": (1020, 220)},
            {"pos": (1050, 430)},
            {"pos": (1020, 640)},  # helt fri - ingen försvarare i närheten
        ],
        defenders=[
            {"pos": (1130, 240)},  # tight på översta anfallaren
            {"pos": (1150, 380)},  # har glidit upp och dubbelbevakar mitten/toppen
            {"pos": (1280, 700)},  # för långt bort i hörnet - hinner inte täcka nedre anfallaren
        ],
        puck=(1050, 430),
    ),
]


if __name__ == "__main__":
    for scene in SCENES:
        render_scene(
            scene["filename"],
            scene["attackers"],
            scene["defenders"],
            scene.get("puck"),
        )
