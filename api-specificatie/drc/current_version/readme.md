Naar aanleiding van gesprekken die gevoerd zijn in Nieuwegein  en voortschrijdend inzicht heb ik het API-ontwerp voor het relateren van informatieobjecten aangepast, zie [redoc](https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/VNG-Realisatie/gemma-zaken/Documenten-relateren-aan-andere-relevante-documenten/api-specificatie/drc/current_version/openapi.yaml#tag/informatieobjectenrelaties/operation/informatieobjectrelatie_create). 

De naamgeving in deze nieuwe versie is consistent gemaakt met de naamgeving van het RGBZ waarin zaken aan elkaar gerelateerd kunnen worden met de relatie "heeft relevante andere".

![afbeelding](https://github.com/VNG-Realisatie/gemma-zaken/assets/37145898/b5fa783f-e61f-42a3-a7f1-a5ee9b4578dc)

Op dezelfde manier modelleren we de relatie "heeft relevante andere" tussen informatieobjecten:

![afbeelding](https://github.com/VNG-Realisatie/gemma-zaken/assets/37145898/87aa8534-97a6-49d0-b13d-aa8ca720876d)
De relatieklasse `INFORMATIEOBJECTENRELATIE` is vertaald naar het REST-endpoint `informatieobjectenrelaties` (in meervoud). 

In het volgende voorbeeld leggen we de relatie tussen de twee documenten `<doc1>` en `<doc2>` waarbij het laatstgenoemde document een publiceerbare versie is van de eerste.

`POST /informatieobjectenrelaties`

```json
{
  "informatieobject": "<doc1>",
  "relevantAnderInformatieobject": "<doc2>",
  "aardRelatie": "publiceerbaar"
}
```

Deze relatie wordt als conveniance ook zichtbaar gemaakt in de resource `/enkelvoudiginformatieobject`:

`GET /enkelvoudiginformatieobjecten/<<doc1>>`

```
{
  ...,
  "relevanteAndereInformatieobjecten": [
    {
      "informatieobject": "<doc2>",
      "aardRelatie": "publiceerbaar",
      "richtingRelatie": "standaard"
    }
  ],
}
```

`GET /enkelvoudiginformatieobjecten/<<doc2>>`

```
{
  ...,
  "relevanteAndereInformatieobjecten": [
    {
      "informatieobject": "<doc1>",
      "aardRelatie": "publiceerbaar",
      "richtingRelatie": "omgekeerd"
    }
  ],
}
```

Het attribuut "richtingRelatie" wordt gebruikt om de waarde van het attribuut "aardRelatie" in de goede richting te lezen.

In de aanvullende specificatie van de standaard leggen we vast dat  het attribuut `aardRelatie` aanvankelijk alleen de twee volgende waarden mag hebben. 

| Waarde attribuut 'aardRelatie'| Beschrijving |
| --- | ---|
| `publiceerbaar` | Het relevante andere informatieobject is een publiceerbare variant. |
| `ongespecificeerd` | De relatie met het relevante andere informatieobject is niet gespecificeerd. |

In de toekomst kan deze tabel eventueel worden uitgebreid met nieuwe waarden als daar behoefte aan is.
