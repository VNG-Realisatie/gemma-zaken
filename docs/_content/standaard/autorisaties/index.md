---
title: "Autorisaties API"
date: '10-7-2019'
weight: 10
---

API voor het beheren van autorisaties

Deze API laat toe om autorisaties van een (taak)applicatie te beheren en uit
te lezen.

De API ondersteunt de volgende operaties:

* Het toevoegen of wijzigen van een applicatie met client ids en van toegestane scopes
* Het ophalen van de toegestane scopes bij een bepaald client id
* Het verwijderen van een applicatie


## Gegevensmodel

![Gegevensmodel Autorisaties API](Autorisaties API.png)


## Specificatie van de Autorisaties API

[Referentie-implementatie Autorisaties API](https://autorisaties-api.vng.cloud)

[Plain text OAS3 specificatie](../../../api-specificatie/ac/openapi.yaml)


## Specificatie van gedrag


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


## Overige documentatie

* [Tutorial autorisatie](../../ontwikkelaars/handleidingen-en-tutorials/_assets/autorisatie.pptx)
