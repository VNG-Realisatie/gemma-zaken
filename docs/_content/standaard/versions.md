---
title: API versies
date: '05-05-2020'
weight: 30
---

<a href="#zaken-api">Zaken API</a> | <a href="#documenten-api">Documenten API</a> | <a href="#besluiten-api">Besluiten API</a> | <a href="#catalogi-api">Catalogi API</a> | <a href="#autorisaties-api">Autorisaties API</a> | <a href="#notificaties-api">Notificaties API</a>

## Algemeen

Een API versie wordt als volgt aangeduid: `<major>.<minor>.<patch>`. Hierbij
geldt dat:

* **Major** - Een major versie update (bijv. van `1.x` naar `2.x`) bevat 
  breaking changes t.o.v. de vorige major versie.
* **Minor** - Een minor versie update (bijv. van `1.0.x` naar `1.1.x`) bevat 
  inhoudelijke wijzigingen aan de API die geen breaking changes betreffen.
* **Patch** - Een patch versie update (bijv. van `1.0.0` naar `1.0.1`) bevat 
  geen inhoudelijke wijzigingen maar slechts documentatie of soepelere 
  validatie regels.

Elke *major* API versie krijgt **minimaal** 1 jaar ondersteuning vanaf de 
release datum van de volgende *major* API versie.

Er wordt **maximaal** 1 *major* versie per jaar gepubliceerd.

Er worden **minimaal** 2 major versies onderhouden middels updates. Dit 
betekent dat er voor deze versies gelijktijdig *minor* en *patch* updates 
worden uitgebracht.

*Opmerking: Er kunnen "tags" bestaan zoals `x.y.z.post0`. Dit zijn 
verbeteringen in de referentie implementatie en betreffen nooit een gewijzigde
API specificatie t.o.v. `x.y.z`.*


## Zaken API

