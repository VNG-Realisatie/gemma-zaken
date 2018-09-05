# Zaakdocumentservices 2.0 Standaard

#### Versie 0.1

## Inleiding

[TODO]

## Inhoudsopgave

- [Beschikbaar stellen van API-spec](#beschikbaar-stellen-van-api-spec)
- [Zaakregistratiecomponent](#zaakregistratiecomponent)

## Beschikbaar stellen van API-spec

Iedere component MOET het OAS schema serveren.

(TODO: uitbreiden met *waar* dit schema moet beschikbaar zijn)

## Zaakregistratiecomponent

Zaakregistratiecomponenten (ZRC) MOETEN aan twee aspecten voldoen:

* de ZRC `openapi.yaml` MOET volledig geïmplementeerd zijn

* het run-time gedrag beschreven in deze standaard MOET correct geïmplementeerd
  zijn.

### OpenAPI specificatie

Alle operaties beschreven in [`openapi.yaml`](./api-specificatie/zrc/openapi.yaml)
MOETEN ondersteund worden en tot hetzelfde resultaat leiden als de referentie-
implementatie van het ZRC.

Het is NIET TOEGESTAAN om gebruik te maken van operaties die niet beschreven
staan in deze OAS spec, of om uitbreidingen op operaties in welke vorm dan ook
toe te voegen.


### Run-time gedrag

Bepaalde gedragen kunnen niet in een OAS spec uitgedrukt worden omdat ze
business-logica bevatten. Deze gedragingen zijn hieronder beschreven en MOETEN
zoals beschreven geïmplementeerd worden.

#### Valideren `zaaktype` op de `Zaak`-resource

Bij het aanmaken (`zaak_create`) en bijwerken (`zaak_update` en
`zaak_partial_update`) MOET de URL-referentie naar het `zaaktype` gevalideerd
worden op het bestaan. Indien het ophalen van het zaaktype niet (uiteindelijk)
resulteert in een `HTTP 200` status code, MOET het ZRC antwoorden met een
`HTTP 400` foutbericht.

Met 'uiteindelijk resulteren' worden redirects (`HTTP 301`, `HTTP 302`)
antwoorden afgedekt, mits de redirect-locatie resulteert in een `HTTP 200`.

(TODO: valideren dat het inderdaad om een zaaktype resource gaat -> validatie
aanscherpen)
