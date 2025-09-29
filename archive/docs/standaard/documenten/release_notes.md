---
title: "Release Notes Documenten API"
date: "13-03-2024"
weight: 10
layout: page-with-side-nav
---

# Release Notes Documenten API

## Versie 1.5.0

| Versie | Releasedatum |
| ------ | ------------ |
| 1.5.0  | 14-03-2024   |

- property `inhoudIsVervallen` bij resource 'enkelvoudiginformatieobjecten' toegevoegd (zie
  toelichting hieronder).
- regel die PUT en PATCH-operaties op 'enkelvoudiginformatieobjecten' alleen toestaat voor
  informatieobjecten waarvan de 'status NIET `definitief`' is
  ([drc-010](index.md#bijwerken-van-documenten-drc-010)), is in overeenstemming met vervallen van
  deze regel in versie 1.4.0 uit de OAS verwijderd.

### Toelichting bij toevoeging property 'inhoudIsVervallen'

#### Beschrijving

"Geeft aan of de inhoud van het informatieobject vervallen (dus niet langer geldig) is."

#### Toegestane waarden

| Waarde  | Beschrijving                                          |
| ------- | ----------------------------------------------------- |
| `null`  |
| `true`  | De inhoud van het informatieobject is vervallen       |
| `false` | De inhoud van het informatieobject is niet vervallen. |

#### Rationale voor toevoeging

- Gebleken behoefte aan een manier om aan te geven dat de inhoud van een informatieobject niet
  langer 'van belang' is, bijvoorbeeld omdat het is vervangen door een ander informatieobject met
  andere inhoud dat gaat over hetzelfde onderwerp.
  [De consultatie naar (onder andere) toevoeging van deze property](https://github.com/VNG-Realisatie/gemma-zaken/discussions/2407)
  wees uit dat deze property in de standaard kon worden opgenomen.

#### Gebruik

Het begrip 'vervallen' in deze indicatie moet gelezen worden als 'ongeldig geworden'. Geldigheid
moet in deze context zowel 'breed' als 'eng' gelezen worden.

- Breed in de zin dat verlies van geldigheid van de inhoud van een informatieobject zowel het gevolg
  kan zijn van een formele procedure, zoals de herroeping van een besluit, als van informele
  handelingen, zoals een bouwtekening waarvan de inhoud door het verschijnen van een meer actuele
  illustratie achterhaald is. Hoewel we in het dagelijks taalgebruik in het laatste geval
  waarschijnlijk zouden zeggen dat de bouwtekening "niet meer actueel is", benoemen we die in de
  context van deze indicatie als "niet meer geldig, dus vervallen".
- Eng in de zin dat verlies van geldigheid niet betekent dat een informatieobject in het geheel geen
  waarde meer heeft. Een herroepen besluit kan immers aanleiding geven voor aantekenen van bezwaar
  of beroep. En de 'vervangen' bouwtekening kan vanuit cultuurhistorisch perspectief best heel
  interessant (blijken te) zijn.

## Versie 1.4.3

| Versie | Releasedatum |
| ------ | ------------ |
| 1.4.3  | 27-10-2023   |

- `lock` attribuut weer toegevoegd aan groepsattribuut `bestandsdelen` aan responses GET/GET List
  /Informatieobjecten (#2293) Dit bleek in versie 1.4.1 niet volledig opgelost.

## Versies 1.4.2 / 1.3.2 / 1.2.5

| Versie | Releasedatum |
| ------ | ------------ |
| 1.4.2  | 26-09-2023   |
| 1.3.2  | 26-09-2023   |
| 1.2.5  | 26-09-2023   |

- Ontbrekende query parameters toegevoegd aan `documenten_zoek` operatie (#2294)
- `expand` parameter toegevoegd aan `documenten_zoek` operatie (#2345)
- Versienummers in documentatie specifiek gemaakt (#2301)
- Parameternaam `UUID__IN` in `documenten_zoek` operatie correct gespeld in OAS yaml (#2300)
- Response bodies verwijderd uit `HEAD` operaties (#2328)

## Versies 1.4.1 / 1.3.1 / 1.2.4

| Versie | Releasedatum |
| ------ | ------------ |
| 1.4.1  | 29-08-2023   |
| 1.3.1  | 29-08-2023   |
| 1.2.4  | 29-08-2023   |

- `lock` attribuut weer toegevoegd aan groepsattribuut `bestandsdelen` aan responses GET/GET List
  /Informatieobjecten (#2293)

## Versie 1.4.0

| Versie | Releasedatum |
| ------ | ------------ |
| 1.4.0  | 22-08-2023   |

- Expand mogelijkheid toegevoegd teneinde met één aanroep meer informatie op te halen en zo de
  performance te verbeteren. (#2235)
- `trefwoorden` toegevoegd aan resource `Informatieobject`. (#2057)
- Validatie op `informatieobjecttype` bij wijzigen `Informatieobject` vervallen (#2241)

## Versie 1.3.0

| Versie | Releasedatum |
| ------ | ------------ |
| 1.3.0  | 29-03-2023   |

- Gelockte documenten kunnen niet verwijderd worden (#1956)
- Telefoonnummer aan relatieklasse `Verzendingen` toegevoegd (#2113)
- Informatieobjecttype aanpasbaar gemaakt (#1777)

## Versie 1.2.0

| Versie | Releasedatum |
| ------ | ------------ |
| 1.2.0  | 19-12-2022   |

- Ontbrekende attributen RGBZ 2 toegevoegd tbh voldoen aan TMLO (#1884)
- Scope `geforceerd-bijwerken` toegevoegd om Informatieobjecten met status `definitief` te kunnen
  bewerken (#1859)
- Relatieklasse `Verzendingen` toegevoegd (#1785)
- Voorbeeldwaarde attribuut `taal` aangepast naar correcte waarde (#1775)
- `documenten_zoek` endpoint toegevoegd (#1881)

## Versies 1.1.0 / 1.0.1 / 1.0.0

| Versie | Releasedatum |
| ------ | ------------ |
| 1.1.0  | 24-05-2021   |
| 1.0.1  | 2019-12-16   |
| 1.0.0  | 2019-11-18   |
