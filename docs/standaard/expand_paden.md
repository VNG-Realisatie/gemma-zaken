# Expand paden

Gebruik uiteindelijk een BNF_grammatica voor de pad_expressies. 
Maak ook een grammatica voor expand paden met willekeurige diepte.
Breid het uit met komma notatie voor meerdere paden tegelijk.

## GET /zaken?expand=XXX

### Diepte 1
```text
zaaktype
hoofdzaak
deelzaken
relevanteAndereZaken 
eigenschappen
rollen
status
zaakinformatieobjecten
zaakobjecten
resultaat
```

### Diepte 2
```text
hoofdzaak.<pad_diepte_1>
deelzaken.<pad_diepte_1>
relevanteAndereZaken.<pad_diepte_1>
eigenschappen.eigenschappen
rollen.roltype
rollen.statussen
status.statustype
status.gezetdoor
status.zaakinformatieobjecten
zaakinformatieobjecten.informatieobject
zaakinformatieobjecten.status
zaakobjecten.object??
zaakobjecten.zaakobjecttype
resultaat.resultaattypen
```



### Diepte 3

```text
hoofdzaak.<pad_diepte_2>
deelzaken.<pad_diepte_2>
relevanteAndereZaken.<pad_diepte_2>
rollen.statussen.statustype
rollen.statussen.gezetdoor
rollen.statussen.zaakinformatieobjecten
status.gezetdoor.roltype
status.zaakinformatieobjecten.informatieobject
status.zaakinformatieobjecten.status
zaakinformatieobjecten.informatieobject.informatieobjecttype?? (niet in Excel) Lost dit het probleem op van Tahir???
zaakinformatieobjecten.status.statustype
zaakinformatieobjecten.status.gezetdoor
zaakinformatieobjecten.status.statustype
zaakinformatieobjecten.status.zaakinformatieobjecten??
```

## BNF grammatica voor expand-paden

### Expand-paden voor Zaken API

Voor de volgende endpoints in de Zaken API definiëren we de expand-paden door middel van een BNF-grammatica.

- `GET /zaken?expand=<expand_pad_zaak>`
- `GET /zaken/{uuid}?expand=<expand_pad_zaak>`

```ebnf
<expand_pad_zaak> ::=
      <expand_pad_zaak_diepte_1>
    | <expand_pad_zaak_diepte_2>
    | <expand_pad_zaak_diepte_3>

<expand_pad_zaak_diepte_1> ::= 
      "zaaktype" 
    | "hoofdzaak" 
    | "deelzaken" 
    | "relevanteAndereZaken" 
    | "eigenschappen" 
    | "rollen" 
    | "status" 
    | "zaakinformatieobjecten" 
    | "zaakobjecten" 
    | "resultaat"

<expand_pad_zaak_diepte_2> ::=
      "hoofdzaak." <expand_pad_zaak_diepte_1> 
    | "deelzaken." <expand_pad_zaak_diepte_1>
    | "relevanteAndereZaken." <expand_pad_zaak_diepte_1>
    | "eigenschappen.eigenschappen"
    | "rollen.roltype"
    | "rollen.statussen"
    | "status.statustype"
    | "status.gezetdoor"
    | "status.zaakinformatieobjecten"
    | "zaakinformatieobjecten.informatieobject"
    | "zaakinformatieobjecten.status"
    | "zaakobjecten.object"
    | "zaakobjecten.zaakobjecttype"
    | "resultaat.resultaattypen"

<expand_pad_zaak_diepte_3> ::= 
      "hoofdzaak." <expand_pad_zaak_diepte_2>
    | "deelzaken." <expand_pad_zaak_diepte_2>
    | "relevanteAndereZaken." <expand_pad_zaak_diepte_2>
    | "rollen.statussen.statustype"
    | "rollen.statussen.gezetdoor"
    | "rollen.statussen.zaakinformatieobjecten"
    | "status.gezetdoor.roltype"
    | "status.zaakinformatieobjecten.informatieobject"
    | "status.zaakinformatieobjecten.status"
    | "zaakinformatieobjecten.informatieobject.informatieobjecttype"
    | "zaakinformatieobjecten.status.statustype"
    | "zaakinformatieobjecten.status.gezetdoor"
    | "zaakinformatieobjecten.status.statustype"
    | "zaakinformatieobjecten.status.zaakinformatieobjecten"
```

