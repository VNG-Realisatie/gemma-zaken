---
title: "ZGW API-landschap grenzen"
date: '07-06-2019'
weight: 50
---

In het Common Ground API-landschap worden straks alle gegevens netjes ontsloten 
middels een API. Er is een API die Kadastergegevens ontsluit, een API voor 
Zaken, Documenten, Personen, Medewerkers, etc.

Op dit moment wordt er hard gewerkt aan een set API's die bij elkaar de
kern vormen voor de API's voor Zaakgericht werken. Deze bestaan op het moment
van schrijven uit de Zaken API, Documenten API, Catalogi API en Besluiten API.
Deze maken op hun beurt weer gebruik van de Autorisaties API en de Notificaties 
API.

## Probleemomschrijving

Een `Zaak` kent typisch een of meer `Betrokkenen` zoals een 
`Natuurlijk Persoon` of `Vestiging`. Ook gaat een `Zaak` meestal over een of 
meer `ZaakObjecten` zoals een `Buurt`, `Kunstwerkdeel`, `Ligplaats` of `Wijk`. 
Allemaal objecten.

Deze objecten "leven" in eigen registraties die middels API's benaderd moeten 
worden. Aangezien de API's voor Zaakgericht werken de eerste set API's is die 
beschikbaar komt als VNG API standaard, is het API-landschap nog beperkt.

De objecten achter de Zaak-relaties `Betrokkenen` en `Zaakobjecten` kunnen 
daarom niet worden ontsloten middels een API. Er kan dus niet een URI opgegeven
worden die verwijst naar zo'n object, zoals bijvoorbeeld hieronder is 
weergegeven:

```http
GET https://zaken.api.haarlem.nl/v1/zaakobjecten/c9a651  HTTP/1.0

{
  "url": "https://zaken.api.haarlem.nl/v1/zaakobjecten/c9a651",
  "zaak": "https://zaken.api.haarlem.nl/v1/zaken/66a38b",
  "object": "https://objecten.api.haarlem.nl/v1/wijken/3fa723",
  "relatieomschrijving": "Speelt alleen in deze wijk",
  "type": "Wijk"
}
```

Er wordt bij het `Zaakobject` aan de ene kant prima gerefereerd naar een `Zaak`
(attribuut `zaak`) maar er kan nog niet verwezen worden naar een `Wijk`
(attribuut `object`).

**Dit zijn de grenzen van het API-landschap. Een API verwijst naar een object
dat nog niet ontsloten wordt middels een API.**

## Oplossing

Het RSGB definieert zogenaamde "matchinggegevens" van alle objecten. Een set 
aan gegevens die nodig zijn om een object uniek te identificeren en op te 
zoeken. Deze staan het meest helder vermeld in de gepubliceerde XSDs van o.a. 
[RGBZ] en [RSGB], onder de ([onhandige][matching-vs-kern-gegevens]) naam 
"kerngegevens".

De beoogde oplossing is nu om de "matchinggegevens" op te nemen in het bericht 
als er niet met een URI kan worden verwezen naar het object. Voor alle andere
objecten kunnen elders gedefinieerde gegevens worden opgenomen om het object
te identificeren.

In het eerder getoonde voorbeeld `Wijk` zijn de "matchinggegevens": `wijkCode`, 
`wijkNaam` en `gem.gemeenteCode`. Deze zijn opgenomen in het bericht, in het 
attribuut `objectIdentificatie`. Ook is de `registratiedatum` opgenomen om
de opgenomen gegevens, of de URL-verwijzing, in het juiste tijdsperspectief
te plaatsen:

```http
GET https://zaken.api.haarlem.nl/v1/zaakobjecten/c9a651  HTTP/1.0

{
  "url": "https://zaken.api.haarlem.nl/v1/zaakobjecten/c9a651",
  "zaak": "https://zaken.api.haarlem.nl/v1/zaken/66a38b",
  "object": null,
  "objectIdentificatie": {
    "wijkCode": "0145",
    "wijkNaam": "Schalkwijk",
    "gemGemeenteCode": "0392"
  },
  "registratiedatum": "2019-06-17T17:41:22Z",
  "relatieomschrijving": "Speelt alleen in deze wijk",
  "type": "Wijk"
}
```

Het `object` attribuut is nu leeg, want er is geen API beschikbaar die `Wijken`
ontsluiten. Zowel `object` als `objectIdentificatie` mogen gevuld zijn om
compatibiliteitsredenen en met het oog op het ontstaan van toekomstige API's.
Beide attributen mogen echter niet tegelijk leeg zijn.

