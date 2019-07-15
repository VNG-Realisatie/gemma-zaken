---
title: "Overzicht van Zaakgericht werken"
date: '14-11-2018'
weight: 10
---

*WIP: Overgenomen uit RGBZ 2.0 zodat samenhang helder wordt maar moet worden herschreven*

Centraal bij Zaakgericht werken staat het begrip ZAAK. Een ZAAK is "een
samenhangende hoeveelheid werk met een welgedefinieerde aanleiding en een
welgedefinieerd eindresultaat, waarvan kwaliteit en doorlooptijd bewaakt moet
worden".

De aanleiding bepaalt de omvang van de zaak. Met die zaak wordt een
bedrijfsproces uitgevoerd waarmee beantwoord wordt aan de aanleiding. Als,
gezien de aanleiding, aan de uitvoering van de zaak alleen invulling gegeven
kan worden door de (parallelle) uitvoering van meerdere bedrijfsprocessen, dan
is er sprake van deelzaken. Met elke deelzaak wordt één bedrijfsproces
uitgevoerd. Elke deelzaak is op zich weer een ZAAK. Deze relateren we aan de
'hoofdzaak': de 'samengestelde' ZAAK zoals die geïnitieerd is.

Kenmerken van groepen vergelijkbare zaken leggen we vast met het ZAAKTYPE
conform de [Zaaktypecatalogus][ztc].

Elke zaak heeft 'ergens betrekking op'. Dit modelleren we met de relatie naar
OBJECT via ZAAKOBJECT als het een object van een type uit het RSGB of RGBZ
betreft. Zo niet, dan leggen we dit vast met zaakgegevens. Soms heeft de ene
zaak betrekking op een andere zaak, wat we modelleren met de relatie 'ZAAK
heeft gerelateerde ZAAK'. Denk bijvoorbeeld aan een bezwaar of beroep dat naar
aanleiding van een beschikking wordt ingediend en dat als een separate zaak
wordt afgehandeld. De aard van de relatie tussen zaken leggen we vast met
ZAKENRELATIE. Een ZAAK wordt geïnitieerd door één of meer BETROKKENEn. Een
betrokkene kan een externe persoon of bedrijf zijn: NATUURLIJK PERSOON, NIET
NATUURLIJK PERSOON of VESTIGING. Ook kan het initiatief voor de ZAAK binnen de
zaakbehandelende organisatie(s) liggen: ORGANISATORISCHE EENHEID of MEDEWERKER.
De belangrijkste ROL van beide laatstgenoemde objecttypen is evenwel het
behandelen van zaken. Met de relatie van ORGANISATORISCHE EENHEID naar
VESTIGING VAN ZAAKBEHANDELENDE ORGANISATIE geven we aan op welke locatie de
ORGANISATORISCHE EENHEID van de zaakbehandelende organisatie haar activiteiten
uitoefent.

Het initiëren van zaken is één van de ROLlen van een BETROKKENE. In het
algemeen betreft ROL de taken, rechten en/of verplichtingen die een specifieke
BETROKKENE heeft ten aanzien van een specifieke ZAAK.

Een zaak doorloopt een aantal STATUSsen. Een STATUS geeft aan in welke toestand
een zaak zich bevindt. De STATUS maakt het mogelijk de voortgang van de zaak op
hoofdlijnen te volgen. Wat de hoofdlijnen zijn wordt in belangrijke mate
bepaald vanuit de belangen van de initiator van de zaak. Deze is veelal
eïnteresseerd in mijlpalen, niet in de diverse stappen die de behandelende
organisatie(s) moet zetten om de zaak af te handelen. Daarnaast kan de STATUS
gebruikt worden voor het genereren van management informatie.

Een zaak heeft in de loop van de tijd meerdere statussen: de achtereenvolgens
bereikte mijlpalen. De STATUS is niet bedoeld om de behandeling van de zaak te
plannen. Deze planning volgt uit de STATUSTYPEn bij de ZAAK. Het STATUSTYPE is
ontleend aan het ImZTC2. Een STATUS wordt altijd gezet door een BETROKKENE in
zijn of haar ROL bij de ZAAK. INFORMATIEOBJECTen ('documenten') die relevant
zijn voor het bereiken van een STATUS of voor de communicatie over die STATUS,
kunnen aan die STATUS gerelateerd worden. Gedurende de uitvoering van een zaak
kan er sprake zijn van contacten met de initiator en/of andere betrokkenen over
die zaak. Relevante informatie over dergelijke contacten modelleren we met
KLANTCONTACT en haar relaties naar ZAAK, BETROKKENE en INFORMATIEOBJECT.

De resultaten van de behandeling van de zaak worden bij de zaak vastgelegd.
Resultaten zijn bijvoorbeeld dat de aanvraag is toegekend, dat de zaak is
ingetrokken door de aanvrager of dat de zaak niet ontvankelijk is verklaard.
Een zaakresultaat is veelal bepalend voor het 'archiefregime' van het
zaakdossier: hoe lang te bewaren? Ook dit zijn kenmerken van ZAAK. De
daadwerkelijke waarde wordt ontleend aan de specificatie van het desbetreffende
zaaktype conform de [Zaaktypecatalogus][ztc]. In
uitzonderingsgevallen kan een specifiek informatieobject in een zaakdossier een
ander archiefregime krijgen, op basis van de specificaties van het zaaktype.
Een zaak leidt in veel gevallen tot één of meer BESLUITen. Kenmerken van
groepen vergelijkbare BESLUITen leggen we vast met het BESLUITTYPE conform de
[Zaaktypecatalogus][ztc]. Een besluit wordt veelal schriftelijk vastgelegd maar
dit is niet noodzakelijk. Vandaar de optionele relatie naar INFORMATIEOBJECT.

Meerdere informatieobjecten ('documenten') kunnen gedurende de behandeling
relevant zijn voor een zaak. Omgekeerd kan een informatieobject relevant zijn
voor meerdere zaken. De relatie tussen ZAAK en INFORMATIEOBJECT modelleren we
dan ook via ZAAK-INFORMATIEOBJECT. De ontvanger of geadresseerde van een
informatieobject hebben we opgenomen in het model door middel van de relatie
VERZENDING tussen INFORMATIEOBJECT en BETROKKENE. In veel gevallen zal een
ontvangen of gecreëerd informatieobject ook daadwerkelijk als één (fysiek)
informatieobject beschouwd worden: het ENKELVOUDIG INFORMATIEOBJECT. Evenwel,
een informatieobject dat door bijvoorbeeld de initiator van een zaak als één
informatieobject wordt beschouwd, kan feitelijk uit meerdere informatieobject
(veelal bestanden) bestaan, bijvoorbeeld omdat het formaat (.pdf, .odt.
CAD-file e.d.) verschilt of omdat de zaakbehandelende organisatie hoofdrapport
en bijlagen ieder apart als ENKELVOUDIG INFORMATIEOBJECT wil beschouwen. Een
dergelijke groep bij elkaar behorende informatieobjecten beschouwen we tevens
als een informatieobject en modelleren we als SAMENGESTELD INFORMATIEOBJECT.
Het objecttype INFORMATIEOBJECT is aldus telkens of een ENKELVOUDIG
INFORMATIEOBJECT of een SAMENGESTELD INFORMATIEOBJECT waarbij de laatstgenoemde
bestaat uit twee of meer ENKELVOUDIGe INFORMATIEOBJECTen.

Kenmerken van groepen vergelijkbare INFORMATIEOBJECTen leggen we vast met het
INFORMATIEOBJECTTYPE conform de [Zaaktypecatalogus][ztc].

[ztc]: /standaard/catalogi/index
