---
title: "Demo Sprint 5"
date: "29-10-2018"
---

Amsterdam, 25 oktober 2018

## Presentatie

- Opening (@MarcelMoerman)
- Inleiding (@TCIMEddy ter vervanging van @ehotting)
- Techniek sprint 5 (@sergei-maertens & @joeribekker)
- Aanpassingen RGBZ (@ArjanKloosterboer)

Slides:

- [ZDS2 Demo Spint 5.pdf](/community/bestanden/zds2-demo-sprint-5.pdf)
- [Opsplitsen RGBZ](/community/bestanden/opsplitsen-rgbz.pdf)

## Feedback

### Wat is de rol en scope van mapper service? Moet dit gestandaardiseerd worden?

Organisaties (gemeentes) hebben intern een authenticatie/autorisatiessyteem- en/of model. De APIs
zijn generiek en hebben hier geen kennis van, omdat het kan (en waarschijnlijk zal) verschillen per
organisaties.

De rol van de mapper/mapper service is het vertalen van interne rollen naar de scopes zoals die bij
de API bekend zijn, om de uitwisselbaarheid te garanderen.

Herbruikbare oplossingen (bijvoorbeeld intappen op Active Directory) zouden kunnen ontwikkeld
worden. Standaardisatie zou kunnen flexibilteit bij organisaties wegnemen en dingen opleggen aan de
gemeentes die niet de moeite waard geacht worden.

### Hoe staat het met authenticatie en autorisatie?

Hier zijn verkennende gesprekken over geweest met de techneuten van de DSO en NLx. De
oplossingsrichting is voorlopig om met [scopes](https://geonovum.github.io/KP-APIs-OAuthNL/#scopes)
te gaan werken, die wellicht via een [JWT](https://jwt.io/introduction/) worden doorgegeven. OAuth
biedt veel meer dan nodig is voor deze APIs en is daarom ter overweging.

### Hoe gaan jullie om met externe gebruikers m.b.t. authenticatie en autorisatie?

Dat wordt nog onderzocht maar we nemen deze vraag mee in het uiteindelijke verhaal.

### De URL werkt niet bij update!?

Na afloop van de presentatie bleek het wel te werken, maar deed de leverancier iets fout.

### Wat is er concreet op 20 december en wat is het vervolg? Stip op de horizon?

todo

### Wordt Docker veel gebruikt binnen gemeenten?

Het korte antwoord is nee. Maar dat geldt waarschijnlijk ook voor REST APIs.

Hoewel alle componenten nu in Docker gewrapped worden, is het geen verplichting of onderdeel van de
standaard om componenten in een Docker aan te bieden. Wij gebruiken Docker omdat het makkelijk uit
te rollen is, en relatief eenvoudig op een eigen server of ontwikkelomgeving op te zetten.

### Wat is de huidige toepasbaarheid van de API's?

Dit is een erg brede vraag, en op basis van de userstories kunnen we MOR, straatartiest-proces en
AVG-inzakeverzoeken beginnen behandelen.

Dit alles steunt op vrij low-level APIs. Typische (combinaties) van calls zullen komen bovendrijven,
en mogelijks wordt daar een convience API op gebouwd of wordt dit in clients opgenomen.

Grofweg is de status op dit moment:

- Je kan zaken en informatieobjecten aanmaken
- Je kan besluiten, statussen, zaakobjecten, betrokkenen en klantcontacten bij zaken aanmaken.
- Al deze gegevens kan je ook uitlezen
- Je kan een Catalogi API inrichten om bovenstaande uit te kunnen voeren.

### Wat was de concrete doelstelling(en) aan het begin van het traject?

Om Zaakgericht Werken een stap verder te brengen worden Zaak- en Documentservices (ZDS) versie 2
ontwikkeld. Hierbij wordt een andere vorm van standaardisatie toegepast. Op basis van relevante
informatiemodellen (RGBZ 2.0 en ImZTC 2.2) wordt met zowel publieke als private partijen in een
agile proces vorm gegeven aan RESTful API’s die concreet invulling geven aan de gewenste standaard.
De standaard wordt tegelijk met een referentie-implementatie ontwikkeld om de implementeerbaarheid
aan te tonen, en als referentie te dienen voor latere implementaties.

### Kunnen jullie agenda meesturen in de uitnodiging?

Op de website waar de bijeenkomsten worden aangekondigd en in de definitieve bevestiging wordt een
link naar de activiteiten van de huidige sprint opgenomen:
[sprintbord](https://github.com/VNG-Realisatie/gemma-zaken/projects/3)

### Wat verstaan jullie onder backward compatible?

todo

### Hoe ziet de implementatie eruit?

todo
