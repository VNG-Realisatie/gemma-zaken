---
title: "Type documentatie"
date: '9-8-2018'
---

De documentatie is geschreven voor verschillende doelgroepen en voor zowel het client- als het server-perspectief.


## Functionele documentatie

**Vorm**

Online of PDF-document.

**Doel en doelgroep**

De *functionele documentatie* van de API is bedoeld voor business developers, architecten, ontwerpers en ontwikkelaars om een goede indruk te krijgen wat de service doet en hoe deze in de GEMMA architectuur past.

**Indeling**

Dit document beantwoordt de volgende vragen:

* Welke functionaliteit en/of welke data biedt de API?
* Waar bevindt deze API zich in de GEMMA architectuur?
* Welke relaties zijn er met andere API's (ook toegelicht aan de hand van proces)?
* Welke standaarden en informatiemodellen worden er gehanteerd?
* Welke beveiligingsmaatregelen zijn er op deze API van toepassing (toegang, authenticatie, privacy, ...)?

**Voorbeelden**

* [Functionele documentatie ROD API](https://www.pre.omgevingswet.overheid.nl/knooppunt/apistore/site/themes/dso/templates/api/documentation/download.jag?tenant=carbon.super&resourceUrl=/registry/resource/_system/governance/apimgt/applicationdata/provider/Kadaster/Omgevingsdocumenten-Opvragen/v1/documentation/files/Functionele%20documentatie%20Registratie%20Omgevingsdocumenten%20Afnamepunt%20API%20v1.pdf)


## API documentatie

**Vorm**

Online (interactief) naslagwerk

**Doel en doelgroep**

De *API documentatie* is voor ontwikkelaars van zowel client- als server-software die op detail niveau willen weten welke resources de API ontsluit en welke velden per resource beschikbaar zijn.

**Indeling**

Dit document beantwoordt de volgende vragen:

* Hoe krijg ik toegang tot de API?
* Welke resources zijn beschikbaar binnen de API?
* Wat zijn de veld specificaties van alle velden in een resource?
* Welke operaties kunnes uitgevoerd worden op een resource?
* Welke antwoorden kan ik verwachten van een resource?

**Voorbeelden**

* [Petstore ReDoc documentatie](https://redocly.github.io/redoc/)
* [Petstore Swagger documentatie](http://petstore.swagger.io/)
* [GMail API documentatie](https://developers.google.com/gmail/api/v1/reference/?hl=nl)

## Component implementatie documentatie

**Vorm**

Online handleiding en design keuzes (eventueel met voorbeeld database)

**Doel en doelgroep**

De *component implementatie documentatie* is voor ontwikkelaars die een eigen component implementatie realiseren met als doel compliant te zijn met de referentie API-specificatie.

**Indeling**

Dit document beantwoordt de volgende vragen:

* Welke design keuzes zijn gemaakt bij de referentie implementatie?
* Welke standaard functies zijn voor elke resource beschikbaar?
* Wat is verplicht, en wat is optioneel om te ondersteunen?
* Wat zijn de richtlijnen voor caching, concurrency, transacties, linked data, en andere technische onderwerpen?
* Hoe kan een eigen component implementatie geverifieerd worden?

**Voorbeelden**

* [DSO API- en URI strategie](https://aandeslagmetdeomgevingswet.nl/digitaal-stelsel/documenten/documenten/api-uri-strategie/)


## Client implementatie documentatie

**Vorm**

Online handleiding en voorbeelden voor gebruik van de API.

**Doel en doelgroep**

De *client implementatie documentatie* is voor ontwikkelaars die een eigen client implementatie realiseren met als doel te communiceren met het component.

**Indeling**

Dit document beantwoordt de volgende vragen:

* Wat zijn typische use-cases/verzoeken die een client zou kunnen maken?
* Wat zijn de best practices?
* Wat zijn de standaard functies die elke resource biedt?
* Hoe om te gaan met fout situaties?
* Wat zijn de richtlijnen voor caching, concurrency, transacties, linked data, en andere technische onderwerpen?
* Hoe kan een eigen client implementatie geverifieerd worden?

**Voorbeelden**

* [GMail API Guide](https://developers.google.com/gmail/api/guides/?hl=nl)
