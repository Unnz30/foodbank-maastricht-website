from pathlib import Path
from html import escape
import textwrap


OUT = Path("design/pages")
OUT.mkdir(parents=True, exist_ok=True)

W = 1440
M = 72
INNER = W - M * 2

COLORS = {
    "canvas": "#fff3dc",
    "paper": "#fffaf0",
    "ink": "#15140f",
    "green": "#0f412c",
    "orange": "#ef5a1a",
    "mustard": "#f5b63f",
    "mint": "#c7d8a8",
    "tomato": "#c93618",
    "muted": "#6f5948",
    "clay": "#7a3727",
    "sky": "#317f8f",
}


def t(x, y, text, cls="s p ink", size=None, weight=None, anchor=None):
    attrs = []
    if size:
        attrs.append(f'font-size="{size}"')
    if weight:
        attrs.append(f'font-weight="{weight}"')
    if anchor:
        attrs.append(f'text-anchor="{anchor}"')
    return f'<text x="{x}" y="{y}" class="{cls}" {" ".join(attrs)}>{escape(text)}</text>'


def wrapped(x, y, text, width=42, line=31, cls="s p muted", size=None):
    out = []
    for i, part in enumerate(textwrap.wrap(text, width=width)):
        out.append(t(x, y + i * line, part, cls=cls, size=size))
    return "\n".join(out)


def rect(x, y, w, h, fill="paper", rx=8, stroke=True, cls=""):
    st = f'stroke="{COLORS["ink"]}" stroke-width="3"' if stroke else ""
    c = f' class="{cls}"' if cls else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{COLORS[fill]}" {st}{c}/>'


