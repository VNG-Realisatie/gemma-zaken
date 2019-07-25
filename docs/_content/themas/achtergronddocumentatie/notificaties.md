---
title: "Notificaties"
date: '11-03-2019'
weight: 70
---

Een component moet een bericht kunnen sturen die andere componenten kunnen
ontvangen zodat zij hierop kunnen acteren indien dit een interessant bericht is
voor het betreffende ontvangende component.

## Uitgangspunten

**Notificatie als REST API component**

Er wordt een notificatiecomponent (NC) ontwikkeld met de functionaliteiten:

1. registreren van abonnees (=componenten of applicaties die berichten willen
   ontvangen)
2. ontvangen van berichten die gerouteerd moeten worden
3. distribueren van berichten naar de abonnees

Taken 1 en 2 worden sowieso via een REST API ontsloten.

De derde taak wordt via webhooks ingevuld, waarbij we als webhook begrijpen:

> Een endpoint/url bij een abonnee die voor de NC bereikbaar is waarnaar de
> berichten gestuurd kunnen worden. De component acteert op deze berichten.
> Van de webhook wordt verwacht dat het bericht correct ontvangen is als die
> met een HTTP 200 status antwoordt.

We onderkennen dat voor voor deze taken een meer gespecialiseerd protocol als
AMQP wellicht beter geschikt is maar wel met zijn eigen uitdagingen komt (zie
ook onderaan).

**Technologie onafhankelijk**

De hierboven genoemde REST API wordt een "standaard". Welke onderliggende
technologie echt gebruikt wordt maakt niet zo veel uit.

Wij gebruiken (waarschijnlijk) onderliggend de Pub/Sub-functionaliteit in
[RabbitMQ](https://www.rabbitmq.com/) met behulp van Topics.

**Kanalen**

Berichten worden verstuurd via bepaalde kanalen (Exchange in AMQP). Consumers
kunnen zich op zo'n kanaal abonneren, aangevuld met bepaalde filters (Topics in
AMQP). Elk component krijgt zijn eigen kanaal.

Ter illustratie: De Zaken API publiceert alles op het kanaal `zaken`. Een zaak
of status wijziging wordt hierop gepubliceerd. Ook als een document wordt
toegevoegd wordt het aanmaken van de relatie tusen de zaak en het document
gepubliceerd op dit kanaal.

Componenten produceren dus berichten op een bepaald kanaal - ook wel "bronnen" genoemd. Een ZRC, DRC, BRC zijn de voor de hand liggende bronnen binnen zaakgericht werken.

**Relevantie van een notificatie bepalen**

Een abonnement op een kanaal kan gepaard gaan met bepaalde filters. Deze
filters zorgen er voor dat de consumer bepaalde notificaties niet doorgegeven
krijgt omdat ze niet voldoen aan het opgegeven filter. Hiermee kan een overdaad
aan irrelevante berichten worden voorkomen.

De vervolg-last van het bepalen of een notificatie, bijvoorbeeld van een
zaakwijziging of het aanmaken van een zaak, relevant is, ligt bij de consumer.
De consumer dient op basis van de notificatie te bepalen of het initieel
relevant is (bijvoorbeeld het Zaaktype), de details op te halen en vervolgens
daadwerkelijk te bepalen of deze notificatie tot een actie leidt.

**Er komt een generieke API voor het ontvangen van notificaties**

Om berichten te kunnen ontvangen, zal elke consumer een beperkte API
specificatie moeten implementeren, beschikbaar op de webhook-url.

Het ontvangen van berichten op de webhook-url zal generiek geimplementeerd
worden in de ZGW componenten. Ook de vorm van het bericht zal gestandaardiseerd
zijn. Bij het aanmaken van een abonnement dient de webhook-url (`callbackUrl`
genaamd in de API specificatie) opgegeven te worden waardoor de precieze URL
niet verder gestandardiseerd wordt.

## Notificatie bericht specificatie

Naast alle API-specificaties voor het beheren van abonnementen en bronnen is
de kern van het verhaal de notificatie zelf. Alle attributen en attribuutnamen
onder voorbehoud.

