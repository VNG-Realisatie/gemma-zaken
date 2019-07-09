---
title: "Ontwerpkeuzes"
date: '31-7-2018'
---

## UUID4 als ID-parameter in endpoints

De ID-parameter, hieronder aangeduid met `{uuid}` wordt gebruikt om via de URL
een enkel object van een bepaald type resource te vinden. Bijvoorbeeld een
`Zaak`:

|URL|Voorbeeld|
|---|---|
| `https://www.example.com/zaken/{uuid}`|`https://www.example.com/zaken/550e8400-e29b-41d4-a716-446655440000`|

Een [UUID (versie 4)] is in de praktijk altijd uniek, zonder dat deze centraal
hoeft te worden bijgehouden. Deze keuze laat onverlet de mogelijkheid om op
andere manieren bij een enkel object te komen, zoals op een combinatie van
velden die samen uniek zijn, zoals `bronorganisatie` en `zaakidentificatie`:
`https://www.example.com/zaken/?bronorganisatie=0329&zaakidentificatie=MOR-0000001`

*Achtergrond*
De paden van API endpoints bevatten referenties naar de objecten in de
achterliggende datastore. Deze parameters zouden semantisch kunnen ingevuld
worden, zoals gebruikmaken van `bronorganisatie` en `zaakidentificatie` voor
een zaak. Echter, na analyse blijkt dat dit lastig consequent toe te passen is
door de hele de API heen. Tevens wekt het de indruk dat dat deze parameters
genoeg zijn om een Zaak te vinden maar dat is niet correct. De volledige URL is
nodig voor het opvragen van een enkele Zaak.

Daarom is besloten om gebruik te maken van [UUID (versie 4)] voor deze
parameters. De motivatie is verder dat deze:

* uniciteit garandeert, ook over meerdere systemen heen;
* geen volgordelijkheid/database IDs lekt;
* de DSO API-richtlijnen volgt;
* semantisch bevragen niet onmogelijk maakt.

[UUID (versie 4)]: https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)


## ISO-8601 durations voor uitdrukken van duur

