# Release Notes

## Zaken API (`zrc 1.5.2`)

- **Oplossen fouten in OAS m.b.t. expand**  

  N.a.v. de volgende issues:

      - #2412: Wat is de bedoeling bij _expand bij anderzaakobject in ZRC 1.5?

      - #2414: ZRC 1.5 laat (onterecht) _expand zien op rol.

  In de resources rollen en zaakobjecten komt het attribuut _expand (onterecht) voor. Dit is verwarrend want dit attribuut kan alleen indirect gebruikt worden via de zaken resource. Dit attribuut is verwijderd daar waar het niet van toepassing is. Deze correctie heeft geen functionele gevolgen.

- **Geneste expansion naar ztc expliciet zichtbaar gemaakt in de OAS**  

  Hiervoor was het geneste expansie-mechanisme textueel beschreven maar niet formeel gemodelleerd in de OAS.

## Catalogi API (`ztc 1.3.2`)

- **Geneste expansion toegevoegd aan Catalogi API**  

  Zie ook Zaken API.

- **Aanscherping specificatie eigenschappen met datumvelden**  

  Regel `zt-015` toegevoegd aan de aanvullende specificatie naar aanleiding van het volgende issue:  

      - #1751: As a developer, I want to have standardized schema descriptions for eigenschappen.

- **Verheldering en aanscherping rule ztc-010**  

  Naar aanleiding van issue [#2456](https://github.com/VNG-Realisatie/gemma-zaken/issues/2456) (Business rule ztc-010 herschrijven).
  
## Documenten API (`drc 1.6.0`)

- **Expand toegevoegd aan ObjectInformatieObject**  
  
  Zie issues #1891 en #2370 waar de wens wordt geuit om in de Documenten API (DRC) de resource objectinformatiobjecten te kunnen expanden op het veld "informatieobject".  
  