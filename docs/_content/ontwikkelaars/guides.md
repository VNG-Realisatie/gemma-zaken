---
title: ZGW API guides
weight: 90
---

*WIP*

In onderstaande voorbeelden wordt gebruik gemaakt van de door VNG gehoste
referentie implementaties van de verschillende componenten.


## Catalogussen ophalen

Het ZTC bevat één of meer catalogussen:

```bash
$ curl https://ref.tst.vng.cloud/ztc/api/v1/catalogussen
[]  
```

## Zaaktypen ophalen

```bash
curl https://ref.tst.vng.cloud/ztc/api/v1/catalogussen/zaaktypen/  
```

## Zaak aanmaken

```bash
$ cat >zaak_aanmaken.json <<EOL
{
  "zaaktype": "foo"
}
EOL

$ curl -H "Content-Type: application/json" --data @zaak_aanmaken.json
```

## Document toevoegen

## Zaak aan een Document koppelen

## Zaak status wijzigen

## Besluit nemen in Zaak

TODO

## Authenticeren

TODO
