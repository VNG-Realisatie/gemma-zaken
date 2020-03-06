---
title: Ontwikkelaars
---
<!-- De ZGW API-standaarden worden gedefineerd in [de OAS3-specificatie en het voorgeschreven runtime-gedrag](../standaard/index). Om ontwikkelaars bij gemeentes en leveranciers te helpen met het realiseren  -->
De ZGW API-standaarden worden gedefineerd in [de OAS3-specificatie en het voorgeschreven runtime-gedrag](../standaard/index.md). Om ontwikkelaars bij gemeentes en leveranciers te helpen met het realiseren
van, en aansluiten op, verschillende producten die volgens de ZGW API-standaarden
werken, zijn naast de bovengenoemde stanadaardspecificaties, voor de verschillende API's referentie-implementaties gerealiseerd. Hierbij zijn diverse handeidingen en tutorials gemaakt. Hieronder een overzicht:

## Handleidingen

### Algemene handleidingen
De handleidingen vormen een algemene introductie voor ontwikkelaars die met de ZGW API's aan de slag willen.
1. [Snel aan de slag met de gehoste referentie-implementatie](./handleidingen-en-tutorials/api-guides)
2. [Installatie en configuratie van een (lokale) kopie van de referentie-implementatie](./handleidingen-en-tutorials/installatie-en-configuratie)
3. [Gebruik van de demo-applicatie](./handleidingen-en-tutorials/demo-applicatie)
4. [Gebruik van testscenario's](./handleidingen-en-tutorials/test-scenarios)
5. [Large files upload (Engels)](./handleidingen-en-tutorials/large-files)

### Tutorials
Tutorials zijn introducties gericht op specifieke functionaliteiten binnen de ZGW API's. Deze tutorials Ze zijn ontwikkeld voor gebruik tijdens API lab-bijeenkomsten, maar kunnen ook individueel doorlopen worden.
1. [Eenmalige setup van de referentie-implementaties](./handleidingen-en-tutorials/eenmalige-setup)
2. [Aan de slag met notificeren](./handleidingen-en-tutorials/notificeren)
3. [Aan de slag met archiveren](./handleidingen-en-tutorials/archiveren) 

## Testomgevingen

VNG-Realisatie stelt de referentieimplementaties beschikbaar op een aantal
omgevingen. Er wordt onderscheid gemaakt tussen twee soorten omgevingen - die
volledig van elkaar gescheiden zijn:

**Stable**

De stable omgevingen zijn de huidige versie van de standaard (of release
candidates daarvan). Deze worden in principe enkel bijgewerkt met bugfixes.
Er zit altijd een versie tag aan gekoppeld. Dit komt in principe overeen met
de `master` branches van de referentieimplementaties.

Deze omgevingen zijn:

* https://zaken-api.vng.cloud
* https://documenten-api.vng.cloud
* https://catalogi-api.vng.cloud
* https://besluiten-api.vng.cloud
* https://notificaties-api.vng.cloud
* https://autorisaties-api.vng.cloud
* https://zaken-auth.vng.cloud


**Volgende release**

Deze omgevingen zijn de nieuwe versies die in ontwikkeling zijn. Ze worden
continue bijgewerkt op basis van de `develop` branch van de
referentieimplementaties. Deze omgevingen dienen om nieuwe features uit te
testen en bugs op te sporen.

Je kan ze vinden op:

* https://zaken-api.test.vng.cloud
* https://documenten-api.test.vng.cloud
* https://catalogi-api.test.vng.cloud
* https://besluiten-api.test.vng.cloud
* https://notificaties-api.test.vng.cloud
* https://autorisaties-api.test.vng.cloud
* https://zaken-auth.test.vng.cloud
