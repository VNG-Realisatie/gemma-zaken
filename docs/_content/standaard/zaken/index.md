---
title: "Zaken API"
date: '10-7-2019'
weight: 10
---

API voor het opslaan en ontsluiten van zaakgegevens.

De API ondersteunt het opslaan en het naar andere applicaties ontsluiten van gegevens over alle gemeentelijke zaken, van elk type. Opslag vindt plaats conform het RGBZ waarin objecten, gegevens daarvan en onderlinge relaties zijn beschreven. Het bevat echter niet alle gegevens uit het RGBZ: documenten worden bijv. opgeslagen in de Documenten API, besluiten in de Besluiten API, etc. Vanuit zaken worden er dan ook relaties gelegd naar andere resources.


## Gegevensmodel

De zaak vormt de kern van het zaakgericht werken. De omvang en afbakening worden bepaald door het traject van (aan)vraag tot (passend) antwoord. Een zaak komt daarmee overeen met een bedrijfsproces.

### Hoofd- en deel-zaken

Als een product of dienst via verschillende bedrijfsprocessen tot stand komt, wordt gewerkt met deelzaken. De hoofdzaak coördineert dat alle deelzaken samen leiden tot het (passende) antwoord op de (aan)vraag van de initiator.

### Relevante andere zaken

Soms heeft de ene zaak betrekking op een andere zaak, zoals een bezwaarzaak die volgt op een vergunningzaak.

Aan elkaar gerelateerde zaken (met elk hun eigen bedrijfsproces/aanleiding) worden vastgelegd als AndereRelevanteZaak. Dit zijn zowel zaken binnen dezelfde organisatie als van verschillende organisaties.

### Zaakobject

Elke zaak heeft ergens betrekking op wat is vastgelegd met de relatie naar zaakobject.  De, bij de ontwikkeling van de API's gebruikte, zaakobjecten (mor,  verblijfsobject, ...) kunnen als resource of m.b.v. identificerende gegevens worden opgenomen bij het zaakobject. Aangezien nog niet kan worden aangenomen dat deze vanuit de bron beschikbaar zijn.

### Betrokken en rollen

Ook heeft elke zaak één of meer betrokkenen, die via hun rol aan de zaak gerelateerd zijn.
De verschillende typen betrokkenen (medewerker, natuurlijk persoon, niet natuurlijk persoon en organisatieonderdeel), zijn nu opgenomen in de ZakenAPI. Aangezien nog niet kan worden aangenomen dat deze vanuit de bron beschikbaar zijn.

### Relatie met besluiten en documenten

Een besluit kan een uitkomst zijn van een zaak van de zaakbehandelende organisatie. Besluit heeft dan ook een optionele relatie met de zaak waarvan het een uitkomst is. Deze relatie wordt in de Zaken API vastgelegd in zaakbesluit.
Een informatieobject kan tot meer dan één zaak behoren en een zaak kan meer dan één informatieobjecten bevatten. De relatie tussen zaak en informatieobject is vastgelegd in zaakinformatieobject (Zaken API) en objectinformatieobject (Documenten API), waarbij zaakinformatieobject leidend is.

### Zaakdossier

Een zaak, met eventuele deelzaken dan wel de verwijzing naar de hoofdzaak, alle kenmerken, alle daaraan gerelateerde Informatieobjecten en alle andere gerelateerde gegevens (via rol, zaakobject, etc.) vormen gezamenlijk het zaakdossier.


[![Gegevensmodel Zaken API 1.0.0](Zaken API.png){:width="1200px"}](Zaken API.png "Zaken gegevensmodel - klik voor groot")

[![Gegevensmodel Zaken API 1.1.0](Zaken API 1.1.0.png){:width="1200px"}](Zaken API 1.1.0.png "Zaken gegevensmodel - klik voor groot")


### Zaakcontactmomenten

<span style="padding: 0.2em 0.5em; border: solid 1px #EEEEEE; border-radius: 3px; background: #DDDFFF;">
    <strong>Nieuw in versie 1.1.0</strong>
</span>

Voor versie 1.1.0 bestond er geen [Contactmomenten](../contactmomenten/index), [Klanten](../klanten/index) en [Verzoeken](../verzoeken/index) API's en werden klantcontacten in de Zaken API opgenomen. Vanaf versie 1.1.0 is deze resource deprecated - consumers horen van de contactmomenten API gebruik te maken.

