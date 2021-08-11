---
title: 'Doorontwikkeling'
date: '15-7-2019'
weight: 10
---

## Verwacht

Na de release van 1.0.0 van de eerste VNG API's worden de API's vanaf nu apart doorontwikkeld. Dit heeft al geleid tot een 1.1 versie van de [Zaken API standaard](https://zaken-api.test.vng.cloud/), [Documenten API standaard](https://documenten-api.test.vng.cloud/) en [Catalogi API standaard](https://catalogi-api.test.vng.cloud/). Voor een volledig overzicht van de releaseplanning zie de [milestones van de standaard](https://github.com/VNG-Realisatie/gemma-zaken/milestones). Deze milestones bevatten ook de releasenotes


* [Catalogi API standaard](https://catalogi-api.test.vng.cloud/)
* [Zaken API standaard](https://zaken-api.test.vng.cloud/)
* [Documenten API standaard](https://documenten-api.test.vng.cloud/)
* [Besluiten API standaard](https://besluiten-api.test.vng.cloud/)
* [Autorisaties API standaard](https://autorisaties-api.test.vng.cloud/)
 
Momenteel wordt er hard gewerkt aan de API standaarden voor Contactmomenten, Klanten en Verzoeken. Van de Contactmomenten API en Verzoeken API is inmiddels een 1.0.0 versie uitgebracht, van de Verzoeken API is een 1.0.0-beta versie beschikbaar.

* [Contactmomenten API standaard](https://contactmomenten-api.vng.cloud/api/v1/schema/)
* [Klanten API standaard](https://klanten-api.vng.cloud/api/v1/schema/)
* [Verzoeken API standaard BETA](https://verzoeken-api.vng.cloud/api/v1/schema/)


## Werkwijze

Het team dat aan de API's voor Zaakgericht Werken werkt doet dit volgens de agile methodiek.
Gemeenten en leveranciers leveren wensen en behoeften in de vorm van user stories rond zaakgericht werken die vervolgens worden vertaald naar wat nodig is in de API's.
De user stories wordenin overleg met de stakeholders toegevoegd aan een [milestone](https://github.com/VNG-Realisatie/gemma-zaken/milestones) en in de betreffende release uitgewerkt.

## Bijdragen

Het is niet nodig om software of documentatie te schrijven om toch bij te
dragen. De ontwikkeling is ook gebaat bij gerapporteerde problemen, suggesties
voor wijzigingen en vragen over dingen die (nog) onduidelijk zijn. Om dit te
doen kan een
[issue worden gemaakt](https://github.com/VNG-Realisatie/gemma-zaken/issues).
Op de supportpagina's van GitHub staat
[uitleg over het maken van issues](https://help.github.com/articles/creating-an-issue/).


## Bijdragen aan documentatie en code

Maak om bij te dragen aan de documentatie of software van de ZGW API's een
zogenaamde Pull Request. Lees alles over hoe git (en GitHub) werkt in deze
introductie over git flow](https://guides.github.com/introduction/flow/).

### 1. Maak je wijzigingen

Dit project hanteert het
**[OneFlow branching model](http://endoflineblog.com/oneflow-a-git-branching-model-and-workflow)**.
Maak je wijzigingen op een nieuwe 'feature branch' met de naam
*feature/naam-die-bijdrage-beschrijft*. Zorg voor heldere beschrijvingen voor
iedere commit, zodat degenen die de bijdrage moeten beoordelen een goed beeld
hebben van wat de bedoeling is.

### 2. Pull Request

Wanneer de bijdrage compleet op de nieuwe feature branch staat kun je een Pull
Request maken. Dit is, zoals de naam zegt, een verzoek aan de eigenaren van de
repository om de branch met wijzigingen op te halen en in het project te
voegen. Verzoek daarbij is om elke Pull Request te voorzien van een duidelijke
beschrijving en eventuele issue nummers die met behulp van de Pull Request
worden opgelost.

### 3. Verbeteren

Alle bijdragen worden beoordeeld in een review proces. Je kunt zelf ook
specifiek aan een teamlid vragen om een review.

Het kan zijn dat een Pull Request direct kan worden ingevoegd. Vaak is het
echter nodig om nog het e.e.a. te verbeteren aan de Pull Request voordat deze
in het project kan worden ingevoegd. Feedback op de Pull Request kan komen van
de eigenaren van de standaard, van andere belanghebbenden of van
geautomatiseerde tests.

Wanneer de gewijzigde documentatie en code door de menselijke review en
geautomatiseerde test komt, worden de wijzigingen van de Pull Request in het
project gevoegd.


## Scrum boards
Er worden vier scrum boards gebruikt om de flow naar resultaat in elke sprint
te faciliteren.

- [2. Scrum ZGW Voorbereiding](https://github.com/VNG-Realisatie/gemma-zaken/projects/1)
  Nieuwe user stories en issues komen hier op de backlog. Wanneer zij worden
  geprioriteerd komen ze in de flow om ze 'ready te maken' zodat ze opgepakt
  kunnen worden in de volgende sprint.

- [1. Scrum ZGW Realisatie Huidige Sprint](https://github.com/VNG-Realisatie/gemma-zaken/projects/3)
  Vanuit de kolom "Ready for Sprint" worden tijdens de maandelijkse sprint
  planning userstories opgepakt die uitgevoerd gaan worden. Deze komen dan in
  de eerste kolom van het scrum board gericht op realisatie van de API
  specificatie.

- [3. Scrum ZGW Gereed Archief](https://github.com/VNG-Realisatie/gemma-zaken/projects/4)
  Op dit board is terug te vinden welke user story gereed was in welke sprint.

- [4. Out of scope](https://github.com/VNG-Realisatie/gemma-zaken/projects/2)
  Op dit bord komen alle user stories die buiten scope zijn voor ZGW API's en die functionaliteit beschrijven voor gebruik van de ZGW API's buiten zaakgericht werken. 
  

## Review

Zowel het board
[Scrum ZGW Voorbereiding](https://github.com/VNG-Realisatie/gemma-zaken/projects/1)
als
[Scrum ZGW Realisatie Sprint x](https://github.com/VNG-Realisatie/gemma-zaken/projects/3)
bevat een kolom voor review. Tijdens de voorbereiding worden user stories
klaargemaakt om in een volgende sprint uitgevoerd te worden. Daar hoort een
review bij: voldoet de user story aan de Definition of Ready? Na de realisatie
vindt opnieuw een review plaats, van iedere Pull Request waarmee een wijziging
of toevoeging op de standaard wordt gedaan.

Reviews worden vaak aan specifieke personen gevraagd, maar iedereen kan een
review uitvoeren. Wanneer de beoordeling binnen je competenties valt, geef de
review dan prioriteit boven eventuele andere bijdragen zodat iedereen zo snel
mogelijk verder kan.



