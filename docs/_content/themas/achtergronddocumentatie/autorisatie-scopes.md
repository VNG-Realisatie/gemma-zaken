---
title: "Scopes als autorisatiemechanisme"
description: ""
weight: 40
---

## Scopes

Een scope in deze context is een label, bijvoorbeeld `zds.scopes.zaken.lezen`
waar een bepaalde betekenis aan toegekend is. We gebruiken scopes om
toegangsniveaus uit te drukken.

Toegangscontrole in de APIs speelt op verschillende niveaus, waarbij met
gegevens binnen de relevante data rekening moet gehouden worden.

In de meest eenvoudige vorm kan een scope bepalen of je al dan niet toegang
hebt tot een operatie binnen een resource. Een `alleen-lezen` scope zou je
bijvoorbeeld toegang kunnen geven op `zaak_read` en `zaak_list`, maar toegang
verbieden op `zaak_create`, `zaak_update` en `zaak_partial_update`.

Zodra je scopes gaat onderkennen die meer businesslogica bevatten, zoals scopes
koppelen aan de rol van een betrokkene, dan kan het zijn dat binnen collecties
een andere (sub)set van records teruggegeven wordt doordat de scope dit inperkt.
Een concreet voorbeeld hiervan kunnen zaakobjecten zijn die wel of niet
privacygevoel zijn. Panden zouden bijvoorbeeld altijd teruggegeven kunnen
worden (voor elke scope), maar gerelateerde natuurlijke personen zouden
weggelaten kunnen worden voor een 'publieke' scope.

Tot slot onderkennen we nog een niveau waarop gegevens ingehouden kunnen worden.
Indien je een record mag lezen, dan kan het zijn dat je niet alle attributen
binnen de record mag lezen. Bijvoorbeeld een klantcontactcentrummedewerker
zou de voornaam + naam van de zaakinitiator mogen lezen, maar niet het BSN
van deze persoon.

De uitdaging bestaat erin om een set van scopes te definieren die beheersbaar
is, maar toch toelaat om om te gaan met:

- vertrouwelijkheidsaanduiding
- roltypen
- AVG/privacy

## Algemeen

_Inzichten van Arjan_:

De mogelijkheden voor een gebruiker om gegevens van een object - zoals
'Zaak 1234' of 'Document Abcd' - te mogen raadplegen en/of bewerken hangen
m.i. af van (minimaal) vier factoren:

1. **_De categorie van het object_**.
   Bijvoorbeeld het zaaktype van een zaak, of een zaak al dan niet beeindigd
   is, etc. Zo zal een gebruiker veelal slechts zaken van bepaalde zaaktypen
   mogen raadplegen, of alleen onderhanden zaken.

2. **_De betrokkenheid van de gebruiker bij het object_**.
   Voor sommige objecten kan hiervan sprake zijn, bijvoorbeeld zaken
   (betrokkenen in rollen), veelal is hiervan voor andere objecten geen sprake
   (zoals zaaktype). Zo zijn de mogelijheden voor een gebruiker zijnde een
   'Behandelaar van een Zaak' anders dan een 'Initiator van een zaak' en geheel
   anders dan een gebruiker die geen Rol heeft als Betrokkene bij de zaak.

3. **_De categorie van het gegeven (van het object)_**.
   De gebruiker wil iets met een gegeven (of relatie) van het object (of met
   een groep gegevens). Met het ene gegeven zal hij/zij meer mogen dan met een
   ander gegeven. Het maakt bijvoorbeeld nogal uit of het om persoonsgegevens
   gaat of om archiveringsgegevens.

4. **_De mate van vertrouwelijkheid van het gegeven (van het object)_**.
   Ook al zou een gebruiker op grond van de voorgaande factoren het gegeven
   mogen raadplegen, dan nog kan het zijn dat hij/zij dat vanwege een bepaalde
   mate van vertrouwelijkheid toch niet mag.

