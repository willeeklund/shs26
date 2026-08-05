"""
Genererar isbane-bilder for rit-situationskorten. Varje scen nedan i
SCENES blir en egen PNG. Byt ut positioner/etiketter och kör om
scriptet (python3 build_rink.py) for att enkelt uppdatera bilderna.

Egna spelare (Göta) = röda X. Motståndare = svarta O. Målvakter = M,
i respektive lagfärg. Pucken = svart prick. "DU" är spelaren som ska
rita sin egen väg på det utskrivna kortet.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1400, 800
ICE = (235, 245, 250)
LINE = (60, 60, 70)
BLUE_LINE = (30, 80, 170)
RED_LINE = (175, 41, 36)
GOTA_RED = (175, 41, 36)
OPPONENT = (30, 30, 30)
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


def render_scene(filename, own_players, opponents, puck=None):
    img, draw = new_rink()

    # Målvakter i respektive mål (alltid med, i rätt lagfärg)
    draw_marker(draw, (GOAL_LEFT_X + 45, H // 2), "M", GOTA_RED)
    draw_marker(draw, (GOAL_RIGHT_X - 45, H // 2), "M", OPPONENT)

    for opp in opponents:
        draw_marker(draw, opp["pos"], "O", OPPONENT, label=opp.get("label"))
    for own in own_players:
        draw_marker(draw, own["pos"], "X", GOTA_RED, label=own.get("label"))
    if puck:
        draw_puck(draw, puck)

    img.save(filename)
    print("Sparade", filename, img.size)


SCENES = [
    dict(
        filename="rink-jobba-hem.png",
        # 3 mot 3: Motståndarna har precis tagit pucken vid mittlinjen - DU måste jobba hem i försvar
        opponents=[
            {"pos": (640, 300)},
            {"pos": (760, 470)},
            {"pos": (880, 250)},
        ],
        puck=(600, 355),
        own_players=[
            {"pos": (240, 540)},
            {"pos": (520, 520), "label": "DU"},
            {"pos": (1100, 220)},  # tappade pucken, hann högt upp
        ],
    ),
    dict(
        filename="rink-bli-spelbar.png",
        # 3 mot 3: Lagkompis har pucken vid kanten, ingen är spelbar - DU ska hitta en öppen yta
        opponents=[
            {"pos": (620, 190)},
            {"pos": (760, 380)},
            {"pos": (380, 420)},
        ],
        puck=(500, 160),
        own_players=[
            {"pos": (450, 150)},  # puckförande lagkompis
            {"pos": (300, 640)},
            {"pos": (460, 610), "label": "DU"},
        ],
    ),
    dict(
        filename="rink-hjalp-forsvar.png",
        # 3 mot 3: En lagkompis pressar puckbäraren i egen zon - DU ska täcka den öppna motståndaren
        opponents=[
            {"pos": (170, 580)},  # puckbärare i hörnet
            {"pos": (260, 380)},  # öppen och farlig framför mål
            {"pos": (400, 150)},  # trailande motståndare vid blålinjen
        ],
        puck=(150, 605),
        own_players=[
            {"pos": (270, 640)},  # pressar puckbäraren
            {"pos": (400, 650)},
            {"pos": (360, 260), "label": "DU"},
        ],
    ),
    dict(
        filename="rink-stotta-anfall.png",
        # 3 mot 3: Laget har pucken djupt i anfallszon - DU står för högt och stöttar inte
        opponents=[
            {"pos": (1080, 540)},
            {"pos": (1010, 210)},
            {"pos": (1200, 480)},
        ],
        puck=(1170, 650),
        own_players=[
            {"pos": (1150, 640)},  # puckförande lagkompis i hörnet
            {"pos": (1230, 300)},
            {"pos": (900, 130), "label": "DU"},
        ],
    ),
    dict(
        filename="rink-tacka-pinch.png",
        # 3 mot 3: Din medback pinchar längs kanten i anfallszon - DU måste täcka mitten om det blir kontring
        opponents=[
            {"pos": (1000, 640)},  # redo att bryta ut
            {"pos": (760, 400)},
            {"pos": (850, 550)},
        ],
        puck=(1140, 700),
        own_players=[
            {"pos": (1160, 720)},  # medbacken som pinchar
            {"pos": (1240, 250)},
            {"pos": (1100, 150), "label": "DU"},
        ],
    ),
]


if __name__ == "__main__":
    for scene in SCENES:
        render_scene(scene["filename"], scene["own_players"], scene["opponents"], scene.get("puck"))
