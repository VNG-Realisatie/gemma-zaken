---
title: "Zaaktypecatalogus (ZTC)"
description: ""
weight: 22
menu:
  docs:
    parent: "developers"
---

*Component voor opslag en ontsluiting van zaaktypegegevens.*

De component ondersteunt het opslaan en naar andere applicaties ontsluiten van zaaktypegegevens. Deze gegevens kunnen door applicaties worden gebruikt om voor zaken van een bepaald type de juiste gegevens(statussen, resultaattypen, documenttypen,..) te bepalen. Applicaties die gebruik maken van deze zaaktypegegevens zijn bijvoorbeeld een zaakafhandelcomponent, een vergunningcomponent of een subsidiecomponent. Opslag van zaaktypegegevens vindt plaats conform het informatiemodel ZTC. De verzameling opgeslagen zaaktypegegevens wordt ook aangeduid met de term "zaaktypecatalogus".

## Verwijzingen

![Jenkins][jenkins]

* [API-specificatie](https://ref.tst.vng.cloud/ztc/api/v1/schema/)
* [Referentie implementatie](https://github.com/VNG-Realisatie/gemma-zaaktypecatalogus)
* Test component
* Communiceren met dit component (client)
* Zelf dit component implementeren (server)

[jenkins]: https://jenkins.nlx.io/buildStatus/icon?job=gemma-zaaktypecatalogus-stable
