---
title: Tutorial notificeren
weight: 40
---

In deze tutorial configureren we de referentieimplementaties van de ZGW
componenten voor het versturen en ontvangen van notificaties via de
notificatierouteringcomponent (NRC).

De tutorial is hands-on - onderaan vind je verdere referenties en bronnen
indien je meer wil lezen.

De volgende componenten zijn meest relevant:

* NRC: voor het routeren van notificaties, kanaal- en abonnementbeheer
* ZRC: voor het versturen van `zaken`-notificaties
* DRC: voor het versturen van `documenten`-notificaties
* ZTC: voor validaties bij het aanmaken van zaken en documenten

## Wat zijn de vereisten voor deze tutorial?

* `docker` en `docker-compose` om lokaal op je (ontwikkelmachine) de
  componenten te hosten. Zie ['installatie en configuratie'](./installatie-en-configuratie) voor een
  uitgebreide beschrijving.

* Het handigste is om de containers in 1 command prompt te hebben draaien, en
  extra commando's in een tweede prompt ernaast uit te voeren. Zorg dat beide
  prompts zich in de juiste directory bevinden: `/pad/naar/gemma-zaken/infra`.

* De [eenmalige setup](./eenmalige-setup) is uitgevoerd.

* Familiariteit met webhooks is een plus

## Aan de slag

### Ontvangen en versturen van notificaties

Het ZRC en DRC versturen notificaties naar het NRC. Het NRC distribueert deze
vervolgens naar de abonnees.

De notificaties zijn inzichtelijk gemaakt op het NRC - ga naar
`http://<nrc-ip>:8004` en klik op de homepage op de 'Logviewer'.

Er zijn twee perspectieven:

* [Notificaties publiceren](#ik-wil-als-bron-notificaties-publiceren)
* [Notificaties ontvangen](#ik-wil-als-consumer-notificaties-ontvangen)

#### Ik wil als bron notificaties publiceren

Het registreren van de kanalen eerder zorgde voor de noodzakelijke stappen.

Eenvoudigweg operaties uitvoeren op de ZRC en/of DRC API zal ervoor zorgen
dat notificaties gepubliceerd worden. Je kan bijvoorbeeld via de API een zaak
aanmaken, wijzigen of statussen toevoegen op een zaak om dit in actie te zien.

Je dient de scope `notificaties.scopes.publiceren` in het JWT te hebben
voor deze acties. Je kan de [tokentool][token-generator] gebruiken om een
JWT te genereren.

1. Bepaal de naam van het kanaal. Voor het ZRC bijvoorbeeld is dit `zaken`.

2. Zorg dat het kanaal bekend is bij het NC. Je kan dit controleren door een
   query te doen:

   ```http
   GET https://ref.tst.vng.cloud/nrc/api/v1/kanaal?naam=zaken HTTP/1.0
   Authorization: Bearer abcd1234
   ```

   Indien een lege lijst terugkomt, dan bestaat het kanaal nog niet. Indien het
   kanaal wel al bestaat, ga dan naar stap 4.

3. Registreer het kanaal (indien het nog niet bestaat)

    ```http
    POST https://ref.tst.vng.cloud/nrc/api/v1/kanaal HTTP/1.0
    Authorization: Bearer abcd1234
    Content-Type: application/json

    {
      "naam": "zaken",
      "documentatieLink": "https://ref.tst.vng.cloud/zrc/ref/kanalen/#zaken",
      "filters": [
        "bronorganisatie",
        "zaaktype",
        "vertrouwelijkheidaanduiding"
      ]
    }
    ```

    De documentatielink hoort te documenteren welke kenmerken relevant zijn
    voor een kanaal, en welke events gepubliceerd worden. Dit helpt consumers
    om te bepalen waarop ze willen abonneren.

4. Verstuur een bericht

    ```http
    POST https://ref.tst.vng.cloud/nrc/api/v1/notificaties HTTP/1.0
    Authorization: Bearer abcd1234
    Content-Type: application/json

    {
      "kanaal": "zaken",
      "hoofdObject": "https://ref.tst.vng.cloud/zrc/api/v1/zaken/ddc6d192",
      "resource": "status",
      "resourceUrl": "https://ref.tst.vng.cloud/zrc/api/v1/statussen/44fdcebf",
      "actie": "create",
      "aanmaakdatum": "2019-03-27T10:59:13Z",
      "kenmerken": {
        "bronorganisatie": "224557609",
        "zaaktype": "https://ref.tst.vng.cloud/ztc/api/v1/catalogussen/39732928/zaaktypen/53c5c164",
        "vertrouwelijkheidaanduiding": "openbaar"
      }
    }
    ```

#### Ik wil als consumer notificaties ontvangen

Je dient de scope `notificaties.scopes.consumeren` in het JWT te hebben
voor deze acties. Je kan de [tokentool][token-generator] gebruiken om een
JWT te genereren.

1. Voorzie een endpoint om notificaties te ontvangen. Een eenvoudige manier om
   deze te inspecteren is met de [webhook-site](https://webhook.site). Voor het
   vervolgen gebruiken we `https://webhook.site/ea216914-fc38-462e-a24c-7dc7e969d873`
   als voorbeeld-URL waarop notificaties bezorgd worden.

2. Vraag op welke kanalen beschikbaar zijn:

   ```http
   GET http://<nrc-ip>:8004/api/v1/kanaal HTTP/1.0
   Authorization: Bearer abcd1234
    ````

3. Registreer je abonnement bij het NRC:

   ```http
   POST http://<nrc-ip>:8004/api/v1/abonnement HTTP/1.0
   Authorization: Bearer abcd1234
   Content-Type: application/json

   {
     "callbackUrl": "https://webhook.site/ea216914-fc38-462e-a24c-7dc7e969d873",
     "auth": "dummy",
     "kanalen": [
       {
         "naam": "zaken",
         "filters": {
           "bronorganisatie": "224557609"
         }
       }
     ]
   }
   ```

    * `callbackUrl` is de volledige URL naar je _eigen_ endpoint waar je
      notificaties wenst op te ontvangen

    * `auth` is de waarde van de `Authorization` header om je _eigen_ endpoint
      te kunnen benaderen. Deze waarde wordt gebruikt door het NRC om berichten
      af te leveren. Voor `webhook.site` kan een dummy waarde gebruikt worden.

    * `kanalen` is een lijst van kanalen waarop je wenst te abonneren, met de
      relevante filters. De beschikbare kenmerken waarop gefilterd kan worden
      horen gedocumenteerd te zijn op de kanalen die opgevraagd zijn in stap 2.

    * `filters` zijn optioneel. Indien je een filter weglaat, dan geldt dit als
      wildcard.

4. Berichten worden nu naar je eigen endpoint gestuurd met een POST request

    Hieronder staat een verzoek zoals dat gedaan wordt door het NRC. Je kan dit
    verzoek uiteraard ook zelf sturen voor test doeleinden:

   ```http
   POST https://webhook.site/ea216914-fc38-462e-a24c-7dc7e969d873 HTTP/1.0
   Content-Type: application/json
   Authorization: Token abcde12345

   {
     "kanaal": "zaken",
     "hoofdObject": "https://zaken-api.vng.cloud/api/v1/zaken/ddc6d192",
     "resource": "status",
     "resourceUrl": "https://zaken-api.vng.cloud/api/v1/statussen/44fdcebf",
     "actie": "create",
     "aanmaakdatum": "2019-03-27T10:59:13Z",
     "kenmerken": {
       "bronorganisatie": "224557609",
       "zaaktype": "https://catalogi-api.vng.cloud/api/v1/zaaktypen/53c5c164",
       "vertrouwelijkheidaanduiding": "openbaar"
     }
   }
   ```

    Merk op dat de `Authorization` header hier verschilt van de `Authorization`
    naar het NRC. De notificatie wordt naar jouw eigen endpoint verstuurd,
    en bij het abonneren heb je aangegeven wat de `Authorization` header
    hiervoor moet zijn.

[token-generator]: https://zaken-auth.vng.cloud


## Achtergrondinformatie

De [technische notificaties achtergrond](/themas/achtergronddocumentatie/notificaties) bevat de
design-standpunten en onderkent de limitaties en risico's van deze aanpak.

[Hier](./_assets/notificeren.pptx) is de presentatie te vinden die gegeven is op het
API-lab.
