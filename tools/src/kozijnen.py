META = {
    "file": "kozijnen.html",
    "path": "kozijnen",
    "current": "kozijnen.html",
    "title": "Kunststof en aluminium kozijnen, door heel Nederland | Saas Projects",
    "description": "Saas Projects monteert kunststof en aluminium kozijnen en renoveert woningen, door heel Nederland. Advies, inmeten, montage en nazorg met één vast aanspreekpunt.",
    "ld": {
        "@context": "https://schema.org",
        "@type": "HomeAndConstructionBusiness",
        "name": "Saas Projects Kozijnen",
        "url": "https://saasprojects.nl/kozijnen",
        "image": "https://saasprojects.nl/assets/img/og.jpg",
        "telephone": "+31626889789",
        "email": "info@saasprojects.nl",
        "address": {"@type": "PostalAddress", "streetAddress": "Hallenweg 16", "postalCode": "5683 CT", "addressLocality": "Best", "addressRegion": "Noord-Brabant", "addressCountry": "NL"},
        "areaServed": {"@type": "Country", "name": "Nederland"},
        "vatID": "NL003577672B78",
        "parentOrganization": {"@type": "Organization", "name": "Saas Projects", "url": "https://saasprojects.nl/"},
    },
}

BODY = f'''
    <section class="hero hero--page">
      <div class="hero__text">
        <span class="label">Saas Projects Kozijnen</span>
        <h1>Kozijnen, <em>vakkundig geplaatst.</em></h1>
        <p class="hero__lede">Montage van kunststof en aluminium kozijnen en renovatie van bestaande woningen. Door heel Nederland, met één vast aanspreekpunt van het eerste gesprek tot de laatste kitnaad.</p>
        <div class="page-hero__meta">
          <div><small>Werkgebied</small><span>Heel Nederland</span></div>
          <div><small>Specialisme</small><span>Kunststof &amp; aluminium</span></div>
          <div><small>Ervaring</small><span>1500+ kozijnen</span></div>
          <div><small>Contact</small><span>Eén vast aanspreekpunt</span></div>
        </div>
      </div>
      <div class="hero__visual" aria-hidden="true"><div class="hero__art"><span class="hero__grid"></span><span class="hero__glow"></span><span class="hero__house"></span></div></div>
    </section>

    <nav class="subnav" aria-label="Op deze pagina">
      <div class="container">
        <ul>
          <li><a href="#diensten">Diensten</a></li>
          <li><a href="#vergelijking">Kunststof of aluminium</a></li>
          <li><a href="#opties">Glas &amp; opties</a></li>
          <li><a href="#werkwijze">Werkwijze</a></li>
          <li><a href="#renovatie">Renovatie</a></li>
          <li><a href="#onderhoud">Onderhoud</a></li>
          <li><a href="#vragen">Vragen</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </div>
    </nav>

    <section class="section">
      <div class="container two-col">
        <p class="pull reveal">Een kozijn is meer dan een raam. Het bepaalt <em>hoe een huis voelt</em>: warm, stil en licht.</p>
        <div class="reveal">
          <p>Nieuwe kozijnen gaan tientallen jaren mee. Daarom verdienen ze aandacht: de juiste keuze in materiaal en glas, een nauwkeurige inmeting en een montage waarbij elk detail klopt. Juist dat laatste maakt het verschil tussen een kozijn dat goed is en een kozijn dat goed blijft.</p>
          <p>Saas Projects is gespecialiseerd in de montage van kunststof en aluminium kozijnen. We werken voor particulieren en voor bedrijven, aan één raam of aan een complete woning. Wat we beloven, doen we, en we vertrekken pas als u tevreden bent.</p>
          <a class="link" href="#contact" style="margin-top:12px">Bespreek uw plannen {ARROW}</a>
        </div>
      </div>
    </section>

    <section class="section section--paper" id="diensten">
      <div class="container">
        <div class="section-head">
          <div class="reveal">
            <span class="label">Diensten</span>
            <h2>Wat we <em>voor u doen.</em></h2>
          </div>
          <p class="lede reveal" style="max-width:26em;margin:0">Van één raam tot een complete verbouwing. Wij nemen het werk uit handen en zorgen dat alles naadloos aansluit.</p>
        </div>
        <div class="tiles">
          <article class="tile reveal">
            <h3>Kunststof kozijnen</h3>
            <p>Goed isolerend, onderhoudsarm en verkrijgbaar in veel kleuren en houtnerfstructuren. De verstandige keuze voor comfort dat jaren meegaat.</p>
            <ul>
              <li>Draai-kiepramen en vaste ramen</li>
              <li>Voordeuren, achterdeuren en tuindeuren</li>
              <li>Schuifpuien</li>
              <li>Kleuren en houtlook naar keuze</li>
            </ul>
          </article>
          <article class="tile reveal">
            <h3>Aluminium kozijnen</h3>
            <p>Slanke profielen, strakke lijnen en ruimte voor grote glaspartijen. Voor een moderne, lichte uitstraling met maximaal zicht naar buiten.</p>
            <ul>
              <li>Ramen met smalle aanzichten</li>
              <li>Schuifpuien en grote glasvlakken</li>
              <li>Strakke deuren en puien</li>
              <li>Moderne architectuur en nieuwbouw</li>
            </ul>
          </article>
          <article class="tile reveal">
            <h3>Renovatie</h3>
            <p>Volledige renovatie van bestaande woningen. Als algemeen aannemer coördineren we alle onderdelen, van planning tot afwerking.</p>
            <ul>
              <li>Advies en planning vooraf</li>
              <li>Coördinatie van alle vakmensen</li>
              <li>Bewaking van tijd en budget</li>
              <li>Eén aanspreekpunt</li>
            </ul>
          </article>
        </div>
      </div>
    </section>

    <section class="section" id="vergelijking">
      <div class="container">
        <div class="section-head">
          <div class="reveal">
            <span class="label">Kunststof of aluminium</span>
            <h2>Twee materialen, <em>elk hun kracht.</em></h2>
          </div>
          <p class="lede reveal" style="max-width:26em;margin:0">Er is geen beste keuze, wel een beste keuze voor uw huis. Dit overzicht helpt; bij de kennismaking adviseren we persoonlijk.</p>
        </div>
        <div class="table-wrap reveal">
          <table class="compare">
            <thead>
              <tr><th scope="col"></th><th scope="col">Kunststof</th><th scope="col">Aluminium</th></tr>
            </thead>
            <tbody>
              <tr><th scope="row">Uitstraling</th><td>Klassiek tot modern, ook in houtlook</td><td>Strak, slank en eigentijds</td></tr>
              <tr><th scope="row">Isolatie</th><td>Van nature zeer goed isolerend</td><td>Goed, dankzij een thermische onderbreking in het profiel</td></tr>
              <tr><th scope="row">Onderhoud</th><td>Minimaal: af en toe schoonmaken</td><td>Minimaal: af en toe schoonmaken</td></tr>
              <tr><th scope="row">Profiel</th><td>Iets breder aanzicht</td><td>Smal aanzicht, meer glas en licht</td></tr>
              <tr><th scope="row">Grote glasvlakken</th><td>Goed mogelijk</td><td>Uitermate geschikt</td></tr>
              <tr><th scope="row">Investering</th><td>Doorgaans voordeliger</td><td>Doorgaans hoger</td></tr>
              <tr><th scope="row">Ideaal voor</th><td>Renovatie, rijwoningen, prijs-kwaliteit</td><td>Moderne woningen, aanbouwen, veel licht</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <section class="section section--paper" id="opties">
      <div class="container">
        <div class="section-head">
          <div class="reveal">
            <span class="label">Glas &amp; opties</span>
            <h2>De details die <em>het verschil maken.</em></h2>
          </div>
          <p class="lede reveal" style="max-width:26em;margin:0">Het kozijn is de basis; de keuzes daarbinnen bepalen het comfort. We lopen ze samen met u door.</p>
        </div>
        <div class="tiles tiles--4">
          <div class="tile reveal"><h3>Isolatieglas</h3><p>HR++ of triple glas, afgestemd op uw woning en uw wensen voor comfort en energieverbruik.</p></div>
          <div class="tile reveal"><h3>Geluidswerend</h3><p>Speciaal glas voor woningen aan een drukke weg, spoor of in de stad.</p></div>
          <div class="tile reveal"><h3>Veiligheid</h3><p>Inbraakwerend hang- en sluitwerk en veiligheidsglas waar dat nodig is.</p></div>
          <div class="tile reveal"><h3>Ventilatie</h3><p>Ventilatieroosters voor een gezond binnenklimaat, ook als alles goed geïsoleerd is.</p></div>
        </div>
      </div>
    </section>

    <section class="section section--night" id="werkwijze">
      <div class="container">
        <div class="section-head" style="margin-bottom:0">
          <div class="reveal">
            <span class="label">Werkwijze</span>
            <h2>Van eerste gesprek tot <em>nazorg.</em></h2>
          </div>
          <p class="lede reveal" style="max-width:26em;margin:0">U weet bij elke stap waar u aan toe bent. Geen verrassingen, wel duidelijke afspraken.</p>
        </div>
        <ol class="steps">
          <li class="reveal"><h3>Kennismaking</h3><p>U vertelt wat u wilt bereiken. We bespreken de mogelijkheden, de planning en een indicatie van de kosten.</p></li>
          <li class="reveal"><h3>Advies op locatie</h3><p>We komen langs, bekijken de situatie en adviseren over materiaal, kleur, glas en opties.</p></li>
          <li class="reveal"><h3>Inmeten</h3><p>Elk kozijn wordt nauwkeurig ingemeten. Precisie hier voorkomt problemen later.</p></li>
          <li class="reveal"><h3>Productie &amp; planning</h3><p>De kozijnen worden op maat gemaakt. Ondertussen plannen we samen de montagedag.</p></li>
          <li class="reveal"><h3>Montage</h3><p>Oude kozijnen eruit, nieuwe erin. Strak afgekit, waterdicht en tochtvrij.</p></li>
          <li class="reveal"><h3>Oplevering &amp; nazorg</h3><p>We lopen alles samen na, leggen de bediening uit en laten de werkplek schoon achter.</p></li>
        </ol>
      </div>
    </section>

    <section class="section">
      <div class="container two-col">
        <div class="reveal">
          <span class="label">De montagedag</span>
          <h2 style="margin-top:22px">Wat u <em>kunt verwachten.</em></h2>
          <p style="margin-top:24px">Een montagedag is voor veel mensen spannend: er gaat tenslotte een gat in de gevel. Wij zorgen dat het rustig en overzichtelijk verloopt.</p>
        </div>
        <div class="reveal">
          <ol class="checklist" style="margin-top:0">
            <li><div><b>Vooraf</b><span>We spreken een tijd af en vertellen welke ruimte er vrij moet zijn rond de ramen.</span></div></li>
            <li><div><b>Uitbreken</b><span>De oude kozijnen worden zorgvuldig verwijderd, met zo min mogelijk schade aan muren en vensterbanken.</span></div></li>
            <li><div><b>Plaatsen</b><span>De nieuwe kozijnen worden waterpas geplaatst, geïsoleerd en verankerd.</span></div></li>
            <li><div><b>Afwerken</b><span>Binnen en buiten strak afgekit en afgewerkt, zodat het eruitziet alsof het er altijd zat.</span></div></li>
            <li><div><b>Opruimen</b><span>We nemen het oude materiaal mee en laten alles schoon achter.</span></div></li>
          </ol>
        </div>
      </div>
    </section>

    <section class="section section--paper" id="renovatie">
      <div class="container two-col">
        <div class="reveal">
          <span class="label">Renovatie</span>
          <h2 style="margin-top:22px">Eén aannemer, <em>het hele project.</em></h2>
        </div>
        <div class="reveal">
          <p>Een renovatie bestaat uit veel onderdelen die op elkaar moeten aansluiten. Als algemeen aannemer nemen wij de coördinatie op ons: we plannen het werk, stemmen af met alle vakmensen en bewaken de voortgang.</p>
          <p>Voor u betekent dat één aanspreekpunt, één planning en één partij die verantwoordelijk is voor het resultaat. U hoeft niet zelf met verschillende bedrijven te schakelen, en weet altijd waar het project staat.</p>
          <div class="chips"><span>Planning</span><span>Coördinatie</span><span>Uitvoering</span><span>Afwerking</span><span>Oplevering</span></div>
        </div>
      </div>
    </section>

    <section class="section" id="onderhoud">
      <div class="container">
        <div class="section-head">
          <div class="reveal">
            <span class="label">Onderhoud</span>
            <h2>Zo blijven ze <em>als nieuw.</em></h2>
          </div>
          <p class="lede reveal" style="max-width:26em;margin:0">Kunststof en aluminium vragen weinig onderhoud. Met deze eenvoudige gewoontes gaan ze nog langer mee.</p>
        </div>
        <div class="tiles tiles--4">
          <div class="tile reveal"><h3>Schoonmaken</h3><p>Twee keer per jaar met lauw water en een milde zeep. Geen schuurmiddelen.</p></div>
          <div class="tile reveal"><h3>Rubbers</h3><p>Houd de afdichtingsrubbers schoon en soepel, zodat ze goed blijven sluiten.</p></div>
          <div class="tile reveal"><h3>Hang- en sluitwerk</h3><p>Smeer scharnieren en sluitingen af en toe met een geschikt smeermiddel.</p></div>
          <div class="tile reveal"><h3>Afwatering</h3><p>Houd de afwateringsopeningen onderin het kozijn vrij van vuil.</p></div>
        </div>
      </div>
    </section>

    <section class="section section--paper">
      <div class="container">
        <div class="statement">
          <span class="label reveal">Werkgebied</span>
          <h2 class="reveal">Wij werken <em>door heel Nederland</em>, van Groningen tot Zeeland en Limburg, vanuit onze basis in Best.</h2>
        </div>
        <div class="facts reveal" style="grid-template-columns:1fr 1fr">
          <div class="fact"><strong>1500+</strong><span>Kozijnen geplaatst</span></div>
          <div class="fact"><strong>6+</strong><span>Jaar ervaring</span></div>
        </div>
      </div>
    </section>

    <section class="section" id="vragen">
      <div class="container two-col">
        <div class="reveal">
          <span class="label">Veelgestelde vragen</span>
          <h2 style="margin-top:22px">Goed om <em>te weten.</em></h2>
          <p style="margin-top:28px">Staat uw vraag er niet bij? <a href="#contact">Neem gerust contact op.</a></p>
        </div>
        <div class="faq reveal">
          <details><summary>Werken jullie echt door heel Nederland?</summary><div><p>Ja. Onze basis is Best in Noord-Brabant, maar we plaatsen kozijnen door het hele land. Bij de kennismaking stemmen we de planning af op uw locatie.</p></div></details>
          <details><summary>Hoe lang duurt de montage?</summary><div><p>Dat hangt af van het aantal en de grootte van de kozijnen. Bij de kennismaking krijgt u een duidelijke planning, zodat u precies weet wanneer we komen en hoe lang we bezig zijn.</p></div></details>
          <details><summary>Kan ik in huis blijven tijdens de montage?</summary><div><p>Meestal wel. We werken per kozijn, zodat uw woning zo kort mogelijk open staat. Het is wel handig om de ruimte rond de ramen vooraf vrij te maken.</p></div></details>
          <details><summary>Heb ik een vergunning nodig?</summary><div><p>Voor het vervangen van kozijnen is meestal geen vergunning nodig. Bij een monument, in een beschermd stads- of dorpsgezicht of als het aanzicht van de gevel sterk verandert, kan dat anders zijn. Check het Omgevingsloket van de overheid of vraag het ons; we denken graag mee.</p></div></details>
          <details><summary>Kunststof of aluminium: wat past bij mijn huis?</summary><div><p>Kunststof is isolerend, onderhoudsarm en doorgaans voordeliger. Aluminium is slanker en geschikt voor grote glasvlakken en een moderne uitstraling. Bekijk de <a href="#vergelijking">vergelijking</a> hierboven, of laat u persoonlijk adviseren.</p></div></details>
          <details><summary>Wat gebeurt er met mijn oude kozijnen?</summary><div><p>Die nemen we mee en voeren we op de juiste manier af. U houdt er geen werk aan over.</p></div></details>
          <details><summary>Werken jullie ook voor bedrijven?</summary><div><p>Ja. Naast particulieren werken we voor bedrijven, verhuurders en andere aannemers. Neem contact op om de mogelijkheden te bespreken.</p></div></details>
          <details><summary>Hoe neem ik contact op?</summary><div><p>Via het formulier hieronder, telefonisch op 06-26889789 of via WhatsApp. We reageren zo snel mogelijk.</p></div></details>
        </div>
      </div>
    </section>

{contact_form("kozijnen", phone=True, paper=True, title="Bespreek uw <em>plannen.</em>", lede="Vertel kort wat u in gedachten heeft. We nemen zo snel mogelijk contact met u op. Liever direct overleggen? Bel of app gerust.")}

'''