### Expand-paden voor Documenten API

Voor de volgende endpoints in de Documenten API definiëren we de expand-paden door middel van een BNF-grammatica.  

- `GET /enkelvoudiginformatieobjecten?expand=<expand_pad_enkelvoudiginformatieobject>`
- `GET /enkelvoudiginformatieobjecten/{uuid}?expand=<expand_pad_enkelvoudiginformatieobject>`
- `GET /gebruiksrechten?expand=<expand_pad_informatieobject>`
- `GET /gebruiksrechten/{uuid}?expand=<expand_pad_informatieobject>`  
- `GET /objectinformatieobjecten?expand=<expand_pad_informatieobject>`  
- `GET /objectinformatieobjecten/{uuid}?expand=<expand_pad_informatieobject>`  
- `GET /verzendingen?expand=<expand_pad_informatieobject>`  
- `GET /verzendingen/{uuid}?expand=<expand_pad_informatieobject>`  

```ebnf
<expand_pad_enkelvoudiginformatieobject> ::= 
    "informatieobjecttype"

<expand_pad_informatieobject> ::= 
    "informatieobject" ["." <expand_pad_enkelvoudiginformatieobjecten>]

```

Let op! De OAS van Documenten API 1.4.3 bevat de volgende fouten:

- Op het endpoint `/objectinformatieobjecten` is geen expand gedefiniëerd.
- Op de endpoints `/gebruiksrechten` en `/verzendingen` kun je niet genest expanden met het veld `informatieobjecttype`, althans deze geneste expand wordt niet beschreven in het respons-schema

# Volledige nesting

## Expand-paden voor ZGW API's

