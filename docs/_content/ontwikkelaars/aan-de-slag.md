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
   
   Of, gebruik `git clone https://github.com/VNG-Realisatie/gemma-zaken.git`
   als authenticatie een issue is.

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

4. Vind en gebruik het juiste IP:

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

5. Bevraag de APIs via de browser.

   De componenten zijn bereikbaar op verschillende poorten op het IP uit de
   vorige stap.
   
   Navigeer in de browser naar:

   * ZRC: `http://<ip>:8000`
   * DRC: `http://<ip>:8001`
   * ZTC: `http://<ip>:8002`
   * BRC: `http://<ip>:8003`

5. Admin aanmaken voor elk referentie component

   Elk referentie componenent heeft een beheer interface. Om deze beheer 
   interface te benaderen, moet een gebruiker worden aangemaakt (voorbeeld 
   voor het ZTC):

   ```bash
   $ docker container ls
   CONTAINER ID    ...      PORTS                    NAMES
   2bea81c01aea    ...      0.0.0.0:8000->8000/tcp   infra_zrc_web_1
   e1638c2da098    ...      0.0.0.0:8003->8000/tcp   infra_brc_web_1
   ...
   $ docker exec -it infra_ztc_web_1 /app/src/manage.py createsuperuser
   ...
   ```

   In plaats van `infra_ztc_web_1` kunnen ook de andere Docker containers 
   benaderd worden door de bewuste naam onder `NAMES` te gebruiken.
   
   Vervolgens kan je daarmee inloggen op `http://<ip>:800x/admin/` om
   testdata in te kunnen richten of gegevens te raadplegen.

6. Autorisaties regelen voor consumers

   _Een consumer moet rechten hebben om bepaalde data op te vragen. Hiertoe
   dienen zowel de provider en als de consumer een gedeeld **secret** te
   hebben._

   Login op de admin en ga naar `Jwt secrets` en klik op **Toevoegen**.
   
   Vul alle gegevens in en klik op **Opslaan**:
   
   * `Identifier`: Een willeurige string, bijvoorbeeld `demo`.
   * `Secret`: Een willekeurige string, bijvoorbeeld `demo`.
   
   Dit zijn de credentials om straks een JWT aan te maken, waarvan zowel de 
   consumer als de provider het secret kennen. Dit moet typisch op elk 
   component gebeuren. Het maakt niet uit wat wordt ingevuld maar het 
   eenvoudigst is als in alle componenten hetzelfde wordt ingevuld.
   
7. Autorisaties regelen tussen componenten

   _Het ZRC moet typisch een Zaaktype valideren in het ZTC. Hiervoor moet het 
   ZRC wel toestemming hebben om het ZTC te bevragen._

   Login op de admin en ga naar `API credentials` en klik op **Toevoegen**.
   
   Vul alle gegevens in en klik op **Opslaan**:
   
   * `Api root`: Vul hier de URL in van de API root van het betreffende "andere"
     component. Bijvoorbeeld: `http://<ip>:800x/api/v1/`
   * `Client id`: Vul hier hetzelfde in als de `Identifier` in stap 6 voor het
     betreffende component wat bereikbaar is op `Api root`.
   * `Secret`: Vul hier hetzelfde in als de `Secret` in stap 6 voor het
     betreffende component wat bereikbaar is op `Api root`.

   De componenten maken zo onderling gebruik van dezelfde secrets als een 
   consumer maar dat is niet erg voor test doeleinden.
   
8. JWT aanmaken

   Navigeer naar: [https://ref.tst.vng.cloud/tokens/generate-jwt/](https://ref.tst.vng.cloud/tokens/generate-jwt/)
   
   Vul de `Identifier` en `Secret` in van stap 6, de relevante **scopes** en 
   **zaaktypes**, en klik op **Bevestig**.
   
   Er wordt nu een JWT gegenereerd die gebruikt kan worden in de `Authorization`
   header. Om het JWT te inspecteren kan je deze (zonder `Bearer`) plakken op
   [jwt.io](jwt.io). Overigens kunnen de `zaakypes` vervangen worden met de
   array `["*"]` voor alle zaaktypes.
   
   _Het aanmaken van een JWT registreert het secret **niet** bij de 
   gehoste referentie componenten. Zie de [API guides](../guides) hoe dit wel
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

### De componenten kunnen elkaar niet bereiken

Helaas een bekend probleem onder Windows. Achterliggende oorzaak is dat als
een component via Docker bereikbaar is op `localhost`

### Niet alle componenten zijn bereikbaar

Bekijk de status van de Docker containers:

```bash
$ docker container ls --all
```

Zijn er één of meerdere containers met de status `Exited`? Dan gaat er iets
niet goed.

In dit stadium van de referentie componenten kan het voorkomen dat er niet goed
gemigreerd wordt van een oude naar een nieuwe versie, of dat er ergens iets
stuk is gegaan. Wat mogelijk helpt is alle oude data te verwijderen en de
referentie componenten opnieuw te installeren:

```bash
$ docker-compose down
$ docker system prune  # Verwijdert alles behalve data!
$ git pull
$ docker-compose pull
$ docker-compose up -d
```

### Foutmelding: Error starting userland proxy / driver failed

Soortgelijke foutmeldingen gebeuren af en toe bij het starten van de Docker
containers. Oorzaak is last te achterhalen. Er zijn 2 acties om te proberen:

```bash
$ docker-compose -f docker-compose.desktop.yml down
$ docker-compose -f docker-compose.desktop.yml up -d
```

Als dat niet werkt:

```bash
$ docker-compose -f docker-compose.desktop.yml down
```

En herstart Docker. Het kan soms voorkomen dat het herstarten alleen een 
oplossing biedt als er verbonden is met een netwerk zodat een publiek IP 
gebruikt kan worden.


