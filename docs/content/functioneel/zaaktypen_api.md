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

### Resource: catalogus

| **Aspect**     | **Beschrijving**                                                                                                                                                                 |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aanleiding     | Een consumer wil informatie van alle beschikbare catalogussen of een specifieke catalogus opvragen.         |
| *Toevoegen*    |      |
| - voorwaarde   | Nog niet beschikbaar.         |
| - gevolg       | Nog te bepalen.             |
| *Wijzigen*     |      |
| - voorwaarde   | Nog niet beschikbaar.         |
| - gevolg       | Nog te bepalen.             |
| *Verwijderen*  |      |
| - voorwaarde   | Nog niet beschikbaar.         |
| - gevolg       | Nog te bepalen.             |
| *Raadplegen lijst*   |      |
| - voorwaarde   | Geen aanvullende voorwaarden gesteld.  |
| - gevolg       | Een lijst met beschikbare catalogussen wordt teruggegeven aan de consumer bij het opvragen van de lijst. |
| *Raadplegen details*   |      |
| - voorwaarde   | De identificatie van de catalogus die opgevraagd wordt moet bekend zijn.  |
| - gevolg       | Een specificieke catalogus wordt teruggegeven aan de consumer. |
| Gegevens       | objecttype CATALOGUS inclusief een lijst met relaties naar daarin gedefinieerde ZAAKTYPEn.<br>Zie de volgende tabel voor de gegevens van deze resource                                 |
| Specificaties  | https://ref.tst.vng.cloud/ztc/api/v1/schema/#tag/catalogussen                                                                                                   |
| Samenhang      | - |
| Bijzonderheden | - |
        


### Resource: zaaktype

| **Aspect**     | **Beschrijving**                                                                                                                                                                 |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aanleiding     | Een consumer wil zaaktypeinformatie opvragen uit de catalogus.            |
| *Toevoegen*    |      |
| - voorwaarde   | Nog niet beschikbaar.         |
| - gevolg       | Nog te bepalen.             |
| *Wijzigen*     |      |
| - voorwaarde   | Nog niet beschikbaar.         |
| - gevolg       | Nog te bepalen.             |
| *Verwijderen*  |      |
| - voorwaarde   | Nog niet beschikbaar.  |
| - gevolg       | Nog te bepalen.             |
| *Raadplegen lijst*   |      |
| - voorwaarde   | Om zaaktypeinformatie op te kunnen vragen moet de consumer weten in welke catalogus het zaaktype is opgenomen. |
| - gevolg       | Een lijst met in de catalogus opgenomen zaaktypen wordt teruggegeven aan de consumer bij het opvragen van de lijst. |
| *Raadplegen details*   |      |
| - voorwaarde   | Om specifieke zaaktypeinformatie op te kunnen vragen moet de consumer weten in welke catalogus het zaaktype is opgenomen. Tevens moet de identficatie van het zaaktype wat uitgevraagd wordt bekend zijn. |
| - gevolg       | Een specificiek zaaktype wordt teruggegeven aan de consumer.         |
| Gegevens       | ZAAKTYPE inclusief STATUSTYPEn, EIGENSCHAPpen en ROLTYPEn<br>Zie de volgende tabel voor de gegevens van deze resource                                 |
| Specificaties  | https://ref.tst.vng.cloud/ztc/api/v1/schema/#operation/zaaktype_read                                                                                |
| Samenhang      | - |
| Bijzonderheden | - |



### Resource: BESLUITTYPE

