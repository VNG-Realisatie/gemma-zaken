---
title: "Zaken API"
date: '10-7-2019'
weight: 10
---

API voor het opslaan en ontsluiten van zaakgegevens.

De API ondersteunt het opslaan en het naar andere applicaties ontsluiten van gegevens over alle gemeentelijke zaken, van elk type. Opslag vindt plaats conform het RGBZ waarin objecten, gegevens daarvan en onderlinge relaties zijn beschreven. Het bevat echter niet alle gegevens uit het RGBZ: documenten worden bijv. opgeslagen in de Documenten API, besluiten in de Besluiten API, etc. Vanuit zaken worden er dan ook relaties gelegd naar andere resources.


## Gegevensmodel

![Gegevensmodel Zaken API](Zaken API.png){:width="1200px"}


## Specificatie van de Catalogi API

[Referentie-implementatie Zaken API](https://zaken-api.vng.cloud/)

[Plain text OAS3 specificatie](../../../api-specificatie/zrc/openapi.yaml)


## Specificatie van gedrag

Zaakregistratiecomponenten (ZRC) MOETEN aan twee aspecten voldoen:

* de ZRC `openapi.yaml` MOET volledig geïmplementeerd zijn.

* het run-time gedrag beschreven in deze standaard MOET correct geïmplementeerd
  zijn.

### OpenAPI specificatie

Alle operaties beschreven in [`openapi.yaml`](../../../api-specificatie/zrc/openapi.yaml)
MOETEN ondersteund worden en tot hetzelfde resultaat leiden als de
referentie-implementatie van het ZRC.

Het is NIET TOEGESTAAN om gebruik te maken van operaties die niet beschreven
staan in deze OAS spec, of om uitbreidingen op operaties in welke vorm dan ook
toe te voegen.

### Run-time gedrag

Bepaalde gedrageningen kunnen niet in een OAS spec uitgedrukt worden omdat ze
businesslogica bevatten. Deze gedragingen zijn hieronder beschreven en MOETEN
zoals beschreven geïmplementeerd worden.

#### **<a name="zrc-001">Valideren `zaaktype` op de `Zaak`-resource ([zrc-001](#zrc-001))</a>**

Bij het aanmaken (`zaak_create`) en bijwerken (`zaak_update` en
`zaak_partial_update`) MOET de URL-referentie naar het `zaaktype` gevalideerd
worden op het bestaan. Indien het ophalen van het zaaktype niet (uiteindelijk)
resulteert in een `HTTP 200` status code, MOET het ZRC antwoorden met een
`HTTP 400` foutbericht.

(TODO: valideren dat het inderdaad om een zaaktype resource gaat -> validatie
aanscherpen)

#### **<a name="zrc-002">Garanderen uniciteit `bronorganisatie` en `identificatie` op de `Zaak`-resource ([zrc-002](#zrc-002))</a>**

Bij het aanmaken (`zaak_create`) en bijwerken (`zaak_update` en
`zaak_partial_update`) MOET gevalideerd worden dat de combinatie `identificatie`
en `bronorganisatie` uniek is, indien de `identificatie` door de consumer
meegestuurd wordt.

Indien de identificatie niet door de consumer gestuurd wordt, dan MOET het ZRC
de identificatie genereren op een manier die garandeert dat de identificatie
uniek is binnen de bronorganisatie.

#### **<a name="zrc-003">Valideren `informatieobject` op de `ZaakInformatieObject`-resource ([zrc-003](#zrc-003))</a>**

Bij het aanmaken (`zaakinformatieobject_create`) MOET de URL-referentie
naar het `informatieobject` gevalideerd worden op het bestaan. Indien het ophalen van het object niet (uiteindelijk) resulteert in een `HTTP 200` status code, MOET het
ZRC antwoorden met een `HTTP 400` foutbericht.

#### **<a name="zrc-004">Valideren relatieinformatie op `ZaakInformatieObject`-resource ([zrc-004](#zrc-004))</a>**

Op basis van het `objectType` MOET de `aardRelatie` gezet worden conform het
RGBZ. Omdat het `objectType` `zaak` is, moet `aardRelatie` gelijk zijn aan `"hoort_bij"`.

De `registratiedatum` MOET door het systeem gezet worden op het moment van
aanmaken.

Bij het updaten (`zaakinformatieobject_update` en
`zaakinformatieobject_partial_update`) is het NIET TOEGESTAAN om de relatie
te wijzingen. Bij andere waardes voor de attributen `zaak`, en
`informatieobject` MOET het ZRC antwoorden met een `HTTP 400` foutbericht.

#### **<a name="zrc-005">Synchroniseren relaties met informatieobjecten ([zrc-005](#zrc-005))</a>**

Wanneer een relatie tussen een `INFORMATIEOBJECT` en een `ZAAK` gemaakt
of bijgewerkt wordt, dan MOET het ZRC in het DRC ook deze relatie
aanmaken/bijwerken.

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

Merk op dat het aanmaken van de relatie niet gelimiteerd is tot het aanmaken
via de API. Indien elders (bijvoorbeeld via een admininterface) een relatie tot
stand kan komen, dan MOET deze ook gesynchroniseerd worden.

#### **<a name="zrc-006">Data filteren bij de bron op basis van zaaktypes ([zrc-006](#zrc-006))</a>**

Het AC legt op het niveau van `zaaktype` vast welke operaties mogelijk zijn en 
wat de maximale vertrouwelijkheidaanduiding is voor een consumer.

Het ZRC MAG ENKEL zaken ontsluiten waarvan:

* het zaaktype voorkomt in de autorisaties van de consumer.
* de vertrouwelijkheidaanduiding lager of gelijk aan de maximale
  vertrouwelijkheidaanduiding is voor het betreffende zaaktype.

De API-specificatie legt vast welke scopes nodig zijn voor welke operaties.
Een provider MOET operaties blokkeren op zaken waarvan de nodige scopes niet
toegekend zijn voor het zaaktype van de betreffende zaak.

Indien een operatie niet toegelaten is, dan MOET de provider met een
`HTTP 403` foutbericht antwoorden.

Een consumer is verbonden aan het concept `Applicatie`, waarop `autorisaties`
gedefinieerd worden. Het is mogelijk om op het niveau van `Applicatie` de vlag
`heeftAlleAutorisaties` te zetten. Indien deze gezet is, dan MOET de provider
alle operaties voor deze consumer toelaten, op alle zaken.

#### **<a name="zrc-007">Afsluiten zaak ([zrc-007](#zrc-007))</a>**
Een zaak wordt afgesloten door een eindstatus toe te kennen aan een `Zaak`. Elk
`ZaakType` MOET minimaal één `StatusType` kennen. De eindstatus binnen een
`ZaakType` is het `StatusType` met het hoogste `volgnummer`.

Een `Zaak` MOET een `Resultaat` hebben voor deze afgesloten kan worden.

De `Zaak.einddatum` MOET logisch afgeleid worden uit het toekennen van de
eindstatus via de `Status.datumStatusGezet`.

Als een `Zaak` een eindstatus heeft dan is de zaak afgesloten en mogen gegevens
van de zaak niet meer aangepast worden (behalve om redenen van correctie). Dit
MOET beveiligd worden met de scope `zds.scopes.zaken.geforceerd-bijwerken`.

Bij het afsluiten van een `Zaak` MOET het ZRC het
`Informatieobject.indicatieGebruiksrecht` controleren van alle gerelateerde
informatieobjecten. Deze MAG NIET `null` zijn, maar MOET `true` of `false`
zijn. Indien dit niet het geval is, dan dient het ZRC een validatiefout te
genereren met code `indicatiegebruiksrecht-unset`.

#### Heropenen zaak

Bij het heropenen van een `Zaak` MOET de client een andere status toevoegen aan
de zaak dan een eindstatus. Hiervoor MOET de client de scope
`zds.scopes.zaken.heropenen` hebben.

Tevens MOET de provider de volgende velden op `null` zetten zodra een
eindstatus wordt gewijzigd in een andere status:

* `Zaak.einddatum`
* `Zaak.archiefactiedatum`
* `Zaak.archiefnominatie`

#### **<a name="zrc-008">Vertrouwelijkheidaanduiding van een zaak ([zrc-008](#zrc-008))</a>**

Indien de client een `vertrouwelijkheidaanduiding` meegeeft bij het aanmaken
of bewerken van een zaak, dan MOET de provider deze waarde toekennen. Indien
de client deze niet expliciet toekent, dan MOET deze afgeleid worden uit
`Zaak.ZaakType.vertrouwelijkheidaanduiding`.

Een `Zaak` response van de provider MOET altijd een geldige waarde voor
`vertrouwelijkheidaanduiding` bevatten. Een client MAG een waarde voor
`vertrouwelijkheidaanduiding` meesturen.

#### **<a name="zrc-009">Valideren `communicatiekanaal` op de `Zaak` resource ([zrc-009](#zrc-009))</a>**

Bij het aanmaken (`zaak_create`) en bijwerken (`zaak_update` en
`zaak_partial_update`) MOET de URL-referentie naar het `communicatiekanaal`
gevalideerd worden op het bestaan. Indien het ophalen van het zaaktype niet
(uiteindelijk) resulteert in een `HTTP 200` status code, MOET het ZRC
antwoorden met een `HTTP 400` foutbericht.

Het ophalen van deze resource moet een JSON-document zijn met de vorm van
een communicatiekanaal zoals gedocumenteerd op de
[referentielijsten-api](https://ref.tst.vng.cloud/referentielijsten/api/v1/schema/#operation/communicatiekanaal_read):

```json
{
    "url": "http://example.com",
    "naam": "string",
    "omschrijving": "string"
}
```

#### **<a name="zrc-010">Valideren `relevanteAndereZaken` op de `Zaak`-resource ([zrc-010](#zrc-010))</a>**

De lijst `relevanteAndereZaken` bevat URL-referenties naar andere zaken. Elke
URL-referentie MOET gevalideerd worden op het bestaan. Indien het ophalen van
de url niet (uiteindelijk) resulteert in een `HTTP 200` status code, MOET het ZRC
antwoorden met een `HTTP 400` foutbericht.

In het foutbericht MOET de naam binnen `invalid-params` dan
`relevanteAndereZaken.<index>` zijn, waarbij index start bij 0.

#### **<a name="zrc-011">Gegevensgroepen ([zrc-011](#zrc-011))</a>**

De client MAG gegevensgroepen zoals `Zaak.verlenging` en `Zaak.opschorting`
meesturen met een waarde `null` om aan te geven dat er geen waarde gezet is.
Dit is equivalent aan het niet-meesturen van de key in de request body.
Als de client een (genest) object meestuurt, dan MOET de provider hierop de
validatie van de gegevensgroep toepassen.

De provider MOET altijd de geneste structuur van de gegevensgroep antwoorden.

#### **<a name="zrc-012">Valideren `hoofdzaak` op de `Zaak`-resource ([zrc-012](#zrc-012))</a>**

Bij het aanmaken of bewerken van een `Zaak` kan de `hoofdzaak` aangegeven
worden. Dit MOET een geldige URL-referentie naar een `Zaak` zijn, indien
opgegeven.

Indien de client een `hoofdzaak` opgeeft die zelf een deelzaak is (i.e.
`Zaak.hoofdzaak` != `null`), dan moet het ZRC antwoorden met een `HTTP 400`
foutbericht (deelzaken van deelzaken zijn NIET toegestaan).

Indien de client een zaak bewerkt en diezelfde zaak als URL-referentie meegeeft
als `hoofdzaak`, dan moet het ZRC antwoorden met een `HTTP 400`
foutbericht (een zaak MAG GEEN deelzaak van zichzelf zijn).

#### **<a name="zrc-013">`Zaak.betalingsindicatie` en `Zaak.laatsteBetaaldatum` ([zrc-013](#zrc-013))</a>**

Indien de betalingsindicatie de waarde `"nvt"` heeft en een waarde gegeven is
voor `laatsteBetaaldatum`, dan MOET het ZRC antwoorden met een `HTTP 400`
foutbericht. Bij alle andere waarden van `betalingsindicatie` MAG een waarde
opgegeven worden voor `laatsteBetaaldatum`.

Indien een waarde ingevuld is voor `laatsteBetaaldatum` en de betalingsindicatie
wordt gewijzigd naar `"nvt"`, dan MOET de `laatsteBetaaldatum` op `null` gezet
worden.

#### **<a name="zrc-014">Valideren van producten en/of diensten bij een `Zaak` ([zrc-014](#zrc-014))</a>**

Bij het aanmaken (`zaak_create`) en bijwerken (`zaak_update` en
`zaak_partial_update`) MOET de collectie `productenOfDiensten` worden getoetst
tegen het `Zaaktype.productenOfDiensten` van het betreffende zaaktype. De
producten en/of diensten van de zaak MOETEN een subset van de producten en/of
diensten op het zaaktype zijn.

#### Archiveren

**<a name="zrc-015">Afleiden van archiveringsparameters ([zrc-015](#zrc-015))</a>**

Het resultaat van een zaak is bepalend voor het archiefregime. Bij het
afsluiten van een zaak MOETEN de attributen `Zaak.archiefnominatie`
en `Zaak.archiefactiedatum` bepaald worden uit het `Zaak.Resultaat` als volgt:

1. Indien de zaak geen `archiefnominatie` heeft, dan MOET deze overgenomen
   worden uit `Resultaat.Resultaattype.archiefnominatie`
2. Indien `Resultaat.Resultaattype.archiefactietermijn` gevuld is:
    1. Bepaal de `brondatum` van de archiefprocedure
        1. Consulteer het groepattribuut `Resultaat.Resultaattype.brondatumArchiefprocedure`
        2. Afhankelijk van de waarde van `afleidingswijze`:
            * `afgehandeld` -> gebruik `Zaak.einddatum`
            * `hoofdzaak` -> gebruik `Zaak.hoofdzaak.einddatum`
            * `eigenschap` -> gebruik de waarde van de eigenschap met als naam
              de waarde van
              `Resultaat.Resultaattype.brondatumArchiefprocedure.datumkenmerk`
            * `ander_datumkenmerk` -> brondatum MOET handmatig afgeleid en
              gezet worden
            * `zaakobject` -> zoek de gerelateerde objecten van type
              `Resultaat.Resultaattype.brondatumArchiefprocedure.objecttype`.
              Lees van elk object het attribuut met de naam
              `Resultaat.Resultaattype.brondatumArchiefprocedure.datumkenmerk`
              en gebruik de maximale waarde.
            * `termijn` -> `Zaak.einddatum` + `Resultaat.Resultaattype.brondatumArchiefprocedure.procestermijn`
            * `gerelateerde_zaak` -> TODO
            * `ingangsdatum_besluit` -> maximale `Besluit.ingangsdatum` van alle
              gerelateerde besluiten
            * `vervaldatum_besluit` -> maximale `Besluit.vervaldatum` van alle
              gerelateerde besluiten
    2. Zet `Zaak.archiefactiedatum` als `brondatum + Resultaat.Resultaattype.archiefactietermijn`

Indien de archiefactiedatum niet bepaald kan worden, dan MAG er geen datum
gezet worden. Dit kan voorkomen als de brondatum niet bepaald kan worden of
de archiefactietermijn niet beschikbaar is.

**<a name="zrc-016">Zetten `Zaak.archiefstatus` ([zrc-016](#zrc-016))</a>**

De standaardwaarde voor archiefstatus is `nog_te_archiveren`. Indien een andere
waarde gezet wordt, dan MOETEN alle gerelateerde informatieobjecten de status
`gearchiveerd` hebben.

De attributen `Zaak.archiefnominatie` en `Zaak.archiefactiedatum` MOETEN een
waarde krijgen als de de archiefstatus een waarde krijgt anders dan
`nog_te_archiveren`.

Indien deze voorwaarden niet voldaan zijn, dan MOET het ZRC met een `HTTP 400`
foutbericht antwoorden.

**<a name="zrc-017">Vernietigen van zaken ([zrc-017](#zrc-017))</a>**

Bij het verwijderen van een `Zaak` MOETEN de zaak en gerelateerde objecten
daadwerkelijk uit de opslag verwijderd worden. Zogenaamde "soft-deletes" zijn
NIET TOEGESTAAN. Onder gerelateerde objecten wordt begrepen:

- `zaak` - de deelzaken van de verwijderde hoofzaak
- `status` - alle statussen van de verwijderde zaak
- `resultaat` - het resultaat van de verwijderde zaak
- `rol` - alle rollen bij de zaak
- `zaakobject` - alle zaakobjecten bij de zaak
- `zaakeigenschap` - alle eigenschappen van de zaak
- `zaakkenmerk` - alle kenmerken van de zaak
- `zaakinformatieobject` - relatie naar enkelvoudige informatieobjecten \*
- `klantcontact` - alle klantcontacten bij een zaak
- `audittrail` - de geschiedenis van het object

Een deelzaak KAN vernietigd worden zonder dat de hoofdzaak vernietigd wordt.

\* Het verwijderen van een `zaakinformatieobject` in het ZRC leidt er toe dat
het `objectinformatieobject` in het DRC ook verwijderd wordt indien dit kan.


## Overige documentatie

* [Referentiemodel Gemeentelijke Basisgegevens Zaken (RGBZ) 2.0](https://www.gemmaonline.nl/index.php/RGBZ_2.0_in_ontwikkeling)
