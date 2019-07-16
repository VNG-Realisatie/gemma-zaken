---
title: "Installatie en configuratie refentie-implementatie"
date: '25-02-2019'
weight: 80
---

De referentie-implementatiecomponenten kunnen gebruikt worden door ontwikkelaars in hun
eigen ontwikkelomgeving om bijvoorbeeld vakapplicaties te testen, of een
ontbrekend component in de eigen software te simuleren.


## Snelle start

Al bekend met alle vereisten en de opzet? Voer dan de commando's hieronder in om snel van
start te gaan. Scroll anders naar beneden voor de uitgebreide handleiding.

```bash
$ git clone git@github.com:VNG-Realisatie/gemma-zaken.git
$ cd gemma-zaken/infra
$ docker-compose pull
$ docker-compose up
```

## Uitgebreide handleiding

### Voorbereiding

Alle componenten van de referentie-implementatie zijn als [Docker][docker] images beschikbaar.
De volgende onderdelen zijn nodig om aan de slag te gaan:

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

### Componenten referentie-implementatie opstarten

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
   $ docker-compose up
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

   * ZRC: `http://<ip-of-localhost>:8000`
   * DRC: `http://<ip-of-localhost>:8001`
   * ZTC: `http://<ip-of-localhost>:8002`
   * BRC: `http://<ip-of-localhost>:8003`
   * NRC: `http://<ip-of-localhost>:8004`
   * AC: `http://<ip-of-localhost>:8005`

6. Admin aanmaken voor elk referentie component

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

   Vervolgens kan je daarmee inloggen op `http://<ip-of-localhost>:800x/admin/` om
   testdata in te kunnen richten of gegevens te raadplegen.

7. Indien extra configuratie nodig is binnen een component, dan vind je deze
   in de documentatie van de component zelf. Deze staat gelinkt op
   `http://<ip-of-localhost>:800x` indien die aanwezig is.

8. De volgende stap is het inrichten van de autorisaties

### Setting up authorizations (Engels)

The components use _tokens_ to exchange authorization data. A consumer talks
to a provider, on condition that a valid token is given. Providers, in turn,
can also be consumers of other providers, and they should also use valid tokens.

Both forms use the same mechanism, which has two parts - basic authentication
of the consumer in the API and specific authorization to API resources.

The provider authenticates the consumer based on its **Identifier** and a shared
 **Secret**, which are sent in JWT in the header of a request. After
the consumer is recognized the provider defines its access based on the data in the
Autorisatiecomponent (AC)


1. Set up authentication for the consumer

   Login to the admin and go to `Client credentials` and click on **Add**.

   Enter all data and click **Save**:

   * `Identifier`:  A random string, for example `demo`.
   * `Secret`: A random string, for example `demo`.

   These are the credentials to create a JWT, of which both the consumer
   and the provider know the secret. This must typically be done on each
   component. It does not matter what is entered but it is easiest if the same
   credentials are entered in all components.

2. Set up access to specified resource for the consumer
   Authorizations for specific resources is run by the AC. The provider will request
   this API to get data about the consumer rights.

   First, configure the AC url in your API:
   Login to the API admin and go to `Autorisatiecomponentconfiguratie` and click on **Add**.
   Enter all data and click **Save**:
   * `Api root`: A url to the AC root, for example `http://<ip-of-localhost>:800x/api/v1/`.
   * `Component`: The sort of component this provider is - this is used to request the correct authorizations from the AC.

   After this, there are two ways of creating rights in the AC - via admin page and
   via POST requests to the AC API.

   The following instructions are for the way using the admin page.

   Login to the AC admin and go to `Applicaties` and click on **Add**.
   Enter all data and click **Save**:

   * `Client IDs:`:  A comma separated list of identifiers. This list should include `Identifier`
     from the step 1, for example `demo, demo2`.
   * `Label`: A name of the consumer, for example `demo client`.
   * `Heeft alle autorisaties`: A flag defining that the current consumer is superuser
     and have access for all the APIs and their resources. This flag is recommended to use only for
     testing purposes. Please don't use it for production.

   Below in the `Autorisaties` section rights for specific APIs, scopes and components of APIs
   can be added. They will be taken into account only if the consumer is not a superuser.

