# Design guidelines

### Optionele en niet-optionele velden

**Impliciet datamodel**

- we gaan uit van `waarden` en `optionele waarden`
- een `waarde` kan niet `null` zijn
- een `optionele waarde` kan `null` zijn (mbv `nullable: true`)

**Voor `application/json` payloads** (voor GET, POST, PUT)

- non-presence van een `waarde`: error (mbv opnemen in `required` array)
- expliciete `null` van een `waarde`: error
- non-presence van een `optionele waarde` wordt geïnterpreteerd als null (mbv `default: null`)
- expliciete `null` van een `optionele waarde`: ok

**Voor `application/merge-patch+json` payloads**
([RFC 7396](https://datatracker.ietf.org/doc/html/rfc7396), alleen voor PATCH)

- non-presence: no-op (geen veranderingen)
- expliciete `null` van een `optionele waarde`: delete / zet op `null`
- expliciete `null` van een `waarde`: invalide mutatie, error

Hierbij een tabel met de verschillende scenario's:

| Waar            | Type waarde           | Non-presence | Expliciete `null` |
| --------------- | --------------------- | ------------ | ----------------- |
| json/parameters | Niet-optionele waarde | Error        | Error             |
| patch           | Optionele waarde      | Null         | Null              |

Voor de Spectral linter hebben we de volgende rules toegevoegd:

| Linting rule                                          | Voorbeeld       | Verwacht resultaat |
| ----------------------------------------------------- | --------------- | ------------------ |
| `required-no-default`                                 | `default: null` | Error              |
| `nonoptional-must-be-required-in-json-and-parameters` | `default: null` | Error              |

nonoptional-must-be-required-in-json-and-parameters: required-no-default: default-must-be-null:
optional-must-not-be-required-in-json-and-parameters:
nonoptional-must-not-be-nullable-in-merge-patch-json: optional-must-be-nullable-in-merge-patch-json:
patch-operation-content-type-must-be-merge-patch-json:

```yaml
hello:
  - item1
  - item2
```
