ZAAKTYPEN API
===============================================
**FUNCTIONELE DOCUMENTATIE**

| **Aspect**      | **Beschrijving**                                                                                                                                                                                  |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Doel            | Het kunnen aanspreken van een voorziening voor het onderhouden en raadplegen van zaaktypen en de zaaktypecatalogi (ZTC) waarvan zij deel uit maken. |
| Domein          | Zaakgericht werken                                                                                                                                                                                |
| Provider        | [Zaaktypecataloguscomponent](https://www.gemmaonline.nl/index.php/GEMMA2/0.9/id-3ef9cdd9-631c-4d3e-88c3-f756423d6314) (GEMMA2)                                                              |
| Consumer        | Componenten waarmee zaaktypen beheerd worden en componenten die zaaktypegegevens gebruiken voor het behandelen van zaken, zoals Zaakafhandelcomponenten (ZAC’s).                                                              |
| Informatiemodel | [IMZTC, versie 2.2](https://www.gemmaonline.nl/images/gemmaonline/1/1d/EgIM_20180621_-_ag_4_-_GEMMA_ImZTC_2.2_-_CONCEPT_20180613.zip) (in-ontwikkeling)                                         |
| Specificaties   | <https://ref.tst.vng.cloud/zrc/api/v1/schema>                                                                                                                                                     |
| Bijzonderheden  | -                                                    |

Deze API omvat (vooralsnog) de resources Catalogussen, Zaaktypen, Informatieobjecttypen, Roltypen, Statustypen en Zaakobjecten.

Op dit moment bieden de resources alleen de mogelijkheid tot raadplegen van de gegevens (GET).

### Resource: catalogus

| **Aspect**     | **Beschrijving**                                                                                                                                                                 |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aanleiding     | Een consumer wil een lijst van alle beschikbare CATALOGUSsen of een specifieke catalogus opvragen.         |
| *Toevoegen*    |      |
| - voorwaarde   | nvt.         |
| - gevolg       | nvt.             |
| *Wijzigen*     |      |
| - voorwaarde   | nvt.         |
| - gevolg       | nvt.             |
| *Verwijderen*  |      |
| - voorwaarde   | nvt.         |
| - gevolg       | nvt.             |
| *Raadplegen*   |      |
| - voorwaarde   | nvt.         |
| - gevolg       | Een lijst met beschikbare catalogussen wordt teruggegeven aan de consumer bij het opvragen van de lijst.<br>Een specificieke catalogus wordt teruggegeven aan de consumer. |
| Gegevens       | objecttype CATALOGUS inclusief een lijst met relaties naar daarin gedefinieerde ZAAKTYPEn.<br>Zie de volgende tabel voor de gegevens van deze resource                                 |
| Specificaties  | https://ref.tst.vng.cloud/ztc/api/v1/schema/#tag/catalogus                                                                                                   |
| Samenhang      | nvt. |
| Bijzonderheden | nvt. |
        


### Resource: zaaktype

| **Aspect**     | **Beschrijving**                                                                                                                                                                 |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aanleiding     | Een consumer wil (een lijst van beschikbare) zaaktype informatie opvragen uit de catalogus.            |
| *Toevoegen*    |      |
| - voorwaarde   | nvt.         |
| - gevolg       | nvt.             |
| *Wijzigen*     |      |
| - voorwaarde   | nvt.         |
| - gevolg       | nvt.             |
| *Verwijderen*  |      |
| - voorwaarde   | nvt.         |
| - gevolg       | nvt.             |
| *Raadplegen*   |      |
| - voorwaarde   | Om zaaktype informatie op te kunnen vragen moet de consumer de UUID van de catalogus waarin het zaaktype is opgenomen weten. Deze UUID kan opgevraagd worden met de catalogus bevragingen services.       |
| - gevolg       | Een lijst met in de catalogus opgenomen zaaktypen wordt teruggegeven aan de consumer bij het opvragen van de lijst.<br>Een specificiek zaaktype wordt teruggegeven aan de consumer.         |
| Gegevens       | ZAAKTYPE inclusief STATUSTYPEn, EIGENSCHAPpen en ROLTYPEn<br>Zie de volgende tabel voor de gegevens van deze resource                                 |
| Specificaties  | https://ref.tst.vng.cloud/ztc/api/v1/schema/#tag/zaaktype                                                                                |
| Samenhang      | - |
| Bijzonderheden | -           |



### Resource: BESLUITTYPE

| **Aspect**     | **Beschrijving**                                                                                                                                                                 |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aanleiding     | Een consumer wil alle BESLUITTYPEn van de besluiten die het resultaat kunnen zijn van het zaakgericht werken van de behandelende organisatie(s) opvragen.            |
| *Toevoegen*    |      |
| - voorwaarde   | nvt.         |
| - gevolg       | nvt.             |
| *Wijzigen*     |      |
| - voorwaarde   | nvt.         |
| - gevolg       | nvt.             |
| *Verwijderen*  |      |
| - voorwaarde   | nvt.         |
| - gevolg       | nvt.             |
| *Raadplegen*   |      |
| - voorwaarde   | Om besluittype informatie op te kunnen vragen moet de consumer de UUID van de catalogus waarin het besluittype is opgenomen weten. Deze UUID kan opgevraagd worden met de catalogus bevragingen services.
         |
| - gevolg       | Een (lijst met) besluittype informatie zoals opgenomen in de catalogus wordt teruggegeven.             |
| Gegevens       | Besluittype <br>Zie de volgende tabel voor de gegevens van deze resource                                 |
| Specificaties  | [https://ref.tst.vng.cloud/ztc/api/v1/schema/#tag/besluittype                                                                                                   |
| Samenhang      | - |
| Bijzonderheden | -           |


### Resource: INFORMATIEOBJECTTYPE

| **Aspect**     | **Beschrijving**                                                                                                                                                                 |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aanleiding     | Een consumer wil alle INFORMATIEOBJECTTYPEn van de INFORMATIEOBJECTEN die voor kunnen komen bij het ZAAKTYPE zoals opgenomen in de CATALOGUS van de organisatie opvragen.            |
| *Toevoegen*    |      |
| - voorwaarde   | nvt.         |
| - gevolg       | nvt.             |
| *Wijzigen*     |      |
| - voorwaarde   | nvt.         |
| - gevolg       | nvt.             |
| *Verwijderen*  |      |
| - voorwaarde   | nvt.         |
| - gevolg       | nvt.             |
| *Raadplegen*   |      |
| - voorwaarde   | Om informatieobjecttype informatie op te kunnen vragen moet de consumer de UUID van de catalogus waarin het informatieobjecttype is opgenomen weten. Deze UUID kan opgevraagd worden met de catalogus bevragingen services.
         |
| - gevolg       | Een (lijst met) besluittype informatie zoals opgenomen in de catalogus wordt teruggegeven.             |
| Gegevens       | Informatieobjecttype <br>Zie de volgende tabel voor de gegevens van deze resource                                 |
| Specificaties  | [https://ref.tst.vng.cloud/ztc/api/v1/schema/#tag/informatieobjecttype                                                                                                   |
| Samenhang      | - |
| Bijzonderheden | -           |


### Resource: eigenschap

| **Aspect**     | **Beschrijving**                                                                                                                                                                 |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aanleiding     | Een consumer wil alle EIGENSCHAPpen van een ZAAKTYPE zoals opgenomen in de CATALOGUS van de organisatie opvragen.             |
| *Toevoegen*    |      |
| - voorwaarde   | nvt.         |
| - gevolg       | nvt.            |
| *Wijzigen*     |      |
| - voorwaarde   | nvt.         |
| - gevolg       | nvt.             |
| *Verwijderen*  |      |
| - voorwaarde   | nvt.         |
| - gevolg       | nvt.             |
| *Raadplegen*   |      |
| - voorwaarde   | Om EIGENSCHAP informatie op te kunnen vragen moet de consumer de UUID van de CATALOGUS en de UUID van het ZAAKTYPE waarin de EIGENSCHAP is opgenomen weten. Deze UUIDs kunnen opgevraagd worden met de catalogus bevragingen services en ZAAKTYPE bevragingen services.         |
| - gevolg       | Een (lijst met) eigenschap informatie van het ZAAKTYPE wordt teruggegeven.            |
| Gegevens       | EIGENSCHAP <br>Zie de volgende tabel voor de gegevens van deze resource                                 |
| Specificaties  | [https://ref.tst.vng.cloud/ztc/api/v1/schema/#tag/eigenschap                                                                                                   |
| Samenhang      | Een relevant inhoudelijk gegeven dat bij ZAAKen van dit ZAAKTYPE geregistreerd moet kunnen worden en geen standaard kenmerk is van een zaak.  |
| Bijzonderheden |      |

      
### Resource: roltype

| **Aspect**     | **Beschrijving**                                                                                                                                                                 |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aanleiding     | Een consumer wil alle ROLTYPEn van een ZAAKTYPE zoals opgenomen in de CATALOGUS van de organisatie opvragen.            |
| *Toevoegen*    |      |
| - voorwaarde   | nvt.         |
| - gevolg       | nvt.             |
| *Wijzigen*     |      |
| - voorwaarde   | nvt.         |
| - gevolg       | nvt.             |
| *Verwijderen*  |      |
| - voorwaarde   | nvt.         |
| - gevolg       | nvt.             |
| *Raadplegen*   |      |
| - voorwaarde   | Om ROLTYPE informatie op te kunnen vragen moet de consumer de UUID van de CATALOGUS en de UUID van het ZAAKTYPE waarin het ROLTYPE is opgenomen weten. Deze UUIDs kunnen opgevraagd worden met de catalogus bevragingen services en zaaktype bevragingen services.         |
| - gevolg       | Een (lijst met) ROLTYPE informatie van het ZAAKTYPE wordt teruggegeven aan de consumer.             |
| Gegevens       | ROLTYPE <br>Zie de volgende tabel voor de gegevens van deze resource                                 |
| Specificaties  | https://ref.tst.vng.cloud/ztc/api/v1/schema/#tag/roltype                                                                                                   |
| Samenhang      | - |
| Bijzonderheden | Generieke aanduiding van de aard van een ROL die een BETROKKENE kan uitoefenen in ZAAKen van een ZAAKTYPE.       |

       
### Resource: STATUSTYPE

| **Aspect**     | **Beschrijving**                                                                                                                                                                 |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aanleiding     | Een consumer wil alle STATUSTYPEn van een ZAAKTYPE zoals opgenomen in de CATALOGUS van de organisatie opvragen.           |
| *Toevoegen*    |      |
| - voorwaarde   | nvt.         |
| - gevolg       | nvt.             |
| *Wijzigen*     |      |
| - voorwaarde   | nvt.         |
| - gevolg       | nvt.             |
| *Verwijderen*  |      |
| - voorwaarde   | nvt.         |
| - gevolg       | nvt.             |
| *Raadplegen*   |      |
| - voorwaarde   | Om STATUSTYPE informatie op te kunnen vragen moet de consumer de UUID van de CATALOGUS en de UUID van het ZAAKTYPE waarin het STATUSTYPE is opgenomen weten. Deze UUIDs kunnen opgevraagd worden met de catalogus bevragingen services en zaaktype bevragingen services.         |
| - gevolg       | Een (lijst met) STATUSTYPE informatie van het ZAAKTYPE wordt teruggegeven aan de consumer.             |
| Gegevens       | STATUSTYPE <br>Zie de volgende tabel voor de gegevens van deze resource                                 |
| Specificaties  | https://ref.tst.vng.cloud/ztc/api/v1/schema/#tag/statustype                                                                                                   |
| Samenhang      | [beschrijving van de samenhang met andere resources, bijvoorbeeld dat een andere resource eerst uitgevoerd moet worden om gegevens te verkrijgen waarmee deze resource aangeroepen kan worden] |
| Bijzonderheden | Generieke aanduiding van de aard van een STATUS           |

