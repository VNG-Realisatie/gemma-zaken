# Zaakdocumentservices 2.0 Standaard

#### Versie 0.1

## Inleiding

De ZDS 2.0 standaard beschrijft de eisen aan API's die gebruikt worden
in applicaties voor zaakgericht werken. We onderscheiden een aantal
registraties en schrijven voor hoe de API eruit ziet en functioneert.

Deze standardisatie zorgt vervolgens voor gegarandeerde interoperabiliteit
tussen registraties en consumers die van de API's gebruik maken.

## Inhoudsopgave

- [Beschikbaar stellen van API-spec](#beschikbaar-stellen-van-api-spec)
- [Definities](#definities)
- [Zaakregistratiecomponent](#zaakregistratiecomponent)
    - [OpenAPI specificatie](#openapi-specificatie)
    - [Run-time gedrag](#run-time-gedrag)
- [Documentregistratiecomponent](#documentregistratiecomponent)
    - [OpenAPI specificatie](#openapi-specificatie-1)
    - [Run-time gedrag](#run-time-gedrag-1)

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

#### Synchroniseren relaties met informatieobjecten

Wanneer een relatie tussen een `INFORMATIEOBJECT` en een ander `OBJECT` gemaakt
wordt, dan MOET het DRC in de bron van `OBJECT` ook deze relatie aanmaken.

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
        "beschrijving": "",
        "registratiedatum": "2018-09-19T17:57:08+0200"
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
