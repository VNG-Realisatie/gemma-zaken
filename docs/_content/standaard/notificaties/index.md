---
title: "Notificaties API"
date: '10-7-2019'
weight: 10
---

Notificaties API voor het routeren van notificaties.

Dit component dient gebruikt te worden om notificaties te routeren tussen
andere componenten.

De API ondersteunt:

* het aanmaken van 'kanalen', waarop producers berichten publiceren
* het aanmaken van abonnementen voor consumers, via het webhook mechanisme
* het ontvangen en routeren van berichten


## Gegevensmodel

[![Gegevensmodel Notificaties API](Notificaties API.png){:width="1200px"}](Notificaties API.png "Notificaties gegevensmodel - klik voor groot")


## Specificatie van de Notificaties API

* [Referentie-implementatie Notificaties API](https://notificaties-api.vng.cloud)
* API specificatie (OAS3) in
  [ReDoc](https://notificaties-api.vng.cloud/api/v1/schema/),
  [Swagger](https://petstore.swagger.io/?url=https://notificaties-api.vng.cloud/api/v1/schema/openapi.yaml),
  [YAML](https://notificaties-api.vng.cloud/api/v1/schema/openapi.yaml) of
  [JSON](https://notificaties-api.vng.cloud/api/v1/schema/openapi.json)


## Specificatie van gedrag

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

## Betrouwbaarheidsgaranties ("reliability" niveau)

Het Pub/Sub karakter van de notificaties API kent een aantal faalmogelijheden:

* de notificaties API kan zelf niet bereikbaar zijn
* de ontvanger van notificaties kan (tijdelijk) niet bereikbaar zijn
* de verzender van notificaties kan een defect hebben waardoor een operatie wel
  doorgevoerd wordt, maar de notificatie niet verstuurd wordt

In alle gevallen is er dus informatieverlies.

Elke schakel in deze keten ZOU de maximale inspanning MOETEN doen om geen
berichten verloren te laten gaan. Consumers MOETEN er tegelijkertijd ook van
uit gaan dat een bericht verloren kan gaan. Applicaties die heel afhankelijk
zijn van notificaties zouden dan ook moeten een backup-mechanisme voorzien,
zoals bijvoorbeeld periodiek pollen van data bij een provider.

Er zijn een aantal suggesties om de reliability te verhogen:

* voer API operaties uit in een database transactie, waarbij de notificatie
  onderdeel is van de transactie. Indien het niet lukt om de notificatie te
  versturen, dan wordt de transactie teruggerold.
* toepassen van een retry-mechanisme: indien een notificatie niet verstuurd of
  afgeleverd kan worden, dan kan dit opnieuw geprobeerd worden, eventueel met
  exponentiële back-off
* maak gebruik van redundante structuur. De referentie-implementatie wordt
  gehost in een kubernetes-cluster met redundantie. Als een _pod_ crasht, dan
  zijn er nog 2 andere _pods_ die notificaties kunnen ontvangen en versturen.
  Updates worden als _rolling release_ uitgevoerd, waardoor je heel dicht bij
  100% availability komt
* pas een buffer toe voor notificaties als ontvanger - indien je applicatie
  niet beschikbaar is, dan kan je nog steeds de notificaties ontvangen en later
  afhandelen als de applicatie weer online is

We eisen deze maatregelen dus niet in de specificatie.


## Overige documentatie

* [Tutorial Notificeren](../../ontwikkelaars/handleidingen-en-tutorials/notificeren)
