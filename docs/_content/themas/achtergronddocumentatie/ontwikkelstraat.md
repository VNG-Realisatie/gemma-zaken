---
title: "Ontwikkelstraat"
date: '31-7-2018'
---

De ontwikkelstraat is zoveel mogelijk geautomatiseerd zodat code-wijzigingen
automatisch leiden tot het bijwerken van (test-)omgevingen.

Verder vinden er automatische checks plaats die de correctheid van
implementaties en netheid van code bewaken.


**Architectuurschets**

![DevOps pipeline](/img/dev-straat.png)

## Github

Alle ontwikkeling vindt plaats op Github. Het centrale punt is de
[gemma-zaken](https://github.com/VNG-Realisatie/gemma-zaken) repository.

Het one-flow git-branching model wordt hier aangehouden - dit betekent dat de
`master` branch altijd de 'huidige waarheid' is, en aanpassingen worden via
feature branches geïntroduceerd.

Daarnaast zijn er repositories voor de referentie-implementaties en
ondersteunende tooling.

### Referentie-implementaties

Iedere referentieimplementatie van een component leeft in zijn eigen repository:

* [ZRC](https://github.com/vng-Realisatie/gemma-zaakregistratiecomponent)
* [DRC](https://github.com/VNG-Realisatie/gemma-documentregistratiecomponent)
* [ZTC](https://github.com/VNG-Realisatie/gemma-zaaktypecatalogus)
* [BRC](https://github.com/VNG-Realisatie/gemma-besluitregistratiecomponent)
* [NRC](https://github.com/VNG-Realisatie/notificaties-api)
* [AC](https://github.com/VNG-Realisatie/gemma-autorisatiecomponent)

Voor de referentieimplementaties wordt het git-flow branching model
aangehouden. Dit houdt in dat de `master` branch de huidige stabiele,
'productie' versie is en de `develop` branch de volgende versie wordt.
Wijzigingen komen via feature branches in `develop` terecht. Releases worden
getagged om ze te merken als een stable release, waarbij semantic versioning
gebruikt wordt.

**Generatie API-specificatie**

Momenteel wordt de OAS 3.0 specificatie gegenereerd uit de referentie-
implementatie, waarna deze via een pull request in gemma-zaken aangeboden
wordt.

De developer moet binnen de ontwikkelomgeving van de component
`generate-schema` aanroepen (beschikbaar via de `vng-api-common` libaries).

Dit is essentieel, aangezien de unit-tests van de referentieimplementaties deze
yaml file gebruiken om de juiste endpoints af te leiden voor een operatie op
een resource.


### Ondersteunende tooling

De volgende repositories bevatten ondersteunende software:

**gemma-zaken-common**
De [gemma-zaken-common](https://github.com/VNG-Realisatie/gemma-zaken-common)
repository bevat code en tooling die gedeeld wordt tussen componenten. Het is
een dependency van ZRC, DRC, ZTC en ORC.

**Zaakintegratietesten (ZIT)**
De
[gemma-zaken-test-integratie](https://github.com/VNG-Realisatie/gemma-zaken-test-integratie)
repository bevat een test-suite die 'live' tegen de services praat. De
test-suite vraagt de openapi specificatie op bij de services, en simuleert
vervolgens de calls zoals een vakapplicatie die kan doen. Deze zijn geschikt
voor ketentesten.

## Jenkins

[Jenkins](https://jenkins.nlx.io/view/Gemma) is de
continuous-integration/deployment server. Voor elke referentieimplementatie
worden de volgende taken uitgevoerd:

* voor een nieuwe pull-request:
  * voer de automatische test-suite uit
  * verifieer dat de Docker image succesvol build
  * valideer de geldigheid van de OAS
  * rapporteer de resultaten naar Github


* voor elke change op de develop branch:
  * voer de automatische test-suite uit
  * bouw een nieuwe docker image
  * rapporteer het resultaat naar Github


* voor elke change op de master branch:
  * voer de automatische test-suite uit
  * rapporteer het resultaat naar Github
  * indien de tests slagen:
    * build een nieuwe docker image
    * push de nieuwe image naar Docker Hub
    * indien de commit getagged is met een release tag:
      * rol de nieuwe image uit in de Kubernetes cluster

## Docker hub

De docker images worden publiek beschikbaar gemaakt op
[Docker Hub](https://hub.docker.com/r/vngr/). De tags zijn gebasseerd op de git
release tags. Jenkins zorgt ervoor dat tags automatisch gepubliceerd worden.

## Kubernetes

Er is een Kubernetes cluster beschikbaar om de referentie-implementaties te
hosten, binnen de `gemma` namespace. Deze cluster is niet publiek toegankelijk,
maar de services, deployments en ingress configuratie wordt in de gemma-zaken
repository bijgehouden.

Vanuit Jenkins worden automatisch deployment updates doorgevoerd.

De referentieimplementaties zijn gehost op:

* ZRC: https://zaken-api.vng.cloud/api/v1/
* DRC: https://documenten-api.vng.cloud/api/v1/
* ZTC: https://catalogi-api.vng.cloud/api/v1/
* BRC: https://besluiten-api.vng.cloud/api/v1/
* NRC: https://notificaties-api.vng.cloud/api/v1/
* AC: https://autorisaties-api.vng.cloud/api/v1/

Merk op dat dit testomgevingen zijn waar geen enkele garantie van stabiliteit
is. In een latere fase komen er stabiele omgevingen.

## Deploy bot

De deploy bot leeft in de `gemma-zaken` repository en is een microservice die
in de cluster draait. Deze accepteert API requests om updates te triggeren van
andere services in de Kubernetes cluster.

## NLX Directory

De referentie-implementaties en hun API specs zijn geïntegreerd in de
[NLX directory](http://directory.demo.nlx.io) (vooralsnog de demo-omgeving).

## Docker-compose

Er is een `docker-compose` file beschikbaar om de volledige
referentie-implementatie stack op te brengen. Zie de [documentatie voor ontwikkelaars](/ontwikkelaars/handleidingen-en-tutorials/installatie-en-configuratie).
