---
title: "Beheer"
date: '22-9-2022'
weight: 10
layout: page-with-side-nav
---

# Beheer

## Gebruikersgroepen

Met het gebruik van de API standaarden voor Zaakgericht werken is het onvermijdelijk dat er verbeterpunten naar boven komen. Om functionele behoeften van gemeenten goed in beeld te hebben en houden is er een zogenoemde Functionele gebruikersgroep ingericht. Hier hebben gemeenten zitting in. De onderwerpen gaan alleen over de functionaliteit van de API's. Ook wordt in de Functionele gebruikersgroep de volgorde en prioriteit van de doorontwikkeling bepaald. Wat is er nodig en wanneer?


Bij het implementeren van de API's komen onvermijdelijk ook technische verbeterpunten naar voren. Deze worden besproken en opgelost in de Technische gebruikersgroep. Aan deze gebruikersgroep nemen leveranciers en gemeenten die zelf software ontwikkelen deel. 

Op basis van de functionele en technische wensen uit de respectieveljke gebruikersgroepen worden issues geprioriteerd en toegekend aan een release. Het is altijd mogelijk om nieuwe issues in te brengen en die, in overleg, hoger geprioriteerd te krijgen. Als leverancier met een functionele wens raden we aan deze via gemeenten in te brengen in het functionele overleg. 

Nieuwe releases van de afzonderlijke API's voor Zaakgericht werken staan als milestones op https://github.com/VNG-Realisatie/gemma-zaken/milestones . De volgende releases staan op de planning voor 7 juli aanstaande:
- Zaken API 1.3 https://github.com/VNG-Realisatie/gemma-zaken/milestone/20
- Documenten API 1.2 https://github.com/VNG-Realisatie/gemma-zaken/milestone/22 
- Catalogi API 1.2 https://github.com/VNG-Realisatie/gemma-zaken/milestone/17 

Wilt u deelnemen aan één van deze werkgroepen, meldt u dan via dit [formulier](https://formulieren.vngrealisatie.nl/Api_ZDS) op de website van VNG Realisatie aan.


## Bijeenkomsten
Voor 2022 staan de volgende bijeenkomsten gepland. Bij elke datum staan de bespreekpunten. Om zo vroeg mogelijk een indicatie Voor toekomstige agenda's te geven staan die bespreekpunten in cursief. Deze agenda's kunnen nog wijzigen tot de bijeenkomst zelf.


### Functionele gebruikersgroep:
- 20-01-2022
- 03-03-2022
- 07-04-2022
- 12-05-2022
- 07-07-2022
- 15-09-2022
- 03-11-2022
- 08-12-2022

De functionele gebruikersgroep kent de volgende leden:


- Utrecht
- Rijswijk
- Dimpact
- Equalit
- Edwin Coster, Delft
- Jan Verbeek, Den Haag
- Nol Witte, Omgevingsdienst Midden-Holland
- Robert Jan van Vliet, Texel
- Erik de Lepper, 's Hertogenbosch
- Eduard Witteveen, Sudwest Fryslan
- Jacco Hovenga, Sudwest Fryslan
- Arjan Kloosterboer, VNG
- Henri Korver, VNG
- Ivo Hendriks, VNG
- Michiel Verhoef, VNG-R


### Technische gebruikersgroep:
- 26-01-2022
  - Status Standaardisatie API's
  - Catalogi API volgende versie: Historiemodel
- 23-02-2022
  - Gedrag Catalogi API
    - Aanmaken Zaak
    - Versieregime Zaaktpye, Informatieobjecttype, Besluittype
    - Mutaties en correcties
    - Historie en geldighied
    - Gebruik en betekenis Catalogus
- 23-03-2022
  - Status Standaardisatie API's
  - Betrokkene Bij Zaak
    - Uitleg hoe bedoeld in API
    - Bevindingen en voorstel tot verbetering
- 14-04-2022
  - Status Standaardisatie API's
  - Betrokkene bij Zaak update
  - Voorstel voor Performance Verbetering: Inclusions
- 25-05-2022
  - Milestoneplanning
  - Status standaardisatie API's
  - Performance verbetering: Inclusions / HAL / ALternatieven?
- 29-06-2022
- - _Gerelateerde zaken https://github.com/VNG-Realisatie/gemma-zaken/issues/1629_
- - _Verwijzen naar persoons-/BAG-gegevens in een andere bron_
- - _Andere dan correspondentieadressen in Verzending registrreren: https://github.com/VNG-Realisatie/gemma-zaken/issues/2112_
- 28-10-2022
- 02-11-2022
- 30-11-2022


De technische gebruikersgroep kent de volgende leden:


- Dimpact
- Alain van Hanegem, Decos
- Aren Slootweg, gemeente Schagen
- Andy Verberne, ATOS
- Bas Retera, Visma Circle
- Bertil Rebergen, Pink Roccade
- David Bronsveld, Decos
- Eduard Witteveen, gemeente Sudwest Fryslan
- Jimmy de Leeuw, Enable U
- Joeri Bekker, Maykin Media
- Johannes Battjes, Visma Roxit
- Maarten Rutte, Pink Roccade
- Michiel Nijdam, Visma Roxit
- Roel de Bruin, Centric
- Ruben van der Linde, Conduction
- Sander Groen, Decos
- WeAreFrank
- Arjan Kloosterboer, VNG
- Henri Korver, VNG
- Ivo Hendriks, VNG
- John van Dijk, VNG
- Michiel Verhoef, VNG

Een melding kan via diverse kanalen binnenkomen, zoals via Github als issue, het VNG API Community Slack kanaal maar ook mondeling (telefonisch, wandelgang) of via e-Mail. Een melding kan gaan om een vraag, een wens of een bug.

Vragen worden, wanneer deze geen gevoelige informatie bevatten, als issue vastgelegd in Github. Indien een vraag vaker gesteld is of anderszins in aanmerking komt, bijvoorbeeld omdat we verwachten dat deze vraag vaker gaat komen, wordt deze met het antwoord opgenomen in een FAQ. Het antwoord wordt daarnaast natuurlijk ook aan de vraagsteller gestuurd. 

Bij een wens wordt deze bekeken, waar nodig als Github issue opgevoerd en voor het team duidelijk(er) beschreven en komt deze op de product backlog om door het team opgepakt te worden in een sprint. Dat hoeft niet altijd de eerstvolgende sprint te zijn, de Product Owner beslist samen met het team, waar API Beheer ook aan deelneemt, bij welke epic de wens past en hoe en in welke sprint deze opgepakt wordt.

Wanneer een fout reproduceerbaar is kan deze opgelost worden. Urgente fouten waarvan de oplossing geen gevolgen heeft voor de standaard worden direct opgepakt en opgelost. Fouten die minder urgent zijn of niet backwards compatible zijn met de huidige versie van de standaard worden in het doorontwikkelingstraject opgepakt en opgelost.

Er kunnen ook fouten in de API Testvoorziening of de onderliggende technische voorzieningen voorkomen. Deze worden door API Beheer doorgezet naar de betreffende beheerteams. 

Lees de meer over de werkwijze van Beheer in de [volledige beschrijving](https://github.com/VNG-Realisatie/api-beheer/tree/master/Processen) op github.
