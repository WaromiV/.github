"""Build self-contained README SVGs from recorded project material.

Run from any directory: python profile/assets/build_specimens.py
No network requests or third-party packages are required.
"""

import base64
import json
import math
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "specimens"
OUT = HERE / "badges"


def image_data(name):
    return "data:image/png;base64," + base64.b64encode((SOURCE / name).read_bytes()).decode()


def save(name, title, description, content, css=""):
    from html import escape
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="640" height="400" viewBox="0 0 640 400" role="img" aria-labelledby="title desc">
  <title id="title">{escape(title)}</title>
  <desc id="desc">{escape(description)}</desc>
  <style>
    text{{font-family:Georgia,"Times New Roman",serif}}
    .mono,.mono text{{font-family:"DejaVu Sans Mono",Consolas,monospace}}
    {css}
    @media(prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
  </style>
  {content}
</svg>
'''
    (OUT / (name + ".svg")).write_text("\n".join(line.rstrip() for line in svg.splitlines()) + "\n")


def login():
    save("login", "login.final.FINAL.v2 — authentication, amended",
         "An absurd authentication document. An enormous crossed-out FINAL, a red v2 correction, one input field, and the original site's potato.", '''
  <rect width="640" height="400" fill="#f2eee4"/>
  <g fill="#24241f">
    <text class="mono" x="28" y="35" font-size="17" letter-spacing="2">AUTHENTICATION</text>
    <text class="mono" x="612" y="35" font-size="17" text-anchor="end">Step 1 of ∞</text>
    <text x="28" y="99" font-size="52" letter-spacing="-2">login.</text>
    <text x="28" y="158" font-size="58" font-style="italic" letter-spacing="-2">final.</text>
    <text x="22" y="259" font-size="124" font-weight="bold" letter-spacing="-7">FINAL.</text>
  </g>
  <path d="M27 218L464 203" stroke="#a63b31" stroke-width="4" fill="none"/>
  <path d="M501 188l-35 19 7-16m-7 16 19 3" stroke="#a63b31" stroke-width="2" fill="none"/>
  <text x="508" y="197" font-size="68" font-style="italic" fill="#a63b31">v2</text>
  <rect x="28" y="285" width="490" height="49" fill="none" stroke="#56584d" stroke-width="1.5"/>
  <text class="mono" x="43" y="316" font-size="17" fill="#5c5b53">enter absolutely anything</text>
  <path class="caret" d="M306 301v19" stroke="#24241f" stroke-width="1.5"/>
  <text x="540" y="334" style="font-family:Apple Color Emoji,Segoe UI Emoji,Noto Color Emoji,sans-serif" font-size="63">🥔</text>
  <text x="28" y="376" font-size="21" font-style="italic" fill="#24241f">Choose your identity. Or a potato.</text>
''', '.caret{animation:blink 2.8s steps(1) infinite}@keyframes blink{0%,65%{opacity:1}66%,100%{opacity:0}}')


def cv():
    save("cv", "Emil Nesteruk — CV",
         "Emil Nesteruk. AI and backend engineering. Open the CV for experience, selected work and contact details.", '''
  <rect width="640" height="400" fill="#f2eee4"/>
  <text class="mono" x="28" y="36" font-size="17" letter-spacing="1.5" fill="#55584f">EMIL NESTERUK</text>
  <text x="23" y="193" font-size="168" letter-spacing="-10" fill="#24241f">CV.</text>
  <text x="30" y="254" font-size="32" fill="#24241f">AI &amp; backend engineering</text>
  <text class="mono" x="31" y="294" font-size="18" fill="#55584f">Experience / selected work / contact</text>
  <text class="mono" x="31" y="373" font-size="19" fill="#24241f">nesterukemil.cv</text>
  <path d="M564 369l40-40m-30 0h30v30" stroke="#a63b31" stroke-width="3" fill="none"/>
''')


def linkedin():
    save("linkedin", "Emil Nesteruk — LinkedIn and long-term AI work",
         "Connect with Emil Nesteruk on LinkedIn to discuss long-term AI engineering work with an established team.", '''
  <rect width="640" height="400" fill="#dce4e9"/>
  <text x="28" y="71" font-size="55" letter-spacing="-2" fill="#203644">LinkedIn</text>
  <text x="28" y="167" font-size="45" fill="#203644">Long-term.</text>
  <text x="28" y="218" font-size="45" fill="#203644">Hands-on.</text>
  <text x="28" y="269" font-size="45" font-style="italic" fill="#203644">AI engineering.</text>
  <text class="mono" x="30" y="313" font-size="18" fill="#405969">Looking for an established team.</text>
  <text class="mono" x="30" y="373" font-size="19" fill="#203644">Let's talk · Emil Nesteruk</text>
  <path d="M564 369l40-40m-30 0h30v30" stroke="#203644" stroke-width="3" fill="none"/>
''')


def benzin():
    m = json.loads((SOURCE / "map-state.json").read_text())
    date = m["capturedAt"][:10]
    save("benzin-kaliningrad", "Benzin v strane — a map of fuel availability",
         f"Actual Kaliningrad map crop from benzinavstrane.net, captured {date}. Original station colours: green available, orange queue, red unavailable, grey unknown. Basemap © OpenStreetMap contributors.", f'''
  <image width="640" height="400" href="{image_data('map-crop.png')}"/>
  <rect x="24" y="24" width="268" height="90" fill="#f2eee4"/>
  <text x="39" y="62" font-size="30" letter-spacing="-.7" fill="#232922">Benzin v strane</text>
  <text class="mono" x="40" y="89" font-size="16" fill="#515a4e">КАЛИНИНГРАД / АЗС</text>
  <rect x="0" y="360" width="640" height="40" fill="#f2eee4"/>
  <g class="mono" font-size="15" fill="#374235">
    <circle cx="23" cy="380" r="5" fill="#22c55e"/><text x="35" y="385">есть</text>
    <circle cx="104" cy="380" r="5" fill="#f59e0b"/><text x="116" y="385">очередь</text>
    <circle cx="219" cy="380" r="5" fill="#ef4444"/><text x="231" y="385">нет</text>
    <circle cx="293" cy="380" r="5" fill="#6b7280"/><text x="305" y="385">нет данных</text>
    <text x="623" y="385" text-anchor="end" font-size="12">© OpenStreetMap contributors</text>
  </g>
''')


def hyprchan():
    # The repository's original sit_sleeping.png contains 16 frames of 122 × 234.
    # Clip the untouched atlas; CSS advances real frames, not a redrawn mascot.
    save("hyprchan", "Hyprchan — caught sleeping on the desktop",
         "A mostly empty Hyprland desktop scene. The original Hyprchan sit_sleeping sprite occupies one corner. State label sit.sleeping is the actual animation ID; this is a staged scene, not live telemetry.", f'''
  <rect width="640" height="400" fill="#191d20"/>
  <path d="M24 40H616" stroke="#626a6b" stroke-width="1"/>
  <g class="mono" font-size="17" fill="#a4adab">
    <text x="28" y="28">1</text><text x="56" y="28" fill="#66726f">2   3   4</text>
    <text x="612" y="28" text-anchor="end">Hyprland</text>
  </g>
  <text x="28" y="99" fill="#e5e8e1" font-size="47" letter-spacing="-1.5">Hyprchan</text>
  <path d="M28 270H610" stroke="#535e5e" stroke-width="1"/>
  <text class="mono" x="28" y="258" font-size="17" fill="#929e99">animation = sit.sleeping</text>
  <svg x="523" y="192" width="78.08" height="149.76" viewBox="0 0 122 234" overflow="hidden">
    <image class="sprite" width="1952" height="234" href="{image_data('sit_sleeping.png')}"/>
  </svg>
  <text x="28" y="369" fill="#c9d2cb" font-size="23" font-style="italic">Something lives here.</text>
''', '.sprite{animation:sleep 4s steps(16) infinite}@keyframes sleep{to{transform:translateX(-1952px)}}')


def stonkfly():
    trace = json.loads((SOURCE / "stonkfly-trace.json").read_text())
    events = trace["events"]
    first, last = events[0], events[-1]
    start, end = first["time"], last["time"]
    # Derive bounds from the full snapshot so later observations cannot clip.
    values = [e["equity"] for e in events]
    raw_step = max((max(values) - min(values)) / 4, .1)
    scale = 10 ** math.floor(math.log10(raw_step))
    step = next(n * scale for n in (1, 2, 2.5, 5, 10) if n * scale >= raw_step)
    lower = math.floor(min(values) / step) * step
    upper = max(math.ceil(max(values) / step) * step, lower + step)
    x = lambda t: 76 + (t - start) / (end - start) * 530
    y = lambda v: 276 - (v - lower) / (upper - lower) * 150
    parts = []
    # Break the path at missing observations; elapsed time is the horizontal axis.
    for i, e in enumerate(events):
        op = "M" if i == 0 or e["time"] - events[i - 1]["time"] > 120 else "L"
        parts.append(f'{op}{x(e["time"]):.2f},{y(e["equity"]):.2f}')
    axis = ""
    for i in range(round((upper - lower) / step) + 1):
        value = lower + i * step
        yy = y(value)
        axis += f'<path d="M76 {yy:.1f}H606" stroke="#b7bfb4" stroke-width="1"/>\n'
        axis += f'<text class="mono" x="65" y="{yy+5:.1f}" text-anchor="end" font-size="15" fill="#526051">{value:.2f}</text>\n'
    gaps = ""
    for a, b in zip(events, events[1:]):
        if b["time"] - a["time"] > 120:
            xa, xb = x(a["time"]), x(b["time"])
            gaps += f'<rect x="{xa+4:.1f}" y="120" width="{xb-xa-8:.1f}" height="161" fill="#e6e9e0"/>\n'
            gaps += f'<text class="mono" x="{(xa+xb)/2:.1f}" y="186" text-anchor="middle" fill="#747d70" font-size="17">{round((b["time"]-a["time"])/60)} min gap</text>\n'
            gaps += f'<text class="mono" x="{(xa+xb)/2:.1f}" y="209" text-anchor="middle" fill="#747d70" font-size="14">no observations</text>\n'
    clock = lambda t: datetime.fromtimestamp(t, timezone.utc).strftime("%H:%M")
    end_date = datetime.fromtimestamp(end, timezone.utc)
    start_date = datetime.fromtimestamp(start, timezone.utc)
    period = f'{start_date:%Y-%m-%d %H:%M}–{end_date:%Y-%m-%d %H:%M} UTC'
    asset_name = f'stonkfly-{end_date:%Y%m%d}-t{last["tick"]}'
    holds = sum(e["side"] == "HOLD" for e in events)
    save(asset_name, "Stonkfly — paper-trading observation record",
         f'Recorded SOL-USDC paper-account equity, {period}, ticks {first["tick"]}–{last["tick"]}. {holds} of {len(events)} neural decisions were HOLD. The line breaks across the missing observations. Snapshot of pre-execution account equity; not a live return or a profitability claim. Built on nftechie/stonkfly.', f'''
  <rect width="640" height="400" fill="#edf0e8"/>
  <text x="28" y="62" font-size="45" letter-spacing="-1.5" fill="#283428">Stonkfly</text>
  <text class="mono" x="612" y="34" font-size="16" text-anchor="end" fill="#45513f">{end_date.strftime('%d %b %Y').upper()}</text>
  <text class="mono" x="612" y="59" font-size="16" text-anchor="end" fill="#45513f">PAPER TRADING</text>
  <text class="mono" x="28" y="101" font-size="16" fill="#53604e">SOL-USDC / OBSERVED EQUITY, USDC</text>
  {axis}{gaps}
  <path d="{' '.join(parts)}" fill="none" stroke="#943f33" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
  <g class="mono" font-size="15" fill="#526051">
    <text x="76" y="303">{clock(start)}</text><text x="606" y="303" text-anchor="end">{clock(end)} UTC</text>
  </g>
  <text x="28" y="344" font-size="25" fill="#283428">{holds} of {len(events)} decisions: HOLD.</text>
  <text class="mono" x="28" y="378" font-size="16" fill="#53604e">ticks {first["tick"]}–{last["tick"]} · built on nftechie/stonkfly</text>
  <g transform="translate(571 335) rotate(-20)" stroke="#45513f" stroke-width="1.5" fill="none">
    <ellipse cx="0" cy="0" rx="5" ry="11" fill="#45513f"/><circle cy="-15" r="4" fill="#45513f"/>
    <ellipse cx="-10" cy="-6" rx="7" ry="13" transform="rotate(-30 -10 -6)"/><ellipse cx="10" cy="-6" rx="7" ry="13" transform="rotate(30 10 -6)"/>
    <path d="M-4-5l-13-9M4-5l13-9M-4 1l-15 3M4 1l15 3M-4 6l-9 13M4 6l9 13"/>
  </g>
''')


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    cv()
    linkedin()
    login()
    benzin()
    hyprchan()
    stonkfly()
