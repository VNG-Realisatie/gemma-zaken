# Dimpact - Melding Openbare Ruimte

In dit hoofdstuk wordt een architectuurschets gegeven voor de user stories voor de Melding Openbare Ruimte (MOR). Het gaat om de volgende user stories.

## User stories

* [User story #169](https://github.com/VNG-Realisatie/gemma-zaken/issues/169): Als burger wil ik een melding openbare ruimte kunnen doen zodat de gemeente deze kan behandelen.
* [User story #139](https://github.com/VNG-Realisatie/gemma-zaken/issues/139): Als medewerker wil ik weten waar welk type melding openbare ruimte (categorie) is gedaan zodat ik de melding kan doorzetten naar de juiste behandelaar of ketenpartner.
* [User story #138](https://github.com/VNG-Realisatie/gemma-zaken/issues/138): Als gemeente wil ik een melding openbare ruimte over afval in het buitengebied automatisch laten routeren naar een afdeling of ketenpartner op basis van de locatie en de categorie van de melding zodat ik een efficiëntere bedrijfsvoering verkrijg.
* [User story #137](https://github.com/VNG-Realisatie/gemma-zaken/issues/137): Als manager wil ik een rapportage kunnen maken van meldingen in de openbare ruimte zodat ik kan achterhalen hoe vaak welke categorie meldingen in welke straat, buurt of wijk voorkomen.
* [User story #111](https://github.com/VNG-Realisatie/gemma-zaken/issues/111): Als behandelaar van een melding openbare ruimte wil ik kunnen zoeken naar zaken en contacten die betrekking hebben op meldingen in hetzelfde gebied van dezelfde categorie of over hetzelfde probleem gaan zodat ik dubbele meldingen kan afhandelen en meldingen kan plannen en routeren voor onze medewerkers in het veld (of voor een ketenpartner).


Samenvallend met meldingen overlast op het water de volgende user stories:
* [User story #52](https://github.com/VNG-Realisatie/gemma-zaken/issues/52): Als behandelaar wil ik locatie- en/of objectinformatie bij de melding ontvangen zodat ik voldoende details weet om de melding op te volgen.
* [User story #51](https://github.com/VNG-Realisatie/gemma-zaken/issues/51): Als behandelaar wil de status van de zaak / melding kunnen aanpassen zodat de actuele status voor de betrokkenen inzichtelijk is.
* [User story #45](https://github.com/VNG-Realisatie/gemma-zaken/issues/45): Als KCC medewerker wil ik een behandelaar kunnen toewijzen zodat de melding kan worden gerouteerd.
* [User story #42](https://github.com/VNG-Realisatie/gemma-zaken/issues/42): Als burger wil ik alle meldingen kunnen inzien in mijn omgeving, binnen mijn gemeente zodat ik weet wat er speelt of dat een melding al gedaan is.
* [User story #40](https://github.com/VNG-Realisatie/gemma-zaken/issues/40): Als burger wil ik weten wat de gemeente met mijn melding gaat doen zodat ik weet of mijn melding naar wens wordt opgepakt.


## Toelichting user stories
Het gaat hier om een aantal user stories voor Melding Openbare Ruimte. De meeste Dimpact-gemeenten maken gebruik van de Atos e-Suite voor de intake en behandeling van meldingen over de openbare ruimte. Daartoe hebben zij in de e-Suite een e-dienst ingericht die bestaat uit een e-formulier met een zaakafhandelproces. De meldingen worden volledig zaakgericht afgehandeld en de burger kan de voortgang volgen via het Mijn Loket gedeelte van de e-Suite; bovendien kan hij e-mail notificaties over de voortgang van de melding. Medewerkers beoordelen de melding en zetten deze door naar behandelaars of naar een ketenpartner. Er zijn managementrapportages ingericht met JasperServer die bijv. inzicht geven in het aantal meldingen per categorie, het voldoen aan servicelevels, etc.

Daarnaast blijken de user stories van Dimpact voor de MOR samen te vallen met een aantal user stories van Amsterdam voor melding van overlast op water. Deze zijn ook vermeld maar niet verwerkt in de analyse die hierna volgt.


## Architectuurschets
De architectuurschets geeft de nieuwe versie van Zaak- Documentservices 2.0 weer; deze bestaat in feite uit drie API specificaties, t.w. die voor Zaaktypen, Zaken en Documenten. Deze API's worden aangeboden (gerealiseerd) door resp. de componenten Zaaktypecatalogus (ZTC), Zaakregistratiecomponent (ZRC) en Documentregistratiecomponent (DRC). Hieronder staan twee architectuurmodellen. Het linker model geeft de specifieke situatie bij Dimpact weer met gebruik van de Atos e-Suite. Het rechter model geeft de situatie weer in het algemene geval.

| ![Architectuurschets t.b.v. Dimpact MOR](./bestanden/Dimpact/apis-componenten-dimpact.png?raw=true) | ![Architectuurschets t.b.v. Dimpact MOR](./bestanden/Dimpact/apis-componenten-generiek.png?raw=true) |
| --- | --- |
| Architectuurschets t.b.v. Dimpact MOR | Architectuurschets MOR generiek |

De burger kan gebruik maken van een formulier om een melding te maken, maar ook van een specifieke app zoals BuitenBeter of Slim Melden. Deze apps sluiten op de ZRC aan net als de e-formulieren(voorziening).

Medewerkers maken gebruik van het Medewerkerportaal van de e-Suite. Dit is in feite een generieke Zaakafhandelcomponent (ZAC).

Managers maken ook gebruik van het Medewerkerportaal o.a. om de werkvoorraad te verdelen, te plannen en om de voortgang te bewaken. Hiervoor kunnen zij gebruik maken van managementrapportages die realtime informatie uit de ZRC verwerken.


## Beknopte Procesbeschrijving
Het MOR-proces is een vrij eenvoudig proces dat start met een melding door de burger. De afhandeling door ketenpartners is niet uitgewerkt.
1. Burger vult een formulier in of gebruikt een app om een melding openbare ruimte te doen. Hij kan daarbij zien welke meldingen al gedaan zijn in het gebied waarin hij zich bevindt. Ook kan hij een bestaande melding aanklikken om deze te "liken" (bevestigen).
2. De medewerker krijgt de melding in zijn werkvoorraad en beoordeelt deze. Ook de medewerker kan de melding op een kaartje zien samen met andere meldingen in hetzelfde gebied. Als de melding voldoende gegevens bevat voor behandeling (en valt onder verantwoordelijkheid van de gemeente), dan maakt de medewerker een zaak aan.
3. De zaak wordt voor behandeling doorgezet naar een medewerker, afdeling (of externe ketenpartner).
4. Als de melding is afgehandeld krijgt de burger een terugmelding (bijv. via e-mail)

Deze procesbeschrijving overstijgt de user stories; deze kunnen a.h.w. geplaatst worden in het proces.

![Bedrijfsproces i.r.t. API's](./bestanden/Dimpact/mor-proces.png?raw=true)


## Generieke architectuurschets (GEMMA-referentiecomponenten)
De architectuurschets van het proces is reeds in termen van GEMMA 2 referentiecomponenten.


## Benodigde APIs per user story

| User story | API | Functionaliteit |
|:------------|:-----|:-----------------|
| [User story #169](https://github.com/VNG-Realisatie/gemma-zaken/issues/169): Als burger wil ik een melding openbare ruimte kunnen doen zodat de gemeente deze kan behandelen. | DRC API, ZRC API | Ophalen meldingen in hetzelfde gebied, Het registreren van een melding (leidt tot een document/informatieobject) |
| [User story #139](https://github.com/VNG-Realisatie/gemma-zaken/issues/139): Als medewerker wil ik weten waar welk type melding openbare ruimte (categorie) is gedaan zodat ik de melding kan doorzetten naar de juiste behandelaar of ketenpartner. | DRC API, ZRC API | Behandelaar aanpassen, status bijwerken, ophalen meldingen in hetzelfde gebied |
| [User story #138](https://github.com/VNG-Realisatie/gemma-zaken/issues/138): Als gemeente wil ik een melding openbare ruimte over afval in het buitengebied automatisch laten routeren naar een afdeling of ketenpartner op basis van de locatie en de categorie van de melding zodat ik een efficiëntere bedrijfsvoering verkrijg. | DRC API | Behandelaar aanpassen, status bijwerken | 
| [User story #137](https://github.com/VNG-Realisatie/gemma-zaken/issues/137): Als manager wil ik een rapportage kunnen maken van meldingen in de openbare ruimte zodat ik kan achterhalen hoe vaak welke categorie meldingen in welke straat, buurt of wijk voorkomen. | ZRC API, DRC API, ZTC API | Selecties ophalen van zaken en/of documenten op basis van criteria als zaaktype, categorie, locatie, trefwoorden. Filteren op basis van servicenormen uit de ZTC |
| [User story #111](https://github.com/VNG-Realisatie/gemma-zaken/issues/111): Als behandelaar van een melding openbare ruimte wil ik kunnen zoeken naar zaken en contacten die betrekking hebben op meldingen in hetzelfde gebied van dezelfde categorie of over hetzelfde probleem gaan zodat ik dubbele meldingen kan afhandelen en meldingen kan plannen en routeren voor onze medewerkers in het veld (of voor een ketenpartner). | ZRC API, DRC API | Zoeken naar meldingen op basis van zaaktype, locatie, categorie, etc.  ||