```ebnf
<zrc_zaak_expand_list> ::= 
      <zrc_zaak_expand> ("," <zrc_zaak_expand_list>)?

<zrc_zaak_expand> ::= 
      "zaaktype" ("." <ztc_zaaktype_expand>)?
    | "hoofdzaak" ("." <zrc_zaak_expand>)?
    | "deelzaken" ("." <zrc_zaak_expand>)?
    | "relevanteAndereZaken" ("." <zrc_zaak_expand>)?
    | "eigenschappen" ("." <zrc_zaakeigenschap_expand>)?
    | "rollen" ("." <zrc_rol_expand>)?
    | "status" ("." <zrc_status_expand>)?
    | "zaakinformatieobjecten" ("." <zrc_zaakinformatieobject_expand>)?
    | "zaakobjecten" ("." <zrc_zaakobject_expand>)?
    | "resultaat" ("." <zrc_resultaat_expand>)?

<zrc_zaakeigenschap_expand> ::=
      "zaak" ("." <zrc_zaak_expand>)?
    | "eigenschap" ("." <ztc_eigenschap_expand>)?

<zrc_rol_expand> ::=
      "zaak" ("." <zrc_zaak_expand>)?
    | "roltype" ("." <ztc_roltype_expand>)?
    | "statussen" ("." <zrc_status_expand>)?

<zrc_status_expand> ::=
      "zaak" ("." <zrc_zaak_expand>)?
    | "statustype" ("." <ztc_statustype_expand>)?
    | "gezetdoor" ("." <zrc_rol_expand>)?   
    | "zaakinformatieobjecten" ("." <zrc_zaakinformatieobject_expand>)?

<zrc_zaakinformatieobject_expand> ::=
      "informatieobject" ("." <drc_enkelvoudiginformatieobject_expand>)?
    | "zaak" ("." <zrc_zaak_expand>)?
    | "status" ("." <zrc_status_expand>)?

<zrc_zaakobject_expand> ::=
      "zaak" ("." <zrc_zaak_expand>)?
    | "object"
    | "zaakobjecttype" ("." <ztc_zaakobjecttype_expand>)?

<zrc_resultaat_expand> ::=
      "zaak" ("." <zrc_zaak_expand>)?
    | "resultaattype" ("." <ztc_resultaattype_expand>)?

<ztc_zaaktype_expand> ::=
      "zaakobjecttypen" ("." <ztc_zaakobjecttype_expand>)? 
    | "catalogus" ("." <ztc_catalogus_expand>)?
    | "statustypen" ("." <ztc_statustype_expand>)?
    | "resultaattypen" ("." <ztc_resultaattype_expand>)?
    | "eigenschappen" ("." <ztc_eigenschap_expand>)?
    | "informatieobjecttypen" ("." <ztc_informatieobjecttype_expand>)?
    | "roltypen" ("." <ztc_roltype_expand>)?
    | "besluittypen" ("." <ztc_besluittype_expand>)?
    | "deelzaaktypen" ("." <ztc_zaaktype_expand>)?
    | "gerelateerdeZaaktypen" ("." <ztc_zaaktype_expand>)?

<ztc_eigenschap_expand> ::=
      "catalogus" ("." <ztc_catalogus_expand>)?
    | "zaaktype" ("." <ztc_zaaktype_expand>)?
    | "statustype" ("." <ztc_statustype_expand>)?

<ztc_zaakobjecttype_expand> ::=
      "objecttype"
    | "zaaktype" ("." <ztc_zaaktype_expand>)?
    | "resultaattypen" ("." <ztc_resultaattype_expand>)?
    | "statustypen" ("." <ztc_statustype_expand>)?
    | "catalogus" ("." <ztc_catalogus_expand>)?

<ztc_catalogus_expand> ::=
      "zaaktypen" ("." <ztc_zaaktype_expand>)?
    | "besluittypen" ("." <ztc_besluittype_expand>)?
    | "informatieobjecttypen" ("." <ztc_informatieobjecttype_expand>)?

<ztc_statustype_expand> ::=
      "zaaktype" ("." <ztc_zaaktype_expand>)?
    | "catalogus" ("." <ztc_catalogus_expand>)?
    | "informatieobjecttypen" ("." <ztc_informatieobjecttype_expand>)?

<ztc_resultaattype_expand> ::=
      "zaaktype" ("." <ztc_zaaktype_expand>)?
    | "resultaattypeomschrijving"
    | "selectielijstklasse"
    | "catalogus" ("." <ztc_catalogus_expand>)?
    | "besluittypen" ("." <ztc_besluittype_expand>)?
    | "informatieobjecttypen" ("." <ztc_informatieobjecttype_expand>)?

<ztc_informatieobjecttype_expand> ::=
      "catalogus" ("." <ztc_catalogus_expand>)?
    | "zaaktypen" ("." <ztc_zaaktype_expand>)?
    | "besluittypen" ("." <ztc_besluittype_expand>)?

<ztc_roltype_expand> ::=
      "zaaktype" ("." <ztc_zaaktype_expand>)?
    | "catalogus" ("." <ztc_catalogus_expand>)?

<ztc_besluittype_expand> ::=
      "catalogus" ("." <ztc_catalogus_expand>)?
    | "zaaktypen" ("." <ztc_zaaktype_expand>)?
    | "informatieobjecttypen" ("." <ztc_informatieobjecttype_expand>)?
    | "resultaattypen" ("." <ztc_resultaattype_expand>)?

<drc_enkelvoudiginformatieobject_expand> ::=
      "link"
    | "informatieobjecttype" ("." <ztc_informatieobjecttype_expand>)?
    | "bestanddelen"

<drc_gebruiksrechten_expand> ::=
    "informatieobject" ("." <drc_enkelvoudiginformatieobject_expand>)?

<drc_objectinformatieobjecten_expand> ::=
      "informatieobject" ("." <drc_enkelvoudiginformatieobject_expand>)?
    | "zaaktypen" ("." <ztc_zaaktype_expand>)?
    | "object" ( "." ( <zrc_zaak_expand> | <brc_besluit_expand> ) )?

<drc_verzendingen_expand> ::=
      "betrokkene" ("." <zrc_rol_expand>)?
    | "informatieobject" ("." <drc_enkelvoudiginformatieobject_expand>)?
    | "contactPersoon" ("." <zrc_rol_expand>)?

<brc_besluit_expand> ::= 
      "besluittype" ("." <ztc_besluittype_expand>)?
```

