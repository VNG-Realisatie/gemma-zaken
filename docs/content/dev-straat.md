# Dev straat

Eisen:

* Server om referentie-implementatie op te hosten
* Automatische deployment master branch referentie-implementatie
* Tooling om spec json/yaml file te genereren uit referentie-implementatie
* Automatisch committen van spec update bij mergen van user story
* ReDoc -> github pages als eerste opzet, auto-deploy via Travis

## Schema generatie

Op dit moment [ondersteunt drf-yasg enkel Swagger 2.0](https://github.com/axnsan12/drf-yasg/issues/33).
Er bestaat wel een [tool](https://github.com/mermade/swagger2openapi) die de
conversie van Swagger 2.0 naar OpenApi 3.0 kan doen.

Opmerking: OpenApi 3.0 is een re-brand van Swagger in de nieuwe versie.

Zie ook:
https://blog.readme.io/an-example-filled-guide-to-swagger-3-2/


### Risico's

* De automatische conversie van Swagger 2.0 output naar OpenApi 3.0 output
  kan foutief zijn of edge-cases missen.

* Voorgestelde wijzigingen aan de OAS 3.0 specificatie via Github (als
  pull-request, of een issue wat geopend is) moet terugvertaald worden naar
  wat dit betekent voor het Swagger 2.0 en de referentieimplementatie.
  Waarschijnlijk is de beste manier om dit aan te pakken om de semantiek van
  de wijzigingen te doorgronden, toe te passen in de referentieimplementatie
  en hiermee het Swagger 2.0 schema. Daarna kan de conversieslag van Swagger
  2.0 naar OpenApi 3.0 uitgevoerd worden, en kan vastgesteld worden of de
  voorgestelde wijzigingen inderdaad bereikt zijn.


## Server/hardware infrastructuur

Maykin communiceert wat nodig is naar Eelco, die Maykin de nodige rechten geeft.
Maykin richt verder de server(s) in.

## Inrichting git-repository

Komen referentie-implementatie en API-specificatie in dezelfde repository?

### Argumenten voor

* Harde koppeling tussen implementatie, tooling en resulterende API-spec.

* Laagdrempelig om een spec-aanpassingen voor te stellen _en_ meteen ook de
  referentie-implementatie bij te werken om een groter draagvlak voor de
  wijziging te krijgen. Dit in tegenstelling met tussen verschillende
  repositories te moeten refereren en het risico te lopen dat zaken out-of-sync
  raken.

* Duidelijkheid kan geschept worden via documentatie in de repository en een
  goede bestandsstructuur.

### Argumenten tegen

* Vervuiling door opname RGBZ 2.0 informatiemodel als datamodel

* Mogelijke vervuiling/onduidelijkheid indien StUF niet eruit gesloopt wordt.

* De API-spec is losjes gekoppeld met de refernetie-implementatie. Voor
  leveranciers moet de API spec aangehouden worden. De referentie-implementatie
  geeft duidelijkheid waar interpretatie mogelijk is, maar hoeft niet gebruikt
  te worden.


## Voorgestelde bestandsstructuur

    .
    ├── api-specificatie
    │   ├── zrc
    │   │   ├── schema.json
    │   │   └── schema.yaml
    │   └── ztc
    │       ├── schema.json
    │       └── schema.yaml
    ├── CONTRIBUTING.md
    ├── docs
    │   └── content
    │       ├── dev-straat.md
    │       └── introduction
    │           ├── productvisie.md
    │           └── samenwerking.md
    ├── LICENCE.md
    ├── README.md
    └── referentie
        ├── zaakregistratiecomponent
        │   └── src
        └── zaaktypecataloguscomponent
            └── src
