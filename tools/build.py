"""Builds the saasprojects.nl pages from src/*.html fragments with a shared layout."""
import hashlib
import json
import pathlib
import re
import sys

SRC = pathlib.Path(sys.argv[1])
OUT = pathlib.Path(sys.argv[2])

NAV = [
    ("webwinkels.html", "Webwinkels"),
    ("bol.html", "Bol.com"),
    ("kozijnen.html", "Kozijnen"),
    ("vanwiel.html", "VanWiel"),
    ("over.html", "Over"),
    ("./#contact", "Contact"),
]

ARROW = '<svg aria-hidden="true"><use href="assets/icons.svg#arrow"/></svg>'

# Web3Forms access key (openbaar bedoeld; aan te vragen op web3forms.com met info@saasprojects.nl)
WEB3FORMS_KEY = "5a45a47b-115b-4865-8482-a3fdf79f6954"


def header(current, dark):
    links = "\n".join(
        f'        <a href="{href}"{" aria-current=\"page\"" if href == current else ""}>{name}</a>'
        for href, name in NAV
    )
    cls = "header header--dark" if dark else "header header--solid"
    return f'''  <header class="{cls}">
    <div class="container header__inner">
      <a class="brand" href="./" aria-label="Saas Projects, naar home"><span class="logo" role="img" aria-label="Saas Projects"></span></a>
      <button class="nav-toggle" aria-expanded="false" aria-controls="nav">Menu</button>
      <nav class="nav" id="nav" aria-label="Hoofdmenu">
{links}
      </nav>
    </div>
  </header>'''


FOOTER = '''  <footer class="footer">
    <div class="container">
      <div class="footer__grid" style="padding-top:0">
        <div>
          <a class="brand brand--footer" href="./" aria-label="Saas Projects, naar home"><span class="logo" role="img" aria-label="Saas Projects"></span></a>
          <p style="max-width:26em">Webwinkels, verkoop via bol.com, kozijnmontage door heel Nederland en fietsenwinkel VanWiel.</p>
        </div>
        <div>
          <h4>Ondernemingen</h4>
          <ul>
            <li><a href="webwinkels.html">Webwinkels</a></li>
            <li><a href="bol.html">Bol.com</a></li>
            <li><a href="kozijnen.html">Kozijnen</a></li>
            <li><a href="vanwiel.html">VanWiel</a></li>
            <li>Nieuw project <span style="opacity:.55">(binnenkort)</span></li>
          </ul>
        </div>
        <div>
          <h4>Contact</h4>
          <ul>
            <li><a href="tel:+31626889789">06-26889789</a></li>
            <li><a href="mailto:info@saasprojects.nl">info@saasprojects.nl</a></li>
            <li>Hallenweg 16<br>5683 CT Best<br><span class="addr-note">Geen bezoekadres</span></li>
          </ul>
        </div>
        <div>
          <h4>Gegevens</h4>
          <ul>
            <li>KvK 81568827</li>
            <li>Btw NL003577672B78</li>
            <li><a href="over.html">Over Saas Projects</a></li>
            <li><a href="juridische-kennisgeving.html">Juridisch</a></li>
            <li><a href="privacybeleid.html">Privacy</a></li>
          </ul>
        </div>
      </div>
      <div class="footer__bottom">
        <span>© <span id="year">2026</span> Saas Projects</span>
        <span>Geen tracking-cookies</span>
      </div>
    </div>
  </footer>'''


