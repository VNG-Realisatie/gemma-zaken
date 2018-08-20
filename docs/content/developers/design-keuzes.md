---
title: "Ontwerpkeuzes"
description: ""
weight: 30
menu:
  docs:
    parent: "developers"
---

## UUID4 als ID-parameter in endpoints

De ID-parameter, hieronder aangeduid met `{uuid}` wordt gebruikt om via de URL
een enkel object van een bepaald type resource te vinden. Bijvoorbeeld een
`Zaak`:

|URL|Voorbeeld|
|---|---|
| `https://www.example.com/zaken/{uuid}/`|`https://www.example.com/zaken/550e8400-e29b-41d4-a716-446655440000/`|

Een [UUID (versie 4)] is in de praktijk altijd uniek, zonder dat deze centraal
hoeft te worden bijgehouden. Deze keuze laat onverlet de mogelijkheid om op
andere manieren bij een enkel object te komen, zoals op een combinatie van
velden die samen uniek zijn, zoals `bronorganisatie` en `zaakidentificatie`:
`https://www.example.com/zaken/?bronorganisatie=0329&zaakidentificatie=MOR-0000001`

*Achtergrond*
De paden van API endpoints bevatten referenties naar de objecten in de
achterliggende datastore. Deze parameters zouden semantisch kunnen ingevuld
worden, zoals gebruikmaken van `bronorganisatie` en `zaakidentificatie` voor
een zaak. Echter, na analyse blijkt dat dit lastig consequent toe te passen is
door de hele de API heen. Tevens wekt het de indruk dat dat deze parameters
genoeg zijn om een Zaak te vinden maar dat is niet correct. De volledige URL is
nodig voor het opvragen van een enkele Zaak.

Daarom is besloten om gebruik te maken van [UUID (versie 4)] voor deze
parameters. De motivatie is verder dat deze:

* uniciteit garandeert, ook over meerdere systemen heen;
* geen volgordelijkheid/database IDs lekt;
* de DSO API-richtlijnen volgt;
* semantisch bevragen niet onmogelijk maakt.

[UUID (versie 4)]: https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)


## ISO-8601 durations voor uitdrukken van duur

Voor het uitdrukken van duur wordt gebruikt gemaakt van [ISO-8601 durations](https://en.wikipedia.org/wiki/ISO_8601#Durations). Dit sluit aan bij ISO-8601 weergave van timestamps doorheen de API.


## Omgang met polymorfe resources

In het RGBZ zijn er voor sommige relaties meerdere types van gerelateerde
resources mogelijk. Concrete voorbeelden hiervan zijn:

* betrokkenen bij een zaak - dit kunnen `Natuurlijke Personen`, `Medewerkers`,
  `Organisatorische Eenheden` en meer zijn. Elk van deze betrokkenen heeft
  verschillende attributen, en een aantal komen (bijna) overal voor.

* objecten gerelateerd aan een zaak via ZAAKOBJECT. Hier zijn erg veel types
  mogelijk, bijvoorbeeld: `Huishouden`, `OpenbareRuimte`, `Wegdeel` etc.

In essentie is dit een vorm van polymorfisme.

Door het uitgangspunt van Common Ground om data-bij-de-bron-opslaan te hanteren,
werken we in de ZDS 2.0 API specificaties met _linked data_, wat betekent
dat de relaties een referentie-url geven naar de gerelateerde resource. Een
client/consumer weet op voorhand niet naar welke vorm van gerelateerde resource
er verwezen wordt.

Daarom is ervoor gekozen om op de relatie bij te houden om welk type resource
het gaat. Een concreet voorbeeld van een response is dan:

```http
GET /zrc/api/v1/rollen/fb1f6871-6dad-4f9b-abf8-0c46797b084a
Content-Type: application/json

{
    "url": "https://example.com/zrc/api/v1/rollen/fb1f6871-6dad-4f9b-abf8-0c46797b084a",
    "zaak": "https://example.com/zrc/api/v1/zaken/6232ba6a-beee-4357-b054-6bde6d1ded6c",
    "betrokkene": "https://brp.utrecht.nl/api/v1/np/ab44ed92-ff55-4c4c-87aa-c538d58e887d",
    "betrokkene_type": "Natuurlijk persoon",
}
```

Het gaat hier dan om het `betrokkene_type` veld.

De URLs in dit voorbeeld zijn uiteraard fictief.

## Naamgeving van de API velden binnen een resource

* Prefixes die slaan op de eigen resource, worden niet gebruikt. Voorbeeld:
  Attribuutsoort [informatieobjecttype.informatieobjecttype-omschrijving](https://www.gemmaonline.nl/index.php/Imztc_2.1/doc/attribuutsoort/informatieobjecttype.informatieobjecttype-omschrijving)
  in RGBZ2 krijgt de naam "omschrijving" in de API, aangezien het een veld is
  binnen de resource `informatieobjecttype`. Dit komt overeen met de in RGBZ
  genoemde XML-tag.
  
  ```javascript
  {
      "url": "https://example.com/drc/api/v1/informatieobjecttypen/8534ba6a-bcde-4387-b054-6bde6d1ded8f",
      "omschrijving": "Document"
      // ...
  }
  ```
* Relaties worden **niet** aangeduid met hun relatie omschrijving (`isVan`, 
  `heeft`, `kent`, etc.). Dit heeft mede te maken met het feit dat er geen 
  mnemonic attributen zijn (zoals in StUF-ZKN) in de REST API, waardoor het 
  niet direct duidelijk is naar wat voor type resource verwezen wordt.
* Indien verwezen wordt naar een andere resource (relatie), wordt de volledige 
  naam van de resource gebruikt als veldnaam. Voorbeeld: De resource `zaak` 
  heeft een veld `zaaktype` en niet `type`. Ter vergelijking, in StUF-ZKN is 
  dit: `zaak-isVan-<zaak type data>` waar `isVan` verwijst naar het `zaaktype`.
  
  ```javascript
  {
      "url": "https://example.com/zrc/api/v1/zaken/6232ba6a-beee-4357-b054-6bde6d1ded6c",
      "zaaktype": "https://example.com/ztc/api/v1/zaaktypen/6232ba6a-beee-4357-b054-6bde6d1ded6c"
      // ...
  }
  ```

## Gerelateerde objecten zonder eigen resource / Groepsattributen

Indien een (hoofd)object een gerelateerd object (of lijst van objecten) heeft, 
dat **geen** eigen resource URL nodig heeft, dan wordt het (child)object inline
(binnen het hoofdobject) geserializeerd. Deze child objecten zijn binnen RGBZ
ook wel gedefinieerd als *groepsattributen*. Typische voorbeeld zijn
(zaak-)kenmerken of (zaak-)eigenschappen waarin `Zaak` het hoofdobject betreft,
en `Kenmerk` en `Eigenschap` de child objecten.

Voorbeeld:

```javascript
{
    "url": "https://example.com/zrc/api/v1/zaken/6232ba6a-beee-4357-b054-6bde6d1ded6c",
    "zaaktype": "https://example.com/ztc/api/v1/zaaktypen/6232ba6a-beee-4357-b054-6bde6d1ded6c"
    // ...
    "kenmerken": [
        {
            "kenmerk": "test",
            "bron": "http://www.example.com/"
        }
    ]
}
```
