# saasprojects.nl

Overkoepelende website van Saas Projects met alle ondernemingen: kozijnmontage (kunststof en aluminium, heel Nederland), verkoop via bol.com, webwinkels en fietsenwinkel VanWiel.
Een snelle statische site: geen WordPress of sitebouwer, geen tracking-cookies, dus ook geen cookiebanner nodig.

## Inhoud

| Bestand | Wat |
| --- | --- |
| `index.html` | Homepage: overzicht van alle ondernemingen, verhaal, principes, contact |
| `kozijnen.html` | Kozijnen & renovatie: diensten, kunststof vs. aluminium, glas & opties, werkwijze, montagedag, renovatie, onderhoud, FAQ |
| `vanwiel.html` | VanWiel: concept, werkwijze, fietskeuzehulp, maatwijzer, onderhoud, FAQ |
| `bol.html` | Bol.com (huis, tuin & keuken): aanpak, categorieën, selectie, service, leveranciers, FAQ |
| `webwinkels.html` | Webwinkels: model, van idee tot winkel, standaard, leveranciers & partners, FAQ |
| `over.html` | Het verhaal, tijdlijn, principes en alle ondernemingen |
| `privacybeleid.html` | AVG-privacybeleid |
| `juridische-kennisgeving.html` | Bedrijfsgegevens (KvK, btw) |
| `bedankt.html` | Bedankpagina na het versturen van het formulier |
| `assets/` | Stijl, script, iconen, lettertype (Montserrat, zelf gehost) en geoptimaliseerde foto's |
| `CNAME`, `.nojekyll`, `404.html` | Instellingen voor GitHub Pages, foutpagina |
| `over-ons/`, `contacteer-ons/`, `feed/` | Doorverwijzingen van adressen van de vorige website |

## Lokaal bekijken

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## Nog in te vullen

Portret en naam zijn ingevuld (`assets/img/ondernemer.webp`). Een nieuwe foto? Vervang dat bestand (staand, 4:5).

## Online zetten (GitHub Pages + domein bij Strato)

Het domein en de e-mail staan bij Strato. De website staat gratis op GitHub Pages en wordt bij elke wijziging automatisch bijgewerkt.

1. **GitHub Pages:** in de (openbare) repository, *Settings, Pages*: *Source* = *Deploy from a branch*, branch kiezen, map `/ (root)`. Het bestand `CNAME` zet het domein `saasprojects.nl` vast. Zet *Enforce HTTPS* aan zodra dat kan.
2. **DNS bij Strato** (*Domeinen, Domeinbeheer*, tandwiel, *DNS*):
   - A-record `saasprojects.nl`: `185.199.108.153` (eventueel ook `.109`, `.110`, `.111`)
   - `www`: CNAME naar `yannick076.github.io`, of dezelfde A-record
   - **MX-record niet wijzigen** (e-mail).
3. **Formulieren:** via Web3Forms. Vul de sleutel in bij `WEB3FORMS_KEY` in `tools/build.py` en bouw de pagina's opnieuw.

## Pagina's aanpassen en opnieuw bouwen

De HTML-pagina's worden gemaakt met `tools/build.py`: de gedeelde kop, voet en contactformulieren staan in dat script, de inhoud per pagina in `tools/src/<pagina>.py`. Na een wijziging:

```bash
python3 tools/build.py tools/src .
```

## Aanpassen

- Teksten staan direct in de HTML-bestanden.
- Kleuren staan bovenaan `assets/css/style.css` (`--ivory`, `--night`, `--bronze` = blauw accent).
- Eigen projectfoto's? Zet ze in `assets/img/` (bij voorkeur `.webp`, ca. 1600px breed) en vervang de bestandsnamen in `index.html`.
