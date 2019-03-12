---
title: "Notificaties (concept)"
date: '11-03-2019'
weight: 70
---

Een component moet een bericht kunnen sturen die andere componenten kunnen
ontvangen zodat zij hierop kunnen acteren indien dit een interesant bericht is
voor het betreffende ontvangende component.

## Uitgangspunten

**Notificatie als REST API component**

Er wordt een notificatiecomponent ontwikkeld met de functionaliteiten:

1. registreren van abonnees (=componenten die berichten willen ontvangen)
2. ontvangen van berichten die gerouteerd moeten worden
3. distribueren van berichten naar de abonnees

Taken 1 en 2 worden sowieso via een REST API ontsloten.

De derde taak wordt via webhooks ingevuld, waarbij we als webhook begrijpen:

> Een endpoint/url bij een abonnee die voor de NC bereikbaar is waarnaar de
> berichten gestuurd kunnen worden. De component acteert op deze berichten.
> Van de webhook wordt verwacht dat het bericht correct ontvangen is als die
> met een HTTP 200 status antwoordt.

We onderkennen dat voor taak 3 een meer gespecialiseerd protocol als AMQP
ook geschikt kan zijn. Als MVP kiezen we echter voor webhooks.

**Technologie onafhankelijk**

De hierboven genoemde REST API wordt een "standaard". Welke onderliggende
technologie echt gebruikt wordt maakt niet zo veel uit.

