ZAAKTYPEN API
===============================================
**FUNCTIONELE DOCUMENTATIE**

| **Aspect**      | **Beschrijving**                                                                                                                                                                                  |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Doel            | Het kunnen aanspreken van een voorziening voor het raadplegen van zaaktypen en de zaaktypecatalogi (ZTC) waarvan zij deel uit maken. |
| Domein          | Zaakgericht werken                                                                                                                                                                                |
| Provider        | [Zaaktypecataloguscomponent](https://www.gemmaonline.nl/index.php/GEMMA2/0.9/id-3ef9cdd9-631c-4d3e-88c3-f756423d6314) (GEMMA2)                                                              |
| Consumer        | Componenten waarmee zaaktypen beheerd worden en componenten die zaaktypegegevens gebruiken voor het behandelen van zaken, zoals Zaakafhandelcomponenten (ZAC’s).                                                              |
| Informatiemodel | [ImZTC, versie 2.2](https://www.gemmaonline.nl/images/gemmaonline/1/1d/EgIM_20180621_-_ag_4_-_GEMMA_ImZTC_2.2_-_CONCEPT_20180613.zip) (in-ontwikkeling)                                         |
| Specificaties   | <https://ref.tst.vng.cloud/ztc/api/v1/schema>        | 
| Bijzonderheden  | -                                                    |

Deze API omvat (vooralsnog) de resources Catalogussen, Zaaktypen, Informatieobjecttypen, Roltypen, Statustypen en Besluittypen.

Op dit moment bieden de resources alleen de mogelijkheid tot raadplegen van de gegevens (GET).

### Resource: Catalogussen

| **Aspect**     | **Beschrijving**                                                                                                                                                                 |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aanleiding     | Een consumer wil informatie opvragen van alle beschikbare catalogussen of een specifieke catalogus.         |
| *Toevoegen*    | Nog niet beschikbaar.     |
| - voorwaarde   | Nog te bepalen.         |
| - gevolg       | Nog te bepalen.             |
| *Wijzigen*     | Nog niet beschikbaar.     |
| - voorwaarde   | Nog te bepalen.         |
| - gevolg       | Nog te bepalen.             |
| *Verwijderen*  | Nog niet beschikbaar.     |
| - voorwaarde   | Nog te bepalen.         |
| - gevolg       | Nog te bepalen.             |
| *Raadplegen lijst*   |      |
| - voorwaarde   | Geen aanvullende voorwaarden gesteld.  |
| - gevolg       | De beschikbare catalogussen worden teruggegeven aan de consumer. |
| *Raadplegen details*   |      |
| - voorwaarde   | De identificatie van de catalogus die opgevraagd wordt moet bekend zijn.  |
| - gevolg       | Een specificieke catalogus wordt teruggegeven aan de consumer. |
| Gegevens       | Objecttype CATALOGUS inclusief relatie naar ZAAKTYPEn.<br>Zie de volgende tabel voor de gegevens van deze resource                                 |
| Specificaties  | https://ref.tst.vng.cloud/ztc/api/v1/schema/#tag/catalogussen                                                                                                   |
| Samenhang      | - |
| Bijzonderheden | - |
        


### Resource: Zaaktypen

| **Aspect**     | **Beschrijving**                                                                                                                                                                 |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aanleiding     | Een consumer wil zaaktypeinformatie opvragen uit de catalogus.            |
| *Toevoegen*    | Nog niet beschikbaar.     |
| - voorwaarde   | Nog te bepalen.         |
| - gevolg       | Nog te bepalen.             |
| *Wijzigen*     | Nog niet beschikbaar.     |
| - voorwaarde   | Nog te bepalen.         |
| - gevolg       | Nog te bepalen.             |
| *Verwijderen*  | Nog niet beschikbaar.     |
| - voorwaarde   | Nog te bepalen.  |
| - gevolg       | Nog te bepalen.             |
| *Raadplegen lijst*   |      |
| - voorwaarde   | Om zaaktypeinformatie op te kunnen vragen moet de consumer weten in welke catalogus het zaaktype is opgenomen. |
| - gevolg       | Een overzicht van zaaktypen zoals opgenomen in de catalogus wordt teruggegeven aan de consumer bij het opvragen van de lijst. |
| *Raadplegen details*   |      |
| - voorwaarde   | Om specifieke zaaktypeinformatie op te kunnen vragen moet de consumer weten in welke catalogus het zaaktype is opgenomen. Tevens moet de identficatie van het zaaktype wat uitgevraagd wordt bekend zijn. |
| - gevolg       | Een specificiek zaaktype wordt teruggegeven aan de consumer.         |
| Gegevens       | Objecttype ZAAKTYPE inclusief relaties naar STATUSTYPEn, EIGENSCHAPpen en ROLTYPEn<br>Zie de volgende tabel voor de gegevens van deze resource                                 |
| Specificaties  | https://ref.tst.vng.cloud/ztc/api/v1/schema/#operation/zaaktype_read                                                                                |
| Samenhang      | - |
| Bijzonderheden | - |



### Resource: Besluittypen

| **Aspect**     | **Beschrijving**                                                                                                                                                                 |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aanleiding     | Een consumer wil (gegevens van een) besluittype(n) opvragen.            |
| *Toevoegen*    | Nog niet beschikbaar.     |
| - voorwaarde   | Nog te bepalen.  |
| - gevolg       | Nog te bepalen.             |
| *Wijzigen*     | Nog niet beschikbaar.     |
| - voorwaarde   | Nog te bpalen.  |
| - gevolg       | Nog te bepalen.             |
| *Verwijderen*  | Nog niet beschikbaar.     |
| - voorwaarde   | Nog te bepalen.  |
| - gevolg       | Nog te bepalen.             |
| *Raadplegen lijst*   |      |
| - voorwaarde   | Om besluittypeinformatie op te kunnen vragen moet de consumer weten in welke catalogus het besluittype is opgenomen. |
| - gevolg       | Een overzicht met besluittypen zoals opgenomen in de catalogus wordt teruggegeven.             |
| *Raadplegen details*   |      |
| - voorwaarde   | Om specifieke besluittypeinformatie op te kunnen vragen moet de consumer weten in welke catalogus het besluittype is opgenomen. Tevens moet de identficatie  van het besluittype wat uitgevraagd wordt bekend zijn. |
| - gevolg       | Besluittypeinformatie zoals opgenomen in de catalogus wordt teruggegeven.             |
| Gegevens       | Objecttype BESLUITTYPE <br>Zie de volgende tabel voor de gegevens van deze resource                                 |
| Specificaties  | https://ref.tst.vng.cloud/ztc/api/v1/schema/#operation/besluittype_read                                                                                |
| Samenhang      | - |
| Bijzonderheden | - |

### Resource: Informatieobjecttypen

| **Aspect**     | **Beschrijving**                                                                                                                                                                 |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aanleiding     | Een consumer wil informatie opvragen van één of meer informatieobjecttypen die voorkomen in een zaaktypecatalogus van de organisatie.            |
| *Toevoegen*    | Nog niet beschikbaar.     |
| - voorwaarde   | Nog te bepalen.  |
| - gevolg       | Nog te bepalen.             |
| *Wijzigen*     | Nog niet beschikbaar.    |
| - voorwaarde   | Nog tebepalen.  |
| - gevolg       | Nog te bepalen.             |
| *Verwijderen*  | Nog niet beschikbaar.     |
| - voorwaarde   | Nog te bepalen.  |
| - gevolg       | Nog te bepalen.             |
| *Raadplegen lijst*   |      |
| - voorwaarde   | Om informatieobjecttypeinformatie op te kunnen vragen moet de consumer weten in welke catalogus het informatieobjecttypeinformatie is opgenomen. |
| - gevolg       | Een overzicht van Informatieobjecttypen zoals opgenomen in de catalogus wordt teruggegeven.             |
| *Raadplegen details*   |      |
| - voorwaarde   | Om details van informatieobjecttypeinformatie op te kunnen vragen moet de consumer weten in welke catalogus het informatieobjecttype is opgenomen. Tevens moet de identficatie van het informatieobjecttype wat uitgevraagd wordt bekend zijn. |
| - gevolg       | Informatieobjecttypeinformatie zoals opgenomen in de catalogus wordt teruggegeven.             |
| Gegevens       | Objecttype INFORMATIEOBJECTTYPE <br>Zie de volgende tabel voor de gegevens van deze resource                                 |
| Specificaties  | https://ref.tst.vng.cloud/ztc/api/v1/schema/#operation/informatieobjecttype_read                                                                                |
| Samenhang      | - |
| Bijzonderheden | - |


### Resource: Eigenschappen

| **Aspect**     | **Beschrijving**                                                                                                                                                                 |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aanleiding     | Een consumer wil een eigenschap of een overzicht van alle eigenschappen opvragen van een zaaktype zoals opgenomen in de catalogus van de organisatie.             |
| *Toevoegen*    | Nog niet beschikbaar.     |
| - voorwaarde   | Nog te bepalen.  |
| - gevolg       | Nog te bepalen.             |
| *Wijzigen*     | Nog niet beschikbaar.     |
| - voorwaarde   | Nog te bepalen.  |
| - gevolg       | Nog te bepalen.             |
| *Verwijderen*  | Nog niet beschikbaar.     |
| - voorwaarde   | Nog te bepalen.  |
| - gevolg       | Nog te bepalen.             |
| *Raadplegen lijst*   |      |
| - voorwaarde   | Om eigenschapinformatie op te kunnen vragen moet de consumer weten in welke catalogus en bij welk zaaktype de eigenschap is opgenomen. |
| - gevolg       | Een overzicht van eigenschapinformatie van het zaaktype wordt teruggegeven.            |
| *Raadplegen details*   |      |
| - voorwaarde   | Om details van eigenschapinformatie op te kunnen vragen moet de consumer weten in welke catalogus en bij welk zaaktype de eigenschap is opgenomen. Tevens moet de identficatie van de eigenschap welke uitgevraagd wordt bekend zijn. |
| - gevolg       | Detailinformatie van de eigenschap wordt teruggegeven.            |
| Gegevens       | Objecttype EIGENSCHAP inclusief de relatie naar ZAAKTYPE<br>Zie de volgende tabel voor de gegevens van deze resource                                 |
| Specificaties  | https://ref.tst.vng.cloud/ztc/api/v1/schema/#operation/eigenschap_read                                                                                |
| Samenhang      | - |
| Bijzonderheden | - |
      
### Resource: Roltypen

| **Aspect**     | **Beschrijving**                                                                                                                                                                 |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aanleiding     | Een consumer wil informatie opvragen van een specifiek roltype of van alle roltypen van een zaaktype zoals opgenomen in de catalogus van de organisatie.            |
| *Toevoegen*    | Nog niet beschikbaar.     |
| - voorwaarde   | Nog te bepalen.  |
| - gevolg       | Nog te bepalen.             |
| *Wijzigen*     | Nog niet beschikbaar.     |
| - voorwaarde   | Nog te bepalen.  |
| - gevolg       | Nog te bepalen.             |
| *Verwijderen*  | Nog niet beschikbaar.     |
| - voorwaarde   | Nog te bepalen.  |
| - gevolg       | Nog te bepalen.             |
| *Raadplegen lijst*   |      |
| - voorwaarde   | Om roltypeinformatie op te kunnen vragen moet de consumer weten in welke catalogus en bij welk zaaktype het roltype is opgenomen. |
| - gevolg       | Een lijst met roltypeinformatie behorend bij het zaaktype wordt teruggegeven aan de consumer.             |
| *Raadplegen details*   |      |
| - voorwaarde   | Om roltypeinformatie op te kunnen vragen moet de consumer weten in welke catalogus en bij welk zaaktype het roltype is opgenomen. Tevens moet de identficatie van het roltype wat uitgevraagd wordt bekend zijn. |
| - gevolg       | Roltypeinformatie wordt teruggegeven aan de consumer.             |
| Gegevens       | Objecttype ROLTYPE inclusief relatie naar het ZAAKTYPE waar het ROLTYPE bij hoort.<br>Zie de volgende tabel voor de gegevens van deze resource                                 |
| Specificaties  | https://ref.tst.vng.cloud/ztc/api/v1/schema/#operation/roltype_read                                                                                                   |
| Samenhang      | - |
| Bijzonderheden | - |

       
### Resource: Statustypen

| **Aspect**     | **Beschrijving**                                                                                                                                                                 |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aanleiding     | Een consumer wil informatie opvragen van een specifiek statustype of van alle statustypen van een zaaktype zoals opgenomen in de catalogus van de organisatie.           |
| *Toevoegen*    | Nog niet beschikbaar.     |
| - voorwaarde   | Nog te bepalen.  |
| - gevolg       | Nog te bepalen.             |
| *Wijzigen*     | Nog niet beschikbaar.     |
| - voorwaarde   | Nog te bepalen.  |
| - gevolg       | Nog te bepalen.             |
| *Verwijderen*  | Nog niet beschikbaar.     |
| - voorwaarde   | Nog te bepalen.  |
| - gevolg       | Nog te bepalen.             |
| *Raadplegen lijst*   |      |
| - voorwaarde   | Om statustypeinformatie op te kunnen vragen moet de consumer weten in welke catalogus en bij welk zaaktype het statustype is opgenomen. |
| - gevolg       | Een lijst met statustypeinformatie wordt teruggegeven aan de consumer.             |
| *Raadplegen details*   |      |
| - voorwaarde   | Om statustypeinformatie op te kunnen vragen moet de consumer weten in welke catalogus en bij welk zaaktype het statustype is opgenomen. Tevens moet de identficatie van het statustype wat uitgevraagd wordt bekend zijn. |
| - gevolg       | Statustypeinformatie wordt teruggegeven aan de consumer.             |
| Gegevens       | Objecttype STATUSTYPE <br>Zie de volgende tabel voor de gegevens van deze resource                                 |
| Specificaties  | https://ref.tst.vng.cloud/ztc/api/v1/schema/#operation/statustype_read                                                                                                   |
| Samenhang      | - |
| Bijzonderheden | - |

