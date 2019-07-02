---
title: "Versies en migraties"
date: '28-06-2019'
weight: 50
---

Gebaseerd op:

* User Story [#931](https://github.com/VNG-Realisatie/gemma-zaken/issues/931)
* User Story [#800](https://github.com/VNG-Realisatie/gemma-zaken/issues/800)

## Inleiding

Versiebeheer is gebaseerd op [Semantic Versioning](https://semver.org) en de
[API strategie](https://aandeslagmetdeomgevingswet.nl/digitaal-stelsel/technisch-aansluiten/standaarden/api-uri-strategie/).
Elke  API heeft een eigen versienummer, opgebouwd uit `MAJOR.MINOR.PATCH` 
element. Bijvoorbeeld versie `2.1.8`:

Zie: [VNG API-Beheer](https://github.com/VNG-Realisatie/api-beheer/blob/master/versiebeheer.md)

Naast verschillende versies zijn er verschillende leveranciers die dezelfde
registraties aanbieden, of worden er meerdere registraties gebruikt om dezelfde
type data te ontsluiten. Zo kunnen er typisch meerdere Catalogi API's 
beschikbaar zijn en gebruikt worden in een Zaken API.

In dit document wordt gekeken naar migratie scenario's voor nieuwe API versies
en het migreren van data naar een geheel andere locatie (bijvoorbeeld een 
andere leverancier). 

## Nieuwe API versies

Stel, er komt een nieuwe versie uit van een van VNG API standaarden. We 
beschrijven 2 scenario's.

### Migratie scenario 1: Nieuwe eigen API versie

```
GET https://gemeente.nl/api/zaken/v1/zaken/6c821f  HTTP/1.0

HTTP 200
{
    "status": "https://gemeente.nl/api/zaken/v1/statussen/8aa57d"
    // ...
}
```

1. Huidige situatie: Zaken API v1.0.0
2. Een Zaak heeft een Status (beide in de Zaken API)
3. Zaken API v2.0.0 komt uit

**Wat gaat er gebeuren?**

1. Zaken API v1.0.0 zal nog even moeten bestaan naast v2.0.0
2. Verzoeken op de Zaken API v1.0.0 geven een waarschuwing mee als header
   dat er een nieuwe versie is.
3. Zaak met UUID `6c821f` moet beschikbaar zijn op de Zaken API v1.0.0 en 
   v2.0.0
4. Verwijzingen binnen dezelfde API wijzen naar dezelfde versie. Ofwel, een 
   Zaak in Zaken API v1.0.0 mag niet wijzen naar een Status in de Zaken API 
   v2.0.0.
5. Voordat Zaken API v1.0.0 wordt stopgezet moeten alle applicaties (die
   iets doen met de Zaken API) kunnen omgaan met Zaken API v2.0.0.
6. Als alle applicaties kunnen omgaan met Zaken API v2.0.0 kunnen alle URL's
   naar de Zaken API v1.0.0 worden aangepast naar de nieuwe versie
7. Zaken API v1.0.0 kan worden stopgezet

```
GET https://gemeente.nl/api/zaken/v2/zaken/6c821f  HTTP/1.0

HTTP 200
{
    "status": "https://gemeente.nl/api/zaken/v2/statussen/8aa57d"
    // ...
}
```

### Migratie scenario 2: Nieuwe externe API versie

```
GET https://gemeente.nl/api/zaken/v1/zaken/6c821f  HTTP/1.0

HTTP 200
{
    "zaaktype": "https://catalogi-api.vng.cloud/api/v1/zaaktypen/a44e32"
    // ...
}
```

1. Huidige situatie: Zaken API v1.0.0 en Catalogi API v1.0.0
2. Een Zaak in de Zaken API heeft een Zaaktype in de Catalogi API
3. Catalogi API v2.0.0 komt uit

**Wat gaat er gebeuren?**

1. Catalogi API v1.0.0 zal nog even moeten bestaan naast v2.0.0
2. Verzoeken op de Catalogi API v1.0.0 geven een waarschuwing mee als header
   dat er een nieuwe versie is.
3. Zaaktype met UUID `a44e32` moet beschikbaar zijn op de Catalogi API v1.0.0 
   en v2.0.0
4. De Zaken API zal geconfigureerd moeten zodat deze Catalogi API v2.0.0 URLs
   zal accepteren
5. Voordat Catalogi API v1.0.0 wordt stopgezet moeten alle applicaties (die
   iets doen met de Catalogi API) kunnen omgaan met Catalogi API v2.0.0.
6. Als alle applicaties kunnen omgaan met Catalogi API v2.0.0 kunnen alle URL's
   naar de Catalogi API v1.0.0 worden aangepast naar de nieuwe versie
7. Catalogi API v1.0.0 kan worden stopgezet

```
GET https://gemeente.nl/api/zaken/v1/zaken/6c821f  HTTP/1.0

HTTP 200
{
    "zaaktype": "https://catalogi-api.vng.cloud/api/v2/zaaktypen/a44e32",
    // ...
}
```

## Data verhuist naar andere locatie

Stel, alle Zaken API data moet verhuizen naar een ander locatie en komt daarmee
beschikbaar op een andere API root URL.

### Migratie scenario 1: Wijziging van leverancier

```
GET https://gemeente.nl/api/zaken/v1/zaken/6c821f  HTTP/1.0

HTTP 200
{
    // ...
}
```

1. Huidige situatie: Zaken API bij gemeente staat op API root URL 
   `https://gemeente.nl/api/zaken/v1/`
2. Alle data moet verhuist worden naar leverancier ACME
3. De Zaken API van de leverancier staat op API root URL 
   `https://example.com/api/zaken/v1/`

**Wat gaat er gebeuren?**

1. Het is onvermijdelijk dat de Zaken API een enige tijd niet beschikbaar is
2. Data moet gemigreerd worden van de gemeente naar de leverancier
3. Alle data (ook de UUID's van objecten) migreert mee
4. Na de data migratie moet de Zaken API van de gemeente een redirect geven op
   alle URL's onder de API root URL naar de API root URL van de leverancier met
   behoud van het relatieve pad (volgens de OAS)
5. Voordat de Zaken API van de gemeente wordt stopgezet moeten alle applicaties
   (die iets doen met de Zaken API) de nieuwe API root URL krijgen
6. Als dit voor alle applicaties is gedaan, kan de Zaken API van de gemeente
   worden stopgezet.

```
GET https://gemeente.nl/api/zaken/v1/zaken/6c821f  HTTP/1.0

HTTP 301
Location: https://example.com/api/zaken/v1/zaken/6c821f
```

```
GET https://example.com/api/zaken/v1/zaken/6c821f  HTTP/1.0

HTTP 200
{
    // ...
}
```


## URL implementatiedetails

In plaats van absolute URL's as-is opslaan kunnen URL's ook gefragementeerd 
opgeslagen worden in de database. Later kan uit deze fragmenten weer de 
volledige URL worden opgebouwd. Dit kan latere versie of locatie migraties 
vergemakkelijken.

**Voorbeeld**

Op dit moment bestaat Catalogi API v1.0.0 en v2.0.0. In de Zaken API staan 3 
Catalogi API's geconfigureerd, elk met hun eigen URL's, te weten:

ID|Leverancier ID|Component ID|Versie|Standaard|API root URL
---|---|---|---|---|---
1|VNG|Catalogi API|v1.0.0|Ja|https://catalogi-api.vng.cloud/api/v1/
2|ACME|Catalogi API|v1.0.0|Nee|https://example.com/api/catalogi/v1/
3|VNG|Catalogi API|v2.0.0|Nee|https://catalogi-api.vng.cloud/api/v1/

URL's naar bijvoorbeeld een Zaaktype van een Zaak kunnen worden opgeslagen als: 

* `{Leverancier ID}`
* `{Component ID}`
* `{Relatieve URL}`

Zo kunnen de database waarden `("Catalogi API", "zaaktypen/a44e32")`,
met de logica om de regel waar `Standaard=Ja` te pakken om de API root URL op
te halen, gemakkelijk omgezet worden in 
`https://catalogi-api.vng.cloud/api/v1/zaaktypen/a44e32` voor API responses.

*Voordelen*

* Als de Catalogi API van v1.0.0 naar v2.0.0 gaat, hoeft alleen de waarde bij 
  `Standaard` aangepast te worden. 
* Als de Catalogi API verhuist naar een andere leverancier en dus de API root 
  URL in zijn geheel wijzigt, hoeft alleen de waarde bij `Standaard` aangepast
  te worden.
* Valide URLs zijn makkelijk te controleren: Het begin van elke URL moet 
  voorkomen in de tabel.
