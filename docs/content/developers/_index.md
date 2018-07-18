---
title: "Technische documentatie voor developers"
description: ""
weight: 10
---

De standaard wordt opgebouwd op basis van drie componenten, elk met hun eigen
OAS 3.0 definities. Het gaat dan om de zaakregistratiecomponent (ZRC),
documentregistratiecomponent (DRC) en de zaaktypecatalogus (ZTC).

De ontwikkeling van iedere component vindt plaats in een aparte git repository:

* [ZRC](https://github.com/vng-Realisatie/gemma-zaakregistratiecomponent)
* [DRC](https://github.com/VNG-Realisatie/gemma-documentregistratiecomponent)
* [ZTC](https://github.com/VNG-Realisatie/gemma-zaaktypecatalogus)

Uitgebreide documentatie per component is beschikbaar in deze repositories.
Dit document is als startpunt bedoeld om snel up-and-running te zijn.

## Ontwikkelen van een applicatie die van deze componenten gebruik maakt

Bij het ontwikkelen van vakapplicaties (ook wel afhandelapplicaties genoemd),
kunnen deze referentie-implementaties ingezet worden als backend services.

### Services starten

Alle componenten zijn als Docker containers beschikbaar.

In `infra` staat een bruikbare `docker-compose.yml` docker-compose file.
Hiervoor heb je nodig:

* Docker
* Docker-compose

Voorbeeld gebruik:

```bash
cd infra
docker-compose pull  # update naar nieuwste images
docker-compose up -d
```

Je kan nu de componenten bereiken:

* ZRC: http://localhost:8000
* DRC: http://localhost:8001
* ZTC: http://localhost:8002

**Docker Machine**

Indien je Docker Machine gebruikt, moet je het Docker VM ip-adres gebruiken.
Dit IP adres kan je vinden met ``docker-machine ls``. Gebruik vervolgens
http://<ip>:800x om de service te bereiken.

Het IP adres is zichtbaar in de URL kolom:

```bash
$ docker-machine ls
NAME      ACTIVE   DRIVER       STATE     URL
default   *        virtualbox   Running   tcp://<ip>:<port>
```

Om de services te stoppen, gebruik:

```bash
docker-compose down
```

### Superuser aanmaken

Je kan een superuser aanmaken voor elke service met:

```bash
docker-compose run (zrc_web|drc_web|ztc_web) python src/manage.py createsuperuser
```

Vervolgens kan je daarmee inloggen op http://localhost:800x/admin/ om testdata
in te kunnen richten.

De API urls zijn:

* http://localhost:800x/api/v1/ - API root
* http://localhost:800x/api/v1/schema/ - API documentatie
