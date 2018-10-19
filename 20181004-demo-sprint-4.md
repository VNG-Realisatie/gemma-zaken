# Demo Sprint 4

Den Haag, 4 oktober 2018

## Presentatie

Slides: [ZDS2 Demo Spint 4.pdf](/community/bestanden/zds2-demo-sprint-4.pdf)

## Feedback

Alle reacties en vragen tijdens de demo zijn hieronder opgenomen. Waar nodig zijn issues aangemaakt. Dit zijn de antwoorden van het scrum team. Reacties zijn uiteraard van harte welkom.

#### Waarom moeten bij het aanmaken van een ObjectInformatieobject (zaakdocument) twee calls gedaan worden naar de DRC (Te weten eentje voor het aanmaken van een Informatieobject en eentje voor het maken van het relatieobject ObjectInformatieobject (het oude zaakdocument)).
Dit komt omdat in het relatieobject de verwijzing naar zowel de zaak als het informatieobject opgenomen moet worden dus de moeten eerst bestaan. NB Mogelijk zou dit in één gecombineerde "convenience method" opgenomen kunnen worden.

#### Wanneer een document bij een besluit hoort, moet dit dan zowel aan de zaak als het besluit gekoppeld worden? Deze opzet betekent dat de componenten (ZRC en DRC) elkaar moeten kunnen bereiken? 
Dat klopt inderdaad. Mogelijk spelen hier ook nog authenticatie en autorsatie issues mee, dit zullen we moeten bekijken. Autorisatie en Authenticatie staat voor de komende sprint (5) op het programma.

#### Moet deze invulling extra eisen stellen aan het compliant zijn?
Dat klopt inderdaad, waar voorheen compliancy werd vastgesteld op berichtuitwisseling worden nu ook eisen gesteld aan de architectuur en hoe de berichten verwerkt worden.Dit is een bekend probleem met microservices wat opgelost kan worden met NLX. Theo Peters (VNG) concludeert dat een applicatie niet alleen moet voldoen aan de API maar ook aan gebruik van NLX.

#### Conflicteert het dubbel vastleggen van de relatie niet met het CG principe van eenmalige opslag?
Nee, het informatieobject wordt nog steeds maar eenmaal opgelagen. Alleen de relatie met andere objecten wordt meermalen opgeslagen, dit zjn echter verwijzingen.

#### Hoe borgen we dat relaties intact blijven? Bijvoorbeeld bij het migreren van applicaties/databases? Of het samenvoegen van meerdere DRC's tot één groot DRC of juist het opslitsen van een groot DRC in meerdere kleinere?
todo

#### Is de DRC is de master en kan daar altjd de juiste verwijzing opgezocht worden?
todo

#### Wanneer je een relatie vastlegt, valideer je meteen of relaties nog kloppen?
totdo

#### Hamvraag is er een andere manier om dit op te lossen en is die beter?
todo

#### Feedback
Ivo van Zitteren (Breda) doet de suggestie om middels autorisatie/authenticatie te borgen dat gegevens schoon blijven.
Jeffrey Gortmaker (VNG) geeft aan dat er grofweg 3 oplossingen zijn en verzoekt het publiek hier over na te denken en hier zo snel mogelijk op te reageren.

#### Als ik wil reageren op vraag van Jeffrey, hoe/waaar doe ik dat? Welk issue is dat?
todo

### Kan het patroon ook zonder synchronisatie gebruikt kan worden? 
Dit wordt bevestigd en het is zaak een sweetspot te vinden tussen alles afdekken en een risico dat dingen uit pas gaan lopen.

#### De logica om te valideren of zaaktype klopt ligt nu bij de ZRC, waarom ligt die niet bij ZTC?
Het is de verantwoordelijkheid van ZRC om het gebruikte zaaktype te valideren. Andy Verberne (ATOS) is het er niet helemaal mee eens. 

#### Feedback/opmerkingen
(Eelco Hotting) In de toekomst gaan we waarschijnlijk gebruik maken van verschillende ZTC's, bijvoorbeeld per domein of proces. Theo Peters (VNG) vult aan: Bijvoorbeeld in het ruimtelijk domein is het interessant om één gezamelijke, gedeelde ZRC en ZTC te gebruiken. In het Sociaal domein willen we dat misschien liever lokaal houden.
(principe CG om technisch mogelijk te maken dat dit kan
 
#### Deze manier van werken vereist business logca, niet meer alleen opslaan zoals nu in de standaard staat.
Dit klopt inderdaad.Door deze business logica te beschrijven wordt het gemakkelijker bovenop deze standaarden te ontwikkelen. Punt van aandacht is wel dat er gradaties zijn van wat een gemeente verstaat onder "zaakgericht werken". Omdat er nooit goed opgeschreven is wat er wel/niet onder verstaan wordt is een doelstelling om deze onduidelijkheid weg te nemen. In ieder geval moet de kern vastgelegd worden waar we het over eens zijn waarbij het belangrijk is de consistentie regels op te nemen.

#### Hoe worden designkeuzes bepaald en vastgelegd?
Dit zijn we nog aan het ontdekken. Weliswaar zit het in de mens om hiervoor een procedure voor te bedenken ("zo gaan we het doen") maar het belangrijkste is elkaar op te zoeken en te overleggen waar nodig is.

#### Wordt een Besluit niet meer gezien als een subtype van een Informatieobject?
Een Besluit is een zelfstandig concept, een Informatieobject is een manier om het Besluit kenbaar te maken maar een ander concept.

#### Zijn bijvoorbeeld informatiemanagers geïnteresseerd in het soort documentatie zoals die nu gemaakt wordt?
Antwoord: Dat is precies de vraag die wij proberen te (laten) beantwoorden. In de werkgroep zitten veelal techneuten en inhoudsdeskundigen waardoor het lastig in te schatten is of documentatie diep genoeg of juist niet te diep gaat en of niet teveel kennis verondersteld wordt aanwezig te zijn. De documentatie die er nu is wordt gegenereerd uit de OAS en is voor niet-technische mensen begrijpelijker dan de OAS.

#### Documenten heten inmiddels informatieobjecten, waarom heet de DRC nog steeds Documentregistratiecomponent?
todo
