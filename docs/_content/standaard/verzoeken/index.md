# Inleiding
Een verzoek is een aanvraag of opdracht aan de gemeente voor de levering van een product of dienst. Verzoeken vormen dus schakel tussen de klant, producten en diensten van de gemeente zoals in de PDC staan, en het zaakgericht werken voor de afhandeling. Dit biedt een aantal voordelen, onder andere op het gebied van herkenbaarheid voor de klant, die niet meer wordt geconfronteerd met voor hem onherkenbare zaaktypen. Voor gemeenten ontstaat bovendien meer flexibiliteit: een aanvraag van een klant leidt niet langer vanzelfsprekend tot een zaak, en één of meerdere verzoeken kunnen worden gerelateerd aan één of meerdere zaken.

# Intake
Op een verzoek wordt intake gedaan. Daarbij wordt het verzoek niet inhoudelijk beoordeeld, maar wordt wel gekeken of de  aangevraagde producten geleverd kunnen worden en of alle benodigde gegevens zijn ingevuld. Na de intake is het verzoek in behandeling genomen dan wel buiten behandeling gesteld. Een verzoek kan uitmonden in een of meerdere zaken of andere activiteiten (d.w.z. niet zaakgericht), dan wel direct worden afgehandeld, bijv. een product zoals een folder dat direct kan worden geleverd. Ook kan een verzoek worden gekoppeld aan reeds lopende zaak. Denk bijvoorbeeld aan een Melding Openbare Ruimte die reeds eerder is gedaan en waarvoor reeds een zaak loopt. 

Status van verzoeken: is in feite de status van de intake: nieuw, in intake/behandeling, in behandeling genomen, afgewezen. Het verzoek is na in behandelingname of afwijzing niet meer te wijzigen. De daadwerkelijke status(sen) van de gecreëerde zaken of anderszins worden voor terugkoppeling naar de klant gebruikt.

# Interactie
Terugkoppeling naar de klant over voortgang gebeurt in termen van de opgestarte zaken of andere activiteiten. Een verzoek heeft alleen een status m.b.t. voortgang van de intake die overigens ook in de PIP getoond kan worden. De klant kan een overzicht van ingediende verzoeken opvragen en moet een verzoek kunnen intrekken. Een verzoek tot intrekken wordt gerelateerd aan het oorspronkelijke verzoek. Ook kan een klant aanvullingen doen op een verzoek. Dat leidt tot een nieuw verzoek dat aan het oorspronkelijke verzoek wordt gekoppeld.

Een verzoek kan meerdere producten/diensten omvatten hetgeen een winkelmandje mogelijk maakt op de website van de gemeente. Als gevolg hiervan kan een verzoek tot meerdere zaken leiden. 

# Gegevens: generiek en specifiek
Bij een verzoek wordt alleen generieke metadata opgeslagen, procesgegevens (domeinspecifiek) worden in een andere registratie opgeslagen. Bijv. bij een Melding Openbare Ruimte worden specifieke gegevens zoals locatie en meldinggegevens in een meldingen-registratie opgeslagen. Vanuit het verzoek wordt verwezen met een URI naar de melding.

Wat betreft behandeltermijn (uiterste en geplande) volgen we de zaaktypen. Terzijde: deze zouden eigenlijk bij de producten in de PDC moeten staan, maar we volgen voorlopig het huidige model.

# Typen verzoeken
Er zijn verschillende typen verzoeken. Minimaal de volgende typen worden onderscheiden:
* aanvragen product of dienst (uit de PDC van de gemeente)
* doen van een melding (bijv. een melding openbare ruimte)
* aanleveren gegevens bij een reeds bestaand verzoek
* bezwaar maken (in feite geen verzoek om een product), maar wel een verzoek

# Relaties/cardinaliteiten
* Een contactmoment kan over een verzoek of een zaak gaan. Met een contactmoment kan geen verzoek worden ingediend. Meerdere contactmomenten kunnen aan een verzoek worden gekoppeld.
* De relatie tussen zaken en verzoeken is m:n. Een verzoek kan tot meerdere zaken leiden en een zaak kan gekoppeld zijn aan meerdere verzoeken (zie eerder voorbeeld over MOR).
* Een verzoek kan meerdere producten omvatten. 1:n
* Een verzoek kan betrekking hebben op meerdere andere verzoeken. Bijv. het verzoek tot intrekken heeft betrekking op een of meer andere verzoeken. Het verzoek met aanvullende gegevens heeft betrekking op een ander verzoek. 1:n

# Relatie met DSO-verzoeken
Het moet mogelijk zijn om DSO-verzoeken te registreren in de Verzoeken API; er moet dus een mapping zijn van de attributen van een DSO-verzoek naar een Verzoek. Ook de relaties tussen DSO-Verzoeken moeten kunnen worden geregistreerd; zie ook de sectie over relaties hiervoor. De procesgegevens (ook wel domeinspecifieke gegevens) kunnen niet in de Verzoeken API worden opgeslagen en moeten in een vergunningen-registratie worden opgeslagen.

# Optioneel
Een verzoek is niet per se nodig om een zaak te starten. Het blijft mogelijk en toegestaan om direct vanuit een formulier een zaak te starten. Implementeren van de Verzoeken API als onderdeel van de API's voor Zaakgericht Werken is optioneel.
