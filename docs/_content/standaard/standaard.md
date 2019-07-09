---
title: "ZGW API Standaard documentatie"
date: '27-06-2019'
weight: 100
---

## Inhoudsopgave

- [Inleiding](#inleiding)
  - [Definities](#definities)
- [Algemene API-eisen](#algemene-api-eisen)
  - [Versionering van de API](#versionering-van-de-api)
  - [Beschikbaar stellen van de OAS](#beschikbaar-stellen-van-de-oas)
- [Gegevensformaten](#gegevensformaten)
- [Autorisatie](#autorisatie)
    - [Autorisatiecomponent](#autorisatiecomponent)
- [Filter parameters](#filter-parameters)
- [Notificaties](#notificaties)
- [Audittrail](#audittrail)
- [Zaakregistratiecomponent](#zaakregistratiecomponent)
    - [OpenAPI specificatie](#openapi-specificatie)
    - [Run-time gedrag](#run-time-gedrag)
- [Documentregistratiecomponent](#documentregistratiecomponent)
    - [OpenAPI specificatie](#openapi-specificatie-1)
    - [Run-time gedrag](#run-time-gedrag-1)
- [Besluitregistratiecomponent](#besluitregistratiecomponent)
    - [OpenAPI specificatie](#openapi-specificatie-2)
   -  [Run-time gedrag](#run-time-gedrag-2)
- [Zaaktypecatalogus](#zaaktypecatalogus)
    - [OpenAPI specificatie](#openapi-specificatie-3)
    - [Run-time gedrag](#run-time-gedrag-3)

## Inleiding

De API's voor Zaakgericht werken vormen de opvolger van zowel de
berichtenstandaard van het Sectormodel Zaken ([StUF-ZKN] 3.10) alsmede het
koppelvlak Zaak- en Document Services ([ZDS] 1.2).

In tegenstelling tot StUF-ZKN en ZDS zijn de API's voor Zaakgericht werken geen
gezamenlijke berichtenstandaard maar is elke API een berichtenstandaard op
zichzelf. Om zaakgericht werken te ondersteunen zijn echter meerdere API's
nodig, die in dit document worden beschreven.

Elke API bestaat uit een Open API-specificatie (OAS), technische documentatie
die het "run-time" gedrag beschrijft en een of meerdere gegevensmodellen. De
OAS is samen met de technische documentatie leidend voor de standaard.

Deze standaardisatie zorgt vervolgens voor gegarandeerde interoperabiliteit
tussen registraties en consumers die van de API's gebruik maken.

[StUF-ZKN]: https://www.gemmaonline.nl/index.php/Sectormodel_Zaken:_StUF-ZKN
[ZDS]: https://www.gemmaonline.nl/index.php/Zaak-_en_Documentservices

### Definities

- OAS schema: een API definitie die de
  [OpenAPI-Specification](https://github.com/OAI/OpenAPI-Specification) volgt.
  **VNG-Realisatie** publiceert de schema's waaraan implementaties moeten voldoen
  op [github](https://github.com/VNG-Realisatie/gemma-zaken/tree/master/api-specificatie).

- Consumer: een technologie die van de API's gebruik maakt. Dit kan een
  taakapplicatie zijn, een andere service in service-naar-service communicatie,
  of eender welke (generieke) client-applicatie.

- 'Uiteindelijk resulteren' betekent dat redirects (`HTTP 301`, `HTTP 302`)
  toegestaan zijn, mits deze redirect-locatie resulteert in een `HTTP 200`.

- Autorisatie: het mechanisme om wel of niet toegang te verlenen tot operaties
  en/of gegevens in de API's. Niet te verwarren met authenticatie.

- Authenticatie: het mechanisme om de identiteit van een een persoon of andere
  entiteit vast te stellen.

- Eindgebruiker: de persoon die gebruik maakt van een (taak)applicatie die
  communiceert via de ZGW API's.

- De codes bij business logica (zoals `zrc-001`) verwijzen naar de
  [Postman tests voor ZGW API's](https://github.com/VNG-Realisatie/gemma-postman-tests)

- Endpoint: een pad dat ontsloten wordt in de API, al dan niet met dynamische
  parameters. Bijvoorbeeld: `/api/v1/zaken/{uuid}`

- Operatie: de combinatie van een HTTP method zoals `POST`, `GET`, `PUT`,
  `PATCH` en `DELETE` en een endpoint.

## Algemene API-eisen

Er wordt zoveel mogelijk uitgegaan van de
[API strategie voor de Nederlandse overheid](api-strategie) (13 februari 2019)
maar de API's zijn in eerste instantie ontwikkeld volgens de
[DSO API- en URI-strategie](dso-strategie). Hier en daar kan worden afgeweken
om redenen van toepasselijkheid of omdat de strategie nog in ontwikkeling is.

[dso-strategie]: https://aandeslagmetdeomgevingswet.nl/digitaal-stelsel/technisch-aansluiten/standaarden/api-uri-strategie/

### Versionering van de API

In overeenstemming met [API-20](api-strategie) MOET het `MAJOR` versienummer in
de URL van de `{API root URL}` zitten. Het versienummer MAG vooraf worden gegaan
door de letter "v", bijvoorbeeld: `https://example.com/api/v1/`.

Zie: Achtergrond over [Versies en migraties](../ontwikkelaars/algemeen/versies-en-migraties)

[api-strategie]: https://docs.geostandaarden.nl/api/API-Strategie/

### Migreren van de API root URL

Als een wijziging van de API root URL **geen** invloed heeft op de inhoud van
de API, ofwel, het betreft geen versiewijziging, dan MOET de API op de oude
`{API root URL}` en alle onderliggende URL's, een HTTP 301 (Definitief
verplaatst) teruggeven. Als `Location`-header MOET de URL staan naar de
resource op de nieuwe `{API root URL}`.

Als een wijziging van de API root URL **wel** invloed heeft op de inhoud van de
API, ofwel, het betreft een versiewijziging, dan MAG de API op de oude
`{API root URL}` GEEN HTTP 301 teruggeven naar de nieuwe `{API root URL}`.

Zie: Achtergrond over [Versies en migraties](../ontwikkelaars/algemeen/versies-en-migraties)

### Beschikbaar stellen van de OAS

Iedere component MOET het OAS schema serveren, onder
`{API root URL}/schema/openapi.yaml`.

Voorbeelden van geldige URLs:

- `https://tstF.vng.cloud/zrc/api/v1/schema/openapi.yaml`
- `https://zrc.nl/api/v1/schema/openapi.yaml`
- `https://api.zrc.nl/v1/schema/openapi.yaml`
- `https://v1.api.zrc.nl/schema/openapi.yaml`

De service-naar-service communicatie MOET het schema opvragen om operaties op
resources uit te voeren.

## Gegevensformaten

Een aantal formaten zijn nog niet formeel vastgelegd in OAS of
[JSON-Schema](json-schema), echter deze worden wel binnen de API's voor
Zaakgericht werken gebruikt en opgelegd.

[json-schema]: https://json-schema.org/

### Duur

Een duur MOET in [ISO-8601 durations](https://en.wikipedia.org/wiki/ISO_8601#Durations)
uitgedrukt worden.

## Autorisatie

De API-endpoints moeten beschermd zijn met autorisatie. Er zijn scopes
gedefinieerd die van toepassing zijn om operaties toe laten. Het kan zijn dat
een operatie toegelaten is door een combinatie van scopes (of-of, of en-en).
Het kan ook dat één scope meerdere operaties toelaat.

De benodigde scopes voor operaties zijn opgenomen in de API-spec en de verdere
betekenis is gedocumenteerd in de referentie-implementaties.

API requests van clients MOETEN een
[JSON Web Token (JWT)](https://tools.ietf.org/html/rfc7519) versturen naar de
API. Dit token MOET in de `Authorization` HTTP header opgenomen worden, met
als type `Bearer`. Voorbeeld:

```
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJkdW1teSIsImlhdCI6MTU1Njg5ODIwMSwiY2xpZW50X2lkIjoiZHVtbXkiLCJ1c2VyX2lkIjoiMTIzIiwidXNlcl9yZXByZXNlbnRhdGlvbiI6IldpbGx5IERlIEtvb25pbmcifQ.41xuzR2jB13B7mbbZsenVyDCaosuJ3mapwX7Arr3wVA
```

Client en server maken gebruik van `shared secret` om het JWT te signen, met
het HMAC SHA-256 algoritme. Iedere client MAG een eigen secret hebben. De
server MOET aan de hand van de `client_id` key in de JWT payload
de bijhorende secret opvragen. De server MOET met het juiste shared secret
het JWT valideren tegen tampering.

Voorbeeld van een payload:

```json
{
    "iss": "dummy",
    "iat": 1556898201,
    "client_id": "dummy",
    "user_id": "123",
    "user_representation": "Willy De Kooning"
}
```

Na succesvolle validatie van het JWT is nu zeker dat de consumer is wie die
beweert te zijn.

Providers MOETEN voor elke aanroep door de client controleren of de client
geautoriseerd is om deze aanroep uit te voeren.

Providers MOETEN een geconfigureerde autorisatiecomponent bevragen met het
`client_id` als query-parameter om de autorisaties van deze client op te
vragen, conform de API-specificatie van het Autorisatiecomponent (AC).

Providers MOGEN deze gegevens cachen om performance-redenen. Indien
er van caching gebruik gemaakt wordt, dan MOETEN providers een mechanisme
inbouwen om wijzingen in het AC meteen door te voeren in de cache. Het is
AANGERADEN om hiervoor te abonneren op notificaties verstuurd door het AC.

**Claims in het JWT**

Zoals in het voorbeeld beschreven, MOETEN een set standaardclaims in het JWT
opgenomen worden:

* `iss`: *(string)* de issuer, welke partij het JWT uitgegeven/gegenereerd heeft. Typisch
  het client ID van de applicatie.
* `iat`: *(integer)* issued-at, moment van genereren van het JWT als UNIX
  timestamp. Dit kan later worden gebruikt.
* `client_id`: *(string)* het client ID van de applicatie, MOET worden gebruikt
  om het bijhorende `secret` op te halen en het JWT te valideren.

Daarnaast ZOUDEN de volgende claims aanwezig MOETEN zijn:

* `user_id`: *(string)* de unieke identificatie van de eindgebruiker in de
  applicatie. In combinatie met `client_id` MOET hieruit de persoon te
  herleiden zijn die verantwoordelijk is voor de API-aanroep. Dit MAG eender
  welk formaat zijn. Indien deze claim niet aanwezig is, wordt de
  `X-NLX-Request-User-Id` uitgelezen.
* `user_representation`: *(string)* de vriendelijke weergave van de
  eindgebruiker die verantwoordelijk is voor de API-aanroep.

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


### Audittrail

Elk component kent een hoofdobject (zie ook [notificaties](#notificaties)).
Alle schrijfacties op het hoofdobject en gerelateerde objecten MOETEN opgenomen
worden in de audittrail van het hoofdobject. Indien een object permanent
verwijderd wordt, dan MOET de audittrail meeverwijderd worden.

Zie de API spec voor de betekenis van de audittrailattributen.

## Zaakregistratiecomponent

Zaakregistratiecomponenten (ZRC) MOETEN aan twee aspecten voldoen:

* de ZRC `openapi.yaml` MOET volledig geïmplementeerd zijn.

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

Bij het aanmaken (`zaakinformatieobject_create`) MOET de URL-referentie
naar het `informatieobject` gevalideerd worden op het bestaan. Indien het ophalen van het object niet (uiteindelijk) resulteert in een `HTTP 200` status code, MOET het
ZRC antwoorden met een `HTTP 400` foutbericht.

#### **<a name="zrc-004">Valideren relatieinformatie op `ZaakInformatieObject`-resource ([zrc-004](#zrc-004))</a>**

Op basis van het `objectType` MOET de `aardRelatie` gezet worden conform het
RGBZ. Omdat het `objectType` `zaak` is, moet `aardRelatie` gelijk zijn aan `"hoort_bij"`.

De `registratiedatum` MOET door het systeem gezet worden op het moment van
aanmaken.

Bij het updaten (`zaakinformatieobject_update` en
`zaakinformatieobject_partial_update`) is het NIET TOEGESTAAN om de relatie
te wijzingen. Bij andere waardes voor de attributen `zaak`, en
`informatieobject` MOET het ZRC antwoorden met een `HTTP 400` foutbericht.

#### **<a name="zrc-005">Synchroniseren relaties met informatieobjecten ([zrc-005](#zrc-005))</a>**

Wanneer een relatie tussen een `INFORMATIEOBJECT` en een `ZAAK` gemaakt
of bijgewerkt wordt, dan MOET het ZRC in het DRC ook deze relatie
aanmaken/bijwerken.

Een voorbeeld:

1. Een informatieobject wordt gerelateerd aan een zaak door een consumer:

    ```http
    POST https://zrc.nl/api/v1/zaakinformatieobjecten HTTP/1.0

    {
        "informatieobject": "https://drc.nl/api/v1/enkelvoudigeinformatieobjecten/1234",
        "zaak": "https://zrc.nl/api/v1/zaken/456789",
        "titel": "",
        "beschrijving": ""
    }
    ```

2. Het ZRC MOET de relatie spiegelen in het DRC:

    ```http
    POST https://drc.nl/api/v1/objectinformatieobjecten HTTP/1.0

    {
        "informatieobject": "https://drc.nl/api/v1/enkelvoudigeinformatieobjecten/1234",
        "object": "https://zrc.nl/api/v1/zaken/456789",
        "objectType": "zaak"
    }
    ```

Merk op dat het aanmaken van de relatie niet gelimiteerd is tot het aanmaken
via de API. Indien elders (bijvoorbeeld via een admininterface) een relatie tot
stand kan komen, dan MOET deze ook gesynchroniseerd worden.

#### **<a name="zrc-006">Data filteren bij de bron op basis van zaaktypes ([zrc-006](#zrc-006))</a>**

Het AC legt op het niveau van `zaaktype` vast welke operaties mogelijk zijn en
wat de maximale vertrouwelijkheidaanduiding is voor een consumer.

Het ZRC MAG ENKEL zaken ontsluiten waarvan:

* het zaaktype voorkomt in de autorisaties van de consumer.
* de vertrouwelijkheidaanduiding lager of gelijk aan de maximale
  vertrouwelijkheidaanduiding is voor het betreffende zaaktype.

De API-specificatie legt vast welke scopes nodig zijn voor welke operaties.
Een provider MOET operaties blokkeren op zaken waarvan de nodige scopes niet
toegekend zijn voor het zaaktype van de betreffende zaak.

Indien een operatie niet toegelaten is, dan MOET de provider met een
`HTTP 403` foutbericht antwoorden.

Een consumer is verbonden aan het concept `Applicatie`, waarop `autorisaties`
gedefinieerd worden. Het is mogelijk om op het niveau van `Applicatie` de vlag
`heeftAlleAutorisaties` te zetten. Indien deze gezet is, dan MOET de provider
alle operaties voor deze consumer toelaten, op alle zaken.

#### **<a name="zrc-007">Afsluiten zaak ([zrc-007](#zrc-007))</a>**
Een zaak wordt afgesloten door een eindstatus toe te kennen aan een `Zaak`. Elk
`ZaakType` MOET minimaal één `StatusType` kennen. De eindstatus binnen een
`ZaakType` is het `StatusType` met het hoogste `volgnummer`.

Een `Zaak` MOET een `Resultaat` hebben voor deze afgesloten kan worden.

De `Zaak.einddatum` MOET logisch afgeleid worden uit het toekennen van de
eindstatus via de `Status.datumStatusGezet`.

Als een `Zaak` een eindstatus heeft dan is de zaak afgesloten en mogen gegevens
van de zaak niet meer aangepast worden (behalve om redenen van correctie). Dit
MOET beveiligd worden met de scope `zds.scopes.zaken.geforceerd-bijwerken`.

Bij het afsluiten van een `Zaak` MOET het ZRC het
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

#### **<a name="zrc-008">Vertrouwelijkheidaanduiding van een zaak ([zrc-008](#zrc-008))</a>**

Indien de client een `vertrouwelijkheidaanduiding` meegeeft bij het aanmaken
of bewerken van een zaak, dan MOET de provider deze waarde toekennen. Indien
de client deze niet expliciet toekent, dan MOET deze afgeleid worden uit
`Zaak.ZaakType.vertrouwelijkheidaanduiding`.

Een `Zaak` response van de provider MOET altijd een geldige waarde voor
`vertrouwelijkheidaanduiding` bevatten. Een client MAG een waarde voor
`vertrouwelijkheidaanduiding` meesturen.

#### **<a name="zrc-009">Valideren `communicatiekanaal` op de `Zaak` resource ([zrc-009](#zrc-009))</a>**

Bij het aanmaken (`zaak_create`) en bijwerken (`zaak_update` en
`zaak_partial_update`) MOET de URL-referentie naar het `communicatiekanaal`
gevalideerd worden op het bestaan. Indien het ophalen van het zaaktype niet
(uiteindelijk) resulteert in een `HTTP 200` status code, MOET het ZRC
antwoorden met een `HTTP 400` foutbericht.

Het ophalen van deze resource moet een JSON-document zijn met de vorm van
een communicatiekanaal zoals gedocumenteerd op de
[referentielijsten-api](https://referentielijsten-api.vng.cloud/api/v1/schema/#operation/communicatiekanaal_read):

```json
{
    "url": "http://example.com",
    "naam": "string",
    "omschrijving": "string"
}
```

#### **<a name="zrc-010">Valideren `relevanteAndereZaken` op de `Zaak`-resource ([zrc-010](#zrc-010))</a>**

De lijst `relevanteAndereZaken` bevat URL-referenties naar andere zaken. Elke
URL-referentie MOET gevalideerd worden op het bestaan. Indien het ophalen van
de url niet (uiteindelijk) resulteert in een `HTTP 200` status code, MOET het ZRC
antwoorden met een `HTTP 400` foutbericht.

In het foutbericht MOET de naam binnen `invalid-params` dan
`relevanteAndereZaken.<index>` zijn, waarbij index start bij 0.

#### **<a name="zrc-011">Gegevensgroepen ([zrc-011](#zrc-011))</a>**

De client MAG gegevensgroepen zoals `Zaak.verlenging` en `Zaak.opschorting`
meesturen met een waarde `null` om aan te geven dat er geen waarde gezet is.
Dit is equivalent aan het niet-meesturen van de key in de request body.
Als de client een (genest) object meestuurt, dan MOET de provider hierop de
validatie van de gegevensgroep toepassen.

De provider MOET altijd de geneste structuur van de gegevensgroep antwoorden.

#### **<a name="zrc-012">Valideren `hoofdzaak` op de `Zaak`-resource ([zrc-012](#zrc-012))</a>**

Bij het aanmaken of bewerken van een `Zaak` kan de `hoofdzaak` aangegeven
worden. Dit MOET een geldige URL-referentie naar een `Zaak` zijn, indien
opgegeven.

Indien de client een `hoofdzaak` opgeeft die zelf een deelzaak is (i.e.
`Zaak.hoofdzaak` != `null`), dan moet het ZRC antwoorden met een `HTTP 400`
foutbericht (deelzaken van deelzaken zijn NIET toegestaan).

Indien de client een zaak bewerkt en diezelfde zaak als URL-referentie meegeeft
als `hoofdzaak`, dan moet het ZRC antwoorden met een `HTTP 400`
foutbericht (een zaak MAG GEEN deelzaak van zichzelf zijn).

#### **<a name="zrc-013">`Zaak.betalingsindicatie` en `Zaak.laatsteBetaaldatum` ([zrc-013](#zrc-013))</a>**

Indien de betalingsindicatie de waarde `"nvt"` heeft en een waarde gegeven is
voor `laatsteBetaaldatum`, dan MOET het ZRC antwoorden met een `HTTP 400`
foutbericht. Bij alle andere waarden van `betalingsindicatie` MAG een waarde
opgegeven worden voor `laatsteBetaaldatum`.

Indien een waarde ingevuld is voor `laatsteBetaaldatum` en de betalingsindicatie
wordt gewijzigd naar `"nvt"`, dan MOET de `laatsteBetaaldatum` op `null` gezet
worden.

#### **<a name="zrc-014">Valideren van producten en/of diensten bij een `Zaak` ([zrc-014](#zrc-014))</a>**

Bij het aanmaken (`zaak_create`) en bijwerken (`zaak_update` en
`zaak_partial_update`) MOET de collectie `productenOfDiensten` worden getoetst
tegen het `Zaaktype.productenOfDiensten` van het betreffende zaaktype. De
producten en/of diensten van de zaak MOETEN een subset van de producten en/of
diensten op het zaaktype zijn.

#### Archiveren

**<a name="zrc-015">Afleiden van archiveringsparameters ([zrc-015](#zrc-015))</a>**

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

**<a name="zrc-016">Zetten `Zaak.archiefstatus` ([zrc-016](#zrc-016))</a>**

De standaardwaarde voor archiefstatus is `nog_te_archiveren`. Indien een andere
waarde gezet wordt, dan MOETEN alle gerelateerde informatieobjecten de status
`gearchiveerd` hebben.

De attributen `Zaak.archiefnominatie` en `Zaak.archiefactiedatum` MOETEN een
waarde krijgen als de de archiefstatus een waarde krijgt anders dan
`nog_te_archiveren`.

Indien deze voorwaarden niet voldaan zijn, dan MOET het ZRC met een `HTTP 400`
foutbericht antwoorden.

**<a name="zrc-017">Vernietigen van zaken ([zrc-017](#zrc-017))</a>**

Bij het verwijderen van een `Zaak` MOETEN de zaak en gerelateerde objecten
daadwerkelijk uit de opslag verwijderd worden. Zogenaamde "soft-deletes" zijn
NIET TOEGESTAAN. Onder gerelateerde objecten wordt begrepen:

- `zaak` - de deelzaken van de verwijderde hoofzaak
- `status` - alle statussen van de verwijderde zaak
- `resultaat` - het resultaat van de verwijderde zaak
- `rol` - alle rollen bij de zaak
- `zaakobject` - alle zaakobjecten bij de zaak
- `zaakeigenschap` - alle eigenschappen van de zaak
- `zaakkenmerk` - alle kenmerken van de zaak
- `zaakinformatieobject` - relatie naar enkelvoudige informatieobjecten \*
- `klantcontact` - alle klantcontacten bij een zaak
- `audittrail` - de geschiedenis van het object

Een deelzaak KAN vernietigd worden zonder dat de hoofdzaak vernietigd wordt.

\* Het verwijderen van een `zaakinformatieobject` in het ZRC leidt er toe dat
het `objectinformatieobject` in het DRC ook verwijderd wordt indien dit kan.

## Documentregistratiecomponent

documentregistratiecomponentsen (DRC) MOETEN aan twee aspecten voldoen:

* de DRC `openapi.yaml` MOET volledig geïmplementeerd zijn.

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

(TODO: valideren dat het van het type `object_type` is -> validatie aanscherpen)

#### **<a name="drc-003">Valideren uniciteit combinatie `object` en `informatieobject` op de `ObjectInformatieObject`-resource ([drc-003](#drc-003))</a>**

Er MOET gevalideerd worden dat de combinatie `object` en `informatieobject`
niet eerder voorkomt. Indien deze al bestaat, dan MOET het DRC antwoorden met
een `HTTP 400` foutbericht.

#### **<a name="drc-004">Valideren bestaan relatie tussen `object` en `informatieobject` in de bron ([drc-004](#drc-004))</a>**

Er MOET gevalideerd worden dat de relatie tussen het `object` en het `informatieobject` al bestaat in de bron van het `object`. De bron van het informatieobject is bekend door de eerdere validaties op deze URL. De API-spec van het ZRC/BRC voorziet in query-parameters om het bestaan te kunnen valideren.

#### **<a name="drc-005">Statuswijzigingen van informatieobjecten ([drc-005](#drc-005))</a>**

Wanneer `InformatieObject.ontvangstdatum` een waarde heeft, dan zijn de waarden
`in bewerking` en `ter vaststelling` voor `InformatieObject.status` NIET
TOEGELATEN. Indien een dergelijke status gezet is _voor_ de verzenddatum opgegeven
wordt, dan moet de API een HTTP 400 foutbericht geven met `status` als veld in
de `invalid-params`. De client MOET dan `ontvangstdatum` leeg laten of eerst de
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

#### Archiveren

**Vernietigen van informatieobjecten**

Een `EnkelvoudigInformatieObject` MAG ALLEEN verwijderd worden indien er geen
`ObjectInformatieObject`-en meer aan hangen. Indien er nog relaties zijn, dan
MOET het DRC antwoorden met een `HTTP 400` foutbericht

Bij het verwijderen van een `EnkelvoudigInformatieObject` MOETEN het
`EnkelvoudigInformatieObject` en gerelateerde objecten daadwerkelijk uit de
opslag verwijderd worden. Zogenaamde "soft-deletes" zijn NIET TOEGESTAAN.
Onder gerelateerde objecten wordt begrepen:

- `gebruiksrechten` - de gebruiksrechten die horen bij het
  `EnkelvoudigInformatieObject`.
- `audittrail` - de geschiedenis van het object.

#### Locken en unlocken van documenten

Bij het bijwerken van `InformatieObject` (`enkelvoudiginformatieobject_update`,
`enkelvoudiginformatieobject_partial_update`) MOET eerst een `lock` verkregen
worden. De consumer voert de `enkelvoudiginformatieobject_lock` operatie uit,
waarbij het DRC MOET antwoorden met een niet-te-raden `lockId`. Het DRC MOET
vervolgens alle schrijf-operaties blokkeren tenzij het correcte `lockId`
meegegeven is.

Het DRC MOET geforceerd unlocken toelaten door 'administrators'. Dit zijn
applicaties die de scope `documenten.geforceerd-unlock` hebben. Deze consumers
MOETEN het `lockId` weglaten indien ze geforceerd unlocken.

## Besluitregistratiecomponent

Besluitregistratiecomponenten (BRC) MOETEN aan twee aspecten voldoen:

* de BRC `openapi.yaml` MOET volledig geïmplementeerd zijn.

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

#### **<a name="brc-004">Valideren relatieinformatie op `BesluitInformatieObject`-resource ([brc-004](#brc-004))</a>**

Op basis van het `objectType` MOET de `aardRelatie` gezet worden conform het
RGBZ. Omdat het `objectType` `besluit` is, moet `aardRelatie` gelijk zijn aan `"legt_vast"`.

Bij het updaten (`besluitinformatieobject_update` en
`besluitinformatieobject_partial_update`) is het NIET TOEGESTAAN om de relatie
te wijzingen. Bij andere waardes voor de attributen `besluit`, en
`informatieobject` MOET het BRC antwoorden met een `HTTP 400` foutbericht.

#### **<a name="brc-005">Synchroniseren relaties met informatieobjecten ([brc-005](#brc-005))</a>**

Wanneer een relatie tussen een `INFORMATIEOBJECT` en een `BESLUIT` gemaakt
of bijgewerkt wordt, dan MOET het BRC in het DRC ook deze relatie
aanmaken/bijwerken.

Een voorbeeld:

1. Een informatieobject wordt gerelateerd aan een besluit door een consumer:

    ```http
    POST https://brc.nl/api/v1/besluitinformatieobjecten HTTP/1.0

    {
        "informatieobject": "https://drc.nl/api/v1/enkelvoudigeinformatieobjecten/1234",
        "besluit": "https://brc.nl/api/v1/besluiten/456789"
    }
    ```

2. Het BRC MOET de relatie spiegelen in het DRC:

    ```http
    POST https://drc.nl/api/v1/objectinformatieobjecten HTTP/1.0

    {
        "informatieobject": "https://drc.nl/api/v1/enkelvoudigeinformatieobjecten/1234",
        "object": "https://brc.nl/api/v1/besluiten/456789",
        "objectType": "besluit",

    }
    ```

Merk op dat het aanmaken van de relatie niet gelimiteerd is tot het aanmaken
via de API. Indien elders (bijvoorbeeld via een admininterface) een relatie tot
stand kan komen, dan MOET deze ook gesynchroniseerd worden.

#### Archiveren

**Vernietigen van besluiten**

Bij het verwijderen van een `Besluit` MOETEN het `Besluit` en gerelateerde
objecten daadwerkelijk uit de opslag verwijderd worden. Zogenaamde
"soft-deletes" zijn NIET TOEGESTAAN. Onder gerelateerde objecten wordt
begrepen:

- `besluitinformatieobject` - relatie naar enkelvoudige informatieobjecten \*
- `audittrail` - de geschiedenis van het object

\* Het verwijderen van een `besluitinformatieobject` in het BRC leidt er toe
dat het `objectinformatieobject` in het DRC ook verwijdert wordt indien dit kan.


## Zaaktypecatalogus

Zaaktypecatalogi (ZTC) MOETEN aan twee aspecten voldoen:

* de ZTC `openapi.yaml` MOET volledig geïmplementeerd zijn.

* het run-time gedrag beschreven in deze standaard MOET correct geïmplementeerd
  zijn.

Het ZTC haalt informatie uit selectielijsten en de Gemeentelijke Selectielijst
2017. Deze gegevens worden ontsloten in de
[VNG-referentielijsten-API](https://referentielijsten-api.vng.cloud/). Op
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
