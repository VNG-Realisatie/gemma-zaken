---
title: "Veelgestelde vragen"
date: '31-5-2018'
weight: 40
---


### Algemeen

#### Wie is de opdrachtgever?

VNG is beheerder en eigenaar van de standaard ZGW API's (nu in ontwikkeling).
Formeel opdrachtgever is [Theo Peters](https://github.com/TheoVNGPeters), Unit
Manager Architectuur en Standaarden.


#### Wat is de opdracht?

Het ontwikkelen van ZGW API's gebaseerd op User Stories, duidelijk herkenbare
architectuurpatronen volgend en in lijn met de gewenste toepassing van RESTful
APIs.


#### Wat is de relatie met Common Ground?

Gestreefd wordt naar de realisatie van een Gegevenslandschap waarbij data niet
langer wordt gekopiëerd en gesynchroniseerd, maar wordt gebruikt in de bron die
wordt aangeboden door een verantwoordelijk bronhouder. Verschillende leden van
het scrumteam zijn actief betrokken bij de realisatie van Common Ground.

Daar waar GEMMA 2 nog niet (helemaal) in lijn is met Common Ground, wordt
Common Ground gevolgd. De principes volgend uit de Common Ground visie worden
toegepast. _Zie: [productvisie](/productvisie)_


#### Wat gaat er concreet gemaakt worden?

_Volgens de [productvisie](/productvisie)_

* Opstellen en realiseren van een nieuwe ZGW API's volgens Open API
Specificatie v3 (AOS 3)
* Realiseren van een open source referentie-implementatie van
zaakregistratiecomponent, documentregistratiecomponent en
zaaktypecataloguscomponent welke de ZGW API's strikt implementeren
* Functionele documentatie voor het gebruik van de API.

_Volgens oorspronkelijke projectdefinitie_

* Een nieuwe versie van de ZDS services (gebaseerd op REST APIs, aansluitend
  bij Common Ground) om de interoperabiliteit tussen leveranciers te
  bewerkstelligen en leveranciers te bewegen in de richting van Common ground
  (Silo's openen). _De nieuwe/opvolgende versie van ZDS is ondertussen hernoemd
  naar de ZGW API's_;
* Een Referentie implementatie van een zaaksysteem in de app store;
* Een multitenant toepassing van dit zaaksysteem/zakenregister en ZTC. (dit
  valt buiten scope van wat het scrumteam zal opleveren)


#### Wat betekent dit voor leveranciers?

Er komt een nieuwe "standaard". Omdat deze vanuit gemeentes wordt gevraagd
wordt er van uit gegaan dat leveranciers deze meer en meer gaan gebruiken.
Voor in het achterhoofd: Er zal niet na de eerste sprint een volledige nieuwe
API specificatie gereed zijn.
De referentie implementatie biedt leveranciers een methode een eigen
implementatie te toetsen aan de interpretatie van de specificaties.


#### Wat is de rol van leveranciers?

Leveranciers zijn welkom bij sprint reviews (demo's). Zij kunnen met gemeentes
overleggen of bepaalde User Stories in de backlog worden opgenomen. Zij kunnen
ook direct issues aanmaken op Github of Pull Requests aanmaken voor wijzigingen
aan de specificaties. Nadere invulling van de rol wordt tijdens eerste sprints
uitgewerkt.


#### Wat is de rol van VNG?

* Beheerder van de standaarden en daarmee ook de standaard die wordt
gerealiseerd.
* Communicatie naar gemeenten
* Toetsen aan en aanpassen van de GEMMA architectuur
* Kwaliteitsbewaking


#### Wie betaalt dit allemaal?

De Opdrachtgever, [VNG Realisatie](https://github.com/VNG-Realisatie/)


#### Is de referentie-implementatie bruikbaar in productie?

Dat is niet het doel en wordt niet aanbevolen. Echter, er worden  kleine Open
Source componenten gerealiseerd waar leveranciers wellicht geen uitbreidingen
op hoeven te doen om ze in de praktijk te gebruiken.

#### Wanneer wordt een Release Candidate vastgesteld als Release?

Wanneer in de release candidate geen gebreken gevonden zijn en deze daarmee voldoende stabiel is wordt deze release candidate een release. De periode voor deze stabiliteit is vastgesteld op 2 maanden, ingaande vanaf de dag waarop de release candidate uitgebracht is. Onder gebreken wordt verstaan fouten in de standaard. Eventuele verbeteringen of verduidelijkingen in documentatie waarbij geen aanpassingen in de API's noodzakelijk zijn worden niet beschouwd als reden om een nieuwe release candidate uit te brengen.
