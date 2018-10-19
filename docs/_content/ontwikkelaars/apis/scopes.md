# Scopes

- vertrouwelijkheidsaanduiding
- roltypen
- AVG/privacy




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