| **Aspect**     | **Beschrijving**                                                                                                                                                                 |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aanleiding     | Een consumer wil besluittypeinformatie van de besluiten die het resultaat kunnen zijn van het zaakgericht werken van de behandelende organisatie(s) opvragen.            |
| *Toevoegen*    |      |
| - voorwaarde   | Nog niet beschikbaar.  |
| - gevolg       | Nog te bepalen.             |
| *Wijzigen*     |      |
| - voorwaarde   | Nog niet beschikbaar.  |
| - gevolg       | Nog te bepalen.             |
| *Verwijderen*  |      |
| - voorwaarde   | Nog niet beschikbaar.  |
| - gevolg       | Nog te bepalen.             |
| *Raadplegen lijst*   |      |
| - voorwaarde   | Om besluittypeinformatie op te kunnen vragen moet de consumer weten in welke catalogus het besluittype is opgenomen. |
| - gevolg       | Een overzicht met besluittype informatie zoals opgenomen in de catalogus wordt teruggegeven.             |
| *Raadplegen details*   |      |
| - voorwaarde   | Om specifieke besluittypeinformatie op te kunnen vragen moet de consumer weten in welke catalogus het besluittype is opgenomen. Tevens moet de identficatie  van het besluittype wat uitgevraagd wordt bekend zijn. |
| - gevolg       | Besluittypeinformatie zoals opgenomen in de catalogus wordt teruggegeven.             |
| Gegevens       | BESLUITTYPE <br>Zie de volgende tabel voor de gegevens van deze resource                                 |
| Specificaties  | https://ref.tst.vng.cloud/ztc/api/v1/schema/#operation/besluittype_read                                                                                |
| Samenhang      | - |
| Bijzonderheden | - |

### Resource: INFORMATIEOBJECTTYPE

| **Aspect**     | **Beschrijving**                                                                                                                                                                 |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aanleiding     | Een consumer wil informatieobjecttypeinformatie van de informatieobjecten die voor kunnen komen bij het zaaktype zoals opgenomen in de catalogus van de organisatie opvragen.            |
| *Toevoegen*    |      |
| - voorwaarde   | Nog niet beschikbaar.  |
| - gevolg       | Nog te bepalen.             |
| *Wijzigen*     |      |
| - voorwaarde   | Nog niet beschikbaar.  |
| - gevolg       | Nog te bepalen.             |
| *Verwijderen*  |      |
| - voorwaarde   | Nog niet beschikbaar.  |
| - gevolg       | Nog te bepalen.             |
| *Raadplegen lijst*   |      |
| - voorwaarde   | Om informatieobjecttypeinformatie op te kunnen vragen moet de consumer weten in welke catalogus het besluittype is opgenomen. |
| - gevolg       | Een overzicht van Informatieobjecttypeinformatie zoals opgenomen in de catalogus wordt teruggegeven.             |
| *Raadplegen details*   |      |
| - voorwaarde   | Om details van informatieobjecttypeinformatie op te kunnen vragen moet de consumer weten in welke catalogus het informatieobjecttype is opgenomen. Tevens moet de identficatie van het informatieobjecttype wat uitgevraagd wordt bekend zijn. |
| - gevolg       | Informatieobjecttypeinformatie zoals opgenomen in de catalogus wordt teruggegeven.             |
| Gegevens       | INFORMATIEOBJECTTYPE <br>Zie de volgende tabel voor de gegevens van deze resource                                 |
| Specificaties  | https://ref.tst.vng.cloud/ztc/api/v1/schema/#operation/informatieobjecttype_read                                                                                |
| Samenhang      | - |
| Bijzonderheden | - |


### Resource: eigenschap

| **Aspect**     | **Beschrijving**                                                                                                                                                                 |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aanleiding     | Een consumer wil alle eigenschappen van een zaaktype zoals opgenomen in de catalogus van de organisatie opvragen.             |
| *Toevoegen*    |      |
| - voorwaarde   | Nog niet beschikbaar.  |
| - gevolg       | Nog te bepalen.             |
| *Wijzigen*     |      |
| - voorwaarde   | Nog niet beschikbaar.  |
| - gevolg       | Nog te bepalen.             |
| *Verwijderen*  |      |
| - voorwaarde   | Nog niet beschikbaar.  |
| - gevolg       | Nog te bepalen.             |
| *Raadplegen lijst*   |      |
| - voorwaarde   | Om eigenschapinformatie op te kunnen vragen moet de consumer weten in welke catalogus en bij welk zaaktype de eigenschap is opgenomen. |
| - gevolg       | Een overzicht van eigenschapinformatie van het zaaktype wordt teruggegeven.            |
| *Raadplegen details*   |      |
| - voorwaarde   | Om details van eigenschapinformatie op te kunnen vragen moet de consumer weten in welke catalogus en bij welk zaaktype de eigenschap is opgenomen. Tevens moet de identficatie van de eigenschap welke uitgevraagd wordt bekend zijn. |
| - gevolg       | Detailinformatie van de eigenschap wordt teruggegeven.            |
| Gegevens       | EIGENSCHAP <br>Zie de volgende tabel voor de gegevens van deze resource                                 |
| Specificaties  | https://ref.tst.vng.cloud/ztc/api/v1/schema/#operation/eigenschap_read                                                                                |
| Samenhang      | Een relevant inhoudelijk gegeven dat bj ZAAKen van dit ZAAKTYPE geregistreerd moet kunnen worden en geen standaard kenmerk is van een ZAAK. |
| Bijzonderheden | - |
      
