# Release Notes Zaken API 1.6.0

To do:

- [#2398](https://github.com/VNG-Realisatie/gemma-zaken/issues/2398): Expand: moeten alle geledingen van de expandparameter worden geexpandeerd of alleen de laatste?

- Uitleggen OneOf-constructie expand.

- Issues voorzien van hyperlinks en soms vooraan zetten


## Expand-mechanisme

### Expand beschikbaar voor alle relevante endpoints

Voorheen kon de expand alleen maar gebruikt worden op het endpoint `/zaken`, maar nu kan de expand ook worden toegepast op de andere resources (rollen, statussen, zaakinformatieobjecten, etc.). Dit is consistenter, gebruikersvriendelijker en biedt in sommige gevallen meer functionaliteit.

Gerelateerde issues:

- #2524: Binnen de Zaken API wil ik dat het expand-mechanisme niet alleen op zaken maar op alle resources kan worden toegepast.

- #2443: Ontbrekende functionaliteiten met expand voor veel gebruikte informatiebehoeften.


###  Expand tot willekeurige diepte

Voorheen mocht de expand maar tot drie niveau's diep worden genest. In deze versie kan de expand tot willekeurige diepte worden uitgevoerd.

Gerelateerde issues:

- #2502. Bestaat er een expand voor de ZRC voor expand=zaaktype,zaaktype.informatieobjecttypen?

- #2507. Ik wil graag dat de Expand overal wordt toegepast en niet alleen voor de ZRC.

- #2397. Expand: welke moeten precies ondersteund worden?


### Cross-over expand naar Documenten API en Besluiten API

Voorheen was de expand naar de Catalogi API de enige cross-over expand die werd ondersteund. Nu is de expand uitgebreid naar de Documenten API en de Besluiten API.

Gerelateerde issues:

- #2507. Ik wil graag dat de Expand overal wordt toegast en niet alleen voor de ZRC.

- #2443: Ontbrekende functionaliteiten met expand voor veel gebruikte informatiebehoeften.

### Functionaliteit om de omvang van responses te reduceren

Expand kan leiden tot extreem grote responses. Om dit probleem het hoofd te bieden is het "fields"-element toegevoegd aan het endpoint `POST /zaken/_zoek`. Daarmee kun je zowel de velden specificeren die je wilt expanden als ook de velden die je (in een expand) terug wilt krijgen zodat de respons niet te groot wordt. Deze oplossing is geinspireerd door de manier waarop GraphQL met expands omgaat. 

Gerelateerde issues:

- #2559. ZRC: reduce expand results.

### Diverse bugs fixes

- Expansion bij zaken mist het attribuut zaakinformatieobjecten in de OAS #2515

- ZRC 1.5 laat (onterecht) _expand zien op rol #2414

- Wat is de bedoeling bij _expand bij anderzaakobject in ZRC 1.5? #2412

## Allerhande bug fixes

- Typefout in enum innRechtsvorm #2581

- objectIdentificatie zaakobject huishouden en terrein_gebouwd_object bevat een foutief element #2576

- Als gemeente wil ik een UUID kunnen gebruiken als betrokkeneIdentificatie.identificatie bij een betrokkeneType medewerker in de zaken API #2290









