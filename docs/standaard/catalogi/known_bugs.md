---
title: "Known Bugs Catalogi API"
date: '04-04-2024'
weight: 10
layout: page-with-side-nav
---

# Known Bugs Catalogi API

## Versie 1.3.1 / 1.3.0

Versie   | Release datum
-------- | -------------
1.3.1    | 26-09-2023
1.3.0    | 22-08-2023

- **Bug**: Attribuut "zaaktypen" is onterecht weggevallen in POST-operatie van `/besluittypen` tijdens het genereren van OAS (zie [#2437](https://github.com/VNG-Realisatie/gemma-zaken/issues/2437)). <br>
**Fix**: Terugzetten van het weggevallen attribuut in de volgende release.