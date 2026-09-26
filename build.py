#!/usr/bin/env python3
"""Build index.html for GitHub Pages from src/page.html.

src/page.html is the editable source (the same fragment used for the Claude
preview). This wraps it in a full HTML document with head metadata, so the
repo root can be served directly by GitHub Pages.

Usage:  python3 build.py
"""
import pathlib, re

ROOT = pathlib.Path(__file__).parent
SITE_URL = "https://marcusw9.github.io/portfolio-v1/"   # update if you use a custom domain
DESC = ("Marcus Wong — Senior Product Manager in London. Marketplaces, 0→1 platforms "
        "and AI-led delivery. £12m+ GMV marketplace launch, £300K saved with an AI-built MVP.")

src = (ROOT / "src" / "page.html").read_text(encoding="utf-8")
split = src.index("</style>") + len("</style>")
head_part, body_part = src[:split], src[split:]
head_part = re.sub(r'<meta name="description"[^>]*>\n?', "", head_part)

head = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="{DESC}">
<meta property="og:type" content="website">
<meta property="og:title" content="Marcus Wong · Senior Product Manager">
<meta property="og:description" content="{DESC}">
<meta property="og:url" content="{SITE_URL}">
<meta name="twitter:card" content="summary">
<link rel="canonical" href="{SITE_URL}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<style>html,body{{margin:0}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
{head_part.strip()}
</head>
<body>"""

out = head + body_part.rstrip() + "\n</body>\n</html>\n"
(ROOT / "index.html").write_text(out, encoding="utf-8")
print(f"Built index.html ({len(out):,} bytes)")
