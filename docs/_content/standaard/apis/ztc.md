---
title: "Catalogus API | Zaak type catalogus (ZTC)"
date: '13-7-2018'
weight: 50
---

*Component voor opslag en ontsluiting van zaaktypegegevens.*

De component ondersteunt het opslaan en naar andere applicaties ontsluiten van
zaaktypegegevens. Deze gegevens kunnen door applicaties worden gebruikt om voor
zaken van een bepaald type de juiste gegevens(statussen, resultaattypen,
  documenttypen,..) te bepalen. Applicaties die gebruik maken van deze
  zaaktypegegevens zijn bijvoorbeeld een zaakafhandelcomponent, een
  vergunningcomponent of een subsidiecomponent. Opslag van zaaktypegegevens
  vindt plaats conform het informatiemodel ZTC. De verzameling opgeslagen
  zaaktypegegevens wordt ook aangeduid met de term "zaaktypecatalogus".

## Verwijzingen

![Jenkins][jenkins]

* [API-specificatie](https://catalogi-api.vng.cloud/api/v1/schema/)
* [Referentie implementatie](https://github.com/VNG-Realisatie/gemma-zaaktypecatalogus)
* Test component
* Communiceren met dit component (client)
* Zelf dit component implementeren (server)

## Testdata

Momenteel is de API van de referentie-implementatie read-only. Leveranciers en
overige ontwikkelaars die tegen de referentie-implementatie willen testen,
kunnen in de [ZTC admin][ztcadmin] data inrichten. De inloggegevens hiervoor
zijn:

* gebruikersnaam: `demo`
* wachtwoord `fmuQC4EDJ8m7vzbh3iu6`

Deze gebruiker heeft geen rechten om objecten te verwijderen, zodat referenties
van andere mensen niet stuk gaan.

[jenkins]: https://jenkins.nlx.io/buildStatus/icon?job=gemma-zaaktypecatalogus-stable
[ztcadmin]: https://catalogi-api.vng.cloud/admin
