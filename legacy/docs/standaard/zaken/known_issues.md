---
title: "Known Issues Zaken API"
date: '04-04-2024'
weight: 10
layout: page-with-side-nav
---

# Known Issues Zaken API

## zrc-issue-001

Versie   | Release datum
-------- | -------------
1.5.1    | 26-09-2023
1.5.0    | 22-08-2023

**Issue**: Het is niet geheel duidelijk welke expand precies ondersteund moeten worden (zie [#2397](https://github.com/VNG-Realisatie/gemma-zaken/issues/2397)).

**Workaround**: In de spreadsheet [expand.xlsx](https://github.com/VNG-Realisatie/gemma-zaken/files/14162505/expand.1.xlsx) wordt precies beschreven welke expands ondersteund moet worden.

**Fix**: Alle expands die ondersteund moeten worden specificeren in de OAS zoals voorgesteld in [PR #2377](https://github.com/VNG-Realisatie/gemma-zaken/pull/2377).

## zrc-issue-002

Versie   | Release datum
-------- | -------------
1.5.1    | 26-09-2023
1.5.0    | 22-08-2023

**Issue**: Endpoints `/rollen` en `zaakobjecten` ondersteunen geen expand maar laten wel een "_expand" attribuut zien (zie [#2414](https://github.com/VNG-Realisatie/gemma-zaken/issues/2414) en [2412](https://github.com/VNG-Realisatie/gemma-zaken/issues/2412)).

**Workaround**: Het "_expand" attribuut niet gebruiken op de plekken die hierboven zijn genoemd.

**Fix**: Verwijderen van het "_expand" attribuut bij de genoemde endpoints zoals voorgesteld in [PR #2427](https://github.com/VNG-Realisatie/gemma-zaken/pull/2427).

## zrc-issue-003

Versie   | Release datum
-------- | -------------
1.5.1    | 26-09-2023
1.5.0    | 22-08-2023

**Issue**: Het is niet duidelijk of in alle geledingen van de expand parameter geëxpandeerd moeten worden of alleen de laatste (zie [#2398](https://github.com/VNG-Realisatie/gemma-zaken/issues/2398)).

**Fix**: Opnemen van de volgende verduidelijkende tekst in de specificatie: "Bij geneste expand worden alle velden die in het pad (met punt-notatie) voorkomen geëxpandeerd."


## zrc-issue-004

Versie   | Release datum
-------- | -------------
1.5.1    | 26-09-2023
1.5.0    | 22-08-2023

**Issue**: Via de veelgebruikte openbare link https://zaken-api.vng.cloud is de genereerde versie van de OAS van de Zaken API te zien (klik [hier](https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/vng-Realisatie/zaken-api/1.5.1/src/openapi.yaml)). Deze OAS is gegenereerd vanuit de code van de referentie-implementatie voor technische doeleinden.  Echter deze OAS is niet normatief, incompleet en bevat zelfs fouten. Dit kan tot misverstanden leiden als de bezoeker hiervan niet op de hoogte is (zie [#2424](https://github.com/VNG-Realisatie/gemma-zaken/issues/2424))

**Workaround**: De normatieve en goede OAS van de Zaken API is hier te vinden: https://vng-realisatie.github.io/gemma-zaken/standaard/zaken.

**Fix**: De link laten verwijzen naar de goede OAS. Dit vereist  een wijziging in de referentie-implementatie.