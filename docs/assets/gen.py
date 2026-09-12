#!/usr/bin/env python3
"""Generate the README visual system for omarchy-t1-desktop. Run from this directory."""
from pathlib import Path

OUT = Path(__file__).resolve().parent

SANS = "ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'JetBrains Mono', Menlo, Consolas, monospace"

DEFS = r"""
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#0e0e14"/>
    <stop offset="0.55" stop-color="#13141c"/>
    <stop offset="1" stop-color="#1a1b26"/>
  </linearGradient>
  <linearGradient id="spectrum" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#f7768e"/>
    <stop offset="0.25" stop-color="#e0af68"/>
    <stop offset="0.5" stop-color="#9ece6a"/>
    <stop offset="0.75" stop-color="#7dcfff"/>
    <stop offset="1" stop-color="#bb9af7"/>
  </linearGradient>
  <linearGradient id="title" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#c0caf5"/>
    <stop offset="1" stop-color="#9ece6a"/>
  </linearGradient>
  <linearGradient id="glass" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#ffffff" stop-opacity="0.08"/>
    <stop offset="1" stop-color="#ffffff" stop-opacity="0.02"/>
  </linearGradient>
  <radialGradient id="orbG" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="#9ece6a" stop-opacity="0.45"/>
    <stop offset="1" stop-color="#9ece6a" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="orbB" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="#7aa2f7" stop-opacity="0.40"/>
    <stop offset="1" stop-color="#7aa2f7" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="orbM" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="#bb9af7" stop-opacity="0.35"/>
    <stop offset="1" stop-color="#bb9af7" stop-opacity="0"/>
  </radialGradient>
  <filter id="glow" x="-20%" y="-200%" width="140%" height="500%">
    <feGaussianBlur stdDeviation="14"/>
  </filter>
  <filter id="soft" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation="40"/>
  </filter>
"""


def pill(x, y, w, h, text, fill="#ffffff", fill_op="0.07", stroke_op="0.14", text_fill="#c0caf5", size=14):
    return f'''<g transform="translate({x} {y})">
      <rect width="{w}" height="{h}" rx="{h/2}" fill="{fill}" fill-opacity="{fill_op}" stroke="#ffffff" stroke-opacity="{stroke_op}"/>
      <text x="{w/2}" y="{h*0.68:.1f}" text-anchor="middle" font-family="{SANS}" font-size="{size}" font-weight="600" fill="{text_fill}">{text}</text>
    </g>'''


def write(name, svg):
    path = OUT / name
    path.write_text(svg.strip() + "\n", encoding="utf-8")
    print(f"wrote {path.name} ({path.stat().st_size} bytes)")


def ico_speaker(x, y, color="#c0caf5"):
    return f'''<g transform="translate({x} {y})" fill="{color}">
      <path d="M 2 7 h 4 l 5 -4 v 14 l -5 -4 h -4 z"/>
      <path d="M 13 8 q 3 2 3 4 q 0 2 -3 4" fill="none" stroke="{color}" stroke-width="1.6" stroke-linecap="round"/>
    </g>'''


def ico_play(x, y, color="#c0caf5"):
    return f'''<g transform="translate({x} {y})" fill="{color}">
      <path d="M 3 3 l 12 7 l -12 7 z"/>
    </g>'''


def ico_sun(x, y, color="#e0af68"):
    return f'''<g transform="translate({x} {y})" fill="none" stroke="{color}" stroke-width="1.7" stroke-linecap="round">
      <circle cx="10" cy="10" r="4" fill="{color}" stroke="none"/>
      <path d="M 10 1 v 2.5 M 10 16.5 v 2.5 M 1 10 h 2.5 M 16.5 10 h 2.5 M 3.5 3.5 l 1.8 1.8 M 14.7 14.7 l 1.8 1.8 M 16.5 3.5 l -1.8 1.8 M 5.3 14.7 l -1.8 1.8"/>
    </g>'''


def ico_moon(x, y, color="#7aa2f7"):
    return f'''<g transform="translate({x} {y})" fill="{color}">
      <path d="M 12 3 a 8 8 0 1 0 5 13 a 7 7 0 0 1 -5 -13 z"/>
    </g>'''


