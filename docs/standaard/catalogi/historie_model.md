---
title: "Histormodel Catalogi API"
date: '25-02-2025'
weight: 10
layout: page-with-side-nav
---

# Historiemodel in de Catalogi API

## Inleiding

Omdat van een Zaak, Informatieobject of Besluit altijd de bijbehorende definities moeten kunnen worden opgevraagd zoals die waren 
ten tijde van het aanmaken van die Zaak, Informatieobject of Besluit is bij het ontwikkelingen van de ZWG standaard gekozen voor 
het maken van nieuwe resources wanneer een type-definitie aangepast moet worden. Deze keuze, hoewel begrijpelijk gezien de tijd 
en kennis, heeft geleid tot een afwijking van gangbaar gedrag van API's. Het automatische versiebeheer in de Catalogi API wijkt af van 
dat van de overige API's: De resources in de Catalogi API zijn dus versies van de betreffende resources. "Zaaktype" moet gelezen worden 
als "Versie van een Zaaktype", "Informatieobjecttype" is een "Versie van een Informatieobjecttype", "Besluittype" is een "Versie van een Besluittype" etc.
Dit begrip is essentieel om de Catalogi API en het historiemodel te begrijpen en correct toe te kunnen passen.

Concreet betekent dit dat wanneer van een Zaaktype een nieuwe versie gemaakt wordt een nieuwe resource wordt aangemaakt met
een eigen identifier (UUID) en eigen waarden. Ditzelfde geldt voor Informatieobjecttype en Besluittype.

Nadeel hiervan is echter dat de relaties tussen de verschillende definities gelegd worden middels urls. Deze urls bevatten de UUID
en wanneer een nieuwe versie van een definitie gemaakt wordt moeten ook alle definities die naar de gewijzigde definitie verwijzen
aangepast worden. Dit wordt al snel een ingewikkelde kluwen van definities die lastg te beheren is.

Daarom is in Catalogi API 1.3.0 het zogenaamde historiemodel ingevoerd.

