---
title: "Authenticatie en autorisatie"
date: '22-10-2018'
---

Authenticatie en autorisatie binnen de APIs zijn van elkaar losgekoppeld. De
APIs hebben geen kennis van de feitelijke eindgebruiker die een taakapplicatie
gebruikt. Echter, binnen organisaties (gemeentes) worden feitelijke
eindgebruikers in bepaalde rollen onderverdeeld die aan permissies gekoppeld
zijn.

De APIs kennen scopes - dit zijn sets van permissies die gegroepeerd worden,
in een generieke vorm. Deze worden afgestemd volgens typisch gebruik. De
taakapplicaties van organisaties communiceren met de APIs op basis van deze
scopes.

Onderaan dit document is een sequence-diagram van de request-response cycle
van eindgebruiker tot de API, inclusief NLX-interactie.

## Authenticatie

Authenticatie is formeel buiten de scope van de APIs - je kan niet inloggen
op de API met gebruikersnaam/wachtwoord bijvoorbeeld. Dit ligt bij de gemeente.

Taakapplicaties haken in op het authenticatiemechanisme dat bij een gemeente
gebruikt wordt. Deze zijn vervolgens verantwoordelijk voor het genereren van
een JWT token (met scopes conform de rechten van de eigenlijke eindgebruiker).

De gemeente heeft hier alle vrijheid - indien de gemeente intern OAUTH2 wil
gebruiken, SAML, Active Directory..., dan kan dat - daar zeggen wij niets over.

Wat essentieel is, is dat de claims binnen de gemeente vertaald worden naar
de scopes gedefinieerd in de ZDS APIs, zodat iedereen dezelfde 'taal' spreekt.

## Autorisatie

[JSON Web Token](https://jwt.io/) is een mechanisme om stateless claims te
kunnen uitwisselen. Een token wordt _ergens_ gegenereerd en via een HTTP Header
meegestuurd in een request naar de API. De API moet vervolgens verzekeren
dat de integriteit van het token in orde is, en past daarna de claims in de
payload toe. Hierbij bevat het token zelf alle informatie en hoeft er niet
met een (centrale) autorisatie-server gecommuniceerd worden.

JWT bestaat uit drie stukken - een header, payload en signature. Uitgevers van
tokens bestaan bij de organisaties (gemeentes). De APIs moeten de shared
secret kennen om de signature te kunnen controleren. Naar veiligheid toe is
het verstandig om per organisatie (of zelfs applicatie binnen een organisatie)
een secret in te stellen. Dit brengt wat beheer-overhead met zich mee.

JWT kunnen niet gerevoked worden - daarom is het wenselijk om een korte expiry
toe te kennen (bijvoorbeeld 24h). Indien er zich security breaches voordoen,
dan moet het betrokken shared secret veranderd worden.

## Delegatie van API A naar API B

We kunnen aparte of dezelfde tokens gebruiken bij API-API communicatie. Welke
keuze gemaakt wordt, wordt uitgewerkt tijdens implemantie om te bepalen wat
meest developer-friendly is.

## Sequence-diagram

Het onderstaande diagram vetrekt uit de browser bij de eindgebruiker (een
medewerker binnen de organisatie, bijvoorbeeld een KCC medewerker). Deze
logt in op de MOR-applicatie, die met de auth-service van de organisatie
praat. Deze service geeft een JWT terug met de correcte scopes voor deze
gebruiker.

Vervolgens wordt dit JWT via de NLX outway & inway naar de API verstuurd. De
zaken-API controleert de integriteit van het token doordat de `secret` gedeeld
is tussen de API en de auth service van de organisatie.

Dit mechanisme zet zich door tot aan de zaaktypecatalogus.

![sequence](./_assets/authenticatie-autorisatie.png?raw=true)


## Referenties

* [JWT vs. OAUTH](https://community.apigee.com/questions/21139/jwt-vs-oauth.html)
* [What the heck is OAUTH?](https://developer.okta.com/blog/2017/06/21/what-the-heck-is-oauth)
* [rfc7519](https://tools.ietf.org/html/rfc7519)
* [JWT Signing Algorithms](https://auth0.com/blog/json-web-token-signing-algorithms-overview/)
