![](RackMultipart20210422-4-vuzou2_html_f2cf87d34556e0e2.gif)

_3 december 2020 – versie 1.0_

# Crash course zaakgericht werken

# Voor Common Ground-ontwikkelaars

### Doelgroep

Leden van Common Ground-ontwikkelteams die werken aan oplossingen die (mogelijk) raken aan het zaakgericht werken.

### Doel van dit document

Veel gemeenten werken zaakgericht. Het is daarom belangrijk dat oplossingen voor (dienstverlenings)vraagstukken die in het kader van Common Ground worden ontwikkeld het zaakgericht werken ondersteunen.

Dit document beschrijft bondig wat het zaakgericht werken is en op welke manier ontwikkelaars van Common Ground-oplossingen het zaakgericht werken kunnen ondersteunen.

### Wat is zaakgericht werken?

Zaakgericht werken is een vorm van procesgericht werken. Informatie die tijdens het uitvoeren van een proces wordt gecreëerd of ontvangen wordt gebundeld in een gestandaardiseerd &#39;zaakdossier&#39;. Dit &#39;zaakdossier&#39; is zo op uniforme wijze toegankelijk voor betrokkenen bij het verloop van de zaak.

Verschillende doelgroepen profiteren van het feit dat zaakgericht wordt gewerkt:

- **Inwoners** kunnen worden geïnformeerd over de behandeling van hun eigen zaken (per mail, brief, MijnOverheid of de website van de gemeente);
- **Behandelafdelingen** kunnen processen die zij uitvoeren monitoren en sturen (bijvoorbeeld het bewaken van behandeltermijnen);
- **Klantcontactcentra** kunnen vragen over lopende zaken beantwoorden op basis van alle relevante informatie, en kunnen zaakgegevens gebruiken voor het creëren van een klantbeeld;
- **Management** kan zaakgegevens gebruiken voor het creëren van managementrapportages op organisatieniveau, en
- **Informatiebeheerders** gebruiken bij zaakdossiers vastgelegde metagegevens om zaakinformatie conform geldende wet- en regelgeving te beheren.

Zaakgericht werken krijgt vorm met de uitvoering van zaken. Hierover worden vooraf afspraken gemaakt. Deze zijn vastgelegd in zogenoemde zaaktypen. Die omvatten een aantal kenmerken die gelden voor een groep gelijksoortige zaken, en waarborgen dat gelijksoortige zaken op eenduidige wijze behandeld worden. In het zaaktype beschreven kenmerken kunnen onder meer betrekking hebben op het volgende:

- de statussen die tijdens behandeling van zaken van het zaaktype gepasseerd moeten worden;
- doorlooptijd(en) voor behandeling van zaken van het zaaktype;
- de samenstelling van het dossier (welke documenten moeten in het zaakdossier voor zaken van het zaaktype zijn opgenomen), en
- mogelijke resultaten van de behandeling van zaken van het zaaktype.

De (mogelijke) resultaten waartoe behandeling van zaken van een specifiek zaaktype kunnen leiden noemen we resultaattypen. Door resultaattypen in combinatie met procestypen te koppelen aan regels in de Selectielijst gemeenten en intergemeentelijke organen kan voor iedere zaak vastgesteld en vastgelegd worden hoe lang het bijbehorende dossier bewaard moet blijven.

In sommige gevallen wordt informatie die hoort bij een bepaalde hoeveelheid werk wel volgens de conventies van zaken vastgelegd, zonder dat zaakinformatie wordt gebruikt voor het sturen van een (behandel)proces. In dit geval spreken we niet van zaakgericht werken, maar van &#39;zaakgericht registreren&#39;. Zaakgericht registreren wordt toegepast in situaties waar niet (altijd) op basis van (vooraf gedefinieerde) processen wordt gewerkt, maar waar het wel belangrijk is dat informatie eenvoudig kan worden gedeeld met inwoners of collega&#39;s, en waar informatiebeheerders die volgens wet- en regelgeving moeten kunnen beheren.

