---
title: "Verzoeken"
date: '18-12-2019'
weight: 70
---

# Inleiding
Een verzoek is een aanvraag of opdracht aan de gemeente (of andere overheid) voor de levering van een product of dienst. Verzoeken vormen dus de schakel tussen de klant, producten en diensten van de gemeente zoals in de PDC staan, en het zaakgericht werken voor de afhandeling. Het concept verzoeken is voor het eerst geintroduceerd in GFO Zaken, maar had in het opvolgende informatiemodel RGBZ geen plaats. In de visie van VNG Realisatie is dat echter een omissie (redenen zijn hieronder gegeven), en daarom is er behoefte aan een concept dat vooraf gaat aan de daadwerkelijke behandeling in een zaak (of andere activiteit).

Met verzoeken introduceren we een nieuw concept in het zaakgericht werken. Voor het bepalen van de functionaliteit die een eerste implementatie van de Verzoeken API moet bieden, gaan we uit van de ingediende user stories en andere/eerdere implementaties van het begrip 'verzoeken' (zie de bronnenlijst onderaan). Op basis daarvan kan een eerste set ontwerpbeslissingen en uitgangspunten worden opgesteld. Die zijn in dit document beschreven. Tegelijkertijd zijn over de precieze verhouding tussen 'verzoeken' en een aantal andere concepten in het zaakgericht werken, met name 'zaak' en '(klant)contactmoment', nog een aantal vragen te beantwoorden (zie relaties/kardinaliteiten hieronder). Mogelijk wordt de Verzoeken API naar aanleiding daarvan in de toekomst uitgebreid. 

# Redenen voor het ontwikkelen van een Verzoeken API
Het (her)introduceren van verzoeken in het zaakgericht werken biedt een aantal voordelen, onder andere op de volgende gebieden:
* Compleetheid: we standaardiseren een extra deel van het proces dat leidt tot levering van producten en diensten, namelijk (het generieke deel van) de gegevens die nodig zijn voor het aanvragen hiervan. Hiermee kunnen we (het generieke deel van) StUF-EF vervangen.
* Herkenbaarheid: de klant communiceert met de gemeente niet langer alleen over zaken (een voor hem niet altijd herkenbaar concept), maar over verzoeken, die (als verzoeken correct worden gebruikt) een voor de klant herkenbare (combinatie van) product(en) vertegenwoordigen. Het blijft mogelijk de voortgang van de afhandeling van een zaak terug te koppelen naar de klant.
* Flexibeler (1): gemeenten worden flexibeler in het aanbieden van meerdere gerelateerde producten tegelijk (één verzoek kan leiden tot meerdere zaken). Tegelijkertijd kunnen meerdere verzoeken worden afgehandeld in één zaak.
* Flexibeler (2): bij het indienen van een verzoek hoeft nog niet duidelijk te zijn hoe dat verzoek zal worden behandeld. In de huidige praktijk moet een vraag om levering van een product of dienst immers direct te worden omgezet naar een zaak van een bepaald zaaktype, anders kan immers geen identificerend kenmerk worden teruggestuurd aan de klant. Door verzoeken onderdeel te maken van het zaakgericht werken, kan het verzoeknummer aan de klant gecommuniceerd (‘uw verzoek is ontvangen!’), zonder dat daarmee is vastgelegd op welke manier de behandeling plaatsvindt (en wellicht is in sommige gevallen een zaak/ontvangstbevestiging niet nodig omdat een verzoek direct geautomatiseerd kan worden afgehandeld). Dit betekent dus ook dat een verzoek op een niet-zaakgerichte manier kan worden afgehandeld!
* Zuiverheid: er ontstaat een duidelijk onderscheid tussen 'klantorders' en interne 'productie-/pickorders'.
* Verantwoording: de informatie die bij de intake aanwezig was, is de informatie die hoort bij het verzoek. Daarmee is meteen duidelijk dat informatie die aan een zaak (of een andere behandelwijze) is gekoppeld, na de initiële aanvraag is toegevoegd.

