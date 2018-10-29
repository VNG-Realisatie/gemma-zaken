# Demo Sprint 4

Den Haag, 4 oktober 2018

## Presentatie

- Opening (@ehotting)
- Techniek sprint 4 (@sergei-maertens)

Slides: [ZDS2 Demo Spint 4.pdf](/community/bestanden/zds2-demo-sprint-4.pdf)

## Feedback

Alle reacties en vragen tijdens de demo zijn hieronder opgenomen. Waar nodig zijn issues aangemaakt. Dit zijn de antwoorden van het scrum team. Reacties zijn uiteraard van harte welkom.

#### Waarom moeten bij het aanmaken van een ObjectInformatieobject (zaakdocument) twee calls gedaan worden naar de DRC (Te weten eentje voor het aanmaken van een Informatieobject en eentje voor het maken van het relatieobject ObjectInformatieobject (het oude zaakdocument)).

Dit komt omdat in het relatieobject de verwijzing naar zowel de zaak als het informatieobject opgenomen moet worden en dus moeten deze eerst bestaan. Je hebt dus een call nodig om het
informatieobject te registreren, en vervolgens een call om het te relateren aan de zaak.

NB: Mogelijk zou dit in één gecombineerde "convenience method" opgenomen kunnen worden.

#### Wanneer een document bij een besluit hoort, moet dit dan zowel aan de zaak als het besluit gekoppeld worden? Deze opzet betekent dat de componenten (ZRC en DRC) elkaar moeten kunnen bereiken?

Dat klopt inderdaad. Mogelijk spelen hier ook nog authenticatie en autorisatie-uitdagingen mee, dit zullen we moeten bekijken. Autorisatie en Authenticatie staat voor de komende sprint (5) op het programma.

#### Moet deze invulling extra eisen stellen aan het compliant zijn?

Dat klopt inderdaad, waar voorheen compliancy werd vastgesteld op berichtuitwisseling worden nu ook eisen gesteld aan de architectuur en hoe de berichten verwerkt worden. Dit is een bekend probleem met microservices wat opgelost kan worden met NLX. Theo Peters (VNG) concludeert dat een applicatie niet alleen moet voldoen aan de API maar ook aan gebruik van NLX.

#### Conflicteert het dubbel vastleggen van de relatie niet met het CG principe van eenmalige opslag?

Nee, het informatieobject wordt nog steeds maar eenmaal opgelagen. Alleen de relatie met andere objecten wordt meermalen opgeslagen, dit zjn echter verwijzingen.

#### Hoe borgen we dat relaties intact blijven? Bijvoorbeeld bij het migreren van applicaties/databases? Of het samenvoegen van meerdere DRC's tot één groot DRC of juist het opslitsen van een groot DRC in meerdere kleinere?

Door het accepteren van eventual-consistency beseffen we ook dat dit door verschillende
factoren uit elkaar kan gaan lopen. We bedachten toen ook dat het technisch mogelijk
is om periodieke, automatische checks te laten draaien die consistentie controleren
en zelfs kunnen oplossen.

#### Is de DRC is de master en kan daar altjd de juiste verwijzing opgezocht worden?

Ja, echter is spreken van _de_ DRC misleidend. Er kunnen meerdere DRCs staan,
dus je moet dan wel weten in welke DRC je de verwijzing moet opzoeken.

#### Wanneer je een relatie vastlegt, valideer je meteen of relaties nog kloppen?

Nu wordt inderdaad bij het vastleggen van de relatie in diezelfde request-response
cycle de validatie uitgevoerd. Indien het synchroniseren faalt om eender welke
reden, dan resulteert dat bij de client in een validatiefout.

#### Hamvraag: is er een andere manier om dit op te lossen en is die beter?

Dit is het best werkbare wat we nu konden bedenken. We staan open voor suggesties
hoe het eenvoudiger/robuuster/performanter kan.

#### Feedback

Ivo van Zitteren (Breda) doet de suggestie om middels autorisatie/authenticatie te borgen dat gegevens schoon blijven.
Jeffrey Gortmaker (VNG) geeft aan dat er grofweg 3 oplossingen zijn en verzoekt het publiek hier over na te denken en hier zo snel mogelijk op te reageren.

#### Als ik wil reageren op vraag van Jeffrey, hoe/waar doe ik dat? Welk issue is dat?

