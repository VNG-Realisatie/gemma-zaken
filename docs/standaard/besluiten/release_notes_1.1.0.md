---
title: "Besluiten API 1.1.0"
weight: 10
layout: page-with-side-nav
---

# Release notes Besluiten API 1.1.0

In de Besluiten API 1.1.0 zijn de volgende issues verwerkt:

- [Issuelijst Milestone "ZGW 1.6.0" voor Besluiten API 1.1.0](https://github.com/VNG-Realisatie/gemma-zaken/issues?q=is%3Aissue%20state%3Aopen%20milestone%3A%22ZGW%201.6%22%20label%3Abesluiten-api)

## Expand-mechanisme toegevoegd

In de vorige release van de ZGW API's was het expand-mechanisme alleen beschikbaar in de Zaken API. In de nieuwe release is dit mechanisme ook mogelijk gemaakt voor de hieronder genoemde andere API's in de ZGW-familie waaronder dus ook de Besluiten API.

- Documenten API
- Besluiten API
- Catalogi API

Net zoals bij de Zaken API is de expand gedefinieerd op alle relevante endpoints en kan de expand tot willekeurige diepte worden uitgevoerd.

Gerelateerde issues:

- [#2507](https://github.com/VNG-Realisatie/gemma-zaken/issues/2507) Ik wil graag dat de Expand overal wordt toegepast en niet alleen voor de ZRC.
- [#2472](https://github.com/VNG-Realisatie/gemma-zaken/issues/2472) BRC: expand op besluit.