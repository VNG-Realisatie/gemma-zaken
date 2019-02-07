# Archiveren (voor dummies)

## [WIP] Archiveringsproces *

Zie: [#751](https://github.com/VNG-Realisatie/gemma-zaken/issues/751)

\* Term gekozen t.b.v. de leesbaarheid. Echter, het gaat met name er om dat 
organisaties hun informatiehuishouding op orde hebben en houden.

In essentie bestaat het archiveringsproces uit 2 stappen:

1. Een zaak-dossier wordt *blijvend bewaard* of kan worden *vernietigd* en
   staat aaangegeven op de `Zaak` (`Zaak.Archiefnominatie`).
2. Vanaf een *bepaalde datum* (`Zaak.Archiefactiedatum`) **moet** het 
   zaak-dossier worden *overgebracht naar een archiefbewaarplaats* of worden 
   *vernietigd*.

Opmerkingen:

1. Een zaak-dossier **mag** eerder worden *overgebracht naar een 
   archiefbewaarplaats*.
2. Het is niet altijd, vanaf het aanmaken van een zaak, duidelijk wat er mee 
   moet gebeuren of wanneer dat moet gebeuren.
3. Het archiversproces doorloopt verschillende stadia te volgen via de
   `Zaak.Archiefstatus`.

### [WIP] Definitie zaak-dossier

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

TODO

### Wat gebeurt er als een zaak-dossier *vernietigd* wordt?

TODO

## Gerelateerde attributen

* `Zaak.Archiefnominatie` Aanduiding of het zaakdossier blijvend bewaard of na een bepaalde termijn vernietigd moet worden:

    * `null`
    * `Blijvend bewaren`
    * `Vernietigen`
    
* `Zaak.Archiefstatus` De fase waarin het zaakdossier zich qua archivering bevindt:

    * `nog te archiveren` (standaardwaarde)
    * `gearchiveerd`
    * `gearchiveerd (procestermijn onbekend)`
    * `vernietigd`
    * `overgedragen`
    
  Als de `Archiefstatus` `gearchiveerd` of `gearchiveerd (procestermijn onbekend)` is, dan is het zaakdossier niet-wijzigbaar.

* `Zaak.Archiefactiedatum` De datum waarop het gearchiveerde zaakdossier vernietigd moet worden dan wel overgebracht moet worden naar een archiefbewaarplaats. 

* `ResultaatType.Archiefnominatie` Aanduiding die aangeeft of `Zaak`en met een resultaat van dit `ResultaatType` blijvend moeten worden bewaard of (op termijn) moeten worden vernietigd . 

* `ResultaatType.Procestermijn` De periode dat het zaakdossier na afronding van de zaak actief gebruikt en/of geraadpleegd wordt ter ondersteuning van de taakuitoefening van de organisatie.

* `ResultaatType.Archiefactietermijn` De termijn, na het vervallen van het bedrijfsvoeringsbelang, waarna het zaakdossier (de `Zaak` met alle bijbehorende `Informatieobject`en) van een `Zaak` met een resultaat van dit `ResultaatType` vernietigd of overgebracht (naar een archiefbewaarplaats) moet worden. 

* `ResultaatType.BrondatumArchiefprocedure.Afleidingswijze` Wijze van bepalen van de brondatum.

  * `afgehandeld` -> `Zaak.Einddatum`
  * `ander datumkenmerk` -> `?` *De termijn start op de datum die is vastgelegd in een ander datumveld dan de datumvelden waarop de overige waarden (van deze attribuutsoort) betrekking hebben.*
  * `eigenschap` -> `?` *De termijn start op de datum die vermeld is in een zaaktype-specifieke eigenschap (zijnde een `datumveld`).*
  * `gerelateerde zaak` -> `Zaak.GerelateerdeZaak.Einddatum` (welke gerelateerde zaak als er meer zijn?) of `Zaak.Einddatum` *De termijn start op de datum waarop de gerelateerde zaak is afgehandeld (ZAAK.Einddatum of ZAAK.Gerelateerde_zaak.Einddatum in het RGBZ).*
  * `hoofdzaak` -> `Zaak.HoofdZaak.Einddatum`
  * `ingangsdatum besluit` -> `Besluit.Ingangsdatum` 
  * `termijn` -> `?` *De termijn start een vast aantal jaren na de datum waarop de zaak is afgehandeld (`Zaak.Einddatum` in het RGBZ).*
  * `vervaldatum besluit` -> `Besluit.Vervaldatum`. 
  * `zaakobject` -> `ZaakObject.Object.DatumEindeGeldigheid` (niet alle objecten hebben dat?) *De termijn start op de einddatum geldigheid van het zaakobject waarop de zaak betrekking heeft (bijvoorbeeld de overlijdendatum van een Persoon).*

TODO:

* `Zaak.StartdatumBewaartermijn` (nieuw!) De datum die de start markeert van de termijn waarop het zaakdossier vernietigd moet worden. 
* `Zaak.Procesobject`
* `Zaak.Selectielijstklasse`
* `ResultaatType.BrondatumArchiefprocedure.*`
* `ResultaatType.Procesobjectaard`
* `ZaakType.SelectielijstProcestype`
* `ZaakType.Archiefclassificatie`
* `Zaak-InformatieobjectType.Archiefregime`
* `Zaak-InformatieobjectType.Vernietigingstermijn` (relatie) De termijn waarna informatieobjecten, van het `InformatieobjectType` bij zaken van het `ZaakType` met een resultaat van het `ResultaatType`, vernietigd moeten worden. 

## Berekenen van de `Zaak.Archiefactiedatum`

De `brondatum` is af te leiden via 
`ResultaatType.BrondatumArchiefprocedure.Afleidingswijze`. In een aantal 
gevallen is dit geen 1-op-1 mapping maar is additionele informatie nodig.

TODO: Additionele gegevens.

`Zaak.Archiefactiedatum` = `brondatum` + `Zaak.ResultaatType.Procestermijn` + `Zaak.ResultaatType.Archiefactietermijn`

## API ondersteuning

### Opvragen lijst van zaken die **blijvend bewaard** dienen te worden

In de Zaken API:

`/api/v1/zaken/?archiefnominatie=blijvend_bewaren&archiefactiedatum__lt=<datum>`

### Opvragen lijst van zaken die **vernietigd** dienen te worden

In de Zaken API:

`/api/v1/zaken/?archiefnominatie=vernietigen&archiefactiedatum__lt=<datum>`
