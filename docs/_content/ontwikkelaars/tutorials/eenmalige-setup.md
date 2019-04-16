---
title: Eenmalige setup na het opstarten van de containers
weight: 90
---

Deze tutorial beschrijft de eenmalige configuratie van de referentie-
implementaties.

Let op: deze setup hoef je slechts 1 keer uit te voeren, typisch als je voor
het eerst de containers opstart. Indien je dit toch een tweede keer uitvoert,
dan zal je zien dat de gegevens al ingevuld zijn of configuratie al bestaat.

## Wat zijn de vereisten voor deze tutorial?

* `docker` en `docker-compose` om lokaal op je (ontwikkelmachine) de
  componenten te hosten. Zie ['aan de slag'](../aan-de-slag) voor een
  uitgebreide beschrijving.

* Het handigste is om de containers in 1 command prompt te hebben draaien, en
  extra commando's in een tweede prompt ernaast uit te voeren. Zorg dat beide
  prompts zich in de juiste directory bevinden: `/pad/naar/gemma-zaken/infra`.

We nemen aan dat nu de containers draaien na het uitvoeren van
`docker-compose up` (of een variatie hierop).

## Aanmaken supergebruikers

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

## API-credentials genereren

Gebruik de [tokentool](https://ref.tst.vng.cloud/tokens/) om een _Client ID_
en _Secret_ te genereren, of verzin deze zelf. Deze credentials moet je straks
opvoeren.

## Configuratie in de administratieve interface

Het IP-adres uit de ['aan de slag'](../aan-de-slag) voorbereiding is hier
nodig om de componenten via de browser aan te spreken.

### ZRC

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

### DRC

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

### ZTC

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

### NRC

1. Open in je browser `http://<ip>:8004/admin/` en log in met je gebruikersnaam
   en wachtwoord uit de vorige stap.

2. Navigeer naar **VNG_API_COMMON** > **JWT secrets** en klik rechtsboven
   op **JWT Secret toevoegen**

7. Vul bij **Identifier** het _Client ID_ in en bij **Secret** het _Secret_.
   Beide komen uit de stap [api-credentials genereren](#api-credentials-genereren).

   Deze credentials laten toe om met de API van het NRC te communiceren.

## Registratie van de kanalen

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


[token-generator]: https://ref.tst.vng.cloud/tokens/