* [Alle versies en wijzigingen](https://github.com/VNG-Realisatie/gemma-zaakregistratiecomponent/blob/develop/CHANGELOG.rst)

### Ondersteuning

Versie   | Release datum | Einddatum ondersteuning | Documentatie
-------- | ------------- | ------------------------|-------------
1.x      | 2019-11-18    | (nog niet bekend)       | [Documentatie][zaken-1.x-docs]

[zaken-1.x-docs]: https://vng-realisatie.github.io/gemma-zaken/standaard/zaken/index

### Releases

Versie   | Release datum | API specificatie 
-------- | ------------- | ----------------
1.0.2    | 2020-06-12    | [ReDoc][zaken-1.0.2-redoc], [Swagger][zaken-1.0.2-swagger], [Diff][zaken-1.0.2-diff]
1.0.1    | 2019-12-16    | [ReDoc][zaken-1.0.1-redoc], [Swagger][zaken-1.0.1-swagger], [Diff][zaken-1.0.1-diff]
1.0.0    | 2019-11-18    | [ReDoc][zaken-1.0.0-redoc], [Swagger][zaken-1.0.0-swagger]

[zaken-1.0.2-redoc]: https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/VNG-Realisatie/gemma-zaakregistratiecomponent/1.0.2/src/openapi.yaml
[zaken-1.0.2-swagger]: https://petstore.swagger.io/?url=https://raw.githubusercontent.com/VNG-Realisatie/gemma-zaakregistratiecomponent/1.0.2/src/openapi.yaml
[zaken-1.0.2-diff]: https://github.com/VNG-Realisatie/gemma-zaakregistratiecomponent/compare/1.0.1...1.0.2?diff=split#diff-3dc0f8f7373b32ea3bf5eabe02993f9a

[zaken-1.0.1-redoc]: https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/VNG-Realisatie/gemma-zaakregistratiecomponent/1.0.1/src/openapi.yaml
[zaken-1.0.1-swagger]: https://petstore.swagger.io/?url=https://raw.githubusercontent.com/VNG-Realisatie/gemma-zaakregistratiecomponent/1.0.1/src/openapi.yaml
[zaken-1.0.1-diff]: https://github.com/VNG-Realisatie/gemma-zaakregistratiecomponent/compare/1.0.0...1.0.1?diff=split#diff-3dc0f8f7373b32ea3bf5eabe02993f9a

[zaken-1.0.0-redoc]: https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/VNG-Realisatie/gemma-zaakregistratiecomponent/1.0.0/src/openapi.yaml
[zaken-1.0.0-swagger]: https://petstore.swagger.io/?url=https://raw.githubusercontent.com/VNG-Realisatie/gemma-zaakregistratiecomponent/1.0.0/src/openapi.yaml


## Documenten API

* [Alle versies en wijzigingen](https://github.com/VNG-Realisatie/gemma-documentregistratiecomponent/blob/develop/CHANGELOG.rst)

### Ondersteuning

Versie   | Release datum | Einddatum ondersteuning | Documentatie
-------- | ------------- | ------------------------|-------------
1.x      | 2019-11-18    | (nog niet bekend)       | [Documentatie][documenten-1.x-docs]

[documenten-1.x-docs]: https://vng-realisatie.github.io/gemma-zaken/standaard/documenten/index

### Releases

Versie   | Release datum | API specificatie 
-------- | ------------- | ----------------
1.0.1    | 2019-12-16    | [ReDoc][documenten-1.0.1-redoc], [Swagger][documenten-1.0.1-swagger], [Diff][documenten-1.0.1-diff]
1.0.0    | 2019-11-18    | [ReDoc][documenten-1.0.0-redoc], [Swagger][documenten-1.0.0-swagger]

[documenten-1.0.1-redoc]: https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/VNG-Realisatie/gemma-documentregistratiecomponent/1.0.1/src/openapi.yaml
[documenten-1.0.1-swagger]: https://petstore.swagger.io/?url=https://raw.githubusercontent.com/VNG-Realisatie/gemma-documentregistratiecomponent/1.0.1/src/openapi.yaml
[documenten-1.0.1-diff]: https://github.com/VNG-Realisatie/gemma-documentregistratiecomponent/compare/1.0.0...1.0.1?diff=split#diff-3dc0f8f7373b32ea3bf5eabe02993f9a

[documenten-1.0.0-redoc]: https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/VNG-Realisatie/gemma-documentregistratiecomponent/1.0.0/src/openapi.yaml
[documenten-1.0.0-swagger]: https://petstore.swagger.io/?url=https://raw.githubusercontent.com/VNG-Realisatie/gemma-documentregistratiecomponent/1.0.0/src/openapi.yaml


## Besluiten API

* [Alle versies en wijzigingen](https://github.com/VNG-Realisatie/gemma-besluitregistratiecomponent/blob/develop/CHANGELOG.rst)

### Ondersteuning

Versie   | Release datum | Einddatum ondersteuning | Documentatie
-------- | ------------- | ------------------------|-------------
1.x      | 2019-11-18    | (nog niet bekend)       | [Documentatie][besluiten-1.x-docs]

[besluiten-1.x-docs]: https://vng-realisatie.github.io/gemma-zaken/standaard/besluiten/index

### Releases

Versie   | Release datum | API specificatie 
-------- | ------------- | ----------------
1.0.1    | 2019-12-16    | [ReDoc][besluiten-1.0.1-redoc], [Swagger][besluiten-1.0.1-swagger], [Diff][besluiten-1.0.1-diff]
1.0.0    | 2019-11-18    | [ReDoc][besluiten-1.0.0-redoc], [Swagger][besluiten-1.0.0-swagger]

[besluiten-1.0.1-redoc]: https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/VNG-Realisatie/gemma-besluitregistratiecomponent/1.0.1/src/openapi.yaml
[besluiten-1.0.1-swagger]: https://petstore.swagger.io/?url=https://raw.githubusercontent.com/VNG-Realisatie/gemma-besluitregistratiecomponent/1.0.1/src/openapi.yaml
[besluiten-1.0.1-diff]: https://github.com/VNG-Realisatie/gemma-besluitregistratiecomponent/compare/1.0.0...1.0.1?diff=split#diff-3dc0f8f7373b32ea3bf5eabe02993f9a

[besluiten-1.0.0-redoc]: https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/VNG-Realisatie/gemma-besluitregistratiecomponent/1.0.0/src/openapi.yaml
[besluiten-1.0.0-swagger]: https://petstore.swagger.io/?url=https://raw.githubusercontent.com/VNG-Realisatie/gemma-besluitregistratiecomponent/1.0.0/src/openapi.yaml


## Catalogi API

* [Alle versies en wijzigingen](https://github.com/VNG-Realisatie/gemma-zaaktypecatalogus/blob/develop/CHANGELOG.rst)

### Ondersteuning

Versie   | Release datum | Einddatum ondersteuning | Documentatie
-------- | ------------- | ------------------------|-------------
1.x      | 2019-11-18    | (nog niet bekend)       | [Documentatie][catalogi-1.x-docs]

[catalogi-1.x-docs]: https://vng-realisatie.github.io/gemma-zaken/standaard/catalogi/index

### Releases

Versie   | Release datum | API specificatie 
-------- | ------------- | ----------------
1.0.0    | 2019-11-18    | [ReDoc][catalogi-1.0.0-redoc], [Swagger][catalogi-1.0.0-swagger]

[catalogi-1.0.1-redoc]: https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/VNG-Realisatie/gemma-zaaktypecatalogus/1.0.1/src/openapi.yaml
[catalogi-1.0.1-swagger]: https://petstore.swagger.io/?url=https://raw.githubusercontent.com/VNG-Realisatie/gemma-zaaktypecatalogus/1.0.1/src/openapi.yaml
[catalogi-1.0.1-diff]: https://github.com/VNG-Realisatie/gemma-zaaktypecatalogus/compare/1.0.0...1.0.1?diff=split#diff-3dc0f8f7373b32ea3bf5eabe02993f9a

[catalogi-1.0.0-redoc]: https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/VNG-Realisatie/gemma-zaaktypecatalogus/1.0.0/src/openapi.yaml
[catalogi-1.0.0-swagger]: https://petstore.swagger.io/?url=https://raw.githubusercontent.com/VNG-Realisatie/gemma-zaaktypecatalogus/1.0.0/src/openapi.yaml


## Autorisaties API

* [Alle versies en wijzigingen](https://github.com/VNG-Realisatie/gemma-autorisatiecomponent/blob/develop/CHANGELOG.rst)

### Ondersteuning

Versie   | Release datum | Einddatum ondersteuning | Documentatie
-------- | ------------- | ------------------------|-------------
1.x      | 2019-11-18    | (nog niet bekend)       | [Documentatie][autorisaties-1.x-docs]

[autorisaties-1.x-docs]: https://vng-realisatie.github.io/gemma-zaken/standaard/autorisaties/index

### Releases

Versie   | Release datum | API specificatie 
-------- | ------------- | ----------------
1.0.0    | 2019-11-18    | [ReDoc][autorisaties-1.0.0-redoc], [Swagger][autorisaties-1.0.0-swagger]

[autorisaties-1.0.1-redoc]: https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/VNG-Realisatie/gemma-autorisatiecomponent/1.0.1/src/openapi.yaml
[autorisaties-1.0.1-swagger]: https://petstore.swagger.io/?url=https://raw.githubusercontent.com/VNG-Realisatie/gemma-autorisatiecomponent/1.0.1/src/openapi.yaml
[autorisaties-1.0.1-diff]: https://github.com/VNG-Realisatie/gemma-autorisatiecomponent/compare/1.0.0...1.0.1?diff=split#diff-3dc0f8f7373b32ea3bf5eabe02993f9a

[autorisaties-1.0.0-redoc]: https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/VNG-Realisatie/gemma-autorisatiecomponent/1.0.0/src/openapi.yaml
[autorisaties-1.0.0-swagger]: https://petstore.swagger.io/?url=https://raw.githubusercontent.com/VNG-Realisatie/gemma-autorisatiecomponent/1.0.0/src/openapi.yaml


## Notificaties API

* [Alle versies en wijzigingen](https://github.com/VNG-Realisatie/notificaties-api/blob/develop/CHANGELOG.rst)

### Ondersteuning

Versie   | Release datum | Einddatum ondersteuning | Documentatie
-------- | ------------- | ------------------------|-------------
1.x      | 2019-11-18    | (nog niet bekend)       | [Documentatie][notificaties-1.x-docs]

[notificaties-1.x-docs]: https://vng-realisatie.github.io/gemma-zaken/standaard/notificaties/index

### Releases

Versie   | Release datum | API specificatie 
-------- | ------------- | ----------------
1.0.0    | 2019-11-18    | [ReDoc][notificaties-1.0.0-redoc], [Swagger][notificaties-1.0.0-swagger]

[notificaties-1.0.1-redoc]: https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/VNG-Realisatie/notificaties-api/1.0.1/src/openapi.yaml
[notificaties-1.0.1-swagger]: https://petstore.swagger.io/?url=https://raw.githubusercontent.com/VNG-Realisatie/notificaties-api/1.0.1/src/openapi.yaml
[notificaties-1.0.1-diff]: https://github.com/VNG-Realisatie/notificaties-api/compare/1.0.0...1.0.1?diff=split#diff-3dc0f8f7373b32ea3bf5eabe02993f9a

[notificaties-1.0.0-redoc]: https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/VNG-Realisatie/notificaties-api/1.0.0/src/openapi.yaml
[notificaties-1.0.0-swagger]: https://petstore.swagger.io/?url=https://raw.githubusercontent.com/VNG-Realisatie/notificaties-api/1.0.0/src/openapi.yaml



