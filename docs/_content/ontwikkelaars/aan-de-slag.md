---
title: "Aan de slag"
date: '14-11-2018'
weight: 100
---

* Snel een API-request doen tegen de door VNG gehoste referentie
  implementaties? Ga naar de [API guides](guides).
* Zelf een implementatie bouwen op basis van de specificaties? Ga naar de
  [API specificaties](apis/index).
* Zelf de componenten draaien voor eigen gebruik? Lees verder!


# Zelf de componenten draaien

De referentie componenten kunnen gebruikt worden door ontwikkelaars in hun
eigen ontwikkelomgeving om bijvoorbeeld vakapplicaties te testen, of een
ontbrekend component in de eigen software te simuleren.


## Snelle start

Al bekend met alle vereisten en de opzet? Hieronder de commando's om snel van
start te gaan. Ga anders naar de **Voorbereiding**.

```bash
$ git clone git@github.com:VNG-Realisatie/gemma-zaken.git
$ cd gemma-zaken/infra
$ docker-compose pull
$ docker-compose up -d
```


## Voorbereiding

Alle referentie componenten zijn als [Docker][docker] containers beschikbaar.
De volgende onderdelen zijn nodig om aan de slag te gaan:

**Verplicht**

* Docker
  * [Windows][docker-win-legacy] (Docker Toolbox, indien Virtualbox moet
    blijven werken)
  * [Windows][docker-win] (Docker for Windows, als Virtualbox niet belangrijk
    is)
  * [MacOS][docker-mac] (Docker for Mac)
  * [Linux][docker-linux] (Docker for Linux)
* Docker Compose (inbegrepen bij Docker Toolbox en Docker for Mac)
  * [Linux][docker-compose-linux]

**Optioneel**

* [Git][git-scm] (handig om snel updates binnen te halen)

[docker]: https://docs.docker.com/
[docker-win-legacy]: https://docs.docker.com/toolbox/toolbox_install_windows/
[docker-win]: https://docs.docker.com/docker-for-windows/
[docker-mac]: https://docs.docker.com/docker-for-mac/install/
[docker-linux]: https://docs.docker.com/docker-for-mac/install/
[docker-compose-linux]: https://docs.docker.com/compose/install/
[git-scm]: https://git-scm.com/downloads


## Referentie componenten opstarten

1. Clone de `VNG-Realisatie/gemma-zaken` repository op de eigen computer:

   ```bash
   git clone git@github.com:VNG-Realisatie/gemma-zaken.git
   ```

   Of, [download][gemma-zaken-download] de repository handmatig en pak deze uit
   in de `gemma-zaken` folder.

2. Navigeer naar de `infra` folder in deze repository.

   * Voor **MacOS, Linux en Windows (met Docker for Windows)**:

     ```bash
     $ cd gemma-zaken/infra
     ```

   * Voor **Windows (met Docker Toolbox)**:

     1. Start de **Docker Quickstart Terminal** vanuit het Start menu.
     2. Navigeer naar de folder waar de repository staat. Als deze bijvoorbeeld
        staat in `C:\Projecten\gemma-zaken` gaat dat als volgt:

        ```bash
        $ cd /C/Projecten/gemma-zaken
        $ cd infra
        ```

3. Start de referentie componenten:

   ```bash
   $ docker-compose pull  # update naar nieuwste versie
   $ docker-compose up -d
   ```

4. Bevraag de APIs via de browser.

   * Voor **MacOS, Linux en Windows (met Docker for Windows)**:

     Navigeer in de browser naar:

     * ZRC: `http://localhost:8000`
     * DRC: `http://localhost:8001`
     * ZTC: `http://localhost:8002`
     * BRC: `http://localhost:8003`

   * Voor **Windows (met Docker Toolbox)**:

     Docker Toolbox werkt iets anders en de referentie componenten zijn niet op
     `localhost` bereikbaar. In plaats daarvan moet het Docker VM IP-adres
     gebruikt worden:

     ```bash
     $ docker-machine ip
     ```

     Typisch is dit: `192.168.99.100`. Navigeer de browser dan naar:

     * ZRC: `http://192.168.99.100:8000`
     * DRC: `http://192.168.99.100:8001`
     * ZTC: `http://192.168.99.100:8002`
     * BRC: `http://192.168.99.100:8003`

5. Admin aanmaken voor elk referentie component

   Elk referentie componenent heeft een beheer interface. Om deze beheer 
   interface te benaderen, moet een gebruiker worden aangemaakt (voorbeeld 
   voor het ZTC):

   ```bash
   docker exec -it infra_ztc_web_1 /app/src/manage.py createsuperuser
   ```

   In plaats van `infra_ztc_web_1` kunnen ook de andere Docker containers benaderd
   worden met de andere componenten: `infra_zrc_web_1`, `infra_drc_web_1`,
   `infra_brc_web_1`, etc. Een lijst van alle componenten is te zien middels
   `docker container ls`.
   
   Vervolgens kan je daarmee inloggen op `http://localhost:800x/admin/` om
   testdata in te kunnen richten of gegevens te raadplegen.

