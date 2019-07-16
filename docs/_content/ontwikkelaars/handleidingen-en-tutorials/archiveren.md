---
title: "Tutorial archiveren"
weight: 30
---

In deze tutorial configureren we de referentieimplementatie van de
Zaaktypecatalogus (ZTC) zodat Zaken in het Zaakregistratiecomponent (ZRC)
juist worden aangemaakt en voorzien worden van de juiste meta attributen zodat
archivering mogelijk is.

De tutorial is hands-on - onderaan vind je verdere referenties en bronnen
indien je meer wil lezen.

De volgende componenten zijn meest relevant:

* ZTC: voor het configureren van zaaktypen
* ZRC: voor het opslaan van zaken

## Wat zijn de vereisten voor deze tutorial?

* `docker` en `docker-compose` om lokaal op je (ontwikkelmachine) de
  componenten te hosten. Zie ['installatie en configuratie'](./installatie-en-configuratie) voor een
  uitgebreide beschrijving.

* Het handigste is om de containers in 1 command prompt te hebben draaien, en
  extra commando's in een tweede prompt ernaast uit te voeren. Zorg dat beide
  prompts zich in de juiste directory bevinden: `/pad/naar/gemma-zaken/infra`.

* De [eenmalige setup](./eenmalige-setup) is uitgevoerd.

* Toegang tot de publieke [VNG Referentielijsten API].

## Aan de slag

### Configuratie van de ZTC

Het IP-adres uit de ['installatie en configuratie'](./installatie-en-configuratie) voorbereiding is hier
nodig om de componenten via de browser aan te spreken.

Open in je browser `http://<ztc-ip>:8002/admin/` en log in met je
gebruikersnaam en wachtwoord.

#### Catalogus aanmaken

Een catalogus fungeert als een verzameling voor alle Zaaktypen bij een
gemeente.

1. Navigeer naar **Catalogussen** en klik op **Toevoegen**.

2. Vul alle verplichte velden in.

   De daadwerkelijke informatie is voor nu niet relevant.

3. Klik op **Opslaan en opnieuw bewerken**.

#### Zaaktype aanmaken

We definieren 1 zaaktype dat is gebaseerd op een procestype uit de
[Selectielijst gemeenten] die ontsloten wordt middels de
[VNG Referentielijsten API].

1. Klik op **Voeg een Zaaktype toe**. Of navigeer naar **Zaaktypen** en klik
   op **Toevoegen**.

2. Vul alle verplichte velden in maar hanteer voor onderstaande velden de
   volgende waarden:

   * **Omschrijving**: Melding Openbare Ruimte
   * **Doorlooptijd behandeling**: 30 00:00:00
   * **Versiedatum**: 01-01-2019
   * **Maakt deel uit van**: `<de catalogus uit de stap hierboven>`
   * **Datum begin geldigheid**: 01-01-2019
   * **Selectielijst procestype**: https://referentielijsten-api.vng.cloud/api/v1/procestypen/3030daa1-d516-4cd9-8276-ef0977e32b20

   De ingevulde URL bij *Selectielijst procestype* verwijst naar het
   procestype *Verzoeken behandelen*. Deze API is overigens zonder
   autorisatie door iedereen te raadplegen:

   > ```http
   > GET https://referentielijsten-api.vng.cloud/api/v1/procestypen/3030daa1-d516-4cd9-8276-ef0977e32b20 HTTP/1.0
   >
   > {
   >   "nummer": 6,
   >   "naam": "Verzoeken behandelen",
   >   "omschrijving": "Het behandelen van een verzoek tot het doen of laten van het orgaan"
   > }
   > ```
   > *\- Deel van de API resource `procestype` (Selectielijst procestype) response*

3. Klik op **Opslaan en opnieuw bewerken**.

#### Resultaattype aanmaken

1. Klik op **Voeg een Resultaattype toe**. Of navigeer naar **Resultaattypen**
   en klik op **Toevoegen**.

