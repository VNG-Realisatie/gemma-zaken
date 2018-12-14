---
title: Generieke beschrijving architectuur ZDS en Inzageverzoek AVG
date: 26-6-2018
---

In dit hoofdstuk wordt een architectuurschets gegeven voor de user stories voor het Inzage verzoek AVG van de gemeente Delft.

## Overall user story

Als burger wil ik een inzageverzoek AVG doen via de website van de gemeente Delft. Verder wil ik op elk moment de status en relevante informatie (inclusief documenten) kunnen opvragen. 

Als behandelaar wil ik:
* vaststellen dat het verzoek aan wet- en regelgeving voldoet (en een verzoek wat daar niet aan voldoet afwijzen); 
* vaststellen of ik het verzoek in behandeling kan nemen; 
* de aanvrager om aanvullende informatie vragen; 
* als de aanvrager niet reageert wil ik het verzoek buiten behandeling stellen; 
* het onderzoek starten en de deskundigen vragen hun domein te onderzoeken op de persoonsgegevens van de aanvrager; 
* een beschikking opstellen en deze versturen.

Als deskundige wil het resultaat van  mijn analyse kunnen toevoegen en, indien nodig, aanpassen

## Architectuurschets
Delft gebruikt VJV voor het indienen en behandelen van de inzageverzoeken. Het verzoek wordt als zaak geregistreerd in de ZRC. Overige (voor de zaak relevante) informatie wordt opgenomen in de ZRC, DRC en de oplossing voor domeinspecifieke gegevens (ORC). De beschikking wordt geregistreerd in de DRC. Via de PIP kan de aanvrager  de status van de aanvraag inclusief de relevante informatie raadplegen.

![Architectuur](./bestanden/Delft-Inzageverzoek/Architectuurschets%20Inzageverzoek%20AVG.png)

## Toelichting op de generieke user story
Delft wil de inzageverzoeken AVG als zaak registreren en behandelen zodat iedereen die dat wil hun recht kan uitoefenen om inzicht te krijgen in de verwerking van hun persoonsgegevens. Het verzoek wordt gedaan met het webformulier dat de gemeente hiervoor heeft ontwikkeld. Het systeem voor webformulieren heet Volg Je Vraag (VJV). 

### Huidige procesgang registreren en afhandelen inzageverzoek
Inzageverzoeken voor de AVG worden afgehandeld door Advies JZ ondersteund door Volg je Vraag (VJV). Inzageverzoeken worden (handmatig) geregistreerd als zaak in het DMS Verseon.

Een inzageverzoek wordt voor domeinen aangevraagd (WMO, Jeugd, Participatie, Schuldhulpverlening, Overig en Algemeen).

De behandelaar controleert of de aanvraag voldoet aan de voorwaarden:
* Aanvrager is 16 jaar of ouder
* Aanvrager staat niet onder curatele

De aanvrager doet daarbij een inzageverzoek voor de eigen gegevens of voor de gegevens van:
* een kind jonger dan 16 jaar waarvan de aanvrager de wettelijke vertegenwoordiger is, of;
* iemand ouder dan 16 die niet onder curatele staat en een schriftelijke volmacht heeft gegeven aan de aanvrager

Indien niet aan de voorwaarden wordt voldaan volgt een afwijzing. Dit is een besluit in de vorm van een beschikking vervat in een document.

De behandelaar verzamelt vervolgens de benodigde gegevens (verwerkingen) bij deskundigen. Dit gebeurt m.b.v. e-mail. De behandelaar redigeert de gegevens (omdat b.v. gegevens van anderen niet mogen  worden doorgestuurd) en stelt het overzicht samen. In bepaalde gevallen (b.v. dossiervorming) worden geen gegevens verstrekt, maar wordt de betrokkene uitgenodigd om het dossier te komen inzien.

De behandelaar maakt de beschikking, voorziet deze van een handtekening en slaat deze (handmatig) op in Verseon.

De beschikking wordt per post verzonden.

