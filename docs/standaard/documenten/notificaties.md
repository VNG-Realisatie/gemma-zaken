## Notificaties
## Berichtkenmerken voor Documenten API

Kanalen worden typisch per component gedefinieerd. Producers versturen berichten op bepaalde kanalen,
consumers ontvangen deze. Consumers abonneren zich op berichten via de Notificaties API.

Hieronder staan de kanalen beschreven die door deze component gebruikt worden, met de kenmerken bij elk bericht.


### documenten

**Kanaal**
`documenten`

**Main resource**

`enkelvoudiginformatieobject`



**Kenmerken**

* `bronorganisatie`: Het RSIN van de Niet-natuurlijk persoon zijnde de organisatie die het informatieobject heeft gecreëerd of heeft ontvangen en als eerste in een samenwerkingsketen heeft vastgelegd.
* `informatieobjecttype`: URL-referentie naar het INFORMATIEOBJECTTYPE (in de Catalogi API).
* `vertrouwelijkheidaanduiding`: Aanduiding van de mate waarin het INFORMATIEOBJECT voor de openbaarheid bestemd is.

**Resources en acties**


* <code>enkelvoudiginformatieobject</code>: create, update, destroy

* <code>gebruiksrechten</code>: create, update, destroy


