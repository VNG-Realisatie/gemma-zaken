---
title: "ZDS en ZGW API's"
date: '11-01-2019'

---

De Zaak- en Documentservices (ZDS) wijken af van de Zaakgericht werken (ZGW)
APIs, maar er is ook overlap. De belangrijkste verschillen en overeenkomsten op
een rij:

[Zaak-Documentservices](https://www.gemmaonline.nl/index.php/Zaak-_en_Documentservices) | [ZGW APIs](https://zaakgerichtwerken.vng.cloud/standaard/)\*
--- | ---
SOAP/XML gebaseerd	                                                                        | REST/JSON gebaseerd
Gebaseerd op het informatiemodel RGBZ1	                                                    | Gebaseerd op informatiemodel RGBZ2 waar van toepassing
Verdere invulling/uitwerking van de basisberichten uit StUF ZKN	                            | Aparte calls voor aparte resources
Uitwisselen van informatie inclusief gerelateerde gegevens, gestructureerd volgens het informatiemodel [RGBZ 1](https://www.gemmaonline.nl/index.php/Informatiemodel_Zaken_(RGBZ))	| Uitwisselen van informatie op basis van atomische resources, waarbij er gerefereerd wordt naar een resource in een component in plaats van deze te embedden.
Ondersteunen van de functies van een zaaksysteem zoals beschreven in [GEMMA 1](https://www.gemmaonline.nl/index.php/Overzicht_GEMMA_1_referentiecomponenten)	            | Ondersteunen van functies van de referentiecomponenten zoals beschreven in [GEMMA 2](https://www.gemmaonline.nl/index.php/Overzicht_generieke_referentiecomponenten_GEMMA_2)
Kent alleen de functionele acties die uitgewerkt zijn in de standaard.	                    | Alle functionele acties die mogelijk zijn met de CRUD functionaliteit zijn mogelijk. De ZGW API's zijn microservices die gecombineerd kunnen worden om een functionele behoefte in te vullen.
Betrokkenen en/of gerelateerde objecten kunnen geheel of gedeeltelijk, in ieder geval met matchinggegevens doorgegeven worden. Deze worden veelal in het zaaksysteem opgeslagen.	                                                             | Een relatie naar een andere resource is een verwijzing naar die resource. Die resource wordt opgeslagen in de betreffende registratie. Dat kan een zaakregistratie (ZRC) zijn maar ook een andere (met een eigen API).
Bestaan voornamelijk uit a-synchrone services	                                            | Bestaan uit alleen maar synchrone services
Een [GEMMA 1](https://www.gemmaonline.nl/index.php/Overzicht_GEMMA_1_referentiecomponenten) Zaaksysteem bevat ook (generieke) zaakafhandelfunctionaliteit. Deze hoeft niet per se via ZDS te communiceren met het eigen zakenmagazijn  | Een [GEMMA 2](https://www.gemmaonline.nl/index.php/Overzicht_generieke_referentiecomponenten_GEMMA_2) [Zaakregistratiecomponent](https://www.gemmaonline.nl/index.php/GEMMA2/0.9/id-a97b6545-d5a7-485d-9b13-3ce22db5b9cf) registreert alleen zaken en (verwijzingen naar) gerelateerden. Afhandelen gebeurt in een [zaakafhandelcomponent](https://www.gemmaonline.nl/index.php/GEMMA2/0.9/id-f2dfbd0b-9d36-405c-bdbe-827f3296de29) (ZAC). Communicatie vindt plaats via de ZGW API's
Zaak- Documentservices is gemaakt om taakspecifieke applicaties te koppelen aan een zaaksysteem. | ZGW API's zijn gemaakt om zaakgericht werken te ondersteunen
Zaak- Documentservices beschrijven alleen hoe zaken, documenten en besluiten in een zaaksysteem vastgelegd kunnen worden. Er wordt niet beschreven hoe een ZTC bevraagd moet worden etc.                                                           | ZGW API's ondersteunen alle onderdelen van het zaakgericht werken, ook het bevragen van een ZTC etc.
De Zaak- Documentservices standaard bestaat uit een specificatiedocument, xsd schema's en documentatie van de onderliggende StUF en CMIS standaarden.                                                                                | ZGW API standaard bestaat per API uit een OpenAPI 3 specificatie (OAS), functionele en technische documentatie en  referentie-implementaties
Beheer van de Zaak- Documentservices gebeurt in de werkgroep Beheer Zaak- Documentservices. Daarnaast volgt de standaard de ontwikkelingen in de StUF standaard (voor zover van toepassing).                                                      | Beheer van de ZGW API standaard zal (open source) plaatsvinden onder regie van [VNG-Realisatie](https://www.vngrealisatie.nl/). Belanghebbenden kunnen wensen, bevindingen of zelfs wijzigingsvoorstellen indienen via issues en pull requests.
Zaak- Documentservices kent extraElementen, label-value combinaties voor gegevens die niet in het RGBZ 1 opgenomen zijn.  | ZGW API's werken op resources. Wanneer een attribuut of zelfs een resource niet bekend is moet deze toegevoegd worden aan de API die bij de juiste registratie hoort.


## Vergelijking

### Operaties

Alle ZGW APIs zitten nu\* op versie 1.0.0

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
Geef Zaakdocument bewerken (`geefZaakdocumentbewerken_Di02`)            | Documenten API `POST /enkelvoudiginformatieobjecten/<ID>/lock`
Voeg Zaakdocument toe (`voegZaakdocumentToe_EdcLk01`)                   | Documenten API `POST /enkelvoudiginformatieobjecten`
Maak Zaakdocument (`maakZaakdocument_EdcLk01`)                          | *niet geïmplementeerd, in overweging* <sup>2</sup>
Update Zaakdocument (`updateZaakdocument_Di02`)                         | Documenten API `POST /enkelvoudiginformatieobjecten`
Genereer Documentidentificatie (`genereerDocumentIdentificatie_Di02`)   | *niet geïmplementeerd, in overweging* <sup>1</sup>
Cancel CheckOut (`cancelCheckout_Di02`)                                 | Documenten API `POST /enkelvoudiginformatieobjecten/<ID>/unlock`
CMIS-integratieservice (*geen operatie*)                                | *n.v.t.*
Koppel Zaakdocument aan Zaak (*bestaat niet*)                           | Documenten API `POST /objectinformatieobjecten`
Ontkoppel Zaakdocument (`ontkoppelZaakdocument_Di02`)                   | Documenten API `DELETE /objectinformatieobjecten`
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
2. De noodzaak van deze operatie is twijfelachtig. Indien er wel vraag blijkt
   te zijn naar het aanmaken van placeholder documenten, wordt deze toegevoegd.

### Attributen

Zie [voortgang](https://github.com/VNG-Realisatie/gemma-zaken/issues/549#issuecomment-446919312) (tijdelijke oplossing).