Het historiemodel moet een aantal doelen invullen:
1. Het beheer van de ZTC eenvoudiger maken.
2. Het gebruik van de ZTC door vak-/taakspecifieke applicaties (TSA's) ongewijzigd te laten

[![Historiemodel Catalogi API ImZTC 2.2](catalogi_history.png)](catalogi_history.png "Historiemodel Catalogi API ImZTC versie 2.2 - klik voor groot")

## Theorie van het historiemodel

### Hoofdtypen en gerelateerde objecttypen

Het historiemodel kent de volgende uitgangspunten:

* Er bestaan drie hoofdtypen: 
	- Zaaktype
	- Informatieobjecttype
	- Besluittype  

	Deze drie hoofdtypen zijn in bovenstaande afbeelding weergegeven in de kleuren groen (Zaaktype met gerelateerde objecttypen), blauw (Informatieobjecttype) en rood (Besluittype).

* Elk hoofdtype kent een eigen lifecycle en kan onafhankelijk van de andere hoofdtypen doorontwikkeld worden. De uitzonderingen hierop zijn het aanmaken en beëindigen van het hoofdobjecttype.

* Elk hoofdtype kan één of meer gerelateerde objecttypen hebben. Dit zijn in feite groepsattributen en deze zijn hard, 1 op 1, gekoppeld aan een versie van het hoofdobjecttype. Bij wijzigingen van het hoofdobjecttype worden ook nieuwe versies van de gerelateerde objecttypen gemaakt en vice versa.

### Datumgeldigheid
Doordat versies van Zaaktype, Informatieobjecttype en Besluittype niet meer 1 op 1 aan elkaar gekoppeld zijn is het noodzakelijk te weten op welke datum de situatie van de gevraagde objecttypen en hun relaties getoond moeten worden. Met behulp van de (optionele) parameter datumGeldigheid kan de hele constellatie zoals geldig op die specifieke datum opgevraagd worden. Wanneer de datumGeldigheid niet expliciet meegegeven wordt geeft het antwoord de huidige constellatie, dus de situatie op het moment van aanroepen, weer.

Een versie van een Zaaktype, Informatieobjecttype of Besluittype kan ook opgevraagd worden door de identificatie (zaaktype.identificatie,
informatieobjecttype.omschrijving of besluittype.omschrijving) en de gewenste datumGeldigheid mee te geven. In situaties waarin wel de identificatie van een objecttype bekend is maar niet de exacte UUID of url is het dan toch mogelijk de correcte versie op te vragen.

De datumGeldigheid is vanuit de zaak geredeneerd de registratiedatum van de zaak.


### Gerelateerde objecttypen van Zaaktype
Bij een versie van een Zaaktype kan slechts één (1) versie van onderstaande gerelateerde objecttypen worden vastgelegd. 

Zaaktype kent de volgende gerelateerde objecttypen:
- Statustype
- Roltype
- Eigenschappen
- Zaakobjecttype
- ResultaatType
- ZaaktypeInformatieobjecttype


### Relatie Zaaktype heeft relevant Informatieobjecttype
- De relatie Zaaktype heeft relevant Informatieobjecttype wordt gelegd vanuit Zaaktype naar Informatieobjecttype.
- De relatie Zaaktype heeft relevant Informatieobjecttype wordt gelegd door in ZaaktypeInformatieobjecttype te verwijzen naar het zaaktype via zaaktype.url en naar het Informatieobjecttype via informatieobjecttype.omschrijving.
Op deze manier is aan één versie van een zaaktype versie-onafhankelijk een Informatieobjecttype gekoppeld. Bij een nieuwe versie van het Informatieobjecttype hoeft de relatie niet aangepast te worden. Het leggen of wijzigen 
(doorknippen) van de relatie is een wijziging (dus nieuwe versie) van het zaaktype en betekent ook een nieuwe versie van het zaakinformatieobjecttype.
- Bij het opvragen van een versie van een Zaaktype worden op basis van de datumGeldigheid de op dat moment geldige gerelateerde Informatieobjecttypen weergegeven.



### Relatie Zaaktype heeft relevant Besluittype
- De relatie Zaaktype heeft relevant Besluittype wordt gelegd vanuit Zaaktype naar Besluittype
- De relatie Zaaktype heeft relevant Besluittype wordt gelegd door in Zaaktype.besluittypen een array met Besluittype.omschrijving-en op te nemen. Idealiter zou de relatie gelegd worden met een relatieklasse zoals ZaaktypeInformatieobjecttype maar dat is helaas niet het geval. Ook hier is de relatie tussen (versie van een) Zaaktype en Besluittype onafhankelijk van de versie van het Besluittype.
- Bij het opvragen van een versie van een Zaaktype worden op basis van de datumGeldigheid de op dat moment geldige gerelateerde Besluittypen weergegeven.


### Is Catalogi API 1.3.x backwards compatible of niet
Op grond van bovenstaande beschrijvingen lijkt Catalogi API versie 1.3.x niet backwards compatible met versie 1.2.x. Voor een deel is dit zo. Namelijk de component waarmee de Zaaktype catalogus (ZTC) beheerd wordt
zal anders werken. Echter, omdat de ZTC beheercomponent een onderdeel is van het product ZTC is dit geen probleem. Immers, bij een nieuwe versie van een ZTC registercomponent hoort ook een nieuwe versie van de 
ZTC beheercomponent.

Consumer applicaties als taakspecifieke applicaties (TSA) of vakapplicaties kunnen nog steeds op de hun bekende wijze de ZTC raadplegen. Een TSA heeft immers alleen leesrechten op een ZTC, schrijven gebeurt alleen door de ZTC beheercomponent. Om de mogelijkheden van de laatste geïmplementeerde versie van de standaard ten volle te benutten is het noodzakelijk om de meest recente versie van de bij het registercomponent horende beheercomponent te gebruiken.

Grof gezegd zijn de GET operaties (GET Resource, GET List en HEAD) backwards compatible. De overige schrijf operaties (POST, PUT, PATCH, DELETE) zijn niet backwards compatible maar slechts door een beperkte set consumer applicaties te gebruiken.

Om deze redenen is besloten versie 1.3.x backwards compatible te laten zijn met eerdere versies. 

## Twee toepassingen van het historiemodel

### 1. Historiemodel toegepast op Zaaktype en Besluittype
[![Historiemodel Zaaktype en Besluittype](hm_zt_bt.jpg)](hm_zt_bt.jpg "Historiemodel Zaaktype en Besluittype - klik voor groot")

In dit voorbeeld is van een Zaaktype versie 1 [gepubliceerd](./index#concepten) op 1 januari 2023. Deze versie van het Zaaktype verwijst rechtstreeks via de Besluittype.omschrijving naar Besluittype versie 1. Op 1 januari 2024 wordt versie 2 van het Zaaktype gepubliceerd welke nog steeds via de Besluittype.omschrijving naar Besluittype versie 1 verwijst. 

Op 1 juli 2024 wordt versie 2 van het Besluittype gepubliceerd. Door de losse koppeling via Besluittype.omschrijving is het niet nodig om een nieuwe versie van het Zaaktype te maken. Op basis van de datumGeldigheid worden de juiste versies van het Zaaktype 
en Besluittype gecombineerd door de API.

###  2. Historiemodel toegepast op Zaaktype en Informatiemodeltype
[![Historiemodel Zaaktype en Informatieobjecttype](hm_zt_iot.jpg)](hm_zt_iot.jpg "Historiemodel Zaaktype en Informatieobjecttype - klik voor groot")

In dit voorbeeld is van een Zaaktype versie 1 [gepubliceerd](./index#concepten) op 1 januari 2023. Deze versie van het Zaaktype verwijst via Zaaktype-Informatieobjecttype versie 1 naar Informatieobjecttype versie 1. Op 1 januari 2024 wordt versie 2 van het Zaaktype gepubliceerd waardoor ook een nieuwe versie van het Zaaktype-Informatieobjecttype wordt gemaakt. Het Informatieobjecttype wordt niet gewijzigd dus Zaaktype-Informatieobjecttype versie 2 verwijst nog steeds naar Informatieobject versie 1. 

Op 1 juli 2024 worden versie 3 van het Zaaktype en bijbehorend Zaaktype-Informatieobjecttype gepubliceerd. Versie 1 van het Informatieobjecttype is nog steeds geldig. Wanneer op 1 augustus 2024  versie 2 van het Informatieobjecttype wordt gepubliceerd blijven versie 3 van het Zaaktype en Zaaktype-Informatieobjecttype geldig en hoeft hiervan geen nieuwe versie te worden gepubliceerd. Op basis van de datumGeldigheid worden de juiste versies van het Zaaktype en Informatieobjecttype gecombineerd door de API.

# Gedetailleerde API aanroepen

## Historiemodel toegepast op Zaaktype en Besluittype

###  Maak het besluittype "Besluittype A" versie 1 aan
`POST {{ztc_url}}/besluittypen`

Request:
```json
{
   	"omschrijving": "Besluittype A",
	"beginGeldigheid" : "2023-01-01",
	"toelichting": "Dit is versie 1 van Besluittype A",
   	...
}
```

Response:
```json
{
   	"url" : "{{ztc_url}}/besluittypen/{{uuid_besluittype_a_v1}}",
   	"omschrijving": "Besluitype A",
	"beginGeldigheid": "2023-01-01",
	"eindeGeldigheid": null,
	"toelichting": "Dit is versie 1 van Besluittype A",
	...
	"concept": true
}
```

### Publiceer het besluittype
`POST {{ztc_url}}/besluittypen/{{uuid_besluittype_a_v1}}/publish`

Response:
```json
{
   	"url" : "{{ztc_url}}/besluittypen/{{uuid_besluittype_a_v1}}",
   	"omschrijving": "Besluitype A",
	"beginGeldigheid": "2023-01-01",
	"eindeGeldigheid": null,
	"toelichting": "Dit is versie 1 van Besluittype A",
	...
	"concept": false
}
```

### Maak het zaaktype "Zaaktype_A" versie 1 aan en relateer het aan besluittype "Besluittype A"
`POST {{ztc_url}}/zaaktypen`

Request:
```json
{
	"identificatie": "Zaaktype_A",
	"beginGeldigheid": "2023-01-01",
	"toelichting": "Dit is versie 1 van Zaaktype_A",	
	...	
	"besluittypen": [ "Besluittype A" ],
	...
}
```

Response:
```json
{
	"url" : "{{ztc_url}}/zaaktypen/{{uuid_zaaktype_a_v1}}",
	"identificatie": "Zaaktype_A",
	"beginGeldigheid" : "2023-01-01",	
	"eindeGeldigheid": null,
	"toelichting": "Dit is versie 1 van Zaaktype_A",
	...
	"besluittypen" : [ "{{ztc_url}}/besluittypen/{{uuid_besluittype_a_v1}}" ],
	...
	"concept": true
}
```

### Publiceer het zaaktype
`POST {{ztc_url}}/zaaktypen/{{uuid_zaaktype_a_v1}}/publish`

Response:
```json
{
	"url" : "{{ztc_url}}/zaaktypen/{{uuid_zaaktype_a_v1}}",
	"identificatie": "Zaaktype_A",
	"beginGeldigheid" : "2023-01-01",
	"eindeGeldigheid": null,	
	"toelichting": "Dit is versie 1 van Zaaktype_A",
	...
	"besluittypen" : [ "{{ztc_url}}/besluittypen/{{uuid_besluittype_a_v1}}" ],
	...
	"concept": false
}
```

### Maak versie 2 van zaaktype "Zaaktype_A" aan en relateer het aan besluittype "Besluittype A"
`POST {{ztc_url}}/zaaktypen`

Request:
```json
{
	"identificatie": "Zaaktype_A",
	"beginGeldigheid": "2024-01-01",
	"toelichting": "Dit is versie 2 van Zaaktype_A",
	...	
	"besluittypen": [ "Besluittype A" ],
	...
}
```

Response:
```json
{
	"url" : "{{ztc_url}}/zaaktypen/{{uuid_zaaktype_a_v2}}",
	"identificatie": "Zaaktype_A",
	"beginGeldigheid" : "2024-01-01",	
	"eindeGeldigheid": null,
	"toelichting": "Dit is versie 2 van Zaaktype_A",
	...
	"besluittypen" : [ "{{ztc_url}}/besluittypen/{{uuid_besluittype_a_v1}}" ],
	...
	"concept": true
}
```

### Geef versie 1 van het zaaktype een eindegeldigheid

Er kunnen niet twee zaaktypen tegelijk geldig zijn. Dus we geven het oude zaaktype een eindegeldigheid van 1 dag voor de begingeldigheid van het nieuwe zaaktype.

`PATCH {{ztc_url}}/zaaktypen/{{uuid_zaaktype_a_v1}}`


Response:
```json
{
	"url" : "{{ztc_url}}/zaaktypen/{{uuid_zaaktype_a_v1}}",
	"identificatie": "Zaaktype_A",
	"beginGeldigheid": "2023-01-01",
	"eindeGeldigheid": "2023-12-31",
	...
	"besluittypen" : [ "{{ztc_url}}/besluittypen/{{uuid_besluittype_a_v1}}" ],
	...
	"concept": true
}
```


### Publiceer zaaktype versie v2
`POST {{ztc_url}}/zaaktypen/{{uuid_zaaktype_a_v2}}/publish`

Response:
```json
{
	"url" : "{{ztc_url}}/zaaktypen/{{uuid_zaaktype_a_v2}}",
	"identificatie": "Zaaktype_A",
	"beginGeldigheid" : "2024-01-01",	
	...
	"besluittypen" : [ "{{ztc_url}}/besluittypen/{{uuid_besluittype_a_v1}}" ],
	...
	"concept": false
}
```


###  Maak een concept besluittype v2 aan
`POST /besluittypen`

Request:
```json
{
   	"omschrijving": "Besluittype A",
	"beginGeldigheid" : "2024-07-01",
	"toelichting": "Dit is versie 2 van Besluittype A",
   	...
}
```

Response:
```json
{
   	"url" : "{{ztc_url}}/besluittypen/{{uuid_besluittype_a_v2}}",
   	"omschrijving": "Besluit genomen",
	"beginGeldigheid": "2024-07-01",
	"toelichting": "Dit is versie 2 van Besluittype A",
	...
	"concept": true
}
```

### Publiceer besluittype versie v2
`POST /besluittypen/besluit-genomen-v2/publish`

Response:
```json
{
   	"url" : "{{ztc_url}}/besluittypen/{{uuid_besluittype_a_v2}}",
   	"omschrijving": "Besluit genomen",
	"beginGeldigheid": "2024-07-01",
	"toelichting": "Dit is versie 2 van Besluittype A",
	...
	"concept": false
}
```

### Bevraag alle versies van zaaktype "Zaaktype_A"

`GET {{ztc_url}}/zaaktypen?identificatie=Zaaktype_A`

```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
		{
			"url" : "{{ztc_url}}/zaaktypen/{{uuid_zaaktype_a_v1}}",
			"identificatie": "Zaaktype_A",
			"beginGeldigheid": "2023-01-01",
			"eindeGeldigheid": "2023-12-31",
			"toelichting": "Dit is versie 1 van Zaaktype_A",
			...
			"besluittypen" : [ "{{ztc_url}}/besluittypen/{{uuid_besluittype_a_v1}}" ],
			...
			"concept": false
		},	
		{
			"url" : "{{ztc_url}}/zaaktypen/{{uuid_zaaktype_a_v2}}",
			"identificatie": "Zaaktype_A",
			"beginGeldigheid" : "2024-01-01",	
			"toelichting": "Dit is versie 2 van Zaaktype_A",
			...
			"besluittypen" : [ 
				"{{ztc_url}}/besluittypen/{{uuid_besluittype_a_v1}}",
				"{{ztc_url}}/besluittypen/{{uuid_besluittype_a_v2}}"
			],
			...
			"concept": false
		}
	]
}
```

###  Bevraag "Zaaktype_A" op 1-4-2024

`GET {{ztc_url}}/zaaktypen?identificatie=Zaaktype_A&datumGeldigheid=2024-04-01`

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
		{
			"url" : "{{ztc_url}}/zaaktypen/{{uuid_zaaktype_a_v2}}",
			"identificatie": "Zaaktype_A",
			"beginGeldigheid" : "2024-01-01",	
			"toelichting": "Dit is versie 2 van Zaaktype_A",
			...
			"besluittypen" : [ "{{ztc_url}}/besluittypen/{{uuid_besluittype_a_v1}}" ],
			...
			"concept": false
		}
	]
}
```


###  Bevraag "Zaaktype_A" op 1-10-2024 (na de creatie van de tweede versie van "Besluittype A" op 1-7-2024)
`GET {{ztc_url}}/zaaktypen?identificatie=Zaaktype_A?datumGeldigheid=2024-10-01`

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
		{
			"url" : "{{ztc_url}}/zaaktypen/{{uuid_zaaktype_a_v2}}",
			"identificatie": "Zaaktype_A",
			"beginGeldigheid" : "2024-01-01",	
			"toelichting": "Dit is versie 2 van Zaaktype_A",
			...
			"besluittypen" : [ "{{ztc_url}}/besluittypen/{{uuid_besluittype_a_v2}}" ],
			...
			"concept": false
		}
	]
}
```

In dit geval wordt versie v2 van het besluittype teruggegeven in plaats van versie v1.

To do:

- Uitzoeken of je in Oneground gepubliceerde zaaktypen kunt deleten. Nu kan ik geen identificatienamen zoals  "Zaaktype_A" hergebruiken. Bovendien kun je niet een scriptje opnieuw draaien (erg vervelend). Je wilt namelijk te tests kunnen opruimen automatisch.
- Uitzoeken of je typen kunt corrigeren. Ik heb die rechten blijkbaar niet.
- Nieuwe release Catalogi API is not niet mogelijk als er nog zoveel vragen zijn. Zie de uitstaande vraag naar Johannes in de email
- We kunnen Oneground of OpenZaak gebruiken als referentie-implementatie van onze testscripts en de gevallen mocken waar ze niet voldoen aan de standaard.
- We de betekenis van de velden: versiedatum, beginObject, eindObject.
- Bestudeer de issues over gevallen waarin eindGeldigheid < beginGeldigheid
- Gebruik expand voor leesbaarheid in de voorbeeld berichten. O nee helaas zit die nog niet in de ztc.
- Moet de eindgeldigheid van de vorige versie van het object niet worden aangepast als er een nieuwe versie van bijv. een zaaktype wordt aangemaakt?
- Want anders krijg je gaten in de aansluiting van geldigheden in de opeenvolgende versies. Je krijgt dan een lege gerelateerde.
- Kijk hoe versiedatum wordt gebruikt in de postman collectie van Johannes.
- Is het de bedoeling dat er gaten kunnen zitten in de geldigheidsperioden?
- Johannes heeft een ander beeld bij één van de diagrammen. Dit moet opgelost worden
- Expand toevoegen aan deze voorbeeldberichten voor de duidelijkheid!
















