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

*Deze sectie beschrijft hoe ontwikkelaars snel aan de slag kunnen met de 
referentie componenten in hun eigen ontwikkelomgeving.*

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
  * [Windows][docker-win] (Docker Toolbox, niet Docker for Windows)
  * [MacOS][docker-mac] (Docker for Mac)
  * [Linux][docker-linux] (Docker for Linux)
* Docker Compose (inbegrepen bij Docker Toolbox en Docker for Mac)
  * [Linux][docker-compose-linux]

**Optioneel**

* [Git][git-scm] (handig om snel updates binnen te halen)

[docker]: https://docs.docker.com/
[docker-win]: https://docs.docker.com/toolbox/toolbox_install_windows/
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
   
   * Voor **MacOS en Linux**:
   
     ```bash
     $ cd gemma-zaken/infra
     ```
    
   * Voor **Windows**:
   
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

   * Voor **MacOS en Linux**:
   
     Navigeer in de browser naar:
    
     * ZRC: `http://localhost:8000`
     * DRC: `http://localhost:8001`
     * ZTC: `http://localhost:8002`
     * BRC: `http://localhost:8003`

   * Voor **Windows** (of **Docker Toolbox** gebruikers):
   
     Docker Toolbox werkt iets anders en de referentie componenten zijn niet op
     `localhost` bereikbaar. In plaats daarvan moet het Docker VM IP-adres
     gebruikt worden:

     ```bash
     $ docker-machine ls
     NAME      ACTIVE   DRIVER       STATE     URL
     default   *        virtualbox   Running   tcp://<ip>:<port>
     ```
     
     Het `<ip>` hierboven is het IP waarop de referentie componenten 
     beschikbaar zijn. Typisch is dit: `192.168.99.100`. Navigeer de browser
     naar:
    
     * ZRC: `http://192.168.99.100:8000`
     * DRC: `http://192.168.99.100:8001`
     * ZTC: `http://192.168.99.100:8002`
     * BRC: `http://192.168.99.100:8003`

[gemma-zaken-download]: https://github.com/VNG-Realisatie/gemma-zaken/archive/master.zip

## En verder...

### Referentie componenten stoppen

De referentie componenten draaien op de achtergrond. Om geen onnodige resources
te gebruiken op de computer kunnen ze eenvoudig weer uitgezet worden:

```bash
$ docker-compose down
```

### Beheer interface

Elk referentie componenent heeft een beheer interface. Om deze beheer interface
te benaderen, moet een gebruiker worden aangemaakt (voorbeeld voor het ZTC):

```bash
docker exec -it infra_ztc_web_1 /app/src/manage.py createsuperuser
```

In plaats van `ztc_web` kunnen ook de andere Docker containers benaderd worden
met de andere componenten: `zrc_web`, `drc_web`, `brc_web`, etc. Een lijst van
alle componenten is te zien middels `docker container ls`.

Vervolgens kan je daarmee inloggen op `http://localhost:800x/admin/` om 
testdata in te kunnen richten of gegevens te raadplegen.

### APIs benaderen

De API's en API documentatie zijn beschikbaar op de volgende URLs:

* `http://localhost:800x/api/v1/` - API root
* `http://localhost:800x/api/v1/schema/` - API documentatie

### API Guides

Er zijn verschillende [API guides](guides) beschikbaar met 
veelvoorkomende consumer handelingen.

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
$ docker-compose pull
$ docker-compose up -d
```