https://github.com/vng-Realisatie/gemma-zaken/issues/new is de eenvoudigste manier,
dit wordt dan verzameld en gerelateerd met andere mogelijke issues.

### Kan het patroon ook zonder synchronisatie gebruikt worden?

Dit wordt bevestigd en het is zaak een sweetspot te vinden tussen alles afdekken en een risico dat dingen uit pas gaan lopen. In de huidige vorm is het wel de bedoeling dat leveranciers
van DRCs de synchronisatie uitvoeren!

#### De logica om te valideren of zaaktype klopt ligt nu bij de ZRC, waarom ligt die niet bij ZTC?

Het is de verantwoordelijkheid van ZRC om het gebruikte zaaktype te valideren. Andy Verberne (ATOS) is het er niet helemaal mee eens. Dit is nog niet in detail gewouwd, dus we nemen de overwegingen mee om het
in het ZTC toe te passen.

#### Feedback/opmerkingen

(Eelco Hotting) In de toekomst gaan we waarschijnlijk gebruik maken van verschillende ZTC's, bijvoorbeeld per domein of proces. Theo Peters (VNG) vult aan: Bijvoorbeeld in het ruimtelijk domein is het interessant om één gezamelijke, gedeelde ZRC en ZTC te gebruiken. In het Sociaal domein willen we dat misschien liever lokaal houden.
(principe CG om technisch mogelijk te maken dat dit kan)

#### Deze manier van werken vereist business logca, niet meer alleen opslaan zoals nu in de standaard staat.

Dit klopt inderdaad. Door deze business logica te beschrijven wordt het gemakkelijker bovenop deze standaarden te ontwikkelen. Punt van aandacht is wel dat er gradaties zijn van wat een gemeente verstaat onder "zaakgericht werken". Omdat er nooit goed opgeschreven is wat er wel/niet onder verstaan wordt is een doelstelling om deze onduidelijkheid weg te nemen. In ieder geval moet de kern vastgelegd worden waar we het over eens zijn waarbij het belangrijk is de consistentieregels op te nemen.

#### Hoe worden designkeuzes bepaald en vastgelegd?

Dit zijn we nog aan het ontdekken. Weliswaar zit het in de mens om hiervoor een procedure te bedenken ("zo gaan we het doen") maar het belangrijkste is elkaar op te zoeken en te overleggen waar nodig is.

#### Wordt een Besluit niet meer gezien als een subtype van een Informatieobject?

BESLUIT is nooit een subtype van INFORMATIEOBJECT geweest. Een Besluit is een
zelfstandig concept met kenmerken als besluitdatum en werkingsperiode. Een
Informatieobject is een ander concept waarin alleen de inhoud van het
besluit wordt vastgelegd.

#### Zijn bijvoorbeeld informatiemanagers geïnteresseerd in het soort documentatie zoals die nu gemaakt wordt?

Dat is precies de vraag die wij proberen te (laten) beantwoorden. In de werkgroep zitten veelal techneuten en inhoudsdeskundigen waardoor het lastig in te schatten is of documentatie diep genoeg of juist niet te diep gaat en of niet teveel kennis verondersteld wordt aanwezig te zijn. De documentatie die er nu is wordt gegenereerd uit de OAS en is voor niet-technische mensen begrijpelijker dan de OAS.

We werken aan functionele documentatie, onder meer om zicht te krijgen op de behoefte daaraan en invulling daarvan, zie bijvoorbeeld:

* https://github.com/VNG-Realisatie/gemma-zaken/pull/451
* https://github.com/VNG-Realisatie/gemma-zaken/pull/457
* https://github.com/VNG-Realisatie/gemma-zaken/pull/476

De huidige versie hiervan staat op github: https://github.com/VNG-Realisatie/gemma-zaken/tree/master/docs/content/functioneel

#### Documenten heten inmiddels informatieobjecten, waarom heet de DRC nog steeds Documentregistratiecomponent?

Hoofdreden: omdat dit nu de naam is die het best bekend is bij iedereen. Zie
ook [#408](https://github.com/VNG-Realisatie/gemma-zaken/issues/408) waar de
naamgeving als user-story getracked wordt. Dit heeft een lage prio, de functionaliteit
van de APIs is op dit moment veel belangrijker.
