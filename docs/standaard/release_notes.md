# Release Notes

## Zaken API (`zrc 1.5.1` -> `zrc 1.5.2`)

- **Geneste expand van catalogi objecten mogelijk gemaakt**

  Via de Zaken API kunnen de catalogi objecten (zaaktype, resultaattype, statustype, etc.) nu op geneste wijze geexpandeerd worden.


- **Oplossen fouten in OAS m.b.t. expand**  

  N.a.v. de volgende issues:

      - #2412: Wat is de bedoeling bij _expand bij anderzaakobject in ZRC 1.5?

      - #2414: ZRC 1.5 laat (onterecht) _expand zien op rol.

  In de resources rollen en zaakobjecten komt het attribuut _expand (onterecht) voor. Dit is verwarrend want dit attribuut kan alleen indirect gebruikt worden via de zaken resource. Dit attribuut is verwijderd daar waar het niet van toepassing is. Deze correctie heeft geen functionele gevolgen.

- **Referenties naar ztc vervangen door relatieve paden**  

  Hiervoor waren de referenties absolute paden wat niet handig is voor het uitrollen van een nieuwe release want dan moeten de paden handmatig worden aangepast.

## Catalogi API (`ztc 1.3.1` -> `ztc 1.3.2`)

- **Geneste expansion toegevoegd aan Catalogi API**  

  Geneste expansie objecten toegevoegd aan het schema van de OAS. De expand is niet toegevoegd aan de operaties van de Catalogi API  zelf maar de geneste expand kan (indirect) aangeroepen worden vanuit de Zaken API.

- **Aanscherping specificatie eigenschappen met datumvelden**  

  Regel `zt-015` toegevoegd aan de aanvullende specificatie naar aanleiding van het volgende issue:  

      - #1751: As a developer, I want to have standardized schema descriptions for eigenschappen.

- **Verheldering en aanscherping rule ztc-010**  

  Naar aanleiding van issue [#2456](https://github.com/VNG-Realisatie/gemma-zaken/issues/2456) (Business rule ztc-010 herschrijven).
  
## Documenten API (`drc 1.5.0` -> `drc 1.6.0`)

- **Geneste expand van catalogi objecten mogelijk gemaakt**

    In het bijzonder is het nu mogelijk om het attribuut  `informatieobjecttype` te kunnen expanden.

- **Expand toegevoegd aan ObjectInformatieObject**  
  
  Zie issue #2370 (met als sub-issues #1891 en #2434) waar de wens wordt geuit om in de Documenten API (DRC) de resource objectinformatiobjecten te kunnen expanden op het veld "informatieobject". 
  