De behandelaar verwijdert de mailberichten van deskundigen na verwerking van de gegevens in het overzicht dat verstrekt wordt aan de klant. Het is onduidelijk of de deskundigen de (mailberichten met) aangeleverde gegevens verwijderen (wat wel zou moeten gebeuren).

### Nieuwe werkwijze registreren en afhandelen inzageverzoek
Onderstaand proces toont het proces op hoofdlijnen:
* Indienen inzageverzoek door de aanvrager, dit verzoek wordt automatisch gerouteerd naar de VJV-behandelaar ‘Advies JZ’;
* Toetsen aan wet- en regelgeving door de behandelaar, en afwijzen indien dit niet voldoet;
* Controleren van de volledigheid door de behandelaar;
* Eventueel de aanvrager om aanvullende informatie vragen door de behandelaar, het registreren van de reactie en het verzoek buiten behandeling stellen als de aanvrager niet tijdig reageert;
* Starten van het verzamelen van de gegevens door de behandelaar;
* Aanleveren van de gegevens (en eventueel wijzigen van die gegevens) door de deskundigen;
* Opstellen van de beschikking door de behandelaar;
* Versturen van de beschikking door de behandelaar;
* Ontvangen van de beschikking door de aanvrager

Voor het verwerken van de aanvragen wordt VJV gebruikt. De aanvraag wordt tevens als zaak geregistreerd in de ZRC. Overige (voor de zaak relevante) informatie wordt ook opgenomen in de ZRC, DRC en ORC/AVG-Rechten (de oplossing voor domeinspecifieke gegevens), het besluit wordt geregistreerd in de BRC.

![Proces](./bestanden/Delft-Inzageverzoek/Proces%20view%20Inzageverzoek%20AVG%20v2.png)

