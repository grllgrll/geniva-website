"""Generate the English-first Geniva site and Turkish equivalents."""
from pathlib import Path
from html import escape
import json
from urllib.parse import quote
from site_pages import CONTENT, render_page

ROOT = Path(__file__).resolve().parent
ORIGIN = 'https://geniva-web.ozkanozdemir.chatgpt.site'
PAGES = ['index', 'solutions', 'software', 'hardware', 'training', 'about', 'references', 'careers', 'contact']
CHANNEL = 'https://www.youtube.com/@GennextCommunity'
ADDRESS = 'İçerenköy Mah. Kayışdağı Cad. Acıbadem Üniversitesi Tıp Fakültesi, C Blok No: 32-36C, TEKMER, Ataşehir / İstanbul'
MAPS = 'https://www.google.com/maps/search/?api=1&query=' + quote(ADDRESS)
VERSION = '20261116d'

def brand():
    return '<span class="brand">geniva<span aria-hidden="true">.</span></span>'

def header(lang, page):
    d = CONTENT[lang]
    nav = []
    for key in ['index', 'solutions', 'about', 'references', 'careers']:
        current = ' aria-current="page"' if key == page else ''
        if key == 'solutions':
            links = ''.join(f'<a href="{p}.html"' + (' aria-current="page"' if p == page else '') + f'>{d["names"][p]}</a>' for p in ['solutions', 'software', 'hardware', 'training'])
            active = 'active' if page in ['solutions','software','hardware','training'] else ''
            nav.append(f'<details class="nav-group"><summary class="{active}">{d["names"][key]}<span aria-hidden="true">⌄</span></summary><div class="nav-sub">{links}</div></details>')
        else:
            nav.append(f'<a href="{key}.html"{current}>{d["names"][key]}</a>')
    en = '../' + page + '.html' if lang == 'tr' else page + '.html'
    tr = page + '.html' if lang == 'tr' else 'tr/' + page + '.html'
    languages = f'<nav class="language" aria-label="{d["language"]}"><a href="{en}" lang="en" data-language'+(' aria-current="true"' if lang == 'en' else '')+f'>EN</a><span aria-hidden="true">/</span><a href="{tr}" lang="tr" data-language'+(' aria-current="true"' if lang == 'tr' else '')+'>TR</a></nav>'
    mobile_languages = languages.replace('class="language"','class="language mobile-language"')
    contact_label = 'İletişim' if lang == 'tr' else 'Contact Us'
    contact_button = f'<a class="header-contact" href="contact.html">{contact_label}</a>'
    return f'<a class="skip" href="#main">{d["skip"]}</a><header class="site-header"><div class="container nav-inner"><a href="index.html" aria-label="Geniva - {d["names"]["index"]}">{brand()}</a><nav class="nav-links" id="navigation" aria-label="{d["navigation"]}">{"".join(nav)}{mobile_languages}</nav><div class="nav-tools">{languages}<button class="menu-toggle" type="button" aria-expanded="false" aria-controls="navigation">{d["menu"]}</button>{contact_button}</div></div></header>'

def footer(lang, prefix):
    d = CONTENT[lang]
    solutions = ''.join(f'<a href="{page}.html">{d["names"][page]}</a>' for page in ['software', 'hardware', 'training'])
    company = ''.join(f'<a href="{page}.html">{d["names"][page]}</a>' for page in ['about', 'references', 'careers', 'contact'])
    return f'''<footer class="site-footer"><div class="container"><div class="footer-top">
    <div class="footer-brand"><a href="index.html" aria-label="Geniva">{brand()}</a><p>{d['tagline']}</p><a href="https://gennext.bio" target="_blank" rel="noopener">Gennext ↗</a><a href="{CHANNEL}" target="_blank" rel="noopener">YouTube · Gennext Community ↗</a></div>
    <nav class="footer-nav" aria-label="{d['names']['solutions']}"><h2>{d['names']['solutions']}</h2>{solutions}</nav>
    <nav class="footer-nav" aria-label="{d['company']}"><h2>{d['company']}</h2>{company}<a href="{prefix}assets/gennext-somatic-{lang}.pdf" target="_blank" rel="noopener">{d['brochure']} ↗</a></nav>
    <div class="footer-nav"><h2>{d['names']['contact']}</h2><a href="mailto:info@gennext.bio">info@gennext.bio</a><a href="tel:+902162504471">+90 216 250 4471</a><address>{ADDRESS}</address><a href="{MAPS}" target="_blank" rel="noopener">{d['map']} ↗</a></div>
    </div><div class="footer-bottom"><span>© 2026 Geniva Bilişim Sağlık A.Ş.</span><span>{d['rights']}</span></div></div></footer>'''

def build():
    reference_data = json.loads((ROOT / 'assets/reference-data.json').read_text())
    generated = []
    for lang in ['en', 'tr']:
        d = CONTENT[lang]
        prefix = '../' if lang == 'tr' else ''
        out = ROOT / 'tr' if lang == 'tr' else ROOT
        out.mkdir(exist_ok=True)
        for page in PAGES:
            title, description = d['metadata'][page]
            en_url = f'{ORIGIN}/{page}.html'
            tr_url = f'{ORIGIN}/tr/{page}.html'
            canonical = tr_url if lang == 'tr' else en_url
            body = render_page(page, lang, prefix, reference_data, ADDRESS, MAPS)
            preload = f'<link rel="preload" as="image" href="{prefix}assets/hero.webp">' if page == 'index' else ''
            html = f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)}</title><meta name="description" content="{escape(description,quote=True)}"><meta name="theme-color" content="#101f3d"><meta name="robots" content="noindex,follow"><link rel="canonical" href="{canonical}"><link rel="alternate" hreflang="en" href="{en_url}"><link rel="alternate" hreflang="tr" href="{tr_url}"><link rel="alternate" hreflang="x-default" href="{en_url}"><meta property="og:type" content="website"><meta property="og:site_name" content="Geniva"><meta property="og:title" content="{escape(title,quote=True)}"><meta property="og:description" content="{escape(description,quote=True)}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="{ORIGIN}/assets/hero.webp"><link rel="icon" type="image/svg+xml" href="{prefix}assets/favicon.svg"><link rel="preload" as="font" type="font/woff2" crossorigin href="{prefix}assets/source-sans-3.woff2">{preload}<link rel="stylesheet" href="{prefix}styles.css?v={VERSION}"><script src="{prefix}app.js?v={VERSION}" defer></script></head><body>{header(lang,page)}<main id="main" tabindex="-1" data-page="{page}">{body}</main>{footer(lang,prefix)}</body></html>'''
            path = out / (page + '.html')
            path.write_text(html)
            generated.append(path.relative_to(ROOT))
    # Keep existing /en/ URLs working, including shared section links.
    alias_dir = ROOT / 'en'
    alias_dir.mkdir(exist_ok=True)
    for page in PAGES:
        target = '../' + page + '.html'
        alias = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Geniva</title><meta name="robots" content="noindex,follow"><link rel="canonical" href="{ORIGIN}/{page}.html"><meta http-equiv="refresh" content="0;url={target}"><script>location.replace({json.dumps(target)}+location.search+location.hash);</script></head><body><p><a href="{target}">Continue to Geniva</a></p></body></html>'''
        path = alias_dir / (page + '.html')
        path.write_text(alias)
        generated.append(path.relative_to(ROOT))
    print(f'Built {len(PAGES)*2} bilingual pages and {len(PAGES)} legacy English redirects.')
    return generated

if __name__ == '__main__':
    build()
