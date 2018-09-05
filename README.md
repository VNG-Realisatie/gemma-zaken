ZAKEN volgens GEMMA 2.0
=====
[![Build Status](https://jenkins.nlx.io/job/gemma-zaken-build-and-test/badge/icon?style=plastic)](https://jenkins.nlx.io/) ![Repo Status](https://img.shields.io/badge/status-concept-lightgrey.svg?style=plastic)

**Zaakgericht werken** is een vorm van procesgericht werken waarbij de informatie die tijdens een bedrijfsproces wordt ontvangen of gecreëerd, samen met informatie over de procesuitvoering, wordt vastgelegd bij een zaak en uniform kan worden ontsloten naar alle betrokkenen.

Je kan de work-in-progress standaard [hier](./standaard.md) lezen.

## Doel
Deze repository bevat alles wat nodig is voor de ontwikkeling van een nieuwe standaard rond Zaakgericht Werken, welke in samenwerking tussen verschillende partijen tot stand komt. Concrete resultaten zijn een OpenAPI Specificatie van de nieuwe Zaak- en Documentservices (v2.0) en bijbehorende referentie-implementaties met persistente data.

## Vragen en bijdragen
Lees meer over hoe je vragen kunt stellen, bugs kunt melden en bij kunt dragen (met code of documentatie) in [`CONTRIBUTING.md`](CONTRIBUTING.md) (EN).

## Documentatie
De volgende documenten beschrijven dit project:

- We werken aan realisatie van de [Productvisie](./docs/content/introduction/productvisie.md) (concept)
- Hoe we [samenwerken](./docs/content/introduction/samenwerking.md) is apart beschreven
- Hoe u kunt [bijdragen](./docs/content/introduction/bijdragen.md) (inclusief het reviewproces)
- De [FAQ](./docs/content/introduction/faq.md) beantwoordt vragen over het project
- De [dev-straat](./docs/content/developers/dev-straat.md) beschrijft de development
  inrichting en tooling
- [Technische documentatie](./docs/content/developers/_index.md) voor developers

Een gehoste versie van de documentatie is beschikbaar op https://ref.tst.vng.cloud

## Rollen

- Opdrachtgever: [@TheoVNGPeters](https://github.com/TheoVNGPeters)
- Projectleider: [@wishalg](https://github.com/wishalg)
- Product Owner: [@ehotting](https://github.com/ehotting)
- Scrum Master:  [@TCIMEddy](https://github.com/TCIMEddy)

## API spec bekijken

Zie de relevante links in dit [overzicht](./docs/content/developers/api-specificaties.md).

## Snelle links

**Referentiecomponenten**

* [Zaakregistratiecomponent](https://github.com/vng-Realisatie/gemma-zaakregistratiecomponent)
* [Documentregistratiecomponent](https://github.com/vng-Realisatie/gemma-documentregistratiecomponent)
* [Zaaktypecatalogus](https://github.com/vng-Realisatie/gemma-zaaktypecatalogus)

**Ondersteunende tooling**

* [Gedeelde code tussen componenten](https://github.com/VNG-Realisatie/gemma-zaken-common)
* [Overige registratiescomponent](https://github.com/VNG-Realisatie/gemma-mock-overigeregistratiecomponenten)
* [Integratietesten](https://github.com/VNG-Realisatie/gemma-zaken-test-integratie)
* [ZDS Client](https://github.com/VNG-Realisatie/gemma-zds-client)
* [Demo applicatie(s)](https://github.com/VNG-Realisatie/gemma-zaken-demo)

## Licentie
Copyright © VNG Realisatie 2018

[Licensed under the EUPL](LICENCE.md)
