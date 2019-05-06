---
title: "Begrippenlijst"
date: '8-8-2018'
weight: 10
---

In onderstaande begrippenlijst worden begrippen zoals deze gebruikt worden in de verschillende content van deze repository toegelicht.

- API: Application Programming Interface - dit is een publieke, technologie-onafhankelijke interface voor gegevensuitwisseling tussen betrokken partijen.
- BRC: Besluitregistratiecomponent. Component voor opslag en ontsluiting van (zaak)besluiten.
- BSM: Bericht Structuur Model, een UML klassediagram dat  is afgeleid van het UGM waarmee de structuur van een specifiek bericht wordt vastgelegd.
- CRUD: CRUD is een afkorting uit de informatica die staat voor de vier basisoperaties die op duurzame gegevens (meestal een database) uitgevoerd kunnen worden. Deze zijn:

    - Create (of insert): Toevoegen van nieuwe gegevens.
    - Read (of select): Opvragen van gegevens.
    - Update: Wijzigen van gegevens.
    - Delete: Verwijderen van gegevens.

- DRC: Documentregistratiecomponent. Component voor opslag en ontsluiting van documenten en daarbij behorende metadata. De component ondersteunt het opslaan en naar andere applicaties ontsluiten van informatieobjecten (in de 'volksmond': documenten). De component slaat deze gestructureerd en voorzien van de benodigde metadata op en stelt applicaties in staat deze te wijzigen, te verwijderen en aan de hand van een aantal zoekcriteria op te vragen. Zie ook https://www.gemmaonline.nl/index.php/GEMMA2/0.9/id-0e99ec6c-283a-4ec9-8efa-e11468e6b878
- EA: Enterprise Architect. Tool waarmee UML (klasse)diagrammen worden getekend.
- EAP: Xml bestand dat als tussenbestand wordt gegenereerd uit wat is geconfigureerd in het Enterprise Architect. Bevat alle informatie die nodig is om schema's, documentatie en testberichten te genereren.
- Extern model: TODO
- Entiteittype: TODO
- Gegevensmodel: In gegevensmodellen worden structuren beschreven waarmee in informatiemodellen beschreven objecten uitgewisseld worden tussen informatiesystemen. Het gaat daarbij dus NIET om complete berichtstructuren maar alleen om de content van die berichtstructuren.
- Imvertor: Software waarmee de UML klassediagram voor een koppelvlak vertaald worden naar berichtschema's.
- Informatiemodel: Een informatiemodel beschrijft de structuur, semantiek en eigenschappen van dingen in de werkelijkheid binnen een gegeven domein ongeacht hoe de gegevens ingewonnen, opgeslagen, beheerd en uitgewisseld worden. Het doet dat in termen van objecten, gegevens (attributen) daarvan en relaties daartussen.
- Klassediagram: Diagram waarin entiteiten staan beschreven met hun eigenschappen, restricties en relaties.
- Linked Data: (TODO)
- Linked Open Data: (TODO)
- Metamodel: Een metamodel is een model van een model. Een model is een abstractie van fenomenen in de echte wereld. Een metamodel is vervolgens een een abstractie van deze abstractie waarbij de eigenschappen van het model beschreven worden. Zie ook https://en.wikipedia.org/wiki/Metamodeling en https://www.noraonline.nl/wiki/Gegevensbeschrijvingen/Metagegevensmodel
- MIG: Metamodel Informatiemodel (SIM) Gemeenten waarin de structuur en eigenschappen van een SIM beschreven worden.
- MUG: Metamodel Uitwisselingsgegevensmodel (UGM) Gemeenten waarin de structuur en eigenschappen van een UGM beschreven worden.
- Objecttype: class in classdiagram (TODO)
- Open Data: (TODO)
- Proxy: View op een objecttype of attribuut dat in een ander SIM gedefinieerd wordt.
- Python: Scripttaal gebruikt voor het maken van de referentieimplementaties van de ZRC, ZTC en DRC. Zie ook https://nl.wikipedia.org/wiki/Python_(programmeertaal)
- Resource: (TODO)
- SCRUM: (TODO)
- SIM: Semantisch informatie model waarin alle begrippen die door meerdere partijen gebruikt en/of begrepen moeten worden zijn opgenomen in een samenhangend begrippenkader. Zie ook https://www.wikixl.nl/wiki/rosa/index.php/Semantisch_model en https://www.geonovum.nl/uploads/documents/Informatiemodellen_1.0.pdf
- Stereotype: Mechanisme in UML om nieuwe type elementen in een model (bijvoorbeeld een SIM) te creeëren door deze van reeds bestaande types af te leiden. Zie ook: https://en.wikipedia.org/wiki/Stereotype_(UML)
- Tracing: Leggen van een harde link tussen componenten in een UGM of koppelvlak naar gerelateerde componenten in UGM of SIM. Daarrmee worden toegekende eigenschappen en definities van de betreffende componenten die gebruikt worden in een UGM of koppelvlak overgenomen uit een (ander) UGM en/of SIM.
- UGM: Uitwisselings gegevens model - Gegevensmodel waarin de opbouw van de gegevens in uitwisseling centraal staat.
- UML: Unified Modeling Language. Visuele modelleertaal waarin we informatiemodellen en koppelvlakken definiëren. We gebruiken alleen klasse diagrammen.
- View: Weergave van een selectie van objecttypen en attributen uit een Model, bedoeld om een specifiek deel vanuit een bepaald perspectief weer te geven.
- XSLT: Extensible Stylesheet Language Transformations - De techniek waarmee XML structuren kunnen worden omgezet naar andersoortige structuren (XML, CSV, TXT, HTML) en waarmee binnen dit project de XSD-schema's specifiek volgens StUF-regels worden gegenereerd op basis van de output van de Imvertor.
- ZRC Zaakregistratiecomponent. Component voor opslag en ontsluiting van zaakgegevens. De component ondersteunt het opslaan en het naar andere applicaties ontsluiten van gegevens over alle gemeentelijke zaken, van elk type. Opslag vindt plaats conform het RGBZ waarin objecten, gegevens daarvan en onderlinge relaties zijn beschreven. Het bevat echter niet alle gegevens uit het RGBZ: documenten worden opgeslagen in het documentenregistratiecomponent, medewerkergegevens in de medewerkerregistratiecomponent, etc. Zie ook https://www.gemmaonline.nl/index.php/GEMMA2/0.9/id-a97b6545-d5a7-485d-9b13-3ce22db5b9cf
- ZTC: Zaaktypecatalogus (Component). Component voor opslag en ontsluiting van zaaktypegegevens. De component ondersteunt het opslaan en naar andere applicaties ontsluiten van zaaktypegegevens. Deze gegevens kunnen door applicaties worden gebruikt om voor zaken van een bepaald type de juiste gegevens(statussen, resultaattypen, documenttypen,..) te bepalen. Applicaties die gebruik maken van deze zaaktypegegevens zijn bijvoorbeeld een zaakafhandelcomponent, een vergunningcomponent of een subsidiecomponent. Opslag van zaaktypegegevens vindt bij voorkeur plaats conform het informatiemodel ZTC. De verzameling opgeslagen zaaktypegegevens wordt ook aangeduid met de term "zaaktypecatalogus". Zie ook https://www.gemmaonline.nl/index.php/GEMMA2/0.9/id-3ef9cdd9-631c-4d3e-88c3-f756423d6314

