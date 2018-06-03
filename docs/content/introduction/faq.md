# Veelgestelde vragen

## Inhoud

* [Wie is de opdrachtgever?](#wie-is-de-opdrachtgever)
* [Wat is de opdracht?](#wat-is-de-opdracht)
* [Wat is de relatie met Common Ground?](#wat-is-de-relatie-met-common-ground)
* [Wat gaat er concreet gemaakt worden?](#wat-gaat-er-concreet-gemaakt-worden)
* [Wat is de rol van leveranciers?](#wat-is-de-rol-van-leveranciers)
* [Wat betekent dit voor leveranciers?](#wat-betekent-dit-voor-leveranciers)
* [Wat betekent dit voor gemeentes?](#wat-betekent-dit-voor-gemeentes)
* [Wat is de rol van VNG?](#wat-is-de-rol-van-vng)
* [Wie betaalt dit allemaal?](#wie-betaalt-dit-allemaal)
* [Worden zaaksystemen hiermee beter, goedkoper, sneller, beter uitwisselbaar, etc.?]
* [Is de referentie-implementatie bruikbaar in productie?]
* [Komt er een landelijke versie van dit "product"?]


## Wie is de opdrachtgever?

[Theo Peters](https://github.com/TheoVNGPeters) van [VNG Realisatie](https://github.com/VNG-Realisatie/)

## Wat is de opdracht?

`Het ontwikkelen van` ZDS 2.0 gebaseerd op duidelijk herkenbare architectuurpatronen en waar mogelijk in lijn met de gewenste toepassing van RESTful APIs.

## Wat is de relatie met Common Ground?

Theo Peters (Opdrachtgever) en Wouter Bruinsma (Product Owner) zijn beiden betrokken bij Common Ground. (uit sprint 0)

Daar waar GEMMA 2 nog niet (helemaal) in lijn is met Common Ground, wordt Common Ground gevolgd. De principes volgend uit de Common Ground visie worden toegepast. _Zie: [productvisie](./productvisie.md)_

## Wat gaat er concreet gemaakt worden?

_Volgens [productvisie](./productvisie.md#realisatie)_

* Realiseren van een open source `referentie implementatie van` zakenregistratiecomponent
* Opstellen en realiseren van een nieuwe "ZDS" 2.0 API `volgens Open API STandaard (AOS) 3`
* `(`Realiseren van toepassingen voor burgers of gemeenten die gebruik maken van zaakgegevens uit het zakenregistratiecomponent, via de gestandaardiseerde API`)`
* `Functionele documentatie voor het gebruik van de API.`

_Volgens projectdefinitie_

* Een nieuwe versie van de ZDS services (gebaseerd op REST APIs, aansluitend bij Common Ground) om de
interoperabiliteit tussen leveranciers te bewerkstelligen en leveranciers te bewegen in de richting van Common ground
(Silo's openen);
* Een Referentie implementatie van een zaaksysteem in de app store;
* Een Multi Tenency toepassing van dit zaaksysteem/zakenregister en ZTC.

## Wat betekent dit voor leveranciers?

Er komt een nieuwe "standaard". Omdat deze vanuit gemeentes wordt gevraagd wordt er van uit gegaan dat leveranciers deze meer en meer gaan gebruiken. Voor in het achterhoofd: Er zal niet na de eerste sprint een volledige nieuwe API specificatie gereed zijn.
De referentie implementatie biedt leveranciers een methode een eigen implementatie te toetsen aan de interpretatie van de specificaties.

## Wat is de rol van leveranciers?

Leveranciers zijn welkom bij sprint reviews (demo's). Zij kunnen met gemeentes overleggen of bepaalde User Stories in de backlog worden opgenomen. Zij kunnen ook direct issues aanmaken op Github of Pull Requests aanmaken voor wijzigingen aan de specificaties.

## Wat betekent dit voor gemeentes?


## Wat is de rol van VNG?

* Beheerder van de standaarden en daarmee ook de standaard die wordt gerealiseerd.
* Communicatie naar gemeenten
* Toetsen aan en aanpassen van de GEMMA architectuur
* Kwaliteitsbewaking

## Wie betaalt dit allemaal?

De Opdrachtgever, [VNG Realisatie](https://github.com/VNG-Realisatie/)

## Worden zaaksystemen hiermee beter, goedkoper, sneller, beter uitwisselbaar, etc.?


## Is de referentie-implementatie bruikbaar in productie?

TODO: In het algemeen niet direct. Echter, we realiseren kleinere componenten waar leveranciers wellicht geen uitbreidingen op kunnen of hoeven doen om ze in de praktijk te gebruiken. Hierdoor kunnen de gerealiseerde componenten wel direct gebruikt worden en bieden leveranciers hier weer lagen/software bovenop.

## Komt er een landelijke versie van dit "product"?

TODO: Basisregistraties wel landelijk, kernregistraties niet.


