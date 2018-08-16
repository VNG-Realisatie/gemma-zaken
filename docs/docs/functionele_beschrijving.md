
#Functionele Documentatie ZAPI ZaakRegistratieComponent (ZRC)

## Inhoud
* [Introductie](#introductie)
* [maakZaakAan](#maakZaakAan)

## Introductie

In dit document wordt de [API](https://github.com/VNG-Realisatie/gemma-zaken/blob/master/api-specificatie/zrc/openapi.yaml) voor de [ZaakRegistratieComponent] (https://www.gemmaonline.nl/index.php/GEMMA2/0.9/id-a97b6545-d5a7-485d-9b13-3ce22db5b9cf) functioneel beschreven.

## maakZaakAan
Met de maakZaakAan service kan in het Zaakregistratiecomponent een lopende zaak toegevoegd worden. Een zaak heeft altijd een geldige zaakidentificatie die uniek is in combinatie met de bronorganisatie die de zaak heeft aangemaakt.

Wanneer geen geldige zaakidentificatie in het bericht aanwezig is wordt deze door de zaakregistratie component zelf aangemaakt. De zaakidentificatie wordt altijd in het antwoordbericht teruggegeven, ongeacht of deze meegegeven is in het maakZaakAan bericht of door de ZRC zelf aangemaakt is.
