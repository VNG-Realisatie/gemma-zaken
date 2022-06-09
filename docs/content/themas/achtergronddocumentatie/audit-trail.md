---
title: "Audit trail"
date: '01-05-2019'
weight: 50
---

Gebaseerd op: User Story [#722](https://github.com/VNG-Realisatie/gemma-zaken/issues/722)

## Inleiding

Consumers willen op een eenvoudige manier een audit trail kunnen opvragen zoals
die nu veelal wordt weergeven in monolithische zaaksystemen.

We hanteren voor het opstellen van een audit trail, de volgende definitie:

> De audit trail bevat voldoende gegevens om achteraf te kunnen herleiden (1)
> welke essentiële handelingen (2) wanneer door (3a) wie of (3b) vanuit welk
> systeem (4) met welk resultaat zijn uitgevoerd.
> Tot essentiële handelingen worden in ieder geval gerekend: opvoeren en
> afvoeren posten, statusveranderingen met wettelijke, financiële of voor de
> voortgang van het proces, de zaak of de klant beslissende gevolgen.

Bron: [NORA](https://www.noraonline.nl/wiki/Inhoud_audit_trail)

We laten de relatie met logging (in het algemeen) en doelbinding volgens de AVG
buiten beschouwing. Hier zijn andere oplossingen voor in de maak, zoals [NLX].

## API implementatie

### Endpoint

De API wordt gerealiseerd als alleen-lezen endpoint binnen de API van het
component, waarbij de resource "audittrail" wordt ontsloten als sub-resource
van het hoofdobject van de bron.

Voor het ZRC zal dit dus zijn: `/api/v1/zaken/<uuid>/audittrail`.

De audit trail bevat dus alle wijzigingen op de zaak, waaronder status
wijzigingen, het koppelen of ontkoppelen van documenten, etc.

**Rationale**

De audit trail API kan worden gerealiseerd op verschillende manieren, t.w.:

1. Als zelfstandig component waar alle andere componenten hun audit regels
   naar toe sturen.
2. Als onderdeel van de component API.

We realiseren geen apart component voor de audit trail waar alle componenten
hun logging heen sturen. Dit zou een synchrone afhankelijkheid creëeren en er
gaat potentieel veel informatie over het netwerk wat veel overhead veroorzaakt,
zelfs als niemand deze audit trail ooit raadpleegt. Ten slotte staat deze opzet
een eventueel centraal logging component niet in de weg.

De audit trail API wordt dus onderdeel van elk component. Er zijn hierin 3
keuzes te maken, t.w.:

1. Endpoint buiten de component OAS, en dus een zelfstandige API naast het
   component (`example.com/zrc/api/v1` en `example.com/zrc/audittrail/api/v1`).
2. Endpoint als onderdeel van de OAS van het component, op root niveau
   (`example.com/zrc/api/v1/audittrail`).
3. Endpoint als sub-resource van zaak.
   (`example.com/zrc/api/v1/zaken/<uuid>/audittrail`).

Bij het NRC is voor het ontvangen van notificaties door componenten gekozen
voor een zelfstandige OAS (optie 1). Dit voorkomt dat een wijziging voor de
audit trail API alle API's van componenten raakt. Echter, bij het NRC geeft de
consumer zelf aan waar deze API te vinden is. Bij de audit trail is hiervan geen
sprake en dus moet de API consistent en snel te vinden zijn. Tevens is de
audit trail ook echt een onderdeel van het component (optie 2 en 3).

We kiezen voor optie 3 omdat een audit trail typisch wordt opgevraagd van een
bepaalde zaak. Dit laat optie 2 overigens mogelijk voor de toekomst.

### Attributen

`uuid` (automatisch)

Unieke identificatie van de audit regel.

`requestId` (optioneel)

Unieke identificatie van het verzoek in het netwerk om over verschillende
gateways heen te kunnen loggen.

Op dit moment wordt alleen de [NLX] header `X-NLX-Request-Id` waarde 
overgenomen in dit attribuut bij elke audit regel, indien aanwezig.

`bron` (automatisch)

De naam van het component waar de wijziging in is gedaan. Hoewel dit attribuut
in de context van de API niet relevant lijkt, aangezien de API onderdeel is van
het component. Mocht deze API echter gebruikt worden in een geaggregeerde
context, dan blijft het formaat voor consumers gelijk.

`applicatieId` (verplicht)

Unieke identificatie van de applicatie, binnen de organisatie.

Deze moet worden gehaald uit het payload attribuut `client_id` van het JWT
token. Indien er geen gebruik wordt gemaakt van JWT of het attribuut
`client_id` is niet aanwezig dan kan terugvallen worden op de [NLX] header
`X-NLX-Request-Application-Id`.

`applicatieWeergave` (optioneel)

Vriendelijke naam van de applicatie. Deze kan worden afgeleid uit het `label`
attribuut van de `Applicatie` resource in het Autorisatie Component (AC).

`gebruikersId` (verplicht)

Unieke identificatie van de gebruiker die binnen de organisatie herleid kan
worden naar een persoon. Dit mag bijvoorbeeld het ID zijn van de gebruiker
zoals deze bekend is in Active Directory, of het ID van de gebruiker zoals deze
alleen binnen de applicatie bekend is. In het laatste geval kan de persoon met
behulp van het `applicatieId` ook tot een persoon herleid worden.

Deze moet worden gehaald uit het payload attribuut `user_id` van het JWT token.
Indien er geen gebruik wordt gemaakt van JWT of het attribuut `user_id` is
niet aanwezig dan kan terugvallen worden op de [NLX] header
`X-NLX-Request-User-Id`.

`gebruikersWeergave` (optioneel)

Vriendelijke naam van de gebruiker.

Deze moet worden gehaald uit het payload attribuut `user_representation` van
het JWT token indien aanwezig.

`actie` (verplicht)

De uitgevoerde handeling *zoals bij notificaties*.

`actieWeergave` (optioneel)

Vriendelijke naam van de actie. Bijvoorbeeld als een relatie tussen
een document en een zaak wordt aangemaakt: "gekoppeld aan Zaak MOR-000001".

*TODO: Wellicht ook toevoegen aan het NRC (buiten scope)*

`resultaat` (verplicht)

HTTP status code van de API response van de uitgevoerde handeling. Een HTTP
status code van "200" of "201" is bijvoorbeeld een succesvol uitgevoerde
handeling, terwijl een "403" aangeeft dat de gebruiker of applicatie het wel
geprobeerd heeft maar de handeling is niet uitgevoerd.

`hoofdObject` (verplicht)

De URL naar het hoofdobject van een component *zoals bij notificaties*. Bij
het ZRC is dit dus altijd de URL naar een zaak.

`resource` (verplicht)

De resource naam *zoals bij notificaties*.

`resourceUrl` (verplicht)

De URL naar het object *zoals bij notificaties*. Dit is bijvoorbeeld de URL
naar een status, een rol, etc.

`resourceWeergave` (optioneel)

Vriendelijke identificatie van het object. Bijvoorbeeld de zaak identificatie
of de omschrijving van een status. Deze weergave kan bijvoorbeeld gebaseerd zijn
op de semantische unieke identificatie zoals deze in het RGBZ staat.

`toelichting` (optioneel)

Toelichting waarom de handeling is uitgevoerd. Dit kan handig zijn voor sommige
handelingen waarbij additionele context gewenst is, zoals het ophogen van een
archiveringstermijn of een correctie buiten het reguliere proces om. Deze kan
voor elk verzoek meegegeven als `X-Audit-Toelichting` header.

`aanmaakdatum` (automatisch)

De datum waarop de handeling is gedaan.

`wijzigingen` (verplicht)

Een object met 2 attributen:

* `oud` - Volledige JSON body van het object zoals dat bestond voordat de actie
  heeft plaatsgevonden. De waarde `null` wordt gebruikt als er geen oude versie
  is (bijvoorbeeld in het geval van het aanmaken van een object).
* `nieuw` - Volledige JSON body van het object na de actie. De waarde `null`
  wordt gebruikt als er geen nieuwe versie is (bijvoorbeeld in het geval dat
  het object wordt verwijderd).

#### Voorbeeld

In het ZRC wordt de audit trail als volgt ontsloten:

```http
GET /api/v1/zaken/<uuid>/audittrail
[
  {
    "uuid": "311cf2",
    "bron": "ZRC",
    "applicatieId": "demo-app",
    "applicatieWeergave": "Demo applicatie",
    "gebruikersId": "14",
    "gebruikersWeergave": "Joeri Bekker",
    "actie": "create",
    "actieWeergave": "",
    "resultaat": 201,
    "hoofdObject": "https://www.example.com/api/v1/zaken/5ab6e2",
    "resource": "status",
    "resourceUrl": "https://www.example.com/api/v1/statussen/11cb71",
    "resourceWeergave": "Ingediend",
    "toelichting": "",
    "aanmaakdatum": "2019-05-05T11:53:18.090384Z",
    "wijzigingen": {
      "oud": null,
      "nieuw": { ... },
  }
]
```

Hiermee kan de volgende (eenvoudige) audit regel worden opgesteld:

```
<aanmaakdatum> <resource> "<resourceWeergave>" is <resultaat> <actie/actieWeergave> in <bron> door <gebruikersWeergave> (<gebruikersId>) via <applicatieWeergave> (<applicatieId)
```

Dat als instantie vertaald kan worden naar:

```
5 mei 2019 11:53 Status "Ingediend" is succesvol aangemaakt in ZRC door Joeri Bekker (14) via Demo Applicatie (demo-app).
```

### Samenstellen van volledige audit trail

Tot nu toe hebben we alleen een audit trail besproken van een enkel component.
Als er echter bij een zaak ook documenten en besluiten worden gemaakt in andere
componenten, dan zou deze idealiter in een volledige audit trail van de zaak
terug komen. Afhankelijk van de gebruikersinterface kan dit wel of niet nodig
zijn.

Alle componenten gaan de audit trail endpoint ontsluiten. Als de zaak wordt
opgevraagd, dan worden ook de gerelateerde documenten en besluiten bekend zoals
die leven in respectievelijk het DRC en het BRC. Hiervoor zal dus 1 call per
component nodig zijn om de volledige audit trail te verkrijgen.

Overigens wordt dit niet persé eenvoudiger als alles in 1 audit trail component
zou zitten. Immers moeten nog steeds alle URLs van de hoofdObjecten bekend zijn
en worden opgevraagd.

### Verwijderen van een object

Als een object wordt verwijderd in het kader van archievering, dan moet ook de
audit trail verwijderd worden.

[NLX]: https://docs.nlx.io/