Wij gebruiken waarschijnlijk de Pub/Sub-functionaliteit in
[RabbitMQ](https://www.rabbitmq.com/).

**Topics**

Topics zijn kanalen waar berichten op binnenkomen en consumers zich kunnen op
abonneren. Voorlopig definieren we voor elke API een eigen topic. Alles wat
gebeurt in de Zaken API, komt op topic `zaken`, dus ook `zaakdocument` en
`status` wijzigingen.

Componenten produceren berichten op een bepaald topic - deze producers worden
door Squad Architectuur "bronnen" genoemd. Een ZRC, DRC, BRC zijn de voor de
hand liggende bronnen binnen zaakgericht werken.

**Relevantie van een notificatie bepalen**

De last van het bepalen of een notificatie, bijvoorbeeld van een zaakwijziging
of het aanmaken van een zaak, relevant is, ligt bij de consumer. De consumer
dient op basis van de notificatie te bepalen of het initieel relevant is
(bijvoorbeeld het Zaaktype), de details op te halen en vervolgens daadwerkelijk
te bepalen of deze notificatie tot een actie leidt.

We houden in gedachten dat bij het registreren van de webhook later mogelijk
een feature komt om alvast 'filters' op te geven zodat irrelevante berichten
niet eens afgeleverd worden.

**Er komt een generieke API voor het ontvangen van notificaties**

Het ontvangen van berichten op de webhook-url zal generiek geimplementeerd
worden in onze componenten. De vorm van het bericht zal gestandaardiseerd zijn.

De precieze urls/endpoints zijn niet relevant, aangezien de consumer deze
expliciet zelf registreert.

## Notificatie

Naast alle API-specificaties voor het beheren van abonnementen en bronnen is
de kern van het verhaal de notificatie zelf. Alle attributen en attribuutnamen
onder voorbehoud.

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

**LET OP: Vooruitlopend op tijdreizen - De URL moet een
`?tijdstempel=<tijd en datum>` meekrijgen zodat niet de actuele versie van de
`Zaak` geeft maar de versie die echt hoort bij het bericht. Verder is er de
wens om het "verschil" van voor en na de wijziging mee te geven in de
notificatie of op te vragen.**

### Kenmerken

Elk component kan `kenmerken` definieren die helpen bij het filteren van
relevante informatie.

**Zaken**

Kenmerk | Omschrijving
--- | ---
zaaktype | Voor de `Zaken` API, de betreffende ZaakType URL.

## Demo applicatie

De demo applicatie zal gebruikt worden om notificaties te tonen zonder hier op
te acteren.

[Voorbeeld sequence diagram (high-level)](http://sequencediagram.org/index.html#initialData=C4S2BsFMAIDkHtQDMQGNICdIDsBQuBDVYeDaAIQFcMBzTXABwI1FRCe2GgFkB5AJQC0BBg0bNW7Apx4DBAIyIBrHABNxLNFM40M8Sg2gBicCBoALYLsg5oAKjsAtAOIB1aAGdU8BpAcbJDi4EYBRUAlAYAGF4AFsGeGwcYACtIOhHfijcNWhcPiFFVBVsVUEAPhCwiJBouISkzgAuaABlSnkvDBB5GB9oEgY0DIIS-ABecYBJbDAQAlMPGpgAN2l7OwKFZTUHaAIkOj1SyfwqWkwKrZEGJucbJGgEj2BvVT6xa9EruSKS1SaAAV4C83qt1ucjhNxgBBaTYAixGB0VQEdaorgOSGYPYALxAACtsE8Qa94O9oOYHlwfHQ6CscKdcJkohUqmhltAYvFEskWo40UpoNhECBqpEWq1gBFKB5oAYMZBcOzwpEufVeZwfoUdqV+YLhaLxbVJdLgLL5QxFfgRcA+gyyFs-mp9aMACoAT180BAcoKAH58r9dWVyiyWgAJNHgEajaDvaUgcBynzMrKCbXbYou2NChMEJMeG2Ie2YWQ67N63M+4l0eC6A6+1DmaB0eS1VQAHWwa2JzzJFPk1COgadIYq4egUYWbTNFtTLIz5THlYBs5lcvzheLdug8Ad5az-1NG8tiu7IE4mEgHiWMhW8FIFGHmFHwdXmZuLXImDQlj3B4CnGl7dvKADuJKguSyKQO2kDqEAA).

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

[Voorbeeld sequence diagram (in-depth)](http://sequencediagram.org/index.html#initialData=C4S2BsFMAIDkHtQDMQGNICdIDsBQuAHAQw1FRGO2GgC0AlAYUJLIqKrkRBVSNBgbwAtgXjYcwZqTRsOdIgCMFYALIBFKa0rUAIo3z0GAWgB8CZGj4gBw0eKoAuaAAUA8gGUAKtAD0RAiA+AG4AjD4KGGL2ADrYPj4ADADMAEwhRgBeRADWOPG45tyW-NCCImISpvJKqmpODFh8MMDwAaix8clpmTl5PgVcPFY25fbAADxGRtXKwOpOAJI6TiEpSbiGk0aFQyVldhJOABKens7QKQkhHT4AQpHY0ADmmJBPIADOwFiYACbQQkg1CWKzW+VwAF4IQtsGAQERwJ9htAguxoAAqdGGTHQIhIF4PX5Q-B6YxmQbFaylWwVRwuDzePwBYJhRRRSCAqg4G5ddJZXJxfo7SkjA5UKqKWbzaDuACuCg+qAwIAUMFJ0BaGtaaB5qT5vUFAwsvD2NLGWxmtScrgA0rhSVthSaqftacBjqdzpdroKAIIKdmc6hEdgvIQh7LAcFQmFwhFIkqox6Y0k4vEEsREiEGRimJ3I11jJxuLy+fyBULhB72HyrJI+bAU52QD43W6YNAAC0k+dNo0qJktczqLkiv1l6ABLY+RBeWugIOgdaNRWb1P7VAtkqt0FtG0YjqbBbNh2gJzOFwSCRuADV4OAWvAQL98kP1KYTKTiwyy8zK43jWGD4fDEYAkxebA2w7VBu3yIA)

### Abonneren

Een consumer abonneert zich op notificaties door de volgende request naar de
NC te sturen:

```http
POST /api/v1/abonnementen

Authorization: Bearer abcdef1234
Content-Type: application/json

{
    "callbackUrl": "https://ref.tst.vng.cloud/zrc/api/v1/callbacks",
    "auth": "Bearer aef34gh...",
    "kanalen": [
        "zaken",
        "informatieobjecten"
    ]
}
```

Het `DELETE`n, `PATCH` en `PUT` op individuele subscribers moet mogelijk zijn.

Details moeten ook opgevraagd kunnen worden, met uitzondering van de `auth`
gegevens.

Filter parameter(s) op `kanelen` zijn handig.

### Kanalen beheren

Een kanaal is het equivalent van een exchange in RabbitMQ.

Kanalen worden aangemaakt door producers (bronnen), en zijn gekarakteriseerd
door een unieke naam.

```http
POST /api/v1/kanalen

Authorization: Bearer abcdef1234
Content-Type: application/json

{
    "naam": "zaken"
}
```

Een kanaal mag slechts eenmalig aangemaakt worden.

Daarnaast moet het ophalen van kanalen mogelijk zijn, zodat consumers kunnen
zien waarop ze zich kunnen abonneren.

### Notificaties insturen

De NC moet notificaties kunnen ontvangen:

```http
POST /api/v1/notificaties

Authorization: Bearer abcdef1234
Content-Type: application/json

{
    "kanaal": "zaken",
    "bronUrl": "https://ref.tst.vng.cloud/zrc/api/v1/zaken/d7a22",
    "resource": "status",
    "resourceUrl": "https://ref.tst.vng.cloud/zrc/api/v1/statussen/d7a22/721c9",
    "actie": "create",
    "aanmaakDatum": "2018-01-01T17:00:00Z",
    "kenmerken": [
        {"bron": "082096752011"},
        {"zaaktype": "https://example.com/api/v1/zaaktypen/5aa5c"},
        {"vertrouwelijkeidaanduiding": "openbaar"}
    ]
}

```

Onder water worden de kenmerken in een bepaald formaat gebruikt voor topics,
zodat consumers deze eenvoudiger kunnen filteren.

Merk op dat de kenmerken als `Array` opgebouwd worden. Dit is omdat _Object keys_
in JSON geen inherente volgorde hebben, en de volgorde wel belangrijk is
voor interne doeleinden.


### Notificaties ophalen

In eerste instantie zetten we enkel in op push via webhooks. Later laten we toe
om ook notificaties te pullen.

```http
GET /api/v1/subscribers/ae54ef/notificaties

Authorization: Bearer abcdef1234
Accept: application/json

[{
    "kanaal": "zaken",
    "bericht": {
        "bronUrl": "https://ref.tst.vng.cloud/zrc/api/v1/zaken/d7a22",
        "resource": "status",
        "resourceUrl": "https://ref.tst.vng.cloud/zrc/api/v1/statussen/d7a22/721c9",
        "actie": "create",
        "aanmaakDatum": "2018-01-01T17:00:00Z",
        "kenmerken": [
            {"bron": "082096752011"},
            {"zaaktype": "https://example.com/api/v1/zaaktypen/5aa5c"},
            {"vertrouwelijkeidaanduiding": "openbaar"}
        ]
    }
}]
```

Dit zal enkel de ongelezen notificaties teruggeven.

# Uitdagingen en oplossingen

## AMQP vs. webhooks: volgorde events

Een van de grote voordelen van direct op AMQP in te haken is dat het protocol
oplossingen voorziet om te garanderen dat berichten in de juiste volgorde
aankomen.

In het scenario dat er bijvoorbeeld twee snelle statusupdates zijn van:

1. Aangemaakt naar
2. In behandeling naar
3. Afgerond

Als je geen AMQP gebruikt, kan het zijn dat door de intrinsieke aard van TCP/HTTP statusupdate 3
voor 2 afgeleverd wordt op de webhook, door latency op de eerste call
bijvoorbeeld.

Dit zou kunnen leiden tot een incorrecte statusupdate via push bij clients.

We verwachten dat dit geen probleem wordt, omdat de inhoud van de wijziging
niet in de notificatie opgenomen is, maar enkel de kennisgeving dat _iets_
gebeurd is, en het is aan de consumer om de nieuwe state van de betrokken
resource(s) te bevragen. Dit betekent ook dat snelle, opeenvolgende
notificaties in principe kunnen geconsolideerd worden (orde van <1s).

## AMQP vs. webhooks: garantie dat een bericht afgeleverd wordt

AMQP voorziet ook in de garantie dat messages bezorgd worden als een node
(tijdelijk) onbereikbaar is en later weer online komt. Dit kan het geval zijn
tijdens deployments bijvoorbeeld, of een onverwachte outage.

Met webhooks kan de HTTP statuscode bij het afleveren gecontroleerd worden.
Indien de consumer niet antwoordt met een HTTP 200 status, dan kan het bericht
gemarkeerd worden als 'niet-afgeleverd', en kan er opnieuw geprobeerd worden
(met exponential backoff). Ook kan de NC een interface bieden om events te
re-senden.

Door de aard van de berichten (enkel kennisgeving _dat_ er een event is, niet
_wat_ de inhoud is), informeert dit ook de client om data te re-fetchen, en
is het risico op kwalijke gevolgen van vertraagde berichten beperkt.

## Bijhouden van berichten

Berichten worden in principe niet bewaard in de NC. Ontvangen notifications
worden meteen doorgezet.

Een uitzondering hierop is het bewaren van berichten om ze opnieuw te kunnen
versturen indien aflevering niet gelukt is - deze moeten opnieuw gescheduled
worden voor aflevering. Hierbij moet het mogelijk zijn om te configureren
hoe vaak een bericht moet/mag geretried worden, en hoe de retry back-off
eruit ziet.