3. Arrange authorizations between components

   _All APIs must have permissions to query the AC, since it's a part of authorization process.
   Some APIs can request other APIs, for example the ZRC typically needs to validate a Zaaktype
   in the ZTC, therefore the ZRC must have permission to query the ZTC._

   The following instruction shows how to set up permission in any API fot the AC.

   Login to the admin of the API and go to `External API credentials` and click on **Add**.

   Enter all data and click **Save**:

   * `Api root`: Enter the URL of the API root of the relevant component (here it is AC).
     For instance: `http://<ip-of-localhost>:800x/api/v1/`
   * `Client id`: Vul hier hetzelfde in als de `Identifier` in stap 1 voor het
     betreffende component wat bereikbaar is op `API root`.
   * `Secret`: Vul hier hetzelfde in als de `Secret` in stap 1 voor het
     betreffende component wat bereikbaar is op `API root`.

   Repeat this step for all APIs querying other components. Please make sure that these relevant
   components have `Client credentials` from step 1. consistent with `External API credentials`

4. Generate JWT

   Navigate: [https://zaken-auth.vng.cloud/generate-jwt/](https://zaken-auth.vng.cloud/generate-jwt/)

   Enter the `Identifier` and `Secret` from step 1 and click **Bevestig**.

   A generated JWT can be used in the `Authorization` header now.  To inspect
   the JWT you can paste the token (without `Bearer`) in [jwt.io](https://jwt.io).
   Don't forget to enter your own secret (bottom right) instead of `your-256-bit-secret`!

   _Creating a JWT does not register the secret with the hosted reference components.
   See the [API guides](./api-guides) how this works._

Voor meer achtergrond informatie over autorisaties zie: [authenticatie & autorisatie](/themas/achtergronddocumentatie/authenticatie-autorisatie)


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

* `http://<ip-of-localhost>:800x/api/v1/` - API root
* `http://<ip-of-localhost>:800x/api/v1/schema/` - API documentatie

### API Guides

Er zijn verschillende [API guides](./api-guides) beschikbaar met
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
- `10.x.y.2:8004`

#### Host network

Er is een alternatieve setup die gebruik maakt van de `host` network mode. Dit
zorgt ervoor dat containers met elkaar kunnen verbinden, ook als URLs naar
`localhost` verwijzen (zie
[#537](https://github.com/VNG-Realisatie/gemma-zaken/issues/537)).

Gebruik:

```bash
$ docker-compose -f docker-compose.yml -f docker-compose.hostnetwork.yml up
```

De `-f` optie specifieert welke config files voor `docker-compose` gebruikt
moeten worden.

Het nadeel hiervan is dat de database en webservices poorten in gebruik nemen
op je lokale machine. Concreet gaat het om:

* 5436, 8000 voor het ZRC
* 5437, 8001 voor het DRC
* 5438, 8002 voor het ZTC
* 5439, 8003 voor het BRC
* 5440, 8004 voor het NRC

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

NRC_DB_PORT=5440
NRC_UWSGI_PORT=8004
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
$ docker-compose up
```

### Foutmelding: Error starting userland proxy / driver failed

Soortgelijke foutmeldingen gebeuren af en toe bij het starten van de Docker
containers. Een mogelijke oplossing:

```bash
$ docker-compose down
```

En herstart Docker. Het kan soms voorkomen dat het herstarten alleen een
oplossing biedt als er verbonden is met een netwerk zodat een publiek IP
gebruikt kan worden. Nadat docker opnieuw is opgestart

```bash
$ docker-compose up
```
