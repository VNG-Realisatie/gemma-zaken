# Samenvatting ADR-validatieresultaten

Bron: [`adr-output.txt`](./adr-output.txt). De meldingen zijn gegroepeerd op ADR-regel; concrete schema- en parameternamen kunnen daardoor als verschillende tekstvarianten van dezelfde foutsoort voorkomen.

## Totaal

| Foutniveau | Aantal |
|---|---:|
| Errors | 138 |
| Warnings | 153 |
| **Totaal** | **291** |

In de uitvoer komen **7 unieke errorregels** en **2 unieke warningregels** voor. Die regels bevatten samen **214 verschillende concrete meldingen** (regel en meldingstekst gecombineerd).

## Resultaten per API

| API / versie | Errors | Warnings | Totaal |
|---|---:|---:|---:|
| AC 1.1.0 | 2 | 13 | 15 |
| BRC 1.1.0 | 5 | 1 | 6 |
| ZTC 1.4.0 | 25 | 0 | 25 |
| DRC 1.8.0 | 27 | 1 | 28 |
| NRC 1.1.0 | 2 | 1 | 3 |
| ZRC 1.8.0 | 77 | 137 | 214 |
| **Totaal** | **138** | **153** | **291** |

## Unieke errors

| ADR-regel | Aantal | Verschillende meldingsteksten | Voorbeeld |
|---|---:|---:|---|
| `nlgov:problem-invalid-input` | 63 | 1 | GET- en DELETE-endpoints met parameters, en alle andere endpoints, moeten een 400-response kunnen retourneren. |
| `nlgov:query-keys-camel-case` | 63 | 57 | `domein__in` is niet lower camelCase. |
| `nlgov:info-contact-fields-exist` | 5 | 1 | `info.contact` mist een of meer van de velden email, name en url. |
| `nlgov:missing-header` | 4 | 1 | Retourneer het volledige versienummer in een response-header. |
| `nlgov:include-major-version-in-uri` | 1 | 1 | Neem het major-versienummer op in de URI. |
| `nlgov:paths-kebab-case` | 1 | 1 | `/zaaknummer_reserveren` is niet kebab-case. |
| `oas3-valid-media-example` | 1 | 1 | De property `value` moet van het type array zijn. |
| **Totaal** | **138** | **63** | |

## Unieke warnings

| ADR-regel | Aantal | Verschillende meldingsteksten | Voorbeeld |
|---|---:|---:|---|
| `nlgov:schema-camel-case` | 150 | 150 | Een schemanaam moet UpperCamelCase zijn, bijvoorbeeld `zrcAutorisatie`. |
| `nlgov:servers-use-https` | 3 | 1 | Server-URL `/api/v1` moet beginnen met `https://`. |
| **Totaal** | **153** | **151** | |

De concrete varianten bij `query-keys-camel-case` en `schema-camel-case` betreffen verschillende parameter- en schemanamen. De voorbeelden hierboven zijn representatief; de oorspronkelijke uitvoer bevat de volledige paden en meldingen.
