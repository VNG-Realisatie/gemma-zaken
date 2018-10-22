# Scopes

- vertrouwelijkheidsaanduiding
- roltypen
- AVG/privacy

## Algemeen
[bijdrage Arjan]<br>
De mogelijkheden voor een gebruiker om gegevens van een object, zoals Zaak 1234 of Document Abcd, te mogen raadplegen en bewerken (cq. om een operatie op een - voorkomen in een - resource uit te voeren) hangen m.i. af van (minimaal) vier factoren.
1) **_De categorie van het object_**. Bijvoorbeeld het zaaktype van een zaak, of een zaak al dan niet beeindigd is, etc. Zo zal een gebruiker veelal slechts zaken van bepaalde zaaktypen mogen raadplegen, of alleen onderhanden zaken. 
2) **_De betrokkenheid van de gebruiker bij het object_**. Voor sommige objecten kan hiervan sprake zijn, bijvoorbeeld zaken (betrokkenen in rollen), veelal is hiervan voor andere objecten geen sprake (zoals zaaktype). Zo zijn de mogelijheden voor een gebruiker zijnde een Behandelaar van een Zaak anders dan een Initiator van een zaak en geheel anders dan een gebruiker die geen Rol heeft als Betrokkene bij de zaak. 
3) **_De categorie van het gegeven (van het object)_** De gebruiker wil iets met een gegeven (of relatie) van het object (of met een groep gegevens). Met het ene gegeven zal hij/zij meer mogen dan met een ander gegeven. Het maakt bijvoorbeeld nogal uit of het om persoonsgegevens gaat of om archiveringsgegevens. 
4) **_De mate van vertrouwelijkheid van het gegeven (van het object)_**. Ook al zou een gebruiker op grond van de voorgaande factoren het gegeven mogen raadplegen, dan nog kan het zijn dat hij/zij dat vanwege een bepaalde mate van vertrouwelijkheid toch niet mag.

[uitwerken op de dwarsdoorsnedes van deze factoren, te beginnen met rollen versus vertrouwelijkheidniveau's]


## Op basis van roltype:

### `zds.scopes.roltype.adviseur`

- zaak:
    * lezen
    * bewerken (toelichting)
    * documenten aan zaak koppelen/bewerken
    * objecten aan zaak koppelen/bewerken
- klantcontact: (adviseur kan de klant contacteren)
    * lezen
    * registreren
- besluit: nvt
- informatieobjecten
    * toevoegen

### `zds.scopes.roltype.behandelaar`

(eventueel behandelaar.intake, behandelaar.archivering, behandelaar.algemeen)

- zaak
    * alles, behalve:
      - bewerken bronorganisatie, identificatie, zaaktype, registratiedatum, verantwoordelijkeOrganisatie,
      - zetten laatste status (cfr. ZTC)

- rest: bijna overal bij

### `zds.scopes.roltype.belanghebbende`

-> scope verfijning: privacy gevoelig of niet

alleen lezen - heel beperkt

- zaak: beperkt
- informatieobjecten: afhankelijk van informatieobject vertrouwelijkheidniveau
    * openbaar
    * documenten waarbij belanghebbende afzender of bestemmeling is (TODO!)
- besluiten: lezen (ev. afhankelijk van status)
- klantcontacten: niets
- zaakobjecten: afhankelijk van objectType
- statussen: alles lezen
- rollen: niets (of enkel zaakcoordinator)

### `zds.scopes.roltype.beslisser`

- besluit: aanmaken, lezen, bewerken
- informatieobjecten: die bij besluit hangen
- lezen (m.u.v. privacy)

### `zds.scopes.roltype.initiator`

- zaak: aanmaken
- informatieobject: aanmaken
- zaakinformatieobject: aanmaken
-




- initiator

- klantcontacter

- zaakcoordinator

- mede-initiator
