---
title: "Authenticatie en autorisatie"
date: '22-10-2018'
weight: 70
---

De APIs moeten beveiligd zijn tegen ongeautoriseerde toegang, om te voorkomen
dat (gevoelige) gegevens op straat komen te liggen. In dit document wordt het
ontwerp van het autorisatiemechanisme toegelicht.

## Aanvalsvectoren

Om te beginnen schetsen we de mogelijke aanvallen waartegen we beschermen en
wat we buiten scope laten.

### Een gebruiker van buitenaf probeert de APIs te benaderen

1. Hiertegen kan je in eerste instantie beschermen door de API niet publiek
   (over internet) beschikbaar te maken, zoals in een afgeschermd, intern
   netwerk binnen de organisatie.

2. NLX voorziet in een oplossing om over organisaties heen via een federatief
   systeem gegevens te ontsluiten. De gebruiker dient hiervoor een outway op
   te starten en bekend te zijn in het NLX netwerk.

   NLX is echter optioneel, de gekozen oplossing laat ook toe om over
   organisaties heen over (publiek) internet op een veilige manier gegevens
   uit te wisselen. Dit is relevant voor SAAS oplossingen, bijvoorbeeld.

### Een medewerker binnen de organisatie probeert de APIs te benaderen

Indien de APIs beschikbaar gesteld worden binnen een afgesloten netwerk, dan
kan je zonder autorisatieoplossing alle gegevens via de APIs ontsluiten. Dit is
de meest reële vector waartegen we beschermen.

### Een applicatie leest meer uit dan nodig

Een applicatie kan geautoriseerd zijn op de APIs voor een subset van alle
gegevens. Veiligheidslekken/programmeerfouten in de applicatie zouden dan
kunnen leiden tot het ontsluiten van meer gegevens dan nodig. De
autorisatieoplossing biedt hier ook oplossingen om dit te voorkomen door te
limiteren tot welke subset van gegevens een applicatie toegang heeft.

## Authenticatie en autorisatie

Authenticatie en autorisatie binnen de APIs zijn van elkaar losgekoppeld. De
APIs hebben geen kennis van de feitelijke eindgebruiker die een taakapplicatie
gebruikt. Echter, binnen organisaties (gemeentes) kunnen feitelijke
eindgebruikers in bepaalde rollen onderverdeeld worden die aan permissies
gekoppeld zijn.

De APIs kennen **scopes** - dit zijn sets van permissies die gegroepeerd worden,
in een generieke vorm. Deze worden afgestemd volgens typisch gebruik. De
taakapplicaties van organisaties communiceren met de APIs op basis van deze
scopes.

### Gelaagdheid authenticatie en autorisaties

![piramide](./_assets/autorisaties.png?raw=true)

Het totale autorisatieverhaal is een gelaagde oplossing.

In de Common Ground visie staat NLX in de basis, waarbij organisaties
geautoriseerd zijn om met andere organisaties te verbinden via out- en inways.
Dit is een gefederaliseerd systeem - als je met een organisatie mag
verbinden, kan je in principe bij alle APIs die de inway ontsluit.

Op de tweede laag staat de API-autorisatie. In een ZGW-context kan het niet zo
zijn dat eender welke applicatie van een organisatie alle data kan opvragen
uit een ZRC (of andere componenten). Op deze laag wordt bepaald welke
_applicaties_ geautoriseerd zijn op welke gegevens, bijvoorbeeld welke operaties
toegelaten zijn voor een subset van zaaktypes. Dit document gaat over deze
laag.

De bovenste laag houdt zich bezig met individuele gebruikers, en wordt ingevuld
door de taakapplicaties en/of de gemeente. Deze leggen vast wat de permissies
zijn van een gebruiker, welke acties deze in een applicatie mag uitvoeren. De
applicatie dient zelf een autorisatiemodel te implementeren die voorkomt dat
de applicatie API calls maakt die eigenlijk niet mogen voor deze gebruiker.

