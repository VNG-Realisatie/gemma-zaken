# Generieke beschrijving architectuur ZDS en Inzageverzoek AVG

In dit hoofdstuk wordt een architectuurschets gegeven voor de user stories voor het Inzage verzoek AVG van de gemeente Delft.

## User stories

* [User story #153](https://github.com/VNG-Realisatie/gemma-zaken/issues/153): Als burger wil ik een verzoek tot inzage in mijn persoonsgegevens kunnen doen via de website van de gemeente Delft.
* [User story #154](https://github.com/VNG-Realisatie/gemma-zaken/issues/154): Als burger wil ik de status en de relevante documenten van mijn in behandeling zijnde inzage verzoek kunnen inzien op de PIP van de gemeente Delft.

## Toelichting op userstory 153 Als burger wil ik een inzageverzoek AVG willen doen via de website van de gemeente Delft

Delft wil de inzageverzoeken AVG als zaak registreren en behandelen zodat alle betrokkenen vanuit eenzelfde informatiepositie kunnen worden voorzien van informatie. Het inzageverzoek wordt gedaan het webformulier dat de gemeente hiervoor heeft ontwikkeld. Het systeem voor webformulieren heet Volg Je Vraag (VJV). 

## Beknopte procesbeschrijving

Onderstaand proces toont het proces op hoofdlijnen:
•	Indienen inzageverzoek door de aanvrager
•	Routeren van het verzoek naar de behandelaar door JZ Advies
•	Behandelen van het verzoek door de behandelaar
•	Opstellen van de beschikking door de behandelaar
•	Versturen van de beschikking door de behandelaar
•	Ontvangen van de beschikking door de aanvrager

![Bedrijfsproces i.r.t. API's](.\Delft-Inzageverzoek/Proces%20view%20Inzageverzoek%20AVG.png?raw=true)

## Architectuurschets
De architectuurschets geeft de nieuwe versie van Zaak- Documentservices 2.0 weer; deze bestaat in feite uit drie API specificaties, t.w. die voor Zaaktypen, Zaken en Documenten. Deze API's worden aangeboden (gerealiseerd) door resp. de componenten Zaaktypecatalogus (ZTC), Zaakregistratiecomponent (ZRC) en Documentregistratiecomponent (DRC). 

![Architectuurschets t.b.v. Dimpact MOR](./bestanden/Dimpact/apis-componenten.png?raw=true)

De burger kan gebruik maken van een formulier om een melding te maken, maar ook van een specifieke app zoals BuitenBeter of Slim Melden. Deze apps sluiten op de ZRC aan net als de e-formulieren(voorziening).

Medewerkers maken gebruik van het Medewerkerportaal van de e-Suite. Dit is in feite een generieke Zaakafhandelcomponent (ZAC).

Managers maken ook gebruik van het Medewerkerportaal o.a. om de werkvoorraad te verdelen, te plannen en om de voortgang te bewaken. Hiervoor kunnen zij gebruik maken van managementrapportages die realtime informatie uit de ZRC verwerken.


## Beknopte Procesbeschrijving
1. Het MOR-proces is een vrij eenvoudig proces dat start met een melding door de burger. Burger vult een formulier in of gebruikt een app om een melding openbare ruimte te doen. Hij kan daarbij zien welke meldingen al gedaan zijn in het gebied waarin hij zich bevindt. Ook kan hij een bestaande melding aanklikken om deze te "liken" (bevestigen).
2. De medewerker krijgt de melding in zijn werkvoorraad en beoordeelt deze. Ook de medewerker kan de melding op een kaartje zien samen met andere meldingen in hetzelfde gebied. Als de melding voldoende gegevens bevat voor behandeling (en valt onder verantwoordelijkheid van de gemeente), dan maakt de medewerker een zaak aan.
3. De zaak wordt voor behandeling doorgezet naar een medewerker, afdeling of externe ketenpartner.
4. Als de melding is afgehandeld krijgt de burger een terugmelding (bijv. via e-mail)

Deze procesbeschrijving overstijgt de user stories; deze kunnen a.h.w. geplaatst worden in het proces.

![Bedrijfsproces i.r.t. API's](./bestanden/Dimpact/mor-proces.png?raw=true)


## Generieke architectuurschets (GEMMA-referentiecomponenten)
Architectuurschetsen zijn reeds in termen van GEMMA 2 referentiecomponenten.


## Benodigde APIs per user story

| User story | API | Functionaliteit |
|:------------|:-----|:-----------------|
| [User story #169](https://github.com/VNG-Realisatie/gemma-zaken/issues/169): Als burger wil ik een melding openbare ruimte kunnen doen zodat de gemeente deze kan behandelen. | DRC API, ZRC API | Ophalen meldingen in hetzelfde gebied, Het registreren van een melding (leidt tot een document/informatieobject) |
| [User story #139](https://github.com/VNG-Realisatie/gemma-zaken/issues/139): Als medewerker wil ik weten waar welk type melding openbare ruimte (categorie) is gedaan zodat ik de melding kan doorzetten naar de juiste behandelaar of ketenpartner. | DRC API, ZRC API | Behandelaar aanpassen, status bijwerken, ophalen meldingen in hetzelfde gebied |
| [User story #138](https://github.com/VNG-Realisatie/gemma-zaken/issues/138): Als gemeente wil ik een melding openbare ruimte over afval in het buitengebied automatisch laten routeren naar een ketenpartner op basis van de locatie en de categorie van de melding zodat ik een efficiëntere bedrijfsvoering verkrijg. | DRC API | Behandelaar aanpassen, status bijwerken | 
| [User story #137](https://github.com/VNG-Realisatie/gemma-zaken/issues/137): Als manager wil ik een rapportage kunnen maken van meldingen in de openbare ruimte zodat ik kan achterhalen hoe vaak welke categorie meldingen in welke straat, buurt of wijk voorkomen. | ZRC API, DRC API, ZTC API | Selecties ophalen van zaken en/of documenten op basis van criteria als zaaktype, categorie, locatie, trefwoorden. Filteren op basis van servicenormen uit de ZTC |
| [User story #111](https://github.com/VNG-Realisatie/gemma-zaken/issues/111): Als behandelaar van een melding openbare ruimte wil ik kunnen zoeken naar zaken en contacten die betrekking hebben op meldingen in hetzelfde gebied van dezelfde categorie of over hetzelfde probleem gaan zodat ik dubbele meldingen kan samenvoegen en meldingen kan plannen en routeren voor onze medewerkers in het veld (of voor een ketenpartner). | ZRC API, DRC API | Zoeken naar meldingen op basis van zaaktype, locatie, categorie, etc.  ||


