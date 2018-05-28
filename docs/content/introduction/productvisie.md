# ZAKEN Productvisie ZDS

## Inhoud
* [Introductie](#introductie)
* [Productvisie ZDS](#productvisie_zds)
* [Centraal aanbieden](#centraal_aanbieden)
* [Uitgangspunten](#uitgangspunten)
* [Realisatie](#realisatie)
* [Gerelateerde trajecten](#gerelateerde_trajecten)


## Introductie

Om Zaakgericht Werken een stap verder te brengen worden Zaak- en Documentservices (ZDS) versie 2 ontwikkeld. Hierbij wordt een andere vorm van standaardisatie toegepast. In plaats van jarenlang overleg over een informatiemodel en de bijbehorende koppelvlakken en services, wordt op basis van een gegeven informatiemodel (RGBZ2) met betrokken partijen in een agile proces vormgegeven aan RESTful API's welke concreet invulling geven aan de gewenste standaard.

Binnen de Gemeentelijke Model Architectuur (GEMMA) versie 2 is het [Katern Zaakgericht Werken](https://www.gemmaonline.nl/index.php/GEMMA_2_Katern_Zaakgericht_Werken) beschikbaar. Hierin wordt uitvoerig beschreven hoe Zaakgericht Werken bedoeld is.

Vanaf mei 2018 wordt met een aantal partijen [samengewerkt](./samenwerking.md) aan realisatie van de ZDS 2.0.


## Productvisie ZDS

De visie op de te realiseren Zaak- en Documentservices is als volgt:

- De services worden vormgegeven op basis van heldere user stories ontleend aan de praktijk, dus op basis van daadwerkelijk gebruik in plaats van op basis van een theoretische inschatting van wat nodig is;

- Alles rond "zaken" vindt zoveel mogelijk geautomatiseerd en op de achtergrond plaats. Medewerkers zijn bezig met inhoudelijke activiteiten, niet met zaken;

- De inhoud van de zaaktypecatalogus (ZTC) wordt zoveel mogelijk gestandaardiseerd, rekening houdend met de [zaakgerichte selectielijst](https://vng.nl/files/vng/20170706-selectielijst-gemeenten-intergemeentelijke-organen-2017.pdf)(pdf) en GEMMA 2 processen. Gestreefd wordt naar het centraal aanbieden van een ZTC. Deze kan bijv. dienen als repository, waar gemeenten zaaktypen 1 op 1 uit kunnen overnemen of deze voor eigen gebruik wijzigen waar nodig.

- Eisen rond [Duurzame toegankelijkheid](https://wiki.nationaalarchief.nl/pagina/DUTO:Kwaliteitseisen) worden vanaf het begin in de standaarden verwerkt.

- Archivering speelt een rol bij de uitvoering van elk proces, vanaf de start tot aan [overbrenging](https://wiki.nationaalarchief.nl/pagina/DUTO:Overbrenging) of [vernietiging](https://wiki.nationaalarchief.nl/pagina/DUTO:Vernietigen). Daar waar nodig worden externe standaarden zoals bijv. [TMLO](https://archief2020.nl/nieuws/toepassingsprofiel-metadatering-lokale-overheden), hoewel suboptimaal, geïntegreerd in de standaard.



## Centraal aanbieden      

  ZRC
	ZTC
  Beheerorganisatie

  Kernregistratie vs Basisregistratie
  Transparantie
  Overdragen van zaken
  Wat kunnen organisaties van elkaar zien


  Transitie
  	Migratie


##	Uitgangspunten

Bij de start van dit traject hanteren we de volgende uitgangspunten:

- GEMMA 2 standaarden worden gevolgd

- Daar waar GEMMA 2 niets voorschrijft worden Open Standaarden gevolgd

- Alle code die ontstaat in dit traject wordt Open Source, gepubliceerd onder de EUPL licentie

- RGBZ 2 is het startpunt, maar wanneer blijkt dat aanpassingen nodig zijn voor goede werking van de Zaak- en Documentservices dan wordt dit voorgesteld. RGBZ 1 bestaat sinds 2010, RGBZ 2 is sinds 2012 in ontwikkeling en nog altijd niet in productie. Met ingang van dit traject komen betrokken standaarden in een "permanent beta" toestand, waarbij ze voortdurend op basis van behoefte en consensus worden gewijzigd.

- Voor de specificatie van API's wordt de onlangs door Forum Standaardisatie op de "Pas toe of leg uit"-lijst geplaatste OpenAPI Specification v3.x gebruikt.

- De principes volgend uit de [Common Ground visie](https://github.com/VNG-Realisatie/common-ground/blob/master/cg-vision.md) (EN) worden als volgt toegepast:
  - Goede scheiding taakafhandeling en registratie
	- Bij eventueel centraal aangeboden voorzieningen worden API's ontsloten via NLX
	- Grote informatiemodellen worden waar nuttig opgesplitst in kleinere informatiemodellen die hoog-frequent kunnen wijzigen

- De [API en URI strategie](https://aandeslagmetdeomgevingswet.nl/digitaal-stelsel/documenten/documenten/api-uri-strategie/) zoals opgesteld binnen het programma Digitaal Stelsel Omgevingswet worden waar mogelijk toegepast.


##	Realisatie

De realisatie gaat van start zonder complete blauwdruk van wat gebouwd moet worden. Door user stories zo goed mogelijk in te vullen en vanuit oogpunt architecuur in de gaten te houden dat design choices worden gemaakt die ruimte openlatne voor verdere ontwikkeling in de richting van de visie, komt de nieuwe standaard stukje bij beetje tot stand.

Om een snelle start te maken wordt gestart met alle gemeenten en partijen waarvan de interesse bekend is. Aanhakers zijn nadrukkelijk welkom.

De ontwikkeling gebeurt geheel Open Source, in de GitHub repository [VNG-Realisatie/gemma-zaken](https://github.com/VNG-Realisatie/gemma-zaken).

Ook de backlog wordt publiek bijgehouden, samengesteld uit GitHub issues op dit open [Kanban bord](https://github.com/VNG-Realisatie/gemma-zaken/projects/1).

Voor meer informatie over de samenwerking, zie [samenwerking.md](./samenwerking.md)


## Gerelateerde trajecten
  DSO
  mijn.gemeente
