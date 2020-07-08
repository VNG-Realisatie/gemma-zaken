# Specificatie van gedrag

De Contactmomenten API MOET aan twee aspecten voldoen:

* de OAS-specificatie `openapi.yaml` MOET volledig geïmplementeerd zijn.

* het run-time gedrag hieronder beschreven MOET correct geïmplementeerd
  zijn.


## Run-time gedrag

Bepaalde gedrageningen kunnen niet in een OAS spec uitgedrukt worden omdat ze
businesslogica bevatten. Deze gedragingen zijn hieronder beschreven en MOETEN
zoals beschreven geïmplementeerd worden.

### **<a name="cm-001">Valideren attribuut `vorigContactmoment` bij aanmaken of bijwerken van een CONTACTMOMENT ([cm-001](#cm-001))</a>**

Bij het aanmaken (`contactmoment_create`) en bijwerken (`contactmoment_update` en
`contactmoment_partial_update`) van een CONTACTMOMENT MOET de URL-referentie
naar het vorige CONTACTMOMENT gevalideerd worden op het bestaan indien deze is meegegeven en niet leeg is. Als het ophalen van de objecten niet (uiteindelijk) resulteert in een `HTTP 200` status code, MOET er geantwoord worden met een `HTTP 400` foutbericht. 

### **<a name="cm-002">Automatisch zetten van het attribuut `volgendContactmoment`in het vorige CONTACTMOMENT ([cm-002](#cm-002))</a>**

Bij het aanmaken (`contactmoment_create`) en bijwerken (`contactmoment_update` en
`contactmoment_partial_update`) van een CONTACTMOMENT MOET op basis van het veld `vorigContactmoment`, indien dit attribuut is meegegeven en niet leeg is, het veld `volgendContactmoment` van het vorige CONTACTMOMENT worden bewerkt zodat er een kruisverwijzing ontstaat.

### **<a name="cm-003">Valideren attribuut `medewerker` bij aanmaken of bijwerken van een CONTACTMOMENT ([cm-003](#cm-003))</a>**

Bij het aanmaken (`contactmoment_create`) en bijwerken (`contactmoment_update` en
`contactmoment_partial_update`) van een CONTACTMOMENT MOET de URL-referentie
naar de MEDEWERKER gevalideerd worden op het bestaan indien deze is meegegeven en niet leeg is. Als het ophalen van de objecten niet (uiteindelijk) resulteert in een `HTTP 200` status code, MOET er geantwoord worden met een `HTTP 400` foutbericht. 

### **<a name="cm-004">Valideren attributen `contactmoment`, `klant` en `rol` bij aanmaken van een KLANT-CONTACTMOMENT relatie ([cm-004](#cm-004))</a>**

Bij het aanmaken van een KLANT-CONTACTMOMENT-relatie (`klantcontactmoment_create`) MOETEN de URL-referenties
naar KLANT en CONTACTMOMENT gevalideerd worden op het bestaan. Indien het ophalen van de objecten niet (uiteindelijk) resulteert in een `HTTP 200` status code, MOET er geantwoord worden met een `HTTP 400` foutbericht. Bovendien MOET de combinatie `contactmoment`, `klant` en `rol` uniek zijn. Als dit niet het geval is, MOET er geantwoord worden met een `HTTP 400` foutbericht.

### **<a name="cm-005">Valideren attributen `contactmoment` en `object` bij aanmaken van een OBJECT-CONTACTMOMENT relatie ([cm-005](#cm-005))</a>**

Bij het aanmaken van een KLANT-CONTACTMOMENT-relatie (`objectcontactmoment_create`) MOETEN de URL-referenties
naar OBJECT en CONTACTMOMENT gevalideerd worden op het bestaan. Indien het ophalen van de objecten niet (uiteindelijk) resulteert in een `HTTP 200` status code, MOET er geantwoord worden met een `HTTP 400` foutbericht. Bovendien MOET de combinatie `object` en `contactmoment` uniek zijn. Als dit niet het geval is, MOET er geantwoord worden met een `HTTP 400` foutbericht.

### **<a name="cm-006">Valideren bestaan relatie tussen OBJECT en CONTACTMOMENT in de bron ([cm-006](#cm-006))</a>**

Bij het aanmaken van een relatie tussen OBJECT en CONTACTMOMENT (`objectcontactmoment_create`) MOET gevalideerd worden dat de relatie tussen het OBJECT en het CONTACTMOMENT al bestaat in de bron van het OBJECT. De bron van het OBJECT is bekend door de eerdere validaties op deze URL. 


### HTTP-Caching

De Contactmomenten API moet HTTP-Caching ondersteunen op basis van de `ETag` header. In
de API spec staat beschreven voor welke resources dit van toepassing is.

De `ETag` MOET worden berekend op de JSON-weergave van de resource.
Verschillende, maar equivalente weergaves (bijvoorbeeld dezelfde API ontsloten
wel/niet via NLX) MOETEN verschillende waarden voor de `ETag` hebben.

Indien de consumer een `HEAD` verzoek uitvoert op deze resources, dan MOET de
provider antwoorden met dezelfde headers als bij een normale `GET`, dus
inclusief de `ETag` header. Er MAG GEEN response body voorkomen.

Indien de consumer gebruik maakt van de `If-None-Match` header, met één of
meerdere waarden voor de `ETag`, dan MOET de provider antwoorden met een
`HTTP 304` bericht indien de huidige `ETag` waarde van de resource hierin
voorkomt. Als de huidige `ETag` waarde hier niet in voorkomt, dan MOET de
provider een normale `HTTP 200` response sturen.