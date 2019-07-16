---
title: "Gebruik van de demo-applicatie"
weight: 70
---

De demo applicatie is een combinatie van verschillende aspecten zoals die te
vinden zijn in zaaksystemen, suites en applicaties. De demo applicatie is
opgezet voor test en demonstratie doeleinden en kan geconfigureerd worden om te
communiceren met de verschillende ZGW APIs.

_Opmerking: De demo applicatie is geen onderdeel van de standaard of referentie
implementaties en kan achterlopen op de meest recente versies van de APIs._

## Gebruik de online demo applicatie

De online demo applicatie is geconfigureerd om te communiceren met de gehoste
referentie implementaties van de verschillende componenten. Deze demo
applicatie kan **niet** anders worden geconfigureerd en is te vinden op:

[https://zgw-demo.vng.cloud](https://zgw-demo.vng.cloud)


## Gebruik een lokale versie van de demo applicatie

Deze versie van de demo applicatie kunt u naar wens configureren op uw eigen
omgeving.


### Snelle start

Al bekend met alle vereisten en de opzet? Hieronder de commando's om snel van
start te gaan. Ga anders naar de **Voorbereiding**.

```bash
$ git clone git@github.com:VNG-Realisatie/gemma-zaken-demo.git
$ cd gemma-zaken-demo
$ docker-compose pull
$ docker-compose up -d
```

### Voorbereiding

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
* Docker Compose (alleen niet inbegrepen bij Docker for Linux)
  * [Linux][docker-compose-linux]

*Docker for Windows werkt alleen op Windows 10 Professional*


**Optioneel**

* [Git][git-scm] (handig om snel updates binnen te halen)

[docker]: https://docs.docker.com/
[docker-win-legacy]: https://docs.docker.com/toolbox/toolbox_install_windows/
[docker-win]: https://docs.docker.com/docker-for-windows/
[docker-mac]: https://docs.docker.com/docker-for-mac/install/
[docker-linux]: https://docs.docker.com/docker-for-mac/install/
[docker-compose-linux]: https://docs.docker.com/compose/install/
[git-scm]: https://git-scm.com/downloads

### Referentie componenten opstarten

1. Clone de `VNG-Realisatie/gemma-zaken` repository op de eigen computer:

   ```bash
   git clone git@github.com:VNG-Realisatie/gemma-zaken.git
   ```

   Of, gebruik `git clone https://github.com/VNG-Realisatie/gemma-zaken.git`
   als authenticatie een issue is.

   Of, [download][gemma-zaken-demo-download] de repository handmatig en pak
   deze uit in de `gemma-zaken-demo` folder.

2. Navigeer naar de project folder.

   * Voor **MacOS, Linux en Windows (met Docker for Windows)**:

     ```bash
     $ cd gemma-zaken-demo
     ```

   * Voor **Windows (met Docker Toolbox)**:

     1. Start de **Docker Quickstart Terminal** vanuit het Start menu.
     2. Navigeer naar de folder waar de repository staat. Als deze bijvoorbeeld
        staat in `C:\Projecten\gemma-zaken-demo` gaat dat als volgt:

        ```bash
        $ cd /C/Projecten/gemma-zaken-demo
        ```

2. Start de demo applicatie:

   ```bash
   $ docker-compose pull  # update naar nieuwste versie
   $ docker-compose up -d --build
   ```

3. Vind en gebruik het juiste IP:

   * Voor **MacOS en Linux**:

     Alle containers zijn bereikbaar op `localhost` of `127.0.0.1`.

   * Voor **Windows (met Docker for Windows)**:

     Het beste is om het NAT IP te gebruiken in plaats van `localhost`. Deze
     laatste kan soms problemen geven als een proces vanuit een Docker
     container met een andere Docker container wil communiceren.

     In een shell, voer `ipconfig` uit en zoek naar `DockerNAT`:

     ```bash
     $ ipconfig
     ...
     Ethernet adapter vEthernet (DockerNAT):
        Connection-specific DNS Suffix  . :
        IPv4 Address. . . . . . . . . . . : 10.0.75.1
        Subnet Mask . . . . . . . . . . . : 255.255.255.0
        Default Gateway . . . . . . . . . :
     ```

     Alle containers zijn bereikbaar op `10.0.75.1`.

   * Voor **Windows (met Docker Toolbox)**:

     Docker Toolbox werkt iets anders en de referentie componenten zijn niet op
     `localhost` bereikbaar. In plaats daarvan moet het Docker VM IP-adres
     gebruikt worden:

     ```bash
     $ docker-machine ip
     192.168.99.100
     ```

    Alle containers zijn bereikbaar op `192.168.99.100`.

4. Navigeer in de browser naar de demo applicatie: `http://<ip>:8080/`

5. Maak een gebruiker aan om de configuratie in te stellen:

   ```bash
   docker exec -it gemmazakendemo_web_1 /app/src/manage.py createsuperuser
   ```

5. In de browser, klik op `Configuratie` en login met de gegevens die in de
   vorige stap zijn ingevuld.

6. Optioneel: Laad voorbeeld configuratie in die gebruik maakt van de gehoste
   referentie implementaties:

   ```bash
   docker exec -it gemmazakendemo_web_1 /app/src/manage.py loaddata /app/src/zac/fixtures/refimpl-conf.json
   ```

   _TIP: Het kan zijn dat de configuratie niet goed hergeladen wordt. In dat
   geval kan in de admin de configuratie nogmaals worden opgeslagen of de Docker
   instantie moet opnieuw gestart worden.


[gemma-zaken-download]: https://github.com/VNG-Realisatie/gemma-zaken-demo/archive/master.zip


## En verder...

### Demo applicatie stoppen

De demo applicatie draait op de achtergrond. Om geen onnodige resources te
gebruiken op de computer kunnen ze eenvoudig weer uitgezet worden:

```bash
$ docker-compose down
```
