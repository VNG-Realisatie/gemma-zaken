# RDAM – Samenloop

In dit hoofdstuk wordt een globale architectuurschets gegeven voor de User Stories in het kader van Samenloopdetectie. Het gaat om de volgende User Stories.

## User stories

* [User story #64](https://github.com/VNG-Realisatie/gemma-zaken/issues/64): Als gemeentemedewerker wil ik een lijst opvragen met aangevraagde en toegekende vergunningen die betrekking hebben op BGT-objecten binnen de wijk (postcodegebied) waarin ik nu loop
* [User story #65](https://github.com/VNG-Realisatie/gemma-zaken/issues/65): als gemeentemedewerker wil ik inzage in alle zaken die betrekking hebben op de persoon/aanvrager behorend bij een zaak die ik in behandeling heb

## Toelichting user stories

Het gaat hier om een aantal Rotterdamse User Stories waarin, bezien vanuit het sociale domein en het fysieke domein, inzicht nodig is in de aanpalende trajecten (zaken) welke elders binnen de gemeente worden uitgevoerd.

### 'Samenloopdetectie':

* Medewerkers – werkend vanuit een taakapplicatie of app - moeten weten of een burger/bedrijf/object al betrokken is in een traject, dat aan een onderwerp gerelateerd is, maar waarvan de dienstverlening niet via de betreffende taakapplicatie loopt.
* Dit voor zover de classificatie en doelbinding dit toestaat.
* Met een onderscheid, voor daartoe geautoriseerde medewerkers, in:
    * ‘dat’ informatie = een lijst met zaaknummers en behandelaars
    * ‘wat’ informatie = na doorklikken op een zaaknummer, inzage krijgen in status en zaakdocumenten.

### Voorbeeld Zorg traject

In een aanvraag voor zorg is het nodig om te weten of er al trajecten lopen voor schuldhulp of leerlingen verzuim (op de persoon en binnen de gezinssituatie). Vanwege privacywetgeving/-beleid mag er geen inhoudelijke informatie (de 'wat-informatie') opgevraagd worden, maar alleen het bestaan ervan (de 'dat-informatie') aangevuld met contactgegevens van de behandelaar/casusregisseur.

### Voorbeeld Fysiek traject

Inspecteurs – bijvoorbeeld t.a.v. bouwvergunningen – lopen door wijken en over bouwterreinen. De inspecteur heeft daarbij een volledig overzicht nodig - op basis van zijn huidige plaats of op basis van in te geven coördinaten van een gebied/wijk/regio – van de verstrekte vergunningen, de status van aangevraagde vergunningen, de behandelaar, de achterliggende tekeningen, etc. Dit om te zien waar een inspectie kan plaatsvinden, of om ter plaatse de betreffende stukken te kunnen inzien.

* De medewerker bekijkt dit rechtstreeks in de taakapplicatie of in een app/site.
* Apps, applicaties en websites laten verzamelingen zien van afgesloten en lopende trajecten.

Hieronder een voorbeeld op een 3d kaart (de pop up laat nu andere gegevens zien).

![3drotterdam.png](./bestanden/rotterdam/3drotterdam.png?raw=true)

* Cliënten hebben interactie met gemeente via portalen (ruim te interpreteren: mijnrotterdam, apps, websites, e.d.). Dit geldt ook voor het bekijken en muteren van zaakinformatie (en documenten).

* Als bron wordt in dit agile traject gebruik gemaakt van de e-Suite.
In realiteit is er sprake van een ‘zs-dms complex’ ipv een enkelvoudige bron. In het verleden zijn meerdere, op zichzelf staande, ZRC’s en DRC’s ontstaan. Soms in de taakapplicaties zelf. Beoogd wordt uiteindelijk alle zaken (zaakinformatie en zaakdossiers) onder te brengen binnen een enkelvoudige bron.

![datenwat](./bestanden/rotterdam/datenwat.png?raw=true)

![informatieburgers](./bestanden/rotterdam/informatieburgers.png?raw=true)

* Soms heeft de e-Suite zelf ook ‘de rol van taakapplicatie’ voor de afhandeling van processen die volledig in de e-Suite zijn vormgegeven (zaakafhandelcomponent).

## Architectuurschets

![architectuurschetsrotterdam](./bestanden/rotterdam/architectuurschetsrotterdam.png?raw=true)

Professionals (intern en van ketenpartners) en cliënten (burgers en bedrijven) maken gebruik van de samenloopfunctionaliteit geleverd door een specifieke app, applicatie of website. Omdat samenloop gaat over vanuit doelbinding relevante zaken wordt in de toepassing (app, applicatie of website) zelf invulling gegeven aan ‘relevante’. De kennis die nodig is om – bijvoorbeeld - te bepalen wie onderdeel uitmaakt van het gezin, of welke objecten in een gebied bij elkaar horen, bevindt zich dus aan de zijde van de toepassing. De toepassing geeft betreffende kennis mee in de zoekvraag richting de ZDS 2.0 interfaces, welke gerealiseerd worden door de ZRC, DRC en ZTC.

## Beknopte Procesbeschrijving

1.	Client of professional voert het zoekgegeven in een toepassing in.
2.	De toepassing geeft de ‘dat-informatie’ (= een lijst met zaaknummers en behandelaars) terug.
3.	In geval de autorisatie (bepaald op zaaktype adhv doelbinding, classificatie en toegepast voor rol/functie) dit toestaat, wordt, na doorklikken op een zaaknummer, inzage verkregen in de ‘wat-informatie’ (detailinformatie en zaakdocumenten (indien vertrouwelijkheidsbepaling dit niet beperkt)).

## Generieke architectuurschets (GEMMA-referentiecomponenten)

Architectuurschetsen zijn reeds in termen van GEMMA 2 referentiecomponenten.

## Benodigde APIs per user story

## User story	API	Functionaliteit

