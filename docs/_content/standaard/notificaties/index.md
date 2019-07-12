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

![Gegevensmodel Notificaties API](Notificaties API.png){:width="1200px"}


## Specificatie van de Notificaties API

[Referentie-implementatie Notificaties API](https://notificaties-api.vng.cloud)

[Plain text OAS3 specificatie](../../../api-specificatie/nrc/openapi.yaml)


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


## Overige documentatie

* [Tutorial Notificeren](../../ontwikkelaars/tutorials/notificeren)