# Intake
Op een verzoek wordt een intake gedaan. Daarbij wordt het verzoek niet inhoudelijk beoordeeld. Wel wordt gekeken of de aangevraagde producten geleverd kunnen worden, en of alle daarvoor benodigde gegevens zijn ingevuld. Na de intake is het verzoek 'in behandeling genomen' danwel 'buiten behandeling gesteld'. De status van een verzoek geeft weer wat er met het verzoek in de intake is gedaan. De status kan in de PIP getoond worden, maar let op: dit kan verwarrend zijn als ook statussen van zaken getoond worden. Het is aan consumers om dit netjes te presenteren.

De status van een verzoek geeft de status van de intake weer (en dus niet van de afhandeling): nieuw, ingetrokken, in intake/behandeling, in behandeling genomen, afgewezen. Nadat een verzoek in behandeling is genomen (of afgewezen) kan het omwille van de verantwoording niet meer worden gewijzigd.

De intake van een verzoek kan zowel automatisch als handmatig plaatsvinden. De API moet beide ondersteunen.

Nadat een verzoek is ingediend kan het niet meer worden gewijzigd. Wel kan de status worden gewijzigd n.a.v. de intake en kunnen er relaties worden gelegd met andere verzoeken, zaken, informatieobjecten, contacten, etc.

# Relatie met zaken
Een verzoek kan resulteren in één of meerdere zaken of andere activiteiten (d.w.z. niet-zaakgericht), danwel direct worden afgehandeld, bijvoorbeeld door levering van een informatiebrochure na aanvraag daarvan. Bovendien kan een verzoek worden gekoppeld aan een reeds lopende zaak. Denk bijvoorbeeld aan een Melding Openbare Ruimte die reeds eerder door een andere klant is gemeld, en waarvoor reeds een zaak loopt. Denk hierbij ook aan een verzoek tot intrekken van een eerder verzoek (dat, indien naar aanleiding van dat eerdere verzoek reeds een zaak was gestart, als tweede (of derde, vierde enz.) verzoek aan die zaak moet worden gekoppeld). Als een zaak aan meerdere verzoeken is gekoppeld, wordt de status van de zaak naar meerdere meerdere indieners teruggekoppeld.

# Interactie met de klant
Zoals hierboven beschreven, kent een verzoek alleen statussen die betrekking hebben op de voortgang van de intake. Terugkoppeling aan de klant over de voortgang van een verzoek heeft twee aspecten:
* Voortgang van de intake met de statussen zoals gedefinieerd in de sectie over Intake.
* Voortgang van de zaken of andere activiteiten die zijn opgestart om het verzoek inhoudelijk te behandelen. Dit gebeurt door middel van de statussen die horen bij de zaken en/of andere activiteiten.

Uitgangspunt is dat een verzoek niet kan  worden gewijzigd. De klant kan een overzicht van ingediende verzoeken opvragen, en moet een verzoek kunnen intrekken. Een verzoek tot intrekken leidt tot een nieuw verzoek dat wordt gerelateerd aan het oorspronkelijke verzoek. Ook kan een klant aanvullingen doen op een verzoek. Dit leidt ook tot een nieuw verzoek dat aan het oorspronkelijke verzoek wordt gekoppeld. Verzoeken voor intrekken en aanvullen worden gerepresenteerd door de relatie naar het betreffende verzoek met een attribuut op de relatie dat het doel vastlegt (intrekken of aanvullen).

Een verzoek kan meerdere producten/diensten omvatten hetgeen een winkelmandje mogelijk maakt op de website van de gemeente. Als gevolg hiervan kan een verzoek tot meerdere zaken leiden. Een verzoek kan ook gekoppeld worden aan een reeds bestaande zaak. Ook in dat geval gaat het verzoek naar status afgehandeld.

Een verzoek heeft geen behandeltermijn en er vindt ook geen terugkoppeling plaats over behandeltermijn van een verzoek. Behandeltermijn komt voort uit zaken of andere afhandelprocessen. Bijv. uit een verzoek kunnen een of meer zaken voortkomen, waarvan de behandeltermijn kan worden teruggekoppeld.

