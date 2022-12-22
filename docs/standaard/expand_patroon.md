# Performance verbeteringen API's voor Zaakgericht werken

## Inleiding
Bij het gebruik van de API's voor Zaakgericht werken is gebleken dat door de opzet van de API's een goede performance lastig te realiseren is. Bovendien wordt veel van de consumer applicatie gevraagd om de noodzakelijke gegevens op te kunnen halen. Een aantal van deze tekortkomingen is fundamenteler van aard en hiervoor wordt dan ook een oplossing uitgewerkt die als API Referentie Architectuur  gebruikt zal gaan worden bij de VNG API standaarden. Op de korte termijn zijn echter ook oplossingen voor de API's voor Zaakgericht werken nodig. 


Het verbeteren van de performance van de API's voor Zaakgericht werken gebeurt op twee onderdelen, te weten:
1. Opnemen van gerelateerde informatie in het antwoord. Hiermee kan het aantal te stellen vragen drastisch worden beperkt.
2. Bieden van betere filtermogelijkheden zodat de consumer makkelijker een specifiek antwoord op kan halen en niet zelf een veel te grote dataset hoeft uit te filteren. 

De filtermogelijkheden zullen worden opgenomen in de betreffende Open API Specificaties (OAS). Deze kunnen geraadpleegd worden via de documentatie website https://vng-realisatie.github.io/gemma-zaken/standaard/

Het opnemen van gerelateerde informatie wordt in deze bijlage beschreven. 

##Uitgangspunten korte termijn verbetering API's voor Zaakgericht werken
Om te voorkomen dat in de korte termijn oplossing beslissingen genomen worden die in de toekomst voor problemen kunnen gaan zorgen gelden onderstaande uitgangspunten.

### Niet tornen aan fundament bestaande standaarden:
- Aanpassingen zoveel mogelijk beperken zodat oplossing relatief eenvoudig te implementeren en eventueel te verwijderen(!) is.
- Dit betekent dat we nu niet kijken naar schrijfoperaties.
- Handhaven CRUD karakter
- Handhaven grenzen tussen bestaande API standaarden (Zaken, Documenten, Besluiten) behalve de Catalogi API.

### Wél optimaliseren van het bevragen van de Zaken API
- In één keer bevragen van resources in de Zaken/Documenten/Besluiten en Catalogi API’s naar aanleiding van inventarisatie samen te voegen calls
- Inventariseren van gewenste filtermogelijkheden op kenmerken die in het zaken/documenten/besluitenregister beschikbaar zijn



## Status van deze bijlage en rationale keuze voor expand patroon
Het opnemen van gerelateerde informatie via een expand patroon, is op het moment van schrijven (nog) niet opgenomen in de [Landelijke API Strategie](https://docs.geostandaarden.nl/api/API-Strategie/). Dit betekent dat er nog geen keuze is gemaakt in een syntax om dit te bereiken. Om de gevolgen zo minimaal te laten zijn bij een keuze in de Landelijke API Strategie is het van belang dat het gekozen expand patroon optioneel is binnen de standaard. Dat wil zeggen dat het niet verplicht is het expand patroon toe te passen en de huidige manier van werken toepasbaar blijft.

Er zijn verschillende mogelijkheden voor het implementeren van een expand patroon. Elke mogelijkheid heeft eigen voor- en nadelen. Tijdens sessies van de Technische Gebruikersgroep van de API's voor Zaakgericht werken zijn zowel het HAL patroon als het Inclusions patroon uitgebreid gepresenteerd en besproken. Ook is deze vergelijking intern bij VNG Realisatie gedaan. Inhoudelijk gezien kan met  beide patronen het aantal calls verminderd worden.

Het Inclusions patroon is geen standaard maar een patroon afkomstig uit de Python wereld. Dit maakt dat er weinig informatie te vinden is buiten deze [beschrijving](https://github.com/VNG-Realisatie/gemma-zaken/discussions/1960). 

Voor HAL spreekt dat het weliswaar geen standaard is maar wel een Draft. Er is dus informatie te vinden over hoe met HAL om te gaan en er bestaan bibliotheken die het werken met HAL kunnen vergemakkelijken. De keerzijde is dat het correct gebruik van HAL veranderingen in de OAS met zich meebrengt. Echter, in de OAS wordt HAL een extra mogelijkheid om het antwoord op een request te structureren. Bestaande consumer implementaties kunnen de bestaande operaties en structuren blijven gebruiken. Wie behoefte heeft aan informatierijkere antwoorden kan er voor kiezen de uitgebreide HAL responses te vragen. Om die reden is er voor gekozen om het expand patroon met HAL op te nemen in de API's voor Zaakgerichtwerken standaard.


## Grenzen aan het expand patroon
Zoals eerder genoemd in de uitgangspunten gelden de volgende grenzen aan het expand patroon:
- Er mogen alleen resources uit de eigen registratie opgenomen worden in de expand. Voor Zaken zijn dit de resources die in de Zaken API specificatie beschikbaar zijn, voor Documenten/Informatieobjecten de resources uit de Documenten API specificatie en voor Besluiten die uit de Besluiten API. Daarnaast mogen de relevante typen uit de Catalogi API opgehaald worden.
- Verwijzingen naar bijvoorbeeld de BRP of andere registraties worden niet opgevolgd. Die dienen door de consumer zelf opgehaald te worden.
- Ook verwijzingen vanuit de Zaken API naar bijvoorbeeld Documenten API of Besluiten API mogen niet meegenomen worden in het expand patroon. 

Het is niet mogelijk om bijvoorbeeld bij een ROL de gegevens van de BETROKKENE op te halen via de rol.betrokkene. De BETROKKENE is immers opgeslagen buiten Zaken API en Catalogi API.

## Uitwerking
Op basis van de grenzen zijn de volgende versies van de API's voor Zaakgericht werken uitgewerkt met HAL:

Zaken API
* API specificatie (OAS3) versie 1.2.1 in
  [ReDoc][documenten-1.2.1-redoc],
  [Swagger][documenten-1.2.1-swagger],

Documenten API
* API specificatie (OAS3) versie 1.1.1 in
  [ReDoc][documenten-1.1.1-redoc],
  [Swagger][documenten-1.1.1-swagger],



