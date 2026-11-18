## Notificaties
## Berichtkenmerken voor Zaken API

Kanalen worden typisch per component gedefinieerd. Producers versturen berichten op bepaalde kanalen,
consumers ontvangen deze. Consumers abonneren zich via de Notificaties API op berichten.

Hieronder staan de kanalen beschreven die door deze component gebruikt worden, met de kenmerken bij elk bericht.

### zaken

**Kanaal**
`zaken`

**Main resource**

`zaak`



**Kenmerken**

* `bronorganisatie`: Het RSIN van de Niet-natuurlijk persoon zijnde de organisatie die de zaak heeft gecreeerd. Dit moet een geldig RSIN zijn van 9 nummers en voldoen aan <a href="https://nl.wikipedia.org/wiki/Burgerservicenummer#11-proef" rel="nofollow">https://nl.wikipedia.org/wiki/Burgerservicenummer#11-proef</a>
* `zaaktype`: URL-referentie naar het ZAAKTYPE (in de Catalogi API) in de CATALOGUS waar deze voorkomt
* `vertrouwelijkheidaanduiding`: Aanduiding van de mate waarin het zaakdossier van de ZAAK voor de openbaarheid bestemd is.

**Resources en acties**


* <code>zaak</code>: create, update, destroy

* <code>status</code>: create

* <code>zaakobject</code>: create, update, destroy

* <code>zaakinformatieobject</code>: create

* <code>zaakeigenschap</code>: create, update, destroy

* <code>klantcontact</code>: create

* <code>rol</code>: create, destroy

* <code>resultaat</code>: create, update, destroy

* <code>zaakbesluit</code>: create

* <code>zaakcontactmoment</code>: create

* <code>zaakverzoek</code>: create


