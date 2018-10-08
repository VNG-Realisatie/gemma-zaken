ZAKEN API
===============================================
**FUNCTIONELE DOCUMENTATIE**

[aanzet tot documentatie van de API’s van het ZDS2-koppelvlak. Is vooralsnog een
‘try-out’ n.a.v. [userstory
\#188](https://github.com/VNG-Realisatie/gemma-zaken/issues/188) om inzicht te
krijgen in de wijze van (functioneel) documenteren van API’s, als onderdeel van
koppelvlakdocumentatie]

| **Aspect**      | **Beschrijving**                                                                                                                                                                                  |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Doel            | Het kunnen aanspreken van een voorziening voor het onderhouden en raadplegen van zaken inclusief bijbehorende statussen, rollen en relaties naar betrokkenen, objecten, zaaktypen en statustypen. |
| Domein          | Zaakgericht werken                                                                                                                                                                                |
| Provider        | [Zaakregistratiecomponent](https://www.gemmaonline.nl/index.php/GEMMA2/0.9/id-a97b6545-d5a7-485d-9b13-3ce22db5b9cf) (GEMMA2)                                                                      |
| Consumer        | Componenten waarmee zaken behandeld worden (Zaakafhandelcomponenten; ZAC’s) en (andere) componenten die zaakgegevens raadplegen.                                                                  |
| Informatiemodel | [RGBZ, versie 2.00.02](https://www.gemmaonline.nl/images/gemmaonline/a/a4/EgIM_20180621_-_ag_4_-_GEMMA_RGBZ_2.0_-_CONCEPT_20180613.zip) (in-ontwikkeling)                                         |
| Specificaties   | <https://ref.tst.vng.cloud/zrc/api/v1/schema>                                                                                                                                                     |
| Bijzonderheden  | Het RGBZ wordt in meerdere API’s uitgewerkt. De versie van het RGBZ waarnaar verwezen wordt omvat meer dan hetgeen in deze API is uitgewerkt.                                                     |

Deze API omvat (vooralsnog) de resources Zaken, Klantcontacten, Rollen, Statussen en Zaakobjecten.

Elke resource biedt de mogelijkheid om objecten toe te voegen (POST), te wijzigen (PUT, PATCH), te verwijderen (DELETE) en te raadplegen (GET), tenzij anders vermeld.

### Resource: Zaken

| **Aspect**     | **Beschrijving**                                                                                                                                                                                                                                                                                                                       |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aanleiding     | Een consumer wil een zaak toevoegen, gegevens van een zaak wijzigen, wijzigingen aanbrengen in de relatie van een zaak tot betrokkenen en/of objecten dan wel één of meer gegevens van zaken en genoemde relaties opvragen.                                                                                                            |
| Voorwaarde     | 1. Het zaaktype van de zaak moet al bestaan en geldig zijn (resource: zaaktypen in API: ZTC). <br>2.  Een te relateren Betrokkene moet al bestaan (resource: [...] in API:     [...]). <br>3.  Een te relateren Object moet al bestaan (resource: [...] in API: [...]). <br>4.  Bij het toevoegen van een zaak mag de (functionele) Zaakidentificatie meegegeven worden; deze dient uniek te zijn binnen de (bron)organisatie. |
| Gevolg         | De zaak wordt, indien sprake is van valide gegevens, toegevoegd dan wel gewijzigd door de Zaakregistratiecomponent dan wel worden gegevens van de gevonden zaken beschikbaar gesteld. Indien t.b.v. het toevoegen van een zaak geen Zaakidentificatie is meegeleverd dan wordt deze door de ZRC bepaald. |
| Gegevens       | Objecttype ZAAK, inclusief relatie naar Zaaktype. <br>Zie de volgende tabel voor de gegevens van deze resource |
| Specificaties  | <https://ref.tst.vng.cloud/zrc/api/v1/schema/#tag/zaken>                                                                                                                                                                                                                                                                               |
| Samenhang      | Update van Zaak.Einddatum vindt plaats vanuit de resource Statussen.                                                                                                                                                                                                                                                                   |
| Bijzonderheden | -  Zaken kunnen niet verwijderd worden; de operatie DELETE wordt dan ook niet ondersteund. <br>-   Een zaak moet tenminste één betrokkene in een Rol hebben. <br>-   De relatie naar Zaaktype (cq. het zaaktype van de zaak) kan niet gewijzigd worden. [ToDo] <br>-  Indien het zaaktype onjuist blijkt te zijn, dient de zaak beeindigd te worden en een nieuwe zaak (met het juiste zaakype) toegevoegd te worden. <br>-   De Einddatum van de zaak kan alleen opgevraagd worden. Muteren hiervan gebeurt in de resource: Statussen. [ToDo] |


*Gegevens*

[tabel van Sergei met de gegevens van de resource Zaken]


*Wijziginghistorie*

| **Datum** | **User-story(’s)** | **Wijziging** |
|-----------|--------------------|---------------|
| [???]     | [???]              | [???]         |


### Resource: Klantcontacten
[nog uit te werken]

| **Aspect**     | **Beschrijving** |
|----------------|------------------|
| Aanleiding     |                  |
| Voorwaarde     |                  |
| Gevolg         |                  |
| Gegevens       |                  |
| Specificaties  |                  |
| Samenhang      |                  |
| Bijzonderheden |                  |


*Gegevens*

[tabel van Sergei met de gegevens van de resource Klantcontacten]


*Wijziginghistorie*

| **Datum** | **User-story(’s)** | **Wijziging** |
|-----------|--------------------|---------------|
|           |                    |               |


### Resource: Rollen
[nog uit te werken]

| **Aspect**     | **Beschrijving** |
|----------------|------------------|
| Aanleiding     |                  |
| Voorwaarde     |                  |
| Gevolg         |                  |
| Gegevens       |                  |
| Specificaties  |                  |
| Samenhang      |                  |
| Bijzonderheden |                  |


*Gegevens*

[tabel van Sergei met de gegevens van de resource Rollen]


*Wijziginghistorie*

[Gedurende het project zinvol, daarna wellicht niet meer]

| **Datum** | **User-story(’s)** | **Wijziging** |
|-----------|--------------------|---------------|
|           |                    |               |


### Resource: Statussen

| **Aspect**     | **Beschrijving**                                                                                                                                                                                                                    |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aanleiding     | Een consumer wil de status van een zaak wijzigen, gegevens van een status bij een zaak wijzigen of (gegevens van een) status(sen) van een zaak opvragen.  |
| Voorwaarde     | 1.  Het statustype van de status moet al bestaan en geldig zijn en behoren bij het zaaktype van de zaak (resource: Statustypen in API: ZTC). [ToDo] <br>2.  De zaak waartoe de status behoort moet al bestaan en nog niet beeindigd zijn. [ToDo] <br>3.  [...] |
| Gevolg         | De status wordt, indien sprake is van valide gegevens, toegevoegd dan wel gewijzigd door de Zaakregistratiecomponent dan wel worden gegevens van de gevonden statussen beschikbaar gesteld. |
| Gegevens       | Objecttype STATUS, inclusief relatie naar ZAAK en naar ZAAKTYPE. <br>Zie de volgende tabel voor de gegevens van deze resource |
| Specificaties  | <https://ref.tst.vng.cloud/zrc/api/v1/schema/#tag/statussen>                                                                                                                                                                        |
| Samenhang      | [met resource Zaken vanwege einddatum; nog uit te werken hoe]                                                                                                                                                                       |
| Bijzonderheden | Statussen kunnen niet verwijderd worden; de operatie DELETE wordt dan ook niet ondersteund.                                                                                                                                                 |


*Gegevens*

[tabel van Sergei met de gegevens van de resource Statussen]


*Wijziginghistorie*

[Gedurende het project zinvol, daarna wellicht niet meer]

| **Datum** | **User-story(’s)** | **Wijziging** |
|-----------|--------------------|---------------|
| [???]     | [???]              | [???]         |


### Resource: Zaakobjecten
[nog uit te werken]

| **Aspect**     | **Beschrijving** |
|----------------|------------------|
| Aanleiding     |                  |
| Voorwaarde     |                  |
| Gevolg         |                  |
| Gegevens       |                  |
| Specificaties  |                  |
| Samenhang      |                  |
| Bijzonderheden |                  |


*Gegevens*

[tabel van Sergei met de gegevens van de resource Zaakobjecten]


*Wijziginghistorie*

| **Datum** | **User-story(’s)** | **Wijziging** |
|-----------|--------------------|---------------|
|           |                    |               |



