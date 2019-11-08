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

In [VNG API-Beheer](https://github.com/VNG-Realisatie/api-beheer/blob/master/versiebeheer.md) kun je lezen dat VNG API Beheer maximaal 2 major versies van elke API standaard ondersteunt. Dat staat echter los van het aantal versies van een API dat door een provider applicatie wordt ondersteund. Zo staat het een leverancier vrij om gelijktijdig alle ooit beschikbaar gestelde API's te ondersteunen. In de onderstaande scenario's gaan we daar niet vanuit.

Naast dat er dus verschillende versies van een API ondersteund kunnen zijn, kunnen er ook verschillende leveranciers zijn die dezelfde
registraties aanbieden, of kunnen er meerdere registraties worden gebruikt om dezelfde type data te ontsluiten. Zo kunnen er typisch meerdere Catalogi API's beschikbaar zijn en gebruikt worden in een Zaken API.

In dit document wordt gekeken naar migratie scenario's waarvoor consumers en providers zich gesteld zien in het geval:
* er nieuwe API versies beschikbaar komen op een provider. 
* er data van een provider naar een geheel andere locatie (bijvoorbeeld een andere leverancier) moet worden gemigreerd.

De scenario's schetsen slechts een mogelijke aanpak, ze mogen niet beschouwd worden als beschrijvingen van de door VNG-Realisatie gewenste oplossingsrichtingen.

## Nieuwe API versies

Stel, er komt een nieuwe versie uit van een van de VNG API standaarden. Waar moet je dan rekening mee houden? We 
beschrijven hieronder 2 scenario's.

### Migratie scenario 1: Nieuwe versie van de eigen API

**Situatieschets:**

1. De Provider ondersteunt op dit moment v1.0.0 van de Zaken API.
2. Een Zaak heeft een Status (beide in de Zaken API):
```
GET https://gemeente.nl/api/zaken/v1/zaken/6c821f  HTTP/1.0

HTTP 200
{
    "status": "https://gemeente.nl/api/zaken/v1/statussen/8aa57d"
    // ...
}
```

3. De provider heeft er voor gekozen de URI's naar gerelateerde objecten in een koppeltabel in de database vast te leggen.
   Dit betekent dat in de database in de records van de zaakobjecten UUID's zijn opgenomen waarmee wordt verwezen naar de
   gerelateerde status- of besluitobjecten. In de koppeltabel zijn deze UUID's eveneens opgenomen met daarbij de
   bijbehorende gegevens om de uri te kunnen samenstellen. Hieronder de voor dit voorbeeld van toepassing zijnde records in de
   koppeltabel.
   
   |**UUID**|**URI**|
   |---|---|
   |8aa57d|https://gemeente.nl/api/zaken/v1/statussen/8aa57d|
   |8aa57d|https://gemeente.nl/api/zaken/v2/statussen/8aa57d|
   
4. De provider gaat de Zaken API v2.0.0 ondersteunen en zal op termijn gaan stoppen met de ondersteuning van v1.0.0.

**Wat gaat er gebeuren?**

1. De provider zal de Zaken API v1.0.0 nog enige tijd naast v2.0.0 moeten ondersteunen.
2. Vanaf het beschikbaar komen van de Zaken API v2.0.0 geven verzoeken op de Zaken API v1.0.0 een waarschuwing mee als header
   waarin staat dat er een nieuwe versie beschikbaar is.
3. In de koppeltabel is voor het statusobject met de UUID's '8aa57d' vastgelegd welke v1.0.0 en welke v2.0.0 URI van toepassing is. 
4. De zaak met UUID `6c821f` is beschikbaar via de Zaken API v1.0.0 en via v2.0.0.
5. Verwijzingen binnen een API wijzen naar dezelfde versie. Ofwel, een 
   Zaak in Zaken API v1.0.0 mag niet wijzen naar een Status in de Zaken API 
   v2.0.0 en een Zaak in Zaken API v2.0.0 mag niet wijzen naar een Status in de Zaken API 
   v1.0.0. Dit principe is te realiseren door wat in punt 4 wordt genoemd.
6. Voordat de Zaken API v1.0.0 wordt stopgezet moeten alle applicaties (die
   iets doen met de Zaken API) kunnen omgaan met Zaken API v2.0.0.
7. Als alle applicaties kunnen omgaan met Zaken API v2.0.0 worden in de Zaken API v1.0.0 alleen de GET endpoints nog ondersteund.
8. In de koppeltabel worden alle URI's naar de Zaken API v1.0.0 verwijderd.
9. De Zaken API v1.0.0 kan worden stopgezet.

```
GET https://gemeente.nl/api/zaken/v2/zaken/6c821f  HTTP/1.0

HTTP 200
{
    "status": "https://gemeente.nl/api/zaken/v2/statussen/8aa57d"
    // ...
}
```

### Migratie scenario 2: Nieuwe versie van een externe API

**Situatieschets:**

1. Provider ondersteunt op dit moment v1.0.0 van de Zaken API en Catalogi API v1.0.0.
```
GET https://gemeente.nl/api/zaken/v1/zaken/6c821f  HTTP/1.0

HTTP 200
{
    "zaaktype": "https://catalogi-api.vng.cloud/api/v1/zaaktypen/a44e32"
    // ...
}
```

2. Een Zaak in de Zaken API heeft een Zaaktype in de Catalogi API.
3. De provider heeft er voor gekozen de URI's van de gerelateerde objecten in een veld van het verwijzende object in de database vast te leggen.
4. De provider gaat de Catalogi API v2.0.0 ondersteunen en zal op termijn gaan stoppen met de ondersteuning van v1.0.0.

**Wat gaat er gebeuren?**

1. De provider van de Catalogi API zal v1.0.0 nog enige tijd naast v2.0.0 moeten ondersteunen.
2. Vanaf het beschikbaar komen van de Catalogi API v2.0.0 geven verzoeken op de Catalogi API v1.0.0 een waarschuwing mee als
   header waarin staat dat er een nieuwe versie beschikbaar is.
3. Het Zaaktype met UUID `a44e32` moet beschikbaar zijn via de Catalogi API v1.0.0 en via v2.0.0.
4. De provider van de Zaken API moet zo geconfigureerd worden dat deze in zijn responses Catalogi API v2.0.0 URI's teruggeeft.
5. Voordat de Catalogi API v1.0.0 wordt stopgezet moeten alle applicaties (die
   iets doen met de Catalogi API) kunnen omgaan met Catalogi API v2.0.0.
6. Als alle applicaties kunnen omgaan met de Catalogi API v2.0.0 worden in de Catalogi API v1.0.0 alleen de GET endpoints nog ondersteund.
7. Daarna moeten de URI's van de gerelateerde objecten in de database worden geconverteerd.
8. De Catalogi API v1.0.0 kan worden stopgezet.

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

**Situatieschets:**

1. Huidige situatie: Zaken API bij gemeente staat op API root URL 
   `https://gemeente.nl/api/zaken/v1/`:
   
```
GET https://gemeente.nl/api/zaken/v1/zaken/6c821f  HTTP/1.0

HTTP 200
{
    // ...
}
```

2. Alle data moet verhuist worden naar leverancier ACME.
3. De Zaken API van de leverancier ACME staat op API root URL 
   `https://example.com/api/zaken/v1/`

**Wat gaat er gebeuren?**

1. Het is onvermijdelijk dat de Zaken API een enige tijd niet beschikbaar is.
2. Data moet gemigreerd worden van de gemeente naar de leverancier.
3. Alle data (ook de UUID's van objecten) migreert ongewijzigd mee.
4. Na de data migratie moet de Zaken API van de gemeente een redirect geven op
   alle URL's onder de API root URL naar de API root URL van de leverancier ACME met
   behoud van het relatieve pad (volgens de OAS).
5. Voordat de Zaken API van de gemeente wordt stopgezet moeten alle applicaties
   (die iets doen met de Zaken API) de nieuwe API root URL configureren of migreren.
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

### Migratie scenario 2: Archivering in een e-Depot

Het archiveren van een dossier heeft als doel het afgesloten dossier voor een vastgelegde termijn te bewaren zodat het indien gewenst geraadpleegd kan worden. Het is daarbij niet van belang dat de componenten zo efficient mogelijk (dus zonder redundantie) opgeslagen worden.
Een mogelijk strategie zou zijn de dossiers in een geresolvde staat op te slaan in het e-Depot. Daarmee bedoelen we dat de in het dossier opgenomen gerelateerde objecten niet meer via een URI op te halen zijn maar in zijn geheel in het dossier opgeslagen wordt.
Het dossier wordt daarmee eigenlijk een BLOB. Daarmee wordt voorkomen dat in geval van overgang naar een nieuwe API versie ook op een e-Depot datamigratie moet worden toegepast.

## URL implementatiedetails

In de bovenstaande scenario's zijn we er vanuit gegaan dat in de database absolute URI's worden opgeslagen. In plaats van absolute URL's as-is opslaan kunnen URI's echter ook gefragmenteerd 
opgeslagen worden in de database. Later kan uit deze fragmenten weer de 
volledige URL worden opgebouwd. Dit kan latere versie of locatie migraties 
vergemakkelijken.

**Voorbeeld**

Op dit moment bestaat Catalogi API v1.0.0 en v2.0.0. In de Zaken API staan 3 
Catalogi API's geconfigureerd, elk met hun eigen URI's, te weten:

ID|Leverancier ID|Component ID|Versie|Standaard|API root URL
---|---|---|---|---|---
1|VNG|Catalogi API|v1.0.0|Ja|https://catalogi-api.vng.cloud/api/v1/
2|ACME|Catalogi API|v1.0.0|Nee|https://example.com/api/catalogi/v1/
3|VNG|Catalogi API|v2.0.0|Nee|https://catalogi-api.vng.cloud/api/v2/

URI's naar bijvoorbeeld een Zaaktype van een Zaak kunnen worden opgeslagen als: 

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
* Valide URI's zijn makkelijk te controleren: Het begin van elke URI moet 
  voorkomen in de tabel.
