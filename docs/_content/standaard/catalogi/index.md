---
title: "Catalogi API"
date: '5-7-2022'
weight: 10
---

API voor opslag en ontsluiting van zaaktype-catalogi, zaaktypen en onderliggende typen.

De API ondersteunt het opslaan en naar andere applicaties ontsluiten van zaaktype-catalogi met zaaktypen. Deze gegevens kunnen door applicaties worden gebruikt om voor zaken van een bepaald type de juiste gegevens (statustypen, resultaattypen, informatieobjecttypen, etc.) te bepalen. Applicaties die gebruik maken van deze zaaktypegegevens zijn bijvoorbeeld een zaakafhandelcomponent, een VTH-applicatie of een subsidie-applicatie. Opslag van zaaktypegegevens vindt plaats conform het informatiemodel ZTC.


## Gegevensmodel

[![Gegevensmodel Catalogi API](Catalogi API.png)](Catalogi API.png "Catalogi gegevensmodel - klik voor groot")


## Specificatie van de Catalogi API

* [Referentie-implementatie Catalogi API](https://catalogi-api.vng.cloud)
* API specificatie (OAS3) in
  [ReDoc](https://catalogi-api.vng.cloud/api/v1/schema/),
  [Swagger](https://petstore.swagger.io/?url=https://catalogi-api.vng.cloud/api/v1/schema/openapi.yaml),
  [YAML](https://catalogi-api.vng.cloud/api/v1/schema/openapi.yaml) of
  [JSON](https://catalogi-api.vng.cloud/api/v1/schema/openapi.json)


## Specificatie van gedrag

Zaaktypecatalogi (ZTC) MOETEN aan twee aspecten voldoen:

* de ZTC `openapi.yaml` MOET volledig geïmplementeerd zijn.

* het run-time gedrag beschreven in deze standaard MOET correct geïmplementeerd
  zijn.

Het ZTC haalt informatie uit selectielijsten en de Gemeentelijke Selectielijst
2017. Deze gegevens worden ontsloten in de
[VNG-referentielijsten-API](https://referentielijsten-api.vng.cloud/api/v1/schema/). Op
korte termijn zal deze API gesplitst worden in een referentielijsten-API en de
selectielijst-API (waar deze nu nog 1 API is)
[#3 on Github](https://github.com/VNG-Realisatie/VNG-referentielijsten/issues/3).


## OpenAPI specificatie

Alle operaties beschreven in [`openapi.yaml`](../../../api-specificatie/ztc/1.0.x/openapi.yaml)
MOETEN ondersteund worden en tot hetzelfde resultaat leiden als de
referentie-implementatie van het ZTC.

Het is NIET TOEGESTAAN om gebruik te maken van operaties die niet beschreven
staan in deze OAS spec, of om uitbreidingen op operaties in welke vorm dan ook
toe te voegen.

### Run-time gedrag

Bepaalde gedrageningen kunnen niet in een OAS spec uitgedrukt worden omdat ze
businesslogica bevatten. Deze gedragingen zijn hieronder beschreven en MOETEN
zoals beschreven geïmplementeerd worden.

#### **<a name="ztc-001">Valideren van `Zaaktype` ([ztc-001](#ztc-001))</a>**

Het attribuut `Zaaktype.selectielijstProcestype` MOET een URL-verwijzing naar
de `Procestype` resource in de selectielijst-API zijn, indien ingevuld.

#### **<a name="ztc-002">Valideren van `Resultaattype` ([ztc-002](#ztc-002))</a>**

Het attribuut `Resultaattype.resultaattypeomschrijving` MOET een URL-verwijzing
naar de `Resultaattypeomschrijving` resource in de referentielijsten-API zijn.
Het ZTC MOET de waarde van `Resultaattypeomschrijving.omschrijving` ontsluiten
(uit de selectielijst) als alleen-lezen attribuut
`Resultaattype.omschrijvingGeneriek`.

Het attribuut `Resultaattype.selectielijstklasse` MOET een URL-verwijzing zijn
naar de `Resultaat` resource in de selectielijst-API. Tevens MOET dit
`resultaat` horen bij het `procestype` geconfigureerd op
`Resultaattype.zaaktype.selectielijstProcestype`.

Indien `Resultaattype.archiefnominatie` niet expliciet opgegeven wordt, dan
MOET het ZTC deze afleiden uit `Resultaat.waardering` van de
selectielijstklasse.

Indien `Resultaattype.archiefactietermijn` niet expliciet opgegeven wordt, dan
MOET het ZTC deze afleiding uit `Resultaat.bewaartermijn` van de
selectielijstklasse.

**`Resultaattype.brondatumArchiefprocedure`**

Het groepattribuut `Resultaattype.brondatumArchiefprocedure` parametriseert
het bepalen van de `brondatum` voor de `archiefactietermijn` van een zaak. Deze
parametrisering is aan validatieregels onderhevig:

* <a name="ztc-003">`Resultaattype.brondatumArchiefprocedure.afleidingswijze` ([ztc-003](#ztc-003))</a>:
    * afleidingswijze MOET `afgehandeld` zijn indien de selectielijstklasse
      als procestermijn `nihil` heeft
    * afleidingswijze MOET `termijn` zijn indien de selectielijstklasse
      als procestermijn `ingeschatte_bestaansduur_procesobject` heeft

* <a name="ztc-004">`Resultaattype.brondatumArchiefprocedure.datumkenmerk` ([ztc-004](#ztc-004))</a>
    * MOET een waarde hebben als de afleidingswijze `eigenschap`, `zaakobject`
      of `ander_datumkenmerk` is
    * MAG GEEN waarde hebben in de andere gevallen

* <a name="ztc-005">`Resultaattype.brondatumArchiefprocedure.einddatumBekend` ([ztc-005](#ztc-005))</a>
    * MAG GEEN waarde hebben indien de afleidingswijze `afgehandeld` of
      `termijn` is

* <a name="ztc-006">`Resultaattype.brondatumArchiefprocedure.objecttype` ([ztc-006](#ztc-006))</a>
    * MOET een waarde hebben als de afleidingswijze `zaakobject`
      of `ander_datumkenmerk` is
    * MAG GEEN waarde hebben in de andere gevallen

* <a name="ztc-007">`Resultaattype.brondatumArchiefprocedure.registratie` ([ztc-007](#ztc-007))</a>
    * MOET een waarde hebben indien de afleidingswijze `ander_datumkenmerk` is
    * MAG GEEN waarde hebben in de andere gevallen

* <a name="ztc-008">`Resultaattype.brondatumArchiefprocedure.procestermijn` ([ztc-008](#ztc-008))</a>
    * MOET een waarde hebben indien de afleidingswijze `termijn` is
    * MAG GEEN waarde hebben in de andere gevallen

Als er geen procestermijn gezet is (lege waarde), wat typisch het geval is als
de archiefactie `bewaren` betreft, dan MOETEN alle waardes voor de 
afleidingswijze mogelijk zijn. De procestermijn kan voor praktische redenen
geïnterpreteerd worden als de waarde 0.


#### Concepten

De resources `Zaaktype`, `InformatieObjecttype` en `Besluittype` bevatten het veld `concept`,
indien dit veld aangemerkt is als `true`, dan betreft het een niet-definitieve versie van
het objecttype. Deze versie mag niet buiten de Catalogi API gebruikt mag worden.
Dat betekent dat je geen zaken van een `ZaakType` dat niet definitief is, mag aanmaken.

Om de versie van een objecttype definitief te maken ("publiceren"), bestaat er een `publish` operatie.
Dit is de tegenhanger van het attribuut `concept`, dus na publiceren heeft `concept` de waarde `false`. De datum beginGeldigheid is reeds gezet bij het aanmaken en/of het eventueel aanpassen van de concept versie en bepaalt vanaf het moment van publiceren vanaf welke datum objecten van de gepubliceerde versie aangemaakt mogen worden. 

Het is dus mogelijk om een nieuwe versie van bijvoorbeeld een zaaktype aan te maken en deze te publiceren met een datum beginGeldigheid in de toekomst. Een dergelijke versie van een zaaktype kan dan niet meer gewijzigd worden (tenzij met een <a name="correctie">([correctie](#correctie))</a>) dus het verdient aanbeveling dit tot een minimum te beperken.. Daarnaast is het van belang de datum eindGeldigheid van de voorgaande versie van het object te zetten met een waarde die 1 dag minder is dan de datum beginGeldigeid van de gepubliceerde versie.

Bovendien gelden er beperkingen op verdere acties die uitgevoerd kunnen worden op dit objecttype en gerelateerde objecttype via de API.
* Beperkingen voor objecttypen met `concept=false` **<a name="ztc-009">([ztc-009](#ztc-009))</a>**:
    * Het objecttype mag NIET:
        * geheel bijgewerkt worden (PUT), m.u.v een <a name="correctie">([correctie](#correctie))</a>
        * deels bijgewerkt worden (PATCH), m.u.v. het bijwerken van enkel het attribuut `eindeGeldigheid` of een <a name="correctie">([correctie](#correctie))</a>
        * verwijderd worden (DELETE)

* Beperkingen voor objecttypen gerelateerd aan een objecttype met `concept=false` **<a name="ztc-010">([ztc-010](#ztc-010))</a>**:

<span style="padding: 0.2em 0.5em; border: solid 1px #EEEEEE; border-radius: 3px; background: #DDDFFF;">
    <strong>Aangepast in versie 1.2.0</strong>
</span><br/>
    * Het objecttype mag NIET:
        * geheel bijgewerkt worden (PUT) m.u.v een <a name="correctie">([correctie](#correctie))</a>
        * deels bijgewerkt worden (PATCH) of een <a name="correctie">([correctie](#correctie))</a>
        * verwijderd worden (DELETE)
    * Voor `ZaakType-InformatieObjectType` gelden bovenstaande regels **(ztc-010)** alleen in het geval waarbij zowel het `ZaakType`
    als het `InformatieObjectType` `concept=False` hebben


<span style="padding: 0.2em 0.5em; border: solid 1px #EEEEEE; border-radius: 3px; background: #DDDFFF;">
    <strong>Vervallen in versie 1.2.0</strong>
</span><br/>
<s>
* Beperkingen die gelden voor objecttypen die NIET gerelateerd zijn aan een objecttype met `concept=false` **<a name="ztc-011">([ztc-011](#ztc-011))</a>**:
    * Er mag GEEN nieuw objecttype aangemaakt worden met een relatie naar een objecttype met `concept=false` (create)
    * Er mag GEEN nieuwe relatie worden gelegd tussen een objecttype en een objecttype met `concept=false` (update, partial_update)
* Voor `ZaakType-InformatieObjectType` gelden bovenstaande regels **(ztc-011)** alleen in het geval waarbij zowel het `ZaakType`
als het `InformatieObjectType` `concept=False` hebben
</s><br/>

#### Publiceren van `ZaakType` **<a name="ztc-012">([ztc-012](#ztc-012))</a>**

<span style="padding: 0.2em 0.5em; border: solid 1px #EEEEEE; border-radius: 3px; background: #DDDFFF;">
    <strong>Vervallen in versie 1.2.0</strong>
</span><br/>
<s>
Een `ZaakType` mag alleen gepubliceerd worden als alle gerelateerde `BesluitType`n en `InformatieObjectType`n `concept=false`
hebben (dus gepubliceerd zijn). Als er geprobeerd wordt om een `ZaakType` te publiceren terwijl er relaties zijn met `BesluitType`n of `InformatieObjectType`n die `concept=true` hebben, dan dient er een HTTP 400 teruggegeven te worden door de API
</s><br/>


<span style="padding: 0.2em 0.5em; border: solid 1px #EEEEEE; border-radius: 3px; background: #DDDFFF;">
    <strong>Nieuw in versie 1.2.0</strong>
</span> 
De relaties tussen `Zaaktype`, `Besluittype` en `Zaaktype` worden gelegd middels de functionele attributen zaaktype.identificatie, informatieobjecttype.omschrijving en besluittype.omschrijving. Hiermee is de vaste relatie dmv. een url tussen versies van Zaaktype, Informatieobjecttype en Besluittype komen te vervallen. Het is dan ook niet meer noodzakelijk om bij een wijziging van bijvoorbeeld een zaaktype ook nieuwe versies van gerelateerde informatieobjecttypen en besluittypen te maken.

#### <a name="ztc-013">Relaties tussen objecttypen ([ztc-013](#ztc-013))</a>

Het is NIET TOEGESTAAN dat objecttypen relaties hebben over verschillende catalogi
heen. Zelfs als de catalogi hetzelfde zijn maar op verschillende endpoints
worden aangeboden mogen de relaties niet door elkaar gelegd worden.

Voorbeeld: Een `Zaaktype` in `Catalogus` X mag geen `Statustype` hebben uit
`Catalogus` Y. Een `Zaaktype` in `Catalogus` X op endpoint `https://www.foo.bar/`
mag geen `Statustype` hebben uit `Catalogus` X op endpoint
`https://www.example.com`.

### Historiemodel Catalogi API

<span style="padding: 0.2em 0.5em; border: solid 1px #EEEEEE; border-radius: 3px; background: #DDDFFF;">
    <strong>Nieuw in versie 1.2.0</strong>
</span>
In voorgaande versies van de Catalogi API waren versies van Zaaktypen, Informatieobjecttypen, Besluittypen, Roltypen, Statustypen, Eigenschappen, Resultaatypen etc. één op één aan elkaar gekoppeld. Dit had als nadeel dat een wijziging in één versie van een object (ongeacht welk) van alle gerelateerde objecten een nieuwe versie gemaakt worden. Dit is in de praktijk niet werkbaar gebleken. Daarom zijn de volgende wijzigingen in Catalogi API 1.2 van toepassing:

- Zaaktype, Informatieobjecttype en Besluittype kunnen onafhankelijk van elkaar gewijzigd worden. Dit is mogelijk door het leggen van relaties op basis van identificatie/omschrijving in plaats van een harde url naar een versie. 

Zaaktype ZAKABC20220101 heeft relevant Besluittype BESXYZ20220403
Wanneer van Zaaktype ZAKABC20220101 een nieuwe versie gemaakt wordt is Besluittype BESXYZ20220403 nog steeds relevant. De relatie is gelegd op basis van Besluittype.omschrijving en datumgeldigheid. 

- Wanneer van een Zaaktype een nieuwe versie wordt gemaakt hoeft er geen nieuwe versie van Roltype, Statustype, Eigenschap Zaakobjecttype en/of Resultaattype gemaakt te worden. In onderstaande uitleg wordt Roltype gebruikt maar hetzelfde geldt voor de overige typen.

De relatie wordt vanuit deze typen naar het Zaaktype gelegd via zaaktypeidentificatie. Op basis van roltype.zaaktypeidentificatie en roltype.beginGeldigheid <= zaaktype.beginGeldigheid <= roltype.eindGeldigheid wordt de juiste versie van het roltype opgehaald. Het is dus niet nodig om van elk gerelateerde objecttype de juiste versie expliciet op te halen.

De bestaande url verwijzing naar zaaktype blijft bestaan maar krijgt een andere betekenis: Het is de verwijzing naar de versie van het zaaktype waarmee deze versie van het roltype voor het eerst in gebruik genomen is. Dit in gebruik nemen is gebeurd met behulp van de bestaande publish operatie op Zaaktypen.

- Wanneer van een Roltype, Statustype, Eigenschap Zaakobjecttype en/of Resultaattype een nieuwe versie wordt gemaakt MOET er een nieuwe versie van Zaaktype gemaakt te worden. Reeds bestaande versies van roltypen etc. blijven geldig voor die nieuwe versie van het Zaaktype. In onderstaande uitleg wordt Roltype gebruikt maar hetzelfde geldt voor de overige typen.

Om een versie van een object in gebruik te nemen moet deze gepubliceerd worden. De publish operatie werkt op Zaaktypen, Informatieobjecttypen en Besluittypen. Om een versie van een roltype te publiceren moet de bijbehorende versie van het zaaktype gepubliceerd worden. 

### Datum beginGeldigheid en eindGeldigheid
<span style="padding: 0.2em 0.5em; border: solid 1px #EEEEEE; border-radius: 3px; background: #DDDFFF;">
    <strong>Nieuw in versie 1.2.0</strong>
</span>
Omdat een versie van Roltype, Statustype, Eigenschap, Zaakobjecttype en Resultaattype niet meer één op één aan een versie van een Zaaktype gekoppeld zijn zijn de attributen beginGeldigheid en eindGeldigheid ook aan die objecttypen toegevoegd. 

De betekenis van de attributen is:
beginGeldigheid  : De datum waarop de versie van het object geldig is geworden
eindGeldigheid : De laatste datum waarop de versie van het object geldig is. 

De versie van het object is dus geldig van beginGeldigheid *tot en met* eindGeldigheid. 

Daarnaast kennen objecten ook nog de datumvelden beginObject en eindObject. Dit zijn respectievelijk de geboortedatum en overlijdensdatum van het object. Oftewel de datum waarop het object voor het eerst gebruikt kon worden en de datum waarom het object voor het laatst gebruikt kon worden.

Om de juiste versie van bijvoorbeeld een roltype bij een zaaktype te vinden wordt gezocht op de versie van het roltype die op een datum geldig is (geweest) voor dat zaaktype. Een versie van een roltype kan aan slechts één versie van een zaaktype gekoppeld zijn. Door te zoeken op Roltypen met de queryparameters roltype.zaaktypeidentificatie = zaaktype.identificatie en roltype.beginGeldigheid <= zaaktype.beginGeldigheid <= roltype.eindGeldigheid

Bij het opvragen van een versie van een zaaktype worden de onderliggende objecten Roltype, Statustype, Eigenschap, Zaakobjecttype en Resultaattype op deze manier bij de versie gezocht. Met de url uit het resultaat kan de voor deze versie van het zaaktype geldige versie van de onderliggende objecten worden opgehaald. Het is dan dus niet meer nodig om nog te filteren op zaaktypeidentificatie en datum.

#### HTTP-Caching

<span style="padding: 0.2em 0.5em; border: solid 1px #EEEEEE; border-radius: 3px; background: #DDDFFF;">
    <strong>Nieuw in versie 1.1.0</strong>
</span>

De Catalogi API moet HTTP-Caching ondersteunen op basis van de `ETag` header. In
de API spec staat beschreven voor welke resources dit van toepassing is.

De `ETag` MOET worden berekend op de JSON-weergave van de resource.
Verschillende, maar equivalente weergaves (bijvoorbeeld dezelfde API ontsloten
wel/niet via NLX) MOETEN verschillende waarden voor de `ETag` hebben.

Indien de consumer een `HEAD` verzoek uitvoert op deze resources, dan MOET de
provider antwoorden met dezelfde headers als bij een normale `GET`, dus
inclusief de `ETag` header. Er MAG GEEN response body voorkomen.

Indien de consumer gebruik maakt van de `If-None-Match` header, met één of
meerdere waarden voor de `ETag`, dan MOET de provider antwoorden met een
`HTTP 304` bericht indien de huidige `ETag` waarde van de resource hierin
voorkomt. Als de huidige `ETag` waarde hier niet in voorkomt, dan MOET de
provider een normale `HTTP 200` response sturen.

#### <a name="correctie">([Correctie](#correctie))</a>

<span style="padding: 0.2em 0.5em; border: solid 1px #EEEEEE; border-radius: 3px; background: #DDDFFF;">
    <strong>Nieuw in versie 1.2.0</strong>
</span>
Het kan voorkomen dat een versie van een object in gebruik is en fouten bevat. Normaal gesproken moet dan van dat object een nieuwe versie gemaakt worden maar die wijzigingen hebben dan geen effect op zaken, informatieobjecten of besluiten die reeds aangemaakt zijn. Daarom is het mogelijk om onder bepaalde omstandigheden correcties aan te brengen. Dit kan dan met een expliciete scope: geforceerd-bijwerken.

De voorwaarden waaronder een correctie uitgevoerd mag worden zijn:
- De wijziging is een uitbreiding, bijvoorbeeld het toevoegen van een optioneel informatieobjecttype aan een zaaktype of een statustype aan het eind van de reeds geconfigureerde statustypen aan een zaaktype. Er mogen dus geen releaties of gerelateerde objecten verwijdjerd worden.
- Zaken van het zaaktype blijven nog steeds geldig en kunnen nog steeds afgehandeld worden. Met andere woorden, de afhandeling van deze zaken is nog steeds geldig.
- Besluiten van het Besluittype blijven nog steeds geldig.
- Informatieobjecten van het Informatieobjecttype blijven nog steeds geldig.

## Overige documentatie

* [Informatiemodel Zaaktypen (ImZTC)](https://www.gemmaonline.nl/index.php/Informatiemodel_Zaaktypen_(ImZTC))
