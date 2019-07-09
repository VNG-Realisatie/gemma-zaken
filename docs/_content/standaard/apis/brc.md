---
title: "Besluiten API | Besluit registratie component (BRC)"
date: '14-11-2018'
weight: 80
---

*Component voor opslag en ontsluiting van besluiten en daarbij behorende metadata.*

Dit component is losgetrokken van het ZRC om besluiten vast te leggen van Zaken
-en andere objecten.

De component ondersteunt het opslaan en het naar andere applicaties ontsluiten
van gegevens over alle gemeentelijke besluiten, van elk type. Opslag vindt plaats
conform het RGBZ waarin objecten, gegevens daarvan en onderlinge relaties zijn
beschreven. Het bevat echter niet alle gegevens uit het RGBZ: documenten worden
opgeslagen in de documentenregistratiecomponent, medewerkergegevens in de
medewerkerregistratiecomponent, etc.

## Verwijzingen

![Jenkins][jenkins]

* [API-specificatie](https://besluiten-api.vng.cloud/api/v1/schema/)
* [Referentie implementatie](https://github.com/VNG-Realisatie/gemma-besluitregistratiecomponent)
* Communiceren met dit component (client)
* Zelf dit component implementeren (server)

[jenkins]: https://jenkins.nlx.io/buildStatus/icon?job=gemma-besluitregistratiecomponent-stable