Opmerkingen:

```ebnf
<zaakobject> ::=
      "zaak" ("." <zaak>)?
    | "object" (* externe expand, nu nog niet in standaard? *)
    | "zaakobjecttype" ("." <zaakobjecttype>)?

<resultaat> ::=
      "zaak" ("." <zaak>)?
    | "object" (* externe expand *)
    | "resultaattype" ("." <resultaattype>)?

<zaakobjecttype> ::=
      "objecttype" (* externe expand, nu nog niet in scope*)
    | "zaaktype" ("." <zaaktype>)?
    | "resultaattypen" ("." <resultaattype>)?
    | "statustypen" ("." <statustype>)?
    | "catalogus" ("." <catalogus>)?

<zaakinformatieobject> ::=
      "informatieobject" ("." <enkelvoudiginformatieobject>)? (* Nu nog niet in scope, maar waarom? Staat niet in Excel en ook niet in OAS*)
    | "zaak" ("." <zaak>)?
    | "status" ("." <status>)?

<resultaattype> ::=
      "zaaktype" ("." <zaaktype>)?
    | "resultaattypeomschrijving" (* externe expand naar referentielijst, nu nog niet in scope *)
    | "selectielijstklasse" (* externe expand naar referentielijst, nu nog niet in scope *)
    | "catalogus" ("." <catalogus>)?
    | "besluittypen" ("." <besluittype>)?
    | "informatieobjecttypen" ("." <informatieobjecttype>)?

```


# To do

- Naast de punt-notatie ook de de grammatica uitschrijven voor komma-notatie (expand=zaaktype,status.statustype)
- alle non-terminals voorzien van een prefix: zrc, ztc, brc, drc,  ...
- Volledige recursie uitwerken!!!! (LeUK)
- Installeer een VSC extensie voor BNF highlightning
- https://bnfparser.firebaseapp.com/ voor speciale BNF syntax en sandbox
- https://bnfplayground.pauliankline.com/
- Genereer een plaatje van de grammatica
- zou gaaf zijn als de bnf klikbaar is zodat je van de ene non-terminal naar de andere kunt springen. Misschien is het gegenereerde plaatje klikbaar?
- Productie-regels bnf opdelen per api, misschien ook naamgeving aanpassen, bijv <ztc_eigenschappen>, <zrc_zaak>
- Genereer een Python programma die alle onnodige recursiepaden signaleert, 
  - bijv. `catalogus.zaaktypen.catalogus`. 
  - Wat is het langste zinvolle pad zonder recursie. (bijv. `zaakinformatieobjecten.zaak.resultaat.resultaattype.informatieobjecttypen.zaaktypen.catalogus.zaaktypen.catalogus`)
  - Kun je een editor maken met intellisense voor de paden: na het intikken van de punt krijg je een lijstje met mogelijke geneste expands.
  - alle paden genereert zonder recursie
  - verdiepingssessie expand
- Comments moeten geannoteerd worden buiten de tekst
- Gebruik yacc en Python om zelf een parser te genereren met comments.
- Maar daar een API van en een ook een docker.
- In het voorbeeld met diepte 3 grammatica moet de "." losgetrokken worden