Het `type` attribuut omschrijft, in het geval van `Zaakobjecten`, het type 
object waar naar verwezen wordt en beïnvloed tevens welke attributen zich 
bevinden in `objectIdentificatie`. In de Open API specificatie wordt dit 
opgelost middels [polymorfisme] waarbij attribuut `type` optreedt als 
"discriminator".

### Generieke oplossing

Het voorbeeld van `Wijk` is eenvoudig generiek te trekken naar alle grenzen van
het API-landschap.

*Indien in een resource een relatie wordt gelegd naar een andere bron die nog 
niet is gestandaardiseerd in het nieuwe gegevenslandschap op basis van API's, 
dan moeten identificerende gegevens worden opgenomen in deze resource die deze
relatie mogelijk maakt zonder URL-verwijzing, als volgt:*

```
{
  "<attribuutnaam>": "<URL-waarde naar andere bron>",
  "<attribuutnaam>Identificatie": {
    // Attributen die de relatie identificeert.
  },
  "registratiedatum": "<datetime>"
}
```

### Zaakgericht werken

#### Zaken API

**Resource "rollen"**

De resource `rollen` kent een attribuut `betrokkene`. Deze kan verwijzen naar 
meerdere type objecten waarvan nog geen bron is gestandaardiseerd.

Hieronder volgt een overzicht van matchinggegevens per objecttype.

* Natuurlijk persoon
    
    * `inpBsn` (=`inp.bsn`)
    * `anpIdentificatie` (=`anp.identificatie`)
    * `inpA_nummer` (=`inp.a-nummer`)
    * `geslachtsnaam`
    * `voorvoegselGeslachtsnaam`
    * `voorletters`
    * `voornamen`
    * `geslachtsaanduiding`
    * `geboortedatum`
    * `verblijfsadres`
    * `subVerblijfBuitenland` (=`sub.verblijfBuitenland`)

* Niet-natuurlijk persoon

    * `innNnpId` (=`inn.nnpId`)
    * `annIdentificatie` (=`ann.identificatie`)
    * `statutaireNaam`
    * `innRechtsvorm` (=`inn.rechtsvorm`)
    * `bezoekadres`
    * `subVerblijfBuitenland` (=`sub.verblijfBuitenland`)

* Vestiging

    * `vestigingsNummer`
    * `handelsnaam`
    * `verblijfsadres`
    * `subVerblijfBuitenland` (=`sub.verblijfBuitenland`)

* Organisatorische eenheid

    * `identificatie`
    * `naam`
    * `isGehuisvestIn` (genest JSON object)
        * Zie: `vestiging`

* Medewerker

    * `identificatie`
    * `achternaam`
    * `voorletters`
    * `voorvoegselAchternaam`

**Resource "zaakobjecten"**

De resource `zaakobjecten` kent een attribuut `object`. Deze kan verwijzen naar 
meerdere type objecten waarvan nog geen bron is gestandaardiseerd.

N.B. Het attribuut `authentiek` wordt achterwege gelaten omdat geen van deze
gegevens worden aangemerkt als authentiek.

Hieronder volgt een overzicht van matchinggegevens per objecttype.

* adres

    * `identificatie`
    * `authentiek`
    * `wplWoonplaatsNaam` (=`wpl.woonplaatsNaam`)
    * `gorOpenbareRuimteNaam` (=`gor.openbareRuimteNaam`)
    * `huisnummer`
    * `huisletter`
    * `huisnummertoevoeging`
    * `postcode`

* besluit

    Niet van toepassing: URL-verwijzing mogelijk naar Besluiten API `besluit`

* buurt

    * `buurtCode`
    * `buurtNaam`
    * `gem.gemeenteCode`
    * `wykWijkCode` (=`wyk.wijkCode`)

* enkelvoudigDocument

    Niet van toepassing: URL-verwijzing mogelijk naar Documenten API `enkelvoudiginformatieobject`

* gemeente

    * `gemeenteCode`
    * `gemeenteNaam`

* gemeentelijkeOpenbareRuimte

    * `identificatie`
    * `openbareRuimteNaam`

* huishouden

    * `nummer`
    * `isGehuisvestIn` (genest JSON object)
        * Zie: `terreinGebouwdObject`

* inrichtingselement

    * `type`
    * `identificatie`
    * `naam`

* kadastraleOnroerendeZaak

    * `kadastraleIdentificatie`
    * `kadastraleAanduiding`

* kunstwerkdeel

    * `type`
    * `identificatie`
    * `naam`