* De aanvrager (initiator) dient via de website (VJV) een inzageverzoek persoonsgegevens in en bepaalt (na authenticatie via DigiD) welke onderdelen geanalyseerd moeten worden. [US #153](https://github.com/VNG-Realisatie/gemma-zaken/issues/153);
* De VJV wordt, na correct en volledige registratie, toegewezen aan de afdeling ‘Advies JZ’ en geregistreerd in VJV, de ZRC en de ORC/AVG-Rechten. [US #153](https://github.com/VNG-Realisatie/gemma-zaken/issues/153), Status ‘Geregistreerd’.
* De Behandelaar van inzageverzoeken controleert of aanvraag voldoet aan de voorwaarden. [US #301](https://github.com/VNG-Realisatie/gemma-zaken/issues/301), statuswijziging ‘Toetsing wet- en regelgeving afgerond’;
  * Indien dit niet het geval is volgt een afwijzing. Registratie in VJV, ZRC en DRC. [US #302](https://github.com/VNG-Realisatie/gemma-zaken/issues/302), statuswijziging ‘Afgehandeld’.
  * Indien dit wel het geval is controleert de Behandelaar of nog aanvullende gegevens nodig zijn (b.v. voor ‘Overige systemen’ en ‘Algemeen’);
    * Als er aanvullende gegevens nodig zijn, wordt per brief gevraagd om een precisering / aanvulling van het verzoek. Met een termijn van (b.v.) 2 weken. De behandeltermijn wordt met dezelfde termijn opgeschort. Registratie in VJV, ZRC en DRC. [US #303](https://github.com/VNG-Realisatie/gemma-zaken/issues/303), statuswijziging ‘Geaccepteerd’;
      * Als de Aanvrager niet binnen de gestelde termijn reageert wordt het verzoek buiten behandeling gesteld. US #..., statuswijziging 'Afgehandeld';
      * Als de initiator aanvullende gegevens heeft verstrekt registreert de Behandelaar deze actie bij het inzageverzoek. Registratie in de ZRC en DRC en de ORC/AVG-rechten. [US #304](https://github.com/VNG-Realisatie/gemma-zaken/issues/304).
  * Als er geen aanvullende gegevens (meer) nodig zijn, dan start de behandelaar het onderzoek om de gegevens bij deskundigen. Registratie in VJV en ZRC. [US #305](https://github.com/VNG-Realisatie/gemma-zaken/issues/305), statuswijziging ‘In behandeling genomen’.

Vanuit VJV worden taken toegewezen aan de diverse medewerkers die vervolgens hun onderzoeksresultaten toevoegen, Registratie in de ZRC, DRC en ORC/AVG-rechten, [US #306](https://github.com/VNG-Realisatie/gemma-zaken/issues/306). Het type onderzoeksresultaat kan zijn:
* Persoon komt niet voor;
* Persoon komt voor met een overzicht van registraties. Een overzicht van de systemen waarin de persoon voorkomt volgens een vooraf vastgesteld formaat. Dit zou dus een vooraf gedefinieerd Informatieobjecttype kunnen zijn);
* Persoon komt voor met informatieobject met een afschrift van een dossier of;
* Persoon komt voor met een uitnodiging om een afspraak te maken om het dossier in te zien. Ook dit kan een informatieobject zijn met details over de te maken afspraak.

Het resultaat wordt opgeslagen in de ORC (AVG-Rechten). Een afschrift van een dossier komt als informatieobject in de DRC met vertrouwelijkheid ‘Zaakvertrouwelijk’. Een overzicht van systemen komt als informatieobject in de DRC met vertrouwelijkheid ‘Intern’.  De details voor een uitnodiging kunnen opgenomen worden in de ORC/AVG-Rechten.

*Ook hier met je wellicht nog iets met rappelleren…

* Een Deskundige moet zijn bevindingen kunnen inzien en wijzigen, [US #307](https://github.com/VNG-Realisatie/gemma-zaken/issues/307). Dit kan zolang de status van (de zaak van) het inzageverzoek nog niet is igesteld op 'Advies ingewonnen';
* Zodra alle deskundigen hebben gereageerd, stelt de Behandelaar dat in. Registratie in de ZRC, [US #308](https://github.com/VNG-Realisatie/gemma-zaken/issues/308), statuswijziging 'Advies ingewonnen';
* De Behandelaar start met het opstellen van het Besluit/de Beschikking. De overzichten van systemen worden hierbij gecontroleerd en samengevoegd tot één overzicht. Registratie in VJV, ZRC en DRC. [US #309](https://github.com/VNG-Realisatie/gemma-zaken/issues/309), statuswijziging ‘Onderzoek afgerond’. De Beschikking is vastgelegd in een Informatieobject van Informatieobjecttype 'Verstuurde persoonsgegevens' met vertrouwelijkheid ‘Zaakvertrouwelijk’;
* De Behandelaar zorgt ervoor dat de Beschikking ondertekent wordt en stuurt de Beschikking naar de Aanvrager. Registratie in VJV, ZRC en DRC. [US #310](https://github.com/VNG-Realisatie/gemma-zaken/issues/310), statuswijziging ‘Afgehandeld’. 

*Openstaade vraag is of alle informatieobjecten met de vertrouwelijkheid ‘Intern’ nu verwijderd kunnen worden (check op tijdreizen.

### User story opvragen status en relevante gegevens
De aanvrager moet op elk moment tussen aanvraag en afhandeling de status en relevante informatie kunnen opvragen. Dit is vervat in user story [US #154](https://github.com/VNG-Realisatie/gemma-zaken/issues/154).

## Informatiemodel AVG-Rechten

![Informatiemodel](./bestanden/Delft-Inzageverzoek/Class%20Diagram%20AVG%20Inzageverzoek.png)

Dit model dient vooral om duidelijk te maken waar het autorisatievraagstuk leeft voor AVG rechten. Dit is versie 1.0 dus ik verwacht wel wat feedback.

### Samengevat
In Gebruiker, GebruikerOnderzoeksdomein en Onderzoeksdomein wordt gedefinieerd wie welk domein onderzoekt, in Inzageverzoek, Onderzoeksvraag en OnderzoeksvraagInformatieobject wordt dat gedaan.

De autorisatievraagstukken:
* Vanwege het gevoelige en bijzondere karakter van deze gegevens mag een Deskundige alleen de gegevens bekijken en wijzigen voor zijn/haar eigen domein;
* Een deskundige mag zijn/haar gegevens alleen wijziging zolang de zaak nog niet de status ‘Onderzoek afgerond’ of hoger heeft.

### De definitie
Voordat er een Inzageverzoek kan worden ingediend moet dus gedefinieerd zijn wie de antwoorden levert. Dit is afhankelijk van de te onderzoeken domeinen (WMO, Jeugd, participatie, schuld etc.). 

Onderzoeksdomein definieert de domeinen. GebruikerOnderzoeksdomein bepaalt welke Gebruiker dit domein onderzoekt. Die Gebruiker is een Medewerker met Roltype ‘Deskundige’. Maar er zijn meer Gebruikers, we hebben b.v. ook een Behandelaar.

### Registratie en behandelen
Bij de registratie van een Inzageverzoek worden de te onderzoeken domeinen vastgelegd in Onderzoeksvraag. Per Onderzoeksvraag worden het Onderzoeksdomein en de Gebruiker opgehaald uit GebruikerOnderzoeksdomein.

Zodra de Behandelaar het onderzoek start, krijgen alle Deskundigen een taak om hun domein te analyseren. Het resultaat daarvan wordt vastgelegd in  Onderzoeksvraag en eventueel in OnderzoeksvraagInformatieobject. Dit Informatieobject is opgeslagen in de DRC. Het resultaat is van een OnderzoeksresultaatType. Dit is een enumeratie met de volgende waarden:
* Persoon komt niet voor;
* Persoon komt voor met een overzicht van registraties (in een Informatieobject)
* Persoon komt voor met een afschrift van een dossier (in een Informatieobject)
* Persoon komt voor met een uitnodiging om het dossier in te komen zien (waarvan een details opgenomen kunnen worden in OnderzoeksresultaatToelichting). 

### De relatie met het autorisatievraagstuk
De relatie met autorisatie is dat:
* De ZAC voor elke deskundige op record niveau kan bepalen wie welke gegevens mag inzien en wijzigen. Voor Onderzoeksvraag en OnderzoeksvraagInformatieobject in AVG-Rechten en Informatieobject in de DRC. Als ik het goed begrijp gaan we dat met scopes ook vastleggen;
* De ZAC op basis van de Status van de Zaak kan bepalen of gegevens alleen gelezen of ook gewijzigd mogen worden. Dat zie ik niet met scopes gebeuren;

## Vervolg
Bij de gemeente Delft loopt een pilot voor het e-Depot. Delft test hierbij het scenario van uitplaatsing, waarbij zaken nadat ze zijn afgehandeld worden uitgeplaatst bij het e-Depot.
Dit betekent dat bij een eventueel bezwaar en beroep het e-Depot informatie uit de originele zaak levert en niet de combinatie ZRC/DRC/Domeinspecifieke gegevens. Delft wil graag onderzoeken wat dit betekent voor de standaard, wat dit betekent voor de ZAC (VJV), of de keuze voor uitplaatsing wel past bij het gebruik van de standaard.
Verder komt 'uitgeplaatst' niet voor in de enumeratie voor archiefstatus. Er is wel een archiefstatus voor 'overgedragen', maar of dat fundamentalistisch correct is.

## Werking van de standaard
Volgens de productvisie zijn actoren (medewerkers, behandelaars en klanten) bezig met een proces en niet met zaakgericht werken.

In de architectuurschets blijkt dit doordat de ZAC (en niet de actor) met de API’s communiceert bij de gegevens te verwerken uit de ZTC, ZRC, DRC, BRC (én ORC/AVG-Rechten).

Dit betekent dat die toepassing moet weten hoe de verschillende API’s aangesproken moeten worden. Wat vergelijkbaar is met de huidige situatie waarin van procesapplicaties (voor b.v. vergunningen, re-integratie, uitkering etc.) verwacht wordt dat ze de huidige ZDS standaard ondersteunen om zaakgericht te kunnen werken/registreren.

Wij verwachten dat de nieuwe standaard continu in ontwikkeling zal blijven. Betekent dit dat procesapplicaties daar ook continu op moeten spelen? of worden de specificaties in de API vooral uitgebreid en minder gewijzigd?