Onderaan dit document is een sequence-diagram van de request-response cycle
van eindgebruiker tot de API, inclusief NLX-interactie.

## Authenticatie

Authenticatie is formeel buiten de scope van de APIs - je kan niet inloggen
op de API met gebruikersnaam/wachtwoord bijvoorbeeld. Dit ligt bij de gemeente.

Taakapplicaties haken in op het authenticatiemechanisme dat bij een gemeente
gebruikt wordt. Deze zijn vervolgens verantwoordelijk voor het genereren van
een JSON Web Token (JWT) wat toegang verleent tot de API aan de taakapplicatie.

De gemeente heeft hier alle vrijheid - indien de gemeente intern OAUTH2 wil
gebruiken, SAML, Active Directory..., dan kan dat - daar zeggen wij niets over.

## Autorisatie

[JSON Web Token](https://jwt.io/) is een mechanisme om stateless claims te
kunnen uitwisselen. Een token wordt _ergens_ gegenereerd en via een HTTP Header
meegestuurd in een request naar de API. De API moet vervolgens verzekeren
dat de integriteit van het token in orde is, en past daarna de claims in de
payload toe.

JWT bestaat uit drie stukken - een header, payload en signature. De APIs moeten
de shared secret kennen om de signature te kunnen controleren. Om redenen van
beveiliging is het verstandig om per organisatie (of zelfs applicatie binnen een
organisatie) een secret in te stellen. Dit brengt wat beheer-overhead met zich
mee.

JWT kunnen niet gerevoked worden - daarom is het wenselijk om een korte expiry
toe te kennen (bijvoorbeeld 24h). Indien er zich security breaches voordoen,
dan moet het betrokken shared secret veranderd worden.

In het JWT nemen we in de payload op wat het `client_id` is van de consumer.
Dit dient om uniek te identificeren welke _applicatie_ met de provider
communiceert. Applicaties registreren zich out-of-band bij providers, waarbij
ze een `client_id` en een `secret` toegekend krijgen. Dit kan verlopen via een
applicatiebeheerder bijvoorbeeld - out-of-band betekent hierbij dat dit niet
zonder menselijke controle kan gebeuren. Het secret wordt gebruikt om het JWT
cryptografisch te ondertekeken, waardoor de provider garantie heeft dat de
consumer ook echt is wie die beweert te zijn (via het `client_id`).

Een autorisatiecomponent (AC) is verantwoordelijk voor het bijhouden van
autorisaties voor een applicatie. Typisch zien we dit voor ons als een
component die centraal (per omgeving zoals testing, acceptatie en productie)
binnen de gemeente ingericht is. De component ontsluit zelf een API waarmee
de autorisaties van consumers ingericht worden.

Een `Applicatie` resource heeft de volgende attributen:

* `client_ids`: een lijst van client IDs. Dezelfde applicatie zal typisch
  tegen meerdere componenten praten (ZRC & ZTC bijvoorbeeld). Om lekken te
  voorkomen en goede beveiligingsprincipes toe te passen, gaan we uit van 1
  client ID per component waarmee gecommuniceerd wordt. De applicatie zelf is
  echter 1 entiteit waarop de autorisaties geconfigureerd worden, dus we houden
  alle `client_ids` bij waarmee deze zich identificeert. Client IDs dienen
  uniek te zijn.

* `label`: een beschrijvend label voor de applicatie, zodat duidelijk is om
  welke applicatie binnen de organisatie het gaat. Bijvoorbeeld:
  "Melding Openbare Ruimte (burger)"

* `autorisaties`: een lijst van autorisaties. Een autorisatie karakteriseert
  zich met de verplichte eigenschappen `component` en `scopes`. De resterende
  eigenschappen worden bepaald door de waarde van `component`. Bijvoorbeeld:

  ```json
  {
    "component": "ZRC",
    "scopes": ["zds.scopes.zaken.lezen"],
    "zaaktype": "https://catalogi-api.vng.cloud/api/v1/catalogussen/123/zaaktypen/abc",
    "maxVetrouwelijkheidaanduiding": "geheim"
  }
  ```
  Het zaaktype wordt gerefereerd via de URL uit het ZTC, en er wordt aangegeven
  welke scopes van toepassing zijn en welke vertrouwelijkheidaanduiding
  maximaal toegelaten is (inclusief). De ZRC component definieert hierbij dan
  dat ook `zaaktype` en `maxVetrouwelijkheidaanduiding` gedefinieerd moeten
  worden.

We voorzien in een minimale-beheerslastoptie om een applicatie alle
autorisaties te geven.

Wanneer een consumer dan via de API een operatie probeert uit te voeren bij een
provider, dan is het aan de provider om:

1. Het JWT te valideren: uitlezen van het `client_id` en op basis van het
   shared `secret` moet het JWT zelf gevalideerd worden.

2. Indien het JWT valide is, dan moet de provider het AC bevragen voor het
   betreffende `client_id`. Het AC antwoordt met de autorisaties voor deze
   consumer.

3. De provider dient na te gaan welke zaak het betreft, en toetst deze zaak
   tegen de autorisaties:

   * is het een zaaktype wat geautoriseerd is?
   * is de operatie toegelaten conform de scopes die in de autorisatie vermeld
     zijn?
   * is de zaak van een vertrouwelijkheidaanduiding die binnen de autorisatie
     valt?

Zodra een stap faalt, dan wordt een `HTTP 403` fout gestuurd naar de consumer.

Bij het opvragen van collecties (bijvoorbeeld: een lijst van zaken) dient de
provider deze dataset bij de bron te filteren op basis van de configureerde
autorisaties in het AC, conform het privacy-by-design principe.

## Delegatie van API A naar API B

Een ZRC dient vaak het achterliggende ZTC te bereiken als onderdeel van het
afhandelen van een operatie door een consumer op het ZRC. Hiervoor dient het
ZRC geauthenticeerd te zijn bij het ZTC.

We gebruiken niet het consumer-JWT hiervoor. De ZRC staat zelf als applicatie
bekend bij het ZTC, en deze construeert een eigen token.

## Sequence-diagram

[TODO - controle of dit nog opgaat]

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

## Wijzigingen ten opzichte van de vorige vorm

In een eerdere sprint werden de scope/zaaktypes claims opgenomen in het JWT
wat verstuurd wordt van de (taak)applicatie naar de API. Dit is niet langer
zo - nu gebruiken we het JWT enkel nog om de (taak)applicatie te autoriseren
met de betreffende API te communiceren. De autorisatie van de acties van de
applicatie zelf is gedelegeerd naar de autorisatiecomponent.

Dit brengt de autorisaties van een taakapplicatie strikter onder controle van
de gemeente, aangezien deze op een AC inricht (of instelt) welke acties
toegelaten zijn op welke zaaktypes. Voordien was de (taak)applicatie zelf
verantwoordelijk voor het genereren van een JWT, en kon deze claims opnemen
die te breed waren. Dit zou dan pas na een audit duidelijk worden. In de
nieuwe/huidige vorm wordt dat voorkomen.

(Taak)applicaties zijn nog steeds zelf verantwoordelijk voor het authenticeren
van eindgebruikers en ienen hiervoor een eigen autorisatiemodel op te stellen.
Dit valt nog steeds buiten de scope van de ZGW APIs.

## Referenties

* [JWT vs. OAUTH](https://community.apigee.com/questions/21139/jwt-vs-oauth.html)
* [What the heck is OAUTH?](https://developer.okta.com/blog/2017/06/21/what-the-heck-is-oauth)
* [rfc7519](https://tools.ietf.org/html/rfc7519)
* [JWT Signing Algorithms](https://auth0.com/blog/json-web-token-signing-algorithms-overview/)
* [NLX en autorisatieservices](https://gitlab.com/commonground/nlx/merge_requests/400)