Over een zaak kunnen één of meerdere klantinteracties plaatsvinden. De relatie met contactmomenten wordt gelegd via Zaakcontactmoment (Zaken API) en objectcontactmoment (Contactmomenten API). De relatie met verzoeken wordt gelegd via Zaakverzoek (Zaken API) en objectverzoek (Verzoeken API). 

## Specificatie van de Zaken API

* [Referentie-implementatie Zaken API](https://zaken-api.vng.cloud/)
* API specificatie (OAS3) in
  [ReDoc](https://zaken-api.vng.cloud/api/v1/schema/),
  [Swagger](https://petstore.swagger.io/?url=https://zaken-api.vng.cloud/api/v1/schema/openapi.yaml),
  [YAML](https://zaken-api.vng.cloud/api/v1/schema/openapi.yaml) of
  [JSON](https://zaken-api.vng.cloud/api/v1/schema/openapi.json)


## Specificatie van gedrag

Zaakregistratiecomponenten (ZRC) MOETEN aan twee aspecten voldoen:

* de ZRC `openapi.yaml` MOET volledig geïmplementeerd zijn.

* het run-time gedrag beschreven in deze standaard MOET correct geïmplementeerd zijn.

### OpenAPI specificatie

Alle operaties beschreven in [`openapi.yaml`](../../../../api-specificatie/zrc/1.0.x/openapi.yaml) MOETEN ondersteund worden en tot hetzelfde resultaat leiden als de referentie-implementatie van het ZRC.

Het is NIET TOEGESTAAN om gebruik te maken van operaties die niet beschreven staan in deze OAS spec, of om uitbreidingen op operaties in welke vorm dan ook toe te voegen.

### Run-time gedrag

Bepaalde gedrageningen kunnen niet in een OAS spec uitgedrukt worden omdat ze businesslogica bevatten. Deze gedragingen zijn hieronder beschreven en MOETEN zoals beschreven geïmplementeerd worden.

#### **<a name="zrc-001">Valideren `zaaktype` op de `Zaak`-resource ([zrc-001](#zrc-001))</a>**

Bij het aanmaken (`zaak_create`) MOET de URL-referentie naar het `zaaktype` gevalideerd worden op het bestaan. Indien het ophalen van het zaaktype niet (uiteindelijk) resulteert in een `HTTP 200` status code, MOET het ZRC antwoorden met een `HTTP 400` foutbericht.

De provider MOET tevens valideren dat het opgehaalde zaaktype een zaaktype is conform de 1.0.x Catalogi API specificatie.

Als er geprobeerd wordt om het `zaaktype` van een bestaande `Zaak` bij te werken (`zaak_update`, `zaak_partial_update`), dan MOET het ZRC antwoorden met een `HTTP 400` foutbericht.

#### **<a name="zrc-002">Garanderen uniciteit `bronorganisatie` en `identificatie` op de `Zaak`-resource ([zrc-002](#zrc-002))</a>**

Bij het aanmaken (`zaak_create`) en bijwerken (`zaak_update` en `zaak_partial_update`) MOET gevalideerd worden dat de combinatie `identificatie` en `bronorganisatie` uniek is, indien de `identificatie` door de consumer meegestuurd wordt.

Indien de identificatie niet door de consumer gestuurd wordt, dan MOET het ZRC de identificatie genereren op een manier die garandeert dat de identificatie uniek is binnen de bronorganisatie.

#### **<a name="zrc-003">Valideren `informatieobject` op de `ZaakInformatieObject`-resource ([zrc-003](#zrc-003))</a>**

Bij het aanmaken (`zaakinformatieobject_create`) MOET de URL-referentie naar het `informatieobject` gevalideerd worden op het bestaan. Indien het ophalen van het object niet (uiteindelijk) resulteert in een `HTTP 200` status code, MOET het ZRC antwoorden met een `HTTP 400` foutbericht.

#### **<a name="zrc-004">Valideren relatieinformatie op `ZaakInformatieObject`-resource ([zrc-004](#zrc-004))</a>**

Op basis van het `objectType` MOET de `aardRelatie` gezet worden conform het RGBZ. Omdat het `objectType` `zaak` is, moet `aardRelatie` gelijk zijn aan `"hoort_bij"`.

De `registratiedatum` MOET door het systeem gezet worden op het moment van aanmaken.

Bij het updaten (`zaakinformatieobject_update` en `zaakinformatieobject_partial_update`) is het NIET TOEGESTAAN om de relatie te wijzingen. Bij andere waardes voor de attributen `zaak`, en `informatieobject` MOET het ZRC antwoorden met een `HTTP 400` foutbericht.

#### **<a name="zrc-005">Synchroniseren relaties met informatieobjecten ([zrc-005](#zrc-005))</a>**

Wanneer een relatie tussen een `INFORMATIEOBJECT` en een `ZAAK` gemaakt of bijgewerkt wordt, dan MOET het ZRC in het DRC ook deze relatie aanmaken/bijwerken.

Een voorbeeld:

1. Een informatieobject wordt gerelateerd aan een zaak door een consumer:

    ```http
    POST https://zrc.nl/api/v1/zaakinformatieobjecten HTTP/1.0

    {
        "informatieobject": "https://drc.nl/api/v1/enkelvoudigeinformatieobjecten/1234",
        "zaak": "https://zrc.nl/api/v1/zaken/456789",
        "titel": "",
        "beschrijving": ""
    }
    ```

2. Het ZRC MOET de relatie spiegelen in het DRC:

    ```http
    POST https://drc.nl/api/v1/objectinformatieobjecten HTTP/1.0

    {
        "informatieobject": "https://drc.nl/api/v1/enkelvoudigeinformatieobjecten/1234",
        "object": "https://zrc.nl/api/v1/zaken/456789",
        "objectType": "zaak"
    }
    ```

Merk op dat het aanmaken van de relatie niet gelimiteerd is tot het aanmaken via de API. Indien elders (bijvoorbeeld via een admininterface) een relatie tot stand kan komen, dan MOET deze ook gesynchroniseerd worden.

#### **<a name="zrc-006">Data filteren bij de bron op basis van zaaktypes ([zrc-006](#zrc-006))</a>**

Het AC legt op het niveau van `zaaktype` vast welke operaties mogelijk zijn en wat de maximale vertrouwelijkheidaanduiding is voor een consumer. 

Het ZRC MAG ENKEL zaken ontsluiten waarvan:

* het zaaktype voorkomt in de autorisaties van de consumer.
* de vertrouwelijkheidaanduiding lager of gelijk aan de maximale vertrouwelijkheidaanduiding is voor het betreffende zaaktype.

De API-specificatie legt vast welke scopes nodig zijn voor welke operaties. Een provider MOET operaties blokkeren op zaken waarvan de nodige scopes niet toegekend zijn voor het zaaktype van de betreffende zaak.

Indien een operatie niet toegelaten is, dan MOET de provider met een `HTTP 403` foutbericht antwoorden.

Een consumer is verbonden aan het concept `Applicatie`, waarop `autorisaties` gedefinieerd worden. Het is mogelijk om op het niveau van `Applicatie` de vlag `heeftAlleAutorisaties` te zetten. Indien deze gezet is, dan MOET de provider alle operaties voor deze consumer toelaten, op alle zaken.

#### **<a name="zrc-007">Afsluiten zaak ([zrc-007](#zrc-007))</a>**

Een zaak wordt afgesloten door een eindstatus toe te kennen aan een `Zaak`. Elk `ZaakType` MOET minimaal één `StatusType` kennen. De eindstatus binnen een `ZaakType` is het `StatusType` met het hoogste `volgnummer`.

Een `Zaak` MOET een `Resultaat` hebben voor deze afgesloten kan worden.

De `Zaak.einddatum` MOET logisch afgeleid worden uit het toekennen van de eindstatus via de `Status.datumStatusGezet`.

Als een `Zaak` een eindstatus heeft dan is de zaak afgesloten en mogen gegevens van de zaak niet meer aangepast worden (behalve om redenen van correctie). Dit MOET beveiligd worden met de scope `zds.scopes.zaken.geforceerd-bijwerken`. "Gegevens van de zaak" omvat hier ook de gerelateerde gegevens zoals klantcontacten, resultaat, rollen, statussen, zaakinformatieobjecten, zaakobjecten, zaakbesluiten en zaakeigenschappen.

Bij het afsluiten van een `Zaak` MOET het ZRC het `Informatieobject.indicatieGebruiksrecht` controleren van alle gerelateerde informatieobjecten. Deze MAG NIET `null` zijn, maar MOET `true` of `false` zijn. Indien dit niet het geval is, dan dient het ZRC een validatiefout te genereren met code `indicatiegebruiksrecht-unset`.

#### **<a name="zrc-009">Heropenen zaak ([zrc-008](#zrc-008))</a>**

Bij het heropenen van een `Zaak` MOET de client een andere status toevoegen aan de zaak dan een eindstatus. Hiervoor MOET de client de scope `zds.scopes.zaken.heropenen` hebben.

Tevens MOET de provider de volgende velden op `null` zetten zodra een eindstatus wordt gewijzigd in een andere status:

* `Zaak.einddatum`
* `Zaak.archiefactiedatum`
* `Zaak.archiefnominatie`

#### **<a name="zrc-009">Vertrouwelijkheidaanduiding van een zaak ([zrc-009](#zrc-009))</a>**

Indien de client een `vertrouwelijkheidaanduiding` meegeeft bij het aanmaken of bewerken van een zaak, dan MOET de provider deze waarde toekennen. Indien de client deze niet expliciet toekent, dan MOET deze afgeleid worden uit `Zaak.ZaakType.vertrouwelijkheidaanduiding`.

Een `Zaak` response van de provider MOET altijd een geldige waarde voor `vertrouwelijkheidaanduiding` bevatten. Een client MAG een waarde voor `vertrouwelijkheidaanduiding` meesturen.

#### **<a name="zrc-010">Valideren `communicatiekanaal` op de `Zaak` resource ([zrc-010](#zrc-010))</a>**

Bij het aanmaken (`zaak_create`) en bijwerken (`zaak_update` en `zaak_partial_update`) MOET de URL-referentie naar het `communicatiekanaal` gevalideerd worden op het bestaan. Indien het ophalen van het zaaktype niet (uiteindelijk) resulteert in een `HTTP 200` status code, MOET het ZRC antwoorden met een `HTTP 400` foutbericht.

Het ophalen van deze resource moet een JSON-document zijn met de vorm van een communicatiekanaal zoals gedocumenteerd op de [referentielijsten-api](https://referentielijsten-api.vng.cloud/api/v1/schema/#operation/communicatiekanaal_read):

```json
{
    "url": "http://example.com",
    "naam": "string",
    "omschrijving": "string"
}
```

#### **<a name="zrc-011">Valideren `relevanteAndereZaken` op de `Zaak`-resource ([zrc-011](#zrc-011))</a>**

De lijst `relevanteAndereZaken` bevat URL-referenties naar andere zaken. Elke URL-referentie MOET gevalideerd worden op het bestaan. Indien het ophalen van de url niet (uiteindelijk) resulteert in een `HTTP 200` status code, MOET het ZRC antwoorden met een `HTTP 400` foutbericht.

In het foutbericht MOET de naam binnen `invalid-params` dan `relevanteAndereZaken.<index>` zijn, waarbij index start bij 0.

#### **<a name="zrc-012">Gegevensgroepen ([zrc-012](#zrc-012))</a>**

De client MAG gegevensgroepen zoals `Zaak.verlenging` en `Zaak.opschorting` meesturen met een waarde `null` om aan te geven dat er geen waarde gezet is. Dit is equivalent aan het niet-meesturen van de key in de request body. Als de client een (genest) object meestuurt, dan MOET de provider hierop de validatie van de gegevensgroep toepassen.

De provider MOET altijd de geneste structuur van de gegevensgroep antwoorden.

#### **<a name="zrc-013">Valideren `hoofdzaak` op de `Zaak`-resource ([zrc-013](#zrc-013))</a>**

Bij het aanmaken of bewerken van een `Zaak` kan de `hoofdzaak` aangegeven worden. Dit MOET een geldige URL-referentie naar een `Zaak` zijn, indien opgegeven.

Indien de client een `hoofdzaak` opgeeft die zelf een deelzaak is (i.e. `Zaak.hoofdzaak` != `null`), dan moet het ZRC antwoorden met een `HTTP 400` foutbericht (deelzaken van deelzaken zijn NIET toegestaan).

Indien de client een zaak bewerkt en diezelfde zaak als URL-referentie meegeeft als `hoofdzaak`, dan moet het ZRC antwoorden met een `HTTP 400` foutbericht (een zaak MAG GEEN deelzaak van zichzelf zijn).

#### **<a name="zrc-014">`Zaak.betalingsindicatie` en `Zaak.laatsteBetaaldatum` ([zrc-014](#zrc-014))</a>**

Indien de betalingsindicatie de waarde `"nvt"` heeft en een waarde gegeven is voor `laatsteBetaaldatum`, dan MOET het ZRC antwoorden met een `HTTP 400` foutbericht. Bij alle andere waarden van `betalingsindicatie` MAG een waarde opgegeven worden voor `laatsteBetaaldatum`.

Indien een waarde ingevuld is voor `laatsteBetaaldatum` en de betalingsindicatie wordt gewijzigd naar `"nvt"`, dan MOET de `laatsteBetaaldatum` op `null` gezet worden.

#### **<a name="zrc-015">Valideren van producten en/of diensten bij een `Zaak` ([zrc-015](#zrc-015))</a>**

Bij het aanmaken (`zaak_create`) en bijwerken (`zaak_update` en `zaak_partial_update`) MOET de collectie `productenOfDiensten` worden getoetst tegen het `Zaaktype.productenOfDiensten` van het betreffende zaaktype. De producten en/of diensten van de zaak MOETEN een subset van de producten en/of diensten op het zaaktype zijn.

#### **Valideren tegen de catalogus en bijhorende typen**

Het zaaktype van een zaak legt vast wat de mogelijke waarden zijn voor gerelateerde resources aan zaken. Dit MOET gevalideerd worden door een provider.

**<a name="zrc-016">Valideren dat het `statustype` van een `Status` bij het `Zaak.zaaktype` hoort ([zrc-016](#zrc-016))</a>**

<span style="padding: 0.2em 0.5em; border: solid 1px #FF6600; border-radius: 3px; background: #FFFF99;">
    <strong>Documentatie toegevoegd in patch 1.0.1</strong>
</span>

Wanneer een `Status` bij een `Zaak` toegevoegd wordt, dan MOET het `Status.statustype` voorkomen in de `Status.zaak.zaaktype.statustypen`.

**<a name="zrc-017">Valideren dat het `informatieobjecttype` van een `ZaakInformatieObject.informatieobject` bij het `Zaak.zaaktype` hoort ([zrc-017](#zrc-017))</a>**

<span style="padding: 0.2em 0.5em; border: solid 1px #FF6600; border-radius: 3px; background: #FFFF99;">
    <strong>Documentatie toegevoegd in patch 1.0.1</strong>
</span>

Wanneer een `ZaakInformatieObject` bij een `Zaak` toegevoegd wordt, dan MOET het `ZaakInformatieObject.informatieobject.informatieobjecttype` voorkomen in de `ZaakInformatieObject.zaak.zaaktype.informatieobjecttypen`.

**<a name="zrc-018">Valideren dat de `eigenschap` van een `ZaakEigenschap` bij het `Zaak.zaaktype` hoort ([zrc-018](#zrc-018))</a>**

<span style="padding: 0.2em 0.5em; border: solid 1px #FF6600; border-radius: 3px; background: #FFFF99;">
    <strong>Documentatie toegevoegd in patch 1.0.1</strong>
</span>

Wanneer een `ZaakEigenschap` bij een `Zaak` toegevoegd wordt, dan MOET de `ZaakEigenschap.eigenschap` voorkomen in de `ZaakEigenschap.zaak.zaaktype.eigenschappen`.

TODO: [fix in ZRC](https://github.com/VNG-Realisatie/gemma-zaken/issues/1476)

**<a name="zrc-019">Valideren dat het `roltype` van een `Rol` bij het `Zaak.zaaktype` hoort ([zrc-019](#zrc-019))</a>**

<span style="padding: 0.2em 0.5em; border: solid 1px #FF6600; border-radius: 3px; background: #FFFF99;">
    <strong>Documentatie toegevoegd in patch 1.0.1</strong>
</span>

Wanneer een `Rol` bij een `Zaak` toegevoegd wordt, dan MOET het `Rol.roltype` voorkomen in de `Rol.zaak.zaaktype.roltypen`.

**<a name="zrc-020">Valideren dat het `resultaattype` van een `Resultaat` bij het `Zaak.zaaktype` hoort ([zrc-020](#zrc-020))</a>**

<span style="padding: 0.2em 0.5em; border: solid 1px #FF6600; border-radius: 3px; background: #FFFF99;">
    <strong>Documentatie toegevoegd in patch 1.0.1</strong>
</span>

Wanneer een `Resultaat` bij een `Zaak` toegevoegd wordt, dan MOET het `Resultaat.resultaattype` voorkomen in de `Resultaat.zaak.zaaktype.resultaattypen`.

#### Archiveren

**<a name="zrc-021">Afleiden van archiveringsparameters ([zrc-021](#zrc-021))</a>**

Het resultaat van een zaak is bepalend voor het archiefregime. Bij het afsluiten van een zaak MOETEN de attributen `Zaak.archiefnominatie` en `Zaak.archiefactiedatum` bepaald worden uit het `Zaak.Resultaat` als volgt:

1. Indien de zaak geen `archiefnominatie` heeft, dan MOET deze overgenomen worden uit `Resultaat.Resultaattype.archiefnominatie`
2. Indien `Resultaat.Resultaattype.archiefactietermijn` gevuld is:
    1. Bepaal de `brondatum` van de archiefprocedure
        1. Consulteer het groepattribuut `Resultaat.Resultaattype.brondatumArchiefprocedure`
        2. Afhankelijk van de waarde van `afleidingswijze`:
            * `afgehandeld` -> gebruik `Zaak.einddatum`
            * `hoofdzaak` -> gebruik `Zaak.hoofdzaak.einddatum`
            * `eigenschap` -> gebruik de waarde van de eigenschap met als naam de waarde van `Resultaat.Resultaattype.brondatumArchiefprocedure.datumkenmerk`
            * `ander_datumkenmerk` -> `Zaak.archiefactiedatum` MOET handmatig afgeleid en gezet worden
            * `zaakobject` -> zoek de gerelateerde objecten van type `Resultaat.Resultaattype.brondatumArchiefprocedure.objecttype`.Lees van elk object het attribuut met de naam  `Resultaat.Resultaattype.brondatumArchiefprocedure.datumkenmerk` en gebruik de maximale waarde.
            * `termijn` -> `Zaak.einddatum` + `Resultaat.Resultaattype.brondatumArchiefprocedure.procestermijn`
            * `gerelateerde_zaak` -> maximale `Zaak.einddatum` van alle gerelateerde zaken
            * `ingangsdatum_besluit` -> maximale `Besluit.ingangsdatum` van alle gerelateerde besluiten
            * `vervaldatum_besluit` -> maximale `Besluit.vervaldatum` van alle gerelateerde besluiten
    2. Zet `Zaak.archiefactiedatum` als `brondatum + Resultaat.Resultaattype.archiefactietermijn`

Indien de archiefactiedatum niet bepaald kan worden, dan MAG er geen datum gezet worden. Dit kan voorkomen als de brondatum niet bepaald kan worden of de archiefactietermijn niet beschikbaar is.

**<a name="zrc-022">Zetten `Zaak.archiefstatus` ([zrc-022](#zrc-022))</a>**

De standaardwaarde voor archiefstatus is `nog_te_archiveren`. Indien een andere waarde gezet wordt, dan MOETEN alle gerelateerde informatieobjecten de status `gearchiveerd` hebben.

De attributen `Zaak.archiefnominatie` en `Zaak.archiefactiedatum` MOETEN een waarde krijgen als de de archiefstatus een waarde krijgt anders dan `nog_te_archiveren`.

Indien deze voorwaarden niet voldaan zijn, dan MOET het ZRC met een `HTTP 400` foutbericht antwoorden.

**<a name="zrc-023">Vernietigen van zaken ([zrc-023](#zrc-023))</a>**

Bij het verwijderen van een `Zaak` MOETEN de zaak en gerelateerde objecten daadwerkelijk uit de opslag verwijderd worden. Zogenaamde "soft-deletes" zijn NIET TOEGESTAAN. Onder gerelateerde objecten wordt begrepen:

- `zaak` - de deelzaken van de verwijderde hoofzaak
- `status` - alle statussen van de verwijderde zaak
- `resultaat` - het resultaat van de verwijderde zaak
- `rol` - alle rollen bij de zaak
- `zaakobject` - alle zaakobjecten bij de zaak
- `zaakeigenschap` - alle eigenschappen van de zaak
- `zaakkenmerk` - alle kenmerken van de zaak
- `zaakinformatieobject` - relatie naar enkelvoudige informatieobjecten \*
- `zaakverzoek` - relatie naar een zaak verzoek (**nieuw in 1.1.0**)
- `zaakcontactmoment` - relatie naar een zaak contactmoment (**nieuw in 1.1.0**)
- `klantcontact` - alle klantcontacten bij een zaak
- `audittrail` - de geschiedenis van het object

Een deelzaak KAN vernietigd worden zonder dat de hoofdzaak vernietigd wordt.

\* Het verwijderen van een `zaakinformatieobject` in het ZRC leidt er toe dat het `objectinformatieobject` in het DRC ook verwijderd wordt indien dit kan.


#### HTTP-Caching

<span style="padding: 0.2em 0.5em; border: solid 1px #EEEEEE; border-radius: 3px; background: #DDDFFF;">
    <strong>Nieuw in versie 1.1.0</strong>
</span>

De Zaken API moet HTTP-Caching ondersteunen op basis van de `ETag` header. In de API spec staat beschreven voor welke resources dit van toepassing is.

De `ETag` MOET worden berekend op de JSON-weergave van de resource. Verschillende, maar equivalente weergaves (bijvoorbeeld dezelfde API ontsloten wel/niet via NLX) MOETEN verschillende waarden voor de `ETag` hebben.

Indien de consumer een `HEAD` verzoek uitvooert op deze resources, dan MOET de provider antwoorden met dezelfde headers als bij een normale `GET`, dus inclusief de `ETag` header. Er MAG GEEN response body voorkomen.

Indien de consumer gebruik maakt van de `If-None-Match` header, met één of meerdere waarden voor de `ETag`, dan MOET de provider antwoorden met een `HTTP 304` bericht indien de huidige `ETag` waarde van de resource hierin voorkomt. Als de huidige `ETag` waarde hier niet in voorkomt, dan MOET de provider een normale `HTTP 200` response sturen.

#### TODO: synchroniseren zaakcontactmomenten



#### **<a name="zrc-024">Synchroniseren relaties met verzoeken ([zrc-024](#zrc-024))</a>**

<span style="padding: 0.2em 0.5em; border: solid 1px #EEEEEE; border-radius: 3px; background: #DDDFFF;">
    <strong>Nieuw in versie 1.1.0</strong>
</span>

Wanneer een relatie tussen een `VERZOEK` en een `ZAAK` gemaakt of bijgewerkt wordt, dan MOET het ZRC in het KIC ook deze relatie aanmaken/bijwerken.

Een voorbeeld:

1. Een verzoek wordt gerelateerd aan een zaak door een consumer:

    ```http
    POST https://zrc.nl/api/v1/zaakverzoeken HTTP/1.0

    {
        "verzoek": "https://vrc.nl/api/v1/verzoeken/1234",
        "zaak": "https://zrc.nl/api/v1/zaken/456789",
    }
    ```

2. Het ZRC MOET de relatie spiegelen in het KIC:

    ```http
    POST https://vrc.nl/api/v1/objectverzoeken HTTP/1.0

    {
        "verzoek": "https://vrc.nl/api/v1/verzoeken/1234",
        "object": "https://zrc.nl/api/v1/zaken/456789",
        "objectType": "zaak"
    }
    ```

Merk op dat het aanmaken van de relatie niet gelimiteerd is tot het aanmaken via de API. Indien elders (bijvoorbeeld via een admininterface) een relatie tot stand kan komen, dan MOET deze ook gesynchroniseerd worden.

#### **<a name="zrc-025">Synchroniseren relaties met contactmomenten ([zrc-025](#zrc-025))</a>**

<span style="padding: 0.2em 0.5em; border: solid 1px #EEEEEE; border-radius: 3px; background: #DDDFFF;">
    <strong>Nieuw in versie 1.1.0</strong>
</span>

Wanneer een relatie tussen een `CONTACTMOMENT` en een `ZAAK` gemaakt of bijgewerkt wordt, dan MOET het ZRC in het CRC ook deze relatie aanmaken/bijwerken.


## Overige documentatie

* [Referentiemodel Gemeentelijke Basisgegevens Zaken (RGBZ) 2.0](https://www.gemmaonline.nl/index.php/RGBZ_2.0_in_ontwikkeling)
* [Tutorial Archiveren](/ontwikkelaars/handleidingen-en-tutorials/archiveren)
