---
title: "ZGW in Gegevenslandschap v0.7"
date: '18-11-2018'
---

![Repo Status](https://img.shields.io/badge/status-concept-lightgrey.svg?style=plastic)

## 1.1 Inleiding

Zaakgericht werken is een concept dat veel wordt gebruikt in gemeenten. Het kent
ook vele vormen en implementatievarianten. In de GEMMA is hier de laatste jaren
meer richting aan gegeven met het katern Zaakgericht Werken,
[Zaakgericht Werken in de praktijk](https://www.gemmaonline.nl/index.php/Thema_Zaakgericht_werken)
en recentelijk de vertaling van [Zaakgericht Werken in de GEMMA
(informatiearchitectuur)](https://www.gemmaonline.nl/index.php/ZGW_in_GEMMA_2).
Met de beweging “Common Ground” (https://wwww.commonground.pleio.nl) beogen
gemeenten de realisatie van een radicaal nieuw informatie- en
applicatielandschap, een “Gegevenslandschap”. Hierin worden gegevens gescheiden
van businesslogica en eindgebruikersfunctionaliteit en dus uit de traditionele
procesapplicaties gehaald en zijn in plaats daarvan via gestandaardiseerde API’s
beschikbaar bij de bron.

In GEMMA 2 en met name de uitwerking van het ZGW-deel is al voor een deel
rekening gehouden met de beweging naar een “Gegevenslandschap”.
Zaakregistratiecomponent (ZRC) en Zaakafhandelcomponent (ZAC),
Documentregistratiecomponent (DRC) en Documentbeheerocmponent (DBC) (zie
[functies en referentiecomponenten](https://www.gemmaonline.nl/index.php/ZG1_Functies_en_Referentiecomponenten)
voor uitgebreide beschrijvingen van de componenten en een toelichting hierop)
zijn afzonderlijke referentiecomponenten voor registratie respectievelijk
proces/interactie.

Toch vraagt de architectuur van het Gegevenslandschap om een aanpassing van hoe
we tegen de informatiearchitectuur ten dienste van het ZGW aan kijken. Het is
ook niet uit te sluiten dat het concept Zaakgericht Werken zelf enige bijstelling
behoeft als gevolg van de transitie naar een Gegevenslandschap.

Dit stuk onderzoekt deze aanpassingen en schetst enkele oplossingsrichtingen.
Het is urgent om op een aantal van deze punten minstens op korte termijn de richting
bepaald te hebben. Op dit moment worden immers de nieuwe zaakgerichte standaarden
(ZGW API's) ontwikkeld. Omdat de architectuur van het Gegevenslandschap/Common
Ground door de Taskforce Samen Organiseren als uitgangspunt voor de toekomstige
(collectieve) informatievoorziening van gemeenten is benoemd, is het belangrijk
dat deze API’s in een gegevenslandschap het ZGW kunnen ondersteunen.

Uitgangspunt voor de zaakgerichte standaarden (ZGW API's) is GEMMA 2 en daar waar
GEMMA 2 nog niet Gegevenslandschap proof is, gaan we uit van Gegevenslandschap.
Openstaande vraag is backwards compatibility: lukt het om de Zaakgerichte API’s
zo te ontwikkelen dat deze zowel binnen een GEMMA 2 landschap (huidige
systemen/leveranciers) als een Gegevenslandschap gebruikt kan worden? Ook om deze
vraag te kunnen beantwoorden is er eerst meer inzicht nodig in hoe (de
informatiearchitectuur voor) ZGW in een Gegevenslandschap vorm krijgt.

### 1.2 Veranderingen agv het Gegevenslandschap

In GEMMA 2 worden processen zaakgericht uitgevoerd, ondersteund door informatiesystemen
die invulling geven aan de generieke of specifieke Zaakafhandelcomponenten. De
primaire verandering agv het gegevenslandschap zit in deze componenten. We
signaleren drie grote veranderingen:
1. scheiding van gegevens en proceslogica;
2. (eenmalige) opslag en (meervoudige) bevraging van gegevens bij (of door) de bron en
3. (mede daardoor) zeer beperkte informatie-uitwisseling (geen gegevensdistributie of
   ‘rondpompen’, alleen nog notificaties) tussen procesapplicaties. We gaan hierop
   hieronder in.

### 1.2.1. Opknippen Procesapplicaties

In GEMMA 2 en bijgevolg in ZGW in GEMMA 2 zijn de taakspecifieke processystemen
als [“Specifieke Zaakafhandelcomponenten”](https://www.gemmaonline.nl/index.php/ZGW_in_GEMMA_2_compleet#Functies_en_Referentiecomponenten_tbv_ZGW_in_GEMMA)
neergezet.
Processen die zaakgericht worden uitgevoerd, worden afgehandeld met een Zaakafhandelcomponent
(ZAC, generiek of specifiek). De generieke ZAC slaat haar gegevens op in de
Zaakregistratiecomponent (ZRC). Daarentegen slaat de specifieke ZAC alle gegevens
zelf op: over de zaak en het proces, het verloop daarvan en veelal ook de
registratie van de objecten waarop dat proces betrekking heeft. Vanuit deze component
wordt een zaak geregistreerd (gekopieerd) in de ZRC en wordt deze zaak bij wijzigingen
(ook) daarin bijgewerkt. Volgens het Gegevenslandschap moeten deze gegevens
gescheiden worden van de procesapplicatie en in een of meerdere registraties
worden ondergebracht en via gestandaardiseerde API’s ontsloten. Voor de
Generieke Zaakafhandelcomponent is hierin al voorzien: deze gebruikt enkel
generieke zaakgegevens. Deze gegevensset beperkt zich dus tot de gegevensset
zoals wordt bijgehouden in de Zaakregistratiecomponent (ZRC). Voor een
specifieke ZAC waarin veel domein- of processpecifieke gegevens worden
bijgehouden heeft dit (vergaande) consequenties.

### 1.2.2. Eenmalige opslag vanuit de bron

Common Ground gaat uit van het beschikbaar stellen en bevragen van gegevens bij de bron. Kopiëren en distribueren van gegevens (gegevensmagazijnen, gegevensdistributie,..) bestaan in een gegevenslandschap niet meer. ‘Beschikbaar stellen bij de bron’ moet evenwel niet altijd letterlijk genomen worden. Anders zouden er precies evenveel registraties als procesapplicaties ontstaan (elke procesapplicatie als zelfstandige bron voor de gegevens ontstaan in die applicatie), wat een nogal gefragmenteerde gemeentelijke informatiehuishouding zou opleveren. Hierbij zouden dan telkens al deze bronregistraties bevraagd moeten worden om een overzicht te krijgen van de gegevens behorende bij alle lopende zaken.
“Soortgelijke gegevens opslaan bij soortgelijke gegevens” is hiervoor een goed uitgangspunt. Zo ontstaan diverse “(kern)registraties”: coherente en integere registraties met meervoudig gebruikte soortgelijke gegevens die vanuit verschillende procesapplicaties worden bijgehouden. Bijvoorbeeld één gemeentelijke kernregistratie medewerkers en niet een (deel-)registratie per afdeling/proces.
Voor het Zaakgericht werken heeft dit als gevolg dat veel objecten die nu in een Zakenmagazijn of procesapplicatie worden bijgehouden (behandelend medewerker, betreffend object, aanvrager (klant),..) vervangen moeten worden door een verwijzing naar de desbetreffende kernregistratie.

### 1.2.3. Vermindering van informatiestromen

In de huidige gemeentelijke informatievoorziening vindt de interactie tussen processen plaats door middel van gegevensuitwisselingsberichten tussen desbetreffende applicaties (cq. referentiecomponenten). De ontvangen informatie wordt veelal ook weer opgeslagen door en in de ontvangende procesapplicatie. Een voorbeeld zijn mutaties van het verblijfsadres van een burger (a.g.v. een verhuizing) die door de GBA- (cq. BRP-)beheerapplicatie verstrekt worden aan bijvoorbeeld een vergunningenapplicatie, belastingenapplicatie en sociaal domeinapplicatie.
In een gegevenslandschap is er van een dergelijke gegevensdistributie geen sprake meer. Hooguit wordt een proces genotificeerd over een gebeurtenis (zoals een verhuizing). De daarbij betrokken gegevens kunnen vervolgens, indien gewenst, door de ontvangende applicatie opgevraagd worden bij de desbetreffende registratie (en niet opnieuw vastgelegd worden) om daarmee de voor het proces relevante afhandeling te kunnen doen. Het versturen van berichten met inhoud tussen verschillende referentiecomponenten wordt dus zoveel mogelijk beperkt en vervangen door het sturen van notificaties en het opvragen van de bijbehorende gegevens uit een registratie.
Specifieke aandacht verdienen aanvragen, meldingen e.d. die ‘op een website’ (of vanuit een App) ingediend worden. Het indienen wordt ondersteund door de referentiecomponent voor het aanvragen van producten en diensten (“e-Formulierencomponent” in GEMMA 2). In GEMMA 2 wordt een dergelijke aanvraag gerouteerd (in een bericht) naar de van toepassing zijnde generieke of specifieke ZAC. In een Gegevenslandschap kan hiervan geen sprake meer zijn. Voor de hand liggend is dat de e-Formulierencomponent die aanvraag opslaat, bijvoorbeeld in een : (kern)registratie Verzoeken”, een notificatie stuurt naar de desbetreffende ZAC die naar aanleiding daarvan de behandeling start (en daartoe onder meer de zojuist genoemde Registratiecomponent bevraagt).

## 1.3 Schets van de oplossing

### 1.3.1. Verandering

Op basis van de hierboven geschetste veranderingen agv het gegevenlandschap en Common Ground zijn we toe aan een nieuwe fase in de zaakgerichte informatievoorziening.
Dit past goed op de ontwikkelrichting zie ZGW al doorlopen heeft: van een zakenmagazijn naast backoffice-silo’s die ongeschikt waren voor klantgerichte (online-) dienstverlening, via alles-in-een zaaksystemen, naar zaakgericht registreren en generieke en specifieke zaakafhandelcomponenten naar een volgende stap in het vormgeven van de informatie-architectuur onder het zaakgericht werken.
Hieronder gaan we uit van een, op basis van het Gegevenslandschap, radicaal anders opgezet applicatielandschap. Daarin zijn veel uitdagingen die aanleiding hebben gegeven tot het zaakgericht werken veel integraler in de applicaties en registraties verwerkt. Voorbeelden van dergelijke uitdagingen zijn het verbeteren van de dienstverlening, een beter inzicht in proces- en voortgang uit back-office applicaties en digitaal uniform archiveren etc. Zaakinformatie zit als gevolg hiervan niet meer op één centrale plaats, maar gedistribueerd over meerdere registraties.
Grof geschetst bewegen we van een situatie zoals in figuur 1 naar een situatie zoals in figuur 2.

### 1.3.2. Huidige Situatie

In figuur 1 staat een schets van de huidige situatie zoals min of meer beschreven door GEMMA 2.

![zgw in de huidige situatie v2.png](./_assets/zgw_in_de_huidige_situatie_v2.png?raw=true)
*Figuur 1 - ZGW in de huidige situatie (~GEMMA 2)*

* Een zaak is geregistreerd in een ZRC. Aan een zaak gerelateerde objecten (RGBZ) worden ook geregistreerd in de ZRC: Betrokkenen, Besluiten, Klantcontacten, Zaakobjecten en eventuele zaaktypespecifieke Objecten met zaaktypespecifieke eigenschappen.
* Vanuit een zaak liggen er verwijzingen naar Zaaktype (ZTC), Document vcq. informatieobject (DRC) en eventuele objecten (in theorie uit Basisregistraties, maar vaak Gegevensmagazijn)
* Voor Betrokkene is in theorie ook sprake van een verwijzing (naar BRP en HR, kernregistratie medewerkers, kernregistratie bedrijven, kernregistratie klanten,..), maar in de praktijk wordt dit meestal in de ZRC zelf opgeslagen.
* De Zaakafhandelcomponent bevat nog veel gegevens:
    * procesdefinities (hoe moet een proces lopen, welke keuzes zijn er mogelijk);
    * procesgegevens (waar in het proces zitten we, welke keuzes zijn in het proces gemaakt, wie is de behandelaar, welke gegevens heeft hij gebruikt voor welke processtap, ..)
    * domein/objectgegevens: gegevens over objecten in het domein waartoe het proces behoort. Bijvoorbeeld voor een Subsidiesysteem de gegevens over een aangevraagde subsidie, doelen die men met subsidies wil stimuleren en de voorwaarden en uitnutting van diverse subsidiepotjes.
* “Aanvraag” mist in dit plaatje. Dat klopt ook. Deze maakt onderdeel uit van de domein/objectgegevens. In de huidige praktijk wordt een aanvraag ook nog vaak (onterecht) met een zaak vereenzelvigd. Waarbij het in de vorm van een Informatieobject als PDFje wordt opgeslagen bij een zaak. Naast dit “verlies” van gestructureerde gegevens uit het formulier, mis je hierdoor ook de flexibiliteit om meerdere meldingen in één zaak af te handelen, of de behandeling van één melding uit te splitsen in twee zaken.
* Er bestaat in de ZRC geen rechtstreekse relatie tussen het merendeel van de domein/objectgegevens en een zaak (dit is beperkt tot zaakobjecten en zaaktypespecifieke gegevens). Deze relatie ligt immers in de ZAC. Idem voor gedetailleerde procesgegevens en een zaak. M.a.w. in het geval van erg complexe processen, kent de zaak in de ZRC enkel dit proces op hoofdlijnen (de zaakstatussen).
* Wel liggen deze relaties in de specifieke zaakafhandelcomponent: daarin is (impliciet of expliciet) een proces geconfigureerd (=procesdefinitie of “procestype”), bijvoorbeeld “Afhandelen evenementensubsidieaanvraag”). Het verloop van een specifieke instantie van dat proces volgt dit procestype. En er liggen relaties tussen dit proces en de domein/objectregistratie(s) die bij dit proces horen.
* De specifieke ZAC heeft wel uiteraard weet van welk zaaktype en welke zaak er bij een bepaald procestype en bij een bepaalde procesinstantie horen, maar vanuit een zaak is dit dus niet direct opvraagbaar.

### 1.3.3. Situatie in een Gegevenslandschap

In het Gegevenslandschap komt bovenstaand plaatje er, door het scheiden van proces en data, eenmalige opslag en bevraging ‘bij de bron’ en het verminderen van informatiestromen anders uit te zien (zie figuur 2):

![zgw-in-gegevenslandschap.png](./_assets/zgw-in-gegevenslandschap.png?raw=true)
*Figuur 2 - ZGW in een Gegevenslandschap*

* De domein/objectgegevens gegevens zijn uit de Zaakafhandelcomponent verdwenen. Procesdefinities en procesgegevens blijven daar echter achter. Dit is ook precies het punt waar procesapplicaties zich op kunnen onderscheiden: goede procesondersteuning.
* Uitgangspunt in het gegevenslandschap is: alle gegevens worden op één plaats opgeslagen. En alle soortgelijke gegevens worden bij elkaar opgeslagen. Er komt dus een registratie met besluiten, een registratie met verzoeken (aanvragen en meldingen), een registratie met klanten, een registratie medewerkers. Etc.
* Objecttypen die ook betekenis hebben of voorkomen in andere domeinen dan enkel het Zaakgericht werken, worden zo als eigenstandige registratie onderkend.
* De “Zaak” is een belangrijk verbindend element tussen de objecten in de registraties. Getekend: een zaak aggregeert al deze andere objecten. Zaak fungeert zo als “sleutel” in een grote “verwijsindex” met verwijzingen naar objecten in andere registraties. Welke op hun beurt weer kunnen relateren naar objecten in andere registraties, bv. de BRP of het HR.
* Dit komt sterk overeen met het concept Linked-data. De Zakenregistratiecomponent is dus niet meer één grote database met daarin alle gegevens over een zaak. Maar meer een kernregistratie van gegevens over zaken zaken met veel links (URL’s) naar objecten in andere registraties (en vice-versa).

## 1.4 Vraagstukken

Bovenstaande plaat schetst het concept ZGW in een Gegevenslandschap al heel behoorlijk. Toch zijn er nog enkele openstaande vragen te beantwoorden. Voor een deel is dit al af te leiden uit de stippellijnen in bovenstaande plaat:

#### 1.4.1. Hoe verhoudt melding/verzoek zich tot een zaak?

In bovenstaande figuur is de relatie tussen Melding/Aanvraag (Verzoek) en Zaak als een stippellijn getekend (Merk op dat er ook zaakgericht gewerkt kan worden in processen die niet naar aanleiding van een verzoek van de klant worden opgestart, marabv. n.a.v. een binnengekomen gebeurtenis.In dat geval is er ook geen Verzoek.. Dit omdat Verzoek niet in het RGBZ voorkomt (zat wel in GFO Zaken) en we dus niet weten hoe Verzoek en Zaak zich tot elkaar verhouden. Essentie van de relatie lijkt te zijn dat een verzoek of melding een op zichzelf staand ‘iets’ is en behandeld wordt als zaak. Één verzoek kan leiden tot meerdere zaken. Meerdere Verzoeken kunnen ook leiden tot één Zaak. Bv. meerdere meldingen die als één zaak worden afgehandeld. Verzoek heeft juridisch ook een eigen betekenis, bijvoorbeeld in het kader van archivering en het bepalen van de afhandeltermijn (ontvangstdatum Verzoek).
Een verzoek kan bv. een subsidieaanvraag of een melding zijn.

![verzoeken v2.png](./_assets/verzoeken_v2.png?raw=true)
*Figuur 3 -Verzoeken*

We kiezen ervoor om Verzoeken als aparte registratie te onderkennen en op te nemen in het RGBZ (als apart Informatiemodel Verzoeken met relatie met Zaak). Zo wordt het eerder aangehaalde nadeel dat gestructureerde gegevens die in een formulier zijn ingevuld “verloren” dreigen te gaan voorkomen.
Een e-formulierencomponent (of ander systeem waarin een burger of bedrijf een aanvraag kan doen) registreert het verzoek in de Verzoekenregistratie. De gegevens van de aanvrager (in figuur 3 een burger) in de klantenregistratie (als deze niet al bestond) en de documenten bij de aanvraag in de documentenregistratie. Meldingspecifieke gegevens in de domeinspecifieke registratie voor meldingen. Denk aan aard van de melding, omschrijving van de klacht etc.
De relatie tussen verzoek en alle informatie die bij de aanvraag aanwezig was, of eventueel later is aangevuld, wordt vastgelegd en mag niet meer gewijzigd worden. Zo is te allen tijde duidelijk welke gegevens er bij de aanvraag zaten.

![van verzoek naar zaak2.png](./_assets/van_verzoek_naar_zaak2.png?raw=true)
*Figuur 4- Van Verzoek naar Zaak*

NU het verzoek is geregistreerd, moet het in behandeling worden genomen. Dit gebeurt door een medewerker die in de regel met een taakapplicatie zal werken. Deze wordt ofwel genotificeerd over een nieuw binnengekomen verzoek, of deze applicatie controleert periodiek, bv. ieder uur, of er nog nieuwe verzoeken van een bepaald type binnen zijn gekomen.
Als het verzoek in behandeling wordt genomen, wordt vanuit de desbetreffende taakapplicatie via de Zaakregistratiecomponent een Zaak aangemaakt. Het Verzoek wordt gerelateerd aan deze zaak (relatie nog in informatiemodel te formaliseren). Objecten die aan Verzoek waren gerelateerd (groen gekleurd in
figuur 4: Klant, Bijlagen, Meldingspecifieke gegevens), worden ook rechtstreeks aan Zaak gerelateerd.
Tijdens de behandeling in de Zaakafhandelcomponent ontstaat bijkomende informatie in de Documentenregistratie en de Meldingenregistratie.
De relatie tussen Verzoek en Zaak wordt nog verder uitgewerkt. Zie
[#390](https://github.com/VNG-Realisatie/gemma-zaken/issues/390)

### 1.4.2. Waar slaan we procesinformatie op?

Een andere vraag is waar we in een gegevenslandschap “Procesinformatie” willen opslaan.
Procesdefinitiegegevens beschrijven het te volgen proces in de afhandelapplicatie. Uit welke stappen bestaat dat proces, welke keuzes kunnen hierin gemaakt worden, welke beslisregels worden gehanteerd, etc. Vergelijkbaar met een Zaaktype voor zaken. Procesgegevens beschrijven hoe dit proces voor één bepaald geval is doorlopen: welke behandelaar heeft welke stap uitgevoerd wanneer. Welke keuzes zijn gemaakt obv de bekende gegevens etc.
In figuur 2 is dit – samen met Procesdefinitiegegevens - gepositioneerd in de Zaakafhandelcomponent (net als nu in de diverse Taaksystemen). Dit lijkt (mogelijk) in strijd met het uitgangspunt van het Gegevenslandschap dat functionaliteit en gegevens van elkaar gescheiden moeten zijn. Procesgegevens zijn immers ook gegevens. Het is echter moeilijk om proces- en procesdefinitiegegevens uit de afhandelende systemen te halen.  In veel gevallen is de procesdefinitie zelfs impliciet (hard gecodeerde flow tussen schermen); dat valt dan niet eens los te knippen.
Toewerken naar een situatie waarbij procesgegevens onafhankelijk van de afhandelende applicatie in een leveranciersonafhankelijke “procesregistratie” komen te staan lijkt ons niet haalbaar. Het meest generieke formaat wat we over alle processen konden afspreken hebben we al, nl. Zaken en Zaaktypen. Dat is voor het sturen en registreren van de afhandeling niet toereikend.  Een ander alternatief is van alle taakapplicaties te eisen dat ze op basis van in BPMN gedefinieerde processen gaan werken en één centrale processenrepository gaan gebruiken. Ook dat lijkt ons te ingrijpend in de huidige leveranciersmarkt. Ook is het de vraag of er dan voldoende interessante markt voor afhandelapplicaties overblijft.
Er is één maar. Het kunnen ontsluiten van procesinformatie is nodig om het handelen als overheid te verantwoorden: het moet dus gearchiveerd worden. Wie heeft op welke datum welke stap gezet? Welke procesflow (en keuzes) is er doorlopen? Welke informatie was wanneer beschikbaar? Hoe luidde de (deel)berekening die heeft geleid tot een bepaald resultaat? Dit is informatie die niet in één van de andere registraties past en voor het grootste deel niet in de ZRC wordt vastgelegd (die kent meestal maar één behandelaar en vooral enkel het proces op hoofdlijnen: de Statussen).
Conclusie: proces- en procesdefinitiegegevens blijven in de afhandelapplicaties. Idealiter maken deze een scheiding tussen schermen (interactie) en afhandeling (proces), en stellen ze hun procesgegevens in een open formaat (via een API) beschikbaar. Alternatief is een “log” van hun procesverloop als document (PDF) als document aan de zaak toe te voegen.

### 1.4.3. Relatie proces – zaak

In de figuur staat ook een stippellijn getekend tussen Zaak en Procesgegevens. Proces staat niet gedefinieerd in het informatiemodel RGBZ, en dus ligt de relatie zaak – proces ook niet eenduidig vast. In GFO zaken was dit min of meer wel het geval met “stap”. Hieruit, en vooral uit de prominente rol van ‘status’ in het RGBZ, blijkt al dat het moeilijk is om alle soorten processen op een eenduidige manier te registreren. Uiteindelijk kom je dan bij een informatiemodel met de rijkheid van BPMN uit (en voor de meer adaptieve processen iets dat lijkt op CMMN). Wat uiteraard niet de bedoeling is. Maar indachtig de vorige vraag: “waar registreren we procesinformatie”, is het noodzakelijk dat de relatie zaak-proces goed is gedefinieerd, zodat we als we nadere procesinformatie willen weten van een zaak, deze bij een zaaknummer kunnen opvragen (indien beschikbaar).
[Er is een issue om deze vraag te beantwoorden](https://github.com/VNG-Realisatie/gemma-zaken/issues/392).

### 1.4.4. Hoe objecten relateren aan een zaak?
Objecten worden in het RGBZ aan een zaak gerelateerd dmv. “Zaakobject”: “een Object waarop de zaak betrekking heeft”. In theorie kun je hier veel kanten mee op. In de praktijk is het gebruik hiervan beperkt tot voornamelijk basisregistratieobjecten. In een gegevenslandschap moeten veel meer soorten objecten aan een zaak gerelateerd kunnen worden. De zaak vormt immers de sleutel om deze bij elkaar te kunnen houden. Denk bijvoorbeeld aan verleende subsidies, uitgegeven marktplaatsen, grafrechten, etc. Vroeger werden deze objectenregistraties bijgehouden in het processysteem en lag daar impliciet de relatie tussen de zaak en deze objecten. Het Gegevenslandschap vraagt om een andere, meer integrale benadering. Het is daarom de vraag of de relatie zaak – object zoals gedefinieerd in het RGBZ (zaak heeft betrekking op object) hiervoor voldoende is genoeg is.
Zeker omdat de domeingegevens voor de complexere processen uit meerdere objecten zullen bestaan. Relateer je dan al die objecten aan een zaak?
[Discussie en verdere verdieping op dit issue](https://github.com/VNG-Realisatie/gemma-zaken/issues/394).

### 1.4.5. Welke bakjes onderkennen we?

In de uitwerking hierboven hebben gezien dat er aparte registraties “bakjes” ontstaan voor verschillende aan zaak gerelateerde objecten die nu nog in de ZRC worden bijgehouden. Voor deze registraties moeten er aparte, aan zaak (RGBZ) gekoppelde informatiemodellen komen. De objecten worden via aparte API’s ontsloten.
Rondom het zaakgericht werken onderkennen we de volgende registraties:
* Zaaktypenregistratie (nu ZTC)(Zaaktype, Statustypen, Resultaattypen,..)
* Documentenregistratie (nu DRC) (documenten cq. informatieobjecten)
* Klanten- en contactenregistratie (voor initiators, belanghebbenden, gemachtigden e.d.). Deze registratie verwijst voor persoonsgegevens naar de BRP, voor bedrijven en instellingen naar het HR en bevat enkel de bijkomende informatie, bijvoorbeeld contactvoorkeuren en de klantcontacten
* Organisatie en medewerkersregistratie (o.a. voor behandelaars, adviseurs, afdelingen, rollen en bevoegdheden)
* Verzoekenregistratie (verzoeken met verwijzingen naar alle bij een verzoek horende gegevens)
* Besluitenregistratie (besluiten)
* Domein/objectregistraties (domein/objectgegevens; meerdere registraties: één per domein/proces, bijvoorbeeld voor meldingen of subsidies)
* Basisregistraties (personen, bedrijven, panden, terreinen, percelen e.d.)
* Evt. andere kernregistraties (Zaakobjecten die nog niet genoemd zijn, maar wel behoren tot kerngegevens (meervoudig gebruikt))
* En natuurlijk, last-but-not least de Zakenregistratie (nu ZRC)
Let wel dat we hier nadrukkelijk spreken over “registraties” en het in GEMMA 2 gebruikelijke achtervoegsel “-component” hebben weggelaten. Waar deze registraties worden geïmplementeerd maakt niet zoveel uit. Er kan prima één softwarepakket zijn dat meerdere registraties implementeert.

### 1.4.6. Wat willen we doen met Zaken?

Zaakgericht werken kent al een lange geschiedenis. Het stamt uit de tijd dat dienstverleningsambities hoger werden en backoffice-applicaties dit niet of nauwelijks aankonden. Daarna was er de gedachte dat een “alles-in-1 zaaksysteem” voor veel processen voldoende zou zijn. Inmiddels draait de slinger een beetje terug en zien we taakspecifieke systemen moderner en opener worden. In een Gegevenslandschap is dit helemaal het geval.
In de loop der jaren zijn er diverse doelen voor zaakgericht werken ontstaan: dienstverlening verbeteren, als basis voor het archiveren, het bieden van managementinformatie,.. waarvan het de vraag is of je ze in een modern applicatielandschap nog met zaakgericht werken wilt oplossen. In het geval van een gemeente die met één dominant generiek zaaksysteem werkt ligt de oplossingsrichting voor de hand. In een Gegevenslandschap veel minder. Bovendien zien we op vele vlakken een terugtrekkende beweging op het “gemeentebrede” dienstverleningsconcept, meer richting domeinspecifieke apps en portalen. Een meer domeingerichte dienstverlening en informatievoorziening (ipv generiek obv zaken) ligt daar dan meer voor de hand.
Enkele voorbeelden:
1.	Een gemeente wil alle Meldingen Openbare Ruimte op een kaart tonen. Vraag je hiertoe alle melding-zaken op met de ZGW API's “toon zaken op de kaart”? Wetende dat de AVG dit voor het overgrote deel aan zaken/zaaktypen niet toestaat? Of kies je voor een meldingen-specifiek koppelvlak, dat mogelijk functioneel rijker is: type melding, prioriteit van de melding, tekstuele toelichting…allemaal wellicht nuttig om op een dergelijke kaart te kunnen weergeven. Maar niet of slechts met moeite (zaaktypespecifieke eigenschappen) met een generiek zaken-koppelvlak te realiseren.
2.	Hoe wil je een proceseigenaar/afdelingshoofd van management-informatie voorzien? Op basis van zaken kun je erg generieke metrieken weergeven. Aantal zaken per afdeling, aantal zaken per status, zaken die voor of achter lopen op plandatum etc. Toch is het vergelijken van een subsidiezaak met een vergunnningenzaak appels met peren vergelijken. En zit een manager vergunningen vermoedelijk op heel andere metrieken te wachten: aantal vergunningen per wijk, aantal afhandeluren per bouwvolume-eenheid etc.
3.	Hoe wil je status-informatie weergeven aan de klant? Heel generiek obv enkel voorgedefinieerde “zaakstatussen”, of wil je dit functioneel rijker doen in een domeinspecifiek portal, bijvoorbeeld specifiek voor subsidies?
Het is belangrijk om hier als gemeente even goed bij stil te staan. Zaakgericht werken is geen panacee voor alle problemen en behoeften. Maar zaakgericht werken is een manier van procesgericht werken die zo ver is uitgewerkt dat anderen dan de uitvoerenden van een proces dat proces ook kunnen begrijpen, op het niveau dat voor een ander waarschijnlijk volstaat: de hoofdlijnen. Dit ‘esperanto’ blijft een onderscheidend kenmerk van zaakgericht werken en zaakgerichte API’s boven domeinspecifieke API’s
Je krijgt hiermee twee niveaus: domeinspecifiek en domeinoverstijgend. Daar waar uniformiteit over de domeinen belangrijk is, gebruiken we Zaken (en zaakgerichte standaarden). Is er echter voldoende zwaarwegende behoefte aan domeinspecifieke functionaliteit, dan kiezen we voor een domeinspecifieke oplossing en dito standaarden. Dit is een afweging die van geval tot geval gemaakt moet worden.

### 1.4.7. Notificeren over zaken

In een gegevenslandschap willen we geen zaken (of andere informatie) meer
“rondsturen”. Vraag is wel hoe een behandelaar met een taakapplicatie te weten
komt dat er een melding voor hem beschikbaar is die behandeld moet worden. Er
zijn nog andere scenario’s te bedenken, waarin het nuttig is dat een partij
actief wordt genotificeerd over een zaak(status). Bijvoorbeeld bij meerdere
behandelaars die met meerdere systemen werken (of moeten we dat niet willen?),
of wanneer er een nieuw document aan een zaak is toegevoegd door een
KCC-medewerker. Het is nuttig om enkele van deze scenario’s uit te werken
binnen de context van een gegevenslandschap en hiervoor een generieke oplossing
voor te stellen. Een verdere uitwerking van
[notificeren over zaken](https://www.gemmaonline.nl/index.php/ZGW_in_GEMMA_2_compleet#Notificeren_over_Zaken)
binnen een gegevenslandschap. Nog verder uit te werken in
[issue #397](https://github.com/VNG-Realisatie/gemma-zaken/issues/397)
