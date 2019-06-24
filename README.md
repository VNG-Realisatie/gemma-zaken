API's voor Zaakgericht Werken
=====
[![Build Status](https://jenkins.nlx.io/job/gemma-zaken-build-and-test/badge/icon?style=plastic)](https://jenkins.nlx.io/) ![Repo Status](https://img.shields.io/badge/status-concept-lightgrey.svg?style=plastic)

**Zaakgericht werken** is een vorm van procesgericht werken waarbij de informatie die tijdens een bedrijfsproces wordt ontvangen of gecreëerd, samen met informatie over de procesuitvoering, wordt vastgelegd bij een zaak en uniform kan worden ontsloten naar alle betrokkenen.

Je kan de work-in-progress standaard [hier](docs/_content/standaard/standaard.md) lezen.

## Doel
Deze repository bevat alles wat nodig is voor de ontwikkeling van een nieuwe standaard rond Zaakgericht Werken, welke in samenwerking tussen verschillende partijen tot stand komt. Concrete resultaten zijn een OpenAPI Specificatie van de nieuwe Zaak- en Documentservices (v2.0) en bijbehorende referentie-implementaties met persistente data.

## Vragen en bijdragen
Lees meer over hoe je vragen kunt stellen, bugs kunt melden en bij kunt dragen (met code of documentatie) in [`CONTRIBUTING.md`](CONTRIBUTING.md) (EN).

## Documentatie
De volgende documenten beschrijven dit project:

- We werken aan realisatie van de [Productvisie](docs/_content/introductie/productvisie.md) (concept)
- Hoe we [samenwerken](docs/_content/introductie/samenwerking.md) is apart beschreven
- Hoe u kunt [bijdragen](docs/_content/community/bijdragen.md) (inclusief het reviewproces)
- De [FAQ](docs/_content/introductie/faq.md) beantwoordt vragen over het project
- De [dev-straat](docs/_content/overige/technisch/dev-straat.md) beschrijft de development
  inrichting en tooling
- [Technische documentatie](docs/_content/ontwikkelaars/aan-de-slag.md) voor developers
- [Designkeuzes en besluiten](docs/_content/overige/technisch/design-keuzes.md) voor scrumteam, developers en stakeholders

Een gehoste versie van de documentatie is beschikbaar op https://ref.tst.vng.cloud

## Rollen

- Opdrachtgever: [@TheoVNGPeters](https://github.com/TheoVNGPeters)
- Delivery manager: [@wishalg](https://github.com/wishalg)
- Product Owner: [@Hugo-ter-Doest](https://github.com/Hugo-ter-Doest)
- Scrum Master:  Peter de Graaf

## API spec bekijken

Zie de relevante links in dit [overzicht](docs/_content/standaard/apis/).

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

* [Gedeelde code tussen componenten](https://github.com/VNG-Realisatie/gemma-zaken-common)
* [Overige registratiescomponent](https://github.com/VNG-Realisatie/gemma-mock-overigeregistratiecomponenten)
* [![Build Status][zit-build-status]][zit-stable]
  [Integratietesten](https://github.com/VNG-Realisatie/gemma-zaken-test-integratie)
* [ZGW Client](https://github.com/VNG-Realisatie/gemma-zds-client)
* [Demo applicatie(s)](https://github.com/VNG-Realisatie/gemma-zaken-demo)
* [Postman tests voor ZGW API's](https://github.com/VNG-Realisatie/gemma-postman-tests)

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
[zit-build-status]: http://jenkins.nlx.io/buildStatus/icon?job=gemma-zaken-test-integratie-master
[zit-stable]: http://jenkins.nlx.io/job/gemma-zaken-test-integratie-master
[nc-build-status]: http://jenkins.nlx.io/buildStatus/icon?job=gemma-notificatiecomponent-stable
[nc-stable]: http://jenkins.nlx.io/job/gemma-notificatiecomponent-stable
[ac-build-status]: http://jenkins.nlx.io/buildStatus/icon?job=gemma-autorisatiecomponent-stable
[ac-stable]: http://jenkins.nlx.io/job/gemma-autorisatiecomponent-stable
