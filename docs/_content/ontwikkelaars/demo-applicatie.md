---
title: Demo applicatie
weight: 50
---

De demo applicatie is een combinatie van verschillende aspecten zoals die te 
vinden zijn in zaaksystemen, suites en applicaties. De demo applicatie is 
opgezet voor test en demonstratie doeleinden en kan geconfigureerd worden om te 
communiceren met de verschillende ZGW APIs.

_Opmerking: De demo applicatie is geen onderdeel van de standaard of referentie
implementaties en kan achterlopen op de meest recente versies van de APIs._

# Gebruik de online demo applicatie

De online demo applicatie is geconfigureerd om te communiceren met de gehoste
referentie implementaties van de verschillende componenten. Deze demo
applicatie kan **niet** anders worden geconfigureerd en is te vinden op:

https://ref.tst.vng.cloud/zaken-demo/


# Gebruik een lokale versie van de demo applicatie

Deze versie van de demo applicatie kunt u naar wens configureren op uw eigen
omgeving.

## Snelle start

Al bekend met alle vereisten en de opzet? Hieronder de commando's om snel van
start te gaan. Ga anders naar de **Voorbereiding**.

```bash
$ docker pull vngr/gemma-zaken-demo
$ docker run -p 8000:8080 --name=gemma-zaken-demo vngr/gemma-zaken-demo
```

## Voorbereiding

Ook voor de demo applicatie is een [Docker][docker] containers beschikbaar. De 
volgende onderdelen zijn nodig om aan de slag te gaan:

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

[docker]: https://docs.docker.com/
[docker-win-legacy]: https://docs.docker.com/toolbox/toolbox_install_windows/
[docker-win]: https://docs.docker.com/docker-for-windows/
[docker-mac]: https://docs.docker.com/docker-for-mac/install/
[docker-linux]: https://docs.docker.com/docker-for-mac/install/
[docker-compose-linux]: https://docs.docker.com/compose/install/

## Demo applicatie starten

1. Download de demo applicatie als Docker container:

   * Voor **MacOS, Linux en Windows (met Docker for Windows)**:

     ```bash
     $ docker pull vngr/gemma-zaken-demo
     ```

   * Voor **Windows (met Docker Toolbox)**:

     1. Start de **Docker Quickstart Terminal** vanuit het Start menu.
     2. Haal de container binnen:

        ```bash
        $ docker pull vngr/gemma-zaken-demo
        ```

2. Start de demo applicatie:

   ```bash
   $ docker run -p 8000:8080 --name=gemma-zaken-demo vngr/gemma-zaken-demo
   ```

3. Navigeer in de browser naar de demo applicatie.

   * Voor **MacOS, Linux en Windows (met Docker for Windows)**:

     Navigeer in de browser naar: `http://localhost:8080`

   * Voor **Windows (met Docker Toolbox)**:

     Docker Toolbox werkt iets anders en de demo applicatie is niet op
     `localhost` bereikbaar. In plaats daarvan moet het Docker VM IP-adres
     gebruikt worden:

     ```bash
     $ docker-machine ls
     NAME      ACTIVE   DRIVER       STATE     URL
     default   *        virtualbox   Running   tcp://<ip>:<port>
     ```

     Het `<ip>` hierboven is het IP waarop de referentie componenten
     beschikbaar zijn. Typisch is dit: `192.168.99.100`. Navigeer de browser
     naar: `http://192.168.99.100:8080`

4. In de browser, klik op `Configuratie` en login met onderstaande gegevens:

   * Gebruikersnaam: `admin`
   * Wachtwoord: `admin`

5. Optioneel: Laad voorbeeld configuratie in die gebruik maakt van de gehoste
   referentie implementaties:

   ```bash
   docker exec -it gemma-zaken-demo /app/src/manage.py loaddata refimpl-conf.json
   ```

## En verder...

