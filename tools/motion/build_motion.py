"""Bouwt de logo-animatie:
- assets/motion/intro.html  (voor de website; laadt bibliotheken uit assets/vendor)
- dist/saasprojects-intro.html  (los bestand: alles erin, ook bibliotheken en lettertype)
Gebruik: python3 tools/motion/build_motion.py
"""
import base64
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
tpl = (ROOT / "tools/motion/intro.template.html").read_text(encoding="utf-8")
logo_d = re.search(r' d="([^"]+)"', (ROOT / "assets/logo.svg").read_text()).group(1)
house_d = re.search(r' d="([^"]+)"', (ROOT / "assets/house.svg").read_text()).group(1)
tpl = tpl.replace("%%LOGO_D%%", logo_d).replace("%%HOUSE_D%%", house_d)

site = (tpl.replace("%%FONT%%", "../fonts/montserrat.woff2")
           .replace('<script src="%%THREE%%"></script>', '<script src="../vendor/three.min.js"></script>')
           .replace('<script src="%%SVGLOADER%%"></script>', '<script src="../vendor/SVGLoader.js"></script>')
           .replace('<script src="%%GSAP%%"></script>', '<script src="../vendor/gsap.min.js"></script>'))
(ROOT / "assets/motion").mkdir(parents=True, exist_ok=True)
(ROOT / "assets/motion/intro.html").write_text(site, encoding="utf-8")

def inline(path):
    return "<script>\n" + (ROOT / path).read_text(encoding="utf-8").replace("</script", "<\\/script") + "\n</script>"

font = base64.b64encode((ROOT / "assets/fonts/montserrat.woff2").read_bytes()).decode()
single = (tpl.replace("%%FONT%%", "data:font/woff2;base64," + font)
             .replace('<script src="%%THREE%%"></script>', inline("assets/vendor/three.min.js"))
             .replace('<script src="%%SVGLOADER%%"></script>', inline("assets/vendor/SVGLoader.js"))
             .replace('<script src="%%GSAP%%"></script>', inline("assets/vendor/gsap.min.js")))
out = ROOT / "dist"
out.mkdir(exist_ok=True)
(out / "saasprojects-intro.html").write_text(single, encoding="utf-8")
print("ok", len(site), len(single))
