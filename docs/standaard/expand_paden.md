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

## Expand-paden voor Zaken API

```ebnf
<zaak> ::= 
      "zaaktype" ("." <zaaktype>)?
    | "hoofdzaak" 
    | "deelzaken" 
    | "relevanteAndereZaken" 
    | "eigenschappen" 
    | "rollen" 
    | "status" 
    | "zaakinformatieobjecten" 
    | "zaakobjecten" 
    | "resultaat" ;

<zaaktype> ::=
      "zaakobjecttypen" ("." <zaakobjecttypen>)?
    | "catalogus" ("." <catalogus>)?



```


# To do

- Vraagtekens ?? gevallen beschrijven in NB of "Let op" sectie.
- Naast de punt-notatie ook de de grammatica uitschrijven voor komma-notatie (expand=zaaktype,status.statustype)
- Volledige recursie uitwerken!!!! (LeUK)