[uitwerken op de dwarsdoorsnedes van deze factoren, te beginnen met rollen versus vertrouwelijkheidniveau's]

## Op basis van roltype:

### Adviseur

Context-check: gebruiker heeft rol adviseur op de zaak in kwestie

`GET /api/v1/rollen/?zaak=<url>&betrokkene=<url>&rolomschrijving=Adviseur`

**Resources**:

* Zaak:
    * mag alle attributen lezen
    * mag `toelichting` bewerken
* ZaakInformatieObject:
    * mag lezen
    * mag toevoegen
    * mag bewerken (`titel`, `beschrijving`)
* EnkelvoudigInformatieObject:
    * mag toevoegen
    * mag lezen
* ZaakObject:
    * mag lezen
    * mag toevoegen
* Klantcontact:
    * mag lezen
    * mag toevoegen

Challenges:

* limiteer in DRC tot zaken waar NP adviseur is

**Scopes nodig voor deze rol**:

* `zds.scopes.zaken.lezen`
* ...

### Behandelaar

Context-check: gebruiker heeft rol adviseur op de zaak in kwestie

`GET /api/v1/rollen/?zaak=<url>&betrokkene=<url>&rolomschrijving=Behandelaar`

Mogelijks subtypes:

* intake
* archivering
* algemeen

**Resources**:

* Zaak:
    * mag alle attributen lezen
    * mag alle attributen bewerken, behalve:
        - bronorganisatie
        - identificatie
        - zaaktype
        - registratiedatum
        - verantwoordelijkeOrganisatie
* Status:
    * mag alles lezen
    * mag alle statussen behalve de laatste zetten
* Zaaktype:
    * mag alles lezen
* Rol/Betrokkene:
    * mag alles lezen
* Klantcontact:
    * mag alles lezen
* ZaakInformatieObject:
    * mag alles lezen
* InformatieObject:
    * mag alles lezen

Challenges:

* beperken op basis van:
    * zaaktypes
    * zaak bij informatieobjecten

**Scopes nodig voor deze rol**:

* `zds.scopes.zaken.lezen`
* ...

### Belanghebbende

Mogelijks subtypes:

* openbaar
* privacy-gevoelig

**Resources**:

* Zaak:
    * beperkt lezen:
        - identificatie
        - bronorganisatie
        - omschrijving
        - registratiedatum?
        - zaaktype?
        - ...?
* InformatieObject:
    * beperkt lezen: afhankelijk van informatieobject vertrouwelijkheidniveau
        - openbaar
        - documenten waarbij belanghebbende afzender of bestemmeling is
* Besluit: lezen (ev. afhankelijk van status)
* Klantcontact: niets
* ZaakObject: afhankelijk van objectType
* Status: alles lezen
* Rol: niets (of enkel zaakcoordinator)

### Beslisser

**Resources**:

* Besluit:
    * mag toevoegen
    * mag lezen
    * mag bewerken
* InformatieObject: (die aan besluit hangen)
    * mag lezen
    * mag toevoegen (?)
    * mag bewerken (?)
* Rest: mag lezen (m.u.v. privacy gevoelig)

### Initiator

**Resources**:

* Zaak:
    - mag toevoegen
    - mag lezen
* InformatieObject:
    - mag toevoegen
    - mag lezen
* ZaakInformatieObject:
    - mag toevoegen
    - mag lezen

**Scopes nodig voor deze rol**:

* `zds.scopes.zaken.aanmaken`
* `zds.scopes.zaken.lezen` (?)
* ...

### TODO

- klantcontacter

- zaakcoordinator

- mede-initiator


## Scope-definities

Dit is heel erg WIP - we zoeken een goede balans!

Een `✓` betekent dat het in de referentieimplementatie gebouwd is.

### Zaken openbaar lezen

**Label**

`zds.scopes.zaken.lezen.openbaar`

**Omvat**

* Toegang tot de volgende resources:
    * Zaak
    * Status
    * ZaakType
    * StatusType

### Zaken alles lezen (✓)

Superset van `zds.scopes.zaken.lezen.openbaar`

**Label**

`zds.scopes.zaken.lezen`

**Omvat**

* Kan alle attributen van zaken lezen, incl. privacy-gevoelig
* Kan alle statussen van zaken lezen, met alle attributen
* Kan alle zaakobjecten van zaken lezen, met alle attributen

### Zaken aanmaken (✓)

**Label**

`zds.scopes.zaken.aanmaken`

**Omvat**

* `zaak_create`
* `status_create` (indien nog geen status gezet is)
* `rol_create`
* `zaakobject_create`

### Zaken bewerken (✓)

**Label**

`zds.scopes.zaken.bijwerken`

**Omvat**

* `zaak_update` (alle attributen die niet alleen-lezen zijn)
* `zaak_partial_update` (alle attributen die niet alleen-lezen zijn)

### Zaakdocumenten registreren

**Label**

`zds.scopes.zaakinformatieobjecten.aanmaken`