* maatschappelijkeActiviteit

    * `kvkNummer`
    * `handelsnaam`

* medewerker

    Gelijk aan `Rol.betrokkene` voor `Medewerker`.

* natuurlijkPersoon

    Gelijk aan `Rol.betrokkene` voor `Natuurlijk persoon`.

* nietNatuurlijkPersoon

    Gelijk aan `Rol.betrokkene` voor `Niet-natuurlijk persoon`.

* openbareRuimte

    * `identificatie`
    * `wplWoonplaatsNaam` (=`wpl.woonplaatsNaam`)
    * `gorOpenbareRuimteNaam` (=`gor.openbareRuimteNaam`)
         
* organisatorischeEenheid

    Gelijk aan `Rol.betrokkene` voor `Organisatorische eenheid`.

* pand

    * `identificatie`

* samengesteldDocument

    * Niet van toepassing: Bestaat niet meer in Documenten API 1.0.

* spoorbaandeel

    * `type`
    * `identificatie`
    * `naam`

* status

    Niet van toepassing: URL-verwijzing mogelijk naar Zaken API `status`

* terreindeel

    * `type`
    * `identificatie`
    * `naam`

* terreinGebouwdObject

    * `identificatie`
    * `adresAanduidingGrp` (genest JSON object)
        * `numIdentificatie` (=`num.identificatie`)
        * `oaoIdentificatie` (=`oao.identificatie`)
        * `wplWoonplaatsNaam` (=`wpl.woonplaatsNaam`)
        * `gorOpenbareRuimteNaam` (=`gor.openbareRuimteNaam`)
        * `aoaPostcode` (=`aoa.postcode`)
        * `aoaHuisnummer` (=`aoa.huisnummer`)
        * `aoaHuisletter` (=`aoa.huisletter`)
        * `aoaHuisnummertoevoeging` (=`aoa.huisnummertoevoeging`)
        * `ogoLocatieAanduiding` (=`ogo.locatieAanduiding`)

* vestiging

    Gelijk aan `Rol.betrokkene` voor `Vestiging`.

* waterdeel

    * `type`
    * `identificatie`
    * `naam`

* wegdeel

    * `type`
    * `identificatie`
    * `naam`

* wijk

    * `wijkCode`
    * `wijkNaam`
    * `gemGemeenteCode` (=`gem.gemeenteCode`)

* woonplaats

    * `identificatie`
    * `woonplaatsNaam`

* wozDeelobject

    * `nummerWOZDeelObject`
    * `isOnderdeelVan` (genest JSON object)
         Zie: `wozObject`

* wozObject

    * `wozObjectNummer`
    * `aanduidingWOZobject` (genest JSON object)
        * `aoaIdentificatie` (=`aoa.identificatie`)
        * `wplWoonplaatsNaam` (=`wpl.woonplaatsNaam`)
        * `aoaPostcode` (=`aoa.postcode`)
        * `gorOpenbareRuimteNaam` (=`gor.openbareRuimteNaam`)
        * `aoaHuisnummer` (=`aoa.huisnummer`)
        * `aoaHuisletter` (=`aoa.huisletter`)
        * `aoaHuisnummertoevoeging` (=`aoa.huisnummertoevoeging`)
        * `locatieOmschrijving`

* wozWaarde

    * `waardepeildatum`
    * `isVoor` (genest JSON object)
         Zie: `wozObject`

* zakelijkRecht

    * `identificatie`
    * `avrAard` (=`avr.aard`)
    * `heeftBetrekkingOp` (genest JSON object)
         Zie: `kadastraleOnroerendeZaak`
    * `heeftAlsGerechtigde` (genest JSON object)
        * `natuurlijkPersoon` (genest JSON object)
            * Zie: `natuurlijkPersoon`
        * `nietNatuurlijkPersoon`  (genest JSON object)
            * Zie: `nietNatuurlijkPersoon`

* overige (*voor onbekende/niet-gestandaardiseerde objecten*)

    * (vrij JSON-veld)


[matching-vs-kern-gegevens]: https://discussie.kinggemeenten.nl/discussie/gemma/stuf-301/wijzig-de-term-kerngegevens-matchinggegevens
[RSGB]: https://www.gemmaonline.nl/index.php/Sectormodel_Basisgegevens:_StUF-BG
[RGBZ]: https://www.gemmaonline.nl/index.php/Documentatie_Zaak-_en_Documentservices
[polymorfisme]: https://swagger.io/docs/specification/data-models/inheritance-and-polymorphism/
