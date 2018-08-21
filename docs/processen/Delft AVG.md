# Generieke beschrijving architectuur ZDS en Inzageverzoek AVG

In dit hoofdstuk wordt een architectuurschets gegeven voor de user stories voor het Inzage verzoek AVG van de gemeente Delft.

## Overall user story

Als burger wil ik een inzageverzoek AVG doen via de website van de gemeente Delft. Verder wil ik op elk moment de status en relevante informatie (inclusief documenten) kunnen opvragen. Vooralsnog zijn hiervoor 2 specifieke user stories gedefinieerd:
* [User story #153](https://github.com/VNG-Realisatie/gemma-zaken/issues/153): Als burger wil ik een verzoek tot inzage in mijn persoonsgegevens kunnen doen via de website van de gemeente Delft.
* [User story #154](https://github.com/VNG-Realisatie/gemma-zaken/issues/154): Als burger wil ik de status en de relevante documenten van mijn inzage verzoek kunnen inzien op de PIP van de gemeente Delft.

## Architectuurschets
Delft gebruikt VJV voor het indienen en behandelen van de inzageverzoeken. Het verzoek wordt als zaak geregistreerd in de ZRC. Overige (voor de zaak relevante) informatie wordt opgenomen in de ZRC, DRC en de oplossing voor domeinspecifieke gegevens (ORC). De beschikking wordt geregistreerd in de DRC. Via de PIP kan de aanvrager  de status van de aanvraag inclusief de relevante informatie raadplegen.

![Architectuur](./bestanden/Delft-Inzageverzoek/Architectuurschets%20Inzageverzoek%20AVG.png)

## Toelichting op de generieke user story
Delft wil de inzageverzoeken AVG als zaak registreren en behandelen zodat alle betrokkenen vanuit eenzelfde informatiepositie kunnen worden voorzien van informatie. Het inzageverzoek wordt gedaan met het webformulier dat de gemeente hiervoor heeft ontwikkeld. Het systeem voor webformulieren heet Volg Je Vraag (VJV). 

### Huidige procesgang registreren en afhandelen inzageverzoek
Inzageverzoeken voor de AVG worden afgehandeld door Advies JZ ondersteund door Volg je Vraag (VJV). Inzageverzoeken worden (handmatig) geregistreerd als zaak in het DMS Verseon.
Een ‘gericht’ inzageverzoek wordt voor specifieke domeinen aangevraagd (WOB, jeugd, participatie, Schuldhulpverlening, overig), een aanvrager kan ook een ‘ongericht’ (algemeen) verzoek indienen. 

De behandelaar controleert of de aanvraag voldoet aan de voorwaarden:
* Aanvrager is 16 jaar of ouder
* Aanvrager doet een inzageverzoek voor de eigen gegevens

Indien niet aan de voorwaarden wordt voldaan volgt een afwijzing.

De behandelaar verzamelt vervolgens de benodigde gegevens (verwerkingen) bij deskundigen. Dit gebeurt m.b.v. e-mail. De behandelaar filtert de gegevens (b.v. gegevens van anderen mogen niet worden doorgestuurd) en stelt het overzicht samen. In bepaalde gevallen (b.v. dossiervorming) worden geen gegevens verstrekt, maar wordt de betrokkene uitgenodigd om het dossier te komen inzien. 

De behandelaar maakt de beschikking, voorziet deze van een handtekening en slaat deze op in Verseon. 

De beschikking wordt per post verzonden. De aanvrager kan ervoor kiezen om deze ook digitaal te ontvangen.

De behandelaar verwijdert de mailberichten van deskundigen na verwerking van de gegevens in het overzicht dat verstrekt wordt aan de klant. Het is onduidelijk of de deskundigen de (mailberichten met) aangeleverde gegevens verwijderen (wat wel zou moeten gebeuren).

### Nieuwe werkwijze registreren en afhandelen inzageverzoek
Onderstaand proces toont het proces op hoofdlijnen:
* Indienen inzageverzoek door de aanvrager
* Routeren van het verzoek naar de behandelaar door JZ Advies
* Toetsen van de voorwaarden door de behandelaar
* Controleren van de volledigheid (met eventueel verzoek tot aanvulling) door de behandelaar
* Verzamelen van de gegevens door de behandelaar
* Aanleveren van de gegevens door de deskundigen
* Opstellen van de beschikking door de behandelaar
* Versturen van de beschikking door de behandelaar
* Ontvangen van de beschikking door de aanvrager

Voor het verwerken van de aanvragen wordt VJV gebruikt. De aanvraag wordt tevens als zaak geregistreerd in de ZRC. Overige (voor de zaak relevante) informatie wordt ook opgenomen in de ZRC, DRC en de oplossing voor domeinspecifieke gegevens (ORC), de beschikking wordt geregistreerd in de DRC.

![Proces](./bestanden/Delft-Inzageverzoek/Proces%20view%20Inzageverzoek%20AVG%20v2.png)

* De aanvrager (initiator) dient via de website (VJV) een inzageverzoek persoonsgegevens in en geeft (na authenticatie via DigiD) op welke onderdelen geanalyseerd moeten worden. [US #153](https://github.com/VNG-Realisatie/gemma-zaken/issues/153);
* De VJV wordt, na correct en volledige registratie, toegewezen aan de afdeling ‘Advies JZ’ en geregistreerd in VJV, de ZRC  en de Domeinspecifieke gegevens. [US #153](https://github.com/VNG-Realisatie/gemma-zaken/issues/153), Status ‘Geregistreerd’.
* Advies JZ routeert de VJV naar de Behandelaar van inzageverzoeken. Dit wordt geregistreerd in VJV en de ZRC. US #..., geen statuswijziging;
Wij zouden graag zien dat deze actie uit het proces wordt gehaald omdat deze geen toegevoegde waarde heeft.
* De Behandelaar van inzageverzoeken controleert of aanvraag voldoet aan de voorwaarden. [US #301](https://github.com/VNG-Realisatie/gemma-zaken/issues/301), statuswijziging ‘Toetsing wet- en regelgeving afgerond’;
  * Indien dit niet het geval is volgt een afwijzing. Registratie in VJV, ZRC en DRC. [US #302](https://github.com/VNG-Realisatie/gemma-zaken/issues/302), statuswijziging ‘Afgehandeld’.
  * Indien dit wel het geval is controleert de Behandelaar of nog aanvullende gegevens nodig zijn (b.v. voor ‘Overige systemen’ en ‘Algemeen’);
    * Als er aanvullende gegevens nodig zijn, wordt per brief gevraagd om een precisering / aanvulling van het verzoek. Met een termijn van (b.v.) 2 weken. De behandeltermijn wordt met dezelfde termijn opgeschort. Registratie in VJV, ZRC en DRC. [US #303](https://github.com/VNG-Realisatie/gemma-zaken/issues/303), statuswijziging ‘Geaccepteerd’;
      * Nog afstemmen en uitbreiden met wat er gebeurt als de reactietermijn verstreken is. Gaan we rappelleren, of wordt het inzageverzoek afgehandeld?
    * Als de initiator aanvullende gegevens heeft verstrekt registreert de Behandelaar deze actie bij het inzageverzoek. Registratie in de ZRC en DRC. [US #304](https://github.com/VNG-Realisatie/gemma-zaken/issues/304).
  * Als er geen aanvullende gegevens (meer) nodig zijn, dan verzamelt de behandelaar de benodigde gegevens bij deskundigen. Registratie in VJV en ZRC. [US #305](https://github.com/VNG-Realisatie/gemma-zaken/issues/305), statuswijziging ‘In behandeling genomen’.

Idealiter worden hiervoor vanuit het ZAC taken toegewezen aan de diverse medewerkers die vervolgens hun resultaten toevoegen aan de Zaak, Registratie in de ZRC, DRC en ORC. Het resultaattype kan zijn:
    * Persoon komt niet voor;
    * Persoon komt voor met een overzicht van registraties. Een overzicht van de systemen waarin de persoon voorkomt volgens een vooraf vastgesteld formaat. Dit zou dus een vooraf gedefinieerd Informatieobjecttype kunnen zijn);
    * Persoon komt voor met informatieobject met een afschrift van een dossier of;
    * Persoon komt voor met een uitnodiging om een afspraak te maken om het dossier in te zien. Ook dit kan een informatieobject zijn met details over de te maken afspraak.

Het resultaat wordt opgeslagen in de Domeinspecifieke gegevens (AVG-rechten). Een afschrift van een dossier kan als informatieobject in de DRC worden opgenomen met vertrouwelijkheid ‘Zaakvertrouwelijk’. Een overzicht van systemen en eventueel een uitnodiging voor het inzien van het dossier, kunnen als Informatieobject in de DRC  worden opgenomen met de vertrouwelijkheid ‘Intern’. Mogelijk moet of kun je hier Informatie-objecttypen voor definiëren;

Ook hier met je wellicht nog iets met rappelleren…

* Een Deskundige moet zijn bevindingen kunnen inzien en wijzigen, [US #307](https://github.com/VNG-Realisatie/gemma-zaken/issues/307). Dit kan zolang niet alle Deskundigen hebben gereageerd en de status nog niet is igesteld op 'Advies ingewonnen'.
* Zodra alle deskundigen hebben gereageerd, stelt de Behandelaar dat in. Registratie in de ZRC, [US #308](https://github.com/VNG-Realisatie/gemma-zaken/issues/308), statuswijziging 'Advies ingewonnen';
* De Behandelaar start met het opstellen van de beschikking. De overzichten van systemen worden hierbij gecontroleerd en samengevoegd tot één overzicht. Registratie in VJV, ZRC en DRC. [US #309](https://github.com/VNG-Realisatie/gemma-zaken/issues/309), statuswijziging ‘Onderzoek afgerond’. De beschikking is een informatieobject met vertrouwelijkheid ‘Zaakvertrouwelijk’;
  * De Behandelaar stuurt de beschikking op naar de Aanvrager. Registratie in VJV, ZRC en DRC. [US #310](https://github.com/VNG-Realisatie/gemma-zaken/issues/310), statuswijziging ‘Afgehandeld’. Alle informatieobjecten met de vertrouwelijkheid ‘Intern’ kunnen nu verwijderd worden. 

### Vervolg
Bij de gemeente  Delft loopt een pilot voor het e-Depot. Delft test hierbij het scenario van uitplaatsing, waarbij zaken nadat ze zijn afgehandeld worden uitgeplaatst bij het e-Depot.
Dit betekent dat bij een eventueel bezwaar en beroep het e-Depot informatie uit de originele zaak levert en niet de combinatie ZRC/DRC/Domeinspecifieke gegevens. Delft wil graag onderzoeken wat dit betekent voor de standaard, wat dit betekent voor de ZAC (VJV), of de keuze voor uitplaatsing wel past bij het gebruik van de standaard

## User story opvragen status en relevante gegevens
De aanvrager moet op elk moment tussen aanvraag en afhandeling de status en relevante informatie kunnen opvragen. Dit is vervat in user story [US #154](https://github.com/VNG-Realisatie/gemma-zaken/issues/154).

## Werking van de standaard
Volgens de productvisie zijn actoren (medewerkers, behandelaars en klanten) bezig met een proces en niet met zaakgericht werken. 
In de architectuurschets blijkt dit doordat de toepassing (en niet de actor) met de API’s communiceert bij de gegevens te verwerken uit de ZTC, ZRC en DRC (én ORC/Domeinspecifieke gegevens/AVG-rechten).

Dit betekent dat die toepassing moet weten hoe de verschillende API’s aangesproken moeten worden. Wat vergelijkbaar is met de huidige situatie waarin van procesapplicaties (voor b.v. vergunningen, re-integratie, uitkering etc.) verwacht wordt dat ze de huidige ZDS standaard ondersteunen om zaakgericht te kunnen werken/registreren.

Wij verwachten dat de nieuwe standaard continu in ontwikkeling zal blijven. Betekent dit dat procesapplicaties daar ook continu op moeten spelen? of worden de specificaties in de API vooral uitgebreid en minder gewijzigd?
