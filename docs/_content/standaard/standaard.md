---
title: "ZGW API Standaard documentatie"
date: '14-11-2018'
weight: 100
---

*Versie 0.1*

## Inleiding

De ZDS 2.0 standaard beschrijft de eisen aan API's die gebruikt worden
in applicaties voor zaakgericht werken. We onderscheiden een aantal
registraties en schrijven voor hoe de API eruit ziet en functioneert.

Deze standardisatie zorgt vervolgens voor gegarandeerde interoperabiliteit
tussen registraties en consumers die van de API's gebruik maken.

## Inhoudsopgave

- [Definities](#definities)
- [Beschikbaar stellen van API-spec](#beschikbaar-stellen-van-api-spec)
- [Gegevensformaten](#gegevensformaten)
- [Autorisatie](#autorisatie)
- [Filter parameters](#filter-parameters)
- [Zaakregistratiecomponent](#zaakregistratiecomponent)
    - [OpenAPI specificatie](#openapi-specificatie)
    - [Run-time gedrag](#run-time-gedrag)
- [Documentregistratiecomponent](#documentregistratiecomponent)
    - [OpenAPI specificatie](#openapi-specificatie-1)
    - [Run-time gedrag](#run-time-gedrag-1)
- [Besluitregistratiecomponent](#besluitregistratiecomponent)
  - [OpenAPI specificatie](#openapi-specificatie-2)
  - [Run-time gedrag](#run-time-gedrag-2)

## Definities

- OAS schema: een API definitie die de
  [OpenAPI-Specification](https://github.com/OAI/OpenAPI-Specification) volgt.
  **vng-Realisatie** publiceert de schema's waaraan implementaties moeten voldoen
  op [github](https://github.com/VNG-Realisatie/gemma-zaken/tree/master/api-specificatie).

- Consumer: een technologie die van de API's gebruik maakt. Dit kan een
  taakapplicatie zijn, een andere service in service-naar-service communicatie,
  of eender welke (generieke) client-applicatie.

- 'Uiteindelijk resulteren' betekent dat redirects (`HTTP 301`, `HTTP 302`)
  toegestaan zijn, mits deze redirect-locatie resulteert in een `HTTP 200`.

- Autorisatie: het mechanisme om wel of niet toegang te verlenen tot operaties
  en/of gegevens in de APIs. Niet te verwarren met authenticatie.

- Authenticatie: het mechanisme om de identiteit van een een persoon of andere
  entiteit vast te stellen.

- Eindgebruiker: de persoon die gebruik maakt van een (taak)applicatie die
  communiceert via de ZDS APIs.

## Beschikbaar stellen van API-spec

Iedere component MOET het OAS schema serveren, onder
`{APIROOT}/schema/openapi.yaml`.

Voorbeelden van geldige URLs:

- `https://ref.tst.vng.cloud/zrc/api/v1/schema/openapi.yaml`
- `https://zrc.nl/api/v1/schema/openapi.yaml`
- `https://api.zrc.nl/v1/schema/openapi.yaml`
- `https://v1.api.zrc.nl/schema/openapi.yaml`

De service-naar-service communicatie MOET het schema opvragen om operaties op
resources uit te voeren.

## Gegevensformaten

Een aantal formaten zijn nog niet formeel vastgelegd in OAS of JSON-Schema,
echter deze worden wel binnen de ZDS APIs gebruikt en opgelegd.

### Duur

Een duur (EN: duration) MOET in [ISO-8601 durations](https://en.wikipedia.org/wiki/ISO_8601#Durations)
uitgedrukt worden.

## Autorisatie

De API-endpoints vereisen autorisatie, in de minimale vorm met scopes. Deze
scopes zijn opgenomen in de OAS spec.

API requests van clients MOETEN een
[JSON Web Token (JWT)](https://tools.ietf.org/html/rfc7519) versturen naar de
API. Dit token MOET in de `Authorization` HTTP header opgenomen worden, met
als type `Bearer`. Voorbeeld:

```
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImNsaWVudF9pZGVudGlmaWVyIjoiZG9jcy1VNW9hSGhmMUEyVFgifQ.eyJpc3MiOiJkb2NzLVU1b2FIaGYxQTJUWCIsImlhdCI6MTU0MzI0NjkwNywiemRzIjp7InNjb3BlcyI6W10sInphYWt0eXBlcyI6W119fQ.e9Khey44Tgobqu8boB_GclDQ8Et7I3DhbPmTTrIu9U4
```

Client en server maken gebruik van `shared secret` om het JWT te signen, met
het HMAC SHA-256 algoritme. Iedere client MAG een eigen secret hebben. De
server MOET aan de hand van de `client_identifier` key in de JWT header
de bijhorende secret opvragen. De server MOET met het juiste shared secret
het JWT valideren tegen tampering.

De ZDS claims in de JWT-payload worden genamespaced onder `zds`.

De claims bevatten de scopes als lijst van strings, waarbij de `scopes` key
gebruikt wordt.

De `zaaktypes` claim MOET gebruikt worden om zaakgegevens te limiteren. Indien
deze claim ontbreekt, `null` is of een lege lijst, dan is het VERBODEN om
zaakgegevens te ontsluiten. Een speciale waarde van `['*']` drukt uit dat alle
zaaktypes toegestaan zijn.

Voorbeeld van een payload:

```json
{
    "zds": {
        "scopes": [
            "zds.scopes.zaken.aanmaken"
        ],
        "zaaktypes": [
            "https://haarlem.ztc.nl/api/v1/zaaktypen/123",
            "https://haarlem.ztc.nl/api/v1/zaaktypen/124",
        ]
    }
}
```

## Filter parameters

Componenten ondersteunen het filteren van gegevens op basis van parameters in
de querystring. Deze parameters MOETEN gevalideerd worden op het juiste
formaat, net zoals inputvalidatie plaatsvindt bij een `create` of `update`.

Indien de validatie faalt, dan MOET de API antwoorden met een HTTP 400
foutbericht, waarbij de `invalid-params` key meer informatie bevat over de fout.

Indien een parameter wordt toegepast die niet in de OAS van de betreffende API
staat, dan MOET de API antwoorden met een HTTP 400 foutbericht.

## Zaakregistratiecomponent

Zaakregistratiecomponenten (ZRC) MOETEN aan twee aspecten voldoen:

* de ZRC `openapi.yaml` MOET volledig geïmplementeerd zijn

* het run-time gedrag beschreven in deze standaard MOET correct geïmplementeerd
  zijn.

### OpenAPI specificatie

Alle operaties beschreven in [`openapi.yaml`](./api-specificatie/zrc/openapi.yaml)
MOETEN ondersteund worden en tot hetzelfde resultaat leiden als de
referentie-implementatie van het ZRC.

Het is NIET TOEGESTAAN om gebruik te maken van operaties die niet beschreven
staan in deze OAS spec, of om uitbreidingen op operaties in welke vorm dan ook
toe te voegen.

### Run-time gedrag

Bepaalde gedrageningen kunnen niet in een OAS spec uitgedrukt worden omdat ze
businesslogica bevatten. Deze gedragingen zijn hieronder beschreven en MOETEN
zoals beschreven geïmplementeerd worden.

#### Valideren `zaaktype` op de `Zaak`-resource

Bij het aanmaken (`zaak_create`) en bijwerken (`zaak_update` en
`zaak_partial_update`) MOET de URL-referentie naar het `zaaktype` gevalideerd
worden op het bestaan. Indien het ophalen van het zaaktype niet (uiteindelijk)
resulteert in een `HTTP 200` status code, MOET het ZRC antwoorden met een
`HTTP 400` foutbericht.

(TODO: valideren dat het inderdaad om een zaaktype resource gaat -> validatie
aanscherpen)

#### Garanderen uniciteit `bronorganisatie` en `identificatie` op de `Zaak`-resource

Bij het aanmaken (`zaak_create`) en bijwerken (`zaak_update` en
`zaak_partial_update`) MOET gevalideerd worden dat de combiantie `identificatie`
en `bronorganisatie` uniek is, indien de `identificatie` door de consumer
meegestuurd wordt.

Indien de identificatie niet door de consumer gestuurd wordt, dan MOET het ZRC
de identificatie genereren op een manier die garandeert dat de identificatie
uniek is binnen de bronorganisatie.

#### Valideren `informatieobject` op de `ZaakInformatieObject`-resource

Bij het aanmaken (`zaakinformatieobject_create`) MOET de URL-referentie naar
het `informatieobject` gevalideerd worden op het bestaan. Indien het ophalen
van het informatieobject niet (uiteindelijk) resulteert in een `HTTP 200`
status code, MOET het ZRC antwoorden met een `HTTP 400` foutbericht.

Er MOET gevalideerd worden dat de combinatie `zaak` en `informatieobject`
niet eerder voorkomt. Indien deze al bestaat, dan MOET het ZRC antwoorden met
een `HTTP 400` foutbericht.

Er MOET gevalideerd worden dat de relatie tussen het informatieobject en de
zaak al bestaat in het DRC. De bron van het informatieobject is bekend door
de eerdere validaties op deze URL. De API-spec van het DRC voorziet in query-
parameters om het bestaan te kunnen valideren.

#### Limiteren zaakgegevens op basis van `zaaktypes` claim

De `zaaktypes` claim is een lijst van URLs van zaaktypes waar de eindgebruiker
rechten op heeft.

De server MOET resultaten van lijst-operaties (`zaak_list`, `zaak__zoek`)
limiteren tot de zaaktypes in de zaaktypesclaim.

De server MOET een HTTP 403 antwoord sturen bij detail-operaties op zaken van
een ander zaaktype dan deze in de claim (`zaak_retrieve`).

#### Afsluiten van zaken

Een zaak wordt afgesloten door een eindstatus toe te kennen aan een `ZAAK`. Het
ZRC MOET bij het zetten van de eindstatus het datumfragment van
`datumStatusGezet` gebruiken als `ZAAK.einddatum`.

Indien een status anders dan de eindstatus gezet wordt, dan MOET het ZRC voor
het attribuut `ZAAK.einddatum` de waarde `null` bevatten.

## Documentregistratiecomponent

documentregistratiecomponentsen (DRC) MOETEN aan twee aspecten voldoen:

* de DRC `openapi.yaml` MOET volledig geïmplementeerd zijn

* het run-time gedrag beschreven in deze standaard MOET correct geïmplementeerd
  zijn.

### OpenAPI specificatie

Alle operaties beschreven in [`openapi.yaml`](./api-specificatie/drc/openapi.yaml)
MOETEN ondersteund worden en tot hetzelfde resultaat leiden als de referentie-
implementatie van het DRC.

Het is NIET TOEGESTAAN om gebruik te maken van operaties die niet beschreven
staan in deze OAS spec, of om uitbreidingen op operaties in welke vorm dan ook
toe te voegen.

### Run-time gedrag

Bepaalde gedrageningen kunnen niet in een OAS spec uitgedrukt worden omdat ze
businesslogica bevatten. Deze gedragingen zijn hieronder beschreven en MOETEN
zoals beschreven geïmplementeerd worden.

#### Valideren `informatieobjecttype` op de `EnkelvoudigInformatieObject`-resource

Bij het aanmaken (`enkelvoudiginformatieobject_create`) MOET de URL-referentie
naar het `informatieobjecttype` gevalideerd worden op het bestaan. Indien het
ophalen van het informatieobjecttype niet (uiteindelijk) resulteert in een
`HTTP 200` status code, MOET het DRC antwoorden met een `HTTP 400` foutbericht.

(TODO: valideren dat het inderdaad om een informatieobjecttype resource gaat
-> validatie aanscherpen)

#### Valideren `object` op de `ObjectInformatieObject`-resource

Bij het aanmaken (`objectinformatieobject_create`) MOET de URL-referentie
naar het `object` gevalideerd worden op het bestaan. Indien het ophalen van het
object niet (uiteindelijk) resulteert in een `HTTP 200` status code, MOET het
DRC antwoorden met een `HTTP 400` foutbericht.

Er MOET gevalideerd worden dat de combinatie `object` en `informatieobject`
niet eerder voorkomt. Indien deze al bestaat, dan MOET het DRC antwoorden met
een `HTTP 400` foutbericht.

(TODO: valideren dat het van het type `object_type` is -> validatie aanscherpen)

#### Valideren relatieinformatie op `ObjectInformatieObject`-resource

Op basis van het `objectType` MOET de `aardRelatie` gezet worden conform het
RGBZ. Dit betekent:

* `aardRelatie` is `"hoort_bij"`, indien `objectType`:
    * `zaak`

* `aardRelatie` is `"legt_vast"`, indien `objectType`:
    * `besluit`

De resource bevat de velden `titel`, `beschrijving` en `registratiedatum`. Deze
velden zijn enkel van toepassing op `aardRelatie` `"hoort_bij"` en MOETEN
genegeerd worden bij `aardRelatie` `"legt_vast"`.

De `registratiedatum` MOET door het systeem gezet worden op het moment van
aanmaken.

Bij het updaten (`objectinformatieobject_update` en
`objectinformatieobject_partial_update`) is het NIET TOEGESTAAN om de relatie
te wijzingen. Bij andere waardes voor de attributen `object`, `objectType` en
`informatieobject` MOET het DRC antwoorden met een `HTTP 400` foutbericht.

#### Synchroniseren relaties met informatieobjecten

Wanneer een relatie tussen een `INFORMATIEOBJECT` en een ander `OBJECT` gemaakt
of bijgewerkt wordt, dan MOET het DRC in de bron van `OBJECT` ook deze relatie
aanmaken/bijwerken.

`OBJECT` is van `OBJECTTYPE`. `OBJECTTYPE` bepaalt de naam van de
relatieresource in de bron van `OBJECT`, zijnde `{objecttype}informatieobject`.
De resource is volledig in kleine letters. De relatieresource moet als geneste
resource ontsloten worden van `OBJECT`.

De relatieresource MAG NIET meer velden ontsluiten dan het veld
`informatieobject`, en de waarde MOET de canonical URL zijn van de
informatieobjectresource.

Een voorbeeld met een object van het type `ZAAK`:

1. Een informatieobject wordt gerelateerd aan een zaak door een consumer:

    ```http
    POST https://drc.nl/api/v1/objectinformatieobjecten

    {
        "informatieobject": "https://drc.nl/api/v1/enkelvoudigeinformatieobjecten/1234",
        "object": "https://zrc.nl/api/v1/zaken/456789",
        "objectType": "zaak",
        "titel": "",
        "beschrijving": ""
    }
    ```

2. Het DRC MOET de relatie spiegelen in het ZRC:

    ```http
    POST https://zrc.nl/api/v1/zaken/456789/zaakinformatieobjecten

    {
       "informatieobject": "https://drc.nl/api/v1/enkelvoudigeinformatieobjecten/1234",
    }
    ```

Merk op dat het aanmaken van de relatie niet gelimiteerd is tot het aanmaken
via de API. Indien elders (bijvoorbeeld een admininterface) een relatie tot
stand kan komen, dan MOET deze ook gesynchroniseerd worden.

## Besluitregistratiecomponent

Besluitregistratiecomponenten (BRC) MOETEN aan twee aspecten voldoen:

* de BRC `openapi.yaml` MOET volledig geïmplementeerd zijn

* het run-time gedrag beschreven in deze standaard MOET correct geïmplementeerd
  zijn.

### OpenAPI specificatie

Alle operaties beschreven in [`openapi.yaml`](./api-specificatie/brc/openapi.yaml)
MOETEN ondersteund worden en tot hetzelfde resultaat leiden als de
referentie-implementatie van het BRC.

Het is NIET TOEGESTAAN om gebruik te maken van operaties die niet beschreven
staan in deze OAS spec, of om uitbreidingen op operaties in welke vorm dan ook
toe te voegen.

### Run-time gedrag

Bepaalde gedrageningen kunnen niet in een OAS spec uitgedrukt worden omdat ze
businesslogica bevatten. Deze gedragingen zijn hieronder beschreven en MOETEN
zoals beschreven geïmplementeerd worden.

#### Valideren `besluittype` op de `Besluit`-resource

Bij het aanmaken (`besluit_create`) en bijwerken (`besluit_update` en
`besluit_partial_update`) MOET de URL-referentie naar het `besluittype` gevalideerd
worden op het bestaan. Indien het ophalen van het besluittype niet (uiteindelijk)
resulteert in een `HTTP 200` status code, MOET het BRC antwoorden met een
`HTTP 400` foutbericht.

(TODO: valideren dat het inderdaad om een besluittype resource gaat -> validatie
aanscherpen)

#### Garanderen uniciteit `verantwoordelijke_organisatie` en `identificatie` op de `Besluit`-resource

Bij het aanmaken (`besluit_create`) MOET gevalideerd worden dat de combinatie
`identificatie` en `verantwoordelijke_organisatie` uniek is, indien de
`identificatie` door de consumer meegestuurd wordt.

Indien de identificatie niet door de consumer gestuurd wordt, dan MOET het BRC
de identificatie genereren op een manier die garandeert dat de identificatie
uniek is binnen de verantwoordelijke_organisatie.

Bij het bijwerken (`besluit_update` en `besluit_partial_update`) is het NIET
TOEGESTAAN om `identificatie` en `verantwoordelijke_organisatie` te wijzingen.

#### Valideren `informatieobject` op de `BesluitInformatieObject`-resource

Bij het aanmaken (`besluitinformatieobject_create`) MOET de URL-referentie naar
het `informatieobject` gevalideerd worden op het bestaan. Indien het ophalen
van het informatieobject niet (uiteindelijk) resulteert in een `HTTP 200`
status code, MOET het BRC antwoorden met een `HTTP 400` foutbericht.

Er MOET gevalideerd worden dat de combinatie `besluit` en `informatieobject`
niet eerder voorkomt. Indien deze al bestaat, dan MOET het BRC antwoorden met
een `HTTP 400` foutbericht.
