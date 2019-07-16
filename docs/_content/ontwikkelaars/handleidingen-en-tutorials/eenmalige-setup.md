---
title: "Tutorial eenmalige setup"
weight: 50
---

Deze tutorial beschrijft de eenmalige configuratie van de referentie-
implementaties. De [autorisatieslides](./_assets/autorisatie.pptx) zoals gegeven op het
API-lab zijn ook beschikbaar.

Let op: deze setup hoef je slechts 1 keer uit te voeren, typisch als je voor
het eerst de containers opstart. Indien je dit toch een tweede keer uitvoert,
dan zal je zien dat de gegevens al ingevuld zijn of configuratie al bestaat.

## Wat zijn de vereisten voor deze tutorial?

* `docker` en `docker-compose` om lokaal op je (ontwikkelmachine) de
  componenten te hosten. Zie ['installatie en configuratie'](./installatie-en-configuratie) voor een
  uitgebreide beschrijving.

* Het handigste is om de containers in 1 command prompt te hebben draaien, en
  extra commando's in een tweede prompt ernaast uit te voeren. Zorg dat beide
  prompts zich in de juiste directory bevinden: `/pad/naar/gemma-zaken/infra`.

We nemen aan dat nu de containers draaien na het uitvoeren van
`docker-compose up` (of een variatie hierop). Instructies daarvoor zijn te vinden in de [handleiding installatie en configuratie](./installatie-en-configuratie).

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

```bash
docker-compose exec ac_web src/manage.py createsuperuser
```

## API-credentials genereren

