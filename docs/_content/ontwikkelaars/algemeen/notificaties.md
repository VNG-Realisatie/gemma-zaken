# Notificaties (voor dummies)

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

** Topics

Topics zijn kanalen waar berichten op binnenkomen. Voorlopig definieren we voor
elke API een eigen topic. Alles wat gebeurt in de Zaken API, komt op Topic `Zaken`, dus ook
`ZaakDocument` en `Status` wijzigingen.


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

### Specifiek deel

Voor elk topic (kanaal) kan een specifieke inhoud worden gedefinieerd.

**Zaken**
Attribuut | Omschrijving
--- | ---
ZaakType | Voor de `Zaken` API

Bronnen:

* [Digilevering koppelvlakspecificatie](https://www.logius.nl/sites/default/files/public/bestanden/diensten/DigiLevering/Koppelvlakspecificatie.pdf)
* [Digilevering documentatie](https://www.logius.nl/diensten/digilevering/documentatie)

### Demo applicatie

De demo applicatie zal gebruikt worden om notificaties te tonen zonder hier op te acteren.



