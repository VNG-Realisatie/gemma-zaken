---
title: "Known Bugs Zaken API"
date: '04-04-2024'
weight: 10
layout: page-with-side-nav
---

# Known Bugs Zaken API

## Versie 1.5.1 / versie 1.5.0

Versie   | Release datum
-------- | -------------
1.5.1    | 26-09-2023
1.5.0    | 22-08-2023 

- **Bug**: Het is niet geheel duidelijk welke expand precies ondersteund moeten worden (zie [#2397](https://github.com/VNG-Realisatie/gemma-zaken/issues/2397)). <br>
**Fix**: In de spreadsheet [expand.xlsx](https://github.com/VNG-Realisatie/gemma-zaken/files/14162505/expand.1.xlsx) wordt precies beschreven welke expands ondersteund moet worden. In de volgende release zullen alle expands in de OAS gespecificeerd zijn zodat deze aanvullende specificatie niet meer nodig zal zijn.

- **Bug**: Endpoints `/rollen` en `zaakobjecten` ondersteunen geen expand maar laten wel een "_expand" attribuut zien (zie [#2414](https://github.com/VNG-Realisatie/gemma-zaken/issues/2414) en [2412](https://github.com/VNG-Realisatie/gemma-zaken/issues/2412)). <br>
**Fix**: verwijderen van het "_expand" attribuut bij de genoemde endpoints zoals voorgesteld in [PR #2427](https://github.com/VNG-Realisatie/gemma-zaken/pull/2427).

- **Bug**: Het is niet duidelijk of of alle geledingen van de expand parameter geexpandeerd moeten worden of alleen de laatste (zie [#2398](https://github.com/VNG-Realisatie/gemma-zaken/issues/2398)). <br>
**Fix**: Bij geneste expand worden alle velden die in het pad (met punt-notatie) voorkomen geëxpandeerd. Dit zal worden opgenomen in de aanvullende specificatie van de volgende release.

- **Bug**: Via de veelgebruikte openbare link https://zaken-api.vng.cloud  is de genereerde versie van de OAS van de Zaken API te zien (klik [hier](https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/vng-Realisatie/zaken-api/1.5.1/src/openapi.yaml)). Deze OAS is gegenereerd vanuit de code van de referentie-implementatie voor technische doeleinden.  Echter deze OAS is niet normatief, incompleet en bevat zelfs fouten. Dit kan tot misverstanden leiden als de bezoeker hiervan niet op de hoogte is (zie [#2424](https://github.com/VNG-Realisatie/gemma-zaken/issues/2424))<br>
**Fix**: De normatieve en goede OAS van de Zaken API is hier te vinden: https://vng-realisatie.github.io/gemma-zaken/standaard/zaken.

|