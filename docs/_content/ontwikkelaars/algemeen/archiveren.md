# Archiveren (voor dummies)

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


TODO:

* `Zaak.StartdatumBewaartermijn` (nieuw!) De datum die de start markeert van de termijn waarop het zaakdossier vernietigd moet worden. 
* `Zaak.Procesobject`
* `Zaak.Selectielijstklasse`
* `ResultaatType.BrondatumArchiefprocedure`
* `ResultaatType.Procesobjectaard`
* `ZaakType.SelectielijstProcestype`
* `ZaakType.Archiefclassificatie`
* `Zaak-InformatieobjectType.Archiefregime`
* `Zaak-InformatieobjectType.Vernietigingstermijn` (relatie) De termijn waarna informatieobjecten, van het `InformatieobjectType` bij zaken van het `ZaakType` met een resultaat van het `ResultaatType`, vernietigd moeten worden. 

## Berekenen van de `Zaak.Archiefactiedatum`

TODO: Eerste idee maar dit is te simplistisch, want de brondatum is 
afhankelijk van het `ResultaatType.afleidingswijzeBrondatumArchiefprocedure`.
Voor de leesbaarheid zetten we dit nu even op de `Zaak.Einddatum`:

`brondatum` = `Zaak.Einddatum`

`Zaak.Archiefactiedatum` = `brondatum` + `Zaak.ResultaatType.Procestermijn` + `Zaak.ResultaatType.Archiefactietermijn`

## Archiveringsproces

Eigenlijk is het hele archiveringsproces te volgen via de `Zaak.Archiefstatus`.

TODO: Wat er precies wel en niet blijft bestaan is nog onduidelijk

## Bevragen

### Opvragen van een lijst met te **archiveren** zaken

In de Zaken API:

`/api/v1/zaken/?archiefnominatie=blijvend_bewaren&archiefactiedatum__lt=<datum>`

### Opvragen van een lijst met te **vernietigen** zaken

In de Zaken API:

`/api/v1/zaken/?archiefnominatie=vernietigen&archiefactiedatum__lt=<datum>`