# --------------------------------------------------------------------------- hero
hero = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="340" viewBox="0 0 1280 340" role="img" aria-label="T1 Touch Bar Desktop: an Omarchy plugin that wires the T1 Touch Bar to the desktop">
  <defs>{DEFS}
    <pattern id="dots" width="28" height="28" patternUnits="userSpaceOnUse">
      <circle cx="1.2" cy="1.2" r="1.2" fill="#ffffff" opacity="0.04"/>
    </pattern>
  </defs>

  <rect width="1280" height="340" rx="32" fill="url(#bg)"/>
  <rect width="1280" height="340" rx="32" fill="url(#dots)"/>
  <circle cx="1140" cy="30" r="220" fill="url(#orbG)" filter="url(#soft)"/>
  <circle cx="160" cy="400" r="200" fill="url(#orbB)" filter="url(#soft)"/>
  <circle cx="700" cy="0" r="140" fill="url(#orbM)" opacity="0.8" filter="url(#soft)"/>

  <g transform="translate(72 52)">
    <rect width="54" height="54" rx="16" fill="#0e0e14" stroke="#ffffff" stroke-opacity="0.12"/>
    <rect x="7" y="22" width="40" height="10" rx="5" fill="url(#spectrum)"/>
  </g>
  <text x="144" y="88" font-family="{SANS}" font-size="20" font-weight="700" letter-spacing="5" fill="#9ece6a">OMARCHY PLUGIN</text>

  <text x="72" y="168" font-family="{SANS}" font-size="58" font-weight="800" letter-spacing="-1.5" fill="url(#title)">T1 Touch Bar Desktop</text>
  <text x="74" y="214" font-family="{SANS}" font-size="22" fill="#a9b1d6">The strip talks to Omarchy. Volume, media, brightness. Dark when the display sleeps.</text>

  {pill(72, 244, 132, 34, "Omarchy 3", size=13)}
  {pill(216, 244, 118, 34, "T1Bridge", size=13)}
  {pill(346, 244, 132, 34, "user service", "#9ece6a", "0.14", "0.35", "#9ece6a", 13)}
  {pill(490, 244, 148, 34, "nn.t1-desktop", size=13)}

  <g transform="translate(980 118)" font-family="{SANS}">
    <text x="0" y="0" font-size="34" font-weight="800" fill="#c0caf5">no root</text>
    <text x="0" y="26" font-size="14" fill="#565f89">your user, your session</text>
    <text x="0" y="84" font-size="34" font-weight="800" fill="#9ece6a">1 second</text>
    <text x="0" y="110" font-size="14" fill="#565f89">the renderer polls status</text>
  </g>

  <rect x="0" y="332" width="1280" height="8" fill="url(#spectrum)"/>
</svg>'''
write("hero.svg", hero)


# --------------------------------------------------------------------------- features
def well(x, fill, inner):
    return f'''<g transform="translate({x} 36)">
    <circle cx="32" cy="32" r="32" fill="{fill}" fill-opacity="0.14"/>
    <g transform="translate(16 16) scale(1.6)">{inner}</g>
  </g>'''


def col(x, icon, title, sub):
    return f'''<g transform="translate({x} 0)">
    {icon}
    <text x="28" y="156" font-family="{SANS}" font-size="22" font-weight="800" fill="#c0caf5">{title}</text>
    <text x="28" y="186" font-family="{SANS}" font-size="14" fill="#565f89">{sub}</text>
  </g>'''


features = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="220" viewBox="0 0 1280 220" role="img" aria-label="Volume, media, brightness OSDs, and a dark bar when the display sleeps">
  <defs>{DEFS}</defs>
  <rect width="1280" height="220" rx="28" fill="#13141c" stroke="#ffffff" stroke-opacity="0.08"/>
  {col(0, well(28, "#7dcfff", ico_speaker(0, 0, "#7dcfff")), "Volume", "PipeWire slider and mute")}
  <line x1="320" y1="28" x2="320" y2="192" stroke="#ffffff" stroke-opacity="0.07"/>
  {col(320, well(28, "#bb9af7", ico_play(0, 0, "#bb9af7")), "Media", "prev, play/pause, next")}
  <line x1="640" y1="28" x2="640" y2="192" stroke="#ffffff" stroke-opacity="0.07"/>
  {col(640, well(28, "#e0af68", ico_sun(0, 0)), "Brightness", "Omarchy OSDs for screen and keys")}
  <line x1="960" y1="28" x2="960" y2="192" stroke="#ffffff" stroke-opacity="0.07"/>
  {col(960, well(28, "#7aa2f7", ico_moon(0, 0)), "Display off", "The bar goes dark with the screen")}
</svg>'''
write("features.svg", features)


