---
title: "API versies"
date: '28-06-2019'
weight: 50
---

Gebaseerd op: User Story [#931](https://github.com/VNG-Realisatie/gemma-zaken/issues/931)

## Inleiding

Versiebeheer is gebaseerd op [Semantic Versioning](https://semver.org) en de
[API strategie](https://aandeslagmetdeomgevingswet.nl/digitaal-stelsel/technisch-aansluiten/standaarden/api-uri-strategie/).
Elke  API heeft een eigen versienummer, opgebouwd uit `MAJOR.MINOR.PATCH` 
element. Bijvoorbeeld versie `2.1.8`:

Gegeven dit versienummer, elke ophoging van de:

* `MAJOR` versie betreft een *backwards-incompatible* API wijziging,
* `MINOR` versie betreft het toevoegen van een *backwards-compatible* API 
  wijziging,
* `PATCH` versie betreft het oplossen van *backwards-compatible* issues.

Zie: [VNG API-Beheer](https://github.com/VNG-Realisatie/api-beheer/blob/master/versiebeheer.md)

### Verschillende API versies

#### Implementatiedetails

In plaats van absolute URL's as-is opslaan kunnen URL's ook gefragementeerd 
opgeslagen worden in de database. Later kan uit deze fragmenten weer de 
volledige URL worden opgebouwd. Dit kan latere versie migraties 
vergemakkelijken.

**Voorbeeld**

Op dit moment bestaat Catalogi API v1.0.0 en v2.0.0. In de Zaken API staan 3 
Catalogi API's geconfigureerd, elk met hun eigen URL's, te weten:

ID|Leverancier ID|Component ID|Versie|Standaard|API root URL
---|---|---|---|---|---
1|VNG|Catalogi API|v1.0.0|Ja|https://catalogi-api.vng.cloud/api/v1/
2|ACME|Catalogi API|v1.0.0|Ja|https://catalogi-api.example.com/api/v1/
3|VNG|Catalogi API|v2.0.0|Nee|https://catalogi-api.vng.cloud/api/v1/

URL's naar bijvoorbeeld een Zaaktype van een Zaak kunnen worden opgeslagen als: 

* `{Leverancier ID}`
* `{Component ID}`
* `{Relatieve URL}`

Zo kunnen de database waarden `("VNG", "Catalogi API", "zaaktypen/a44e32")`,
met de logica om `Standaard=Ja` waarde van deze leverancier te pakken, 
gemakkelijk omgezet worden naar:
`https://catalogi-api.vng.cloud/api/v1/zaaktypen/a44e32` voor API responses.

Als Catalogi API v2.0.0 de leidende standaard wordt en `Standaard=Ja` bij 
`ID=3` wordt opgegeven (en `Standaard=Nee` bij `ID=1`), wijzen alle Zaaktypen 
URL's nu naar Catalogi v2.0.0 in plaats van v1.0.0 zonder ingewikkelde 
migraties.

Valide URLs zijn ook makkelijk te controleren, het begin van elke URL moet 
voorkomen in de tabel.

#### Migratie scenario 1: Een nieuwe API versie

1. Huidige situatie: Zaken API v1.0.0
2. Een Zaak heeft een Status (beide in de Zaken API)
3. Zaken API v2.0.0 komt uit

```http
GET https://gemeente.nl/api/v1/zaken/6c821f

{
    "status": "https://gemeente.nl/api/v1/statussen/8aa57d"
}
```

**Wat gaat er gebeuren?**

1. Zaken API v1.0.0 zal nog even moeten bestaan naast v2.0.0
2. Verzoeken op de Zaken API v1.0.0 geven een waarschuwing mee als header
   dat er een nieuwe versie is.
3. Zaak met UUID `6c821f` moet beschikbaar zijn op de Zaken API v1.0.0 en 
   v2.0.0
4. Verwijzingen binnen dezelfde API wijzen naar dezelfde versie. Ofwel, een 
   Zaak in Zaken API v1.0.0 mag niet wijzen naar een Status in de Zaken API 
   v2.0.0.
5. Voordat Zaken API v1.0.0 wordt uitgefaseerd moeten alle applicaties (die
   iets doen met de Zaken API) kunnen omgaan met Zaken API v2.0.0.
6. Als alle applicaties kunnen omgaan met Zaken API v2.0.0 kunnen alle URL's
   naar de Catalogi API v1.0.0 worden aangepast naar de nieuwe versie
7. Catalogi API v1.0.0 kan worden uitgefaseerd


```http
GET https://gemeente.nl/api/v2/zaken/6c821f

{
    "status": "https://gemeente.nl/api/v2/statussen/8aa57d"
}
```

#### Migratie scenario 2: Verwijzingen naar een (externe) nieuwe API versie

1. Huidige situatie: Zaken API v1.0.0 en Catalogi API v1.0.0
2. Een Zaak in de Zaken API heeft een Zaaktype in de Catalogi API
3. Catalogi API v2.0.0 komt uit

```http
GET https://gemeente.nl/api/v1/zaken/6c821f

{
    "zaaktype": "https://catalogi-api.vng.cloud/api/v1/zaaktypen/a44e32",
}
```

**Wat gaat er gebeuren?**

1. Catalogi API v1.0.0 zal nog even moeten bestaan naast v2.0.0
2. Verzoeken op de Catalogi API v1.0.0 geven een waarschuwing mee als header
   dat er een nieuwe versie is.
3. Zaaktype met UUID `a44e32` moet beschikbaar zijn op de Catalogi API v1.0.0 
   en v2.0.0
4. De Zaken API zal geconfigureerd moeten zodat deze Catalogi API v2.0.0 URLs
   zal accepteren
5. Voordat Catalogi API v1.0.0 wordt uitgefaseerd moeten alle applicaties (die
   iets doen met de Catalogi API) kunnen omgaan met Catalogi API v2.0.0.
6. Als alle applicaties kunnen omgaan met Catalogi API v2.0.0 kunnen alle URL's
   naar de Catalogi API v1.0.0 worden aangepast naar de nieuwe versie
7. Catalogi API v1.0.0 kan worden uitgefaseerd