Meer informatie over zaakgericht werken en zaakgericht registreren is te vinden in de [Gemeentelijke Modelarchitectuur (GEMMA)](https://www.gemmaonline.nl/index.php/Thema_Zaakgericht_werken).

### Kenmerken van zaken

Hoewel zaakgericht werken een vorm van procesgericht werken is, is het niet de noodzakelijk om complete (bedrijfs)processen als zaak te modelleren. Voor de hierboven beschreven doelgroepen en doelen is het voldoende om het proces op hoofdlijnen te kennen. Voor het zaakgericht werken zijn daarom alleen de mijlpalen (belangrijke statussen) binnen een bedrijfsproces van belang. Fout! Verwijzingsbron niet gevonden. illustreert de relatie tussen bedrijfsproces en zaak.

De statussen die horen bij groepen van gelijkaardige zaken, worden vastgelegd in zaaktypen. Een zaaktype vormt daarmee de &#39;blauwdruk&#39; voor zaken van een bepaalde soort, waar de karakteristieke eigenschappen daarvan beschreven zijn. Naast statussen kunnen die eigenschappen bijvoorbeeld ook bestaan uit verplicht toe te voegen documenten of mogelijke resultaten van de zaakbehandeling.

![](RackMultipart20210422-4-vuzou2_html_772d9026f859a600.png)

_Figuur_ 1_: Een zaak kent het bedrijfsproces alleen op hoofdlijnen._

### API-standaarden voor zaakgericht werken

Om zaakgericht werken mogelijk te maken op een manier die aansluit bij de informatiekundige visie Common Ground, is aantal API-standaarden ontwikkeld. Het gaat om de volgende standaarden voor het creëren, bijwerken, lezen en verwijderen van gegevens die te maken hebben met zaken:

- Zaken API (creëren, bijwerken, lezen en verwijderen van zaakgegevens)
- Catalogi API (creëren, bijwerken, lezen en verwijderen van zaak- besluit en resultaattypes)
- Documenten API (creëren, bijwerken, lezen en verwijderen van informatieobjecten en bijbehorende metagegevens)
- Besluiten API (creëren, bijwerken, lezen en verwijderen van besluitgegevens)
- Contactmomenten API (in ontwikkeling, release 4e kwartaal 2020 - creëren, bijwerken, lezen en verwijderen van gegevens die een contactmoment beschrijven
- Klanten API (in ontwikkeling, release 4e kwartaal 2020 - creëren, bijwerken, lezen en verwijderen van klantgegevens
- Verzoeken API (in ontwikkeling, release 1e helft 2021 - creëren, bijwerken, lezen en verwijderen van verzoek- of bestellinggegevens)

De gegevens die de hierboven genoemde API&#39;s toegankelijk maken komen bij de behandeling van vrijwel alle zaken voor. In veel gevallen zijn voor het behandelen van een zaak echter ook (domein)specifieke gegevens nodig, zoals de hoogte van het subsidiebedrag bij een subsidieaanvraag, de verhuisdatum bij een verhuizing, de gewenste ophaallocatie bij de aanvraag van een nieuw paspoort etc. Deze gegevens kunnen met de hierboven genoemde API&#39;s niet (gestructureerd) worden vastgelegd. Hiervoor zijn dus aanvullende API&#39;s nodig.

Om de API-standaarden voor zaakgericht werken te gebruiken is ten slotte een tweetal ondersteunende API&#39;s nodig, te weten:

- Autorisaties API (configureren welke informatiesystemen toegang hebben tot middels de hierboven genoemde API&#39;s toegankelijk gemaakte gegevens)
- Notificaties API (aanbieden en routeren van notificaties over wijzigingen in gegevens die door de hierboven genoemde API&#39;s toegankelijk gemaakt worden, en het abonneren op kanalen)

### Gegevensopslag binnen Common Ground

De informatiearchitectuur bij de informatiekundige visie Common Ground is nader uitgewerkt in het [GEMMA Gegevenslandschap](https://www.gemmaonline.nl/index.php/Gegevenslandschap). Eén van de uitgangspunten daarbij is, is dat gelijksoortige gegevens waar mogelijk opgeslagen worden in gespecialiseerde registers. De gegevens worden vanuit deze registers middels API&#39;s beschikbaar gemaakt voor gebruik in applicaties die door medewerkers of inwoners worden bediend. Uitgangspunt daarbij is dat duplicatie en synchronisatie van gegevens zoveel mogelijk wordt beperkt. Dit bepaalt het patroon voor opslag van gegevens waar in het gegevenslandschap zaakgericht wordt gewerkt of geregistreerd.

### Casus: Melding openbare ruimte

Om de toegankelijkheid van dit patroon te verhogen, wordt de manier waarop zaakgericht werken in een gegevenslandschap werkt verder geïllustreerd aan de hand van een voorbeeldcasus waarin een inwoner bij de gemeente melding maakt van naast een container gedumpt grofvuil. Gemeenten noemen zo&#39;n soort melding vaak een &#39;melding openbare ruimte&#39;.

Figuur 2 laat zien dat de gegevens die de &#39;melding openbare ruimte&#39; bij ontvangst beschrijven uiteenvallen in een aantal individuele dataobjecten, namelijk:

1. de melding zelf;
2. de klant die de melding heeft gedaan;
3. een document dat de klant ter illustratie bij de melding heeft gevoegd, en
4. de zaak waarbinnen de melding behandeld zal worden.

![](RackMultipart20210422-4-vuzou2_html_b8c7213436f11beb.png)

_Figuur_ 2_: decompositie van een melding openbare ruimte in verschillende &#39;typen&#39; gegevens._

N.B. Het aantal dataobjecten is hier omwille van de leesbaarheid beperkt. Uiteraard zijn diverse voorbeelden te bedenken waarbij meer of andere dataobjecten onderdeel uitmaken van een &#39;melding openbare ruimte&#39;.

De dataobjecten &#39;klant&#39;, &#39;zaak&#39; en &#39;document&#39; kennen binnen de collectie API-standaarden voor zaakgericht alle drie een eigen API. Dit betekent dat de applicatie die de &#39;melding openbare ruimte&#39; vastlegt, daarbij vier API&#39;s aanspreekt. Naast de drie reeds genoemde is immers ook een API nodig om de (domein)specifieke details die de melding beschrijven vast te leggen. Deze noemen we verder de &#39;meldingen API&#39; (niet-concrete componenten worden om ze te onderscheiden van concrete componenten voor Zaakgericht werken steeds aangeduid met aanhalingstekens).

### Initiële vastlegging

In dit voorbeeld gaan we ervan uit dat de gemeente een app aanbiedt (de &#39;meldingenapp&#39;) die inwoners kunnen gebruiken om melding te maken van problemen of defecten in de openbare ruimte.

1. Onze casus begint wanneer een inwoner in de &#39;meldingenapp&#39; een formulier invult om melding te maken van het dumpen van grofvuil naast een vuilcontainer. Daarbij uploadt zij een foto waarop het geconstateerde te zien is.
2. Vanuit de &#39;meldingenapp&#39; wordt met behulp van de Zaken API in het zakenregister een zaak aangemaakt van het juiste zaaktype. (formulier)inhoud die als zaakgegevens kan worden vastgelegd, wordt bij de zaak opgeslagen.
3. Vanuit de &#39;meldingenapp&#39; worden de overige gegevens verdeeld over de juiste registers. Daarbij wordt telkens een relatie gelegd met de zaak. In dit geval gaat het om:

- de NAW-gegevens van de melder middels de Klanten API in het klantenregister;
- de foto van de situatie middels de Documenten API in het documentenregister, en
- de gegevens die melding beschrijven (locatie, wat is er precies geconstateerd) middels de &#39;Meldingen API&#39; in het &#39;meldingenregister&#39;.

![](RackMultipart20210422-4-vuzou2_html_95318c86b5876bf6.png)

_Figuur_ 3_: Meldinggegevens worden middels API&#39;s verdeeld over registers._

Het bovenstaande is geïllustreerd in Figuur 3. Dit model laat tevens zien dat de zaak fungeert als knooppunt voor, en verwijsindex naar alle gegevens die horen bij de melding en de behandeling daarvan. Hierdoor kunnen de eerder in dit document genoemde doelgroepen de voortgang van de zaak volgen, en hebben zij (mits daartoe gemachtigd) toegang tot alle daarbij horende (object)gegevens en documenten.

Het sequencediagram in Figuur 4 laat zien hoe de hierboven beschreven zaakgegevens middels de API&#39;s voor Zaakgericht werken worden vastgelegd.

![](RackMultipart20210422-4-vuzou2_html_c8a1eeaed0bcd9b3.png)

_Figuur_ 4_: Vereenvoudigd sequencediagram vastleggen zaakgegevens met API&#39;s voor Zaakgericht werken._

Bij dit diagram zijn een aantal opmerkingen te maken:

- Het diagram is enigszins vereenvoudigd. Interacties met ondersteunende API&#39;s (voor notificaties, autorisaties, validatie met Catalogi API) zijn omwille van de leesbaarheid weggelaten.
- De indiener hoeft niet te wachten tot alle API-calls zijn afgerond. Meestal is een zaakidentificatie (dus het vastleggen van de zaak en de response daarop) de enige noodzakelijk terugkoppeling naar de indiener. Het uploaden van een document kan asynchroon gebeuren.
- De eerste vier van de geïllustreerde calls kunnen parallel worden uitgevoerd.
- Als de klantgegevens al bekend zijn (bijvoorbeeld uit een eerdere zaak), dan hoeven er geen nieuwe klantgegevens worden vastgelegd, maar kunnen bestaande klantgegevens aan de Zaak worden gekoppeld. Als er in het geheel geen sprake is van een klant (bijvoorbeeld als een zaak wordt gestart op basis van een anonieme melding) dan hoeven geen klantgegevens te worden vastgelegd of gekoppeld.

### Gegevens vastleggen tijdens behandeling en afsluiten zaak

Tijdens de behandeling van de zaak kunnen nieuwe gegevens ontstaan of ontvangen worden (Figuur 5). Ook deze worden aan de zaak gekoppeld. In het voorbeeld van de &#39;melding openbare ruimte&#39; kan bijvoorbeeld gedacht worden aan:

1. Het verslag van een telefoongesprek met de indiener om meer gedetailleerde informatie te krijgen over waar precies het grofvuil is aangetroffen. Dit verslag wordt vastgelegd in het Contactmomentenregister.
2. Een ingeplande opdracht voor de afdeling reiniging om het aangetroffen grofvuil op te halen. De gegevens die deze opdracht beschrijven worden opgeslagen in een &#39;opdrachtenregister&#39;. Alle informatie over deze opdracht is beschreven in een aan de opdracht gerelateerde opdrachtbrief, die is opgeslagen in het documentenregister.

![](RackMultipart20210422-4-vuzou2_html_a43dd6656fe4f645.png)

_Figuur_ 5_: Tijdens de behandeling van de melding kunnen nieuwe gegevens worden toegevoegd._

Als de behandeling van de zaak is afgerond wordt de zaak afgesloten. In veel gevallen kan op basis van het resultaat van de zaak (dus het bereikte resultaattype) bij het zaakdossier een bewaartermijn worden vastgelegd. Bij het verlopen van de bewaartermijn kan de zaak, eventueel met daaraan gekoppelde, in andere registers opgeslagen gegevens, vernietigd worden.

### Verzoeken en zaakgericht werken

Dit document passeert het concept &#39;verzoeken&#39; en de rol daarvan binnen het zaakgericht werken. Hiervoor is gekozen omdat uitwerking van dit concept, net als de invulling van de bijbehorende API-standaard nog onderwerp is van discussie. Op het moment dat het concept en de API-standaard zodanig zijn uitgewerkt dat de rol daarvan binnen het zaakgericht werken volledig is bepaald, wordt dit document bijgewerkt.

![](RackMultipart20210422-4-vuzou2_html_da6b4288f80bd662.gif) ![](RackMultipart20210422-4-vuzou2_html_152eb09e054afaeb.gif)

**VNG Realisatie**
