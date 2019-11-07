API's voor Zaakgericht Werken
=====
[![Status badge](https://img.shields.io/endpoint.svg?style=plastic&url=https%3A//api-test.nl/api/v1/provider-latest-badge/64a5b8c4-ab12-4cf6-bbdb-295654f2ec67/)] (https://api-test.nl/server/1/be77d2e9-6843-47f9-b2d3-d426e92f1562/64a5b8c4-ab12-4cf6-bbdb-295654f2ec67/latest/)[![Build Status](https://jenkins.nlx.io/job/gemma-zaken-build-and-test/badge/icon?style=plastic)](https://jenkins.nlx.io/) ![Repo Status](https://img.shields.io/badge/status-concept-lightgrey.svg?style=plastic) 


**Zaakgericht werken** is een vorm van procesgericht werken waarbij de informatie die tijdens een bedrijfsproces wordt ontvangen of gecreëerd, samen met informatie over de procesuitvoering, wordt vastgelegd bij een zaak en uniform kan worden ontsloten naar alle betrokkenen.

Je kan de work-in-progress standaard [hier](docs/_content/standaard/index.md) lezen.

## Doel
Deze repository bevat alles wat nodig is voor de ontwikkeling van een nieuwe standaard rond Zaakgericht Werken, welke in samenwerking tussen verschillende partijen tot stand komt. Concrete resultaten zijn een OpenAPI Specificatie van de nieuwe Zaak- en Documentservices (v2.0) en bijbehorende referentie-implementaties met persistente data.

## Vragen en bijdragen
Lees meer over hoe je vragen kunt stellen, bugs kunt melden en bij kunt dragen (met code of documentatie) in [`CONTRIBUTING.md`](CONTRIBUTING.md) (EN).

## Documentatie
De volgende documenten beschrijven dit project:

- We werken aan realisatie van de [Productvisie](docs/_content/productvisie/index.md) (concept)
- Hoe u kunt [bijdragen](docs/_content/doorontwikkeling/index.md) (inclusief het reviewproces)
- De [FAQ](docs/_content/overige/faq.md) beantwoordt vragen over het project
- De [dev-straat](docs/_content/themas/achtergronddocumentatie/ontwikkelstraat.md) beschrijft de development
  inrichting en tooling
- [Technische documentatie](docs/_content/ontwikkelaars/index.md) voor developers
- [Designkeuzes en besluiten](docs/_content/themas/achtergronddocumentatie/ontwerpkeuzes.md) voor scrumteam, developers en stakeholders

Een gehoste versie van de documentatie is beschikbaar op https://zaakgerichtwerken.vng.cloud

## Rollen

- Opdrachtgever: [@TheoVNGPeters](https://github.com/TheoVNGPeters)
- Delivery manager: [@wishalg](https://github.com/wishalg)
- Product Owner: [@Hugo-ter-Doest](https://github.com/Hugo-ter-Doest)
- Scrum Master:  Peter de Graaf

## API spec bekijken

Zie de relevante links in dit [overzicht](docs/_content/standaard/index.md).

## Snelle links

**Referentie-implementaties van componenten**

* [![Build Status][zrc-build-status]][zrc-stable]
  [Zaakregistratiecomponent](https://github.com/vng-Realisatie/gemma-zaakregistratiecomponent)
* [![Build Status][drc-build-status]][drc-stable]
  [Documentregistratiecomponent](https://github.com/vng-Realisatie/gemma-documentregistratiecomponent)
* [![Build Status][ztc-build-status]][ztc-stable]
  [Zaaktypecatalogus](https://github.com/vng-Realisatie/gemma-zaaktypecatalogus)
* [![Build Status][brc-build-status]][brc-stable]
  [Besluitregistratiecomponent](https://github.com/vng-Realisatie/gemma-besluitregistratiecomponent)
* [![Build Status][nc-build-status]][nc-stable]
  [Notificatiecomponent](https://github.com/VNG-Realisatie/gemma-notificatiecomponent)
* [![Build Status][ac-build-status]][ac-stable]
  [Autorisatiecomponent](https://github.com/VNG-Realisatie/gemma-autorisatiecomponent)


**Ondersteunende tooling**

* [![Build Status][vng-api-common-build-status]][vng-api-common]
  [Gedeelde code tussen componenten](https://github.com/VNG-Realisatie/gemma-zaken-common)
* [ZGW Client](https://github.com/VNG-Realisatie/gemma-zds-client)
* [Demo applicatie(s)](https://github.com/VNG-Realisatie/gemma-zaken-demo)
* [Postman tests voor ZGW API's](https://github.com/VNG-Realisatie/gemma-postman-tests)
* [Referentielijsten API](https://github.com/VNG-Realisatie/VNG-referentielijsten)

## Licentie
Copyright © VNG Realisatie 2018

[Licensed under the EUPL](LICENCE.md)

[zrc-build-status]: http://jenkins.nlx.io/buildStatus/icon?job=gemma-zaakregistratiecomponent-stable
[zrc-stable]: http://jenkins.nlx.io/job/gemma-zaakregistratiecomponent-stable
[drc-build-status]: http://jenkins.nlx.io/buildStatus/icon?job=gemma-documentregistratiecomponent-stable
[drc-stable]: http://jenkins.nlx.io/job/gemma-documentregistratiecomponent-stable
[ztc-build-status]: http://jenkins.nlx.io/buildStatus/icon?job=gemma-zaaktypecatalogus-stable
[ztc-stable]: http://jenkins.nlx.io/job/gemma-zaaktypecatalogus-stable
[brc-build-status]: http://jenkins.nlx.io/buildStatus/icon?job=gemma-besluitregistratiecomponent-stable
[brc-stable]: http://jenkins.nlx.io/job/gemma-besluitregistratiecomponent-stable
[nc-build-status]: http://jenkins.nlx.io/buildStatus/icon?job=gemma-notificatiecomponent-stable
[nc-stable]: http://jenkins.nlx.io/job/gemma-notificatiecomponent-stable
[ac-build-status]: http://jenkins.nlx.io/buildStatus/icon?job=gemma-autorisatiecomponent-stable
[ac-stable]: http://jenkins.nlx.io/job/gemma-autorisatiecomponent-stable

[vng-api-common-build-status]: https://travis-ci.org/VNG-Realisatie/vng-api-common.svg?branch=master
[vng-api-common]: https://travis-ci.org/VNG-Realisatie/vng-api-common
