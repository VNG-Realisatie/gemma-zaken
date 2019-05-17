---
title: "ZGW API Standaard documentatie"
date: '14-11-2018'
weight: 100
---

*Versie 0.1*

## Inleiding

De ZGW API standaard beschrijft de eisen aan API's die gebruikt worden
in applicaties voor zaakgericht werken. We onderscheiden een aantal
registraties en schrijven voor hoe de API eruit ziet en functioneert.

Deze standardisatie zorgt vervolgens voor gegarandeerde interoperabiliteit
tussen registraties en consumers die van de API's gebruik maken.

## Inhoudsopgave

- [Definities](#definities)
- [Beschikbaar stellen van API-spec](#beschikbaar-stellen-van-api-spec)
- [Gegevensformaten](#gegevensformaten)
- [Autorisatie](#autorisatie)
    - [Autorisatiecomponent](#autorisatiecomponent)
- [Filter parameters](#filter-parameters)
- [Notificaties](#notificaties)
- [Zaakregistratiecomponent](#zaakregistratiecomponent)
    - [OpenAPI specificatie](#openapi-specificatie)
    - [Run-time gedrag](#run-time-gedrag)
- [Documentregistratiecomponent](#documentregistratiecomponent)
    - [OpenAPI specificatie](#openapi-specificatie-1)
    - [Run-time gedrag](#run-time-gedrag-1)
- [Besluitregistratiecomponent](#besluitregistratiecomponent)
  - [OpenAPI specificatie](#openapi-specificatie-2)
  - [Run-time gedrag](#run-time-gedrag-2)
- [Zaaktypecatalogus](#zaaktypecatalogus)
    - [OpenAPI specificatie](#openapi-specificatie-3)
    - [Run-time gedrag](#run-time-gedrag-3)

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
  communiceert via de ZGW API's.

- De codes bij business logica (zoals `zrc-001`) verwijzen naar de [Postman tests voor ZGW API's](https://github.com/VNG-Realisatie/gemma-postman-tests)

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
echter deze worden wel binnen de ZGW API's gebruikt en opgelegd.

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
server MOET aan de hand van de `client_id` key in de JWT payload
de bijhorende secret opvragen. De server MOET met het juiste shared secret
het JWT valideren tegen tampering.

Voorbeeld van een payload:

```json
{
    "iss": "voorbeeld-consumers",
    "iat": 1556898201,
    "client_id": "dsh5thqAzL6I9SC5IPgR"
}
```

Na succesvolle validatie van het JWT is nu zeker dat de consumer is wie die
beweert te zijn.

Providers MOETEN voor elke aanroep door de client controleren of de client
geautoriseerd is om deze aanroep uit te voeren.

Providers MOETEN een geconfigureerde autorisatiecomponent bevragen met het
`client_id` als query-parameter om de autorisaties van deze client op te
vragen, conform de API-specificatie van het AC.

Providers MOGEN deze gegevens cachen om performance-redenen. Indien
er van caching gebruik gemaakt wordt, dan MOETEN providers een mechanisme
inbouwen om wijzingen in het AC meteen door te voeren in de cache. Het is
AANGERADEN om hiervoor te abonneren op notificaties verstuurd door het AC.

### Autorisatiecomponent

Alle operaties beschreven in [`openapi.yaml`](../../../api-specificatie/ac/openapi.yaml)
MOETEN ondersteund worden en tot hetzelfde resultaat leiden als de
referentie-implementatie van het AC.

Het is NIET TOEGESTAAN om gebruik te maken van operaties die niet beschreven
staan in deze OAS spec, of om uitbreidingen op operaties in welke vorm dan ook
toe te voegen.

#### Run-time gedrag

De AC MAG bij de registratie van autorisaties die een of meer zaaktypen
bevatten controleren of de zaaktypen bestaan. Merk op dat hiervoor het AC
zelf geautoriseerd moet zijn om het ZTC te bevragen.

##### Uniciteit van `client_ids`

Een applicatie MAG zich met meerdere `client_id`s identificeren, waarbij er
een `client_id` per provider gebruikt wordt. Als eenmaal een `client_id` aan een
applicatie toegekend is, dan MAG dit `client_id` NIET opnieuw gebruikt worden.
Een `client_id` identifieert uniek 1 en slechts 1 applicatie.

##### Autorisatiesspecificatie

Autorisaties MOETEN gespecifieerd worden op 1 van de volgende manieren:

* opvoeren van `Autorisatie`-objecten bij een `Applicatie`, waarbij de vlag
  `heeftAlleAutorisaties` `false` is
* het zetten van de vlag `heeftAlleAutorisaties` op `true`, waarbij er GEEN
  `Autorisatie`-objecten mogen opgevoerd worden

## Filter parameters

Componenten ondersteunen het filteren van gegevens op basis van parameters in
de querystring. Deze parameters MOETEN gevalideerd worden op het juiste
formaat, net zoals inputvalidatie plaatsvindt bij een `create` of `update`.

Indien de validatie faalt, dan MOET de API antwoorden met een HTTP 400
foutbericht, waarbij de `invalid-params` key meer informatie bevat over de fout.

Indien een parameter wordt toegepast die niet in de OAS van de betreffende API
staat, dan MOET de API antwoorden met een HTTP 400 foutbericht.

## Notificaties

Componenten dienen events te publiceren naar (een)
notificatierouteringcomponent(en) (NRC). De NRC MOET volledig de
[`openapi.yaml`](../../../api-specificatie/nrc/openapi.yaml) implementeren.

Applicaties MOGEN een abonnement nemen op 1 of meer kanalen. Deze applicaties
zijn dan event consumers. Een event consumer MOET de
[API volgens `openapi.yaml`](../../../api-specificatie/nrc/consumer-api/openapi.yaml)
implementeren om berichten te kunnen ontvangen.

Componenten geven aan indien het nemen van een abonnement op bepaalde kanalen
verplicht is. Deze componenten zijn dan naast provider ook een event consumer.

### Kanalen

Elke bron, wat bij de ZGW API's één-op-éen overeen komt met een component
zoals het ZRC, DRC, BRC, etc., MOETEN hun kanaal registreren bij de NRC indien
dit nog niet bestaat. Elke bron MOET tevens documenteren op welke kanalen die
publiceert.

### Abonneren

Consumers MOGEN zich abonneren op kanalen. Een consumer MOET hiervoor een
endpoint registreren, beveiligd met een `Authorization` header. Bij het
registeren geeft de consumer een geldige header waarde mee zodat het NRC de
berichten kan afleveren.

Optioneel MAG een abonnement filters bevatten op basis van berichtkenmerken.

### Berichten en kenmerken

Bronnen MOETEN events versturen naar het NRC. Het NRC MOET deze vervolgens
bij de endpoints van abonnementen afleveren, conform de filters van het
abonnement op basis van de kenmerken.

Berichten MOETEN informatie-arm zijn, in het kader van privacy-by-design. Het
formaat van berichten is beschreven in de NRC OAS.

In de documentatie van elke bron MOET beschreven zijn welke kanalen en
kenmerken geldig zijn. Tevens MOET beschreven zijn welke gebeurtenissen tot
een notificatie leiden.

### Toekomstige ontwikkelingen

* pollen
* berichten bewaren (retentie)
* (gemiste) berichten opvragen
* abonnementen automatisch annuleren indien herhaaldelijk fout bij afleveren

## Zaakregistratiecomponent

Zaakregistratiecomponenten (ZRC) MOETEN aan twee aspecten voldoen:

* de ZRC `openapi.yaml` MOET volledig geïmplementeerd zijn

* het run-time gedrag beschreven in deze standaard MOET correct geïmplementeerd
  zijn.

### OpenAPI specificatie

Alle operaties beschreven in [`openapi.yaml`](../../../api-specificatie/zrc/openapi.yaml)
MOETEN ondersteund worden en tot hetzelfde resultaat leiden als de
referentie-implementatie van het ZRC.

Het is NIET TOEGESTAAN om gebruik te maken van operaties die niet beschreven
staan in deze OAS spec, of om uitbreidingen op operaties in welke vorm dan ook
toe te voegen.

### Run-time gedrag

Bepaalde gedrageningen kunnen niet in een OAS spec uitgedrukt worden omdat ze
businesslogica bevatten. Deze gedragingen zijn hieronder beschreven en MOETEN
zoals beschreven geïmplementeerd worden.

#### **<a name="zrc-001">Valideren `zaaktype` op de `Zaak`-resource ([zrc-001](#zrc-001))</a>**

Bij het aanmaken (`zaak_create`) en bijwerken (`zaak_update` en
`zaak_partial_update`) MOET de URL-referentie naar het `zaaktype` gevalideerd
worden op het bestaan. Indien het ophalen van het zaaktype niet (uiteindelijk)
resulteert in een `HTTP 200` status code, MOET het ZRC antwoorden met een
`HTTP 400` foutbericht.

(TODO: valideren dat het inderdaad om een zaaktype resource gaat -> validatie
aanscherpen)

#### **<a name="zrc-002">Garanderen uniciteit `bronorganisatie` en `identificatie` op de `Zaak`-resource ([zrc-002](#zrc-002))</a>**

Bij het aanmaken (`zaak_create`) en bijwerken (`zaak_update` en
`zaak_partial_update`) MOET gevalideerd worden dat de combinatie `identificatie`
en `bronorganisatie` uniek is, indien de `identificatie` door de consumer
meegestuurd wordt.

Indien de identificatie niet door de consumer gestuurd wordt, dan MOET het ZRC
de identificatie genereren op een manier die garandeert dat de identificatie
uniek is binnen de bronorganisatie.

#### **<a name="zrc-003">Valideren `informatieobject` op de `ZaakInformatieObject`-resource ([zrc-003](#zrc-003))</a>**

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

#### **<a name="zrc-004">Limiteren zaakgegevens op basis van `zaaktypes` claim ([zrc-004](#zrc-004))</a>**

De `zaaktypes` claim is een lijst van URLs van zaaktypes waar de eindgebruiker
rechten op heeft.

De server MOET resultaten van lijst-operaties (`zaak_list`, `zaak__zoek`)
limiteren tot de zaaktypes in de zaaktypesclaim.

De server MOET een HTTP 403 antwoord sturen bij detail-operaties op zaken van
een ander zaaktype dan deze in de claim (`zaak_retrieve`).

#### **<a name="zrc-005">Afsluiten zaak ([zrc-005](#zrc-005))</a>**
Een zaak wordt afgesloten door een eindstatus toe te kennen aan een `Zaak`. Elk
`ZaakType` MOET minimaal één `StatusType` kennen. De eindstatus binnen een
`ZaakType` is het `StatusType` met het hoogste `volgnummer`.

Een `Zaak` MOET een `Resultaat` hebben voor deze afgesloten kan worden.

De `Zaak.einddatum` MOET logisch afgeleid worden uit het toekennen van de
eindstatus via de `Status.datumStatusGezet`.

Als een `Zaak` een eindstatus heeft dan is de zaak afgesloten en mogen gegevens
van de zaak niet meer aangepast worden (behalve om redenen van correctie). Dit
MOET beveiligd worden met de scope `zds.scopes.zaken.geforceerd-bijwerken`.

Bij het afsluiten van een `Zaak` MOET het ZRC
`Informatieobject.indicatieGebruiksrecht` controleren van alle gerelateerde
informatieobjecten. Deze MAG NIET `null` zijn, maar MOET `true` of `false`
zijn. Indien dit niet het geval is, dan dient het ZRC een validatiefout te
genereren met code `indicatiegebruiksrecht-unset`.

#### Heropenen zaak

Bij het heropenen van een `Zaak` MOET de client een andere status toevoegen aan
de zaak dan een eindstatus. Hiervoor MOET de client de scope
`zds.scopes.zaken.heropenen` hebben.

Tevens MOET de provider de volgende velden op `null` zetten zodra een
eindstatus wordt gewijzigd in een andere status:

* `Zaak.einddatum`
* `Zaak.archiefactiedatum`
* `Zaak.archiefnominatie`

#### **<a name="zrc-006">Vertrouwelijkheidaanduiding van een zaak ([zrc-006](#zrc-006))</a>**

Indien de client een `vertrouwelijkheidaanduiding` meegeeft bij het aanmaken
of bewerken van een zaak, dan MOET de provider deze waarde toekennen. Indien
de client deze niet expliciet toekent, dan MOET deze afgeleid worden uit
`Zaak.ZaakType.vertrouwelijkheidaanduiding`.

Een `Zaak` response van de provider MOET altijd een geldige waarde voor
`vertrouwelijkheidaanduiding` bevatten. Een client MAG een waarde voor
`vertrouwelijkheidaanduiding` meesturen.

#### **<a name="zrc-007">Valideren `communicatiekanaal` op de `Zaak` resource ([zrc-007](#zrc-007))</a>**

Bij het aanmaken (`zaak_create`) en bijwerken (`zaak_update` en
`zaak_partial_update`) MOET de URL-referentie naar het `communicatiekanaal`
gevalideerd worden op het bestaan. Indien het ophalen van het zaaktype niet
(uiteindelijk) resulteert in een `HTTP 200` status code, MOET het ZRC
antwoorden met een `HTTP 400` foutbericht.

Het ophalen van deze resource moet een JSON-document zijn met de vorm van
een communicatiekanaal zoals gedocumenteerd op de
[referentielijsten-api](https://ref.tst.vng.cloud/referentielijsten/api/v1/schema/#operation/communicatiekanaal_read):

```json
{
    "url": "http://example.com",
    "naam": "string",
    "omschrijving": "string"
}
```

#### **<a name="zrc-008">Valideren `relevanteAndereZaken` op de `Zaak`-resource ([zrc-008](#zrc-008))</a>**

De lijst `relevanteAndereZaken` bevat URL-referenties naar andere zaken. Elke
URL-referentie MOET gevalideerd worden op het bestaan. Indien het ophalen van
de url niet (uiteindelijk) resulteert in een `HTTP 200` status code, MOET het ZRC
antwoorden met een `HTTP 400` foutbericht.

In het foutbericht MOET de naam binnen `invalid-params` dan
`relevanteAndereZaken.<index>` zijn, waarbij index start bij 0.

#### **<a name="zrc-009">Gegevensgroepen ([zrc-009](#zrc-009))</a>**

De client MAG gegevensgroepen zoals `Zaak.verlenging` en `Zaak.opschorting`
meesturen met een waarde `null` om aan te geven dat er geen waarde gezet is.
Dit is equivalent aan het niet-meesturen van de key in de request body.
Als de client een (genest) object meestuurt, dan MOET de provider hierop de
validatie van de gegevensgroep toepassen.

De provider MOET altijd de geneste structuur van de gegevensgroep antwoorden.

#### **<a name="zrc-010">Valideren `hoofdzaak` op de `Zaak`-resource ([zrc-010](#zrc-010))</a>**

Bij het aanmaken of bewerken van een `Zaak` kan de `hoofdzaak` aangegeven
worden. Dit MOET een geldige URL-referentie naar een `Zaak` zijn, indien
opgegeven.

Indien de client een `hoofdzaak` opgeeft die zelf een deelzaak is (i.e.
`Zaak.hoofdzaak` != `null`), dan moet het ZRC antwoorden met een `HTTP 400`
foutbericht (deelzaken van deelzaken zijn NIET toegestaan).

Indien de client een zaak bewerkt en diezelfde zaak als URL-referentie meegeeft
als `hoofdzaak`, dan moet het ZRC antwoorden met een `HTTP 400`
foutbericht (een zaak MAG GEEN deelzaak van zichzelf zijn).

#### **<a name="zrc-011">`Zaak.betalingsindicatie` en `Zaak.laatsteBetaaldatum` ([zrc-011](#zrc-011))</a>**

Indien de betalingsindicatie de waarde `"nvt"` heeft en een waarde gegeven is
voor `laatsteBetaaldatum`, dan MOET het ZRC antwoorden met een `HTTP 400`
foutbericht. Bij alle andere waarden van `betalingsindicatie` MAG een waarde
opgegeven worden voor `laatsteBetaaldatum`.

Indien een waarde ingevuld is voor `laatsteBetaaldatum` en de betalingsindicatie
wordt gewijzigd naar `"nvt"`, dan MOET de `laatsteBetaaldatum` op `null` gezet
worden.

#### **<a name="zrc-012">Valideren van producten en/of diensten bij een `Zaak` ([zrc-012](#zrc-012))</a>**

Bij het aanmaken (`zaak_create`) en bijwerken (`zaak_update` en
`zaak_partial_update`) MOET de collectie `productenOfDiensten` worden getoetst
tegen het `Zaaktype.productenOfDiensten` van het betreffende zaaktype. De
producten en/of diensten van de zaak MOETEN een subset van de producten en/of
diensten op het zaaktype zijn.

#### Archiveren

**<a name="zrc-013">Afleiden van archiveringsparameters ([zrc-013](#zrc-013))</a>**

Het resultaat van een zaak is bepalend voor het archiefregime. Bij het
afsluiten van een zaak MOETEN de attributen `Zaak.archiefnominatie`
en `Zaak.archiefactiedatum` bepaald worden uit het `Zaak.Resultaat` als volgt:

1. Indien de zaak geen `archiefnominatie` heeft, dan MOET deze overgenomen
   worden uit `Resultaat.Resultaattype.archiefnominatie`
2. Indien `Resultaat.Resultaattype.archiefactietermijn` gevuld is:
    1. Bepaal de `brondatum` van de archiefprocedure
        1. Consulteer het groepattribuut `Resultaat.Resultaattype.brondatumArchiefprocedure`
        2. Afhankelijk van de waarde van `afleidingswijze`:
            * `afgehandeld` -> gebruik `Zaak.einddatum`
            * `hoofdzaak` -> gebruik `Zaak.hoofdzaak.einddatum`
            * `eigenschap` -> gebruik de waarde van de eigenschap met als naam
              de waarde van
              `Resultaat.Resultaattype.brondatumArchiefprocedure.datumkenmerk`
            * `ander_datumkenmerk` -> brondatum MOET handmatig afgeleid en
              gezet worden
            * `zaakobject` -> zoek de gerelateerde objecten van type
              `Resultaat.Resultaattype.brondatumArchiefprocedure.objecttype`.
              Lees van elk object het attribuut met de naam
              `Resultaat.Resultaattype.brondatumArchiefprocedure.datumkenmerk`
              en gebruik de maximale waarde.
            * `termijn` -> `Zaak.einddatum` + `Resultaat.Resultaattype.brondatumArchiefprocedure.procestermijn`
            * `gerelateerde_zaak` -> TODO
            * `ingangsdatum_besluit` -> maximale `Besluit.ingangsdatum` van alle
              gerelateerde besluiten
            * `vervaldatum_besluit` -> maximale `Besluit.vervaldatum` van alle
              gerelateerde besluiten
    2. Zet `Zaak.archiefactiedatum` als `brondatum + Resultaat.Resultaattype.archiefactietermijn`

Indien de archiefactiedatum niet bepaald kan worden, dan MAG er geen datum
gezet worden. Dit kan voorkomen als de brondatum niet bepaald kan worden of
de archiefactietermijn niet beschikbaar is.

**<a name="zrc-014">Zetten `Zaak.archiefstatus` ([zrc-014](#zrc-014))</a>**

De standaardwaarde voor archiefstatus is `nog_te_archiveren`. Indien een andere
waarde gezet wordt, dan MOETEN alle gerelateerde informatieobjecten de status
`gearchiveerd` hebben.

De attributen `Zaak.archiefnominatie` en `Zaak.archiefactiedatum` MOETEN een
waarde krijgen als de de archiefstatus een waarde krijgt anders dan
`nog_te_archiveren`.

Indien deze voorwaarden niet voldaan zijn, dan MOET het ZRC met een `HTTP 400`
foutbericht antwoorden.

**<a name="zrc-015">Vernietigen van zaken ([zrc-015](#zrc-015))</a>**

Bij `DELETE` requests op zaken MOETEN de zaak en gerelateerde objecten fysiek
uit de opslag verwijderd worden. Soft-deletes zijn NIET TOEGESTAAN. Onder
gerelateerde objecten wordt begrepen:

- `zaak` - de deelzaken van de verwijderde hoofzaak
- `status` - alle statussen van de verwijderde zaak
- `resultaat` - het resultaat van de verwijderde zaak
- `rol` - alle rollen bij de zaak
- `zaakobject` - alle zaakobjecten bij de zaak
- `zaakeigenschap` - alle eigenschappen van de zaak
- `zaakkenmerk` - alle kenmerken van de zaak
- `zaakinformatieobject` - dit moet door-cascaden naar DRCs, zie ook
  https://github.com/VNG-Realisatie/gemma-zaken/issues/791 (TODO)
- `klantcontact` - alle klantcontacten bij een zaak

Een deelzaak KAN vernietigd worden zonder dat de hoofdzaak vernietigd wordt.

#### Data filteren bij de bron

Het autorisatiecomponent (AC) legt op het niveau van `zaaktype` vast welke
operaties mogelijk en wat de maximale vertrouwelijkheidaanduiding is voor een
consumer.

Het ZRC MAG ENKEL zaken ontsluiten waarvan:

* het zaaktype voorkomt in de autorisaties van de consumer
* de vertrouwelijkheidaanduiding lager of gelijk aan de maximale
  vertrouwelijkheidaanduiding is voor het betreffende zaaktype

De API-specificatie legt vast welke scopes nodig zijn voor welke operaties.
Een provider MOET operaties blokkeren op zaken waarvan de nodige scopes niet
toegekend zijn voor het zaaktype van de betreffende zaak.

Indien een operatie niet toegelaten is, dan MOET de provider met een
`HTTP 403` foutbericht antwoorden.

Een consumer is verbonden aan het concept `Applicatie`, waarop `autorisaties`
gedefinieerd worden. Het is mogelijk om op het niveau van `Applicatie` de vlag
`heeftAlleAutorisaties` te zetten. Indien deze gezet is, dan MOET de provider
alle operaties voor deze consumer toelaten, op alle zaken.

## Documentregistratiecomponent

documentregistratiecomponentsen (DRC) MOETEN aan twee aspecten voldoen:

* de DRC `openapi.yaml` MOET volledig geïmplementeerd zijn

* het run-time gedrag beschreven in deze standaard MOET correct geïmplementeerd
  zijn.

### OpenAPI specificatie

Alle operaties beschreven in [`openapi.yaml`](../../../api-specificatie/drc/openapi.yaml)
MOETEN ondersteund worden en tot hetzelfde resultaat leiden als de referentie-
implementatie van het DRC.

Het is NIET TOEGESTAAN om gebruik te maken van operaties die niet beschreven
staan in deze OAS spec, of om uitbreidingen op operaties in welke vorm dan ook
toe te voegen.

### Run-time gedrag

Bepaalde gedrageningen kunnen niet in een OAS spec uitgedrukt worden omdat ze
businesslogica bevatten. Deze gedragingen zijn hieronder beschreven en MOETEN
zoals beschreven geïmplementeerd worden.

#### **<a name="drc-001">Valideren `informatieobjecttype` op de `EnkelvoudigInformatieObject`-resource ([drc-001](#drc-001))</a>**

Bij het aanmaken (`enkelvoudiginformatieobject_create`) MOET de URL-referentie
naar het `informatieobjecttype` gevalideerd worden op het bestaan. Indien het
ophalen van het informatieobjecttype niet (uiteindelijk) resulteert in een
`HTTP 200` status code, MOET het DRC antwoorden met een `HTTP 400` foutbericht.

(TODO: valideren dat het inderdaad om een informatieobjecttype resource gaat
-> validatie aanscherpen)

#### **<a name="drc-002">Valideren `object` op de `ObjectInformatieObject`-resource ([drc-002](#drc-002))</a>**

Bij het aanmaken (`objectinformatieobject_create`) MOET de URL-referentie
naar het `object` gevalideerd worden op het bestaan. Indien het ophalen van het
object niet (uiteindelijk) resulteert in een `HTTP 200` status code, MOET het
DRC antwoorden met een `HTTP 400` foutbericht.

Er MOET gevalideerd worden dat de combinatie `object` en `informatieobject`
niet eerder voorkomt. Indien deze al bestaat, dan MOET het DRC antwoorden met
een `HTTP 400` foutbericht.

(TODO: valideren dat het van het type `object_type` is -> validatie aanscherpen)

#### **<a name="drc-003">Valideren relatieinformatie op `ObjectInformatieObject`-resource ([drc-003](#drc-003))</a>**

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

#### **<a name="drc-004">Synchroniseren relaties met informatieobjecten ([drc-004](#drc-004))</a>**

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

Een voorbeeld met een object van het type `Zaak`:

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

#### **<a name="drc-005">Statuswijzigingen van informatieobjecten ([drc-005](#drc-005))</a>**

Wanneer `InformatieObject.verzenddatum` een waarde heeft, dan zijn de waarden
`in bewerking` en `ter vaststelling` voor `InformatieObject.status` NIET
TOEGELATEN. Indien een dergelijke status gezet is _voor_ de verzenddatum opgegeven
wordt, dan moet de API een HTTP 400 foutbericht geven met `status` als veld in
de `invalid-params`. De client MOET dan `verzenddatum` leeg laten of eerst de
status wijzingen.

#### **<a name="drc-006">Gebruiksrechten op informatieobjecten ([drc-006](#drc-006))</a>**

Indien er geen gebruiksrechtenvoorwaarden van toepassing zijn op een
informatieobject, dan moet `InformatieObject.indicatieGebruiksrechten` op de
waarde `false` gezet worden. Indien de voorwaarden (nog) niet bekend zijn,
dan moet de indicatie op `null` gezet worden.

Om de indicatie op `true` te zetten, MOET je de resource `Gebruiksrechten`
aanmaken in de API. Providers MOETEN bij het aanmaken van gebruiksrechten
voor een informatieobject de `indicatieGebruiksrechten` van dat informatieobject
op `true` zetten.

Indien de laatste gebruiksrechten op een informatieobject verwijderd worden,
dan MOET de indicatie weer op `null` gezet worden.

#### **<a name="drc-007">Vertrouwelijkheidaanduiding van een informatieobject ([drc-007](#drc-007))</a>**

Indien de client een `vertrouwelijkheidaanduiding` meegeeft bij het aanmaken
of bewerken van een informatieobject, dan MOET de provider deze waarde
toekennen. Indien de client deze niet expliciet toekent, dan MOET deze afgeleid
worden uit `InformatieOject.InformatieObjectType.vertrouwelijkheidaanduiding`.

Een `InformatieOject` response van de provider MOET altijd een geldige waarde
voor `vertrouwelijkheidaanduiding` bevatten. Een client MAG een waarde voor
`vertrouwelijkheidaanduiding` meesturen.


## Besluitregistratiecomponent

Besluitregistratiecomponenten (BRC) MOETEN aan twee aspecten voldoen:

* de BRC `openapi.yaml` MOET volledig geïmplementeerd zijn

* het run-time gedrag beschreven in deze standaard MOET correct geïmplementeerd
  zijn.

### OpenAPI specificatie

Alle operaties beschreven in [`openapi.yaml`](../../../api-specificatie/brc/openapi.yaml)
MOETEN ondersteund worden en tot hetzelfde resultaat leiden als de
referentie-implementatie van het BRC.

Het is NIET TOEGESTAAN om gebruik te maken van operaties die niet beschreven
staan in deze OAS spec, of om uitbreidingen op operaties in welke vorm dan ook
toe te voegen.

### Run-time gedrag

Bepaalde gedrageningen kunnen niet in een OAS spec uitgedrukt worden omdat ze
businesslogica bevatten. Deze gedragingen zijn hieronder beschreven en MOETEN
zoals beschreven geïmplementeerd worden.

#### **<a name="brc-001">Valideren `besluittype` op de `Besluit`-resource ([brc-001](#brc-001))</a>**

Bij het aanmaken (`besluit_create`) en bijwerken (`besluit_update` en
`besluit_partial_update`) MOET de URL-referentie naar het `besluittype` gevalideerd
worden op het bestaan. Indien het ophalen van het besluittype niet (uiteindelijk)
resulteert in een `HTTP 200` status code, MOET het BRC antwoorden met een
`HTTP 400` foutbericht.

(TODO: valideren dat het inderdaad om een besluittype resource gaat -> validatie
aanscherpen)

#### **<a name="brc-002">Garanderen uniciteit `verantwoordelijke_organisatie` en `identificatie` op de `Besluit`-resource ([brc-002](#brc-002))</a>**

Bij het aanmaken (`besluit_create`) MOET gevalideerd worden dat de combinatie
`identificatie` en `verantwoordelijke_organisatie` uniek is, indien de
`identificatie` door de consumer meegestuurd wordt.

Indien de identificatie niet door de consumer gestuurd wordt, dan MOET het BRC
de identificatie genereren op een manier die garandeert dat de identificatie
uniek is binnen de verantwoordelijke_organisatie.

Bij het bijwerken (`besluit_update` en `besluit_partial_update`) is het NIET
TOEGESTAAN om `identificatie` en `verantwoordelijke_organisatie` te wijzingen.

#### **<a name="brc-003">Valideren `informatieobject` op de `BesluitInformatieObject`-resource ([brc-003](#brc-003))</a>**

Bij het aanmaken (`besluitinformatieobject_create`) MOET de URL-referentie naar
het `informatieobject` gevalideerd worden op het bestaan. Indien het ophalen
van het informatieobject niet (uiteindelijk) resulteert in een `HTTP 200`
status code, MOET het BRC antwoorden met een `HTTP 400` foutbericht.

Er MOET gevalideerd worden dat de combinatie `besluit` en `informatieobject`
niet eerder voorkomt. Indien deze al bestaat, dan MOET het BRC antwoorden met
een `HTTP 400` foutbericht.

## Zaaktypecatalogus

Zaaktypecatalogi (ZTC) MOETEN aan twee aspecten voldoen:

* de ZTC `openapi.yaml` MOET volledig geïmplementeerd zijn

* het run-time gedrag beschreven in deze standaard MOET correct geïmplementeerd
  zijn.

Het ZTC haalt informatie uit selectielijsten en de Gemeentelijke Selectielijst
2017. Deze gegevens worden ontsloten in de
[VNG-referentielijsten-API](https://ref.tst.vng.cloud/referentielijsten/). Op
korte termijn zal deze API gesplitst worden in een referentielijsten-API en de
selectielijst-API (waar deze nu nog 1 API is)
[#3 on Github](https://github.com/VNG-Realisatie/VNG-referentielijsten/issues/3).

### OpenAPI specificatie

Alle operaties beschreven in [`openapi.yaml`](../../../api-specificatie/ztc/openapi.yaml)
MOETEN ondersteund worden en tot hetzelfde resultaat leiden als de
referentie-implementatie van het ZTC.

Het is NIET TOEGESTAAN om gebruik te maken van operaties die niet beschreven
staan in deze OAS spec, of om uitbreidingen op operaties in welke vorm dan ook
toe te voegen.

### Run-time gedrag

Bepaalde gedrageningen kunnen niet in een OAS spec uitgedrukt worden omdat ze
businesslogica bevatten. Deze gedragingen zijn hieronder beschreven en MOETEN
zoals beschreven geïmplementeerd worden.

#### **<a name="ztc-001">Valideren van `Zaaktype` ([ztc-001](#ztc-001))</a>**

Het attribuut `Zaaktype.selectielijstProcestype` MOET een URL-verwijzing naar
de `Procestype` resource in de selectielijst-API zijn, indien ingevuld.

#### **<a name="ztc-002">Valideren van `Resultaattype` ([ztc-002](#ztc-002))</a>**

Het attribuut `Resultaattype.resultaattypeomschrijving` MOET een URL-verwijzing
naar de `Resultaattypeomschrijving` resource in de referentielijsten-API zijn.
Het ZTC MOET de waarde van `Resultaattypeomschrijving.omschrijving` ontsluiten
(uit de selectielijst) als alleen-lezen attribuut
`Resultaattype.omschrijvingGeneriek`.

Het attribuut `Resultaattype.selectielijstklasse` MOET een URL-verwijzing zijn
naar de `Resultaat` resource in de selectielijst-API. Tevens MOET dit
`resultaat` horen bij het `procestype` geconfigureerd op
`Resultaattype.zaaktype.selectielijstProcestype`.

Indien `Resultaattype.archiefnominatie` niet expliciet opgegeven wordt, dan
MOET het ZTC deze afleiden uit `Resultaat.waardering` van de
selectielijstklasse.

Indien `Resultaattype.archiefactietermijn` niet expliciet opgegeven wordt, dan
MOET het ZTC deze afleiding uit `Resultaat.bewaartermijn` van de
selectielijstklasse.

**`Resultaattype.brondatumArchiefprocedure`**

Het groepattribuut `Resultaattype.brondatumArchiefprocedure` parametriseert
het bepalen van de `brondatum` voor de `archiefactietermijn` van een zaak. Deze
parametrisering is aan validatieregels onderhevig:

* `Resultaattype.brondatumArchiefprocedure.afleidingswijze`:
    * afleidingswijze MOET `afgehandeld` zijn indien de selectielijstklasse
      als procestermijn `nihil` heeft en vice versa
    * afleidingswijze MOET `termijn` zijn indien de selectielijstklasse
      als procestermijn `ingeschatte_bestaansduur_procesobject` heeft en vice
      versa

* `Resultaattype.brondatumArchiefprocedure.datumkenmerk`
    * MOET een waarde hebben als de afleidingswijze `eigenschap`, `zaakobject`
      of `ander_datumkenmerk` is
    * MAG GEEN waarde hebben in de andere gevallen

* `Resultaattype.brondatumArchiefprocedure.einddatumBekend`
    * MAG GEEN waarde hebben indien de afleidingswijze `afgehandeld` of
      `termijn` is

* `Resultaattype.brondatumArchiefprocedure.objecttype`
    * MOET een waarde hebben als de afleidingswijze `zaakobject`
      of `ander_datumkenmerk` is
    * MAG GEEN waarde hebben in de andere gevallen

* `Resultaattype.brondatumArchiefprocedure.registratie`
    * MOET een waarde hebben indien de afleidingswijze `ander_datumkenmerk` is
    * MAG GEEN waarde hebben in de andere gevallen

* `Resultaattype.brondatumArchiefprocedure.procestermijn`
    * MOET een waarde hebben indien de afleidingswijze `termijn` is
    * MAG GEEN waarde hebben in de andere gevallen
