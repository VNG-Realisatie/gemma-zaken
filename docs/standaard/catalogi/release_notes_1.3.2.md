---
title: "Release notes Catalogi API 1.3.2"
weight: 10
layout: page-with-side-nav
---

# Release notes Catalogi API 1.3.2

## Expand-mechanisme toegevoegd

In de vorige release van de ZGW API's was het expand-mechanisme alleen beschikbaar in de Zaken API. In de nieuwe release is dit mechanisme ook mogelijk gemaakt voor de hieronder genoemde andere API's in de ZGW-familie waaronder dus ook de Catalagi API.

- Documenten API
- Besluiten API
- Catalogi API

Net zoals bij de Zaken API is de expand gedefiniëerd op alle relevante endpoints en kan de expand tot willekeurige diepte worden uitgevoerd.

### Gerelateerde issues:

- [#2487](https://github.com/VNG-Realisatie/gemma-zaken/issues/2487) Zou het expand-mechanisme ook niet in de Catalogi API zelf bruikbaar moeten zijn?
- [#2507](https://github.com/VNG-Realisatie/gemma-zaken/issues/2507) Ik wil graag dat de Expand overal wordt toegepast en niet alleen voor de ZRC


## Historiemodel

### Betere documentatie historiemodel

Sinds de release van de vorige versie van de Catalogi API is er veel onduidelijkheid over het historiemodel. In deze versie is een [Primer document](https://vng-realisatie.github.io/gemma-zaken/standaard/catalogi/historie_model/historie_model.html) toegevoegd waarin het historiemodel wordt uitgelegd aan de hand van diagrammen met voorbeeldberichten. 

### Diverse bug fixes

In de vorige release van de Catalogi API bleek het nieuwe historiemodel nog niet helemaal volwassen te zijn en kwamen er diverse bugs naar boven tijdens de implementaties. Zie [hier](https://github.com/VNG-Realisatie/gemma-zaken/issues?q=is%3Aissue%20state%3Aopen%20label%3AHistoriemodel%20milestone%3A%22ZGW%201.6%22) de lijst met bugs fixes die we in deze versie hebben doorgevoerd.

## Allerhande issues opgelost

### PUT en PATCH toegevoegd voor catalogussen

Deze essentiële operaties ontbraken in de OAS-specificatie en zijn nu toegevoegd.

#### Gerelateerde issues:

- [#2560](https://github.com/VNG-Realisatie/gemma-zaken/issues/2560) ZTC: update method for catalog

### Het veld "catalogus" deprecated gemaakt in de POST/PUT/PATCH en business rule ztc-013 verwijderd

In de POST/PUT/PATCH voor Resultaattype en Roltype kan een catalogus worden meegegeven in de request.
Dit is overbodig want je geeft al een zaaktype mee die een catalogus heeft. Naar aanleiding van dit inzicht is tevens de business rule ztc-013 verwijderd.

#### Gerelateerde issues:

- [#2468](https://github.com/VNG-Realisatie/gemma-zaken/issues/2468) ZTC: onterecht catalogus in POST/PUT/PATCH voor Resultaattype en Roltype
- [#2482](https://github.com/VNG-Realisatie/gemma-zaken/issues/2482) ZTC: business rule ztc-013 is vaag en moet aangescherpt


### Filtering op objecttypen verduidelijkt

Beschrijvingen van de query parameters aangespast (zie deze [commit](https://github.com/VNG-Realisatie/gemma-zaken/commit/016e46987430ba9ae2c0a6efc2821cf6d9580970))


#### Gerelateerde issues:

- [#2479](https://github.com/VNG-Realisatie/gemma-zaken/issues/2479) ZTC 1.3 filter op status bij objecttypes zonder status onduidelijk


### Problemen met relatie resultaattype-besluittype en resultaattype-informatieobjecttype opgelost

Problemen omtrennt de relaties resultaattype-besluittype en resultaattype-informatieobjecttype opgelost door beschrijvingen aan te passen en het veld "besluittypen" optioneel te maken (zie [commit](https://github.com/VNG-Realisatie/gemma-zaken/commit/30d6b8e830e721d450ead1925b5acad1f612ce71))

#### Gerelateerde issues:

- [#2467](https://github.com/VNG-Realisatie/gemma-zaken/issues/2467) ZTC: problemen relatie resultaattype-besluittype en resultaattype-informatieobjecttype oplossen

### Business rule ztc-010 herschreven

Business rule ztc-010 was onduidelijk en is herschreven (zie deze [commit](https://github.com/VNG-Realisatie/gemma-zaken/commit/713d1442b5c5aa87f55739007454ea61ead3a486))

#### Gerelateerde issues:

- [#2456](https://github.com/VNG-Realisatie/gemma-zaken/issues/2456) Business rule ztc-010 herschrijven

### Per abuis verdwenen attribuut weer toegevoegd aan specificatie

In de berichten van operatie `POST /besluittypen` was het attribuut "zaaktypen" per ongeluk weggevallen. Dit element in deze versie weer toegevoegd.

#### Gerelateerde issues:

- [#2437](https://github.com/VNG-Realisatie/gemma-zaken/issues/2437) ZTC 1.3 POST besluittype: wat is er met zaaktypen gebeurd.

### Datum/tijd formaat voor eigenschappen duidelijk gespecificeerd

Het formaat van datum/tijd waren niet scherp gespecificeerd in de beschrijvingen voor eigenschappen. Dat is nu strak getrokken.

#### Gerelateerde issues:

- [#1751](https://github.com/VNG-Realisatie/gemma-zaken/issues/1751) As a developer, I want to have standardized schema descriptions for eigenschappen.