Attribuut | Omschrijving
--- | ---
kanaal | De naam van het kanaal (Exchange in AMQP) behorend bij de bron. (bijv. `zaken`, `documenten`, `besluiten`, etc.)
hoofdObject | De URL van de resource behorend bij het kanaal (bijv. `Zaak`) van de actuele resource (omdat we nog geen historie hebben)
resource | Naam van de daadwerkelijk resource die is gewijzigd (bijv. `Status`)
resourceUrl | De URL van de daadwerkelijk resource (optioneel)
actie | De actie die de gebeurtenis op abstract niveau omschrijft. Dit is een vaste lijst bestaande uit `gewijzigd`, `verwijderd`, `aangemaakt` eventueel aangevuld met additionele waarden, die per bron zijn vastgelegd in de standaard.
aanmaakdatum | Datum en tijd van gebeurtenis
kenmerken | Een lijst van objecten die de kenmerken van het bericht vormen. De mogelijke kenmerken worden vastgelegd per bron in de standaard.

**LET OP: Vooruitlopend op tijdreizen - De URL moet een
`?tijdstempel=<tijd en datum>` meekrijgen zodat niet de actuele versie van de
`Zaak` geeft maar de versie die echt hoort bij het bericht. Verder is er de
wens om het "verschil" van voor en na de wijziging mee te geven in de
notificatie of op te vragen.**

### Bronnen

In het geval van de ZGW API's wordt elk component gezien als bron en heeft dus
zijn eigen kanaal, met eigen kenmerken en eventueel additionele acties.

Elk component kan `kenmerken` definieren die helpen bij het filteren van
relevante informatie.

#### Zaken API

* Kanaal: `zaken`
* Additionele acties: -

Kenmerk | Omschrijving
--- | ---
bronorganisatie | Overeenkomstig veld in ZAAK
zaaktype | Overeenkomstig veld in ZAAK
vertrouwelijkheidaanduiding | Overeenkomstig veld in ZAAK

#### Documenten API

* Kanaal: `documenten`
* Additionele acties: -

Kenmerk | Omschrijving
--- | ---
bronorganisatie | Overeenkomstig veld in ENKELVOUDIG INFORMATIEOBJECT
informatieobjecttype | Overeenkomstig veld in ENKELVOUDIG INFORMATIEOBJECT
vertrouwelijkheidaanduiding | Overeenkomstig veld in ENKELVOUDIG INFORMATIEOBJECT

#### Besluiten API

* Kanaal: `besluiten`
* Additionele acties: -

Kenmerk | Omschrijving
--- | ---
verantwoordelijkeOrganisatie | Overeenkomstig veld in BESLUIT
besluittype | Overeenkomstig veld in BESLUIT

#### Zaaktypen API

Op dit moment nog niet gespecificeerd.

## API specificatie

### Abonneren

Een consumer abonneert zich op notificaties door de volgende request naar de
NC te sturen:

```http
POST /api/v1/abonnementen HTTP/1.0

Authorization: Bearer abcdef1234
Content-Type: application/json

{
    "callbackUrl": "https://zaken-api.vng.cloud/api/v1/callbacks",
    "auth": "Bearer aef34gh...",
    "kanalen": [{
        "naam": "zaken",
        "filters": {
            "bronorganisatie": "082096752011",
            "zaaktype": "https://example.com/api/v1/zaaktypen/5aa5c",
            "vertrouwelijkheidaanduiding": "*"
        }
    }, {
        "naam": "documenten",
        "filters": {
            "bronorganisatie": "082096752011",
            "informatieobjecttype": "https://example.com/api/v1/informatieobjecttype/b8c11",
            "vertrouwelijkaanduiding": "openbaar"
        }
    }]
}
```

Het `DELETE`n, `PATCH` en `PUT` op individuele subscribers moet mogelijk zijn.

Details moeten ook opgevraagd kunnen worden, met uitzondering van de `auth`
gegevens.

Filter parameter(s) op `kanalen` zijn handig.

Alle `kenmerken` die een component definieert MOETEN aanwezig zijn in een
filter maar de waardes mogen naar wens worden ingevuld zodat er alleen berichten
binnenkomen die voldoen aan de filterkenmerken. De waarde `*` betekent dat er
niet gefilterd wordt op het element.

Onder de motorkap worden de kenmerken vertaald naar een RabbitMQ-"topic". Elke
waarde wordt base64-encoded en gescheiden door punten. Het voorbeeld wordt dus
`MDgyMDk2NzUyMDEx`.`aHR0cHM6Ly9leGFtcGxlLmNvbS9hcGkvdjEvemFha3R5cGVuLzVhYTVj`.`b3BlbmJhYXI=`,
ofwel als we elk element weer decoden:
`082096752011`.`https://example.com/api/v1/zaaktypen/5aa5c`.`openbaar`.

Dit is een intern implementatiedetail.

### Kanalen beheren

