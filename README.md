API's voor Zaakgericht Werken
=====

[![Status badge][api-test-oas-status]][api-test-oas]
[![Build Status][docs-build-status]][jenkins]
![Repo Status][repo-status]

[api-test-oas-status]: https://img.shields.io/endpoint.svg?style=plastic&url=https%3A//api-test.nl/api/v1/provider-latest-badge/64a5b8c4-ab12-4cf6-bbdb-295654f2ec67/
[api-test-oas]: https://api-test.nl/server/1/be77d2e9-6843-47f9-b2d3-d426e92f1562/64a5b8c4-ab12-4cf6-bbdb-295654f2ec67/latest/
[docs-build-status]: https://jenkins.nlx.io/job/gemma-zaken-build-and-test/badge/icon?style=plastic
[jenkins]: (https://jenkins.nlx.io/
[repo-status]: https://img.shields.io/badge/Status-stable%2F1.0.x-brightgreen?style=plastic

**Zaakgericht werken** is een vorm van procesgericht werken waarbij de informatie die tijdens een bedrijfsproces wordt ontvangen of gecreëerd, samen met informatie over de procesuitvoering, wordt vastgelegd bij een zaak en uniform kan worden ontsloten naar alle betrokkenen.

## Doel
Deze repository bevat alles wat nodig is voor de ontwikkeling van een nieuwe standaard rond Zaakgericht Werken, welke in samenwerking tussen verschillende partijen tot stand komt. Concrete resultaten zijn meerdere OpenAPI Specificaties ten behoeve van zaakgericht werken en bijbehorende referentie-implementaties met persistente data.

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

## Beheer en ondersteuning

- Contact: standaarden.ondersteuning@vng.nl

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
* [![Build Status][nrc-build-status]][nrc-stable]
  [Notificatiecomponent](https://github.com/VNG-Realisatie/notificaties-api)
* [![Build Status][ac-build-status]][ac-stable]
  [Autorisatiecomponent](https://github.com/VNG-Realisatie/gemma-autorisatiecomponent)
* [![Build Status][kcc-build-status]][kcc-stable]
  [Klantinteracties API](https://github.com/VNG-Realisatie/klantinteracties-api)

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
[nrc-build-status]: http://jenkins.nlx.io/buildStatus/icon?job=gemma-notificatiecomponent-stable
[nrc-stable]: http://jenkins.nlx.io/job/gemma-notificatiecomponent-stable
[ac-build-status]: http://jenkins.nlx.io/buildStatus/icon?job=gemma-autorisatiecomponent-stable
[ac-stable]: http://jenkins.nlx.io/job/gemma-autorisatiecomponent-stable
[kcc-build-status]: https://travis-ci.org/VNG-Realisatie/klantinteracties-api.svg?branch=master
[kcc-stable]: https://travis-ci.org/VNG-Realisatie/klantinteracties-api

[vng-api-common-build-status]: https://travis-ci.org/VNG-Realisatie/vng-api-common.svg?branch=master
[vng-api-common]: https://travis-ci.org/VNG-Realisatie/vng-api-common
