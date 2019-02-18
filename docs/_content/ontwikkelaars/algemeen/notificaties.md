# Notificaties (voor dummies)

Een component moet een bericht kunnen sturen die andere componenten kunnen ontvangen zodat zij hierop kunnen acteren indien dit een interesant bericht is voor het betreffende ontvangende component.

## Uitgangspunten

**Notificatie als REST API component**

Er wordt een notificatiecomponent ontwikkeld dat zorgt voor het routeren van
berichten. Dit kan een bestaand product zijn met een eigen REST API er voor om 
product specifieke eigenschappen te abstraheren.

Als voorbeeld kan [Google Cloud Pub/Sub API](https://cloud.google.com/pubsub/docs/reference/rest/)
gebruikt worden.

**Technologie onafhankelijk**

De hierboven genoemde REST API wordt een "standaard". Welke onderliggende
technologie echt gebruikt wordt maakt niet zo veel uit.

**Topics**

Topics zijn kanalen waar berichten op binnenkomen. Voorlopig definieren we voor
elke API een eigen topic. Alles wat gebeurt in de Zaken API, komt op Topic `Zaken`, dus ook
`ZaakDocument` en `Status` wijzigingen.

**Relevantie van een notificatie bepalen**

De last van het bepalen of een notificatie, bijvoorbeeld van een Zaak wijziging of het aanmaken van een Zaak,
relevant is, ligt bij de consumer. De consumer dient op basis van de notificatie te bepalen of het initieel relevant is (bijvoorbeeld het Zaaktype), de details op te halen en vervolgens daadwerkelijk te bepalen of deze notificatie tot een actie leidt.

## Notificatie

### Meta gegevens

Attribuut | Omschrijving
--- | ---
UUID | Een unieke identificatie van de notificatie
Topic | Het kanaal waar berichten behorend bij dit topic op gepubliceerd worden, en waar subscribers op kunnen subscriben.

Voorlopige inhoud

### Generiek deel

Elk bericht zal een generiek deel hebben.

Attribuut | Omschrijving
--- | ---
URL | De URL van de resource behorend bij het Topic (bijv. `Zaak`) (van de actuele resource - omdat we nog geen historie hebben)
Methode | De HTTP methode die is gebruikt voor het wijzigen (`PUT`, `POST`)
Resource | Naam van de daadwerkelijk resource die is gewijzigd (bijv. `Status`)
Resource-URL | De URL van de daadwerkelijk resource (optioneel)

**LET OP: Vooruitlopend op tijdreizen - De URL moet een `?tijdstempel=<tijd en datum>` meekrijgen zodat niet de actuele versie van de `Zaak` geeft maar de versie die echt hoort bij het bericht.**

### Specifiek deel

Voor elk topic (kanaal) kan een specifieke inhoud worden gedefinieerd.

**Zaken**

Attribuut | Omschrijving
--- | ---
ZaakType | Voor de `Zaken` API

### Demo applicatie

De demo applicatie zal gebruikt worden om notificaties te tonen zonder hier op te acteren.

Voorbeeld:

1. Burger B wil een bericht ontvangen van elke MOR-melding in mijn buurt (geografisch gebied).
2. `Zaak` van `ZaakType` *MOR* krijgt een nieuwe `Status`.
3. Er komt een notificatie op topic `Zaken` met o.a. het `ZaakType` (MOR) als extra informatie.
4. De MOR-applicatie (consumer) is subscribed op topic `Zaken` en ziet dat het `ZaakType` *MOR* relevant is.
5. De MOR-applicatie haalt de details van de `Zaak` en `Status` op.
6. De MOR-applicatie ziet in de details van de `Zaak` dat het geografische gebied van belang is voor burger B.
7. De MOR-applicatie stuurt een bericht naar burger B dat de `Zaak` in zijn geografische gebied een nieuwe `Status` heeft.

Dit voorbeeld is uitgebreider weergegeven als [sequence diagram](http://sequencediagram.org/index.html#initialData=C4S2BsFMAIDkHtQDMQGNICdIDsBQuBDVYeDaAIQFcMBzTXABwI1FRCe2GgFkB5AJQC0BBg0bNW7Apx4DBAIyIBrHABNxLNFM40M8Sg2gBicCBoALYLsg5oAKjsAtAOIB1aAGdU8BpAcbJDi4EYBRUAlAYAGF4AFsGeGwcYACtIOhHfijcNWhcPiFFVBVsVUEAPhCwiJBouISkzgAuaABlSnkvDBB5GB9oEgY0DIIS-ABecYBJbDAQAlMPGpgAN2l7OwKFZTUHaAIkOj1SyfwqWkwKrZEGJucbJGgEj2BvVT6xa9EruSKS1SaAAV4C83qt1ucjhNxgBBaTYAixGB0VQEdaorgOSGYPYALxAACtsE8Qa94O9oOYHlwfHQ6CscKdcJkohUqmhltAYvFEskWo40UpoNhECBqpEWq1gBFKB5oAYMZBcOzwpEufVeZwfoUdqV+YLhaLxbVJdLgLL5QxFfgRcA+gyyFs-mp9aMACoAT180BAcoKAH58r9dWVyiyWgAJNHgEajaDvaUgcBynzMrKCbXbYou2NChMEJMeG2Ie2YWQ67N63M+4l0eC6A6+1DmaB0eS1VQAHWwa2JzzJFPk1COgadIYq4egUYWbTNFtTLIz5THlYBs5lcvzheLdug8Ad5az-1NG8tiu7IE4mEgHiWMhW8FIFGHmFHwdXmZuLXImDQlj3B4CnGl7dvKADuJKguSyKQO2kDqEAA).

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
