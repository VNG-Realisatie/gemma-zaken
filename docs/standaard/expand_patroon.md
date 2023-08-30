---
title: Performance verbeteringen API's voor Zaakgericht werken
date: '29-08-2023'
weight: 10
layout: page-with-side-nav
---
# Performance verbeteringen API's voor Zaakgericht werken

## Inleiding
Bij het gebruik van de API's voor Zaakgericht werken is gebleken dat door de opzet van de API's een goede performance lastig te realiseren is. Bovendien wordt veel van de consumer applicatie gevraagd om de noodzakelijke gegevens op te kunnen halen. Een aantal van deze tekortkomingen is fundamenteler van aard en hiervoor wordt dan ook een oplossing uitgewerkt die als API Referentie Architectuur  gebruikt zal gaan worden bij de VNG API standaarden. Op de korte termijn zijn echter ook oplossingen voor de API's voor Zaakgericht werken nodig. 


Het verbeteren van de performance van de API's voor Zaakgericht werken gebeurt op twee onderdelen, te weten:
1. Opnemen van gerelateerde informatie in het antwoord. Hiermee kan het aantal te stellen vragen drastisch worden beperkt.
2. Bieden van betere filtermogelijkheden zodat de consumer makkelijker een specifiek antwoord op kan halen en niet zelf een veel te grote dataset hoeft uit te filteren. 

De filtermogelijkheden zullen worden opgenomen in de betreffende Open API Specificaties (OAS). Deze kunnen geraadpleegd worden via de documentatie website https://vng-realisatie.github.io/gemma-zaken/standaard/

Het opnemen van gerelateerde informatie vereist meer achtergrondinformatie en dit wordt in deze bijlage beschreven. 

##Uitgangspunten korte termijn verbetering API's voor Zaakgericht werken
Om te voorkomen dat in de korte termijn oplossing beslissingen genomen worden die in de toekomst voor problemen kunnen gaan zorgen gelden onderstaande uitgangspunten.

### Niet tornen aan fundament bestaande standaarden:
- Aanpassingen zoveel mogelijk laten passen binnen de bestaande structuren
- Dit betekent dat we nu niet kijken naar schrijfoperaties.
- Handhaven CRUD karakter
- Grootste problemen nu met Zaken APPI en Documenten API, deze lossen we als eerste op
- Handhaven grenzen tussen bestaande API standaarden (Zaken, Documenten, Besluiten) behalve de Catalogi API.

### Wél optimaliseren van het bevragen van de Zaken API en Documenten API
- In één keer bevragen van resources in de Zaken/Documenten en Catalogi API’s naar aanleiding van inventarisatie samen te voegen calls
- Inventariseren van gewenste filtermogelijkheden op kenmerken die in het zaken/documenten/besluitenregister beschikbaar zijn


## Rationale keuze voor expand patroon
Het opnemen van gerelateerde informatie via een expand patroon, is op het moment van schrijven (nog) niet opgenomen in de [Landelijke API Strategie](https://docs.geostandaarden.nl/api/API-Strategie/). Dit betekent dat er nog geen keuze is gemaakt in een syntax om dit te bereiken. Om de gevolgen zo minimaal te laten zijn bij een keuze in de Landelijke API Strategie is het van belang dat het gekozen expand patroon voor consumers optioneel is binnen de standaard. Dat wil zeggen dat voor consumers het niet verplicht is het expand patroon toe te passen en de huidige manier van werken toepasbaar blijft. Providers dienen het expand mechanisme uiteraard in te bouwen.

Er zijn verschillende mogelijkheden voor het implementeren van een expand patroon. Elke mogelijkheid heeft eigen voor- en nadelen. Tijdens sessies van de Technische Gebruikersgroep van de API's voor Zaakgericht werken zijn zowel het HAL patroon als het Inclusions patroon uitgebreid gepresenteerd en besproken. Ook is deze vergelijking intern bij VNG Realisatie gedaan. Inhoudelijk gezien kan met beide patronen het aantal calls verminderd worden. Uiteindelijk is gekozen voor een derde variant, nl. expand parameter met inline expand. Net als bij het Inclusions patroon is de structuur van de gegevens in expand gelijk aan die van de resources. Het voordeel is echter dat net als bij HAL de geëxpandeerde gegevens op de plek staan waar ze uitgevraagd zijn. Weliswaar kan dit leiden tot grotere berichten maar dit weegt in onze ogen niet op tegen de eenvoud voor de consumer die de informatie daar krijgt waar deze nodig is.

Hoewel de vergelijking tussen Inclusions en HAL+JSON VNG uitgesproken heeft te willen kiezen voor HAL+JSON is dit geen zuivere vergelijking geweest. Het belangrijkste is dat in de HAL+JSON variant noodzakelijk was een ander contenttype te kiezen. Weliswaar kan de consumer hiermee sturen in welk formaat de response gestuurd moet worden maar die keuze gaat over vorm, niet over inhoud. Een keuze voor een ander contenttype betekent dat *dezelfde informatie* op een andere manier weergegeven wordt. Dit besef heeft er toe geleid dat in Zaken API versie 1.5.0 en Documenten API 1.4.0 het expand patroon uitgewerkt is in het reeds gebruikte plain JSON formaat. De noodzaak tot HAL+JSON of een ander contenttype kwam hiermee te vervallen en dit heeft geleid tot het terugtrekken van Zaken API versie 1.2.1. 

## Grenzen aan het expand patroon
Zoals eerder genoemd in de uitgangspunten gelden de volgende grenzen aan het expand patroon:
- Er mogen alleen resources uit de eigen registratie opgenomen worden in de expand. Voor Zaken zijn dit de resources die in de Zaken API specificatie beschikbaar zijn, voor Documenten/Informatieobjecten de resources uit de Documenten API specificatie en voor Besluiten die uit de Besluiten API. Daarnaast mogen de relevante typen uit de Catalogi API opgehaald worden.
- Verwijzingen naar bijvoorbeeld de BRP of andere registraties worden niet opgevolgd. Die dienen door de consumer zelf opgehaald te worden.
- Ook verwijzingen vanuit de Zaken API naar bijvoorbeeld Documenten API of Besluiten API mogen niet meegenomen worden in het expand patroon. 

Het is niet mogelijk om bijvoorbeeld bij een ROL de gegevens van de BETROKKENE op te halen via de rol.betrokkene. De BETROKKENE is immers opgeslagen buiten Zaken API en Catalogi API.

## Uitwerking
Op basis van de grenzen zijn de volgende versies van de API's voor Zaakgericht werken uitgewerkt met expand:

Zaken API
* API specificatie (OAS3) versie 1.5.0 in
  - [ReDoc](./zaken/redoc-1.5.0),
  - [Swagger](./zaken/swagger-ui-1.5.0),

Documenten API
* API specificatie (OAS3) versie 1.4.0 in
  - [ReDoc](./documenten/redoc-1.4.0),
  - [Swagger](./documenten/swagger-ui-1.4.0),



