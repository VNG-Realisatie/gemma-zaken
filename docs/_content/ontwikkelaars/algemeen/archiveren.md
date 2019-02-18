# Archiveren (voor dummies)

## [WIP] Archiveringsproces *

Zie: [#751](https://github.com/VNG-Realisatie/gemma-zaken/issues/751)

\* Term gekozen t.b.v. de leesbaarheid. Echter, het gaat met name er om dat 
organisaties hun informatiehuishouding op orde hebben en houden.

In essentie bestaat het archiveringsproces uit 3 stappen:

1. Proces in het kort:
   1. een zaak wordt afgesloten met een *einddatum*,
   2. doorloopt hierna eerst een *procestermijn*,
   3. het einde van de procestermijn heet de *brondatum*
   4. hierna begint de *archiefactietermijn* (ook wel *bewaartermijn*),
   5. na de *bewaartermijn* wordt het zaak-dossier gearchiveerd (aangegeven 
      op de `Zaak.Archiefstatus`).
2. Een zaak-dossier wordt *blijvend bewaard* of kan worden *vernietigd* en 
   staat aangegeven op `Zaak.Archiefnominatie`.
3. Na de *bewaartermijn*, dus vanaf de `Zaak.Archiefactiedatum` **moet** het 
   zaak-dossier op een moment worden *overgebracht naar een 
   archiefbewaarplaats* of worden *vernietigd*.

Opmerkingen:

1. Een zaak-dossier **mag** eerder worden *overgebracht naar een 
   archiefbewaarplaats*.
2. Het is niet altijd, vanaf het aanmaken van een zaak, duidelijk wat er mee 
   moet gebeuren of wanneer dat moet gebeuren.
3. Het archiveringsproces doorloopt verschillende stadia te volgen via de
   `Zaak.Archiefstatus`.

### Definitie zaak-dossier

Zie: [#750](https://github.com/VNG-Realisatie/gemma-zaken/issues/750)

Een zaakdossier is het geheel van zaak-metadata, bijbehorende 
informatieobjecten incl. metadata, statussen, resultaten en besluiten, en 
gerelateerde entiteiten:

* Deelzaken (of hoofdzaak)
* Vervolgzaken (of is zelf vervolgzaak)
* Gerelateerde zaken (via zakenrelatie)
* Zaakobjecten: objecten uit het RGBZ of RSGB waarop de zaak betrekking heeft
* Andere zaakobjecten: objecten waarop de zaak betrekking heeft maar die geen 
  onderdeel uitmaken van RGBZ of RSGB. Dit kunnen business objecten zoals 
  melding of aanvraag zijn.

### Wat gebeurt er als een zaak-dossier *blijvend bewaard* wordt?

Het zaak-dossier is overgedragen naar een bewaarplaats.

### Wat gebeurt er als een zaak-dossier *vernietigd* wordt?

Het vernietigen is het definitief verwijderen van data volgens de NEN2082 (Eis 80):

> Vernietigen van archiefstukken/archiefbestanddelen moet zo gebeuren dat deze niet meer op enigerlei wijze kunnen worden gereproduceerd.

## Gerelateerde attributen

* `Zaak.Archiefnominatie` (*optioneel*) Aanduiding of het zaakdossier blijvend bewaard of na een bepaalde termijn vernietigd moet worden:

  Naam | Definitie
  --- | ---
  `Blijvend bewaren` | Het zaakdossier moet bewaard blijven en op de Archiefactiedatum overgedragen worden naar een archiefbewaarplaats. 
  `Vernietigen` | Het zaakdossier moet op of na de Archiefactiedatum vernietigd worden.
    
* `Zaak.Archiefstatus` De fase waarin het zaakdossier zich qua archivering bevindt:

  Naam | Definitie
  --- | ---
  `nog te archiveren` | De zaak cq. het zaakdossier is nog niet als geheel gearchiveerd (*standaard waarde*).
  `gearchiveerd` | De zaak cq. het zaakdossier is als geheel niet-wijzigbaar bewaarbaar gemaakt.
  `gearchiveerd (procestermijn onbekend)` | De zaak cq. het zaakdossier is als geheel niet-wijzigbaar bewaarbaar gemaakt maar de vernietigingsdatum kan nog niet bepaald worden. 
  `vernietigd` | De zaak cq. het zaakdossier is vernietigd. *Niet geïmplementeerd omdat vernietigde zaken echt weg zijn.*
  `overgedragen` | De zaak cq. het zaakdossier is overgebracht naar een archiefbewaarplaats.

* `Zaak.Archiefactiedatum` De datum waarop het gearchiveerde zaakdossier vernietigd moet worden dan wel overgebracht moet worden naar een archiefbewaarplaats. 

* `ResultaatType.Archiefnominatie` Aanduiding die aangeeft of `Zaak`en met een resultaat van dit `ResultaatType` blijvend moeten worden bewaard of (op termijn) moeten worden vernietigd . 

* `ResultaatType.Procestermijn` (*optioneel*) De periode dat het zaakdossier na afronding van de zaak actief gebruikt en/of geraadpleegd wordt ter ondersteuning van de taakuitoefening van de organisatie.

* `ResultaatType.Archiefactietermijn` De termijn, na het vervallen van het bedrijfsvoeringsbelang, waarna het zaakdossier (de `Zaak` met alle bijbehorende `Informatieobject`en) van een `Zaak` met een resultaat van dit `ResultaatType` vernietigd of overgebracht (naar een archiefbewaarplaats) moet worden. 

* `ResultaatType.BrondatumArchiefprocedure`

  * `Afleidingswijze` Wijze van bepalen van de brondatum:

    Naam | Definitie | Regels
    --- | --- | ---
    `afgehandeld` | De termijn start op de datum waarop de zaak is afgehandeld (ZAAK.Einddatum in het RGBZ).
    `ander datumkenmerk` | De termijn start op de datum die is vastgelegd in een ander datumveld dan de datumvelden waarop de overige waarden (van deze attribuutsoort) betrekking hebben. | `Objecttype`, `Registratie` en `Datumkenmerk` zijn niet leeg.
    `eigenschap` | De termijn start op de datum die vermeld is in een zaaktype-specifieke eigenschap (zijnde een ?datumveld?). | `ResultaatType.ZaakType` heeft een `Eigenschap`; `Objecttype`, en `Datumkenmerk` zijn niet leeg.
    `gerelateerde zaak` | De termijn start op de datum waarop de gerelateerde zaak is afgehandeld (ZAAK.Einddatum of ZAAK.Gerelateerde_zaak.Einddatum in het RGBZ). | `ResultaatType.ZaakType` heeft gerelateerd `ZaakType`
    `hoofdzaak` | De termijn start op de datum waarop de gerelateerde zaak is afgehandeld, waarvan de zaak een deelzaak is (ZAAK.Einddatum van de hoofdzaak in het RGBZ). | `ResultaatType.ZaakType` is deelzaaktype van `ZaakType`
    `ingangsdatum besluit` | De termijn start op de datum waarop het besluit van kracht wordt (BESLUIT.Ingangsdatum in het RGBZ). | `ResultaatType.ZaakType` heeft relevant `BesluitType`
    `termijn` | De termijn start een vast aantal jaren na de datum waarop de zaak is afgehandeld (ZAAK.Einddatum in het RGBZ). 
    `vervaldatum besluit` | De termijn start op de dag na de datum waarop het besluit vervalt (BESLUIT.Vervaldatum in het RGBZ). | `ResultaatType.ZaakType` heeft relevant `BesluitType`
    `zaakobject` | De termijn start op de einddatum geldigheid van het zaakobject waarop de zaak betrekking heeft (bijvoorbeeld de overlijdendatum van een Persoon). | `ZaakObjectType` is relevant voor `ResultaatType.ZaakType`; `Objecttype` is niet leeg en komt overeen met de naam van het `ZaakObjectType`; `Datumkenmerk` is niet leeg en komt overeen met een attribuutnaam dat bestaat op `ZaakObjectType`.

   * `Registratie` (*optioneel*) De naam van de registratie waarvan het procesobject deel uit maakt.
   * `Objecttype` (*optioneel*) Het soort object in de registratie dat het procesobject representeert.
   * `Datumkenmerk` (*optioneel*) Naam van de attribuutsoort van het procesobject dat bepalend is voor het einde van de procestermijn. 



TODO:

* `Zaak.StartdatumBewaartermijn` (nieuw!) De datum die de start markeert van de termijn waarop het zaakdossier vernietigd moet worden. 
* `Zaak.Procesobject`
* `Zaak.Selectielijstklasse`
* `ResultaatType.BrondatumArchiefprocedure.EinddatumBekend`
* `ResultaatType.Procesobjectaard`
* `ZaakType.SelectielijstProcestype`
* `ZaakType.Archiefclassificatie`
* `Zaak-InformatieobjectType.Archiefregime`
* `Zaak-InformatieobjectType.Vernietigingstermijn` (relatie) De termijn waarna informatieobjecten, van het `InformatieobjectType` bij zaken van het `ZaakType` met een resultaat van het `ResultaatType`, vernietigd moeten worden. 

### Berekenen van de `Zaak.Archiefactiedatum`

1. Bepaal de *brondatum* van de `Zaak`:

`ResultaatType.BrondatumArchiefprocedure.Afleidingswijze` | Waarde van *brondatum*
--- | ---
`afgehandeld` | `Zaak.Einddatum`
`gerelateerde zaak` | De hoogste datum van van alle `Zaak.GerelateerdeZaak.Einddatum` of `Zaak.Einddatum` *
`hoofdzaak` | `Zaak.HoofdZaak.Einddatum`
`ingangsdatum besluit` | `Zaak.Besluit.Ingangsdatum` 
`vervaldatum besluit` | `Zaak.Besluit.Vervaldatum`
`ander datumkenmerk` | *Deze kan worden geimplementeerd door een schrijfbaar brondatum attribuut op te nemen*
`eigenschap` | `Zaak.Eigenschappen[<ResultaatType.BrondatumArchiefprocedure.Datumkenmerk>]`
`termijn` | *Door onduidelijkheid en suggesties van Ben de Jong en het team wordt deze niet geïmplementeerd.*
`zaakobject` | De hoogste datum van alle `Zaak.ZaakObject.Object.[<ResultaatType.BrondatumArchiefprocedure.Datumkenmerk>]` (typisch `DatumEindeGeldigheid`) *

\* Aanscherping op RGBZ 2.0.2 beschrijving.

2. Als de *brondatum* is bepaald:
   `Zaak.Archiefactiedatum` = *brondatum* + `Zaak.ResultaatType.Procestermijn` + `Zaak.ResultaatType.Archiefactietermijn`

## API ondersteuning

### Opvragen lijst van zaken die gearchiveerd dienen te worden

In de Zaken API:

```http
GET /api/v1/zaken/?archiefnominatie=<archiefnominatie>&archiefactiedatum__lt=<datum>&archiefstatus=nog_te_archiveren
```

### Archiveren van zaken

In de Zaken API:

```http
PATCH /api/v1/zaken/<uuid>
{
  "archiefstatus": "gearchiveerd"
}
```

Hierna is de Zaak niet meer wijzigbaar (zelfde situatie als afgesloten zaak).

### Zaak-dossier overdragen

In de verschillende APIs zijn dit GET operaties die voor alle relevante Zaak-dossier resources moeten werken.
Na overdragen moet de `Zaak.Archiefstatus` gezet worden op `overgedragen`. Hierna kan het zaak-dossier worden vernietigd.

### Zaak-dossier vernietigen

In de verschillende APIs zijn dit DELETE operaties die voor alle relevante Zaak-dossier resources moeten werken.
Er vind **geen** validatie plaats op de archiefactietermijn, wel moet er een aparte scope komen die DELETE toe staat.

# TODO

* Overige attributen uit TODO verwerken
* Schrijfbaar brondatum attribuut definieren
* Ergens opschrijven dat we niet alles automatisch gaan doen, aangezien sommige velden tekstueel beschrijven hoe de brondatum bepaald moet worden.
