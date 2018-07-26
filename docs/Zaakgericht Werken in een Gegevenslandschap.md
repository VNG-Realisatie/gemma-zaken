# Zaakgericht Werken in een Gegevenslandschap

![Repo Status](https://img.shields.io/badge/status-concept-lightgrey.svg?style=plastic)

## 1.1 Inleiding

Zaakgericht werken is een concept dat veel wordt gebruikt in gemeenten. Het kent ook vele vormen en implementatievarianten. In de GEMMA is hier de laatste jaren meer richting aan gegeven met het katern Zaakgericht Werken, Zaakgericht Werken in de praktijk en recentelijk de vertaling van Zaakgericht Werken in de GEMMA (informatiearchitectuur).

Zie:
* https://www.gemmaonline.nl/index.php/GEMMA_2_Katern_Zaakgericht_Werken 
* https://www.gemmaonline.nl/index.php/Thema_Zaakgericht_werken#Zaakgericht_werken_in_de_praktijk 
* https://www.gemmaonline.nl/index.php/ZGW_in_GEMMA_2

Met de beweging van Common Ground (commonground.pleio.nl) beogen gemeenten een radicaal nieuw informatie- en applicatielandschap, een “gegevenslandschap”. Hierin worden gegevens gescheiden van eindgebruikersfunctionaliteit en dus uit de traditionele procesapplicaties gehaald en zijn in plaats daarvan via gestandaardiseerde API’s beschikbaar bij de bron.

In GEMMA 2 en met name de uitwerking van het ZGW-deel is hier al voor een deel rekening mee gehouden. ZRC en ZAC, DRC en DBC zijn afzonderlijke referentiecomponenten voor registratie resp. proces/interactie. Toch vraagt de architectuur van het Gegevenslandschap om een aanpassing van hoe we tegen de informatiearchitectuur ten dienste van het ZGW aan kijken. Het is ook niet uit te sluiten dat het concept Zaakgericht Werken zelf enige bijstelling behoeft als gevolg van de transitie naar een gegevenslandschap.

Dit stuk doet een voorzet in deze discussie.
Het is urgent om op dit punt minstens op korte termijn de richting bepaald te hebben. Op dit moment worden de ZDS 2.0 API’s ontwikkeld. Het is belangrijk dat deze in een gegevenslandschap het ZGW kunnen ondersteunen.

Uitgangspunt voor de ZDS 2.0 is GEMMA 2 en daar waar GEMMA 2 nog niet Common Ground/Gegevenslandschap Proof is, gaan we uit van Gegevenslandschap/Common Ground. 
Openstaande vraag is backwards compatibility: lukt het om de ZDS API zo te ontwikkelen dat deze zowel binnen een GEMMA 2 landschap (huidige systemen/leveranciers) als een Gegevenslandschap gebruikt kan worden. Ook daarom is er eerst meer inzicht nodig in hoe (de informatiearchitectuur voor) ZGW in een Gegevenslandschap vorm krijgt.

## 1.2 Veranderingen agv het Gegevenslandschap

In GEMMA 2 worden processen zaakgericht uitgevoerd, ondersteund door informatiesystemen die invulling geven aan de generieke of specifieke Zaakafhandelcomponenten. De primaire verandering agv het gegevenslandschap zit in deze ondersteunende componenten.

We signaleren drie grote veranderingen daarin: scheiding van gegevens en proceslogica, (eenmalige) opslag en (meervoudige) bevraging van gegevens bij (of door) de bron en (mede daardoor) zeer beperkte informatie-uitwisseling (geen gegevensdistributie of ‘rondpompen’, alleen nog notificaties) tussen procesapplicaties. We gaan hierop hieronder in.

### 1.2.1. Opknippen Procesapplicaties

In GEMMA 2 en bijgevolg in ZGW in GEMMA 2 zijn de taakspecifieke informatiesystemen “geherwaardeerd” en deze als “Specifieke Zaakafhandelcomponenten” neergezet. Processen worden afgehandeld met een Zaakafhandelcomponent (ZAC, generiek of specifiek). De generieke ZAC slaat haar gegevens op in de Zaakregistratiecomponent (ZRC). Daarentegen slaat de specifieke ZAC alle gegevens zelf op: over de zaak en het proces, het verloop daarvan en veelal ook de registratie van de objecten waarop dat proces betrekking heeft. Vanuit deze component wordt een zaak geregistreerd (gekopieerd) in de ZRC en wordt deze zaak bij wijzigingen (ook) daarin bijgewerkt. Volgens het Gegevenslandschap moeten deze gegevens gescheiden worden van de procesapplicatie en in een of meerdere registraties worden ondergebracht en via gestandaardiseerde API’s ontsloten. 
Voor de Generieke Zaakafhandelcomponent is hierin al voorzien: deze beperkt zich tot de gegevensset zoals wordt bijgehouden in de Zaakregistratiecomponent (ZRC). Voor de specifieke ZAC heeft dit (vergaande) consequenties. Merk op dat zaakgegevens nu potentieel dubbel worden vastgelegd: zowel in de specifieke ZAC als in de ZRC.

### 1.2.2. Eenmalige opslag vanuit de bron

Common Ground gaat uit van het beschikbaar stellen en bevragen van gegevens bij de bron. Kopiëren en distribueren van gegevens (gegevensmagazijnen, gegevensdistributie,..) bestaan in een gegevenslandschap niet meer.  ‘Beschikbaar stellen bij de bron’ moet evenwel niet altijd letterlijk genomen worden. Anders zouden er precies evenveel registraties als procesapplicaties ontstaan, wat een nogal gefragmenteerde gemeentelijke informatiehuishouding zou opleveren en waarbij bijvoorbeeld telkens alle bronregistraties bevraagd zouden moeten worden om een overzicht te krijgen van alle lopende zaken. 
“Soortgelijke gegevens opslaan bij soortgelijke gegevens” is hiervoor een goed uitgangspunt. Zo ontstaan diverse “kernregistraties”: coherente en integere registraties met meervoudig gebruikte soortgelijke gegevens die vanuit verschillende procesapplicaties worden bijgehouden.  Bijvoorbeeld één gemeentelijke kernregistratie medewerkers en niet een (deel-)registratie per afdeling/proces. 

Voor het Zaakgericht werken heeft dit als gevolg dat veel objecten die nu in een Zakenmagazijn of procesapplicatie worden bijgehouden (behandelend medewerker, betreffend object, aanvrager (klant),..) vervangen moeten worden door een verwijzing naar de desbetreffende kernregistratie.

### 1.2.3. Vermindering van informatiestromen

In de huidige gemeentelijke informatievoorziening vindt de interactie tussen processen plaats door middel van gegevensuitwisselingsberichten tussen desbetreffende applicaties (cq. referentiecomponenten). De ontvangen informatie wordt veelal ook weer opgeslagen door en in de ontvangende procesapplicatie. Een voorbeeld zijn mutaties van het verblijfsadres van een burger (a.g.v. een verhuizing) die door de GBA- (cq. BRP-)beheerapplicatie verstrekt worden aan bijvoorbeeld een vergunningenapplicatie, belastingenapplicatie en sociaal domeinapplicatie.
In een gegevenslandschap is er van een dergelijke gegevensdistributie geen sprake meer. Hooguit wordt een proces genotificeerd over een gebeurtenis (zoals een verhuizing). De daarbij betrokken gegevens kunnen vervolgens, indien gewenst, door de ontvangende applicatie opgehaald worden uit de desbetreffende registratie (en niet opnieuw vastgelegd worden) om daarmee de voor het proces relevante afhandeling te kunnen doen. 
Het versturen van berichten met inhoud tussen verschillende referentiecomponenten wordt dus zoveel mogelijk beperkt en vervangen door het sturen van notificaties en het opvragen van de bijbehorende gegevens uit een registratie.
Specifieke aandacht verdienen aanvragen, meldingen e.d. die ‘op een website’ (of vanuit een App) ingediend worden. Het indienen wordt ondersteund door de referentiecomponent voor het aanvragen van producten en diensten (“e-Formulierencomponent”). In GEMMA 2 wordt een dergelijke aanvraag gerouteerd (in een bericht) naar de van toepassing zijnde generieke of specifieke ZAC. In een gegevenslandschap kan hiervan geen sprake zijn. Voor de hand liggend is dat de e-Formulierencomponent die aanvraag opslaat (vanuit de bron, dus; in een desbetreffende registratiecomponent; kernregistratie verzoeken?), een notificatie stuurt naar de desbetreffende ZAC die naar aanleiding daarvan de behandeling start (en daartoe onder meer de zojuist genoemde registratiecomponent bevraagt). 
 
## 1.3 Schets van de oplossing

### 1.3.1. Verandering

Samenvattend geven bovenstaande veranderingen aan dat we door toedoen van common ground en de architectuur van een gegevenslandschap, toe zijn aan een nieuwe fase in een zaakgerichte informatievoorziening. Opmerking AK Aan het zaakgericht werken an sich verandert niet zo veel of zelfs niets. Wel aan de wijze waarop de informatie daarvoor beschikbaar is. Dit past goed op de ontwikkelrichting zie ZGW al doorlopen heeft: van zakenmagazijn naast backoffice-silo’s die ongeschikt waren voor klantgerichte (online-) dienstverlening, via alles-in-een zaaksystemen, naar zaakgericht registreren en generieke en specifieke zaakafhandelcomponenten naar een volgende stap in het vormgeven van de informatie-architectuur onder het zaakgericht werken.
Hierbij gaan we uit van een, op basis van de visie op een gegevenslandschap, radicaal anders opgezet applicatielandschap. Daarin zijn veel uitdagingen die aanleiding hebben gegeven tot het zaakgericht werken veel integraler in de applicaties en registraties verwerkt. Voorbeelden van dergelijke uitdagingen zijn het verbeteren van de dienstverlening, een beter inzicht in proces- en voortgang uit back-office applicaties en digitaal uniform archiveren etc.. En zaakinformatie als gevolg niet meer op één centrale plats zit, maar gedistribueerd over meerdere registraties.

Opmerking AK Is dat zo? Kern is en blijft toch de ZRC?! De kernregistratie zaken. Zaakinfo zit dan nog steeds op één plek. Aan zaken gerelateerde info, zoals gegevens van betrokkenen, van medewerkers en van objecten waarop zaken betrekking hebben, ja, die zitten elders.
Grof geschetst bewegen we van een situatie zoals in figuur 1 naar een situatie zoals in figuur 2.

### 1.3.2. Huidige Situatie

In figuur 1 staat een schets van de huidige situatie zoals min of meer beschreven door GEMMA 2.

Figuur 1: ZGW in de huidige situatie (~GEMMA 2)

* Een zaak is geregistreerd in een ZRC. Aan een zaak gerelateerde objecten (RGBZ) worden ook geregistreerd in de ZRC: betrokkenen, besluiten, klantcontacten, zaakobjecten en eventuele zaaktypespecifieke objecten met zaaktypespecifieke eigenschappen.
* Vanuit een zaak liggen er verwijzingen naar zaaktype (ZTRC), Document vcq. informatieobject (DRC) en eventuele objecten (in theorie de Basisregistratie, maar vaak Gegevensmagazijn)
* Voor betrokkene is in theorie ook sprake van een verwijzing (naar BRP en HR, kernregistratie medewerkers, kernregistratie bedrijven, kernregistratie klanten,..), maar in de praktijk wordt dit vaak in de ZRC zelf opgeslagen.
* De Zaakafhandelcomponent bevat nog veel gegevens:
    * procesdefinities (hoe moet een proces lopen, welke keuzes zijn er mogelijk);
    * procesgegevens (waar in het proces zitten we, welke keuzes zijn in het proces gemaakt, wie is de behandelaar, welke gegevens heeft hij gebruikt voor welke processtap, ..)
    * domein/objectgegevens: gegevens over objecten in het domein waartoe het proces behoort. Bijvoorbeeld voor een Subsidiesysteem de gegevens over een aangevraagde subsidie, doelen die men met subsidies wil stimuleren en de voorwaarden en uitnutting van diverse subsidiepotjes.

* “Aanvraag” mist in dit plaatje. Dat klopt ook. Deze maakt onderdeel uit van de domein/objectgegevens. In de huidige praktijk wordt een aanvraag ook nog vaak (onterecht) met een zaak vereenzelvigd. Waarbij het in de vorm van een Informatieobject als PDFje wordt opgeslagen bij een zaak. 
* Er bestaat in de ZRC geen rechtstreekse relatie tussen het merendeel van de domein/objectgegevens en een zaak (dit is beperkt tot zaakobjecten en zaaktypespecifieke gegevens). Idem voor gedetailleerde procesgegevens en een zaak. M.a.w. in het geval van erg complexe processen, kent de zaak in de ZRC enkel dit proces op hoofdlijnen (de zaakstatussen).
* Wel liggen deze relaties in de specifieke zaakafhandelcomponent: daarin is (impliciet of expliciet) een proces geconfigureerd (=procesdefinitie (“procestype”), bijvoorbeeld afhandelen evenementensubsidieaanvraag). Het verloop van een specifieke instantie van dat proces volgt dit procestype. En er liggen relaties tussen dit proces en de domein/objectregistratie(s) die bij dit proces horen.
* De ZAC heeft wel uiteraard weet van welk zaaktype en welke zaak er bij een bepaald procestype en bij een bepaalde procesinstantie horen, maar vanuit een zaak is dit dus niet direct opvraagbaar. Opmerking AK De specifieke ZAC, ja.. Maar de generieke ZAC toch niet?

### 1.3.3. Situatie in een Gegevenslandschap

In een gegevenslandschap komt bovenstaand plaatje er, door het scheiden van proces en data, eenmalige opslag en bevraging ‘bij de bron’ en het verminderen van informatiestromen anders uit te zien (zie figuur 2):
* De domein/objectgegevens gegevens zijn uit de Zaakafhandelcomponent verdwenen. Procesdefinities en procesgegevens blijven daar echter achter .
* Uitgangspunt in het gegevenslandschap is: alle gegevens worden op één plaats opgeslagen. En alle soortgelijke gegevens worden bij elkaar opgeslagen. Er komt dus een registratie met besluiten, een registratie met aanvragen en meldingen, een registratie met klanten, een registratie medewerkers. Etc.
* De “Zaak” is een belangrijk verbindend element tussen de objecten in de registraties. Getekend: een zaak aggregeert al deze andere objecten. Zaak fungeert zo als “sleutel” in een grote “verwijsindex” naar objecten in andere registraties.  Opmerking AK En wat moet ik me daarbij voorstellen, wat is het nut daarvan? Welke op hun beurt weer kunnen relateren naar concepten in andere registraties, bv. de BRP of het HR. Opmerking AK Er zijn ook andere verbindende objecten zoals de klant (of een NP of NNP) die een mail gestuurd heeft (document), houder is van een vergunning, een handhavingsverzoek heeft ingediend (aanvraag/melding) en een paspoort heeft gekregen. Dergelijke relaties zijn in de figuur niet gevisualiseerd. Terecht, de focus is zaakgericht werken. Maar wel even vermelden.
* Documenten die bij een zaak horen kunnen dan in de DRC worden opgehaald mbv het zaaknummer. Idem voor besluit(en) per zaak en betrokkenen. 
* Dit komt sterk overeen met het concept Linked-data
Opmerking AK Wat is de overeenkomst dan? M.i. is het simpelweg een objecten- of informatiemodel met objecten en relaties. LinkedData is dan een manier om gebruik te kunnen maken van de in die modellen onderscheiden relaties. De Zakenregistratiecomponent is dus niet meer één grote database met daarin alle gegevens over een zaak. Maar meer een kernregistratie van zaken met veel links (URL’s) naar objecten in andere registraties (dan wel verwijzen andere objecten naar zaken).
Opmerking AK Essentie hiervan is dat objecten die nu in het RGBZ en daarmee in de ZRC voorkomen maar ook relevantie hebben in een andere context of domein, als aparte registratie neergezet worden om recht te doen aan de betekenis als zelfstandige objecttype.
* Dit kunnen zijn (niet uitputtend):
    * Kernregistratie Klanten en Contacten (voor initiators,  belanghebbenden, gemachtigden e.d.)
    * Kernregistratie medewerkers (o.a. voor behandelaars)
    * Kernregistratie besluiten (besluiten)
* Documentregistratiecomponent (documenten cq. informatieobjecten)
    * Zaaktyperegistratiecomponent (Zaaktype, Statustypen, Resultaattypen,..)
    * Domein/objectregistraties (domein/objectgegevens; meerdere registraties: één per domein/proces)
    * Meldingenregistratie (ontvangen aanvragen en meldingen)
    * Basisregistraties (personen, bedrijven, panden, terreinen, percelen e.d.)
    * Evt. andere kernregistraties (Zaakobjecten die nog niet genoemd zijn, maar wel behoren tot kerngegevens (meervoudig gebruikt))
 


Figuur 2: ZGW in een gegevenslandschap

## 1.4 Vraagstukken

Bovenstaande plaat schetst het concept ZGW in een gegevenslandschap al heel aardig.

Toch zijn er nog enkele openstaande vragen te beantwoorden. Voor een deel is dit al af te leiden uit de stippellijnen in bovenstaande plaat:

### 1.4.1. Hoe verhoudt melding/verzoek zich tot een zaak?

In bovenstaande figuur is de relatie tussen Melding/Aanvraag (Verzoek) en Zaak als een stippellijn getekend. Dit omdat Verzoek niet in het RGBZ voorkomt (zat wel in GFO Zaken) en we dus niet weten hoe Verzoek en Zaak zich tot elkaar verhouden. Essentie van de relatie lijkt te zijn dat een verzoek of melding een op zich zelf staand ‘iets’ is en behandeld wordt als zaak. Één verzoek kan leiden tot meerdere zaken. Meerdere Verzoeken kunnen ook leiden tot één Zaak? 
Documenten bij een Verzoek worden bij het Verzoek vastgelegd. Later ook rechtstreeks gerelateerd aan de zaak?

### 1.4.2. Waar slaan we procesinformatie op?

Het is nog onduidelijk waar we in een gegevenslandschap “Procesinformatie” willen opslaan. In bovenstande figuur is dit – samen met procesdefinitiegegevens - gepositioneerd in de Zaakafhandelcomponent (net als nu in de diverse Taaksystemen). 
Dit is echter (mogelijk) in strijd met het uitgangspunt in Common ground dat functionaliteit en gegevens van elkaar gescheiden moeten zijn. Procesgegevens zijn immers ook gegevens. 
De procesdefinitie is in veel gevallen zelfs impliciet (hard gecodeeerde flow tussen schermen); dat valt dan niet eens los te knippen.

Conclusie: hier is sprake van een glijdende schaal. Je wilt liefst alle domeingegevens en zo veel mogelijk procesgegevens uit de applicaties halen en via een gestandaardiseerde APi ontsluiten. We moeten echter wel oppassen dat we hier te ver in willen gaan en het paard daarmee achter de wagen spannen. In de praktijk zal dit voor veel bestaande taaksystemen een groeipad worden..

Er is één maar. Het delen van procesinformatie is nodig om het handelen als overheid te verantwoorden: het moet dus gearchiveerd worden. Wie heeft op welke datum welke stap gezet? Welke procesflow (en keuzes) is er doorlopen? Welke informatie was wanneer beschikbaar? Hoe luidde de (deel)berekening die heeft geleid tot een bepaald resultaat? Dit is informatie die niet in één van de andere registraties past (tenzij als logfile in PDF in de DRC) en voor het grootste deel niet in de ZRC wordt vastgelegd (die kent meestal maar één behandelaar en vooral enkel het proces op hoofdlijnen: de Statussen).
Dit pleit voor een procesverloopregistratie, waarin op een zo gestandaardiseerde manier als mogelijk informatie over het verloop van alle processen wordt bijgehouden. Probleem is echter dat het ene proces het andere niet is en het erg moeilijk is dit gestandaardiseerd te doen (een zaak probeert dat feitelijk ook, en deze kent niet voor niets enkel statussen). Dus wellicht krijg je dan een subsiedieprocesverloopregistratie, een vergunningprocesverloopregistratie, een burgerzakenprocesverloopregistratie, … Dat is dan weer niet aanlokkelijk.
Wellicht dat een combinatie met de desbetreffende domeinregistratie dan nog het meest voor de hand ligt. Een domeinregistratie Vergunningen (en handhaving), waarin –volgens een gestandaardiseerd informatiemodel- naast de in het vergunningproces betrokken objecttypen, ook het verloop van de vergunningprocessen wordt geregistreerd.
 
### 1.4.3. Relatie proces – zaak

In de figuur staat ook een stippellijn getekend tussen Zaak en Procesgegevens. Proces staat niet gedefinieerd in het informatiemodel RGBZ, en dus ligt de relatie zaak – proces ook niet eenduidig vast. 
In GFO zaken was dit min of meer wel het geval met “stap”. Hieruit, en vooral uit de prominente rol van ‘status’ in het RGBZ, blijkt al dat het moeilijk is om alle soorten processen op een eenduidige manier te registreren. Uiteindelijk kom je dan bij een informatiemodel met de rijkheid van BPMN uit (en voor de meer adaptieve processen iets dat lijkt op CMMN). Wat uiteraard niet de bedoeling is.
Maar indachtig de vorige vraag: “waar registreren we procesinformatie”, is het noodzakelijk dat de relatie zaak-proces goed is gedefinieerd, zodat we als we nadere procesinformatie willen weten van een zaak, deze bij een zaaknummer kunnen opvragen (indien beschikbaar).

### 1.4.4. Redundantie van gegevens in de ZRC?

In navolging van bovenstaande 2 vragen: als er een goede processenregistratie is per proces, die via een API ontsloten wordt, is een centrale ZRC dan niet meer nodig? Gegevens in de ZRC zijn allemaal afgeleid van de procesgegevens. De ZRC bevat dan in feite een kopie of abstractieslag van deze procesgegevens en zondigt hiermee wellicht tegen het gegevenslandschap-principe van éénmalige opslag. Of is die abstractie of afleiding wellicht niet zodanig in een algoritme te vatten dat eenduidig zaakgegevens af te leiden zijn? 
Een Zaken-API zou dan een tweede API op de bakjes met procesinformatie kunnen zijn. Het nadeel: meerdere registraties moeten aanroepen voor een compleet overzicht over zaken, kan dan worden opgelost met een index-service oid.
In de praktijk zal een ZRC nog lang nodig blijven, maar het is wel goed om al over deze (of andere) stip op de horizon na te denken.

### 1.4.5. Hoe objecten relateren aan een zaak?

Objecten worden in het RGBZ aan een zaak gerelateerd dmv. “Zaakobject”: “een Object waarop de zaak betrekking heeft”.  In theorie kun je hier veel kanten mee op. In de praktijk zal het gebruik hiervan beperkt zijn tot voornamelijk basisregistratieobjecten. In een gegevenslandschap moeten veel meer soorten objecten aan een zaak gerelateerd kunnen worden. De zaak vormt immers de sleutel om deze bij elkaar te kunnen houden. Denk bijvoorbeeld aan verleende subsidies, uitgegeven marktplaatsen, grafrechten, etc. Vroeger werden deze objectenregistraties bijgehouden in het processysteem en lag daar impliciet de relatie tussen de zaak en deze objecten. Het Gegevensandschap vraagt om een andere, meer integrale benadering.
Het is daarom de vraag of de relatie zaak – object zoals gedefinieerd in het RGBZ (zaak heeft betrekking op object) hiervoor voldoende is genoeg is.
Afgeleide vraag hiervan is het in operationele zin aan elkaar relateren van objecten in diverse bakjes aan een zak in een ZRC. Opmerking AK https://github.com/VNG-Realisatie/gemma-zaken/projects/3#column-3039059

### 1.4.6. Welke bakjes onderkennen we?

In de uitwerking hierboven hebben we al enkele registraties (‘bakjes’) naast de ZRC onderscheiden. Een aparte registratie met besluiten, een aparte registratie voor documenten (bestaat nu vaak al), een aparte registratie voor klanten en klantcontacten,…
Dit is echter slechts een eerste aanzet en nog niet volledig uitgewerkt. Willen we voor iedere “object” een aparte registratie? 
Opmerking AK  Benoem domeinen, werk de informatievoorzienin daarvan uit in informatiemodellen en je hebt de objecttypen, registraties en bakjes. Zo simpel is dat … 
Of horen sommige objecten echt bij elkaar? Wat is de relatie met het ImZTC? Om de eenduidigheid van de implementaties ten goede te komen, is het nodig om dit verder uit te werken.  Hoe vertalen we de objecten uit het RGBZ naar registraties in een gegevenslandschap en hoe relateren we deze aan elkaar? Met het informatiemodel laten we de implementatie nadrukkelijk vrij.
In een gegevenslandschap is het wenselijk om dit verder uit te werken in een gegevensmodel. En wellicht ook met een concreet voorbeeld om dit concept aan iedereen goed duidelijk te maken.

### 1.4.7. Wat willen we doen met Zaak?

Zaakgericht werken kent al een lange geschiedenis. Het stamt uit de tijd dat dienstverleningsambities hoger werden en backoffice-applicaties dit niet of nauwelijks aankonden. Daarna was er de gedachte dat een “alles-in-1 zaaksysteem” voor veel processen voldoende zou zijn. Inmiddels draait de slinger een beetje terug en zien we taakspecifieke systemen moderner en opener worden. In een gegevenslandschap is dit helemaal het geval.

In de loop der jaren zijn er diverse doelen voor zaakgericht werken ontstaan: dienstverlening verbeteren, als basis voor het archiveren, het bieden van managementinformatie,.. waarvan het de vraag is of je ze in een modern applicatielandschap nog met zaakgericht werken wilt oplossen. In het geval van een gemeente die met één dominant generiek zaaksysteem werkt ligt de oplossingsrichting voor de hand. In een gegevenslandshap veel minder. Bovendien zien we op vele vlakken een terugtrekkende beweging op het “gemeentebrede” dienstverlenigsconcept, meer richting domeinspecifieke Apps en portalen. Een meer domeingerichte dienstverlening en informatievoorziening (ipv generiek obv zaken) ligt dan meer voor de hand. Opmerking AK  Die twee zijn niet strijdig. Het lijkt er op dat in de redenering  en de voorbeelden het zaakgericht werken als panacee voor alle problemen en behoeften wordt gezien. Evenwel, zaakgericht werken is niet mee of minder dan een manier van procesgericht werken. Een manier die zo ver is uitgewerkt dat anderen dan de uitvoerenden van een proces dat proces ook kunnen begrijpen, op het niveau dat voor een ander volstaat: de hoofdlijnen. Dit ‘esperanto’ blijft een onderscheidend kenmerk van zaakgericht werken en zaken. Je krijgt daarmee twee niveau’s: domeinspecifiek en domeinoverstijgend. Het tweede doen we met zaken.

Enkele voorbeelden:
1. Een gemeente wil alle Meldingen Openbare Ruimte op een kaart tonen. Vraag je hiertoe alle melding-zaken op met een generiek ZDS-koppelvlak? Wetende dat de AVG dit voor het overgrote deel aan zaken/zaaktypen niet toestaat? Of kies je voor een meldingen-specifiek koppelvlak, dat mogelijk functioneel rijker is: type melding, prioriteit van de melding, tekstuele toelichting…allemaal wellicht nuttig om op een dergelijke kaart te kunnen weergeven. Maar niet of slechts met moeite (zaaktypespecifieke eigenschappen) met een generiek zaken-koppelvlak te realiseren.
2. Hoe wil je een proceseigenaar/afdelingshoofd van management-informatie voorzien? Op basis van zaken kun je erg generieke metrieken weergeven. Aantal zaken per afdeling, aantal zaken per status, zaken die voor of achter lopen op plandatum etc. Toch is het vergelijken van een subsidiezaak met een vergunnningenzaak appels met peren vergelijken. En zit een manager vergunningen vermoedelijk op heel andere metrieken te wachten: aantal vergunningen per wijk, aantal afhandeluren per bouwvolume-eenheid etc.
3. Hoe wil je status-informatie weergeven aan de klant? Heel generiek obv enkel voorgedefinieerde “zaakstatussen”, of wil je dit functioneel rijker doen in een domeinspecifiek portal, bijvoorbeeld specifiek voor subsidies?

Het is belangrijk om hier als gemeente even goed bij stil te staan. In veel gevallen zal het nog steeds handig blijken om iets met zaken op te lossen, of misschien beide: generieke informatie via zaken tonen en als aanvulling daarop enkele functioneel rijkere portalen of apps per domein.

### 1.4.8. Notificeren over zaken

In een gegevenslandschap willen we geen zaken (of andere informatie) meer “rondsturen”. Vraag is wel hoe een behandelaar met een taakapplicatie te weten komt dat er een melding voor hem beschikbaar is die behandeld moet worden. Er zijn nog andere scenario’s te bedenken, waarin het nuttig is dat een partij actief wordt genotificeerd over een zaak(status). Bijvoorbeeld bij meerdere behandelaars die met meerdere systemen werken (of moeten we dat niet willen?), of wanneer er een nieuw document aan een zaak is toegevoegd door een KCC-medewerker. Het is nuttig om enkele van deze scenario’s uit te werken binnen de context van een gegevenslandschap en hiervoor een generieke oplossing voor te stellen. Een verdere uitwerking van https://www.gemmaonline.nl/index.php/ZGW_in_GEMMA_2_compleet#Notificeren_over_Zaken binnen een gegevenslandschap.

## 1.5 Uitwerking voor een specifieke casus

* Acties bovenstaande uitwerken voor een specifiek voorbeeld, met echte gegevensmodellen… Opmerking AK Hoe stel je je dat voor? Ik heb er nog geen beeld bij. Waarop doel je met ‘bovenstaande’?

## 1.6 Consequenties voor ZDS en andere standaarden 

* Acties hoe kunnen ZDS standaarden zowel GEMMA 2 als CG ondersteunen?
* Acties migratie: hoe de standaarden vormgeven, zodat hier stapsgewijs naartoe kan worden gemigreerd
