# Inleiding
Een verzoek is een aanvraag of opdracht aan de gemeente (of andere overheid) voor de levering van een product of dienst. Verzoeken vormen dus de schakel tussen de klant, producten en diensten van de gemeente zoals in de PDC staan, en het zaakgericht werken voor de afhandeling. Dit biedt een aantal voordelen, onder andere op het gebied van herkenbaarheid voor de klant, die niet meer wordt geconfronteerd met voor hem onherkenbare concepten uit de gemeentelijke bedrijfsvoering. Voor gemeenten ontstaat bovendien meer flexibiliteit: een aanvraag van een klant leidt niet langer vanzelfsprekend tot een zaak, en één of meerdere verzoeken kunnen worden gerelateerd aan één of meerdere zaken.

Verzoeken zijn voor het eerst geintroduceerd in GFO-Zaken, maar is daarna weer verdwenen in het opvolgende informatiemodel RGBZ. In de visie van VNG Realisatie is dat echter een omissie, en daarom is er behoefte aan een concept dat vooraf gaat aan de daadwerkelijke behandeling in een zaak (of andere activiteit).

# Intake
Op een verzoek wordt een intake gedaan. Daarbij wordt het verzoek niet inhoudelijk beoordeeld, maar wordt wel gekeken of de  aangevraagde producten geleverd kunnen worden en of alle daarvoor benodigde gegevens zijn ingevuld. Na de intake is het verzoek in behandeling genomen dan wel buiten behandeling gesteld. Een verzoek kan uitmonden in een of meerdere zaken of andere activiteiten (d.w.z. niet zaakgericht), dan wel direct worden afgehandeld, bijv. een product zoals een folder dat direct kan worden geleverd. Ook kan een verzoek worden gekoppeld aan een reeds lopende zaak. Denk bijvoorbeeld aan een Melding Openbare Ruimte die reeds eerder is gedaan en waarvoor reeds een zaak loopt.

Status van verzoeken: is in feite de status van de intake: nieuw, ingetrokken, in intake/behandeling, in behandeling genomen, afgewezen. Nadat een verzoek in behandeling is genomen (of afgewezen) kan het niet meer worden gewijzigd.

# Interactie met de klant
Terugkoppeling naar de klant over de voortgang van een verzoek gebeurt d.m.v. van de statussen van de opgestarte zaken en/of andere activiteiten. Een verzoek heeft alleen een status m.b.t. voortgang van de intake (zie hierboven) die overigens ook in de PIP getoond kan worden (let op: dit kan verwarrend zijn als ook statussen van zaken getoond worden; dit is aan de consumers om op te lossen). De klant kan een overzicht van ingediende verzoeken opvragen en moet een verzoek kunnen intrekken. Een verzoek tot intrekken wordt gerelateerd aan het oorspronkelijke verzoek. Ook kan een klant aanvullingen doen op een verzoek. Dat leidt tot een nieuw verzoek dat aan het oorspronkelijke verzoek wordt gekoppeld.

Een verzoek kan meerdere producten/diensten omvatten hetgeen een winkelmandje mogelijk maakt op de website van de gemeente. Als gevolg hiervan kan een verzoek tot meerdere zaken leiden. Een verzoek kan ook gekoppeld worden aan een reeds bestaande zaak. Ook in dat geval gaat het verzoek naar status afgehandeld.

# Gegevens: generiek en specifiek
Bij een verzoek wordt alleen generieke metadata opgeslagen. Procesgegevens (domeinspecifiek) worden in een andere registratie opgeslagen. Bijv. bij een Melding Openbare Ruimte worden specifieke gegevens zoals locatie en meldinggegevens in een meldingen-registratie opgeslagen. Vanuit het verzoek wordt verwezen met een URI naar de melding.

Wat betreft behandeltermijn (uiterste en geplande) volgen we de zaaktypen. Een verzoek heeft geen termijnen. Terzijde: deze zouden eigenlijk bij de producten in de PDC moeten staan, omdat producten de interface vormen tussen klant en dienstverlener. Voor nu volgen we het huidige model.

# Typen verzoeken
Er zijn verschillende typen verzoeken. Minimaal de volgende typen worden onderscheiden:
* aanvragen product of dienst (uit de PDC van de gemeente)
* doen van een melding (bijv. een melding openbare ruimte)
* aanleveren gegevens bij een reeds bestaand verzoek
* verzoek tot het in behandeling nemen van een bezwaar 

# Relaties/cardinaliteiten
* Een contactmoment kan over een verzoek of een zaak gaan. Met een contactmoment kan geen verzoek worden ingediend maar een contactmoment kan wel tot een verzoek leiden. Meerdere contactmomenten kunnen aan een verzoek worden gekoppeld. Er is dus een 1:n relatie van verzoek naar contacten.
* De relatie tussen zaken en verzoeken is m:n. Een verzoek kan tot meerdere zaken leiden en een zaak kan gekoppeld zijn aan meerdere verzoeken (zie eerder voorbeeld over MOR).
* Een verzoek kan meerdere producten omvatten. 1:n van verzoek naar producten
* Een verzoek kan betrekking hebben op meerdere andere verzoeken. Bijv. het verzoek tot intrekken heeft betrekking op een of meer andere verzoeken. Het verzoek met aanvullende gegevens heeft betrekking op een ander verzoek. Er is dus een 1:n relatie van verzoek naar verzoeken.
* Een verzoek kan bijlagen hebben in de vorm van informatieobjecten. Een informatieobject heeft altijd maar betrekking op 1 verzoek. Er is dus een 1:n relatie van verzoek naar informatieobjecten. 

# Relatie met DSO-verzoeken
Het moet mogelijk zijn om DSO-verzoeken te registreren in de Verzoeken API; er moet dus een mapping zijn van de attributen van een DSO-verzoek naar een ZGW Verzoek. Ook de relaties tussen DSO-Verzoeken moeten kunnen worden geregistreerd; zie ook de sectie over relaties hiervoor. De procesgegevens (ook wel domeinspecifieke gegevens) kunnen niet in de Verzoeken API worden opgeslagen en moeten in een vergunningen-registratie worden opgeslagen.

# Optioneel
Vanwege het ingrijpende karakter van de invoering van verzoeken is implementatie van de Verzoeken API als onderdeel van de API's voor Zaakgericht Werken optioneel. Een verzoek is niet per se nodig om een zaak te starten. Het blijft mogelijk en toegestaan om direct vanuit een formulier een zaak te starten.

# Verantwoording 
Bij de ontwikkeling van deze visie is gebruik gemaakt van de input uit de volgende bronnen:
* Definitie van Verzoeken in [GFO-Zaken](https://www.gemmaonline.nl/index.php/GFO_Zaken_(Zaken_in_zicht))
* Positionering van Verzoeken in het rapport [Zaakgericht werken in het gemeentelijk gegevenslandschap](https://www.gemmaonline.nl/images/gemmaonline/f/f6/20190620_-_Zaakgericht_werken_in_het_Gemeentelijk_Gegevenslandschap_v101.pdf)
* Verzoeken in DSO
* Verzoeken API zoals ontwikkeld door Den Bosch samen met leverancier Conduction