Een kanaal is het equivalent van een exchange in RabbitMQ.

Kanalen worden aangemaakt door producers (bronnen), en zijn gekarakteriseerd
door een unieke naam.

```http
POST /api/v1/kanalen HTTP/1.0

Authorization: Bearer abcdef1234
Content-Type: application/json

{
    "naam": "zaken",
    "documentatieLink": "http://example.com",
    "filters": [
        "bronorganisatie",
        "zaaktype",
        "vertrouwelijkheidaanduiding"
    ]
}
```

Een kanaal mag slechts eenmalig aangemaakt worden.

Daarnaast moet het ophalen van kanalen mogelijk zijn, zodat consumers kunnen
zien waarop ze zich kunnen abonneren.

De `filters` geven aan welke kenmerken zullen opgenomen worden in berichten
op dit kanaal, en tonen waarop consumers kunnen filteren. Bij het abonneren
moeten de filters getoetst worden tegen deze filters. Ook hier is volgorde
belangrijk.

### Notificaties insturen (publiceren)

De NC moet notificaties kunnen ontvangen:

```http
POST /api/v1/notificaties HTTP/1.0

Authorization: Bearer abcdef1234
Content-Type: application/json

{
    "kanaal": "zaken",
    "hoofdObject": "https://zaken-api.vng.cloud/api/v1/zaken/d7a22",
    "resource": "status",
    "resourceUrl": "https://zaken-api.vng.cloud/api/v1/statussen/d7a22/721c9",
    "actie": "create",
    "aanmaakdatum": "2018-01-01T17:00:00Z",
    "kenmerken": {
        "bron": "082096752011",
        "zaaktype": "https://example.com/api/v1/zaaktypen/5aa5c",
        "vertrouwelijkeidaanduiding": "openbaar"
    }
}

```

Onder water worden de kenmerken in een bepaald formaat gebruikt voor topics,
zodat consumers deze eenvoudiger kunnen filteren.

Merk op dat de kenmerken als `Array` opgebouwd worden. Dit is omdat _Object keys_
in JSON geen inherente volgorde hebben, en de volgorde wel belangrijk is
voor interne doeleinden.

### Notificaties ophalen (CONCEPT)

In eerste instantie zetten we enkel in op push via webhooks. Later laten we toe
om ook notificaties te pullen.

```http
GET /api/v1/abonnementen/ae54ef/notificaties HTTP/1.0

Authorization: Bearer abcdef1234
Accept: application/json

[{
    "kanaal": "zaken",
    "hoofdObject": "https://zaken-api.vng.cloud/api/v1/zaken/d7a22",
    "resource": "status",
    "resourceUrl": "https://zaken-api.vng.cloud/api/v1/statussen/d7a22/721c9",
    "actie": "create",
    "aanmaakdatum": "2018-01-01T17:00:00Z",
    "kenmerken": {
        "bron": "082096752011",
        "zaaktype": "https://example.com/api/v1/zaaktypen/5aa5c",
        "vertrouwelijkeidaanduiding": "openbaar"
    }
}]
```

Dit zal enkel de niet bezorgde notificaties teruggeven.

## Uitdagingen en oplossingen

### AMQP vs. webhooks: volgorde events

Een van de grote voordelen van direct op AMQP in te haken is dat het protocol
oplossingen voorziet om te garanderen dat berichten in de juiste volgorde
aankomen.

In het scenario dat er bijvoorbeeld twee snelle statusupdates zijn van:

1. Aangemaakt naar
2. In behandeling naar
3. Afgerond

Als je geen AMQP gebruikt, kan het zijn dat door de intrinsieke aard van
TCP/HTTP statusupdate 3 voor 2 afgeleverd wordt op de webhook, door latency op
de eerste call bijvoorbeeld.

Dit zou kunnen leiden tot een incorrecte statusupdate via push bij clients.

We verwachten dat dit geen probleem wordt, omdat de inhoud van de wijziging
niet in de notificatie opgenomen is, maar enkel de kennisgeving dat _iets_
gebeurd is, en het is aan de consumer om de nieuwe state van de betrokken
resource(s) te bevragen. Dit betekent ook dat snelle, opeenvolgende
notificaties in principe kunnen geconsolideerd worden (orde van <1s).

### AMQP vs. webhooks: garantie dat een bericht afgeleverd wordt

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

### AMQP en NLx

NLx ondersteund geen AMQP.

### Bijhouden van berichten

Berichten worden in principe niet bewaard in de NC. Ontvangen notifications
worden meteen doorgezet.

