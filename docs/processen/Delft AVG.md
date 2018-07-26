# Generieke beschrijving architectuur ZDS en Inzageverzoek AVG

In dit hoofdstuk wordt een architectuurschets gegeven voor de user stories voor het Inzage verzoek AVG van de gemeente Delft.

## User stories

* [User story #153](https://github.com/VNG-Realisatie/gemma-zaken/issues/153): Als burger wil ik een verzoek tot inzage in mijn persoonsgegevens kunnen doen via de website van de gemeente Delft.
* [User story #154](https://github.com/VNG-Realisatie/gemma-zaken/issues/154): Als burger wil ik de status en de relevante documenten van mijn in behandeling zijnde inzage verzoek kunnen inzien op de PIP van de gemeente Delft.

## Toelichting op [User story #153](https://github.com/VNG-Realisatie/gemma-zaken/issues/153)

Delft wil de inzageverzoeken AVG als zaak registreren en behandelen zodat alle betrokkenen vanuit eenzelfde informatiepositie kunnen worden voorzien van informatie. Het inzageverzoek wordt gedaan het webformulier dat de gemeente hiervoor heeft ontwikkeld. Het systeem voor webformulieren heet Volg Je Vraag (VJV). 

## Beknopte procesbeschrijving

Onderstaand proces toont het proces op hoofdlijnen:
Indienen inzageverzoek door de aanvrager
* Routeren van het verzoek naar de behandelaar door JZ Advies
* Behandelen van het verzoek door de behandelaar
* Opstellen van de beschikking door de behandelaar
* Versturen van de beschikking door de behandelaar
* Ontvangen van de beschikking door de aanvrager

![Proces](./bestanden/Delft-Inzageverzoek/Proces%20view%20Inzageverzoek%20AVG%20v2.png)

## Architectuurschets User Story
Inzageverzoeken voor de AVG worden afgehandeld door Advies JZ ondersteund door Volg je Vraag (VJV). Inzageverzoeken worden geregistreerd als zaak.
Een inzageverzoek kan voor specifieke domeinen worden aangevraagd (WOB, jeugd, participatie, Schuldhulpverlening, overig), of er kan een algemeen verzoek worden ingediend. 
De behandelaar controleert of de aanvraag voldoet aan de voorwaarden:
* Aanvrager is 16 jaar of ouder
* Aanvrager doet een inzageverzoek voor de eigen gegevens

Indien niet aan de voorwaarden wordt voldaan volgt een afwijzing.
De behandelaar verzamelt vervolgens de benodigde gegevens (verwerkingen). Waar worden deze bewaard? De ruwe verzameling komt uit verschillende bronnen. Gaat daar nog een bepaald filter overheen. Kan de ruwe verzameling gegevens bevatten waar de aanvrager geen toegang toe mag krijgen?
De behandelaar maakt de beschikking en stuurt deze naar de aanvrager.
De beschikking wordt per post verzonden. De aanvrager kan ervoor kiezen om deze ook digitaal te ontvangen.
Voor het verwerken van de aanvragen wordt VJV gebruikt. De aanvraag wordt tevens als zaak geregistreerd in de ZRC. Overige (voor de zaak relevante) informatie wordt ook opgenomen in de ZRC, de beschikking wordt geregistreerd in de DRC.

## Werking van de standaard
Volgens de productvisie zijn actoren (medewerkers, behandelaars en klanten) bezig met een proces en niet met zaakgericht werken. 
In de architectuurschets blijkt dit doordat de toepassing (en niet de actor) met de API’s communiceert bij de gegevens te verwerken uit de ZTC, ZRC en DRC (én ORC).
Dit betekent dat die toepassing moet weten hoe de verschillende API’s aangesproken moeten worden. Wat vergelijkbaar is met de huidige situatie waarin van procesapplicaties (voor b.v. vergunningen, re-integratie, uitkering etc.) verwacht wordt dat ze de huidige ZDS standaard ondersteunen om zaakgericht te kunnen werken/registreren.
Wij verwachten dat de nieuwe standaard continu in ontwikkeling zal blijven. Betekent dit dat procesapplicaties daar ook continu op moeten spelen