2. Vul alle verplichte velden in maar hanteer voor onderstaande velden de
   volgende waarden:

   * **Is relevant voor**: `<het zaaktype uit de stap hierboven>`
   * **Omschrijving**: Afgewezen
   * **Resultaattypeomschrijving**: https://referentielijsten-api.vng.cloud/api/v1/resultaattypeomschrijvingen/e6a0c939-3404-45b0-88e3-76c94fb80ea7
   * **Selectielijstklasse**: https://referentielijsten-api.vng.cloud/api/v1/resultaten/65559080-1d2b-4ddf-8966-b620e4ec224e
   * **Afleidingswijze brondatum**: Afgehandeld
   * **Datum begin geldigheid**: 01-01-2019

   De ingevulde URL bij *Selectielijstklasse* verwijst naar het archiefregime
   dat aangeeft dat een zaak van dit zaaktype na 1 jaar vernietigd moet
   worden, indien dit resultaat aan de betreffende zaak wordt gegeven:

   > ```http
   > GET https://referentielijsten-api.vng.cloud/api/v1/resultaten/65559080-1d2b-4ddf-8966-b620e4ec224e HTTP/1.0
   >
   > {
   >   "naam": "Afgewezen",
   >   "waardering": "vernietigen",
   >   "procestermijn": "nihil",
   >   "bewaartermijn": "P1Y"
   > }
   > ```
   > *\- Deel van de API resource `resultaten` (Selectielijstklasse) response*

   De *Afleidingswijze brondatum* kan alleen gezet worden op "Afgehandeld". De
   *Selectielijstklasse* geeft aan dat de `procestermijn` `nihil` is, wat
   betekent dat na eindigen van de zaak (de zaak eindatum) er alleen rekening
   hoeft worden gehouden met de `bewaartermijn` van 1 jaar. Er is geen andere
   eigenschap, of hoofdzaak, etc. die van belang zijn om de brondatum te
   bepalen.

   De *Resultaattypeomschrijving* is alleen een geniereke omschrijving zoals
   deze standaard wordt gehanteerd en voor het archiveren zelf niet relevant.

3. Klik op **Opslaan**.

   We zijn voor nu klaar met het configureren van de ZTC.

#### Statustypen aanmaken

We maken 2 Statustypen aan, één als initiële status (nieuw), en één om de Zaak
af te sluiten (afgerond).

1. Navigeer naar **Statustypen** en klik op **Toevoegen**.

2. Vul alle verplichte velden in maar hanteer voor onderstaande velden de
   volgende waarden:

   * **Omschrijving**: Nieuw
   * **Is van**: `<het zaaktype uit de stap hierboven>`
   * **Datum begin geldigheid**: 01-01-2019

3. Klik op **Opslaan en nieuwe toevoegen**.

4. Vul alle verplichte velden in maar hanteer voor onderstaande velden de
   volgende waarden:

   * **Omschrijving**: Afgerond
   * **Is van**: `<het zaaktype uit de stap hierboven>`
   * **Datum begin geldigheid**: 01-01-2019

5. Klik op **Opslaan**.


### Zaak afhandelen

Dit deel gaan we doen op basis van de API. Je kunt bijvoorbeeld [Postman]
gebruiken, of een andere applicatie om met de ZTC en ZRC API te communiceren.

#### ZTC configuratie opvragen

In het eerste deel hebben we een Zaaktype aangemaakt. We hebben de URL hiervan
nodig om een Zaak aan te maken, samen met enkele andere URLs uit het ZTC die
fungeren als de unieke identificatie van verschillende typen.

1. Haal de Catalogussen op:

   ```http
   GET http://<ztc-ip>:8002/api/v1/catalogussen HTTP/1.0
   Authorization: Bearer abcd1234
   ```

   *Voorbeeld antwoord*

   ```json
   [
       {
           "url": "<catalogus url>",
           "domein": "DEMO",
           "rsin": "123456782",
           "contactpersoonBeheerNaam": "VNG API-lab",
           "contactpersoonBeheerTelefoonnummer": "+31 (0)20 123 45 67",
           "contactpersoonBeheerEmailadres": "vngapilab@example.com",
           "zaaktypen": [
               "<zaaktype url>"
           ],
           "besluittypen": [],
           "informatieobjecttypen": []
       }
   ]
   ```

