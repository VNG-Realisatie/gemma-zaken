INFORMATIEOBJECTEN  API
==========
**FUNCTIONELE DOCUMENTATIE**


| **Aspect**      | **Beschrijving**                                                                                                                                                                       |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Doel            | Het opvragen van (lijsten van) enkelvoudige informatieobjecten en/of zaakinformatieobjecten |
| Domein          | Zaakgericht werken.                                                                                             |
| Provider        | [Documentregistratiecomponent](https://www.gemmaonline.nl/index.php/GEMMA2/0.9/id-0e99ec6c-283a-4ec9-8efa-e11468e6b878) |
| Consumer        | [Documentbeheercomponent](https://www.gemmaonline.nl/index.php/GEMMA2/0.9/id-25ee9ea7-be66-4bdd-b40c-191777a88b35)  |
| Informatiemodel | RGBZ2  |
| Specificaties   | https://ref.tst.vng.cloud/drc/api/v1/schema/ |
| Bijzonderheden  | - |

Deze API omvat (vooralsnog) de resources Enkelvoudiginformatieobject en Zaakinformatieobject.

Elke resource biedt de mogelijkheid om objecten toe te voegen (POST) en te raadplegen (GET), tenzij anders vermeld.


### Resource: Enkelvoudiginformatieobjecten


| **Aspect**     | **Beschrijving**                                                                                                                                                                 |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aanleiding     | Een consumer wil weten welke informatieobjecten bij een object horen uit of een enkelvoudiginformatieobject toevoegen aan de documentregistratiecomponent DRC.            |
| *Toevoegen*    |      |
| - voorwaarde   | Het enkelvoudiginformatieobject dient beschikbaar te zijn voordat dit toegevoegd kan worden aan de DRC         |
| - gevolg       | Na het succesvol toevoegen wordt een verwijzing in de vorm van een URI naar het enkelvoudiginformatieobject teruggeven aan de comsumer.             |
| Specificaties  | https://ref.tst.vng.cloud/drc/api/v1/schema/#operation/enkelvoudiginformatieobject_create   | 
| *Wijzigen*     | Nog niet beschikbaar.     |
| - voorwaarde   | Nog te bepalen.         |
| - gevolg       | Nog te bepalen.             |
| *Verwijderen*  | Nog niet beschikbaar.     |
| - voorwaarde   | Nog te bepalen.         |
| - gevolg       | Nog te bepalen.             |
| *Raadplegen lijst*   |      |
| - voorwaarde   | Geen voorwaarden.  |
| - gevolg       | Een overzicht van in de Documentregistratiecomponent opgeslagen informatieobjecten wordt geretourneerd. Het is mogelijk te filteren op de volgende gegevens:<br/><ul><li>Object: URL naar het gerelateerde OBJECT waar alle INFORMATIEOBJECTEN aan gerelateerd zijn.</li><li>Informatieobject: URL naar het gerelateerde INFORMATIEOBJECT waar alle OBJECTEN aan gerelateerd zijn.</li></ul>|
| Specificaties  | https://ref.tst.vng.cloud/drc/api/v1/schema/#operation/enkelvoudiginformatieobject_list   | 
| *Raadplegen details*   |      |
| - voorwaarde   | Bij het opvragen van een specifiek enkelvoudiginformatieobject moet de identificatie van het informatieobject door de consumer aangeleverd worden.     |
| - gevolg       | Een enkelvoudiginformatieobject geïdentificeerd door de aangeleverde identificatie wordt geretourneerd. |
| Gegevens       | Objecttype ENKELVOUDIGINFORMATIEOBJECT inclusief relatie naar INFORMATIEOBJECTTYPE.<br>Zie de volgende tabel voor de gegevens van deze resource                                 |
| Specificaties  | https://ref.tst.vng.cloud/drc/api/v1/schema/#operation/enkelvoudiginformatieobject_read   | 
| Samenhang      | - |
| Bijzonderheden | EnkelvoudigInformatieobject is een subtype van Informatieobject. Beide objecttypen zijn "platgeslagen" zodat met het opvragen van een enkelvoudiginformatieobject ook de eigenschappen van het type informatieobject geretourneerd worden.
|



### Resource: Objectinformatieobjecten


| **Aspect**     | **Beschrijving**                                                                                                                                                                 |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aanleiding     | Een consumer wil objectinformatieobjecten opvragen uit of een objectinformatieobject toevoegen aan de documentregistratiecomponent DRC.            |
| *Toevoegen*    |      |
| - voorwaarde   | Zowel de verwijzing (URI) waarmee het object als de verwijzing (URI) waarmee het informatieobject geïdentificeerd kunnen worden moeten aangeleverd worden door de consumer.         |
| - gevolg       | Na het toevoegen van een objectinformatieobject is het informatieobject gekoppeld aan een ander object, zoals een zaak of een besluit.|
| Specificaties  | https://ref.tst.vng.cloud/drc/api/v1/schema/#operation/objectinformatieobject_create   |
| *Wijzigen*     | Nog niet beschikbaar.     |
| - voorwaarde   | Nog te bepalen.         |
| - gevolg       | Nog te bepalen.             |
| *Verwijderen*  | Nog niet beschikbaar.     |
| - voorwaarde   | Nog te bepalen.         |
| - gevolg       | Nog te bepalen.             |
| *Raadplegen lijst*   |      |
| - voorwaarde   | Geen voorwaarden   |
| - gevolg       | Een overzicht van in de Documentregistratiecomponent opgeslagen objectinformatieobjecten wordt geretourneerd. |
| Specificaties  | https://ref.tst.vng.cloud/drc/api/v1/schema/#operation/objectinformatieobject_list   |
| *Raadplegen detail*   |      |
| - voorwaarde   | Bij het opvragen van een specifiek objectinformatieobject moet de identificatie van het objectinformatieobject door de consumer aangeleverd worden.         |
| - gevolg       | Het objectinformatieobject gedentificeerd door de aangeleverde identificatie wordt geretourneerd.             |
| Gegevens       | Objecttype OBJECTINFORMATIEOBJECT inclusief relaties naar INFORMATIEOBJECT en OBJECTTYPE.<br>Zie de volgende tabel voor de gegevens van deze resource                                 |
| Specificaties  | https://ref.tst.vng.cloud/drc/api/v1/schema/#operation/objectinformatieobject_read   |
| Samenhang      | Om een objectinformatieobject toe te voegen dienen zowel het object als het enkelvoudiginformatieobject te bestaan. |
| Bijzonderheden | -  |
