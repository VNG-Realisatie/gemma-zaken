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


### Resource: enkelvoudiginformatieobjecten


| **Aspect**     | **Beschrijving**                                                                                                                                                                 |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aanleiding     | Een consumer wil (een lijst van) enkelvoudige informatieobjecten opvragen uit of een enkelvoudig informatieobject toevoegen aan de documentregistratiecomponent DRC.            |
| *Toevoegen*    |      |
| - voorwaarde   | Het enkelvoudg document dient beschikbaar te zijn voordat dit toegevoegd kan worden aan de DRC         |
| - gevolg       | Na het succesvol toevoegen wordt een URI naar het enkelvoudg document teruggeven aan de comsumer.             |
| *Wijzigen*     |      |
| - voorwaarde   | nv.         |
| - gevolg       | nvt.             |
| *Verwijderen*  |      |
| - voorwaarde   | nvt.         |
| - gevolg       | nvt.             |
| *Raadplegen*   |      |
| - voorwaarde   | Bij het opvragen van een lijst met enkelvoudiginformatieobjecten geen voorwaarden.<br/> Bij het opvragen van een specifiek enkelvoudg informatieobject moet de uri waarmee het informatieobject opgevraagd kan worden door de consumer aangeleverd worden.     |
| - gevolg       | Bij het vragen van een lijst wordt een lijst URI's, waarmee de informatieobjecten opgraagd kunnen worden, geretourneerd.<br/> Bij het opvragen van een enkelvoudg informatieobject wordt dit zoals opgeslagen in de DRC worden teruggegeven. |
| Gegevens       | Enkelvoudige informatieobjecten <br>Zie de volgende tabel voor de gegevens van deze resource                                 |
| Specificaties  | https://ref.tst.vng.cloud/drc/api/v1/schema/#tag/enkelvoudiginformatieobjecten   | 
| Samenhang      | nvt. |
| Bijzonderheden | Enkelvoudig Informatieobject is een subtype van Informatieobject. Beide objecttypen zijn "platgeslagen" zodat de eigenschappen 
van Informatieobject opgenomen zijn in het enkelvoudiginformatieobjecttype.  |



### Resource: zaakinformatieobjecten


| **Aspect**     | **Beschrijving**                                                                                                                                                                 |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aanleiding     | Een consumer wil (een lijst van) zaakinformatieobjecten opvragen uit of een zaakinformatieobject toevoegen aan de documentregistratiecomponent DRC.            |
| *Toevoegen*    |      |
| - voorwaarde   | Zowel de uri waarmee de zaak als de uri waarmee het informatieobject geïdentificeerd kan worden moeten bekend zijn bij de consumer         |
| - gevolg       | Na het toevoegen van een zaakinformatieobject is het informatieobject gekoppeld aan een zaak.|
| *Wijzigen*     |      |
| - voorwaarde   | nvt.         |
| - gevolg       | nvt.             |
| *Verwijderen*  |      |
| - voorwaarde   | nvt.         |
| - gevolg       | nvt.             |
| *Raadplegen*   |      |
| - voorwaarde   | Bij het opvragen van een lijst met zaakinformatieobjecten geen voorwaarden.<br/> Bij het opvragen van een specifiek zaakinformatieobject moet de uri waarmee het zaakinformatieobject opgevraagd kan worden door de consumer aangeleverd worden.         |
| - gevolg       | Bij het vragen van een lijst wordt een lijst URI's, waarmee de zaakinformatieobjecten opgraagd kunnen worden, geretourneerd.<br/> Bij het opvragen van een zaakinformatieobject wordt dit zoals opgeslagen in de DRC worden teruggegeven.             |
| Gegevens       | Zaakinformatieobjecten  <br>Zie de volgende tabel voor de gegevens van deze resource                                 |
| Specificaties  | https://ref.tst.vng.cloud/drc/api/v1/schema/#tag/zaakinformatieobjecten   |
| Samenhang      | Om een zaakinformatieobject toe te voegen dienen eerst zowel de zaak als het enkelvoudiginoformatieobject toegevoegd te worden. |
| Bijzonderheden | nvt.  |