def contact_form(name, subject_options=None, phone=False, title="Neem <em>contact</em> op.", lede=None, paper=False):
    lede = lede or "Een vraag, een idee of interesse in samenwerking? Laat het weten. U hoort snel van ons."
    subject = ""
    if subject_options:
        opts = "\n".join(f"              <option>{o}</option>" for o in subject_options)
        subject = f'''          <div class="field">
            <label for="onderwerp">Onderwerp</label>
            <select id="onderwerp" name="onderwerp">
{opts}
            </select>
          </div>
'''
    second = ('<div class="field"><label for="telefoon">Telefoon (optioneel)</label><input id="telefoon" name="telefoon" type="tel" autocomplete="tel"></div>'
              if phone else '<div class="field"><label for="email">E-mail</label><input id="email" name="email" type="email" autocomplete="email" required></div>')
    email_row = '          <div class="field"><label for="email">E-mail</label><input id="email" name="email" type="email" autocomplete="email" required></div>\n' if phone else ""
    cls = "section section--paper" if paper else "section"
    return f'''    <section class="{cls}" id="contact">
      <div class="container contact">
        <div class="reveal">
          <span class="label">Contact</span>
          <h2>{title}</h2>
          <p class="lede">{lede}</p>
          <ul class="details">
            <li><small>Telefoon</small><a href="tel:+31626889789">06-26889789</a></li>
            <li><small>WhatsApp</small><a href="https://wa.me/31626889789" rel="noopener">Stuur een bericht</a></li>
            <li><small>E-mail</small><a href="mailto:info@saasprojects.nl">info@saasprojects.nl</a></li>
            <li><small>Adres</small><span>Hallenweg 16, 5683 CT Best<br><span class="addr-note">Geen bezoekadres</span></span></li>
          </ul>
        </div>
        <form class="form reveal" name="{name}" method="POST" action="https://api.web3forms.com/submit">
          <input type="hidden" name="access_key" value="{WEB3FORMS_KEY}">
          <input type="hidden" name="subject" value="Nieuw bericht via saasprojects.nl ({name})">
          <input type="hidden" name="from_name" value="saasprojects.nl">
          <input type="hidden" name="redirect" value="https://saasprojects.nl/bedankt.html">
          <input type="checkbox" name="botcheck" class="hidden" tabindex="-1" autocomplete="off" aria-hidden="true">
          <div class="row">
            <div class="field"><label for="naam">Naam</label><input id="naam" name="naam" autocomplete="name" required></div>
            {second}
          </div>
{email_row}{subject}          <div class="field"><label for="bericht">Bericht</label><textarea id="bericht" name="bericht" required></textarea></div>
          <label class="check"><input type="checkbox" name="akkoord" required> <span>Ik ga akkoord dat mijn gegevens worden gebruikt om contact met mij op te nemen, zoals beschreven in het <a href="privacybeleid.html">privacybeleid</a>.</span></label>
          <button class="btn" type="submit">Verstuur bericht {ARROW}</button>
        </form>
      </div>
    </section>'''


def next_link(href, kind, name):
    return f'''    <div class="container">
      <a class="next reveal" href="{href}"><small>Volgende · {kind}</small><strong>{name} {ARROW}</strong></a>
    </div>'''


def page(meta, body):
    robots = '\n  <meta name="robots" content="noindex">' if meta.get("noindex") else ""
    canonical = f'\n  <link rel="canonical" href="https://saasprojects.nl/{meta["path"]}">' if "path" in meta else ""
    og = ""
    if "path" in meta:
        og = f'''
  <meta property="og:type" content="website">
  <meta property="og:locale" content="nl_NL">
  <meta property="og:site_name" content="Saas Projects">
  <meta property="og:title" content="{meta['title']}">
  <meta property="og:description" content="{meta['description']}">
  <meta property="og:url" content="https://saasprojects.nl/{meta['path']}">
  <meta property="og:image" content="https://saasprojects.nl/assets/img/og.jpg">'''
    base = '\n  <base href="/">' if meta.get("base") else ""
    ld = ""
    if meta.get("ld"):
        ld = "\n  <script type=\"application/ld+json\">\n  " + json.dumps(meta["ld"], ensure_ascii=False, indent=2).replace("\n", "\n  ") + "\n  </script>"
    return f'''<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">{base}
  <title>{meta['title']}</title>
  <meta name="description" content="{meta['description']}">{robots}{canonical}
  <meta name="theme-color" content="#121110">{og}
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
  <link rel="preload" href="assets/fonts/montserrat.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="assets/css/style.css?v={asset_version('assets/css/style.css')}">{ld}
</head>
<body>
  <a class="skip" href="#main">Naar de inhoud</a>

{header(meta.get('current', ''), meta.get('dark', True))}

  <main id="main">
{body}
  </main>

{FOOTER}

  <script src="assets/js/main.js?v={asset_version('assets/js/main.js')}" defer></script>
</body>
</html>
'''


def asset_version(path):
    p = OUT / path
    return hashlib.sha1(p.read_bytes()).hexdigest()[:8] if p.exists() else "1"


HELPERS = {"contact_form": contact_form, "next_link": next_link, "ARROW": ARROW, "WEB3FORMS_KEY": WEB3FORMS_KEY}

for src in sorted(SRC.glob("*.py")):
    scope = dict(HELPERS)
    exec(compile(src.read_text(encoding="utf-8"), str(src), "exec"), scope)
    html = page(scope["META"], scope["BODY"].strip("\n"))
    html = html.replace("__WEB3FORMS_KEY__", WEB3FORMS_KEY)
    (OUT / scope["META"]["file"]).write_text(html, encoding="utf-8")
    print("built", scope["META"]["file"])
