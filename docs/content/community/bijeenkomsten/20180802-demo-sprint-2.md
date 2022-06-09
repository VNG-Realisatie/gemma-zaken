---
title: "Demo Sprint 2"
date: '3-8-2018'
---

Delft, 2 augustus 2018

## Presentatie

- Opening (@RitaBerghuis & @EdwinCoster)
- Introductie Context (@ehotting)
- Demo ZDS 2.0 (@joeribekker & @sergei-maertens)
- Resultaten sprint 2 (@boerbas)
- Vooruitkijken naar sprint 3 (@ehotting)
- Feedback (@TCIMEddy)

Slides: [ZDS2 Demo Spint 2.pdf](/community/bestanden/zds2-demo-sprint-2.pdf)

## Feedback

Alle reacties tijdens de demo zijn hieronder opgenomen, in de categoriën 'proces' en 'inhoudelijk'. Waar nodig zijn issues aangemaakt. Dit zijn de antwoorden van het scrum team.


### Proces

#### Wanneer is de nieuwe standaard klaar/bruikbaar?
Het is aan VNG Realisatie (als beheerder van de standaard) om ZDS 2.0 tot standaard te verheffen. Vooralsnog zijn de API's daar nog niet klaar voor. Daarnaast moet VNG Realisatie met de leveranciers nog bedenken hoe het vaststellen van dit type nieuwe standaarden precies werkt. Input is welkom op dit onderwerp! Voorzien is dat het scrum team in ieder geval een half jaar aan ZDS 2.0 werkt, tot eind 2018. Daarbij is de verwachting dat de API's al eerder bruikbaar zijn, maar wellicht nog niet tot standaard verheven.


