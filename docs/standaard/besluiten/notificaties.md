## Notificaties
## Berichtkenmerken voor Besluiten API

Kanalen worden typisch per component gedefinieerd. Producers versturen berichten op bepaalde kanalen,
consumers ontvangen deze. Consumers abonneren zich via de Notificatie API.

Hieronder staan de kanalen beschreven die door deze component gebruikt worden, met de kenmerken bij elk bericht.

### besluiten

**Kanaal**
`besluiten`

**Main resource**

`besluit`



**Kenmerken**

* `verantwoordelijke_organisatie`: Het RSIN van de niet-natuurlijk persoon zijnde de organisatie die het besluit heeft vastgesteld.
* `besluittype`: URL-referentie naar het BESLUITTYPE (in de Catalogi API).

**Resources en acties**


* <code>besluit</code>: create, update, destroy


