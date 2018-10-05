# RDAM – Samenloop in het Sociaal Domein

Hieronder wordt een globale architectuurschets gegeven voor een user story in het kader van samenloopdetectie in het Sociaal Domein. 

## User story
* [User story #65](https://github.com/VNG-Realisatie/gemma-zaken/issues/65): als gemeentemedewerker wil ik inzage in alle zaken die betrekking hebben op de persoon/aanvrager behorend bij een zaak die ik in behandeling heb, zodat ik alle relevante informatie heb over de sociale omgeving, zijnde het gezin en betrokken personen.

## Toelichting user story

In de behandeling van een zorgcasus van een client is het nodig om te weten wat in het verleden aan zorgtrajecten zijn doorlopen en welke onderhanden zijn. Denk bijvoorbeeld aan schuldhulpverlening, leerlingen verzuim, uitkeringverstrekking, e.d. Niet alleen trajecten van de client zelf, maar ook binnen de gezinssituatie. Is er bijvoorbeeld sprake van een voogd of bewindvoering. Met een integraal overzicht van alle bestaande raakvlakken met de gemeente, kan de dienstverlening beter op de situatie worden afgestemd. Onderling kunnen afdelingen beter samenwerken en heeft de client een eenduidig beeld vanuit de gemeente.

Het gaat hier dus om inzicht te verkrijgen in alle (aanpalende) trajecten (zaken), rondom een, in het Sociaal domein, in behandeling zijnde casus van een persoon/gezin. Daarbij is het gewenst de zaken te zien van alle in en bij het gezin betrokken personen ongeacht de betreffende afdelingen en taakapplicaties. De medewerker werkt aan de casus in een eigen taakapplicatie (de zaakafhandelcomponent; in deze userstory Gidso (Topicus) en Edison) en krijgt de aanpalende zaakinformatie te zien binnen de eigen zaakafhandelcomponent of een aanvullende user interface. 

* Dit betreft zowel afgesloten als in behandeling zijnde zaakinformatie. 
* Dit voor zover de doelbinding en classificatie dit toestaat.
* Met een onderscheid, voor daartoe geautoriseerde medewerkers, in:
    * ‘dat’ zaakinformatie = een lijst met zaaknummers en behandelaars
    * ‘wat’ zaakinformatie = na doorklikken op een zaaknummer, inzage krijgen in status en zaakdocumenten.
* Binnen de operational datastore van de zaakafhandelcomponent is bekend welke personen onderdeel uitmaken van of betrokken zijn bij het gezin.
* In de zaakafhandelcomponent zal een nadere aanduiding plaatsvinden naar relevante zaaktypen en organisatieonderdelen (waarbij bepaald moet worden hoe de verantwoordelijkheid van filtering is verdeeld tussen ZAC, API, component en gegevenslaag). 
* Op lange termijn zou het fijn zijn als deze aanvullende zaakinformatie niet alleen van binnen de grenzen van de enkelvoudige gemeente vandaan komt, maar ook vanuit andere organisaties (andere gemeenten, zorgverleners, provincie, etc.).  

Vanwege privacywetgeving/-beleid mag er geen inhoudelijke informatie (de 'wat-informatie') zonder doelbinding opgevraagd worden, maar alleen het bestaan ervan (de 'dat-informatie') aangevuld met contactgegevens van de behandelaar/casusregisseur. <juridische check moet nog gemaakt>

* Als primaire bron voor zaken (zaakinformatie en zaakdossiers) wordt binnen Rotterdam op dit moment gebruik gemaakt van de e-Suite (DIMPACT). In realiteit is er sprake van een ‘zs-dms complex’ ipv een enkelvoudige bron. Er zijn in het verleden meerdere, op zichzelf staande, ZRC’s en DRC’s ontstaan. Voor deze userstory is beoogd de e-Suite te gebruiken. 
* De e-Suite kan zelf ook ‘de rol van taakapplicatie’ (zaakafhandelcomponent) hebben, voor processen die volledig in de e-Suite zijn vormgegeven. In deze user story is daar geen sprake van. Er is een afzonderlijke zaakafhandelcomponent (Gidso en Edison). 

![datenwat](./bestanden/rotterdam/datenwat.png?raw=true)

## Architectuurschets

![architectuurschetsrotterdam](./bestanden/rotterdam/architectuurschetsrotterdam.png?raw=true)

Toelichting architectuurschets: Cliënten (burgers) maken gebruik van dienstverlening, hier Zorg genoemd. De dienstverlening wordt geleverd door Professionals (intern medewerkers en ketenpartners) vanuit het sociaal domein. Voor het bepalen van de juiste dienstverlening wordt samenloopdetectie gebruikt. Hiervoor wordt samenloopfunctionaliteit geleverd vanuit een app (moet nog geeraliseerd) of de taakapplicaties Gidso en Edison. Deze taakapplicaties doen hiervoor een beroep op ZDS 2.0 functionaliteit door de api interfaces aan te roepen. De ZDS2.0 api's maken onderliggend gebruik van de ZDS 2.0 referentie applicatiecomponenten, welke binnen Rotterdam ingevuld worden vanuit de e-Suite applicatiecomponent.

Omdat samenloop gaat over vanuit doelbinding relevante zaken wordt in de toepassing (app, Gidso en Edison) zelf invulling gegeven aan ‘relevante’. De kennis die nodig is om – bijvoorbeeld - te bepalen wie onderdeel uitmaakt van het gezin, of welke zaaktypen interessant zijn, bevindt zich dus aan de zijde van de toepassing. De toepassing geeft betreffende kennis mee in de zoekvraag richting de ZDS 2.0 interfaces.

## Beknopte Procesbeschrijving

1.	Professional voert het zoekgegeven in app, Gidso of Edison in.
2.	De toepassing geeft de ‘dat-informatie’ (= een lijst met zaaknummers en behandelaars) terug.
3.	In geval de autorisatie (bepaald op zaaktype adhv doelbinding, classificatie en toegepast voor rol/functie) dit toestaat, wordt, na doorklikken op een zaaknummer, inzage verkregen in de ‘wat-informatie’ (detailinformatie en zaakdocumenten (indien vertrouwelijkheidsbepaling dit niet beperkt)).

## Generieke architectuurschets (GEMMA-referentiecomponenten)

Architectuurschetsen zijn reeds in termen van GEMMA 2 referentiecomponenten.
