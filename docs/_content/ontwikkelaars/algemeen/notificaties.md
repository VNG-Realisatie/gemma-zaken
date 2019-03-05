---
title: "Notificaties (concept)"
date: '25-02-2019'
weight: 70
---

Een component moet een bericht kunnen sturen die andere componenten kunnen ontvangen zodat zij hierop kunnen acteren indien dit een interesant bericht is voor het betreffende ontvangende component.

## Uitgangspunten

**Notificatie als REST API component**

Er wordt een notificatiecomponent ontwikkeld dat zorgt voor het routeren van
berichten. Dit kan een bestaand product zijn met een eigen REST API er voor om 
product specifieke eigenschappen te abstraheren.

Als inspiratie wordt [Google Cloud Pub/Sub API](https://cloud.google.com/pubsub/docs/reference/rest/)
gebruikt.

**Technologie onafhankelijk**

De hierboven genoemde REST API wordt een "standaard". Welke onderliggende
technologie echt gebruikt wordt maakt niet zo veel uit. Wij gebruiken voor nu
de Pub/Sub-functionaliteit in [RabbitMQ](https://www.rabbitmq.com/)

**Topics**

Topics zijn kanalen waar berichten op binnenkomen. Voorlopig definieren we voor
elke API een eigen topic. Alles wat gebeurt in de Zaken API, komt op Topic `Zaken`, dus ook
`ZaakDocument` en `Status` wijzigingen. Voor zover we nu kunnen zien wil Squad
Architectuur dit "bronnen" noemen.

**Relevantie van een notificatie bepalen**

De last van het bepalen of een notificatie, bijvoorbeeld van een Zaak wijziging of het aanmaken van een Zaak,
relevant is, ligt bij de consumer. De consumer dient op basis van de notificatie te bepalen of het initieel relevant is (bijvoorbeeld het Zaaktype), de details op te halen en vervolgens daadwerkelijk te bepalen of deze notificatie tot een actie leidt.

**Er komt een generieke API voor het ontvangen van notificaties**

Er komt een aparte API die naast elke component geimplementeerd kan worden. Het ontvangen van notificaties wordt dus geen onderdeel van de API van het component zelf. Dit zorgt voor meer flexibiliteit.
Echter, de API interface is wel generiek, dus hij kan voor elk component op dezelfde wijze geimplementeerd worden. Hij kan zelfs de ontvanger zijn van meer dan 1 component door in meerdere abonnementen naar 1 "push" endpoint te verwijzen.

## Notificatie

Naast alle API-specificaties voor het beheren van abonnementen en bronnen is de kern
van het verhaal de notificatie zelf. Alle attributen en attribuutnamen onder voorbehoud.

Attribuut | Omschrijving
--- | ---
id | Unieke identificatie van het bericht
bron.rsin | Het RSIN van de versturende organisatie.
bron.naam | De naam van de bron.
bericht.bronUrl | De URL van de resource behorend bij de bron (bijv. `Zaak`) van de actuele resource (omdat we nog geen historie hebben)
bericht.resource | Naam van de daadwerkelijk resource die is gewijzigd (bijv. `Status`)
bericht.resourceUrl | De URL van de daadwerkelijk resource (optioneel)
bericht.actie | Typisch OAS-variant van de HTTP methode die is gebruikt voor het wijzigen (`update`, `delete`, `create`) maar dit kan ook een ander soort actie zijn. De acties worden per API-component vastgelegd in de standaard.
bericht.aanmaakDatum | Datum en tijd van gebeurtenis
bericht.kenmerken | Een object waar arbitraire gegevens toegoevoegd kunnen worden. Deze gegevens worden echter vastgelegd per component in de standaard.

**LET OP: Vooruitlopend op tijdreizen - De URL moet een `?tijdstempel=<tijd en datum>` meekrijgen zodat niet de actuele versie van de `Zaak` geeft maar de versie die echt hoort bij het bericht. Verder is er de wens om het "verschil" van voor en na de wijziging mee te geven in de notificatie of op te vragen.**

### Kenmerken

Elk component kan `kenmerken` definieren die helpen bij het filteren van relevante informatie.

**Zaken**

Kenmerk | Omschrijving
--- | ---
zaaktype | Voor de `Zaken` API, de betreffende ZaakType URL.

## Demo applicatie

De demo applicatie zal gebruikt worden om notificaties te tonen zonder hier op te acteren.

[Voorbeeld sequence diagram](http://sequencediagram.org/index.html#initialData=C4S2BsFMAIDkHtQDMQGNICdIDsBQuBDVYeDaAIQFcMBzTXABwI1FRCe2GgFkB5AJQC0BBg0bNW7Apx4DBAIyIBrHABNxLNFM40M8Sg2gBicCBoALYLsg5oAKjsAtAOIB1aAGdU8BpAcbJDi4EYBRUAlAYAGF4AFsGeGwcYACtIOhHfijcNWhcPiFFVBVsVUEAPhCwiJBouISkzgAuaABlSnkvDBB5GB9oEgY0DIIS-ABecYBJbDAQAlMPGpgAN2l7OwKFZTUHaAIkOj1SyfwqWkwKrZEGJucbJGgEj2BvVT6xa9EruSKS1SaAAV4C83qt1ucjhNxgBBaTYAixGB0VQEdaorgOSGYPYALxAACtsE8Qa94O9oOYHlwfHQ6CscKdcJkohUqmhltAYvFEskWo40UpoNhECBqpEWq1gBFKB5oAYMZBcOzwpEufVeZwfoUdqV+YLhaLxbVJdLgLL5QxFfgRcA+gyyFs-mp9aMACoAT180BAcoKAH58r9dWVyiyWgAJNHgEajaDvaUgcBynzMrKCbXbYou2NChMEJMeG2Ie2YWQ67N63M+4l0eC6A6+1DmaB0eS1VQAHWwa2JzzJFPk1COgadIYq4egUYWbTNFtTLIz5THlYBs5lcvzheLdug8Ad5az-1NG8tiu7IE4mEgHiWMhW8FIFGHmFHwdXmZuLXImDQlj3B4CnGl7dvKADuJKguSyKQO2kDqEAA).

## Notificaties bij andere standaarden
Zowel bij Regie- en Zaakservices als bij DigiLevering wordt notificaties opgelost met een publish/subscribe mechanisme. Een centrale notificatiecomponent ontvangt gebeurtenissen en distribueert deze naar abonnees. Abonnees hebben de mogelijkheid zich te abonneren op bepaalde gebeurtenissen. Bij DigiLevering zijn gebeurtenissen gedefinieerd in termen van objecttypen en attributen en kunnen bovendien filters worden gedefinieerd op attributen van de objecten.

Bij Regie- en Zaakservices kunnen alleen notificaties op zaakniveau worden gestuurd, d.w.z. als een zaak wordt gecreeerd of gewijzigd. De volgende gegevens moeten worden opgenomen in het notificatie-bericht :

* Zaakidentificatie
* Zaaktype
* Zaakstatus (optioneel)

Ideeen en attributen die andere standaarden gebruiken worden bekeken!

Bronnen:

* [Digilevering koppelvlakspecificatie](https://www.logius.nl/sites/default/files/public/bestanden/diensten/DigiLevering/Koppelvlakspecificatie.pdf)
* [Digilevering documentatie](https://www.logius.nl/diensten/digilevering/documentatie)
* [Regie- en Zaakservices specificaties](https://www.gemmaonline.nl/images/gemmaonline/c/cd/Koppelvlakspecificatie_Regie-zaak_services_v1.0.pdf)

# API specificatie (concept)

## Notificatie API specificatie

Wanneer een abonnement wordt aangemaakt, gelden de volgende vereisten:

1. Berichten dienen 7 dagen bewaard te blijven (`messageRetentionDuration=604800`)
2. Abonnementen dienen actief te blijven voor 31 dagen bij geen activiteit (`expirationPolicy.ttl=2678400`)
3. Abonnementen mogen worden opgezegd als het pushUrl 7 dagen of langer niet bereikbaar is geweest.
4. Opgehaalde berichten mogen niet meer dan 1x worden opgehaald (pull) of worden afgeleverd (push). Oude berichten worden dus verwijderd (`retainAckedMessages=false`)

### Bronnen (topics) beheren

Ondersteuning voor: GET (``list`` en ``retrieve``), POST, DELETE

**/api/v1/bronnen[/{id}]**
```javascript
{
  "url": "https://example.com/api/v1/bronnen/9b441a" // Alleen-lezen
  "id": "9b441a",
  "rsin": "082096752011",
  "naam": "zaken"
}
```

*Gebaseerd op Google Cloud Pub/Sub*

projects.topics.create/delete/get/list

### Abonnementen (subscriptions)

Ondersteuning voor: GET (``list`` en ``retrieve``), POST, PUT, PATCH en DELETE

**/api/v1/abonnementen[/{id}]**
```javascript
{
  "url": "https://example.com/api/v1/api/v1/abonnementen/761a81", // Alleen-lezen
  "id": "761a81", // Alleen-lezen, eventueel een UUID als onderliggende techniek dit toestaat
  "bron": {  // De "bron" vorm het topic: <rsin>-<naam>
    "rsin": "082096752011",
    "naam": "zaken"
  },
  "versturenNaar": "https://example.com/api/v1/notificaties/ontvangen"  // Optioneel
}
```

TODO: Waarom bron als rsin+naam en geen URL naar bron?

*Gebaseerd op Google Cloud Pub/Sub*

projects.subscriptions.create/get/list/delete/patch
- id = name
- '{rsin}-{bronNaam}' = topic
- versturenNaar = pushConfig.pushEndpoint

### Abonnementen bij een bron opvragen

Ondersteuning voor: GET (``list``)

**/api/v1/bronnen/{id}/abonnementen**
```javascript
[
  {
    "url": "https://example.com/api/v1/api/v1/abonnementen/761a81", // Alleen-lezen
    "id": "761a81", // Alleen-lezen, eventueel een UUID als onderliggende techniek dit toestaat
    "bron": {  // De "bron" vorm het topic: <rsin>-<naam>
      "rsin": "082096752011",
      "naam": "zaken"
    },
    "versturenNaar": "https://example.com/api/v1/notificaties/ontvangen"  // Optioneel
  }
]
```

*Gebaseerd op Google Cloud Pub/Sub*

projects.topics.subscribers.list

### Notificaties versturen

Ondersteuning voor: POST

**/api/v1/bronnen/{id}/notificaties**
```javascript
{
  "bronUrl": "https://example.com/api/v1/zaken/d7a22"
  "resource": "status",
  "resourceUrl": "https://example.com/api/v1/statussen/721c9",
  "actie": "create",  // "create", "update", etc. niet "read" of "list" want dat is geen verandering)
  "aanmaakDatum": "2018-01-01T17:00:00Z",
  "kenmerken": {
    "zaaktype": "https://example.com/api/v1/zaaktypen/5aa5c"
  }
}
```

*Gebaseerd op Google Cloud Pub/Sub*

projects.topics.publish

### Notificaties ophalen (pull)

Ondersteuning voor: GET (``list``)

**/api/v1/abonnementen/{id}/notificaties**
```javascript
[
  {
    "id": "3aa9c5",
    "bron": {
      "rsin": "082096752011",
      "naam": "zaken"
    }
    "bericht": {
      "bronUrl": "https://example.com/api/v1/zaken/d7a22"
      "resource": "status",
      "resourceUrl": "https://example.com/api/v1/statussen/721c9",
      "actie": "create",  // "create", "update", etc. niet "read" of "list" want dat is geen verandering)
      "aanmaakDatum": "2018-01-01T17:00:00Z",
      "kenmerken": {
        "zaaktype": "https://example.com/api/v1/zaaktypen/5aa5c"
      }
    }
  }
]
```

*Gebaseerd op Google Cloud Pub/Sub*

projects.subscriptions.pull
- id = messageId
- aanmaakDatum = publishTime
- other attributes = data
- kenmerken = attributes

Also, automatically ACK messages, by calling subscribtions/acknowledge after the notifications are pulled.
And, `returnImmediately=True`. For now, no streaming.

## Notificatie ontvanger (push) API specificatie

Als bij een abonnement de `verstuurNaar` is opgegeven, worden notificaties "gepushed" naar dit endpoint. De ontvanger moet de volgende API hebben geimplementeerd.

Ondersteuning voor: POST

**/api/v1/notificaties/ontvangen**

Zie: [Notificaties ophalen (pull)](#notificaties-ophalen-pull) voor de specificatie.