Een uitzondering hierop is het bewaren van berichten om ze opnieuw te kunnen
versturen indien aflevering niet gelukt is - deze moeten opnieuw gescheduled
worden voor aflevering. Hierbij moet het mogelijk zijn om te configureren
hoevaak gepoogd moet worden een bericht af te leveren en hoe lang je moet
wachten om opnieuw te proberen.

### Notificaties bij andere standaarden

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

# Oude schetsen

[Voorbeeld sequence diagram (in-depth)](http://sequencediagram.org/index.html#initialData=C4S2BsFMAIDkHtQDMQGNICdIDsBQuAHAQw1FRGO2GgC0AlAYUJLIqKrkRBVSNBgbwAtgXjYcwZqTRsOdIgCMFYALIBFKa0rUAIo3z0GAWgB8CZGj4gBw0eKoAuaAAUA8gGUAKtAD0RAiA+AG4AjD4KGGL2ADrYPj4ADADMAEwhRgBeRADWOPG45tyW-NCCImISpvJKqmpODFh8MMDwAaix8clpmTl5PgVcPFY25fbAADxGRtXKwOpOAJI6TiEpSbiGk0aFQyVldhJOABKens7QKQkhHT4AQpHY0ADmmJBPIADOwFiYACbQQkg1CWKzW+VwAF4IQtsGAQERwJ9htAguxoAAqdGGTHQIhIF4PX5Q-B6YxmQbFaylWwVRwuDzePwBYJhRRRSCAqg4G5ddJZXJxfo7SkjA5UKqKWbzaDuACuCg+qAwIAUMFJ0BaGtaaB5qT5vUFAwsvD2NLGWxmtScrgA0rhSVthSaqftacBjqdzpdroKAIIKdmc6hEdgvIQh7LAcFQmFwhFIkqox6Y0k4vEEsREiEGRimJ3I11jJxuLy+fyBULhB72HyrJI+bAU52QD43W6YNAAC0k+dNo0qJktczqLkiv1l6ABLY+RBeWugIOgdaNRWb1P7VAtkqt0FtG0YjqbBbNh2gJzOFwSCRuADV4OAWvAQL98kP1KYTKTiwyy8zK43jWGD4fDEYAkxebA2w7VBu3yIA)

[Voorbeeld sequence diagram (high-level)](http://sequencediagram.org/index.html#initialData=C4S2BsFMAIDkHtQDMQGNICdIDsBQuBDVYeDaAIQFcMBzTXABwI1FRCe2GgFkB5AJQC0BBg0bNW7Apx4DBAIyIBrHABNxLNFM40M8Sg2gBicCBoALYLsg5oAKjsAtAOIB1aAGdU8BpAcbJDi4EYBRUAlAYAGF4AFsGeGwcYACtIOhHfijcNWhcPiFFVBVsVUEAPhCwiJBouISkzgAuaABlSnkvDBB5GB9oEgY0DIIS-ABecYBJbDAQAlMPGpgAN2l7OwKFZTUHaAIkOj1SyfwqWkwKrZEGJucbJGgEj2BvVT6xa9EruSKS1SaAAV4C83qt1ucjhNxgBBaTYAixGB0VQEdaorgOSGYPYALxAACtsE8Qa94O9oOYHlwfHQ6CscKdcJkohUqmhltAYvFEskWo40UpoNhECBqpEWq1gBFKB5oAYMZBcOzwpEufVeZwfoUdqV+YLhaLxbVJdLgLL5QxFfgRcA+gyyFs-mp9aMACoAT180BAcoKAH58r9dWVyiyWgAJNHgEajaDvaUgcBynzMrKCbXbYou2NChMEJMeG2Ie2YWQ67N63M+4l0eC6A6+1DmaB0eS1VQAHWwa2JzzJFPk1COgadIYq4egUYWbTNFtTLIz5THlYBs5lcvzheLdug8Ad5az-1NG8tiu7IE4mEgHiWMhW8FIFGHmFHwdXmZuLXImDQlj3B4CnGl7dvKADuJKguSyKQO2kDqEAA).

## Reliability

De referentie-implementatie implementeert geen features die als enige doel
hebben om de reliability te verhogen - de scope creep hiervoor is namelijk te
hoog voor de beschikbare resources.

De hosting in een Kubernetes cluster met redundante pods beschermen voldoende
tegen onverwachte crashes. Daarnaast worden de berichten gelogd en is het
mogelijk om met een developer-interventie notificaties die niet afgeleverd
konden worden, opnieuw te versturen.