def line(x1, y1, x2, y2, width=2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{COLORS["ink"]}" stroke-width="{width}"/>'


def button(x, y, label, w=210, fill="mustard"):
    return "\n".join([
        rect(x, y, w, 54, fill=fill, rx=27),
        t(x + w / 2, y + 35, label, cls="s label ink", anchor="middle"),
    ])


def image_box(x, y, w, h, label, fill="paper", kind="veg"):
    shapes = [rect(x, y, w, h, fill=fill)]
    if kind == "veg":
        shapes += [
            f'<circle cx="{x+w*.28}" cy="{y+h*.42}" r="{min(w,h)*.11}" fill="{COLORS["mint"]}" stroke="{COLORS["ink"]}" stroke-width="3"/>',
            f'<circle cx="{x+w*.48}" cy="{y+h*.52}" r="{min(w,h)*.14}" fill="{COLORS["tomato"]}" stroke="{COLORS["ink"]}" stroke-width="3"/>',
            f'<circle cx="{x+w*.68}" cy="{y+h*.39}" r="{min(w,h)*.1}" fill="{COLORS["mustard"]}" stroke="{COLORS["ink"]}" stroke-width="3"/>',
            f'<path d="M{x+w*.22} {y+h*.72} C{x+w*.38} {y+h*.58}, {x+w*.62} {y+h*.58}, {x+w*.78} {y+h*.72}" fill="none" stroke="{COLORS["ink"]}" stroke-width="3" stroke-linecap="round"/>',
        ]
    elif kind == "people":
        for cx, cy, r in [(x+w*.28, y+h*.38, 24), (x+w*.5, y+h*.34, 28), (x+w*.72, y+h*.4, 22)]:
            shapes.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{COLORS["mustard"]}" stroke="{COLORS["ink"]}" stroke-width="3"/>')
        shapes.append(f'<path d="M{x+w*.16} {y+h*.78} C{x+w*.22} {y+h*.56}, {x+w*.36} {y+h*.56}, {x+w*.42} {y+h*.78}" fill="none" stroke="{COLORS["ink"]}" stroke-width="3"/>')
        shapes.append(f'<path d="M{x+w*.36} {y+h*.82} C{x+w*.44} {y+h*.54}, {x+w*.56} {y+h*.54}, {x+w*.64} {y+h*.82}" fill="none" stroke="{COLORS["ink"]}" stroke-width="3"/>')
        shapes.append(f'<path d="M{x+w*.62} {y+h*.78} C{x+w*.68} {y+h*.58}, {x+w*.8} {y+h*.58}, {x+w*.86} {y+h*.78}" fill="none" stroke="{COLORS["ink"]}" stroke-width="3"/>')
    elif kind == "venue":
        shapes += [
            f'<path d="M{x+w*.16} {y+h*.48} L{x+w*.5} {y+h*.22} L{x+w*.84} {y+h*.48} Z" fill="{COLORS["orange"]}" stroke="{COLORS["ink"]}" stroke-width="3"/>',
            f'<rect x="{x+w*.22}" y="{y+h*.48}" width="{w*.56}" height="{h*.28}" fill="{COLORS["clay"]}" stroke="{COLORS["ink"]}" stroke-width="3"/>',
            f'<rect x="{x+w*.42}" y="{y+h*.58}" width="{w*.16}" height="{h*.18}" fill="{COLORS["green"]}" stroke="{COLORS["ink"]}" stroke-width="3"/>',
        ]
    shapes.append(t(x + 20, y + h - 24, label, cls="s small ink"))
    return "\n".join(shapes)


def veggie_doodle(x, y, scale=1):
    return f'''
    <g fill="none" stroke="{COLORS["green"]}" stroke-width="{4*scale}" stroke-linecap="round" stroke-linejoin="round">
      <path d="M{x} {y+86*scale} C{x+38*scale} {y+6*scale}, {x+116*scale} {y+8*scale}, {x+168*scale} {y+86*scale}"/>
      <path d="M{x+42*scale} {y+48*scale} C{x+34*scale} {y+10*scale}, {x+64*scale} {y-10*scale}, {x+112*scale} {y}"/>
      <path d="M{x+90*scale} {y+50*scale} C{x+114*scale} {y+2*scale}, {x+156*scale} {y+2*scale}, {x+190*scale} {y+28*scale}"/>
      <circle cx="{x+26*scale}" cy="{y+104*scale}" r="{14*scale}"/>
      <circle cx="{x+174*scale}" cy="{y+92*scale}" r="{18*scale}"/>
    </g>'''


def people_doodle(x, y, scale=1):
    return f'''
    <g fill="none" stroke="{COLORS["green"]}" stroke-width="{4*scale}" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="{x+36*scale}" cy="{y+28*scale}" r="{18*scale}"/>
      <path d="M{x+8*scale} {y+94*scale} C{x+16*scale} {y+56*scale}, {x+58*scale} {y+56*scale}, {x+66*scale} {y+94*scale}"/>
      <circle cx="{x+118*scale}" cy="{y+22*scale}" r="{21*scale}"/>
      <path d="M{x+86*scale} {y+98*scale} C{x+96*scale} {y+52*scale}, {x+140*scale} {y+52*scale}, {x+150*scale} {y+98*scale}"/>
      <circle cx="{x+196*scale}" cy="{y+34*scale}" r="{16*scale}"/>
      <path d="M{x+172*scale} {y+94*scale} C{x+180*scale} {y+60*scale}, {x+214*scale} {y+60*scale}, {x+222*scale} {y+94*scale}"/>
    </g>'''


def header(active):
    nav = [("About", "about"), ("Get Involved", "involved"), ("Events", "events"), ("Contact", "contact")]
    parts = [rect(0, 0, W, 78, fill="paper", rx=0)]
    parts.append(f'<circle cx="104" cy="39" r="21" fill="{COLORS["orange"]}" stroke="{COLORS["ink"]}" stroke-width="3"/>')
    parts.append(t(104, 47, "FM", cls="s label paper", anchor="middle"))
    parts.append(t(142, 34, "Foodbank Maastricht", cls="s label ink"))
    parts.append(t(142, 58, "Friday kitchen", cls="s small muted"))
    x = 770
    for label, key in nav:
        fill = "ink" if key == active else "paper"
        color = "paper" if key == active else "ink"
        parts.append(f'<rect x="{x}" y="22" width="{len(label)*10+42}" height="36" rx="18" fill="{COLORS[fill]}" stroke="{COLORS["ink"]}" stroke-width="2"/>')
        parts.append(t(x + (len(label)*10+42)/2, 46, label, cls=f"s small {color}", anchor="middle"))
        x += len(label) * 10 + 58
    parts.append(rect(1246, 22, 96, 36, fill="paper", rx=18))
    parts.append(t(1270, 46, "NL", cls="s small ink"))
    parts.append(t(1310, 46, "EN", cls="s small ink"))
    return "\n".join(parts)


def footer(y):
    h = 360
    return "\n".join([
        f'<rect x="0" y="{y}" width="{W}" height="{h}" fill="{COLORS["green"]}" stroke="{COLORS["ink"]}" stroke-width="3"/>',
        f'<circle cx="1230" cy="{y+80}" r="82" fill="{COLORS["mustard"]}" opacity="0.2"/>',
        t(M, y + 92, "Foodbank Maastricht", cls="g h2 paper"),
        wrapped(M, y + 142, "A volunteer-run Friday kitchen rescuing surplus food in Maastricht.", width=44, cls="s p paper"),
        t(760, y + 92, "Visit", cls="s label paper"),
        wrapped(760, y + 132, "Biesenwal 3, 6211 AD Maastricht", width=24, cls="s p paper"),
        t(1030, y + 92, "Contact", cls="s label paper"),
        t(1030, y + 132, "foodbankmaastricht@gmail.com", cls="s p paper"),
        rect(1030, y + 170, 112, 40, fill="green", rx=20),
        t(1086, y + 196, "Facebook", cls="s small paper", anchor="middle"),
        rect(1160, y + 170, 116, 40, fill="green", rx=20),
        t(1218, y + 196, "Instagram", cls="s small paper", anchor="middle"),
        line(M, y + 270, W - M, y + 270, width=1),
        t(M, y + 314, "Built for Foodbank Maastricht. Replace placeholder photos with community images when ready.", cls="s small paper"),
    ])


def page(title, active, height, body):
    css = """
    .s{font-family:Inter,Arial,sans-serif}.g{font-family:Georgia,serif}
    .ink{fill:#15140f}.paper{fill:#fffaf0}.muted{fill:#6f5948}.tomato{fill:#c93618}
    .small{font-size:18px}.p{font-size:24px}.label{font-size:17px;font-weight:900;text-transform:uppercase}
    .h1{font-size:86px;font-weight:700}.h2{font-size:52px;font-weight:700}.h3{font-size:31px;font-weight:800}
    """
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{height}" viewBox="0 0 {W} {height}">
  <defs><style>{css}</style></defs>
  <rect width="{W}" height="{height}" fill="{COLORS["canvas"]}"/>
  {header(active)}
  {body}
</svg>
'''


def home():
    y = 78
    parts = []
    parts.append(rect(0, y, W, 590, fill="orange", rx=0))
    parts.append(f'<circle cx="1230" cy="{y+100}" r="88" fill="{COLORS["mustard"]}"/>')
    parts.append(t(M, y + 110, "FOODBANK MAASTRICHT", cls="s label paper"))
    parts.append(t(M, y + 245, "Rescue.", cls="g h1 paper", size=118))
    parts.append(t(M, y + 370, "Cook. Share.", cls="g h1 paper", size=118))
    parts.append(t(M, y + 430, "Friday food rescue in Maastricht.", cls="s p paper"))
    parts.append(button(M, y + 470, "Join us Friday", 210))
    parts.append(image_box(820, y + 120, 260, 230, "Market haul", fill="paper", kind="veg"))
    parts.append(image_box(990, y + 320, 280, 190, "Dinner table", fill="mint", kind="people"))
    parts.append(image_box(720, y + 330, 250, 180, "Cooking", fill="mustard", kind="veg"))
    y += 640
    parts.append(rect(126, y - 54, 1188, 126, fill="paper"))
    for i, (num, label) in enumerate([("12+", "years active"), ("51,000 kg", "rescued in 2024"), ("100%", "volunteer-run")]):
        x = 170 + i * 395
        if i:
            parts.append(line(126 + i * 396, y - 54, 126 + i * 396, y + 72))
        parts.append(t(x, y + 5, num, cls="g h2 tomato"))
        parts.append(t(x, y + 42, label, cls="s p ink"))
    y += 210
    parts.append(t(M, y, "HOW FRIDAY WORKS", cls="s label tomato"))
    parts.append(t(M, y + 92, "Collect", cls="g h1 ink", size=104))
    parts.append(t(M, y + 200, "Cook", cls="g h1 ink", size=104))
    parts.append(t(M, y + 308, "Eat", cls="g h1 ink", size=104))
    parts.append(veggie_doodle(M + 20, y + 360, 1.1))
    for i, (n, h, p) in enumerate([("01", "Collect", "Surplus produce from local market stands."), ("02", "Cook", "A menu built together from what arrives."), ("03", "Eat", "A donation-based vegan dinner at 20:00.")]):
        yy = y + 40 + i * 150
        parts.append(line(610, yy - 42, 1230, yy - 42))
        parts.append(t(610, yy + 18, n, cls="g h2 tomato"))
        parts.append(t(720, yy + 16, h, cls="g h2 ink"))
        parts.append(t(720, yy + 54, p, cls="s p muted"))
    y += 600
    parts.append(rect(0, y, W, 330, fill="mint", rx=0))
    parts.append(t(M, y + 105, "Everyone who walks in is a volunteer", cls="g h2 ink"))
    parts.append(wrapped(M + 650, y + 100, "Foodbank Maastricht is a shared kitchen, not a service counter. People come to chop, stir, wash, laugh, eat, and keep good food moving through the city instead of into the bin.", width=42, cls="s p muted"))
    parts.append(people_doodle(M + 660, y + 205, 1.0))
    y += 450
    parts.append(rect(M, y, INNER, 260, fill="mustard"))
    parts.append(t(M + 44, y + 70, "NEXT FRIDAY'S DINNER", cls="s label ink"))
    parts.append(wrapped(M + 44, y + 125, "Pull up a chair at Landbouwbelang for the weekly three-course vegan dinner.", width=44, cls="g h2 ink", line=58))
    parts.append(button(1100, y + 105, "See events", 150, fill="ink"))
    parts.append(t(175, y + 220, "Friday 12 June 2026   |   20:00   |   Landbouwbelang", cls="s p ink"))
    y += 390
    parts.append(rect(0, y, W, 820, fill="mustard", rx=0, stroke=False))
    parts.append(t(M, y + 100, "FOLLOW THE FRIDAY KITCHEN", cls="s label tomato"))
    parts.append(wrapped(M, y + 150, "Placeholder snapshots for now, ready for real market hauls, cooking scenes, and dinner-table moments.", width=60, cls="s p muted"))
    for i in range(6):
        x = M + (i % 3) * 420
        yy = y + 250 + (i // 3) * 300
        parts.append(image_box(x, yy, 380, 260, f"Instagram tile {i+1}", fill="paper", kind="veg" if i % 2 == 0 else "people"))
    parts.append(button(M, y + 710, "Follow @foodbankmaastricht", 310))
    y += 950
    parts.append(t(M, y, "LATEST NEWS", cls="s label tomato"))
    for i, (cat, title, fill) in enumerate([("Kitchen Dispatch", "Market crates, bright herbs, full tables", "orange"), ("Impact", "What 51,000 kg of rescued food feels like", "green"), ("Menu Notes", "Three courses from whatever arrives", "mustard")]):
        x = M + i * 430
        parts.append(rect(x, y + 60, 390, 430, fill="paper"))
        parts.append(image_box(x, y + 60, 390, 170, "Placeholder image", fill="mint", kind="veg"))
        parts.append(rect(x + 24, y + 255, 180, 36, fill=fill, rx=18))
        parts.append(t(x + 114, y + 279, cat, cls="s small paper" if fill != "mustard" else "s small ink", anchor="middle"))
        parts.append(t(x + 24, y + 326, "12 June 2026", cls="s small tomato"))
        parts.append(wrapped(x + 24, y + 370, title, width=22, cls="g h3 ink", line=36))
    y += 610
    parts.append(rect(0, y, W, 280, fill="green", rx=0))
    parts.append(t(M, y + 110, "Bring your hands, your appetite, or your support.", cls="g h2 paper"))
    parts.append(button(890, y + 112, "Volunteer on Friday", 240))
    parts.append(button(1150, y + 112, "Make a donation", 210, fill="paper"))
    y += 280
    parts.append(footer(y))
    OUT.joinpath("home.svg").write_text(page("Home", "", y + 360, "\n".join(parts)))


def hero(y, label, title, fill="green"):
    return "\n".join([
        rect(0, y, W, 420, fill=fill, rx=0),
        t(M, y + 120, label.upper(), cls="s label paper"),
        wrapped(M, y + 220, title, width=30, cls="g h1 paper", line=86),
        image_box(930, y + 100, 330, 230, "Hero image", fill="paper", kind="people"),
    ])


def about():
    y = 78
    parts = [hero(y, "About", "A Friday kitchen with deep Maastricht roots")]
    y += 560
    parts.append(t(M, y, "Origin story", cls="g h2 ink"))
    parts.append(wrapped(M, y + 55, "Foodbank Maastricht was founded over 12 years ago at Landbouwbelang, a cultural community space in Maastricht. What began as a practical response to food waste became a steady weekly ritual.", width=54))
    parts.append(image_box(820, y - 30, 430, 280, "Landbouwbelang", fill="paper", kind="venue"))
    y += 430
    parts.append(rect(0, y, W, 700, fill="orange", rx=0))
    parts.append(t(M, y + 95, "HOW IT WORKS", cls="s label paper"))
    parts.append(t(M, y + 165, "From market leftovers to Friday dinner", cls="g h2 paper"))
    for i, (time, head, body) in enumerate([("15:00", "Collect surplus produce", "Leave for the Markt to collect leftover fruit and vegetables."), ("16:00", "Cook together", "Return to Landbouwbelang, decide the menu, and start cooking."), ("20:00", "Share dinner", "Sit down together for a vegan three-course dinner.")]):
        yy = y + 260 + i * 130
        parts.append(line(M, yy - 45, W - M, yy - 45))
        parts.append(t(M, yy, time, cls="g h2 paper"))
        parts.append(t(M + 220, yy, head, cls="g h2 paper"))
        parts.append(t(M + 220, yy + 38, body, cls="s p paper"))
    y += 830
    parts.append(t(M, y, "Everyone is a volunteer", cls="g h2 ink"))
    parts.append(wrapped(M, y + 58, "There is no hard line between organizers, cooks, guests, and helpers. Everyone who walks in is invited to take part.", width=50))
    parts.append(t(M + 680, y, "Hosted by Landbouwbelang", cls="g h2 ink"))
    parts.append(wrapped(M + 680, y + 58, "Landbouwbelang provides the space where surplus produce becomes dinner.", width=44))
    y += 340
    parts.append(rect(0, y, W, 520, fill="mint", rx=0))
    parts.append(t(M, y + 100, "Volunteer faces", cls="g h2 ink"))
    for i, name in enumerate(["Mara", "Sam", "Noor", "Jules"]):
        x = M + i * 305
        parts.append(image_box(x, y + 170, 250, 250, name, fill="paper", kind="people"))
    y += 520
    parts.append(footer(y))
    OUT.joinpath("about.svg").write_text(page("About", "about", y + 360, "\n".join(parts)))


def involved():
    y = 78
    parts = [hero(y, "Get involved", "Show up on Friday and become part of the table", "orange")]
    y += 560
    parts.append(t(M, y, "Volunteer on Fridays", cls="g h2 ink"))
    parts.append(wrapped(M, y + 58, "Come to Landbouwbelang on Friday afternoon to help collect food, cook, clean, serve, or welcome guests.", width=52))
    parts.append(rect(780, y - 20, 490, 430, fill="paper"))
    parts.append(t(820, y + 45, "Simple sign-up", cls="g h2 ink"))
    for i, label in enumerate(["Name", "Email", "Message"]):
        h = 56 if i < 2 else 120
        parts.append(rect(820, y + 90 + i * 78, 390, h, fill="paper", rx=6))
        parts.append(t(842, y + 125 + i * 78, label, cls="s p muted"))
    parts.append(button(820, y + 360, "Send volunteer message", 290))
    y += 560
    parts.append(rect(0, y, W, 340, fill="green", rx=0))
    parts.append(t(M, y + 120, "Support the kitchen", cls="g h2 paper"))
    parts.append(wrapped(M, y + 175, "Donations help cover basic costs for a free, volunteer-run initiative.", width=54, cls="s p paper"))
    parts.append(button(1070, y + 150, "Donate", 150))
    y += 480
    parts.append(image_box(M, y - 30, 430, 280, "Market produce", fill="paper", kind="veg"))
    parts.append(t(640, y, "Donate surplus food", cls="g h2 ink"))
    parts.append(wrapped(640, y + 58, "Market vendors and local businesses can donate surplus fruit, vegetables, and other vegan-friendly ingredients.", width=48))
    parts.append(button(640, y + 190, "Contact us about food donations", 360))
    y += 360
    parts.append(footer(y))
    OUT.joinpath("get-involved.svg").write_text(page("Get Involved", "involved", y + 360, "\n".join(parts)))


def events():
    y = 78
    parts = [hero(y, "Events", "Friday dinner is the weekly heartbeat")]
    y += 560
    parts.append(rect(M, y, INNER, 270, fill="mustard"))
    parts.append(t(M + 40, y + 80, "NEXT FRIDAY'S DINNER", cls="s label ink"))
    parts.append(wrapped(M + 40, y + 145, "The next communal vegan dinner is scheduled for Friday at 20:00 at Landbouwbelang.", width=46, cls="g h2 ink", line=56))
    parts.append(rect(1040, y + 80, 230, 110, fill="paper"))
    parts.append(t(1155, y + 145, "Friday 12 June", cls="s p ink", anchor="middle"))
    y += 420
    parts.append(rect(0, y, W, 360, fill="mint", rx=0))
    parts.append(t(M, y + 130, "Every Friday at 20:00", cls="g h2 ink"))
    parts.append(wrapped(M, y + 190, "Dinners happen weekly at Landbouwbelang, Biesenwal 3, Maastricht. Arrive earlier if you want to help cook or clean.", width=54))
    parts.append(image_box(860, y + 70, 360, 230, "Cooking together", fill="paper", kind="people"))
    y += 500
    parts.append(t(M, y, "FROM THE KITCHEN", cls="s label tomato"))
    parts.append(t(M, y + 70, "Live from Foodbank Maastricht", cls="g h2 ink"))
    parts.append(rect(M, y + 140, 610, 470, fill="mustard"))
    parts.append(t(M + 40, y + 205, "Facebook updates", cls="s label ink"))
    parts.append(rect(M + 40, y + 255, 520, 280, fill="paper"))
    parts.append(rect(750, y + 140, 620, 470, fill="green"))
    parts.append(t(790, y + 205, "Instagram moments", cls="s label paper"))
    for i in range(4):
        x = 790 + (i % 2) * 250
        yy = y + 250 + (i // 2) * 150
        parts.append(image_box(x, yy, 210, 120, f"Post {i+1}", fill="paper", kind="veg" if i % 2 else "people"))
    parts.append(button(790, y + 545, "Open Instagram", 210))
    y += 760
    parts.append(footer(y))
    OUT.joinpath("events.svg").write_text(page("Events", "events", y + 360, "\n".join(parts)))


def contact():
    y = 78
    parts = [hero(y, "Contact", "Find us at Landbouwbelang")]
    y += 560
    parts.append(t(M, y, "Details", cls="g h2 ink"))
    parts.append(t(M, y + 70, "Visit", cls="s label tomato"))
    parts.append(t(M, y + 110, "Biesenwal 3, 6211 AD Maastricht (Landbouwbelang)", cls="s p muted"))
    parts.append(t(M, y + 175, "Contact", cls="s label tomato"))
    parts.append(t(M, y + 215, "foodbankmaastricht@gmail.com", cls="s p muted"))
    parts.append(t(M, y + 280, "Follow", cls="s label tomato"))
    parts.append(t(M, y + 320, "Facebook / Instagram", cls="s p muted"))
    parts.append(rect(780, y - 20, 490, 430, fill="paper"))
    parts.append(t(820, y + 45, "General contact form", cls="g h2 ink"))
    for i, label in enumerate(["Name", "Email", "Message"]):
        h = 56 if i < 2 else 120
        parts.append(rect(820, y + 90 + i * 78, 390, h, fill="paper", rx=6))
        parts.append(t(842, y + 125 + i * 78, label, cls="s p muted"))
    parts.append(button(820, y + 360, "Send message", 220))
    y += 560
    parts.append(rect(M, y, INNER, 440, fill="mint"))
    parts.append(t(M + 50, y + 90, "Map to Biesenwal 3, Maastricht", cls="g h2 ink"))
    parts.append(f'<path d="M{M+80} {y+270} C{M+260} {y+130}, {M+460} {y+400}, {M+660} {y+250} S{M+1040} {y+190}, {M+1180} {y+300}" fill="none" stroke="{COLORS["ink"]}" stroke-width="3"/>')
    parts.append(f'<circle cx="{M+650}" cy="{y+260}" r="34" fill="{COLORS["tomato"]}" stroke="{COLORS["ink"]}" stroke-width="3"/>')
    y += 580
    parts.append(footer(y))
    OUT.joinpath("contact.svg").write_text(page("Contact", "contact", y + 360, "\n".join(parts)))


def combined():
    files = ["home.svg", "about.svg", "get-involved.svg", "events.svg", "contact.svg"]
    x = 0
    parts = []
    for file in files:
        svg = OUT.joinpath(file).read_text()
        inner = svg.split(">", 1)[1].rsplit("</svg>", 1)[0]
        parts.append(f'<g transform="translate({x} 0)">{inner}</g>')
        x += W + 120
    Path("design/all-pages-full.svg").write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{x}" height="5200" viewBox="0 0 {x} 5200">{"".join(parts)}</svg>')


home()
about()
involved()
events()
contact()
combined()
