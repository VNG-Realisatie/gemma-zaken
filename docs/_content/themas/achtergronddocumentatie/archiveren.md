---
title: "Archiveringsproces *"
date: '25-02-2019'
weight: 70
---

Zie: [#751](https://github.com/VNG-Realisatie/gemma-zaken/issues/751)

\* Term gekozen t.b.v. de leesbaarheid. Echter, het gaat met name er om dat
organisaties hun informatiehuishouding op orde hebben en houden.

In essentie bestaat het archiveringsproces uit 3 stappen:

1. Proces in het kort:
   1. een zaak wordt afgesloten met een *einddatum*;
   2. doorloopt hierna eerst een *procestermijn* (dit is de periode waarin de
      zaak nog gebruikt wordt voor de taakuitoefening; bijv. een zaak waarin
      een bouwvergunning is verleend, blijft in de procestermijn ten behoeve
      van toezicht);
   3. het einde van de procestermijn heet de *brondatum*;
   4. hierna begint de *archiefactietermijn* ook wel *bewaartermijn* genoemd;
   5. na de *bewaartermijn* moet de archiefactie worden uitgevoerd, hetzij
      (permanent) bewaren hetzij vernietigen;
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

## Algemeen

### Definitie zaak-dossier

Zie: [#750](https://github.com/VNG-Realisatie/gemma-zaken/issues/750)

Een zaakdossier is het geheel van zaak-metadata, bijbehorende
informatieobjecten incl. metadata, statussen, resultaten en besluiten, en
gerelateerde entiteiten:

* De deelzaken (of hoofdzaak)
* De relatie met vervolgzaken (of is zelf vervolgzaak)
* Gerelateerde zaken (via zakenrelatie)
* Zaakobjecten: objecten uit het RGBZ of RSGB waarop de zaak betrekking heeft
* Andere zaakobjecten: objecten waarop de zaak betrekking heeft maar die geen
  onderdeel uitmaken van RGBZ of RSGB. Dit kunnen business objecten zoals
  melding of aanvraag zijn.

### Wat gebeurt er als een zaak-dossier *blijvend bewaard* wordt?

Het zaak-dossier wordt overgedragen naar een bewaarplaats.

### Wat gebeurt er als een zaak-dossier *vernietigd* wordt?

Het vernietigen is het definitief verwijderen van data volgens de NEN2082 (Eis 80):

> Vernietigen van archiefstukken/archiefbestanddelen moet zo gebeuren dat deze
> niet meer op enigerlei wijze kunnen worden gereproduceerd.

### Bepalen van de aan archivering gerelateerde attributen voor `ResultaatType`

Zie: [Selectielijst gemeenten en intergemeentelijke organen 2017](https://vng.nl/files/vng/20170706-selectielijst-gemeenten-intergemeentelijke-organen-2017.pdf)

Het ZTC dient ingericht te worden volgens de selectielijst. Het ZTC dient
validaties uit te voeren om te zorgen dat inrichting correct is.

*Voorbeeld*

Als `ResultaatType.BrondatumArchiefprocedure.Afleidingswijze` wordt ingesteld
op `eigenschap` moet het ZTC valideren dat het betreffende `ZaakType` een
`Eigenschap` heeft met als `naam`, de waarde die staat in
`ResultaatType.BrondatumArchiefprocedure.datumkenmerk`.

### Berekenen van de `Zaak.Archiefactiedatum`

1. Bepaal de *brondatum* van de `Zaak` door de `ResultaatType.BrondatumArchiefprocedure.Afleidingswijze` te raadplegen:

   Afleidingswijze | Waarde van *brondatum*
   --- | ---
   `afgehandeld` | `Zaak.Einddatum`
   `gerelateerde zaak` | *TODO: Wat is dit precies?* De hoogste datum van van alle `Zaak.GerelateerdeZaak.Einddatum` of `Zaak.Einddatum` ([#776](https://github.com/VNG-Realisatie/gemma-zaken/issues/776))
   `hoofdzaak` | `Zaak.HoofdZaak.Einddatum`
   `ingangsdatum besluit` | *TODO* `Zaak.Besluit.Ingangsdatum` ([#775](https://github.com/VNG-Realisatie/gemma-zaken/issues/775))
   `vervaldatum besluit` | *TODO* `Zaak.Besluit.Vervaldatum` ([#775](https://github.com/VNG-Realisatie/gemma-zaken/issues/775))
   `ander datumkenmerk` | Handmatig bepalen.
   `eigenschap` | De waarde van de `Zaak.Eigenschap` met de `naam` die overeenkomt met de waarde uit `ResultaatType.BrondatumArchiefprocedure.Datumkenmerk`
   `termijn` | `Zaak.Einddatum` + `ResultaatType.BrondatumArchiefprocedure.Procestermijn`
   `zaakobject` | De waarde van het attribuut op `Zaak.ZaakObject.Object`, van type `ResultaatType.BrondatumArchiefprocedure.Objecttype`, waarvan de `naam` van het attribuut overeenkomt met de waarde uit `ResultaatType.BrondatumArchiefprocedure.Datumkenmerk`

2. Als de *brondatum* is bepaald:

   `Zaak.Archiefactiedatum` = *brondatum* + `Zaak.Resultaat.ResultaatType.Archiefactietermijn`

User Story: [#345](https://github.com/VNG-Realisatie/gemma-zaken/issues/345)

#### Foutsituaties bij het berekenen van *brondatum*

In sommige situaties kan de *brondatum* niet worden bepaald. Dit is niet altijd een foutsituatie. In het algemeen moet een fout optreden als de configuratie in het ZTC niet overeenkomt met de inrichting van de `Zaak` of gerelateerde gegevens, of als er ongeldige waardes zijn.

*Voorbeeld*

Als de afleidingswijze een `eigenschap` betreft en de `Zaak` heeft zo'n `eigenschap` niet (zelfs als de `Zaak` de `eigenschap` volgens het `Zaaktype` wel zou moeten hebben), dan treed een fout op. Ook als de `eigenschap` wel bestaat maar de waarde is geen geldige datum, dan treed een fout op. Echter, als de `eigenschap` bestaat en de waarde is leeg, dan kan de *brondatum* niet worden bepaald en blijft de `Zaak.archiefactiedatum` leeg

### Wanneer wordt de `Zaak.Archiefactiedatum` berekend?

De `Zaak.Archiefactiedatum` wordt berekend als aan de volgende voorwaarden wordt voldaan:

1) Er wordt een `Resultaat` voor de `Zaak` aangemaakt of gewijzigd; hiermee wordt het `ResultaatType` bekend,
2) De eind `Status` wordt gezet (eind `StatusType` wordt gekoppeld) waardoor de einddatum bekend wordt,
3) De *brondatum* kan worden berekend,
4) De `ResultaatType.archiefactietermijn` van het `Zaak.Resultaat` is valide.

## API ondersteuning

### Opvragen lijst van zaken die gearchiveerd dienen te worden

In de Zaken API:

```http
GET /api/v1/zaken/?archiefnominatie=<archiefnominatie>&archiefactiedatum__lt=<datum>&archiefstatus=nog_te_archiveren
```

User Stories: [#347](https://github.com/VNG-Realisatie/gemma-zaken/issues/347), [#348](https://github.com/VNG-Realisatie/gemma-zaken/issues/348)

### Archiveren van zaken

In de Zaken API:

```http
PATCH /api/v1/zaken/<uuid>
{
  "archiefstatus": "gearchiveerd"
}
```

Hierna is de Zaak in principe niet meer wijzigbaar (zelfde situatie als afgesloten zaak). Uit praktische overwegingen is er geen validatie aan de kant van de provider hierop maar dient de consumer hier op verantwoorde wijze mee om te gaan.

### Zaak-dossier overdragen

In de verschillende APIs zijn dit `GET` operaties die voor alle relevante Zaak-dossier resources moeten werken.
Na overdragen moet de `Zaak.archiefstatus` gezet worden op `overgedragen`. Hierna kan het zaak-dossier worden vernietigd.

### Zaak-dossier vernietigen

In de verschillende APIs zijn dit `DELETE` operaties die voor alle relevante Zaak-dossier resources moeten werken.
Er vind **geen** validatie plaats op de `Zaak.archiefactietermijn`, wel moet er een aparte scope komen die `DELETE` toe staat.

User Story: [#349](https://github.com/VNG-Realisatie/gemma-zaken/issues/349)

# Relevante attributen uit het informatiemodel

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

## Overige

Onderstaande attributen uit RGBZ 2.0.2 zijn geidentificeert als relevant maar
hebben nog geen plek gekregen in het verhaal.

* `Zaak.StartdatumBewaartermijn` (nieuw!) De datum die de start markeert van de termijn waarop het zaakdossier vernietigd moet worden.
* `Zaak.Procesobject`
* `Zaak.Selectielijstklasse`
* `ResultaatType.BrondatumArchiefprocedure.EinddatumBekend`
* `ResultaatType.Procesobjectaard`
* `ZaakType.SelectielijstProcestype`
* `ZaakType.Archiefclassificatie`
* `Zaak-InformatieobjectType.Archiefregime`
* `Zaak-InformatieobjectType.Vernietigingstermijn` (relatie) De termijn waarna informatieobjecten, van het `InformatieobjectType` bij zaken van het `ZaakType` met een resultaat van het `ResultaatType`, vernietigd moeten worden.

### TODO

* Overige attributen uit TODO verwerken
* Schrijfbaar brondatum attribuut definieren
* Ergens opschrijven dat we niet alles automatisch gaan doen, aangezien sommige velden tekstueel beschrijven hoe de brondatum bepaald moet worden.