# --------------------------------------------------------------------------- display on / off
display = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="168" viewBox="0 0 1280 168" role="img" aria-label="When the display is on the controls light; when it blanks the Touch Bar goes dark">
  <defs>{DEFS}</defs>
  <rect width="1280" height="168" rx="24" fill="#13141c" stroke="#ffffff" stroke-opacity="0.08"/>

  <g transform="translate(36 28)">
    <text x="0" y="18" font-family="{MONO}" font-size="13" fill="#9ece6a">display on</text>
    <rect y="36" width="540" height="44" rx="12" fill="#0e0e14" stroke="#9ece6a" stroke-opacity="0.35"/>
    <rect x="16" y="50" width="508" height="16" rx="8" fill="#9ece6a" fill-opacity="0.22"/>
    <text x="0" y="106" font-family="{SANS}" font-size="14" fill="#a9b1d6">the renderer paints; this plugin feeds it state</text>
  </g>

  <g transform="translate(600 70)">
    <rect x="-18" y="-18" width="36" height="36" rx="18" fill="#7aa2f7" fill-opacity="0.18"/>
    <path d="M -8 0 h 14 m 0 0 l -6 -6 m 6 6 l -6 6" fill="none" stroke="#c0caf5" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
  </g>

  <g transform="translate(668 28)">
    <text x="0" y="18" font-family="{MONO}" font-size="13" fill="#565f89">display off</text>
    <rect y="36" width="540" height="44" rx="12" fill="#05060d" stroke="#ffffff" stroke-opacity="0.06"/>
    <rect x="16" y="50" width="508" height="16" rx="8" fill="#ffffff" fill-opacity="0.04"/>
    <text x="0" y="106" font-family="{SANS}" font-size="14" fill="#565f89">lock screen blanks · bar sleeps with it</text>
  </g>
</svg>'''
write("display.svg", display)


# --------------------------------------------------------------------------- terminal
rows = [
    ("cmd",  "$ omarchy plugin add https://github.com/niconistal/omarchy-t1-desktop.git --enable"),
    ("blank", ""),
    ("ok",   "enabled  nn.t1-desktop"),
    ("note", "wrote ~/.config/systemd/user/t1-touchbar.service.d/t1-desktop.conf"),
    ("note", "restarted t1-touchbar.service"),
    ("blank", ""),
    ("cmd",  "$ omarchy-shell t1desktop status"),
    ("mint", 'T1BRIDGE-DESKTOP 1 31 42 0 1'),
    ("dim",  "  caps  volume  mute  display-on"),
    ("blank", ""),
    ("cmd",  "$ omarchy-shell t1desktop last"),
    ("note", "install: already installed"),
]

colors = {
    "cmd":  "#c0caf5",
    "ok":   "#9ece6a",
    "note": "#a9b1d6",
    "mint": "#9ece6a",
    "dim":  "#565f89",
}
weights = {"cmd": "700", "ok": "700", "mint": "700"}

texts = []
y = 92
for kind, line in rows:
    if kind == "blank":
        y += 12
        continue
    line = line.replace("&", "&amp;").replace("<", "&lt;")
    w = weights.get(kind, "500")
    c = colors[kind]
    texts.append(
        f'<text x="36" y="{y}" font-family="{MONO}" font-size="15" font-weight="{w}" fill="{c}" font-variant-ligatures="none">{line}</text>'
    )
    y += 26

terminal = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="400" viewBox="0 0 1280 400" role="img" aria-label="Install with omarchy plugin add, then check t1desktop status">
  <defs>{DEFS}</defs>
  <rect width="1280" height="400" rx="28" fill="#0e0e14" stroke="#ffffff" stroke-opacity="0.10"/>
  <rect width="1280" height="48" rx="28" fill="#13141c"/>
  <rect y="24" width="1280" height="24" fill="#13141c"/>
  <circle cx="32" cy="24" r="7" fill="#f7768e"/>
  <circle cx="56" cy="24" r="7" fill="#e0af68"/>
  <circle cx="80" cy="24" r="7" fill="#9ece6a"/>
  <text x="640" y="30" text-anchor="middle" font-family="{MONO}" font-size="13" fill="#565f89">omarchy  ·  nn.t1-desktop</text>
  {"".join(texts)}
  <rect x="0" y="392" width="1280" height="8" fill="url(#spectrum)"/>
</svg>'''
write("terminal.svg", terminal)

print("done")
