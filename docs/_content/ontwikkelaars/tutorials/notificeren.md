---
title: Tutorial notificeren
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
  componenten te hosten. Zie ['aan de slag'](../aan-de-slag) voor een
  uitgebreide beschrijving.

* Het handigste is om de containers in 1 command prompt te hebben draaien, en
  extra commando's in een tweede prompt ernaast uit te voeren. Zorg dat beide
  prompts zich in de juiste directory bevinden: `/pad/naar/gemma-zaken/infra`.

* Familiariteit met webhooks is een plus

## Eenmalige setup na het opstarten van de containers

Let op: deze setup hoef je slechts 1 keer uit te voeren, typisch als je voor
het eerst de containers opstart. Indien je dit toch een tweede keer uitvoert,
dan zal je zien dat de gegevens al ingevuld zijn of configuratie al bestaat.

We nemen aan dat nu de containers draaien na het uitvoeren van
`docker-compose up` (of een variatie hierop).

### Aanmaken supergebruikers

Supergebruikers laten je toe om in de administratieve omgeving van de
componenten de nodige instellingen te maken. Deze moeten initieel in de
database aangemaakt worden.

Voer op de command prompt het `createsuperuser` commando uit voor elke
component:

```bash
docker-compose exec zrc_web src/manage.py createsuperuser
Username: bob
Email address: bob@example.com
Password:
Password (again):
Superuser created successfully.
```

De commando's zijn interactief, en wachtwoorden die je intikt _zie je niet_.

Doe dit ook voor de andere componenten:

```bash
docker-compose exec drc_web src/manage.py createsuperuser
```

```bash
docker-compose exec ztc_web src/manage.py createsuperuser
```

```bash
docker-compose exec brc_web src/manage.py createsuperuser
```

```bash
docker-compose exec nrc_web src/manage.py createsuperuser
```

### API-credentials genereren