Voor het uitdrukken van duur wordt gebruikt gemaakt van [ISO-8601 durations](https://en.wikipedia.org/wiki/ISO_8601#Durations). Dit sluit aan bij ISO-8601 weergave van timestamps doorheen de API.


## Omgang met polymorfe resources

In het RGBZ zijn er voor sommige relaties meerdere types van gerelateerde
resources mogelijk. Concrete voorbeelden hiervan zijn:

* betrokkenen bij een zaak - dit kunnen `Natuurlijke Personen`, `Medewerkers`,
  `Organisatorische Eenheden` en meer zijn. Elk van deze betrokkenen heeft
  verschillende attributen, en een aantal komen (bijna) overal voor.

* objecten gerelateerd aan een zaak via ZAAKOBJECT. Hier zijn erg veel types
  mogelijk, bijvoorbeeld: `Huishouden`, `OpenbareRuimte`, `Wegdeel` etc.

In essentie is dit een vorm van polymorfisme.

Door het uitgangspunt van Common Ground om data-bij-de-bron-opslaan te hanteren,
werken we in de ZGW API specificaties met _URL referenties_, wat in deze context
betekent dat de relaties een referentie-url geven naar de gerelateerde resource.
Een client/consumer weet op voorhand niet naar welke vorm van gerelateerde
resource er verwezen wordt.

Daarom is ervoor gekozen om op de relatie bij te houden om welk type resource
het gaat. Een concreet voorbeeld van een response is dan:

```http
GET https://zaken.api.haarlem.nl/v1/zaakobjecten/c9a651  HTTP/1.0
Content-Type: application/json

{
  "url": "https://zaken.api.haarlem.nl/v1/zaakobjecten/c9a651",
  "zaak": "https://zaken.api.haarlem.nl/v1/zaken/66a38b",
  "object": "https://objecten.api.haarlem.nl/v1/wijken/3fa723",
  "relatieomschrijving": "Speelt alleen in deze wijk",
  "type": "Wijk"
}
```

Het gaat hier dan om het `type` veld.

De URLs in dit voorbeeld zijn uiteraard fictief.


## Naamgeving van de API velden binnen een resource

* Prefixes die slaan op de eigen resource, worden niet gebruikt. Voorbeeld:
  Attribuutsoort [informatieobjecttype.informatieobjecttype-omschrijving](https://www.gemmaonline.nl/index.php/Imztc_2.1/doc/attribuutsoort/informatieobjecttype.informatieobjecttype-omschrijving)
  in RGBZ2 krijgt de naam "omschrijving" in de API, aangezien het een veld is
  binnen de resource `informatieobjecttype`. Dit komt overeen met de in RGBZ
  genoemde XML-tag.

  ```javascript
  {
      "url": "https://example.com/drc/api/v1/informatieobjecttypen/8534ba6a-bcde-4387-b054-6bde6d1ded8f",
      "omschrijving": "Document"
      // ...
  }
  ```
* Relaties worden **niet** aangeduid met hun relatie omschrijving (`isVan`,
  `heeft`, `kent`, etc.). Dit heeft mede te maken met het feit dat er geen
  mnemonic attributen zijn (zoals in StUF-ZKN) in de REST API, waardoor het
  niet direct duidelijk is naar wat voor type resource verwezen wordt.
* Indien verwezen wordt naar een andere resource (relatie), wordt de volledige
  naam van de resource gebruikt als veldnaam. Voorbeeld: De resource `zaak`
  heeft een veld `zaaktype` en niet `type`. Ter vergelijking, in StUF-ZKN is
  dit: `zaak-isVan-<zaak type data>` waar `isVan` verwijst naar het `zaaktype`.

  ```javascript
  {
      "url": "https://example.com/zrc/api/v1/zaken/6232ba6a-beee-4357-b054-6bde6d1ded6c",
      "zaaktype": "https://example.com/ztc/api/v1/zaaktypen/6232ba6a-beee-4357-b054-6bde6d1ded6c"
      // ...
  }
  ```


## Groepattributen

Indien een object een groepattribuutsoort heeft (een groep van bij elkaar behorende attribuutsoorten), al dan niet herhalend d.w.z. kardinaliteit nul of meer (een 'lijst' van waarden van de attributen van het groepattribuut), dan wordt het groepattribuut inline
(binnen de resource voor het object) ontsloten. Het krijgt dus geen eigen resource, het heeft immers geen zelfstandig bestaansrecht. Het heeft alleen bestaansrecht als eigenschap van het object, net zoals attribuutsoorten.
Typische voorbeelden zijn (zaak-)kenmerken en (zaak-)eigenschappen waarin `Zaak` het hoofdobject betreft,
en `Kenmerk` en `Eigenschap` de groepattributen.

Voorbeeld:

```javascript
{
    "url": "https://example.com/zrc/api/v1/zaken/6232ba6a-beee-4357-b054-6bde6d1ded6c",
    "zaaktype": "https://example.com/ztc/api/v1/zaaktypen/6232ba6a-beee-4357-b054-6bde6d1ded6c"
    // ...
    "kenmerken": [
        {
            "kenmerk": "test",
            "bron": "http://www.example.com/"
        }
    ]
}
```


## Input validatie

Componenten die APIs aanbieden (ZRC, DRC, ZTC) moet aan volledige
inputvalidatie doen. Dit betekent dat er _meer_ validatie nodig is dan enkel
garanderen dat een veld aan het url-formaat voldoet, en dat er communicatie
tussen systemen is in het geval van gedistribueerde componenten.

Een concreet voorbeeld hiervan is het zetten van een STATUS op een ZAAK:

1. Het aanmaken van een status gebeurt door een nieuwe status te POSTen, met
   onder andere de URL van het `statusType`.
2. Het ZRC MOET deze `statusType` url opvragen uit het ZTC, en controleren dat
   het zaaktype van dit statustype overeenkomt met het zaaktype van de
   betreffende zaak.

De foutberichten voor deze validatie zullen opgesteld worden en opgenomen in
de API spec.

Noot: voor suites kan de implementatie hiervan uiteraard afwijken - indien
alles in 1 enkele database leeft, en de suite ontsluit 3 APIs, dan kan prima
de validatie intern gebeuren op een geoptimaliseerde manier. Belangrijk is dat
de fout-responses (zie ook #130) correct teruggegeven worden.

Noot 2: authenticatie en authorisatie worden in een later stadium uitgewerkt.
Het is bekend dat hier goed over nagedacht moet worden.


## Documenteren (input)validatie

De [input validatie](#input-validatie) kan enkel in tekstuele vorm in de OAS
api-spec opgenomen worden. We houden het formaat:

```md
Er wordt gevalideerd op:
- geldigheid besluit URL
- geldigheid informatieobject URL
```

Deze documentatie wordt opgenomen in de `description` key voor de operation
(bijvoorbeeld `besluitinformatieobject_create`).

Voorbeeld:

```yaml
paths:
  /besluiten:
    post:
      operationId: besluitinformatieobject_create
      description: |-
        Registreer in welk(e) INFORMATIEOBJECT(en) een BESLUIT vastgelegd is.

        Er wordt gevalideerd op:
        - geldigheid besluit URL
        - geldigheid informatieobject URL
```


## Besluitenregistratie (BRC)

Er komt een aparte besluitenregistratie (naast ZRC, ZTC en DRC) om besluiten
in vast te leggen. De motivatie hiervoor is dat besluiten een bestaansrecht
hebben onafhankelijk van zaken: niet elk besluit ontstaat gedurende de
uitvoering van een zaak (denk aan raadsbesluiten).

Hierbij lopen we wat vooruit, maar volgen we wel data-bij-de-bron principes uit
Common Ground.
BESLUITTYPE laten we vooralsnog in de ZTC. Nader bepaald moet gaan worden hoe we hiermee omgaan, zoals onderbrengen in de BRC, aparte type-componenten cq. api's e.d.

Dit betekent dat er voor BESLUIT een informatiemodel moet komen, ontrokken aan het
RGBZ. BESLUIT krijgt een optionele relatie naar ZAAK.

De verwachting is dat er later vergelijkbare designkeuzes gemaakt worden voor
andere resources, zoals bijvoorbeeld klantcontacten.


## Response bij input validatie

De DSO schrijft een structuur voor waar een fout-response aan moet voldoen
in het geval van validatiefouten:

```json
{
    "type": "...",
    "title": "...",
    "status": 400,
    "detail": "...",
    "instance": "...",
    "invalid-params": [{
        "type": "...",
        "name": "<veldnaam>",
        "reason": "Maximale lengte overschreden.",
    }]
}
```

Op het [forum](https://forum.pdok.nl/t/formaat-foutafhandeling-input-validatie-api-50/1848)
is nagevraagd hoe er moet omgegaan worden met meerdere fouten op hetzelfde veld,
met de conclusie dat dit beter gespecifieerd moet worden.

In de ZGW API's kiezen we ervoor om elke fout op een veld als apart object op te
nemen binnen de `"invalid-params"` sleutel. Dit laat clients toe om elke
individuele fout te renderen zoals zij wensen.

Tevens voegen we op hoofdniveau van fouten en binnen een object in
`"invalid-params"` een sleutel `"code"` toe. Dit veld bevat een waarde die door
machines kan begrepen worden, bijvoorbeeld `"invalid"` of
`"max_length_exceeded"`. De `"type"` sleutel is namelijk optioneel en bedoeld
voor developers om meer informatie over het fouttype te lezen, en niet voor
automatische verwerking.

Een voorbeeld response is dan:

```json
{
    "type": "URI: https://zaken-api.vng.cloud/ref/fouten/ValidationError/",
    "title": "Ongeldige gegevens",
    "status": 400,
    "code": "invalid",
    "detail": "Er deden zich validatiefouten voor",
    "instance": "urn:uuid:2d3f8adb-470d-4bf4-8c43-4b2ebeef7504",
    "invalid-params": [
        {
            "name": "identificatie",
            "code": "max-length",
            "reason": "Maximale lengte overschreden.",
        },
            {
            "name": "identificatie",
            "code": "special-characters",
            "reason": "De identificatie mag geen speciale karakters bevatten.",
        }
    ]
}
```

Merk op dat de concrete codes hier fictief zijn en puur ter illustratie zijn.


## Relaties aangeven in query parameters

Om relaties zowel naar een andere resource (zoals `status`) als naar een genest attribuut (zoals `kenmerken`) te gebruiken binnen query parameters, wordt de `__` (dubbele underscore) gebruikt tussen de attribuutnamen.

**Voorbeelden**

*Voor filteren:*
* `?zaak__kenmerken=test`
* `?zaak__status=http://example.com`

*Voor de `fields` query parameter:*
* `?fields=zaak__kenmerken`
* `?fields=zaak__status`


## URIs eindigen nooit op een trailing slash ("/")

De URIs die gebruikt worden om collecties van objecten, of individuele objecten
op te vragen, eindigen nooit op een trailing slash:

**Voorbeelden**

*Goed*
* `/api/v1/zaken`
* `/api/v1/zaken?identificatie=12345`
* `/api/v1/zaken/67890`

*Fout*
* `/api/v1/zaken/`
* `/api/v1/zaken/?identificatie=12345`
* `/api/v1/zaken/67890/`

**Rationale**
De DSO heeft hier geen expliciet standpunt over maar alle voorbeelden zijn
zonder trailing slash. Daarnaast zijn veel commerciele APIs die dit voorbeeld
volgen zoals [Google](https://developers.google.com/gmail/api/v1/reference/users/drafts/list)
en [Facebook](https://developers.facebook.com/docs/graph-api/reference/photo/#Creating).
Verschillende bronnen zijn hier wel over verdeeld, zoals
[REST API tutorial](https://restfulapi.net/resource-naming/) en [Wikipedia](https://en.wikipedia.org/wiki/Representational_state_transfer#Relationship_between_URL_and_HTTP_methods)
maar er is gekozen om te kijken naar de praktijk en DSO.


## Nesten van resources

De [DSO API-strategie](https://aandeslagmetdeomgevingswet.nl/digitaal-stelsel/technisch-aansluiten/standaarden/api-uri-strategie/) stelt:

> **API-09 Relaties van geneste resources worden binnen het eindpunt gecreëerd"**
> Als een relatie alleen kan bestaan binnen een andere resource (geneste resource), wordt de relatie binnen het eindpunt gecreëerd. De afhankelijke resource heeft geen eigen eindpunt

Aanvullingen hierop:

* Er mag worden afgeweken van deze richtlijn, mits goed onderbouwd en gedocumenteerd.
* Er wordt niet dieper genest dan 1 niveau, tenzij goed onderbouwd en gedocumenteerd.

**Rationale**

Conceptueel is dit precies zoals het moet zijn. Echter, voortschrijdend inzicht, voortkomend uit gemaakte implementaties van referentie componenten en demo consumers, leidt er toe dat deze richtlijn wordt opgerekt.

Concreet voorbeeld is een consumer die een lijst van ZAKEN van verschillende ZAAKTYPEN laat zien en daar het STATUSTYPE bij wil laten zien. Conceptueel bevind een STATUSTYPE zich altijd binnen ZAAKTYPE (in het ImZTC). Echter, dit zou in het voorbeeld betekenen dat we voor elk ZAAKTYPE dat voorkomt in de lijst van ZAKEN, een aparte call gemaakt moet worden om de STATUSTYPEs op te halen. Veel efficienter is het om in 1x een lijst van STATUSTYPEN op te halen en de consumer deze te koppelen aan de relevante ZAAK.


## Vertaling van relaties

Een 0-op-N of 1-op-N relatie tussen objecttypen A en B in een informatiemodel
zoals RGBZ of ImZTC kan eenvoudig vertaald worden naar een REST API door een
hyperlink op te nemen in de resource dat meerdere keren kan voorkomen in de
relatie, B in dit geval. Het veld met de hyperlink in resource B verwijst naar
de gerelateerde resource A. Dit is het principe van 'linked data'.

Bijvoorbeeld in het RGBZ kan een zaak kan nul of meer statussen hebben en een
status kan niet bestaan zonder een zaak, oftewel er is sprake van een 1-op-N
relatie tussen `Zaak` en `Status`. De resource `Status` bevat naast zijn eigen
gegevens het (toegevoegde) veld `"zaak"` dat de url naar de resource van de
gerelateerde zaak bevat.

Opmerking: We gaan er gemakshalve vanuit dat 0-op-N of 1-op-N relaties geen
eigen gegevens hebben. In het RGBZ komt dit in ieder geval niet voor.

Een **N-op-M** relatie tussen objecttypen A en B wordt vertaald als een nieuwe
resource R die fungeert als een kruistabel zoals in databases. De resource R
bevat de volgende velden:

* url naar zichzelf (resource R),
* url naar resource A,
* url naar resource B,
* de gegevens van de relatie zelf (als die er zijn).

Het voordeel om een N-op-M relatie als resource te vertalen is dat je `POST` en
`DELETE` operaties kunt uitvoeren om relaties toe te voegen of te verwijderen.
Als je dat niet doet en je de relaties bijvoorbeeld bijhoudt bij één of beide
gerelateerde resources, dan belandt je al snel in een minder handige situtie
waabij je de `PATCH` (of `PUT`)-operaties moet gebruiken om het lijstje met
hyperlinks naar de gerelateerde resources bij te werken.

Bijvoorbeeld in het RGBZ is de relatie tussen `Zaak` en `Informatieobject` N-op-M.
Deze relatie is vertaald naar de resource `ZaakInformatieObject` met de
volgende velden:

* url (hyperlink naar zichzelf),
* zaak (hyperlink naar de gerelateerde zaak),
* informatieobject (hyperlink naar het gerelateerde informatieobject).

In geval van de ZGW API's is de relatie tussen zaken en informatieobjecten
gedistribueerd over meerdere ZRC- en DRC-instanties en daarmee een speciaal
geval. Zie [Many-to-many relaties verspreid over API's](#many-to-many-relaties-verspreid-over-apis)
voor de designkeuzes hierbij.


## Many-to-many relaties verspreid over API's

Deze beslissing komt voort uit
[issue #166](https://github.com/VNG-Realisatie/gemma-zaken/issues/166).

Tussen twee componenten A en B (met component A de component waar in het IM de
relatie naar component B loopt), wordt de relatie in beide componenten
bewaard. Eventuele metagegevens (extra informatie op de relatie) komt in
component A te liggen, en component B bevat _enkel_ de relatieinformatie zelf.

Dit is een technische oplossing zodat beide componenten de relaties kunnen
opvragen zonder alle (mogelijks honderden) componenten af te moeten lopen om
te vragen of ze een relatie hebben.

Een consumer maakt 1x een relatie aan, tussen component A en B, met
metagegevens over de relatie in component A. Component A is vervolgens
verantwoordelijk om de relatie in component B aan te maken.

We stemmen de `objectTypes` af zodat die mappen op de namen van resources om
generieke synchronisatieimplementaties mogelijk te maken.

Component B moet dan aan de volgende spelregels voldoen:

- de naam van de resource is `{resourceB}{resourceA}`, in component B
- de resource wordt genest ontsloten binnen `ResourceB`
- de resource accepteert een URL-veld met de naam `resourceA`

Deze spelregels en interactie worden actief getest in de
[integratietests](https://github.com/vng-Realisatie/gemma-zaken-test-integratie)
om compliancy af te kunnen dwingen.

Een concreet voorbeeld hiervan is een `INFORMATIEOBJECT` in het DRC en een
`ZAAK` in het ZRC:

1. De consumer maakt in het DRC een relatie (met polymorfe relatieinformatie):

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

2. Het DRC doet vervolgens een request naar het ZRC (op basis van de URL van `object`):

    ```http
    POST https://zrc.nl/api/v1/zaken/456789/zaakinformatieobjecten

    {
       "informatieobject": "https://drc.nl/api/v1/enkelvoudigeinformatieobjecten/1234",
    }
    ```


## Zaak afsluiten

Een zaak wordt afgesloten door een eindstatus toe te kennen aan een `ZAAK`. Elk
`ZAAKTYPE` heeft minimaal één `STATUSTYPE`. De eindstatus binnen een `ZAAKTYPE`
is het `STATUSTYPE` met het hoogste `volgnummer`.

Het toekennen van dit `STATUSTYPE` aan een `ZAAK` bepaalt ook een logisch af te
leiden `ZAAK.einddatum`; dit is namelijk de datum waarop de eindstatus
is toegekend. Om die reden is `ZAAK.einddatum` een alleen-lezen attribuut van
`ZAAK`.

Als een `ZAAK` een eindstatus heeft dan is de zaak afgesloten en mogen gegevens
van de zaak niet meer aangepast worden (behalve om redenen van correctie). Dit
is voorlopig een verantwoordelijkheid van de consumer en/of autorisatielaag.

In API-calls, kan de flow er als volgt uit zien:

1. Consumer wil onderstaande `ZAAK` afsluiten:

```javascript
GET /zrc/api/v1/zaken/12345

HTTP 200
{
    "einddatum": null,
    // ...
}
```

2. Consumer wil onderstaande eindstatus zetten:

```javascript
GET /ztc/api/v1/catalogus/12345/statustypen?zaaktype=/ztc/api/v1/zaaktype/44912

HTTP 200
[{
    "uuid": 99321,
    "volgnummer": 1,
    "isEindstatus": false,
    // ...
},{
    "uuid": 67890,
    "volgnummer": 2,  # Het laatste STATUSTYPE binnen dit ZAAKTYPE
    "isEindstatus": true,
    // ...
}]
```

3. Consumer werkt een `ZAAK` bij met de eindstatus:

```javascript
POST /zrc/api/v1/zaakstatussen
{
    "zaak": "/zrc/api/v1/zaken/45678",
    "statustype": "/ztc/api/v1/catalogus/12345/statustypen/67890",
    "datumStatusGezet": "2018-10-08T12:23:07+01:00",
    // ...
}
```

4. Consumer haalt de `ZAAK` opnieuw op:

```javascript
GET /zrc/api/v1/zaken/12345

HTTP 200
{
    "einddatum": "2018-10-08",
    // ...
}
```

**Rationale**

In de ZDS 1.x standaard is er nog [geen eenduidig besluit genomen over hoe een
zaak wordt afgesloten](https://discussie.kinggemeenten.nl/discussie/gemma/koppelvlak-zs-dms/afsluiten-van-een-zaak):
Dit kan door het toevoegen van de laatste status (`STATUSTYPE` met het hoogste
`volgnummer`) aan de `ZAAK` of door het vullen van de `einddatum` (van de
`ZAAK`).

Er is echter behoefte aan een consistente manier om zaken af te sluiten. In
deze oplossing worden zowel `ZAAK.einddatum` als `STATUSTYPE` gebruikt waarbij
er geen onduidelijkheid meer ontstaat over hoe een `ZAAK` wordt afgesloten.

## Mechanisme voor autorisatie

De DSO schrijft voor om OAUTH2 te gebruiken op API niveau voor authenticatie
en autorisatie. Kort samengevat is OAUTH2 te complex voor onze behoeften en
maken we geen gebruik van de features ervan. We gebruiken JSON Web Tokens
om autorisatie te regelen, en dan in de HMAC 'signed' vorm (dus geen
assymetrische encryptie).

In de payload van het JWT voorzien we in een `scopes` key, met als waarde
een lijst van strings die de scopes voorstellen:

```json
{
    "scopes": [
        "zds.scopes.scope1",
        "zds.scopes.scope2.1",
        "zds.scopes.scope2.3",
    ]
}
```

*(scope namen zijn fictief)*

**Rationale**

OAUTH2 is een framework voor token-uitgifte, wat complex is voor server en
client. De grondslag is delegation - de eindgebruiker geeft een applicatie
toestemming om als die gebruiker acties uit te voeren en/of hun gegevens te
gebruiken. Hierbij identificeert de applicatie zich bij de service, wat
registratie van applicaties bij elke instantie van de zaken-APIs met zich
meebrengt (en dus extra beheer).

Daarbij komt dat OAUTH2 geen authenticatie-service is, dus gemeentes moeten nog
steeds een mechanisme hebben in de (centrale) authenticatie-service om een
persoon te kunnen authenticeren met wat de gemeente gebruikt (bijvoorbeeld
Active Directory).

OAUTH2 kent twee soorten tokens die uitgegeven worden - opake tokens en
transparante tokens (zoals JWT). JWT wordt vaak gecombineerd met OAUTH2 omdat
je claims kan meegeven _en_ het token kan gevalideerd worden tegen _tampering_.

JWT wordt typisch in een federatiecontext gebruikt - hierbij wordt de gebruiker
losgekoppeld van het token zelf en gaat het om wat er wel/niet kan. De claims
in JWT kunnen volgens afspraak ingesteld worden, wat alle flexibiliteit toelaat.

Het grote voordeel van JWT is dat het stateless is, en er dus niet naar de
autorisatieservice moet teruggekeerd worden om de claims te valideren.

Vergeleken met OAUTH2 biedt JWT ons alles wat we nodig hebben, en het is veel
meer lichtgewicht.

Door de aard van de claims (aangeven van scopes), is het ook geen probleem
dat de payload van de tokens niet versleuteld uitgewisseld wordt. Dit laat ons
ook toe om bijvoorbeeld in NLX achter te kijken welke scopes/payloads over de
lijn gingen - dit zou met encryptie niet mogelijk zijn.

In de JWT-situatie wordt de organisatie zelf ook verantwoorlijke voor de
token-uitgifte. Organisaties hebben alle vrijheid om dit naar eigen wensen
in te richten.

De volledige architectuur is uitgewerk in
[de documentatie](../../ontwikkelaars/algemeen/authenticatie-autorisatie)

## Enumeraties

Enumeraties zijn in essentie lijstjes met mogelijke waarden. Deze waarden zijn
semi-technisch van aard en geven niet altijd de volledige intentie aan van de
waarde. Deze waarden staan op dit moment niet in het RGBZ.

We kiezen er voor waarden in zo compact mogelijke tekstuele representatie van
op te nemen in de OAS. Daarnaast mag voor elk attribuut dat een enumeratie
betreft, een weergave-attribuut worden toegevoegd als `string`, die de
volledige tekstuele waarde als alleen-lezen teruggeeft. Zo'n attribuut eindigt
altijd op `Weergave`.

In de omschrijving van het enumeratie-attribuut, staat de mapping omschreven
tussen de waarde en de omschrijving die wordt getoond in het weergave-attribuut.

*Voorbeelden:*

```yaml
---
taal: en
taalWeergave: Engels

```

In het schema:
```yaml
---
taal:
  type: string
  description: |-
    De taal afkorting volgens ISO 639-2:
    * dut - Dutch
    * eng - English
  enum:
  - dut
  - eng
taalWeergave:
  type: string
  description: De volledige naam van de taal
```

## Bestandsnamen

In RGBZ worden bestandsnamen als gegevensgroep `bestandsnaam` + `extensie`
gespecifieerd. We kiezen ervoor om in de API deze te combineren in 1 veld
`bestandsnaam`. Dit is in lijn met bestaande APIs in de industrie en ook
besturingssystemen slaan de twee als 1 entiteit op.

## Fysieke integriteit (TMLO)

In het RGBZ zijn attributen i.v.m. archiveren opgenomen, afkomstig uit TMLO.
Deze zijn te vaag gespecifieerd om er echt (geautomatiseerd) iets mee te kunnen
doen. Daarom is een initiële lijst van gangbare checksum-algoritmes opgenomen
als enum. Als er een landelijke referentielijst komt, dan zal de enum in een
latere versie daarnaar verwijzen.

De kwestie is gedetailleerd beschreven in de landelijke
[KP-Api](https://github.com/Geonovum/KP-APIs/issues/20) repository.

Een statische lijst is makkelijk aan versionering te koppelen, wat het voor
partijen heel duidelijk maakt welke algoritmes ze moeten ondersteunen.