6. Autorisaties regelen

   Login op de admin en ga naar `Jwt secrets` en klik op **Toevoegen**.
   
   Vul `Identifier` en `Secret` in, en klik op **Opslaan**. Dit zijn de
   credentials om een JWT aan te maken, waarvan zowel de consumer als de
   provider het secret kennen. Dit moet typisch op elk component gebeuren.
   
7. JWT aanmaken

   Navigeer naar: [https://ref.tst.vng.cloud/tokens/generate-jwt/](https://ref.tst.vng.cloud/tokens/generate-jwt/)
   
   Vul de `Identifier` en `Secret` in van de vorige stap, de relevante 
   **scopes** en **zaaktypes**, en klik op **Bevestig**.
   
   Er wordt nu een JWT gegenereerd die gebruikt kan worden in de `Authorization`
   header. Om het JWT te inspecteren kan je deze (zonder `Bearer`) plakken op
   [jwt.io](jwt.io). Overigens kunnen de `zaakypes` vervangen worden met de
   array `["*"]` voor alle zaaktypes.
   
   _Het aanmaken van een JWT registreert het secret **niet** bij de 
   gehoste referentie componenten. Zie de [API guides](../guides). hoe dit wel
   werkt._


[gemma-zaken-download]: https://github.com/VNG-Realisatie/gemma-zaken/archive/master.zip


## En verder...

### Referentie componenten stoppen

De referentie componenten draaien op de achtergrond. Om geen onnodige resources
te gebruiken op de computer kunnen ze eenvoudig weer uitgezet worden:

```bash
$ docker-compose down
```


### APIs benaderen

De API's en API documentatie zijn beschikbaar op de volgende URLs:

* `http://localhost:800x/api/v1/` - API root
* `http://localhost:800x/api/v1/schema/` - API documentatie


### API Guides

Er zijn verschillende [API guides](guides) beschikbaar met
veelvoorkomende consumer handelingen.


### Poorten wijzigen

#### Bridge network

De default `docker-compose` setup gebruikt de `bridge` network mode. Een groot
nadeel hiervan is dat URLs in requests/responses met `localhost:800x` binnen
containers niet kunnen geresolved worden, wat leidt tot (obscure) validatiefouten.

Indien je `Docker for Windows` gebruikt, kan je hier omheen werken door de
componenten niet via `localhost` te benaderen, maar via een IP-adres.

Open een shell, en voer uit:

```bash
> ipconfig
```

Ga op zoek naar het `DockerNAT` netwerk - daar staat een gateway (`10.x.y.1`)
normaal. De componenten zouden moeten bereikbaar zijn op:

- `10.x.y.2:8000`
- `10.x.y.2:8001`
- `10.x.y.2:8002`
- `10.x.y.2:8003`

#### Host network

Er is een alternatieve setup die gebruik maakt van de `host` network mode. Dit
zorgt ervoor dat containers met elkaar kunnen verbinden, ook als URLs naar
`localhost` verwijzen (zie
[#537](https://github.com/VNG-Realisatie/gemma-zaken/issues/537)).

Gebruik:

```bash
$ docker-compose -f docker-compose.yml -f docker-compose.hostnetwork.yml up -d
```

De `-f` optie specifieert welke config files voor `docker-compose` gebruikt
moeten worden.

Het nadeel hiervan is dat de database en webservices poorten in gebruik nemen
op je lokale machine. Concreet gaat het om:

* 5436, 8000 voor het ZRC
* 5437, 8001 voor het DRC
* 5438, 8002 voor het ZTC
* 5439, 8003 voor het BRC

Je kan deze poorten aanpassen, indien gewenst. Dit doe je door een bestand
`.env` aan te maken in de map `infra` (=zelfde locatie waar je `docker-compose up`
uitvoert).

De inhoud hiervan is (met de defaults):

```
ZRC_DB_PORT=5436
ZRC_UWSGI_PORT=8000

DRC_DB_PORT=5437
DRC_UWSGI_PORT=8001

ZTC_DB_PORT=5438
ZTC_UWSGI_PORT=8002

BRC_DB_PORT=5439
BRC_UWSGI_PORT=8003
```

Je kan zelf de vrije poortnummers invullen die je wenst te gebruiken. Je hoeft
enkel de poorten op te geven die je wil wijzingen - indien variabelen ontbreken
wordt op de defaults teruggevallen.


## Eerste hulp

Bekijk de status van de Docker containers:

```bash
$ docker container ls --all
```

Zijn er één of meerdere containers met de status `Exited`? Dan gaat er iets
niet goed.

In dit stadium van de referentie componenten kan het voorkomen dat er niet goed
gemigreerd wordt van een oude naar een nieuwe versie, of dat er ergens iets
stuk is gegaan. Wat mogelijk helpt is alle oude data te verwijderen en de
referentie componenten opnieuw installeren:

```bash
$ docker-compose down
$ docker system prune  # Verwijdert alle data!
$ git pull
$ docker-compose pull
$ docker-compose up -d
```



