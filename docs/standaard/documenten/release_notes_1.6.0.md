---
title: "Release Notes Documenten API 1.6.0"
weight: 10
layout: page-with-side-nav
---

# Release notes Documenten API 1.6.0

In de Documenten API 1.6.0 zijn de volgende issues verwerkt:

- [Issuelijst Milestone "ZGW 1.6.0" voor Documenten API 1.6.0](https://github.com/VNG-Realisatie/gemma-zaken/issues?q=is%3Aissue%20state%3Aopen%20milestone%3A%22ZGW%201.6%22%20label%3Adocumenten-api)

## Expand-mechanisme toegevoegd

In de vorige release van de ZGW API's was het expand-mechanisme alleen beschikbaar in de Zaken API. In de nieuwe release is dit mechanisme ook mogelijk gemaakt voor de hieronder genoemde andere API's in de ZGW-familie waaronder dus ook de Documenten API.

- Documenten API
- Besluiten API
- Catalogi API

Net zoals bij de Zaken API is de expand gedefiniëerd op alle relevante endpoints en kan de expand tot willekeurige diepte worden uitgevoerd.

### Gerelateerde issues:

- [#2507](https://github.com/VNG-Realisatie/gemma-zaken/issues/2507) Ik wil graag dat de Expand overal wordt toegepast en niet alleen voor de ZRC.
- [#2485](https://github.com/VNG-Realisatie/gemma-zaken/issues/2485) In de OAS van de Documenten API worden de geneste expands in het informatieobjecttype niet weergegeven.
- [#2469](https://github.com/VNG-Realisatie/gemma-zaken/issues/2469) DRC: is er nu wel of geen expand op objectinformatieobjecten?
- [#2405](https://github.com/VNG-Realisatie/gemma-zaken/issues/2405) ZRC 1.5/DRC 1.4 Expand op lijst documenten bij de zaak.
- [#2370](https://github.com/VNG-Realisatie/gemma-zaken/issues/2370) Documenten API: Als ontwikkelaar wil ik expand op ObjectInformatieObjecten.

## Veld voor bekendmaking aan initiatiefnemer toegevoegd

Boolean veld "tonenAanInitiator" toegevoegd (default: false) om aan te geven of het document getoond mag worden aan de initiator van de zaak waarin het document is opgenomen.

### Gerelateerde issues:

- [#2546](https://github.com/VNG-Realisatie/gemma-zaken/issues/2546) DRC: veld voor bekendmaking aan initiatiefnemer


## Trefwoorden toegevoegd aan PATCH-operatie

Trefwoorden zaten wel in de POST en PUT maar niet in de PATCH. Nu ook aan de PATCH toegevoegd (zie deze [commit](https://github.com/VNG-Realisatie/gemma-zaken/commit/fe9f85f039637a678986473df03a1e592c75e8aa)).

- [#2449](https://github.com/VNG-Realisatie/gemma-zaken/issues/2449) DRC 1.5: PATCH op EIO heeft geen trefwoorden.

## Verzenddatum niet meer verplicht bij uitgaande documenten

Bij uitgaande documenten is het niet meer verplicht om de verzenddatum op te geven, zie [commit](https://github.com/VNG-Realisatie/gemma-zaken/commit/943bad2199a4b942cd99fd8160c1a68f338e4dff).

### Gerelateerde issues:

- [#2188](https://github.com/VNG-Realisatie/gemma-zaken/issues/2188) DRC: Als zaakbehandelaar wil ik een uitgaand document opstellen met een geadresseerde, voordat ik de verzenddatum weet.