NB: termijnen zouden eigenlijk bij de producten in de PDC moeten staan, omdat producten de interface vormen tussen klant en dienstverlener. Voor nu volgen we echter de huidige praktijk waarin termijnen zijn gekoppeld aan zaaktypen.

# Gegevens: generiek en specifiek
In de verzoekenregistratie wordt alleen generieke metadata opgeslagen. Procesgegevens (domeinspecifiek) en informatieobjecten worden in  andere registraties opgeslagen. Bij een Melding Openbare Ruimte worden bijvoorbeeld specifieke gegevens zoals locatie en meldinggegevens in een meldingen-registratie opgeslagen. Vanuit het verzoek wordt met een URI verwezen naar de aanvullende domeinspecifieke gegevens bij de melding.

# Typen verzoeken
Vooralsnog onderscheiden we geen typen verzoeken. De relatie met producten uit de PDC is waarschijnlijk voldoende om de afhandeling te bepalen. 

# Relaties/cardinaliteiten
* Meerdere contactmomenten kunnen worden gekoppeld aan een verzoek. Een contactmoment kan tot een verzoek leiden, en de klant kan contact opnemen over een ingediend verzoek. Ook kan een contact worden gekoppeld meerdere verzoeken. Er is dus een m:n relatie.
* Iets vergelijkbaars geldt voor 'verzoeken' en 'zaken'.² Wederom geldt echter dat de kardinaliteit van de relatie tussen deze twee enititeiten duidelijk is. Hierboven is immers beschreven dat een verzoek tot meerdere zaken kan leiden, en een zaak kan gekoppeld zijn aan meerdere verzoeken.
* Een verzoek kan meerdere producten omvatten. 1:n van verzoek naar producten
* Een verzoek kan betrekking hebben op meerdere andere verzoeken. Bijv. het verzoek tot intrekken heeft betrekking op een of meer andere verzoeken. Het verzoek met aanvullende gegevens heeft betrekking op een ander verzoek. Er is dus een 1:n relatie van verzoek naar verzoeken.
* Een verzoek kan bijlagen hebben in de vorm van informatieobjecten. Een informatieobject heeft altijd betrekking op slechts 1 verzoek. Er is dus een 1:n relatie van verzoek naar informatieobjecten. 

# Relatie met DSO-verzoeken
Het moet mogelijk zijn om DSO-verzoeken te registreren in de Verzoeken API; er moet dus een mapping zijn van de attributen van een DSO-verzoek naar een ZGW Verzoek. Ook de relaties tussen DSO-Verzoeken moeten kunnen worden geregistreerd; zie ook de sectie over relaties hiervoor. De procesgegevens (ook wel domeinspecifieke gegevens) kunnen niet in de Verzoeken API worden opgeslagen en moeten in een vergunningenregistratie worden opgeslagen.

# Optioneel
Vanwege het ingrijpende karakter van de invoering van verzoeken is implementatie van de Verzoeken API als onderdeel van de API's voor Zaakgericht Werken optioneel. Een verzoek is niet per se nodig om een zaak te starten. Het blijft mogelijk en toegestaan om direct vanuit een formulier een zaak te starten.

# Verantwoording 
Bij de ontwikkeling van deze visie is gebruik gemaakt van de input uit de volgende bronnen:
* Definitie van Verzoeken in [GFO-Zaken](https://www.gemmaonline.nl/index.php/GFO_Zaken_(Zaken_in_zicht))
* Positionering van Verzoeken in het rapport [Zaakgericht werken in het gemeentelijk gegevenslandschap](https://www.gemmaonline.nl/images/gemmaonline/f/f6/20190620_-_Zaakgericht_werken_in_het_Gemeentelijk_Gegevenslandschap_v101.pdf)
* Verzoeken in DSO
* [Verzoeken API](https://github.com/gemeenteshertogenbosch/verzoekregistratiecomponent) zoals ontwikkeld door Den Bosch samen met leverancier Conduction


² Welke activiteiten die onderdeel zijn van de intake voor een zaak, kunnen strakt op het niveau van het verzoek worden afgehandeld? Hoe koppelen we 'verzoek', via '(PDC-)product/dienst' precies aan 'zaaktype'?
