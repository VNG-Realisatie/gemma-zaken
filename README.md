API's voor Zaakgericht Werken
=====

[![Status badge][api-test-fullsuite-status]][api-test-fullsuite]
[![Build Status][docs-ci-status]][docs-ci]
![Repo Status][repo-status]

[api-test-fullsuite-status]: https://shields.api-test.nl/endpoint.svg?style=plastic&url=https%3A//api-test.nl/api/v1/provider-latest-badge/6ad4f59e-7051-491d-a601-488f1b66ad7d/
[api-test-fullsuite]: https://api-test.nl/server/1/224fd5be-bc64-4d55-a190-454bee3cc8e3/6ad4f59e-7051-491d-a601-488f1b66ad7d/latest/
[docs-ci-status]: https://travis-ci.org/VNG-Realisatie/gemma-zaken.svg?branch=master
[docs-ci]: https://travis-ci.org/VNG-Realisatie/gemma-zaken
[repo-status]: https://img.shields.io/badge/Status-stable%2F1.0.x-brightgreen?style=plastic


**Zaakgericht werken** is een vorm van procesgericht werken waarbij de informatie die tijdens een bedrijfsproces wordt ontvangen of gecreëerd, samen met informatie over de procesuitvoering, wordt vastgelegd bij een zaak en uniform kan worden ontsloten naar alle betrokkenen.

## Doel
Deze repository bevat alles wat nodig is voor de ontwikkeling van een nieuwe standaard rond Zaakgericht Werken, welke in samenwerking tussen verschillende partijen tot stand komt. Concrete resultaten zijn meerdere OpenAPI Specificaties ten behoeve van zaakgericht werken en bijbehorende referentie-implementaties met persistente data.

## Vragen en bijdragen
Lees meer over hoe je vragen kunt stellen, bugs kunt melden en bij kunt dragen (met code of documentatie) in [`CONTRIBUTING.md`](CONTRIBUTING.md) (EN).

## Documentatie
De volgende documenten beschrijven dit project:

- We werken aan realisatie van de [Productvisie](https://vng-realisatie.github.io/gemma-zaken/productvisie/) (concept)
- Hoe u kunt [bijdragen](https://vng-realisatie.github.io/gemma-zaken/doorontwikkeling/) (inclusief het reviewproces)
- De [FAQ](docs/_content/overige/faq.md) beantwoordt vragen over het project
- De [dev-straat](https://vng-realisatie.github.io/gemma-zaken/themas/achtergronddocumentatie/ontwikkelstraat) beschrijft de development
  inrichting en tooling
- [Technische documentatie](https://vng-realisatie.github.io/gemma-zaken/ontwikkelaars/) voor developers
- [Designkeuzes en besluiten](https://vng-realisatie.github.io/gemma-zaken/themas/achtergronddocumentatie/ontwerpkeuzes) voor scrumteam, developers en stakeholders

Een hoogover overzicht van de API's voor Zaakgericht werken staat [hier](https://www.vngrealisatie.nl/producten/api-standaarden-zaakgericht-werken). De volledige documentatie zoals deze op github is beschreven is te vinden op de [github pages](https://vng-realisatie.github.io/gemma-zaken/).
De Visie en uitwerking van Zaakgericht Werken in de GEMMA Architectuur staat beschreven op het [Thema Zaakgericht werken](https://www.gemmaonline.nl/index.php/Thema_Zaakgericht_werken) op GEMMA Online.

## Beheer en ondersteuning

- Contact: standaarden.ondersteuning@vng.nl

## API spec bekijken

Zie de relevante links in dit [overzicht](https://vng-realisatie.github.io/gemma-zaken/standaard/index).

## Snelle links

**Referentie-implementaties van componenten**

* [![Build Status][zrc-ci-status]][zrc-ci]
  [Zaakregistratiecomponent](https://github.com/vng-Realisatie/gemma-zaakregistratiecomponent)
* [![Build Status][drc-ci-status]][drc-ci]
  [Documentregistratiecomponent](https://github.com/vng-Realisatie/gemma-documentregistratiecomponent)
* [![Build Status][ztc-ci-status]][ztc-ci]
  [Zaaktypecatalogus](https://github.com/vng-Realisatie/gemma-zaaktypecatalogus)
* [![Build Status][brc-ci-status]][brc-ci]
  [Besluitregistratiecomponent](https://github.com/vng-Realisatie/gemma-besluitregistratiecomponent)
* [![Build Status][nrc-ci-status]][nrc-ci]
  [Notificatiecomponent](https://github.com/VNG-Realisatie/notificaties-api)
* [![Build Status][ac-ci-status]][ac-ci]
  [Autorisatiecomponent](https://github.com/VNG-Realisatie/gemma-autorisatiecomponent)
* [![Build Status][kcc-ci-status]][kcc-ci]
  [Klantinteracties API](https://github.com/VNG-Realisatie/klantinteracties-api)

**Ondersteunende tooling**

* [![Build Status][vng-api-common-ci-status]][vng-api-common]
  [Gedeelde code tussen componenten](https://github.com/VNG-Realisatie/gemma-zaken-common)
* [![Build Status][ref-lijsten-ci-status]][ref-lijsten-ci]
  [Referentielijsten API](https://github.com/VNG-Realisatie/VNG-referentielijsten)
* [ZGW Client](https://github.com/VNG-Realisatie/gemma-zds-client)
* [Demo applicatie(s)](https://github.com/VNG-Realisatie/gemma-zaken-demo)
* [Postman tests voor ZGW API's](https://github.com/VNG-Realisatie/gemma-postman-tests)

## Licentie

Copyright © VNG Realisatie 2018 - 2020

[Licensed under the EUPL](LICENCE.md)

[zrc-ci-status]: https://travis-ci.org/VNG-Realisatie/gemma-zaakregistratiecomponent.svg?branch=master
[zrc-ci]: https://travis-ci.org/VNG-Realisatie/gemma-zaakregistratiecomponent
[drc-ci-status]: https://travis-ci.org/VNG-Realisatie/gemma-documentregistratiecomponent.svg?branch=master
[drc-ci]: https://travis-ci.org/VNG-Realisatie/gemma-documentregistratiecomponent
[ztc-ci-status]: https://travis-ci.org/VNG-Realisatie/gemma-zaaktypecatalogus.svg?branch=master
[ztc-ci]: https://travis-ci.org/VNG-Realisatie/gemma-zaaktypecatalogus
[brc-ci-status]: https://travis-ci.org/VNG-Realisatie/gemma-besluitregistratiecomponent.svg?branch=master
[brc-ci]: https://travis-ci.org/VNG-Realisatie/gemma-besluitregistratiecomponent
[nrc-ci-status]: https://travis-ci.org/VNG-Realisatie/notificaties-api.svg?branch=master
[nrc-ci]: https://travis-ci.org/VNG-Realisatie/notificaties-api
[ac-ci-status]: https://travis-ci.org/VNG-Realisatie/gemma-autorisatiecomponent.svg?branch=master
[ac-ci]: https://travis-ci.org/VNG-Realisatie/gemma-autorisatiecomponent
[kcc-ci-status]: https://travis-ci.org/VNG-Realisatie/klantinteracties-api.svg?branch=master
[kcc-ci]: https://travis-ci.org/VNG-Realisatie/klantinteracties-api

[ref-lijsten-ci-status]:  https://travis-ci.org/VNG-Realisatie/VNG-referentielijsten.svg?branch=master
[ref-lijsten-ci]:  https://travis-ci.org/VNG-Realisatie/VNG-referentielijsten

[vng-api-common-ci-status]: https://travis-ci.org/VNG-Realisatie/vng-api-common.svg?branch=master
[vng-api-common]: https://travis-ci.org/VNG-Realisatie/vng-api-common