2. Uit de response kunnen we het aangemaakt Zaaktype halen. Hiervan vragen we
   de details op

   ```http
   GET <zaaktype-url> HTTP/1.0
   Authorization: Bearer abcd1234
   ```

   *Voorbeeld (deel van) antwoord*

    ```json
    {
       "url": "<zaaktype-url>",
       "catalogus": "<catalogus url>",
       "omschrijving": "Melding Openbare Ruimte",
       "doorlooptijd": "P30D",
       "selectielijstProcestype": "https://referentielijsten-api.vng.cloud/api/v1/procestypen/3030daa1-d516-4cd9-8276-ef0977e32b20",
       "statustypen": [
           "<statustype nieuw url>",
           "<statustype afgerond url>"
       ],
       "resultaattypen": [
           "<resultaattype url>"
       ]
    }
    ```

3. Uit de response kunnen we de relevante Statustypen en Resultaattypen halen.

   We hebben nu de volgende unieke URLs die we nodig hebben bij het afhandelen
   van een zaak. Deze gebruiken we bij de volgende stappen:

   * `zaaktype url`
   * `statustype nieuw url`
   * `statustype afgerond url`
   * `resultaattype url`

#### Zaak aanmaken

1. Maak een Zaak aan:

   ```http
   POST http://<zrc-ip>:8000/api/v1/zaken HTTP/1.0
   Authorization: Bearer abcd1234
   Accept-Crs: EPSG:4326
   Content-Crs: EPSG:4326
   Content-Type: application/json

   {
       "bronorganisatie": "509381406",
       "omschrijving": "API-lab zaak test",
       "zaaktype": "<zaaktype url>",
       "verantwoordelijkeOrganisatie": "245122461",
       "startdatum": "2019-04-17",
       "toelichting": "Fiets in de Keizersgracht voorkomt dat rondvaartboot kan passeren."
   }
   ```

   Het antwoord bevat o.a. de `url` van de zojuist aangemaakt Zaak. We
   refereren hiernaar middels `zaak url`.

2. Zet de initiele Status van de Zaak:

   ```http
   POST http://<zrc-ip>:8000/api/v1/statussen HTTP/1.0
   Authorization: Bearer abcd1234
   Content-Type: application/json

   {
       "zaak": "<zaak url>",
       "statusType": "<statustype nieuw url>",
       "statustoelichting": "Zaak aangemaakt door burger."
   }
   ```

#### Zaak afronden

1. Voordat we de Zaak gaan afronden, bekijken we de Zaak zoals deze in het ZRC
   aanwezig is. Uiteraard bevat deze de gegevens zoals we deze hebben
   verstuurd maar we focussen nu op enkele andere attributen:

   ```http
   GET <zaak_url> HTTP/1.0
   Authorization: Bearer abcd1234
   Accept-Crs: EPSG:4326
   ```

   *Voorbeeld (deel van) antwoord*

   ```json
   {
       "url": "<zaak url>",
       "identificatie": "3ce2848b-df34-44ae-8e10-dc12d6a69417",

       "bronorganisatie": "509381406",
       "omschrijving": "API-lab zaak test",
       "zaaktype": "<zaaktype url>",
       "verantwoordelijkeOrganisatie": "245122461",
       "startdatum": "2019-04-17",
       "toelichting": "Fiets in de Keizersgracht voorkomt dat rondvaartboot kan passeren.",

       "einddatum": null,
       "selectielijstklasse": "",
       "status": "<status url>",
       "archiefnominatie": null,
       "archiefstatus": "nog_te_archiveren",
       "archiefactiedatum": null,
       "resultaat": null
    }
    ```

    De Zaak heeft op dit moment geen `einddatum`, `archiefnominatie` of
    `archiefactiedatum`. Deze laatste is de datum waarop de actie bij
    `archiefnominatie` moet plaatsvinden.

