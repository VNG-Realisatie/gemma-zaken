---
title: "Productvisie API's voor Zaakgericht Werken"
date: '29-5-2018'
weight: 100

---

## Introductie

Om Zaakgericht Werken (ZGW) een stap verder te brengen wordt de opvolger van de
Zaak- en Documentservices (ZDS) ontwikkeld, inmiddels bekend als de ZGW API's.
Hierbij wordt een andere vorm van standaardisatie toegepast. Op basis van
relevante informatiemodellen (RGBZ 2.0 en ImZTC 2.2) wordt met zowel publieke
als private partijen in een agile  proces vorm gegeven aan RESTful API's die
concreet invulling geven aan de gewenste standaard. De standaard wordt tegelijk
met een referentie-implementatie ontwikkeld om de implementeerbaarheid aan te
tonen, en als referentie te dienen voor latere implementaties.

### Toegevoegde waarde voor gemeenten

- Kortere doorlooptijd van het inrichten van nieuwe koppelingen (plug and play
  is veelgehoorde wens)
- Lagere ontwikkelkosten van koppelingen op basis van de ZGW API's
- Lagere beheerkosten door backwards compatibiliteit (wijzigingen in de
  standaard leiden meestal niet tot aanpassingen in bestaande koppelingen)
- Voorkomen lock-in door echt uitwisselbare componenten
- Hogere kwaliteit van de standaard doordat deze in de praktijk en met
  medewerking van gemeenten en leveranciers is ontwikkeld. En ook door parallel
  aan de standaard een werkende referentie-implementatie te ontwikkelen
- Een herbruikbare, plug and play API waarmee in apps en applicaties de basale
  zaak(document) functionaliteiten consistent gebruikt kunnen worden

### Toegevoegde waarde voor leveranciers

- Lagere ontwikkelkosten van het koppelvlak
- Kunnen zich onderscheiden op onderdelen die burgers, bedrijven en medewerkers
  raken (i.p.v. te concurreren op infrastructuur)

### Toegevoegde waarde voor VNG Realisatie

- Beheer van de standaard is eenvoudiger doordat aanpassingen gemakkelijker
  zijn door te voeren
- Kwaliteitscontrole van koppelvlakken van leveranciers is eenvoudiger en
  daarmee goedkoper.
- Backwards compatibiliteit is eenvoudiger te behouden

### Context

