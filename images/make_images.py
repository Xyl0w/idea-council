"""Draw the three "no Claude Code" diagrams for the Idea Council guide (2 Nov 2026).

    tools/.venv/Scripts/python brand/lead-magnets/idea-council/github/images/make_images.py

Diagrams, not app screenshots (house rule): generic chat cards in the kit's paper palette (src/kit/theme.ts PAPER_*,
clay BRAND). Writes chat-overview.png, chat-round1.png, chat-rounds2-3.png next to this file, 1600x900.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
W, H = 1600, 900
PAPER, CARD, SUNK, RAIL = "#FBF8F3", "#FFFFFF", "#F5EFE7", "#E6DCCF"
TEXT, MUTED, CLAY, CLAY_TEXT = "#1E1916", "#76695F", "#D97757", "#B4532F"
FONTS = Path("C:/Windows/Fonts")


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONTS / name), size)


BLACK = lambda s: font("ariblk.ttf", s)  # noqa: E731
BOLD = lambda s: font("arialbd.ttf", s)  # noqa: E731
BODY = lambda s: font("arial.ttf", s)  # noqa: E731
MONO = lambda s: font("courbd.ttf", s) if (FONTS / "courbd.ttf").exists() else font("cour.ttf", s)  # noqa: E731


def canvas() -> tuple[Image.Image, ImageDraw.ImageDraw]:
    im = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(im)
    for x in range(0, W, 40):  # faint grid paper, like the kit's canvas
        d.line([(x, 0), (x, H)], fill="#F1EBE2", width=1)
    for y in range(0, H, 40):
        d.line([(0, y), (W, y)], fill="#F1EBE2", width=1)
    return im, d


def card(d: ImageDraw.ImageDraw, box, fill=CARD, outline=RAIL, width=3, r=22, shadow=True) -> None:
    x0, y0, x1, y1 = box
    if shadow:
        d.rounded_rectangle((x0 + 6, y0 + 8, x1 + 6, y1 + 8), r, fill="#E9E0D4")
    d.rounded_rectangle(box, r, fill=fill, outline=outline, width=width)


def chat_card(d, x, y, w, h, title, lines, accent=False, badge=None, title_size=20) -> None:
    """A generic chat window: a title bar with three dots, then message bubbles. Not any real app."""
    card(d, (x, y, x + w, y + h), outline=CLAY if accent else RAIL, width=4 if accent else 3)
    d.rounded_rectangle((x, y, x + w, y + 46), 22, fill=SUNK)
    d.rectangle((x, y + 24, x + w, y + 46), fill=SUNK)
    for i in range(3):
        d.ellipse((x + 18 + i * 20, y + 17, x + 30 + i * 20, y + 29), fill=RAIL)
    d.text((x + 86 if title_size >= 20 else x + 78, y + 12 + (20 - title_size) // 2), title, font=BOLD(title_size), fill=TEXT)
    if badge:
        tw = d.textlength(badge, font=BOLD(16))
        d.rounded_rectangle((x + w - tw - 34, y + 11, x + w - 12, y + 35), 12, fill=CLAY)
        d.text((x + w - tw - 23, y + 14), badge, font=BOLD(16), fill="#FFFFFF")
    yy = y + 62
    for who, text in lines:
        f = MONO(17) if who == "mono" else BODY(17)
        tw = d.textlength(text, font=f)
        if who == "you":
            d.rounded_rectangle((x + w - tw - 40, yy, x + w - 14, yy + 34), 14, fill=CLAY)
            d.text((x + w - tw - 27, yy + 7), text, font=f, fill="#FFFFFF")
        else:
            d.rounded_rectangle((x + 14, yy, x + tw + 40, yy + 34), 14, fill=SUNK)
            d.text((x + 27, yy + 7), text, font=f, fill=TEXT)
        yy += 44


def arrow(d, a, b, color=CLAY, width=5) -> None:
    d.line([a, b], fill=color, width=width)
    import math
    ang = math.atan2(b[1] - a[1], b[0] - a[0])
    s = 16
    p1 = (b[0] - s * math.cos(ang - 0.45), b[1] - s * math.sin(ang - 0.45))
    p2 = (b[0] - s * math.cos(ang + 0.45), b[1] - s * math.sin(ang + 0.45))
    d.polygon([b, p1, p2], fill=color)


def heading(d, title, sub) -> None:
    d.text((70, 52), title, font=BLACK(52), fill=TEXT)
    d.text((72, 122), sub, font=BODY(26), fill=MUTED)


def step_label(d, x, y, n, text) -> None:
    d.ellipse((x, y, x + 54, y + 54), fill=CLAY)
    tw = d.textlength(str(n), font=BLACK(28))
    d.text((x + 27 - tw / 2, y + 8), str(n), font=BLACK(28), fill="#FFFFFF")
    d.text((x + 70, y + 10), text, font=BOLD(28), fill=TEXT)


ROLES = ["The Customer", "The Investor", "The Operator", "The Marketer", "Risk & Safety", "The Contrarian", "The Outsider"]


def overview() -> None:
    im, d = canvas()
    heading(d, "The council in a normal chat", "No Claude Code? Nine chats in three rounds, about 15 minutes.")
    # Round 1: seven small chat cards
    step_label(d, 70, 200, 1, "Seven new chats")
    for i in range(7):
        cx, cy = 80 + (i % 2) * 215, 285 + (i // 2) * 135
        if i == 6:
            cx = 80 + 107
        chat_card(d, cx, cy, 200, 115, ROLES[i], [("ai", "VERDICT: …")], title_size=16)
    # Round 2
    arrow(d, (530, 520), (610, 520))
    step_label(d, 620, 200, 2, "One review chat")
    chat_card(d, 630, 300, 380, 300, "Review", [("you", "Answers A–G"), ("ai", "Strongest: C"), ("ai", "Weakest: F"),
                                                 ("ai", "Everyone missed: …"), ("ai", "Changes verdict? no")])
    d.text((640, 625), "Names removed, order shuffled", font=BODY(22), fill=MUTED)
    # Round 3
    arrow(d, (1030, 520), (1110, 520))
    step_label(d, 1120, 200, 3, "One chair chat")
    chat_card(d, 1130, 300, 400, 300, "Chair", [("you", "Idea + answers + review"), ("ai", "Verdict: go with changes"),
                                                ("ai", "Vote: 4 go, 2 change, 1 don't"), ("ai", "Test: …"),
                                                ("ai", "Questions for you: …")], accent=True)
    d.text((1140, 625), "One verdict and one cheap test", font=BODY(22), fill=MUTED)
    im.save(HERE / "chat-overview.png", optimize=True)


def round1() -> None:
    im, d = canvas()
    heading(d, "Round 1: seven advisors, seven new chats",
            "Same idea in every chat, a different role each time. Each one answers alone.")
    card(d, (620, 205, 980, 330), fill=CARD, outline=CLAY, width=4)
    d.text((650, 222), "Your idea", font=BLACK(30), fill=CLAY_TEXT)
    d.text((650, 268), "3–5 lines: what, who, budget,", font=BODY(21), fill=TEXT)
    d.text((650, 296), "time, what success looks like", font=BODY(21), fill=TEXT)
    xs = [40, 265, 490, 715, 940, 1165, 1390]
    for i, role in enumerate(ROLES):
        x = xs[i] - 10
        arrow(d, (800, 335), (x + 105, 455), color="#E3B4A1", width=3)
        chat_card(d, x, 465, 205, 250, role, [("you", "Role + idea"), ("ai", "VERDICT: …"), ("ai", "TOP 3 RISKS"),
                                              ("ai", "2 QUESTIONS")], badge=None, title_size=17)
    card(d, (300, 760, 1300, 845), fill=SUNK, outline=RAIL, shadow=False)
    d.text((330, 776), "Keep the chats apart:", font=BOLD(24), fill=TEXT)
    d.text((330 + d.textlength("Keep the chats apart: ", font=BOLD(24)), 778), "turn memory off, or use a temporary / incognito chat,", font=BODY(24), fill=TEXT)
    d.text((330, 808), "so no advisor can see what another one said.", font=BODY(24), fill=TEXT)
    im.save(HERE / "chat-round1.png", optimize=True)


def rounds23() -> None:
    im, d = canvas()
    heading(d, "Rounds 2 and 3: review blind, then one verdict",
            "Remove the role names, shuffle, label A to G. Then hand everything to a chair.")
    # A–G chips with names crossed out
    for i, letter in enumerate("ABCDEFG"):
        y = 215 + i * 88
        card(d, (70, y, 400, y + 70), r=16, shadow=False)
        d.rounded_rectangle((84, y + 13, 128, y + 57), 10, fill=CLAY)
        tw = d.textlength(letter, font=BLACK(26))
        d.text((106 - tw / 2, y + 18), letter, font=BLACK(26), fill="#FFFFFF")
        name = ROLES[(i * 3) % 7]
        d.text((146, y + 22), name, font=BODY(22), fill="#B8ADA3")
        nw = d.textlength(name, font=BODY(22))
        d.line([(144, y + 36), (148 + nw, y + 36)], fill=CLAY, width=3)
    arrow(d, (420, 520), (500, 520))
    chat_card(d, 510, 250, 440, 470, "2 · Review chat", [("you", "Answers A–G"), ("ai", "STRONGEST: C, because …"),
                                                         ("ai", "WEAKEST: F, because …"), ("ai", "EVERYONE MISSED: …"),
                                                         ("ai", "CHANGES VERDICT? no")])
    arrow(d, (970, 520), (1050, 520))
    chat_card(d, 1060, 250, 480, 470, "3 · Chair chat", [("you", "Idea + A–G + review"), ("ai", "1 Verdict + the vote"),
                                                        ("ai", "2 Where they agree"), ("ai", "3 Real disagreements"),
                                                        ("ai", "4 What everyone missed"), ("ai", "5 One cheap test"),
                                                        ("ai", "6 Up to 4 questions")], accent=True)
    card(d, (510, 760, 1540, 845), fill=SUNK, outline=RAIL, shadow=False)
    d.text((540, 778), "Then answer the chair's questions, and run the test before you trust the verdict.",
           font=BODY(24), fill=TEXT)
    im.save(HERE / "chat-rounds2-3.png", optimize=True)


if __name__ == "__main__":
    overview()
    round1()
    rounds23()
    print("wrote", ", ".join(p.name for p in sorted(HERE.glob("chat-*.png"))))
