---
title: "ZDS versus ZGW"
date: '11-01-2019'
---

De Zaak- en Documentservices (ZDS) wijken af van de Zaakgericht werken (ZGW)
APIs, maar er is ook overlap. De belangrijkste verschillen en overeenkomsten op
een rij:

1. De ZGW APIs zijn in REST/JSON terwijl ZDS volgens SOAP/XML werken.
2. De ZGW APIs zijn veel flexibeler dan ZDS. Dit is nodig omdat er geen directe
   acties meer op de database mag worden gedaan door bijvoorbeeld een 
   Zaaksysteem. Alle acties moeten via de ZGW APIs verlopen.
3. De ZGW APIs kunnen alles wat ZDS ook kan.
4. De ZGW APIs zijn opgedeeld. Er is niet meer 1 specificatie of endpoint om
   alle operaties, zoals deze in ZDS bestonden, uit te voeren of data op te
   vragen.
5. De ZGW APIs zullen sneller opvolgende versies krijgen. Hierbij is het niet
   ondenkbaar dat de Zaken API op versie 2 zit, terwijl de Besluiten API al op
   versie 4 zit. Het is daarom ook niet zo dat ZGW een versie nummer krijgt.
   Immers is ZGW alleen maar de verzamelnaam van alle Zaakgericht werken APIs. 
6. De ZGW APIs worden aangetoond middels een referentie implementatie om de
   theoretische specificaties te toetsen aan de praktijk, migratie problemen
   te detecteren en om het vereiste gedrag te definieren daar waar de 
   specificatie ruimte laat voor interpretaties.
7. De ZGW APIs zijn ontwikkeld vanuit developer-first oogpunt waardoor
   koppelingen sneller gemaakt kunnen worden.
8. De ZGW APIs kennen alleen synchrone operaties.
9. De ZGW APIs worden net als ZDS beheerd en onderhouden door VNG, zij het in
   een andere vorm.


## Vergelijking

### Operaties

Alle ZGW APIs zitten nu\* op versie 1.0.0-alpha.

ZDS 1.2 | ZGW APIs\*
--- | ---
Geef Zaakstatus (`geefZaakstatus_ZakLv01`)                              | Zaken API `GET /statussen?zaak=<ID>`  
Geef Zaakdetails (`geefZaakdetails_ZakLv01`)                            | Zaken API `GET /zaken/<ID>` 
Actualiseer Zaakstatus (`actualiseerZaakstatus_ZakLk01`)                | Zaken API `POST /statussen/`
Creëer Zaak (`creeerZaak_ZakLk01`)                                      | Zaken API `POST /zaken`
Update Zaak (`updateZaak_ZakLk01`)                                      | Zaken API `PUT /zaken/<ID>`
Genereer Zaakidentificatie (`genereerZaakIdentificatie_Di02`)           | *niet geïmplementeerd, in overweging* <sup>1</sup>
Geef lijst Zaakdocumenten (`geefLijstZaakdocumenten_ZakLv01`)           | Documenten API `GET /objectinformatieobjecten`
Geef Zaakdocument lezen (`geefZaakdocumentLezen_EdcLv01`)               | Documenten API `GET /enkelvoudiginformatieobjecten/<ID>`
Geef Zaakdocument bewerken (`geefZaakdocumentbewerken_Di02`)            | *niet geïmplementeerd, komt binnenkort* <sup>2</sup>
Voeg Zaakdocument toe (`voegZaakdocumentToe_EdcLk01`)                   | Documenten API `POST /enkelvoudiginformatieobjecten`
Maak Zaakdocument (`maakZaakdocument_EdcLk01`)                          | *niet geïmplementeerd, in overweging* <sup>3</sup>
Update Zaakdocument (`updateZaakdocument_Di02`)                         | Documenten API `POST /enkelvoudiginformatieobjecten`    
Genereer Documentidentificatie (`genereerDocumentIdentificatie_Di02`)   | *niet geïmplementeerd, in overweging* <sup>1</sup>
Cancel CheckOut (`cancelCheckout_Di02`)                                 | *niet geïmplementeerd, komt binnenkort* <sup>2</sup>
CMIS-integratieservice (*geen operatie*)                                | *n.v.t.*
Koppel Zaakdocument aan Zaak (*bestaat niet*)                           | Documenten API `POST /objectinformatieobjecten`
Ontkoppel Zaakdocument (`ontkoppelZaakdocument_Di02`)                   | *niet geïmplementeerd, komt binnenkort* <sup>4</sup>
Voeg besluit toe (`voegBesluitToe_Di01`)                                | Besluiten API `POST /besluiten`
Update Besluit (`updateBesluit_BslLk01`)                                | Besluiten API `PUT /besluiten`
Genereer Besluit Identificatie (`genereerBesluitIdentificatie_Di02`)    | *niet geïmplementeerd, in overweging* <sup>1</sup>
Geef Besluitdetails (`geefBesluitDetails_BslLv01`)                      | Besluiten API `GET /besluiten/<ID>`
Geef lijst Besluiten (`geefLijstBesluiten_ZakLv01`)                     | Besluiten API `GET /besluiten`
Overdragen te behandelen Zaak (`overdragenZaak_Di01`)                   | *n.v.t.*


\* Op het moment van publicatie.
1. Er is op dit moment geen generator voor identificaties voor Zaken, 
   Documenten en Besluiten. De identificaties worden nu automatisch aangemaakt
   als een object *zonder identificatie* wordt aangemaakt. Indien er wel vraag
   blijkt te zijn naar zo'n generator, wordt deze resource toegevoegd.
2. Het *locken* en *unlocken* van documenten is nog niet geïmplementeerd. Deze
   functionaliteit wordt nog toegevoegd.
3. De noodzaak van deze operatie is twijfelachtig. Indien er wel vraag blijkt
   te zijn naar het aanmaken van placeholder documenten, wordt deze toegevoegd.
4. Het verwijderen van een relatie tussen een Document en een Zaak wordt nog
   toegevoegd.


### Attributen

Zie [voortgang](https://github.com/VNG-Realisatie/gemma-zaken/issues/549#issuecomment-446919312) (tijdelijke oplossing).
