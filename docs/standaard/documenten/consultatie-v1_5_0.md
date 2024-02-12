# Consultatie specificaties Documenten API versie 1.5

Op initatief van een aantal gemeenten en leveranciers worden onderstaande wijzigingen aan belanghebbenden voorgelegd. Het voornemen is dat het gewijzigd of ongewijzigd doorvoeren van deze aanpassingen leidt tot het uitbrengen van een nieuwe _minorversie_ van de Documenten API (1.5). De user story waarin de discussie die tot deze voorgestelde wijzigen heeft geleid is [#2242](https://github.com/VNG-Realisatie/gemma-zaken/issues/2242).

De voorgestelde wijzigingen worden hieronder in vier onderdelen nader toegelicht. ['Wat wordt gewijzigd?'](#wat-wordt-gewijzigd) en ['wat is nieuw?'](#wat-is-er-nieuw) beschrijven de voorstelde wijzigingen. ['Wat vervalt (op termijn?')](#wat-vervalt-op-termijn) licht toe op welke manier duidelijk wordt gemaakt dat bepaalde property's bij voorkeur niet meer worden gebruikt en hoe we die uiteindelijk uit de standaard gaan verwijderen. [Aandachtspunten en vragen bij deze consultatie](#aandachtspunten-bij-deze-consultatie) noemt een aantal zaken waarover belanghebbenden naar aanleiding van consultatie specifiek zouden kunnen nadenken.

## Wat wordt gewijzigd?

Hieronder is ter referentie steeds hetgeen vervalt (of depricated wordt verklaard) doorgehaald.

### property 'status'

#### Beschrijving

~Aanduiding van de stand van zaken van een informatieobject. De waarden `in bewerking` en `ter vaststelling` komen niet voor als het attribuut ontvangstdatum van een waarde is voorzien. Wijziging van de Status in 'gearchiveerd' impliceert dat het informatieobject een duurzaam, niet-wijzigbaar Formaat dient te hebben.~

Geeft de status van het informatieobject aan in een proces van bewerking en eventuele vaststelling.

#### Toegestane waarden

Waarde | Betekenis
-- | --
null |
in_bewerking | ~Aan het informatieobject wordt nog gewerkt.~ De inhoud van het informatieobject kan op ieder moment en onaangekondigd veranderen.
concept _(geheel nieuw)_ | De inhoud van het informatieobject heeft een mate van bestendigheid bereikt waardoor die aan derden ter beoordeling kan worden voorgelegd. Deze beoordeling kan leiden tot verandering van de inhoud van het informatieobject.
definitief | ~Informatieobject door bevoegd iets of iemand vastgesteld dan wel ontvangen.~ De inhoud van het informatieobject heeft een mate van bestendigheid bereikt waardoor die niet (langer) zomaar veranderd kan worden.
ter_vaststelling | ~Informatieobject gereed maar moet nog vastgesteld worden.~ De inhoud van het informatieobject is betrokken bij een lopend besluitvormingsproces.
vastgesteld _(geheel nieuw)_ | De inhoud van het informatieobject is tijdens een besluitvormingsproces bekrachtigd.
~gearchiveerd~ | ~Informatieobject duurzaam bewaarbaar gemaakt; een gearchiveerd informatie-element.~

#### Rationale voor wijzigingen

Bij gebruik van de bestaande toegestane statuswaarden werden de volgende problemen geconstateerd:

- het toekennen van de waarde `gearchiveerd` resulteerde in verlies van kennis over bewerking of vaststelling. Was sprake van een gearchiveerd concept (een informatieobject met als voorlaatste status `in_bewerking`) of een definitief informatieobject (met als voorlaatste status `definitief`)? Dit heeft geleid tot het 'lostrekken' van 'archiefstatus' uit 'status'.
- De waarde `definitief` was ambigu. Die kón betekenen dat de inhoud van een informatieobject in een formeel besluitvormingsproces was bekrachtigd, maar ook dat eenvoudigweg sprake was van een door de gemeente ontvangen informatieobject waarin door de gemeente zelf geen wijzigen mogen worden doorgevoerd. Dit heeft geleid tot het toevoegen van de status `vastgesteld` en het aanpassen van de betekenis van `definitief`.
- Er was behoefte aan het middels statussen onderscheid aanbrengen tussen informatieobjecten waaraan in kleine kring wordt gewerkt en informatieobjecten die een zekere mate van volwassenheid hebben bereikt waardoor die aan een groep belanghebbenden ter consultatie kan worden voorgelegd. Dit heeft geleid tot het toevoegen van de status `concept` en het aanpassen van de betekenis van `in_bewerking`.

#### Toelichting bij de nieuwe set toegestane statuswaarden

Deze set statussen is feite een samenstelling van twee verzamelingen 'statustypen'. De waarden `in_bewerking`, `concept` en `definitief` representeren punten op de 'bewerkingstijdslijn' die helpen te bepalen hoe de 'volwassenheid' van de inhoud van het informatieobject moet worden beoordeeld.

`ter_vaststelling` en `vastgesteld` liggen op de 'besluitvormingstijdslijn' en geven aan hoe ver het besluitvormingsproces waarin het informatieobject een rol speelt, gevorderd is.

Besluitvorming gaat vrijwel altijd over 'definitieve' inhoud van informatieobjecten. Dit betekent dat sprake is van een 'opvolgende' reeks statussen. Hierdoor konden de statussen die horen bij de twee verschillende tijdslijnen in één verzameling worden opgenomen. 

Een informatieobject hoeft zeker niet altijd alle statussen te doorlopen. Al terwijl een informatieobject nog `in voorbereiding` is kan bijvoorbeeld duidelijk worden dat de dienst waaraan de inhoud daarvan bijdroeg niet geleverd hoeft te worden. Bovendien wordt de inhoud van veel informatieobjecten niet in een besluitvormingsproces bekrachtigd. En ontvangen informatieobjecten worden (door de gemeente) niet bewerkt en krijgen dus direct na ontvangst de status `definitief`.

Voor de betekenis bij de verschillende waarden is getracht consequent het informatieobjectperspectief als uitgangspunt te nemen:

- bij de betekenis van de eerste drie waarden (`in_voorbereiding`, `concept` en `definitief`) is als uitgangspunt de mate van verandering (of omgekeerd de 'volwassenheid') genomen die van de inhoud van het informatieobject bij het bereiken van een status verwacht mag worden.
- bij de betekenis van de laatste twee waarden (`ter_vaststelling` en `vastgesteld`) is het besluitvormingsproces als uitgangspunt genomen, maar ook geprobeerd (met name bij `vastgesteld`) geprobeerd te beschrijven wat het doorlopen van dit proces betekent voor de inhoud van het informatieobject ("het is bekrachtigd").

De Bewerkings- en vaststellingsstatus `definitief` moet niet verward worden met de Archiefstatus `onmuteerbaar`. Die laatste betekent in feite "geen enkele wijziging toegestaan". Voor zover het gaat om door de gemeente gecreëerde informatieobjecten betekent `definitief` daarentegen dat naar aanleiding van overleg, reviews en afspraken een 'overeengekomen' of 'afgestemde' versie van informatieobjectinhoud is ontstaan. Wijzigingen hierin zijn niet verboden, maar zullen in veel gevallen vragen om verantwoording bij doorgevoerde wijzigingen op basis van nieuwe reviews en afspraken.

Rationale en tabel illustreren dat, door voor te stellen bovenstaande wijzigingen in een minor-versie van de Documenten API te verwerken, een situatie ontstaat waarin sommige waarden meerdere betekenissen kunnen hebben. Onder aandachtspunten wordt uitgelegd waarom hiervoor toch is gekozen.

### Gedragsregel 'Zetten Zaak.archiefstatus (zrc-022)'

Link huidige: [zrc-022](../zaken/index.md/#archiveren)

De standaardwaarde voor archiefstatus [van de zaak, IH] is `nog_te_archiveren`. Indien een andere waarde gezet wordt, dan MOETEN alle gerelateerde informatieobjecten de status `gearchiveerd` (depricated) EN/OF de archiefstatus `onveranderlijk` of `duurzaam_toegankelijk` hebben (zie [archiefstatus](#property-archiefstatus) hieronder).

De attributen Zaak.archiefnominatie en Zaak.archiefactiedatum MOETEN een waarde krijgen als de de archiefstatus een waarde krijgt anders dan nog_te_archiveren.

Indien deze voorwaarden niet voldaan zijn, dan MOET het ZRC met een HTTP 400 foutbericht antwoorden.

#### Rationale voor wijziging

Dat informatieobjecten na afsluiten van een zaak niet meer ('zomaar') gewijzigd kunnen worden, is een algemeen geldende eis. Bovenstaande is daarom een uitvoerbare gedragsregel met algemene geldigheid. De wijziging in deze regel ontstaat omdat statussen die te maken hebben met archivering zijn verhuisd van `status` naar `archiefstatus`. Zowel de archiefstatussen `onveranderlijk` of `duurzaam_toegankelijk` geven invulling aan de eis van onmuteerbaarheid. En zolang de bestaande statuswaarden met de toevoeging 'depricated' gebruikt mogen worden blijft ook registratie van `gearchiveerd` bij `status` een geldige manier om aan deze gedragsregel te voldoen. 

### Gedragsregel 'Statuswijzigingen van informatieobjecten (drc-005)'

Link huidige: [drc-005](./index.md/#statuswijzigingen-van-informatieobjecten-drc-005)

~Wanneer `InformatieObject.ontvangstdatum` een waarde heeft, dan zijn de waarden `in bewerking` en `ter_vaststelling` voor InformatieObject.status NIET TOEGESTAAN. Indien een dergelijke status gezet is voor de verzenddatum opgegeven wordt, dan moet de API een HTTP 400 foutbericht geven met status als veld in de invalid-params. De client MOET dan ontvangstdatum leeg laten of eerst de status wijzingen.~

#### Rationale voor wijziging

Dit is een complexe gedragsregel waarvan moeilijk is vast te stellen dat die altijd geldt. En dat laatste is een voorwaarde voor opname in de standaard. Ja, in veel gevallen (ontvangen bouwtekening voor omgevingsvergunning, ontvangen inkomensverklaring bij aanvraag stadspas) mag een ontvangen informatieobject niet door de gemeente bewerkt worden. Maar als sprake is van informatieobject waarvan de inhoud door (keten)samenwerking tot stand komt, kunnen best wijzigingen in een ontvangen informatieobject worden aangebracht. Bij het voorstel deze regel te schrappen hoort daarom het aandachtspunt dat medewekers van de gemeente ervoor zorgdragen dat in ontvangen informatieobjecten waarin geen wijzigingen mogen worden aangebracht, dit ook niet gebeurt.

## Wat is nieuw?

### property 'archiefstatus'

#### Beschrijving

Geeft aan in hoeverre het informatieobject duurzaam toegankelijk is en op het voorgeschreven moment vernietigd of overgebracht kan worden.

#### Toegestane waarden

Waarde | Betekenis
-- | --
null |
mutabel | Vorm en inhoud van het informatieobject kunnen vrijelijk veranderen.
onveranderlijk | Vorm en inhoud van het informatieobject zijn onveranderlijk geworden zodat authenticiteit en integriteit gewaarborgd zijn.
duurzaam_toegankelijk | Het informatieobject voldoet aan de eisen van duurzame toegankelijkheid (het is vindbaar, beschikbaar, leesbaar, interpreteerbaar, betrouwbaar en toekomstbestendig) en kan op het in de selectielijst voorgeschreven moment vernietigd of overgebracht worden.

#### Toelichting

Deze set statussen geeft aan in hoeverre het informatieobject voldoet aan de eisen voor 'duurzaam toegankelijk overheidsinformatie'. Of in andere woorden: in hoeverre het informatieobject als 'gearchiveerd' kan worden beschouwd.

De waarde `mutabel` geeft aan dat het informatieobject nog vrijelijk bewerkt kan worden. Het informatieobject bevindt zich in wat ook wel de 'dynamische fase' genoemd werd.

De waarde `onveranderlijk` geeft aan dat het informatieobject is 'bevroren'. Inhoud en vorm liggen nu vast. Hiermee zijn authenticiteit en integriteit van het informatieobject gewaarborgd. Door het uitvoeren van informatiebeheershandelingen kan nog wel de duurzame toegankelijkheid van het informatieobject worden verbeterd. Voor het verkrijgen van deze status is het echter geen eis dat het informatieobject aan alle relevante bijbehorende eisen voldoet.

De waarde `duurzaam_toegankelijk` geeft aan dat informatiebeheershandelingen ertoe hebben geleid dat het informatieobject voldoet aan relevante eisen voor duurzame toegankelijkheid. Het is, voor zover deze kwaliteiten afhankelijk zijn van de vorm waarin het informatieobject is geregistreerd of de metadata die daarbij zijn vastgelegd, _vindbaar_, _beschikbaar_, _leesbaar_, _interpreteerbaar_, _betrouwbaar_ en _toekomstbestendig_. Concreet betekent dit bijvoorbeeld dat de inhoud van het informatieobject is geregistreerd in een duurzaam bestandsformaat. Deze waarde betekent ook dat bepaald kan worden op welk moment het informatieobject vernietigd of overgebracht moet worden worden (let op: dit hoeft niet te betekenen dat een concrete vernietigings- of overbrengingsdatum bekend is - [die kan immers afhankelijk zijn van een nog niet bekend datumkenmerk bij een procesobject](https://redact.gemmaonline.nl/index.php/4._De_Selectielijst_in_de_praktijk). Informatiebeheeractiviteiten houden niet op bij het bereiken van deze status. Het duurzaam toegankelijk houden van informatieobjecten vereist, zeker bij lange bewaartermijnen, immers voortdurend aandacht.

Een informatieobject hoeft niet altijd alle archiefstatussen te doorlopen. Ontvangen informatieobjecten worden (door de gemeente) niet bewerkt en krijgen dus direct na ontvangst de status `onveranderlijk` of - als aan de bijbehorende eisen is voldaan - `duurzaam toegankelijk`. En als de daarvoor benodigde informatiebeheeractiviteiten worden uitgevoerd als onderdeel van het primaire proces waarin een informatieobject ontstaat (['archiveren by design'](https://www.nationaalarchief.nl/archiveren/kennisbank/archiving-by-design-en-vernietigen) kan een informatieobject van `mutabel` ineens `duurzaam_toegankelijk` worden.

#### Rationale voor toevoeging

- het toekennen van de waarde `gearchiveerd` resulteerde in verlies van kennis over bewerking of vaststelling. Was sprake van een gearchiveerd concept (een informatieobject met als voorlaatste status `in_bewerking`) of een definitief informatieobject (met als voorlaatste status `definitief`)? Dit heeft geleid tot het 'lostrekken' van 'archiefstatus' uit 'status'.
- [Gedragsregel zrc-022](#gedragsregel-zetten-zaakarchiefstatus-zrc-022) vereist dat aan een zaak gerelateerde informatieobjecten bij afsluiten van de zaak de status `gearchiveerd` hebben. In de pratijk is er niet altijd sprake van dat informatieobjecten op dit moment ook zoals de huidige defintie omschrijft 'duurzaam bewaarbaar zijn gemaakt'. Activiteiten die daaraan bijdragen (zoals het omzetten naar een duuzaam bewaarbaar bestandsformaat) kunnen immers ook ná afsluiten van de zaak plaatsvinden. Wél vereist is dat de inhoud van informatieobjecten na afsluiten van de zaak niet zomaar meer kan worden aangepast. Het toestaan van mutaties staat immers verantwoording over het verloop van de zaak in de weg. Dit heeft geleid tot het toevoegen van de archiefstatussen `muteerbaar` (voor gebruik tijdens lopende zaken zolang de inhoud van het informatieobject mag worden aangepast), `onveranderlijk` (wanneer de inhoud van het informatieobject om welke reden dan ook 'onherroepelijk' is geworden) en `duurzaam_toegankelijk` (wanneer het aan alle voor het specifieke informatieobject noodzakelijke eisen ten aanzien van duurzame toegankelijkheid voldoet).

### property 'inhoudIsVervallen'

#### Beschrijving

Geeft aan of de inhoud van het informatieobject vervallen (dus niet langer geldig) is.

#### Toegestane waarden

Waarde | Beschrijving
-- | --
null |
true | De inhoud van het informatieobject is vervallen
False | De inhoud van het informatieobject is niet vervallen.

#### Rationale voor toevoeging

- Er was behoefte aan een manier om aan te geven dat informatieobjecten niet langer 'van belang' zijn, bijvoorbeeld omdat ze zijn vervangen door een ander informatieobject dat met andere inhoud gaat over hetzelfde onderwerp.

#### Toelichting

Het begrip 'vervallen' in deze indicatie moet gelezen worden als 'ongeldig geworden'. Geldigheid moet in deze context zowel 'breed' als 'eng' gelezen worden.

- Breed in de zin dat verlies van geldigheid van de inhoud van een informatieobject zowel het gevolg kan zijn van een formele procedure, zoals de herroeping van een besluit, als van informele handelingen, zoals een bouwtekening waarvan de inhoud door het verschijnen van een meer actuele illustratie achterhaald is. Hoewel we in het dagelijks taalgebruik in het laatste geval waarschijnlijk zouden zeggen dat de bouwtekening "niet meer actueel is", benoemen we die in de context van deze indicatie als "niet meer geldig, dus vervallen".

- Eng in de zin dat verlies van geldigheid niet betekent dat een informatieobject in het geheel geen waarde meer heeft. Een herroepen besluit kan immers aanleiding geven voor aantekenen van bezwaar of beroep. En de 'vervangen' bouwtekening kan vanuit cultuurhistorisch perspectief best heel interessant (blijken te) zijn.

### property 'bevatNietOpenbarePersoonsgegevens'

#### Beschrijving

Geeft aan of in de inhoud van het informatieobject persoonsgegevens aanwezig zijn die niet openbaar gemaakt mogen worden.

#### Rationale voor toevoeging

- Er was behoefte aan een manier om aan te geven dat de inhoud van een informatieobject persoonsgegevens omvat die niet openbaar gemaakt mogen worden.

#### Toegestane waarden

Waarde | Beschrijving
-- | --
null |
true | In het informatieobject zijn persoonsgegevens aanwezig die niet openbaar gemaakt mogen worden.
false | In het informatieobject zijn geen persoonsgegevens die niet openbaar gemaakt mogen worden.

#### Toelichting

In deze indicatie wordt expliciet verwezen naar "persoonsgegevens die niet openbaar gemaakt mogen worden". Dit betekent niet dat voor ieder informatieobject waarin persoonsgegvens aanwezig zijn de waarde 'ja' gekozen moet worden. Het kan immers gerechtvaardigd zijn persoonsgegevens wél openbaar te maken.

__Merk op dat de áfwezigheid van persoonsgegevens niet kan worden gezien als vrijbrief voor openbare publicatie. Er kunnen immers andere beperkingsgronden (vertrouwelijk gedeelde bedrijfs- en fabricagegegevens, schending van belangen gediend met opsporing en vervolging van strafbare feiten, ...) of auteursrechtelijke beperkingen gelden.__

## Wat vervalt (op termijn)?

Belanghebbenden gaven aan bovenstaande wijziging bij voorkeur verwerkt te zien in een _minor_ release van de Documenten API. Dit heeft als postief gevolg dat de overgang naar nieuwe property's en waarden niet in één 'big bang' hoeft te gebeuren. Maar het betekent dat het 'oude' niet zonder meer uit de specificatie mag verdwijnen, maar dat sprake moet zijn van een overgangsperiode waarin oud en nieuw naast elkaar kunnen bestaan. Dit kan worden bereikt door middel van 'deprication'. Met name de property `status` vormt hierbij een uitdaging. Daarvoor geldt immers dat sommige toegestane waarden geheel nieuw zijn, sommige een (door introductie van nieuwe waarden) geactualiseerde betekenis hebben gekregen, terwijl één waarde `gearchiveerd` geheel vervalt. Om aan te geven dat we willen dat 'oude' waarden zo min mogelijk worden gebruikt, zagen we drie mogelijkheden:

1. Het toekennen van het 'depricated'-label aan individuele enum-waarden. Dit is, volgens de OpenAPI-specificaties versie 3.0 die we voor deze standaarden hanteren, [niet mogelijk](https://stackoverflow.com/questions/63963150/with-swagger-2-0-or-even-3-0-is-it-possible-to-mark-an-enum-value-as-deprecat).
2. Het opnemen van een geheel nieuwe property `statusv2` (of iets dergelijks), terwijl aan de bestaande property `status` het 'depricated'-label wordt toegekend. Dit leidt ertoe dat we ofwel tot in lengte van dagen met een lelijke, niet descriptieve propertynaam met daarin een versieaanduiding blijven zitten, ofwel later nog een wijziging moeten doorvoeren om de 'v2'-suffix weer te verwijderen. Om deze reden is hiervoor niet gekozen.
3. Het toevoegen van een nieuwe enum met daarin nieuwe toegestane statuswaarden onder de naam `StatusEnumV2` en het toekennen van het 'depricated'-label aan de bestaande enum `StatusEnum`. Hoewel hierbij dezelfde suffix-problematiek speelt als bij 2. hierboven, hebben we geoordeeld dat dit in de naam van een enum minder erg is dan in de naam van een property. Voor deze oplossing is derhalve gekozen.

In de volgende _major_ release van de Documenten API kan de enum `StatusEnum` geheel komen te vervallen.

## Aandachtspunten bij deze consultatie

### Interacties tussen API-consumers en -providers

Depricaten van de statuswaarden die in versies < 1.5.0 van de Documenten API werden gehanteerd heeft een aantal consequenties:

- API-consumers kunnen (of ze nu kennis hebben van in 1.5.0 doorgevoerde wijzigingen of niet) naast de nieuwe ook de in eerdere versies gehanteerde statuswaarden registeren.
- API-consumers zonder kennis van versies > 1.4.3 kunnen mogelijk in 1.5.0 toegevoegde statuswaarden niet interpreteren.
- API-consumers met kennis van versies > 1.4.3 verwachten kennis over de archiefstatus te kunnen halen uit de waarde van de property `archiefstatus`, terwijl die kennis ook in de vorm van de deprecated waarde `gearchiveerd` bij `status` geregistreerd kan zijn.

Op basis hiervan verwachten we van API-providers het volgende gedrag:

- bij `status` wordt, depricated of niet, iedere geldige waarde (`in_bewerking`, `concept`, `definitief`, `ter_vaststelling`, `vastgesteld` of `gearchiveerd`) die een consumer aanbiedt geregistreerd.
- aan consumers die API-versies > 1.4.3 bevragen wordt de geregistreerde statuswaarde, depricated of niet.
- aan consumers die API-versies < 1.5.0 bevragen worden alleen statuswaarden geleverd die in die API-versies geldig waren (`in_bewerking`, `ter_vaststelling`, `definitief` of `gearchiveerd`). Als een andere waarde is geregistreerd wordt de statuswaarde `null` geleverd.
- bij registratie van statuswaarde `gearchiveerd`, wordt door de provider automatisch óók de archiefstatus `onveranderlijk` of eventueel `duurzaam_toegankelijk` geregistreerd. Zo worden consumers bediend die op basis van 1.5-specificaties daar de kennis over de archiefstatus verwachten.

Van API-consumers verwachten we dat ze zo snel mogelijk overstappen van bestaande naar nieuwe statuswaarden, en dat zij archiefstatussen, geldigheidsinformatie en informmatie over aanwezigheid van persoonsgegevens (laatste twee voor zover relevant) in de bijbehorende nieuwe property's gaan registeren.

**We horen graag van belanghebbenden of zij zich kunnen vinden in de keuze bovenstaande wijzigingen in een _minor_ versie door te voeren en of zij opmerkingen hebben over het gedrag dat we van met name API-providers verwachten.**

### Gelijke waarde, andere semantiek

Een ander aandachtspunt is dat statuswaarden `in_bewerking`, `ter_vaststelling` en `definitief` straks in twee enums voorkomen, waarbij de betekenis van dezelfde waarde subtiel kan verschillen. Voor API-providers is echter niet altijd te achterhalen op basis van welke enum, en dus met welke betekenis een API-consumer een statuswaarde registreert. Vanwege het zeer subtiele karakter van de verschillen verwachten we hierdoor in de praktijk echter geen grote problemen.

**We horen graag van belanghebbenden of zij deze verwachting delen.**

De tabel hieronder illustreert hoe 'oude' statuswaarden zich vertalen naar nieuwe (archief)statuswaarden.

 'oude' waarde | te mappen naar of interpreteren als | te mappen naar of interpreteren als
--|--|--                                        
_status (1.4.3)_ | _status (1.5.0)_   | _archiefstatus (1.5.0)_ 
`in_bewerking` | `in_bewerking (veilig) |
 | `concept` (onder voorwaarde van voldoende bestendigheid) |
`ter_vaststelling` | `ter_vaststelling` (veilig) |
`definitief` | `definitief` (veilig) |
 | `vastgesteld` (onder voorwaarde van bekrachtiging in besluitvormingsproces) |
`gearchiveerd` | | `onveranderlijk` (veilig)
 | | `duurzaam_toegankelijk `(onder voorwaarde dat wordt voldaan aan eisen voor duurzame toegankelijkheid)

### Derde `archiefstatus` nodig of gewenst?

De keuze voor [drie mogelijke waarden bij archiefstatus](#property-archiefstatus) is hierboven gemotiveerd. Waar de waarden `muteerbaar` en `onveranderlijk`, wat [minimaal nodig is](#gedragsregel-zetten-zaakarchiefstatus-zrc-022) voor afsluiten van een zaak, noodzakelijk zijn om met zaken te kunnen werken, geldt dat voor `duurzaam_toegankelijk` niet. We zien echter twee redenen om deze waarde toch op te nemen:

1. Informatieobjecten met status `gearchiveerd` waarvoor daadwerkelijk de duurzame toegankelijkheid of opslag geregeld is, kunnen zonder deze waarde niet van een `archiefstatus` worden voorzien die uitdrukt dat het informatieobject voldoet aan de eisen van duurzame toegankelijkheid. Omzetting zou met in deze gevallen met andere woorden verlies van kennis en bekenis tot gevolg hebben;
2. Op basis van `onveranderlijke` informatieobjecten kan een 'werklijst' voor informatiebeheerders worden gecreëerd. Het uitgevoerde werk levert dan een `duurzaam_toegankelijk` informatieobject op.

**Over nut en noodzaak van het opnemen van archiefstatus `duurzaam_toegankelijk` was tijdens het voorbereiden van bovenstaande wijzigingen geen volledige overeenstemming. Belanghebbenden met inzichten die helpen bepalen of we deze waarde moeten opnemen of niet zijn daarom van harte uitgenodigd die inzichten te delen.**