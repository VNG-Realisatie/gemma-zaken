---
title: "Hoe komen we samen tot API-standaarden"
date: '26-3-2019'
---
## Hoe komen we samen tot API-standaarden

Standaarden kunnen we alleen samen maken. We waarderen alle suggesties, zijn
blij met feedback en verwelkomen verbeteringen in dit project. Brede
samenwerking leidt tot de beste standaarden. 

Voorheen werd er toegewerkt naar één openbare consultatie waarmee een standaard eenmalig werd getoetst bij stakeholders. Bij de nieuwe werkwijze is er sprake van een voortdurende afstemming met partijen waarbij meerdere instrumenten worden ingezet, t.w.:

- Repositories op Github: te allen tijde kunnen partijen de stand van zaken raadplegen en de planning raadplegen. Ook kunnen zij bugs inschieten en wensen aanmelden in de vorm van user stories.
- Referentiecomponenten en API testvoorziening in de cloud waartegen getest kan worden.
- Elke vier weken wordt er een publieke Sprint-demo georganiseerd waar de gerealiseerde user stories worden gedemonstreerd. Bezoekers kunnen vragen stellen en direct feedback geven op de resultaten.
- API-labs, eveneens openbaar, geven developers van gemeenten en leveranciers de kans om met ondersteuning van het ZGW team te experimenteren met de API's. Ook hier kunnen uiteraard bugs en nieuwe wensen gemeld worden.
- Presentaties op de Leveranciersdag van VNG-Realisatie

Deze instrumenten tesamen zullen de openbare consultatie vormen/vervangen. Er zal dus sprake zijn van een voortdurende consultatie van de stakeholders, waarmee ook de kans ontstaat om de standaard voortdurend te verbeteren op aangeven van de gebruikers.

'Issues' en 'Pull Requests' zijn dus meer dan welkom.


## Problemen, suggesties en vragen

Het is niet nodig om software of documentatie te schrijven om toch bij te
dragen. De ontwikkeling is ook gebaat bij gerapporteerde problemen, suggesties
voor wijzigingen en vragen over dingen die (nog) onduidelijk zijn. Om dit te
doen kan een
[issue worden gemaakt](https://github.com/VNG-Realisatie/gemma-zaken/issues).
Op de supportpagina's van GitHub staat
[uitleg over het maken van issues](https://help.github.com/articles/creating-an-issue/).


## Documentatie en code

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


## Agile Scrum

Het team wat aan de ZGW API's werkt doet dit volgens de agile scrum methodiek.
Iedere sprint duurt vier weken. Gemeenten leveren user stories rond zaakgericht 
werken, welke vervolgens worden vertaald naar wat nodig is in de RESTful API 
specificatie.

### Scrum boards
Er worden vier scrum boards gebruikt om de flow naar resultaat in elke sprint
te faciliteren.

- [Scrum ZGW Voorbereiding](https://github.com/VNG-Realisatie/gemma-zaken/projects/1)
  Nieuwe user stories en issues komen hier op de backlog. Wanneer zij worden
  geprioriteerd komen ze in de flow om ze 'ready te maken' zodat ze opgepakt
  kunnen worden in de volgende sprint.

- [Scrum ZGW Realisatie Sprint x](https://github.com/VNG-Realisatie/gemma-zaken/projects/3)
  Vanuit de kolom "Ready for Sprint" worden tijdens de maandelijkse sprint
  planning userstories opgepakt die uitgevoerd gaan worden. Deze komen dan in
  de eerste kolom van het scrum board gericht op realisatie van de API
  specificatie.

- [Scrum ZGW Gereed Archief](https://github.com/VNG-Realisatie/gemma-zaken/projects/4)
  Op dit board is terug te vinden welke user story gereed was in welke sprint.

- [Organisatie & Impediments](https://github.com/VNG-Realisatie/gemma-zaken/projects/2)
  Op dit board bewaakt het team de voortgang van niet-inhoudelijke actiepunten
  en blokkades.

### Review

Zowel het board
[Scrum ZGW Voorbereiding](https://github.com/VNG-Realisatie/gemma-zaken/projects/1)
als
[Scrum ZGW Realisatie](https://github.com/VNG-Realisatie/gemma-zaken/projects/3)
bevat een kolom voor review. Tijdens de voorbereiding worden user stories
klaargemaakt om in een volgende sprint uitgevoerd te worden. Daar hoort een
review bij: voldoet de user story aan de Definition of Ready? Na de realisatie
vindt opnieuw een review plaats, van iedere Pull Request waarmee een wijziging
of toevoeging op de standaard wordt gedaan.

Reviews worden vaak aan specifieke personen gevraagd, maar iedereen kan een
review uitvoeren. Wanneer de beoordeling binnen je competenties valt, geef de
review dan prioriteit boven eventuele andere bijdragen zodat iedereen zo snel
mogelijk verder kan.
