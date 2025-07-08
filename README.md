| Eigenaar                   | Ingevuld door   |
| -------------------------- | --------------- |
| Kenniscentrum Architectuur | Rutger ter Borg |

# API's voor Zaakgericht Werken

**Zaakgericht werken** is een vorm van procesgericht werken waarbij de informatie die tijdens een
bedrijfsproces wordt ontvangen of gecreëerd, samen met informatie over de procesuitvoering, wordt
vastgelegd bij een zaak en uniform kan worden ontsloten naar alle betrokkenen.

## Doel

Deze repository bevat alles wat nodig is voor de ontwikkeling van een nieuwe standaard rond
Zaakgericht Werken, welke in samenwerking tussen verschillende partijen tot stand komt. Concrete
resultaten zijn meerdere OpenAPI Specificaties ten behoeve van zaakgericht werken.

## Vragen en bijdragen

Lees meer over hoe je vragen kunt stellen, bugs kunt melden en bij kunt dragen (met code of
documentatie) in [`CONTRIBUTING.md`](CONTRIBUTING.md) (EN).

## Documentatie

De volgende documenten beschrijven dit project:

- We werken aan realisatie van de
  [Productvisie](https://vng-realisatie.github.io/gemma-zaken/productvisie/) (concept)
- Hoe u kunt [bijdragen](https://vng-realisatie.github.io/gemma-zaken/doorontwikkeling/) (inclusief
  het reviewproces)
- De [FAQ](docs/overige/faq.md) beantwoordt vragen over het project
- De
  [dev-straat](https://vng-realisatie.github.io/gemma-zaken/themas/achtergronddocumentatie/ontwikkelstraat)
  beschrijft de development inrichting en tooling
- [Technische documentatie](https://vng-realisatie.github.io/gemma-zaken/ontwikkelaars/) voor
  developers
- [Designkeuzes en besluiten](https://vng-realisatie.github.io/gemma-zaken/themas/achtergronddocumentatie/ontwerpkeuzes)
  voor scrumteam, developers en stakeholders

Een hoogover overzicht van de API's voor Zaakgericht werken staat
[hier](https://www.vngrealisatie.nl/producten/api-standaarden-zaakgericht-werken). De volledige
documentatie zoals deze op github is beschreven is te vinden op de
[github pages](https://vng-realisatie.github.io/gemma-zaken/). De Visie en uitwerking van
Zaakgericht Werken in de GEMMA Architectuur staat beschreven op het
[Thema Zaakgericht werken](https://www.gemmaonline.nl/index.php/Thema_Zaakgericht_werken) op GEMMA
Online.

## Beheer en ondersteuning

- Contact: standaarden.ondersteuning@vng.nl

## <a name="api_spec">API specs van de standaard bekijken</a>

Om de API specs en aanvullende bedrijfsregels van de _standaard_ te bekijken, volg de relevante
links in dit [overzicht](https://vng-realisatie.github.io/gemma-zaken/standaard/index).

## Migratie

De folder waar voorheen `infra` te vinden was (om via ansible naar het kubernetes cluster te
deployen) is gemigreerd naar:

[zgw-infra](https://github.com/VNG-Realisatie/zgw-infra)

Het is ook te adviseren om de instructies daar te volgen wanneer je de `zgw-apis` wilt deployen of
testen.

## Snelle links

**Ondersteunende tooling**

- [![Build Status][vng-api-common-ci-status]][vng-api-common]
  [Gedeelde code tussen componenten](https://github.com/VNG-Realisatie/gemma-zaken-common)
- [![Build Status][ref-lijsten-ci-status]][ref-lijsten-ci]
  [Referentielijsten API](https://github.com/VNG-Realisatie/VNG-referentielijsten)
- [ZGW Client](https://github.com/VNG-Realisatie/gemma-zds-client)
- [Demo applicatie(s)](https://github.com/VNG-Realisatie/gemma-zaken-demo)
- [Postman tests voor ZGW API's](https://github.com/VNG-Realisatie/gemma-postman-tests)

## Licentie

Copyright © 2018–2025 VNG Realisatie.

Licensed under the [European Union Public License (EUPL) v1.2](LICENSE).