### Resource: roltype

| **Aspect**     | **Beschrijving**                                                                                                                                                                 |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aanleiding     | Een consumer wil alle roltypen van een zaaktype zoals opgenomen in de catalogus van de organisatie opvragen.            |
| *Toevoegen*    |      |
| - voorwaarde   | Nog niet beschikbaar.  |
| - gevolg       | Nog te bepalen.             |
| *Wijzigen*     |      |
| - voorwaarde   | Nog niet beschikbaar.  |
| - gevolg       | Nog te bepalen.             |
| *Verwijderen*  |      |
| - voorwaarde   | Nog niet beschikbaar.  |
| - gevolg       | Nog te bepalen.             |
| *Raadplegen lijst*   |      |
| - voorwaarde   | Om roltypeinformatie op te kunnen vragen moet de consumer weten in welke catalogus en bij welk zaaktype het roltype is opgenomen. |
| - gevolg       | Een lijst met roltypeinformatie behorend bij het zaaktype wordt teruggegeven aan de consumer.             |
| *Raadplegen details*   |      |
| - voorwaarde   | Om roltypeinformatie op te kunnen vragen moet de consumer weten in welke catalogus en bij welk zaaktype het roltype is opgenomen. Tevens moet de identficatie van het roltype wat uitgevraagd wordt bekend zijn. |
| - gevolg       | Roltypeinformatie wordt teruggegeven aan de consumer.             |
| Gegevens       | ROLTYPE <br>Zie de volgende tabel voor de gegevens van deze resource                                 |
| Specificaties  | https://ref.tst.vng.cloud/ztc/api/v1/schema/#operation/roltype_read                                                                                                   |
| Samenhang      | - |
| Bijzonderheden | Generieke aanduiding van de aard van een ROL die een BETROKKENE kan uitoefenen in ZAAKen van een ZAAKTYPE.       |

       
### Resource: STATUSTYPE

| **Aspect**     | **Beschrijving**                                                                                                                                                                 |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aanleiding     | Een consumer wil statustypeinformatie van een ZAAKTYPE zoals opgenomen in de CATALOGUS van de organisatie opvragen.           |
| *Toevoegen*    |      |
| - voorwaarde   | Nog niet beschikbaar.  |
| - gevolg       | Nog te bepalen.             |
| *Wijzigen*     |      |
| - voorwaarde   | Nog niet beschikbaar.  |
| - gevolg       | Nog te bepalen.             |
| *Verwijderen*  |      |
| - voorwaarde   | Nog niet beschikbaar.  |
| - gevolg       | Nog te bepalen.             |
| *Raadplegen lijst*   |      |
| - voorwaarde   | Om statustypeinformatie op te kunnen vragen moet de consumer weten in welke catalogus en bij welk zaaktype het statustype is opgenomen. |
| - gevolg       | Een lijst met statustypeinformatie wordt teruggegeven aan de consumer.             |
| *Raadplegen details*   |      |
| - voorwaarde   | Om statustypeinformatie op te kunnen vragen moet de consumer weten in welke catalogus en bij welk zaaktype het statustype is opgenomen. Tevens moet de identficatie van het statustype wat uitgevraagd wordt bekend zijn. |
| - gevolg       | Statustypeinformatie wordt teruggegeven aan de consumer.             |
| Gegevens       | STATUSTYPE <br>Zie de volgende tabel voor de gegevens van deze resource                                 |
| Specificaties  | https://ref.tst.vng.cloud/ztc/api/v1/schema/#operation/statustype_read                                                                                                   |
| Samenhang      | - |
| Bijzonderheden | Generieke aanduiding van de aard van een STATUS. |

