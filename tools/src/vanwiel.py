META = {
    "file": "vanwiel.html",
    "path": "vanwiel",
    "current": "vanwiel.html",
    "title": "VanWiel, de online fietsenwinkel van Saas Projects",
    "description": "VanWiel is de online fietsenwinkel van Saas Projects voor fietsen, e-bikes en accessoires, in Nederland, België, Duitsland, Frankrijk en Oostenrijk. Kies online, laat hem thuis bezorgen en krijg persoonlijk advies. Met fietskeuzehulp en onderhoudstips.",
    "ld": {
        "@context": "https://schema.org",
        "@type": "OnlineStore",
        "name": "VanWiel",
        "url": "https://vanwiel.nl",
        "email": "info@vanwiel.nl",
        "sameAs": ["https://vanwiel.be", "https://vanwiel.de", "https://vanwiel.fr", "https://vanwiel.at"],
        "areaServed": ["NL", "BE", "DE", "FR", "AT"],
        "parentOrganization": {"@type": "Organization", "name": "Saas Projects", "url": "https://saasprojects.nl/"},
    },
}

BODY = f'''
    <section class="page-hero page-hero--night">
      <span class="page-hero__mark" aria-hidden="true">VanWiel</span>
      <div class="container">
        <span class="label">Online fietsenwinkel</span>
        <h1>VanWiel. <em>Fietsen, zonder gedoe.</em></h1>
        <p class="lede">Een nieuwe fiets uitkiezen hoort leuk te zijn. Bij VanWiel kiest u online uit fietsen, e-bikes en accessoires, in uw eigen tempo, en laat u uw bestelling thuis bezorgen. Met persoonlijk advies wanneer u dat wilt.</p>
        <div style="margin-top:40px;display:flex;gap:28px;flex-wrap:wrap">
          <a class="btn btn--light" href="https://vanwiel.nl" rel="noopener">Naar vanwiel.nl <svg aria-hidden="true"><use href="assets/icons.svg#external"/></svg></a>
        </div>
        <div class="page-hero__meta">
          <div><small>Assortiment</small><span>Fietsen, e-bikes &amp; accessoires</span></div>
          <div><small>Bestellen</small><span>Online, 24/7</span></div>
          <div><small>Levering</small><span>Thuisbezorgd in 5 landen</span></div>
          <div><small>Onderdeel van</small><span>Saas Projects</span></div>
        </div>
      </div>
    </section>

    <nav class="subnav" aria-label="Op deze pagina">
      <div class="container">
        <ul>
          <li><a href="#concept">Het concept</a></li>
          <li><a href="#assortiment">Assortiment</a></li>
          <li><a href="#hoe">Zo werkt het</a></li>
          <li><a href="#keuzehulp">Fietskeuzehulp</a></li>
          <li><a href="#maat">De juiste maat</a></li>
          <li><a href="#landen">Landen</a></li>
          <li><a href="#onderhoud">Onderhoud</a></li>
          <li><a href="#vragen">Vragen</a></li>
        </ul>
      </div>
    </nav>

    <section class="section" id="concept">
      <div class="container two-col">
        <p class="pull reveal">Nederland is een fietsland. Dan verdient iedereen <em>een fiets die past.</em></p>
        <div class="reveal">
          <p>VanWiel is ontstaan uit een eenvoudige gedachte: een fiets kopen moet overzichtelijk, eerlijk en prettig zijn. Geen verkooppraatjes, geen eindeloos zoeken, maar een heldere winkel waar u in alle rust kunt vergelijken en kiezen.</p>
          <p>Achter VanWiel staat dezelfde ondernemer als achter Saas Projects. Dat betekent dezelfde standaard: duidelijke informatie, afspraken die we nakomen en persoonlijk contact als u een vraag heeft. U spreekt niet met een callcenter, maar met mensen die het verschil kennen tussen een fiets en de juiste fiets.</p>
          <a class="link" href="https://vanwiel.nl" rel="noopener" style="margin-top:12px">Bekijk het assortiment <svg aria-hidden="true"><use href="assets/icons.svg#external"/></svg></a>
        </div>
      </div>
    </section>

    <section class="section section--paper" id="assortiment">
      <div class="container">
        <div class="section-head">
          <div class="reveal">
            <span class="label">Assortiment</span>
            <h2>Alles voor <em>onderweg.</em></h2>
          </div>
          <p class="lede reveal" style="max-width:26em;margin:0">Van de dagelijkse fiets tot de elektrische fiets voor langere afstanden, en alles wat erbij hoort.</p>
        </div>
        <div class="tiles">
          <article class="tile reveal"><h3>Fietsen</h3><p>Voor de dagelijkse rit naar werk of school, of om te ontspannen in het weekend.</p></article>
          <article class="tile reveal"><h3>E-bikes</h3><p>Elektrische ondersteuning voor langere afstanden, tegenwind en wie zonder moeite wil fietsen.</p></article>
          <article class="tile reveal"><h3>Accessoires</h3><p>De onderdelen en extra's die uw fiets compleet, veilig en comfortabel maken.</p></article>
        </div>
        <p class="reveal" style="margin-top:48px"><a class="link" href="https://vanwiel.nl" rel="noopener">Bekijk het volledige assortiment op vanwiel.nl <svg aria-hidden="true"><use href="assets/icons.svg#external"/></svg></a></p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <div class="reveal">
            <span class="label">Waarom VanWiel</span>
            <h2>De winkel, <em>opnieuw bedacht.</em></h2>
          </div>
        </div>
        <div class="tiles tiles--4">
          <div class="tile reveal"><h3>In uw eigen tempo</h3><p>Vergelijk modellen wanneer het u uitkomt, 's avonds op de bank of in de pauze.</p></div>
          <div class="tile reveal"><h3>Heldere informatie</h3><p>Duidelijke specificaties en eerlijke beschrijvingen, zodat u weet wat u koopt.</p></div>
          <div class="tile reveal"><h3>Thuisbezorgd</h3><p>Geen gesleep: uw nieuwe fiets komt naar u toe.</p></div>
          <div class="tile reveal"><h3>Persoonlijk advies</h3><p>Twijfelt u? Stel uw vraag en krijg een eerlijk antwoord van iemand die meedenkt.</p></div>
        </div>
      </div>
    </section>

    <section class="section section--night" id="hoe">
      <div class="container">
        <div class="reveal">
          <span class="label">Zo werkt het</span>
          <h2 style="margin-top:22px">In vier stappen <em>op de fiets.</em></h2>
        </div>
        <ol class="steps">
          <li class="reveal"><h3>Kiezen</h3><p>Bekijk het assortiment op vanwiel.nl en vergelijk de modellen die bij u passen.</p></li>
          <li class="reveal"><h3>Advies</h3><p>Twijfelt u over model of maat? Neem contact op, we helpen u graag kiezen.</p></li>
          <li class="reveal"><h3>Bestellen</h3><p>Bestel eenvoudig en veilig online. U ontvangt direct een bevestiging.</p></li>
          <li class="reveal"><h3>Fietsen</h3><p>Uw fiets wordt thuisbezorgd. Even afstellen, en u kunt op weg.</p></li>
        </ol>
      </div>
    </section>

    <section class="section" id="keuzehulp">
      <div class="container">
        <div class="section-head">
          <div class="reveal">
            <span class="label">Fietskeuzehulp</span>
            <h2>Welke fiets <em>past bij u?</em></h2>
          </div>
          <p class="lede reveal" style="max-width:26em;margin:0">Begin niet bij de fiets, maar bij uw ritten. Waar fietst u heen, hoe ver en hoe vaak? Dit overzicht helpt u op weg.</p>
        </div>
        <div class="tiles tiles--2">
          <article class="tile reveal"><h3>Dagelijks naar werk of school</h3>
            <p>U fietst vaak, bij elk weer. Kies voor betrouwbaarheid en comfort.</p>
            <ul><li>Let op: goede verlichting en spatborden</li><li>Een bagagedrager of tassenhouder</li><li>Versnellingen voor wind en bruggen</li></ul>
          </article>
          <article class="tile reveal"><h3>Langere afstanden</h3>
            <p>Woon-werk boven de tien kilometer of veel tegenwind? Een elektrische fiets maakt elke rit lichter.</p>
            <ul><li>Let op: actieradius van de accu</li><li>Waar en hoe u de accu oplaadt</li><li>Een stevig frame en goede remmen</li></ul>
          </article>
          <article class="tile reveal"><h3>Ontspannen toeren</h3>
            <p>Voor het weekend, de natuur in of een terrasje. Comfort en zithouding staan voorop.</p>
            <ul><li>Let op: rechtop zitten, comfortabel zadel</li><li>Een lage instap als u dat prettig vindt</li><li>Ruimte voor een tas of mand</li></ul>
          </article>
          <article class="tile reveal"><h3>Sportief rijden</h3>
            <p>U wilt snelheid, afstand of trainen. Een lichte fiets met een sportievere houding past beter.</p>
            <ul><li>Let op: gewicht en versnellingen</li><li>Een goed passend frame</li><li>Bandbreedte passend bij de ondergrond</li></ul>
          </article>
        </div>
      </div>
    </section>

    <section class="section section--paper" id="maat">
      <div class="container two-col">
        <div class="reveal">
          <span class="label">De juiste maat</span>
          <h2 style="margin-top:22px">Een fiets die <em>als gegoten zit.</em></h2>
          <p style="margin-top:28px">Een fiets in de verkeerde maat fietst nooit fijn, hoe mooi hij ook is. Gelukkig is de juiste maat eenvoudig te bepalen.</p>
        </div>
        <div class="reveal">
          <ol class="checklist">
            <li><div><b>Meet uw binnenbeenlengte</b><span>Ga op blote voeten met de rug tegen de muur staan en meet van de vloer tot in het kruis.</span></div></li>
            <li><div><b>Bereken een indicatie</b><span>Voor een stads- of toerfiets geeft uw binnenbeenlengte × 0,66 een goede indicatie van de framehoogte in centimeters.</span></div></li>
            <li><div><b>Bekijk de maattabel</b><span>Vergelijk de uitkomst met de maatinformatie bij het model. Merken kunnen iets van elkaar verschillen.</span></div></li>
            <li><div><b>Twijfelt u?</b><span>Zit u tussen twee maten in, neem dan contact op. We kijken graag met u mee.</span></div></li>
          </ol>
        </div>
      </div>
    </section>

    <section class="section" id="landen">
      <div class="container">
        <div class="section-head">
          <div class="reveal">
            <span class="label">Landen</span>
            <h2>Vijf landen, <em>één winkel.</em></h2>
          </div>
          <p class="lede reveal" style="max-width:26em;margin:0">VanWiel verkoopt en levert in Nederland, België, Duitsland, Frankrijk en Oostenrijk. Alle landen bestellen in dezelfde winkel: vanwiel.be, .de, .fr en .at brengen u direct naar vanwiel.nl.</p>
        </div>
        <div class="countries">
          <a class="country reveal" href="https://vanwiel.nl" rel="noopener"><span class="country__code">NL</span><span class="country__name">Nederland</span><span class="country__domain">Levering via vanwiel.nl <svg aria-hidden="true"><use href="assets/icons.svg#external"/></svg></span></a>
          <a class="country reveal" href="https://vanwiel.nl" rel="noopener"><span class="country__code">BE</span><span class="country__name">België</span><span class="country__domain">Levering via vanwiel.nl <svg aria-hidden="true"><use href="assets/icons.svg#external"/></svg></span></a>
          <a class="country reveal" href="https://vanwiel.nl" rel="noopener"><span class="country__code">DE</span><span class="country__name">Duitsland</span><span class="country__domain">Levering via vanwiel.nl <svg aria-hidden="true"><use href="assets/icons.svg#external"/></svg></span></a>
          <a class="country reveal" href="https://vanwiel.nl" rel="noopener"><span class="country__code">FR</span><span class="country__name">Frankrijk</span><span class="country__domain">Levering via vanwiel.nl <svg aria-hidden="true"><use href="assets/icons.svg#external"/></svg></span></a>
          <a class="country reveal" href="https://vanwiel.nl" rel="noopener"><span class="country__code">AT</span><span class="country__name">Oostenrijk</span><span class="country__domain">Levering via vanwiel.nl <svg aria-hidden="true"><use href="assets/icons.svg#external"/></svg></span></a>
        </div>
      </div>
    </section>

    <section class="section section--paper" id="onderhoud">
      <div class="container">
        <div class="section-head">
          <div class="reveal">
            <span class="label">Onderhoud</span>
            <h2>Langer plezier <em>van uw fiets.</em></h2>
          </div>
          <p class="lede reveal" style="max-width:26em;margin:0">Een paar minuten aandacht per maand voorkomt de meeste problemen.</p>
        </div>
        <div class="tiles tiles--4">
          <div class="tile reveal"><h3>Bandenspanning</h3><p>Controleer maandelijks. De juiste spanning staat op de zijkant van de band.</p></div>
          <div class="tile reveal"><h3>Ketting</h3><p>Schoonmaken en licht smeren, zeker na regen of in de winter.</p></div>
          <div class="tile reveal"><h3>Remmen</h3><p>Voelt de rem anders aan of piept hij? Laat hem op tijd nakijken.</p></div>
          <div class="tile reveal"><h3>Accu</h3><p>Bij een e-bike: bewaar de accu droog en op kamertemperatuur, ook in de winter.</p></div>
        </div>
      </div>
    </section>

    <section class="section" id="vragen">
      <div class="container two-col">
        <div class="reveal">
          <span class="label">Veelgestelde vragen</span>
          <h2 style="margin-top:22px">Goed om <em>te weten.</em></h2>
          <p style="margin-top:28px">Kijk voor bezorging, garantie en voorwaarden altijd op <a href="https://vanwiel.nl" rel="noopener">vanwiel.nl</a>.</p>
        </div>
        <div class="faq reveal">
          <details><summary>Waar kan ik een fiets bestellen?</summary><div><p>Alle fietsen bestelt u op <a href="https://vanwiel.nl" rel="noopener">vanwiel.nl</a>. Daar vindt u ook de actuele prijzen, levertijden en voorwaarden.</p></div></details>
          <details><summary>Wordt mijn fiets thuisbezorgd?</summary><div><p>Ja, uw fiets wordt bij u thuis bezorgd. De verwachte levertijd ziet u bij het product en in uw orderbevestiging.</p></div></details>
          <details><summary>Kan ik mijn fiets retourneren?</summary><div><p>Bij een online aankoop heeft u wettelijk 14 dagen bedenktijd. Hoe retourneren precies werkt, leest u in de voorwaarden op vanwiel.nl.</p></div></details>
          <details><summary>Ik twijfel over de maat. Wat nu?</summary><div><p>Gebruik de <a href="#maat">maatwijzer</a> hierboven als eerste indicatie en neem contact op als u twijfelt. We helpen u graag de juiste maat te kiezen.</p></div></details>
          <details><summary>In welke landen leveren jullie?</summary><div><p>VanWiel levert in Nederland, België, Duitsland, Frankrijk en Oostenrijk. U bestelt overal via <a href="https://vanwiel.nl" rel="noopener">vanwiel.nl</a>; ook vanwiel.be, vanwiel.de, vanwiel.fr en vanwiel.at brengen u daar.</p></div></details>
          <details><summary>Hoe bereik ik VanWiel?</summary><div><p>Mail naar <a href="mailto:info@vanwiel.nl">info@vanwiel.nl</a>. We reageren zo snel mogelijk.</p></div></details>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="cta-panel reveal">
          <div>
            <span class="label">VanWiel</span>
            <h2 style="margin-top:22px">Klaar voor <em>uw nieuwe fiets?</em></h2>
            <p>Bekijk het volledige assortiment en bestel online.</p>
          </div>
          <div class="actions">
            <a class="btn btn--light" href="https://vanwiel.nl" rel="noopener">Naar vanwiel.nl <svg aria-hidden="true"><use href="assets/icons.svg#external"/></svg></a>
            <a class="link" href="mailto:info@vanwiel.nl">info@vanwiel.nl {ARROW}</a>
          </div>
        </div>
      </div>
    </section>

'''