Gebruik de [tokentool](https://zaken-auth.vng.cloud) om een _Client ID_
en _Secret_ te genereren, of verzin deze zelf. Deze credentials moet je straks
opvoeren.

## Bootstrapping

Je kan een basisconfiguratie genereren en inladen met docker-compose:

```bash
docker-compose run tokentool src/manage.py generate_fixtures
# Client ID: abc123
# Secret: letmein
```

Deze fixtures worden vervolgens ingeladen bij het herstarten van de services:

```bash
docker-compose down
docker-compose up
```

Eenmaal alle services weer 'up' zijn, verwijder dan de gegenereerde fixtures:

```bash
docker-compose run tokentool rm /tmp/fixtures/*
```

Als je deze bestanden laat bestaan, dan worden aanpassingen in de volgende
stappen bij de volgende herstart overschreven.

## Configuratie in de administratieve interface

Het IP-adres uit ['installatie en configuratie'](./installatie-en-configuratie) voorbereiding is hier
nodig om de componenten via de browser aan te spreken.

Via de homepage van elke component kan je een view-config pagina bereiken die
de status van configuratie toont.

### ZRC

1. Open in je browser `http://<zrc-ip>:8000/admin/` en log in met je
   gebruikersnaam en wachtwoord uit de "Aanmaken supergebruikers" stap.

2. Navigeer naar **Sites** > **Sites** en klik `example.com` aan.

3. Wijzig 'Domeinnaam' naar `<zrc-ip>:8000` en wijzig 'Weergavenaam' naar `ZRC`

4. Sla de wijzigingen op

5. Navigeer terug naar de **Voorpagina**

6. Navigeer naar **VNG_API_COMMON** en klik door naar
   **API credentials**. Voor elke record moet je de API root
   wijzigen van `http://localhost:800x`, waarbij je `localhost` vervangt door
   het IP adres van de service.

   De mapping van poort naar service is:

   * 8001: DRC
   * 8002: ZTC
   * 8003: BRC
   * 8004: NRC
   * 8005: AC

7. Configureer het AC: navigeer terug naar de **Voorpagina**. Klik vervolgens
   op **AUTHORIZATIONS** > **Autorisatiecomponentconfiguratie**. Stel de velden
   juist in:

    * **Api root**: `http://<ac-ip>:8005/api/v1/`
    * **Component**: Zaakregistratiecomponent

    Klik vervolgens op **Opslaan**

8. Configureer het NRC: navigeer terug naar de **Voorpagina**. Klik vervolgens
   op **NOTIFICATIES** > **Notificatiescomponentconfiguratie**.

    * Vul bij **Api root** het adres van het NRC in: `http://<nrc-ip>:8004/api/v1/`

    Klik vervolgens op **Opslaan**

### DRC

1. Open in je browser `http://<drc-ip>:8001/admin/` en log in met je
   gebruikersnaam en wachtwoord uit de vorige stap.

2. Navigeer naar **Sites** > **Sites** en klik `example.com` aan.

3. Wijzig 'Domeinnaam' naar `<drc-ip>:8001` en wijzig 'Weergavenaam' naar `DRC`

4. Sla de wijzigingen op

5. Navigeer terug naar de **Voorpagina**

6. Navigeer naar **VNG_API_COMMON** en klik door naar
   **API credentials**. Voor elke record moet je de API root
   wijzigen van `http://localhost:800x`, waarbij je `localhost` vervangt door
   het IP adres van de service.

   De mapping van poort naar service is:

   * 8000: ZRC
   * 8002: ZTC
   * 8003: BRC
   * 8004: NRC
   * 8005: AC

7. Configureer het AC: navigeer terug naar de **Voorpagina**. Klik vervolgens
   op **AUTHORIZATIONS** > **Autorisatiecomponentconfiguratie**. Stel de velden
   juist in:

    * **Api root**: `http://<ac-ip>:8005/api/v1/`
    * **Component**: Zaakregistratiecomponent

    Klik vervolgens op **Opslaan**

8. Configureer het NRC: navigeer terug naar de **Voorpagina**. Klik vervolgens
   op **NOTIFICATIES** > **Notificatiescomponentconfiguratie**.

    * Vul bij **Api root** het adres van het NRC in: `http://<nrc-ip>:8004/api/v1/`

    Klik vervolgens op **Opslaan**

### ZTC

1. Open in je browser `http://<ztc-ip>:8002/admin/` en log in met je
   gebruikersnaam en wachtwoord uit de vorige stap.

2. Navigeer naar **MISCELLANEOUS** > **Sites** en klik `example.com` aan.

3. Wijzig 'Domeinnaam' naar `<ztc-ip>:8002` en wijzig 'Weergavenaam' naar `ZTC`

4. Sla de wijzigingen op

5. Navigeer terug naar de **Voorpagina**

6. Navigeer naar **MISCELLANEOUS** en klik door naar
   **API credentials**. Voor elke record moet je de API root
   wijzigen van `http://localhost:800x`, waarbij je `localhost` vervangt door
   het IP adres van de service.

   De mapping van poort naar service is:

   * 8000: ZRC
   * 8001: DRC
   * 8003: BRC
   * 8004: NRC
   * 8005: AC

7. Configureer het AC: navigeer terug naar de **Voorpagina**. Klik vervolgens
   op **AUTHORIZATIONS** > **Autorisatiecomponentconfiguratie**. Stel de velden
   juist in:

    * **Api root**: `http://<ac-ip>:8005/api/v1/`
    * **Component**: Zaakregistratiecomponent

    Klik vervolgens op **Opslaan**

8. Configureer het NRC: navigeer terug naar de **Voorpagina**. Klik vervolgens
   op **NOTIFICATIES** > **Notificatiescomponentconfiguratie**.

    * Vul bij **Api root** het adres van het NRC in: `http://<nrc-ip>:8004/api/v1/`

    Klik vervolgens op **Opslaan**

### BRC

1. Open in je browser `http://<brc-ip>:8003/admin/` en log in met je
   gebruikersnaam en wachtwoord uit de "Aanmaken supergebruikers" stap.

2. Navigeer naar **Sites** > **Sites** en klik `example.com` aan.

3. Wijzig 'Domeinnaam' naar `<brc-ip>:8000` en wijzig 'Weergavenaam' naar `BRC`

4. Sla de wijzigingen op

5. Navigeer terug naar de **Voorpagina**

6. Navigeer naar **VNG_API_COMMON** en klik door naar
   **API credentials**. Voor elke record moet je de API root
   wijzigen van `http://localhost:800x`, waarbij je `localhost` vervangt door
   het IP adres van de service.

   De mapping van poort naar service is:

   * 8000: ZRC
   * 8001: DRC
   * 8002: ZTC
   * 8004: NRC
   * 8005: AC

7. Configureer het AC: navigeer terug naar de **Voorpagina**. Klik vervolgens
   op **AUTHORIZATIONS** > **Autorisatiecomponentconfiguratie**. Stel de velden
   juist in:

    * **Api root**: `http://<ac-ip>:8005/api/v1/`
    * **Component**: Zaakregistratiecomponent

    Klik vervolgens op **Opslaan**

8. Configureer het NRC: navigeer terug naar de **Voorpagina**. Klik vervolgens
   op **NOTIFICATIES** > **Notificatiescomponentconfiguratie**.

    * Vul bij **Api root** het adres van het NRC in: `http://<nrc-ip>:8004/api/v1/`

    Klik vervolgens op **Opslaan**

### NRC

1. Open in je browser `http://<nrc-ip>:8004/admin/` en log in met je
   gebruikersnaam en wachtwoord uit de vorige stap.

2. Navigeer naar **VNG_API_COMMON** en klik door naar
   **API credentials**. Voor elke record moet je de API root
   wijzigen van `http://localhost:800x`, waarbij je `localhost` vervangt door
   het IP adres van de service.

   De mapping van poort naar service is:

   * 8000: ZRC
   * 8001: DRC
   * 8002: ZTC
   * 8003: BRC
   * 8005: AC

3. Configureer het AC: navigeer terug naar de **Voorpagina**. Klik vervolgens
   op **AUTHORIZATIONS** > **Autorisatiecomponentconfiguratie**. Stel de velden
   juist in:

    * **Api root**: `http://<ac-ip>:8005/api/v1/`
    * **Component**: Zaakregistratiecomponent

    Klik vervolgens op **Opslaan**

4. Configureer het NRC: navigeer terug naar de **Voorpagina**. Klik vervolgens
   op **NOTIFICATIES** > **Notificatiescomponentconfiguratie**.

    * Vul bij **Api root** het adres van het NRC in: `http://<nrc-ip>:8004/api/v1/`

    Klik vervolgens op **Opslaan**

### AC

1. Open in je browser `http://<ac-ip>:8005/admin/` en log in met je
   gebruikersnaam en wachtwoord uit de vorige stap.

2. Navigeer naar **Sites** > **Sites** en klik `example.com` aan.

3. Wijzig 'Domeinnaam' naar `<ac-ip>:8005` en wijzig 'Weergavenaam' naar `AC`

4. Sla de wijzigingen op

5. Navigeer terug naar de **Voorpagina**

6. Navigeer naar **VNG_API_COMMON** en klik door naar
   **API credentials**. Voor elke record moet je de API root
   wijzigen van `http://localhost:800x`, waarbij je `localhost` vervangt door
   het IP adres van de service.

   De mapping van poort naar service is:

   * 8000: ZRC
   * 8001: DRC
   * 8002: ZTC
   * 8003: BRC
   * 8004: NRC

7. Configureer het AC: navigeer terug naar de **Voorpagina**. Klik vervolgens
   op **AUTHORIZATIONS** > **Autorisatiecomponentconfiguratie**. Stel de velden
   juist in:

    * **Api root**: `http://<ac-ip>:8005/api/v1/`
    * **Component**: Zaakregistratiecomponent

    Klik vervolgens op **Opslaan**

8. Configureer het NRC: navigeer terug naar de **Voorpagina**. Klik vervolgens
   op **NOTIFICATIES** > **Notificatiescomponentconfiguratie**.

    * Vul bij **Api root** het adres van het NRC in: `http://<nrc-ip>:8004/api/v1/`

    Klik vervolgens op **Opslaan**

## Registratie van de kanalen

Het ZRC, DRC en AC moeten hun notificatiekanaal registeren. Dit doe je op de
command prompt:

```bash
docker-compose exec zrc_web src/manage.py register_kanaal
# Registered kanaal 'zaken' with http://<nrc-ip>:8004/api/v1
```

```bash
docker-compose exec drc_web src/manage.py register_kanaal
# Registered kanaal 'documenten' with http://<nrc-ip>:8004/api/v1
```

```bash
docker-compose exec ac_web src/manage.py register_kanaal
# Registered kanaal 'autorisaties' with http://<nrc-ip>:8004/api/v1
```

[token-generator]: https://zaken-auth.vng.cloud