Gebruik de [tokentool](https://ref.tst.vng.cloud/tokens/) om een _Client ID_
en _Secret_ te genereren, of verzin deze zelf. Deze credentials moet je straks
opvoeren.

### Configuratie in de administratieve interface

Het IP-adres uit de ['aan de slag'](../aan-de-slag) voorbereiding is hier
nodig om de componenten via de browser aan te spreken.

#### ZRC

1. Open in je browser `http://<ip>:8000/admin/` en log in met je gebruikersnaam
   en wachtwoord uit de vorige stap.

2. Navigeer naar **Sites** > **Sites** en klik `example.com` aan.

3. Wijzig 'Domeinnaam' naar `<ip>:8000` en wijzig 'Weergavenaam' naar `ZRC`

4. Sla de wijzigingen op

5. Navigeer terug naar de **Voorpagina**

6. Navigeer naar **VNG_API_COMMON** > **JWT secrets** en klik rechtsboven
   op **JWT Secret toevoegen**

7. Vul bij **Identifier** het _Client ID_ in en bij **Secret** het _Secret_.
   Beide komen uit de stap [api-credentials genereren](#api-credentials-genereren).

   Deze credentials laten toe om met de API van het ZRC te communiceren.

8. Ga een stap terug naar **VNG_API_COMMON** en navigeer naar
   **API credentials**. Klik rechtsboven op **API Credential toevoegen**.

   Deze credentials worden gebruikt als het ZRC met een _andere_ API moet
   communiceren (zoals een NRC).

9. Configureer credentials voor het NRC:

    * Vul bij **Api root** het adres van het NRC in: `http://<ip>:8004/api/v1`
    * Vul bij **Client id** het _Client ID_ in
    * Vul bij **Secret** het _Secret_ in

    Klik vervolgens op **Opslaan en nieuwe toevoegen**

10. Configureer credentials voor het DRC:

    * Vul bij **Api root** het adres van het DRC in: `http://<ip>:8001/api/v1`
    * Vul bij **Client id** het _Client ID_ in
    * Vul bij **Secret** het _Secret_ in

    Klik vervolgens op **Opslaan en nieuwe toevoegen**

11. Configureer credentials voor het ZTC:

    * Vul bij **Api root** het adres van het ZTC in: `http://<ip>:8002/api/v1`
    * Vul bij **Client id** het _Client ID_ in
    * Vul bij **Secret** het _Secret_ in

    Klik vervolgens op **Opslaan**

12. Ga terug naar de **Voorpagina**

13. Navigeer naar **NOTIFICATIES** > **Notificatiescomponentconfiguratie**

14. Wijzig de **Api root** naar `http://<ip>:8004/api/v1` - dit is je eigen,
    lokale NRC. Vul opnieuw je **Client id** en **Secret** in.

#### DRC

1. Open in je browser `http://<ip>:8001/admin/` en log in met je gebruikersnaam
   en wachtwoord uit de vorige stap.

2. Navigeer naar **Sites** > **Sites** en klik `example.com` aan.

3. Wijzig 'Domeinnaam' naar `<ip>:8001` en wijzig 'Weergavenaam' naar `DRC`

4. Sla de wijzigingen op

5. Navigeer terug naar de **Voorpagina**

6. Navigeer naar **VNG_API_COMMON** > **JWT secrets** en klik rechtsboven
   op **JWT Secret toevoegen**

7. Vul bij **Identifier** het _Client ID_ in en bij **Secret** het _Secret_.
   Beide komen uit de stap [api-credentials genereren](#api-credentials-genereren).

   Deze credentials laten toe om met de API van het DRC te communiceren.

8. Ga een stap terug naar **VNG_API_COMMON** en navigeer naar
   **API credentials**. Klik rechtsboven op **API Credential toevoegen**.

   Deze credentials worden gebruikt als het DRC met een _andere_ API moet
   communiceren (zoals een NRC).

9. Configureer credentials voor het NRC:

    * Vul bij **Api root** het adres van het NRC in: `http://<ip>:8004/api/v1`
    * Vul bij **Client id** het _Client ID_ in
    * Vul bij **Secret** het _Secret_ in

    Klik vervolgens op **Opslaan en nieuwe toevoegen**

10. Configureer credentials voor het ZRC:

    * Vul bij **Api root** het adres van het ZRC in: `http://<ip>:8000/api/v1`
    * Vul bij **Client id** het _Client ID_ in
    * Vul bij **Secret** het _Secret_ in

    Klik vervolgens op **Opslaan en nieuwe toevoegen**

11. Configureer credentials voor het ZTC:

    * Vul bij **Api root** het adres van het ZTC in: `http://<ip>:8002/api/v1`
    * Vul bij **Client id** het _Client ID_ in
    * Vul bij **Secret** het _Secret_ in

    Klik vervolgens op **Opslaan**

12. Ga terug naar de **Voorpagina**

13. Navigeer naar **NOTIFICATIES** > **Notificatiescomponentconfiguratie**

14. Wijzig de **Api root** naar `http://<ip>:8004/api/v1` - dit is je eigen,
    lokale NRC. Vul opnieuw je **Client id** en **Secret** in.

#### ZTC

1. Open in je browser `http://<ip>:8002/admin/` en log in met je gebruikersnaam
   en wachtwoord uit de vorige stap.

2. Navigeer naar **MISCELLANEOUS** > **Sites** en klik `example.com` aan.

3. Wijzig 'Domeinnaam' naar `<ip>:8002` en wijzig 'Weergavenaam' naar `ZTC`

4. Sla de wijzigingen op

5. Navigeer terug naar de **Voorpagina**

6. Navigeer naar **MISCELLANEOUS** > **JWT secrets** en klik rechtsboven
   op **JWT Secret toevoegen**

7. Vul bij **Identifier** het _Client ID_ in en bij **Secret** het _Secret_.
   Beide komen uit de stap [api-credentials genereren](#api-credentials-genereren).

   Deze credentials laten toe om met de API van het ZTC te communiceren.

#### NRC

1. Open in je browser `http://<ip>:8004/admin/` en log in met je gebruikersnaam
   en wachtwoord uit de vorige stap.

2. Navigeer naar **VNG_API_COMMON** > **JWT secrets** en klik rechtsboven
   op **JWT Secret toevoegen**

7. Vul bij **Identifier** het _Client ID_ in en bij **Secret** het _Secret_.
   Beide komen uit de stap [api-credentials genereren](#api-credentials-genereren).

   Deze credentials laten toe om met de API van het NRC te communiceren.

### Registratie van de kanalen

Het ZRC en DRC moeten hun notificatiekanaal registeren. Dit doe je op de
command prompt:

```bash
docker-compose exec zrc_web src/manage.py register_kanaal
# Registered kanaal 'zaken' with http://<ip>:8004/api/v1
```

```bash
docker-compose exec drc_web src/manage.py register_kanaal
# Registered kanaal 'documenten' with http://<ip>:8004/api/v1
```

### Ontvangen en versturen van notificaties

Het ZRC en DRC versturen notificaties naar het NRC. Het NRC distribueert deze
vervolgens naar de abonnees.

De notificaties zijn inzichtelijk gemaakt op het NRC - ga naar
`http://<ip>:8004` en klik op de homepage op de 'Logviewer'.

Er zijn twee perspectieven:

* [Notificaties publiceren](#ik-wil-als-bron-notificaties-publiceren)
* [Notificaties ontvangen](#ik-wil-als-consumer-notificaties-ontvangen)

#### Ik wil als bron notificaties publiceren

Het registreren van de kanalen eerder zorgde voor de noodzakelijke stappen.

Eenvoudigweg operaties uitvoeren op de ZRC en/of DRC API zal ervoor zorgen
dat notificaties gepubliceerd worden. Je kan bijvoorbeeld via de API een zaak
aanmaken, wijzigen of statussen toevoegen op een zaak om dit in actie te zien.

Als je wilt zien wat een component precies doet, verwijzen we naar naar de
[volledige uitleg](../notificeren).

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
    GET http://<ip>:8004/api/v1/kanaal HTTP/1.0
    Authorization: Bearer abcd1234
    ````

3. Registreer je abonnement bij het NC:

    ```http
    POST http://<ip>:8004/api/v1/abonnement HTTP/1.0
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
      te kunnen benaderen. Deze waarde wordt gebruikt door het NC om berichten
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

    Merk op dat de `Authorization` header hier verschilt van de `Authorization`
    naar het NRC. De notificatie wordt naar jouw eigen endpoint verstuurd,
    en bij het abonneren heb je aangegeven wat de `Authorization` header
    hiervoor moet zijn.

[token-generator]: https://ref.tst.vng.cloud/tokens/


## Achtergrondinformatie

De [technische notificaties achtergrond](../algemeen/notificaties) bevat de
design-standpunten en onderkent de limitaties en risico's van deze aanpak.