Binnen de Gemeentelijke Model Architectuur (GEMMA) versie 2 is het
[Katern Zaakgericht Werken](https://www.gemmaonline.nl/index.php/GEMMA_2_Katern_Zaakgericht_Werken)
beschikbaar. Hierin wordt uitvoerig beschreven hoe Zaakgericht Werken bedoeld
is. Dit is verder uitgewerkt in de GEMMA Informatiearchitectuur in o.a.
[referentiecomponenten en Integratiepatronen Zaakgericht werken](https://www.gemmaonline.nl/index.php/ZGW_in_GEMMA_2).

Vanaf mei 2018 wordt met een aantal partijen [samengewerkt](../overige/samenwerking)

aan realisatie van de ZGW API's.

De naam Zaak- en Documentservices (ZDS) werd eerder gebruikt om duidelijk te
maken welke huidige standaard wordt gemoderniseerd. Inmiddels heeft de opvolger
een meer passende naam gekregen: de Zaakgericht Werken API's (ZGW API's). Dit
behelst een collectie van meerdere aparte API's, waaronder de Zaken API,
Documenten API, etc. De naam "ZDS 2.0" wordt niet meer gebruikt.

## Productvisie ZGW

De visie op de te realiseren Zaak- en Documentservices is als volgt:

- De services worden vormgegeven op basis van heldere user stories ontleend aan
  de praktijk, dus op basis van daadwerkelijk gebruik in plaats van op basis van
  een theoretische inschatting van wat nodig is; Hieronder valt ook het uitwerken
  van
  [klantcontacten](https://www.gemmaonline.nl/index.php/Klantcontacten_en_het_RGBZ)
  in de API.
- Alles rond "zaken" vindt zoveel mogelijk geautomatiseerd en op de achtergrond
  plaats. Medewerkers zijn bezig met inhoudelijke activiteiten, niet met zaken;
- De inhoud van de zaaktypecatalogus (ZTC) wordt zoveel mogelijk
  gestandaardiseerd, rekening houdend met de
  [zaakgerichte selectielijst](https://vng.nl/files/vng/20170706-selectielijst-gemeenten-intergemeentelijke-organen-2017.pdf)
  (pdf) en GEMMA 2 processen. Gestreefd wordt naar het centraal aanbieden van een
  ZTC. Deze kan bijv. dienen als repository, waar gemeenten zaaktypen 1 op 1 uit
  kunnen overnemen of deze voor eigen gebruik wijzigen waar nodig.
- Voor elk gegeven geldt een authentieke bron die wordt ontsloten via API's. Er
  wordt niet gekopieerd en gesynchroniseerd. Er worden relaties gelegd en
  doorgeknipt. Bijvoorbeeld: wanneer een informatieobject in meerdere zaken een
  rol speelt wordt vanuit elke zaak een relatie gelegd naar (een specifieke
  versie van) betreffend informatieobject. Het informatieobject blijft in de
  DRC onder verantwoordelijkheid van de opsteller. Dit heeft consequenties voor
  bijvoorbeeld de logica die besluit tot overbrengen of vernietigen.
- Door te werken met API's die een logische scope hebben binnen de
  informatiemodellen wordt toegewerkt naar een gegevenslandschap waarbij
  componenten zonder enige impact kunnen worden vervangen door een component van
  een andere leverancier. In de huidige praktijk is dit onmogelijk omdat de scope
  van wat een leverancierspecifieke implementatie van een service afdekt niet
  uniform is. Hiermee worden (onbedoelde) vendor lockins bestreden.

## Scope

Realisatie van de productvisie valt uiteen in vier delen die niet los van
elkaar gezien kunnen worden:

1. Specificeren van Zaak- Documentservices v2.0
2. Beschikbaar maken van Open Source referentieimplementatie
3. Realiseren van toepassingen voor burgers of gemeenten gebruikmakend van de
   ZGW API's
4. Centraal aanbieden van componenten op basis van de nieuwe API's

Delen 1 en 2 worden uitgevoerd door een centraal scrumteam bestaand uit
samenwerkende gemeenten.

Deel 3 wordt uitgevoerd door planning af te stemmen tussen dit scrumteam en
projecten die tegelijkertijd in gemeenten worden uitgevoerd. Bij deel 3 zorgt
het centrale scrumteam voor het tijdig beschikbaar zijn van de relevante delen
van de nieuwe API's.

Deel 4 is buiten scope voor het centrale scrumteam. Dit deel van de visie wordt
nader uitgewerkt en op een later moment uitgevoerd.



## Uitgangspunten

Bij de start van dit traject hanteren we de volgende uitgangspunten:

- De
  [GEMMA 2 Architectuur](https://www.gemmaonline.nl/index.php/GEMMA_Architectuur)
  en de
  [GEMMA 2 standaarden](https://www.gemmaonline.nl/index.php/GEMMA_Gegevens-_en_berichtenarchitectuur)
  (voor zover van toepassing) worden gevolgd
- Daar waar GEMMA 2 nog niet (helemaal) in lijn is met Common Ground, wordt
  Common Ground gevolgd.
- Daar waar GEMMA 2 niets voorschrijft worden
  [Open Standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  gevolgd
- Alle code, documenten en specificaties die ontstaan in dit traject wordt Open
  Source, gepubliceerd onder de
  [EUPL licentie](https://joinup.ec.europa.eu/collection/eupl/eupl-text-11-12)
- [RGBZ 2](https://www.gemmaonline.nl/index.php/RGBZ_2.0_in_ontwikkeling) en
  het daarvan afgeleide gegevensmodel UGM GBZ (GEMMA 2) zijn het startpunt voor
  de uitwerking van services. Wanneer blijkt dat aanpassingen nodig zijn voor
  goede werking van de Zaak- en Documentservices dan is dit mogelijk. In eerste
  instantie betreft dat het UGM GBZ. Indien uit de user-storys blijkt dat 'de
  werkelijkheid' niet correct gemodelleerd is in het RGBZ, dan is aanpassing
  mogelijk. Met ingang van dit traject komen betrokken standaarden in een
  toestand, waarbij deze voortdurend op basis van behoefte en consensus worden
  gewijzigd en frequent nieuwe versies worden vastgesteld.
- Voor de specificatie van API's wordt de onlangs door Forum Standaardisatie op
  de
  ["Pas toe of leg uit"-lijst](https://www.forumstandaardisatie.nl/lijst-open-standaarden/in_lijst/verplicht-pas-toe-leg-uit)
  geplaatste
  [OpenAPI Specification v3.x](https://www.forumstandaardisatie.nl/standaard/openapi-specification)
  gebruikt.
- De principes volgend uit de
  [Common Ground visie](https://github.com/VNG-Realisatie/common-ground/blob/master/cg-vision.md)
  (EN) worden als volgt toegepast:
  - Goede scheiding zaakafhandeling en -registratie (ook conform GEMMA 2 met
    Zaakregistratiecomponent en Zaakafhandelcomponent)
  - Er wordt bij het opstellen van de specificatie uitgegaan van een
    gegevenslandschap waarbij alle gegevens bij de bron kunnen worden
    geraadpleegd en geen lokale kopie wordt gemaakt. Om de transitie mogelijk te
    maken worden waar ndogi tijdelijke voorzieningen getroffen
  - Bij eventueel centraal aangeboden voorzieningen worden API's ontsloten via
    [NLX](https://www.nlx.io/)
  - Grote informatiemodellen worden waar nuttig opgesplitst in kleinere
    informatiemodellen die hoog-frequent kunnen wijzigen
  - De modernste bewezen techniek wordt toegepast, en de toegepaste techniek
    verandert mee met de ontwikkelingen door de jaren heen. We gaan over in een
    toestand die kan worden aangeduid als "permanent beta".
- De
  [API en URI strategie](https://aandeslagmetdeomgevingswet.nl/digitaal-stelsel/documenten/documenten/api-uri-strategie/)
  zoals opgesteld binnen het programma Digitaal Stelsel Omgevingswet worden waar
  mogelijk toegepast.
- Eisen rond
  [Duurzame toegankelijkheid](https://wiki.nationaalarchief.nl/pagina/DUTO:Kwaliteitseisen)
  worden vanaf het begin in de standaarden verwerkt.
- Archivering speelt een rol bij de uitvoering van elk proces, vanaf de start
  tot aan
  [overbrenging](https://wiki.nationaalarchief.nl/pagina/DUTO:Overbrenging) of [vernietiging](https://wiki.nationaalarchief.nl/pagina/DUTO:Vernietigen). De
  gegevensstandaard voor archiefstukken
  [TMLO](https://archief2020.nl/nieuws/toepassingsprofiel-metadatering-lokale-overheden)
  is al
  [geïntegreerd in RGBZ en ImZTC](https://www.gemmaonline.nl/index.php/Metadateren_van_zaakdossiers_conform_het_TMLO).

## Realisatie

De realisatie gaat van start zonder complete blauwdruk van wat gebouwd moet
worden. Door user-stories zo goed mogelijk in te vullen en vanuit oogpunt
architectuur in de gaten te houden dat designchoices worden gemaakt die ruimte
openlaten voor verdere ontwikkeling in de richting van de visie, komt de nieuwe
standaard stukje bij beetje tot stand.

Om een snelle start te maken wordt gestart met alle gemeenten en partijen
waarvan de interesse bekend is. Aanhakers zijn nadrukkelijk welkom.

De ontwikkeling gebeurt in de GitHub repository
[VNG-Realisatie/gemma-zaken](https://github.com/VNG-Realisatie/gemma-zaken).

Ook de backlog wordt publiek bijgehouden, samengesteld uit GitHub issues op dit
open [Scrum bord](https://github.com/VNG-Realisatie/gemma-zaken/projects/1).

Bij de ontwikkeling van de API's wordt gestreefd naar backwards compatibility.

Voor meer informatie over de samenwerking, zie
[samenwerking](../overige/samenwerking)

Naast de (nieuw te ontwikkelen) OpenAPI 3 specificatie wordt een [referentie implementatie](https://nl.wikipedia.org/wiki/Referentie-implementatie) gemaakt.
De referentie implementatie heeft de volgende karakteristieken:

- Wordt gelijktijdig ontwikkeld met de specificatie en (geautomatiseerde) test
  suite;
- Maakt het mogelijk scenariotesten uit te voeren, wat vraagt om persistentie
  van testdata;
- Bewijst dat de specificatie geïmplementeerd kan worden;
- Zorgt er voor dat leveranciers hun eigen implementatie kunnen testen;
- Is de defacto standaard voor andere implementaties;
- Geeft duidelijkheid over de intentie van de specificatie waar deze ruimte
  biedt voor interpretaties.

## Transitie

Een BIG BANG overgang is onmogelijk. Er zal een geleidelijke transitie moeten
plaatsvinden waarbij het nieuwe naast het oude bestaat. De te ontwikkelen
ZGW API's (en verder) is de toekomst, rekening moet worden gehouden met de
huidige werkelijkheid die daarnaast moet kunnen bestaan. Idealiter in de zelfde
achterliggende bronnen die op meerdere manieren worden ontsloten.

In het ZGW Scrumteam ligt de focus op het ontwikkelen van de nieuwe wereld. De
rol van architecten in het team bestaat o.a. uit het in de gaten houden of een
transitie mogelijk blijft.

## Centraal aanbieden

Het principe "raadplegen bij de bron" veronderstelt waar mogelijk een enkele
bron die wordt bijgehouden door de verantwoordelijke en welke kan worden
geraadpleegd door afnemers.

Voorzien wordt dat vanuit een centraal punt aanbieden van componenten (SaaS)
naast decentraal gebruik van grote waarde kan zijn. Om daar te komen is het
volgordelijk nodig eerst de API specificatie uit te werken.

Een centraal gepositioneerde *Zaakregistratiecomponent* (ZRC) en
*Documentregistratiecomponent* (DRC) is in veel ketensamenwerkingen wellicht
een welkome oplossing als alternatief van de huidige praktijk van
ketenautomatisering waarbij dossiers steeds worden gekopieerd naar een volgende
silo. In de praktijk betekent dit dan dat organisaties afhankelijk van het
proces en de ketenpartners het proces koppelen aan een andere ZRC en DRC.

- Binnen het DSO (zie: [Gerelateerde trajecten](#gerelateerde_trajecten)) is
  hier mogelijk op korte termijn behoefte aan.
- Ook binnen het Sociaal Domein heeft deze constructie potentie.

Een landelijke *Zaaktypecatalogus* (ZTC) kan dienen als repository van content
die voor veel gemeenten gelijk zal blijken. Voor veel zaken zal het niet nodig
blijken af te wijken van de referentie. Ook hier geldt dat organisaties per
proces zouden kunnen kiezen welke authoratieve bron voor Zaaktypen wordt
geraadpleegd - bijvoorbeeld voor interne processen een intern ZTC en voor
ketenprocessen een centrale ZTC.

Gestreefd wordt naar het landelijk aanbieden van een ZTC. Deze kan bijv.
dienen als repository, waar gemeenten zaaktypen 1 op 1 uit kunnen overnemen of
deze voor eigen gebruik wijzigen waar nodig.

Wanneer componenten centraal worden aangeboden is een *beheerorganisatie*
noodzakelijk met een andere opdracht dan de beheerorganisatie die nu de
standaarden beheert. Het valt daarom buiten de scope van het traject om te
komen tot een volledige 1.0.0 release van alle APIs onder de ZGW API's. Er
wordt gestreefd naar een 1.0.0-RC (release candidate) die in beheer kan worden
genomen door VNG Realisatie.

## Gerelateerde trajecten

- Binnen het
  [Digitaal Stelsel Omgevingswet](https://www.omgevingswetportaal.nl/wet-en-regelgeving/dso)
  zijn wellicht kansen om Zaakgericht Werken zoals gemeenten dat kennen te
  introduceren op basis van de ZGW API's. Momenteel wordt samenwerking daar
  voorzien door middel van een omgeving waar bestanden kunnen worden gedeeld.
- De gemeenten Almere, Amsterdam, Haarlem, Heerenveen, Hoorn, Medemblik (en
  wellicht nog meer) zijn voornemens gezamelijk een Open Source Mijn Gemeente
  website te produceren. Daarbij zijn de ZGW API's wellicht een interessante
  aanvulling, hier liggen kansen om samen op te trekken.
- Dimpact en Atos stellen de Atos e-Suite in de context van Common Ground
  beschikbaar als platform voor proeven die innovatie en ontwikkeling stimuleren.
- Het project Landelijke Online Diensten (LOD) heeft een landelijke dienst voor
  aangifte overlijden en aangifte verhuizing gerealiseerd. Voor de koppeling
  tussen deze dienst (de voorkant) en de verwerkende systemen in de gemeente (de
  achterkant) worden twee "productaanvragen" API's ontworpen en gerealiseerd.