2. De Zaak moet voorzien worden van een Resultaat. Door een Resultaat aan de
   Zaak te hangen, wordt het Resultaattype bekend en kan het archiefregime
   bij het afsluiten van de zaak worden toegepast.

   ```http
   POST http://<zrc-ip>:8000/api/v1/resultaten HTTP/1.0
   Authorization: Bearer abcd1234
   Content-Type: application/json

   {
       "zaak": "<zaak url>",
       "resultaatType": "<resultaattype url>",
       "toelichting": "Zaak beoordeeld en is reeds opgelost."
   }
   ```

3. Zet de laatste Status van de Zaak, waarmee de Zaak wordt gesloten:

   ```http
   POST http://<zrc-ip>:8000/api/v1/statussen HTTP/1.0
   Authorization: Bearer abcd1234
   Content-Type: application/json

   {
       "zaak": "<zaak url>",
       "statusType": "<statustype afgerond url>",
       "statustoelichting": "Zaak afgerond door ambtenaar."
   }
   ```

   Na het afsluiten van de Zaak wordt de `einddatum` van de Zaak gezet. Ook
   wordt de `archiefactiedatum` berekend en `archiefnominatie` overgenomen uit
   het Resultaatttype.

4. We vragen nogmaals de Zaak details op om de gewijzigde attributen van stap
   1 door te nemen:

   ```http
   GET <zaak_url> HTTP/1.0
   Authorization: Bearer abcd1234
   Accept-Crs: EPSG:4326
   ```

   *Voorbeeld (deel van) antwoord*

   ```json
   {
       "url": "<zaak url>",
       "identificatie": "3ce2848b-df34-44ae-8e10-dc12d6a69417",

       "bronorganisatie": "509381406",
       "omschrijving": "API-lab zaak test",
       "zaaktype": "<zaaktype url>",
       "verantwoordelijkeOrganisatie": "245122461",
       "startdatum": "2019-04-17",
       "toelichting": "Fiets in de Keizersgracht voorkomt dat rondvaartboot kan passeren.",

       "einddatum": "2019-04-17",
       "selectielijstklasse": "",
       "status": "<status url>",
       "archiefnominatie": "vernietigen",
       "archiefstatus": "nog_te_archiveren",
       "archiefactiedatum": "2020-04-17",
       "resultaat": "<resultaat url>"
    }
    ```

    Hier zien we dat alle relevante attributen zijn gezet om de Zaak op 4
    april 2020 te vernietigen. Dat is 1 jaar na de einddatum, zoals opgegeven
    in het ZTC.


### Samenvatting

We hebben het volgende gedaan in de ZTC:

* Catalogus aangemaakt;
* Zaaktype "Melding Openbare Ruimte" aangemaakt in de Catalogus, gebaseerd op
  procestype "Verzoeken behandelen" uit de [Selectielijst gemeenten];
* Resultaattype "Afgewezen" aangemaakt die binnen het procestype
  "Verzoeken behandelen" ook "Afgewezen" representeert en een bewaartermijn
  van 1 jaar voorschrijft, waarna de zaak vernietigd mag worden.

Hierna hebben we een Zaak afgehandeld:

* Een Zaak aangemaakt van Zaaktype "Melding Openbare Ruimte";
* Eerste Status op de Zaak gezet;
* Het Resultaat op de Zaak gezet die een koppeling legt met het Resultaattype;
* Laatste Status op de Zaak gezet waardoor de Zaak werd afgesloten en de
  `archiefactiedatum` werd berekend.


## Achtergrondinformatie

De [achtergronddocumentatie over archiveren](/themas/achtergronddocumentatie/archiveren) bevat meer informatie over andere scenario's bedoeld om de `archiefactiedatum` te bepalen.

[Hier](./_assets/archiveren.pptx) is de presentatie te vinden die gegeven is op het
API-lab.

[Selectielijst gemeenten]: https://vng.nl/selectielijst
[VNG Referentielijsten API]: https://referentielijsten-api.vng.cloud/api/v1/
[Postman]: https://www.getpostman.com/downloads/
