# Expand paden

Gebruik uiteindelijk een BNF-grammatica voor de pad-expressies. 
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
hoofdzaak.<pad-diepte-1>
deelzaken.<pad-diepte-1>
relevanteAndereZaken.<pad-diepte-1>
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
hoofdzaak.<pad-diepte-2>
deelzaken.<pad-diepte-2>
relevanteAndereZaken.<pad-diepte-2>
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

## BNF grammatica voor expand paden tot diepte 3

# Pad-expressies voor het expanderen van zaken

```ebnf
<expand-zaak> ::= 
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

<expand-zaak-diepte-2> ::=
      "hoofdzaak." <expand-zaak> 
    | "deelzaken." <expand-zaak>
    | "relevanteAndereZaken." <expand-zaak>
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

<expand-zaak-diepte-3> ::= 
      "hoofdzaak." <expand-zaak-diepte-2>
    | "deelzaken." <expand-zaak-diepte-2>
    | "relevanteAndereZaken." <expand-zaak-diepte-2>
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























