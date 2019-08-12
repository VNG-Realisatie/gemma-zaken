---
title: "Caching op API-niveau"
date: '05-08-2019'
---

In de Common Ground visie wordt data bij de bron opgeslagen en ontsloten via
(REST) APIs. Indien je vaak de API bevraagt, dan komt het voor dat de resource
zelf niet gewijzigd is en dat je onnodig gegevens uitwisselt over HTTP waar
verder niets mee gedaan wordt.

Deze uitwisseling van gegevens brengt overhead met zich mee en belast consumers,
met een mindere gebruikservaring voor eindgebruikers tot gevolgd, omdat deze
moeten wachten tot alles opgehaald is.

[User story #1096](https://github.com/VNG-Realisatie/gemma-zaken/issues/1096)

## Caching als oplossing

Consumers kunnen ervoor kiezen om gegevens te cachen. Dit is uitermate geschikt
voor resources die zelden wijzigen zoals zaaktypen, informatieobjecttypen...
maar ook voor resources zoals documenten, resultaten... die minder vaak
wijzigen.

De APIs kunnen hier voorzien in een mechanisme om consumers te informeren over
de "versheid" van de gecachete gevens, met als resultaat dat er enkel data
over het netwerk gaat als er iets gewijzigd is.

Dit is een opt-in mechanisme, consumers kunnen er ook voor kiezen om altijd
de resource(s) volledig op te vragen.

## Mechanisme

Er bestaat een standaard HTTP Header `ETag` die toelaat om een bepaalde 'versie'
van een resource te identificeren. APIs bepalen de waarde en geven deze mee in
de `ETag` header bij het opvragen van resources. Consumers kunnen deze waarde
opslaan in de resource cache.

Vervolgens kan bij een nieuwe opvraag van dezelfde resource gebruik gemaakt
worden van de HTTP Header `If-None-Match` - deze maakt het verzoek conditioneel.
De API antwoordt met een `HTTP 200` bericht op `GET` en `HEAD` requests als dit
niet meer de huidige versie van de resource is. Indien het wel nog de huidige
versie is, dan antwoordt de API met een `HTTP 304` response.

De `If-Match` header bestaat ook, die kent het inverse gedrag. In het kader van
caching focussen we in eerste instantie op het ondersteunen van de `ETag` en
`If-None-Match` headers.

Merk op dat de waarde van deze headers een lijst van `ETag`s kan zijn,
gescheiden met een komma.

**Weak validators**

Er bestaat een onderscheid tussen weak en strong comparisons, waarbij weak
comparison inhoudt dat de resources semantisch equivalent zijn.

Een voorbeeld hiervan is dezelfde resource, maar op verschillende domeinen - de
URL referenties in de resource verschillen dan, maar inhoudelijk zijn ze
hetzelfde.

**Strong validators**

Een voorbeeld hiervan is het aanmaken van een zaak met een bepaalde
omschrijving (situatie A). De omschrijving wordt daarna twee keer (situatie B
en C) bijgewerkt. Bij de laatste aanpassing (situatie C) werd de waarde
opgegeven die ook gebruikt is toen de zaak werd aangemaakt (dus gelijk aan
situatie A). Als er verder geen attributen gewijzigd zijn, zal de hash van
situatie A en C hetzelfde zijn. Als een consumer nooit de zaak heeft opgevraagd
in situatie B, zal de consumer de gecachete versie van situatie A blijven
gebruiken. Situatie A en C zijn namelijk inhoudelijk hetzelfde. Resource versie
A en C zijn naast elkaar niet van elkaar te onderscheiden.

In eerste instantie beperken we ons tot strong comparisons.

## Berekening van de ETag waarde

Uitgangspunten:

* De `ETag` betreft de _resource_ en niet de gegevens van het onderliggende
  datamodel.
* De APIs wisselen enkel JSON gegevens uit

We beschouwen daarom de JSON-weergave in de API van een resource, en nemen de
`md5`-hash hiervan, waarbij we de keys in de JSON deterministisch sorteren (!).

De werkelijke vorm/berekening van de `ETag` hoeft in principe niet op deze
manier te gebeuren, maar helpt wel in de voorspelbaarheid. Uiteindelijk is het
belangrijk dat de consumer de `ETag` waarde krijgt en kan gebruiken om deze
terug te sturen naar de provider.

## Wat met concurrency?

Er bestaat er een risico dat gegevens concurrent bijgewerkt worden door
verschillende consumers.

Dit probleem kan ook met `ETag`s en conditional updates opgelost worden, maar
dat is voor een ander moment.

## Bronnen

* [API development: ETags and Conditional Get](https://fideloper.com/api-etag-conditional-get)
* [MDN: ETag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag)
* [Implementing HTTP Caching...](https://stackoverflow.com/questions/26615183/implementing-http-caching-etag-feature-using-md5-in-asp-net-web-api)
* [ETags](https://specs.openstack.org/openstack/api-wg/guidelines/etags.html)
