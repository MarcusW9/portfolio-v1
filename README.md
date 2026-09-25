# Marcus Wong — Portfolio

Personal portfolio for Marcus Wong, Senior Product Manager (London).

**Live site:** https://marcusw9.github.io/portfolio/ (once GitHub Pages is enabled)

## Structure

```
index.html      ← built page served by GitHub Pages (don't edit by hand)
src/page.html   ← the editable source: markup, styles and scripts in one file
build.py        ← wraps src/page.html into a full HTML document → index.html
favicon.svg     ← browser tab icon
.nojekyll       ← tells GitHub Pages to serve files as-is
```

The site is a single self-contained page: no framework, no build tools beyond
Python 3, no external assets except Google Fonts.

## Updating the site

1. Edit `src/page.html`
2. Run `python3 build.py`
3. Commit and push — GitHub Pages redeploys automatically in about a minute

## Enabling GitHub Pages (one-time)

Repo → **Settings** → **Pages** → Source: **Deploy from a branch** →
Branch: **main**, folder **/ (root)** → Save.

### Custom domain (optional)

Add a `CNAME` file containing your domain (e.g. `marcuswong.co.uk`), point the
domain's DNS at GitHub Pages, and update `SITE_URL` in `build.py`.
