from pathlib import Path
import json, shutil, sys

if len(sys.argv) != 2:
    raise SystemExit("usage: apply_overlay.py <dashboard-output-dir>")

dest = Path(sys.argv[1]).resolve()
src = Path(__file__).resolve().parent
logo_src = src / "lyvra-browser-logo.png"
logo_dst = dest / "assets" / "branding" / "lyvra-browser-logo.png"
logo_dst.parent.mkdir(parents=True, exist_ok=True)
shutil.copy2(logo_src, logo_dst)

index = dest / "index.html"
html = index.read_text(encoding="utf-8")
head_marker = "<title>LYVRA · NEON COMMAND DASHBOARD</title>"
head_add = """<title>LYVRA · NEON COMMAND DASHBOARD</title>
<link rel="icon" type="image/png" sizes="192x192" href="assets/branding/lyvra-browser-logo.png">
<link rel="apple-touch-icon" sizes="192x192" href="assets/branding/lyvra-browser-logo.png">
<link rel="manifest" href="site.webmanifest">
<meta name="theme-color" content="#05030a">"""
if 'lyvra-browser-logo.png' not in html:
    html = html.replace(head_marker, head_add, 1)
hero_marker = '<header class="hero"><div class="brand">'
hero_add = '<header class="hero"><div class="browserBrandMark"><img src="assets/branding/lyvra-browser-logo.png" width="192" height="192" alt="LYVRA Cyber-Emblem" decoding="async" fetchpriority="high"></div><div class="brand">'
if 'class="browserBrandMark"' not in html:
    html = html.replace(hero_marker, hero_add, 1)
index.write_text(html, encoding="utf-8")

css = dest / "assets" / "runtime" / "dashboard.css"
style = css.read_text(encoding="utf-8")
rule = """
/* LYVRA browser/site emblem */
.browserBrandMark{display:flex;justify-content:center;align-items:center;margin:0 auto 12px;pointer-events:none}
.browserBrandMark img{width:clamp(132px,18vw,220px);height:auto;display:block;object-fit:contain;filter:drop-shadow(0 0 18px rgba(0,232,255,.42)) drop-shadow(0 0 26px rgba(255,0,214,.28))}
@media (max-width:640px){.browserBrandMark img{width:132px}.browserBrandMark{margin-bottom:8px}}
"""
if "/* LYVRA browser/site emblem */" not in style:
    css.write_text(style + rule, encoding="utf-8")

manifest = {
    "name": "LYVRA Dashboard",
    "short_name": "LYVRA",
    "description": "LYVRA Neon Command Dashboard",
    "start_url": "/",
    "scope": "/",
    "display": "standalone",
    "background_color": "#05030a",
    "theme_color": "#05030a",
    "icons": [
        {
            "src": "/assets/branding/lyvra-browser-logo.png",
            "sizes": "192x192",
            "type": "image/png"
        }
    ]
}
(dest / "site.webmanifest").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