#### Wanneer wordt nagedacht over implementatie en hoe wordt dat afgestemd met leveranciers?
Na de zomervakantie wordt een eerste meeting met leveranciers belegd waarin een aantal zaken wordt besproken, waaronder dit onderwerp. Zie issue [#280](https://github.com/VNG-Realisatie/gemma-zaken/issues/280).


#### Wie levert welke componenten in de nieuwe architectuur?
De referentie-implementaties worden geleverd door VNG Realisatie. Daadwerkelijke productiewaardige software wordt geleverd door de markt. Bij de ZDS 2.0 API's is het zo dat iedere component één of meerdere keren kan voorkomen in een architectuur. Het is aan de gemeente op welke manier men de architectuur wil vormgeven, met losse componenten van verschillende leveranciers of een enkele suite die alles oplost. Bij andere API-gebaseerde standaarden is dat wellicht anders en ligt in sommige gevallen een centrale component meer voor de hand.


#### Hoe borgen we dat het qua complexiteit niet explodeert?

Zie issue [#281](https://github.com/VNG-Realisatie/gemma-zaken/issues/281).


#### Hoe wordt de review gedaan? Welk proces?

Vooralsnog worden reviews binnen het scrum team uitgevoerd. Onderzocht wordt hoe het proces voor bredere review en bijdragen er uit moet zien. Onderkend wordt dat zo spoedig mogelijk verbreding nodig is. Zie hiervoor ook issue [#280](https://github.com/VNG-Realisatie/gemma-zaken/issues/280).


#### Wordt de inhoud van ZTC ook gestandaardiseerd?

Dit staat los van de standaard ZTC 2.0 en is buiten scope voor dit project. Wel is het goed om hier alvast over na te denken. Met de API's is het bijvoorbeeld eenvoudig om per proces een andere ZTC te hanteren. Het is goed denkbaar dat binnen een bepaald domein de processen zodanig gestandaardiseerd worden dat alle gemeenten voor die processen gebruik maken van een centrale ZTC. Zodra standaardisatie van de zaaktypen nuttig blijkt is het wellicht handiger voor die zaaktypen ook gebruik te maken van een centraal aangeboden ZTC. Interessante materie om gezamelijk te verkennen.


#### Referentie-implementaties vervullen voor API's de rol van het huidige StUF testplatform. Hoe krijgt software dan het stempel 'compliant'?
Onderkend wordt dat ook voor de nieuwe API's een mechanisme moet bestaan om software te valideren. Vooralsnog valt dit echter buiten scope van de opdracht aan het huidige scrum team. Zie issue [#263](https://github.com/VNG-Realisatie/gemma-zaken/issues/263).


#### Prioriteren jullie wel op basis van de hoogste businesswaarde voor NL?

Op dit moment wordt opportunistisch geprioriteerd, omdat feedback van gebruikers het meest belangrijk is. Daarom wordt voorrang gegeven aan user stories waarbij binnen gemeenten projecten lopen waarin de bijbehorende delen van de API direct toegepast kunnen worden. Het betreft hier de ontwikkeling van een standaard, de hoogste businesswaarde wordt geleverd wanneer de API's aantoonbaar implementeerbaar zijn en vanaf het begin een groot deel van de user stories afdekken. Daarbij zal het nodig zijn invulling te geven aan een flink deel van de RGBZ2, de volgorde waarin dit gebeurt is van minder belang.


#### Kan de locatie van demo's centraler, bijv. in Utrecht?

De zes demo's zijn ieder gepland in een gemeente die betrokken is bij het opstellen van de standaard. Op deze manier houden we de kosten van de organisatie laag en de betrokkenheid van de deelnemende gemeenten groot.


#### Dit soort demo's is leuk/zinvol!

Dank! Het is deel van de agile scrum-methodiek, waaraan we zo goed mogelijk invulling proberen te geven ondanks de uitdagingen qua werken op afstand en de grootte van het team. De demo's zijn erg belangrijk voor de transparantie over de voortgang, het controleren of in de juiste richting wordt gewerkt en om feedback op te halen.


#### Kunnen leveranciers ook zelf dingen in demo tonen?
Dit is iets te bespreken in de bijeenkomst met leveranciers, zie issue [#280](https://github.com/VNG-Realisatie/gemma-zaken/issues/280). We moeten zorgen dat enerzijds het speelveld voor alle leveranciers gelijk blijft, en anderzijds de betrokkenheid zo hoog mogelijk is en blijft. Er zijn allerlei opties, te denken valt bijvoorbeeld aan een demo's door een gemeente die een user story aan heeft gedragen voor uitbreiding van ZDS 2.0 en deze vervolgens intern door een leverancier laat implementeren.


#### Na beslissing in de Regiegroep is het een tijd stil geweest, waarom was er geen communicatie?

Punt is helder en doorgegeven aan VNG Realisatie.


#### Gaan we eisen (architectuur) dat alle zaaksystemen met componenten van anderen kunnen werken?

Ja, dat is wel expliciet de bedoeling. We standaardiseren op het niveau van de API specificaties. In de bijbehorende architectuur en afspraken zal o.a. staan dat componenten iedere los gedefinieerde API ook los moeten aanbieden. Een gevolg zal zijn dat zaaksystemen met componenten van anderen kunnen werken. Dit maakt een einde aan de huidige praktijk waarbij functionaliteit vaak onnodig redundant in organisaties aanwezig is, en waarbij data gekopieerd en gesynchroniseerd moet worden.

#### Is StUF end-of-life?

Nee, de transitie naar nieuwe standaarden kan niet in de vorm van een Big Bang. Er zal een lange periode zijn waarbij het nieuwe naast het oude bestaat. StUF blijft van groot belang. Wel is het zo dat gestreeft wordt naar een gegevenslandsschap, wat praktisch gezien alleen vorm kan krijgen wanneer we op de nieuw manier standaardiseren.


#### Zijn er naast ZDS nog meer standaarden in ontwikkeling op deze manier, en weten de verschillende initiatieven van elkaar?

Het ZDS 2.0 traject is het meest concreet aan het werk met een team, projectplan en budget. Daarnaast wordt gewerkt aan API's voor RSGB, qua proces op een andere manier. Verschillende betrokkenen bij ZDS 2.0 zijn ook daar bij betrokken. Nadere afstemming (ook over proces van realisatie) vindt voortdurend plaats.


### Inhoudelijk

#### Waar kunnen we de ‘zoemende’ API’s vinden?

|Specificatie|Referentie|
|---|---|
|[ZRC OAS](https://zaken-api.vng.cloud/api/v1/schema/)|[zoemende API](https://zaken-api.vng.cloud/api/v1/)|
|[ZTC OAS](https://documenten-api.vng.cloud/api/v1/schema/)|[zoemende API](https://documenten-api.vng.cloud/api/v1/)|
|[DRC OAS](https://catalogi-api.vng.cloud/api/v1/schema/)|[zoemende API](https://catalogi-api.vng.cloud/api/v1/)|


#### Referentie-implementatie van ZTC is leeg

Dat klopt, op dit moment worden updates van de software automatisch deployed maar is nog geen aandacht gegeven aan persistente inhoud. Het is wel mogelijk de ZTC te vullen met een administratieve interface, maar de autorisatie daarvoor deze wordt voor de referentie-implementatie niet vrijgegeven. Wanneer de software lokaal wordt gedraaid kan een super-user worden aangemaakt volgens de instructies. Issue [#279](https://github.com/VNG-Realisatie/gemma-zaken/issues/279) is aangemaakt om om te regelen dat er ofwel een standaard vulling van de ZTC komt, ofwel de mogelijkheid dit met de API zelf te doen.


#### Hoever gaan we in meenemen alle velden uit RGBZ2 en imZTC in de API's?

Dat is nu nog niet bekend. Vooralsnog breiden we de API's uit op basis van user stories, en komt er dus in wat nodig is. Daarna zal een fase komen waarbij we actief gaan kijken welke velden uit RGBZ2 er nog niet in zitten, en of er user stories zijn waar deze in gebruikt worden. Zo niet, dan blijven ze achterwege. Waarschijnlijk wordt de standaard kleiner dan de huidige, daarentegen zullen mogelijk ook wat compositie-API's worden toegevoegd om veelvoorkomende patronen te ondersteunen.


#### Wat zijn de beelden bij de scopes van de API's?

Autorisatie staat voor komende sprints op de planning. Gezocht wordt naar een balans tussen beheersbaarheid (= weinig verschillende scopes) en voldoende mogelijkheden om vertrouwelijkheid en integriteit te garanderen. Uitdaging rond data visibility kan worden opgelost door de afnemer zelf de mogelijkheid te geven te limiteren wat de API teruggeeft - met bijv. de ``?field=`` functionaliteit.


#### Wordt rekening gehouden met Multitenancy?

De API specificatie laat dit toe (net als RGBZ2), multitenancy heeft vooral te maken met de manier waarop geïmplementeerd wordt. In ieder geval kan één API endpoint meerdere organisaties faciliteren indien gewenst.


#### Hoe wordt de CMIS standaard in ZDS 2.0 verwerkt?

Zie hiervoor [#223](https://github.com/VNG-Realisatie/gemma-zaken/issues/223)

#### Seperation of concerns: wat doet welke component en wat mag worden verwacht van de basisinfra

[nog te beantwoorden]

#### Wat kunnen we verwachten van NLX/infra?

[nog te beantwoorden]

#### Hoe gaan we om met de coordinatenstelsels?

Dit staat beschreven in de DSO API strategie. Momenteel is er 1 stelsel
ondersteund, maar volgens DSO moeten er nog een EU- en Nederland-specifiek (RD)
stelsel ondersteund worden. Zie
[#216](https://github.com/VNG-Realisatie/gemma-zaken/issues/216) voor de DSO
checklist.

#### Wat is status van de referentieimplementatie?

    ->  We gaan de referentieimplementatie nog duiden en definieren


#### Concurrency/locking, hoe werkt dat?

Kort samengevat - hier is nog geen concrete beslissing over genomen.

Echter, dit is technisch in ieder geval mogelijk via het gebruik maken van
`ETag` headers - bij het uitgeven van een resource
krijg je een dergelijke tag en bij het aanpassen stuur je deze weer mee. De
waarde wijzigt als de resource wijzigt, dus als iemand anders ondertussen de
resource had gewijzigd, dan weet je dat jouw lokale kopie niet up-to-date is.

Zie bijvoorbeeld [optimistic locking](https://sookocheff.com/post/api/optimistic-locking-in-a-rest-api/)

Een alternatief zou expliciet locken/unlocken van een resource kunnen zijn,
maar dat introduceert wel een extra complexiteit en risico dat een lock nooit
vrijgegeven wordt, dus hier moet goed over nagedacht worden (= pessimistic locking).
