---
title: "Gebruik testscenario's"
date: '31-05-2019'
weight: 60
---

De ZGW API standaard bestaat uit een OAS en documentatie met voornamelijk
gedragsregels van de provider implementatie. De provider implementatie van deze
gedragsregels worden getest middels test scenario's, geschreven in [Postman].

Deze test scenario's worden onderhouden door de [API-teams] van de
respectievelijke API's en o.a. gebruikt voor het [API testplatform] en
continuous integration (CI) platformen van [API beheer].

## Zelf aan de slag

Zorg dat de componenten de test data hebben ingeladen. Indien gebruik wordt
gemaakt van de Docker componenten, dan kan de test data ingeladen worden die
zich bevind in deze [Test scenario's] repository.

1. Download, installeer en start [Postman].

1. Navigeer naar **File** \> **Import...** en klik op de tab
   **Import From Link**:

   ![import_collection](./_assets/import_collection.png)

1. Voer onderstaande URL in en klik op **Import**:
   `https://raw.githubusercontent.com/VNG-Realisatie/gemma-postman-tests/master/ZGW_api_postman_tests.json`

1. Er verschijnt een nieuwe collectie: **ZGW api tests**.

1. Navigeer naar **Manage Environments** (rechts bovenin) \> **Import** \>
   **Choose file**

   ![import_environment](./_assets/import_environment.png)

1. Voer onderstaande URL in en klik op **Open**:
   `https://raw.githubusercontent.com/VNG-Realisatie/gemma-postman-tests/master/local.postman_environment.json`

1. Er verschijnt een nieuwe omgeving (environment): **ZGW api tests local**.

   Deze omgeving is afgestemd op lokaal draaiende Docker componenten. Open de
   omgevingsinstellingen door te klikken op de naam **ZGW api tests local** en
   pas aan waar nodig. Klik **Update** om de wijzigingen op te slaan.

1. Sluit het venster.

1. Hover over de collectie **ZGW api tests** en klik op de **Play** knop.

   ![import_environment](./_assets/start_runner.png)

   Of, klik bovenaan op **Runner** en navigeer naar de **ZGW api tests**
   collectie.

1. Navigeer in de **Collection Runner** binnen de **ZGW api tests** collectie
   naar **standaard.md** en eventueel verder naar een specifieke API.

1. Selecteer de omgeving **ZGW api tests local**.

1. Klik helemaal onderaan op de blauw knop **Run** om de test scenario's uit te
   voeren van de geselecteerde API(s) en de geselecteerde omgeving.

   ![import_environment](./_assets/run_collection.png)


[Test scenario's]: https://github.com/VNG-Realisatie/gemma-postman-tests
[Zaakgericht werken (ZGW) API's]: https://github.com/VNG-Realisatie/gemma-zaken
[API-teams]: https://github.com/VNG-Realisatie
[Postman]: https://www.getpostman.com/downloads/
[API testplatform]: https://github.com/VNG-Realisatie/api-testvoorziening
[API beheer]: https://github.com/VNG-Realisatie/api-beheer
