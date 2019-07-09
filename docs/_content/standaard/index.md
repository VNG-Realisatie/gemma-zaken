---
title: ZGW API Standaard
layout: subjects
---

De ZGW API Standaard bestaat uit 2 delen:

* [Standaard ("in ontwikkeling")](standaard) als startpunt om de APIs te
  implementeren of te gebruiken.
* [API specificaties](apis/index) met alle beschikbare resources en attributen.

Hieronder de directe links naar alle Open API specificaties (OAS):

* [Zaken API specificatie](https://zaken-api.vng.cloud/api/v1/schema/)
* [Catalogus API specificatie](https://catalogi-api.vng.cloud/api/v1/schema/)
* [Documenten API specificatie](https://documenten-api.vng.cloud/api/v1/schema/)
* [Besluiten API specificatie](https://besluiten-api.vng.cloud/api/v1/schema/)
* [Autorisaties API specificatie](https://autorisaties-api.vng.cloud/api/v1/schema/)
* [Notificaties API specificatie](https://notificaties-api.vng.cloud/api/v1/schema/)
* [Notificaties API specificatie voor consumers](https://redocly.github.io/redoc/?url=https://zaakgerichtwerken.vng.cloud/api-specificatie/nrc/consumer-api/openapi.yaml)

In de figuur hieronder is een overzicht weergegeven van de API's voor Zaakgericht werken. De Catalogi API en Zaken API zijn puur voor zaakgericht werken bedoeld, en hebben geen functie daarbuiten. De Documenten API en Besluiten API zullen ook buiten zaakgericht werken toepassingen krijgen. Immers, niet alle documenten zijn zaakgericht en niet alle besluiten zullen in de context van een zaak worden genomen. Denk bij het laatste bijv. aan raadsbesluiten.

Naast deze API zijn er nog een aantal API’s ontwikkeld ter ondersteuning, t.w. Notificaties API, Autorisatie API en de Referentielijsten API.

![overzicht API's](apis.png)
