---
title: ZGW API guides
weight: 90
---

*WIP*

In onderstaande voorbeelden wordt gebruik gemaakt van de door VNG gehoste
referentie implementaties van de verschillende componenten.


## Voorbereidingen



### Autorisatie

Om gebruik te kunnen maken van de verschillende APIs moet u beschikken over de
juiste autorisaties. Dit gebeurt middels een JSON Web Token ([JWT][jwt]) die de 
rechten bevat om gebruik te maken van bepaalde APIs en/of API resources. Het
JWT dient bij elk verzoek aan de APIs te worden meegegeven.

U kunt deze JWT eenvoudig verkrijgen door onderstaande stappen te volgen.


#### Stap 1: Client ID en secret aanmaken

Alle componenten moeten weten wie u bent. Dit proces is voor test doeleinden 
toegevoegd om uw **Client ID** en **secret** bekend te maken bij alle 
componenten.

1. Ga naar: https://ref.tst.vng.cloud/tokens/

2. Vul het **Client label** in (_bijv. `mijn-consumer`_) en klik op **Submit**.

3. Bewaar de gegevens op de volgende pagina:
   
   * Client ID (_bijv. `mijn-consumer-RuAJiUr4sUQp`_)
   * Secret (_bijv. `qy7gBX1zZj06epGQeyX9KrBNTMUu6eefSecretqy7gBX1zZj06epGQeyX9KrBNTMUu6eef`_)

Deze gegevens zijn nu direct bekend gemaakt bij alle beschikbare componenten.


#### Stap 2: JWT genereren

In onderstaande stap wordt het daadwerkelijk JWT gegenereerd op basis van het
**Client ID** en een **secret** waar zowel u als de componenten van op de
hoogte zijn.

1. Klik op **Generate a JWT**.
      
2. Op de volgende pagina kent u de juiste autorisaties toe in de vorm van 
   *scopes* en *zaaktypes*:

   a. Vink de **scopes** aan die van toepassing zijn. Voor test doeleinden kan
      alles aangevinkt worden om alle rechten te verkrijgen.
      
   b. Vink de verschillende **zaaktypes** aan die van toepassing zijn. Voor
      test doeleinden kan weer alles aangevinkt worden.

3.  Klik op **Submit**.

4. Bewaar de waarde die staat achter **Authorization**. Dit is het gegenereerde
   JWT.

U kunt op elk moment een ander JWT genereren met andere autorisaties. In
productie omgevingen dienen de autorisaties zo minimaal mogelijk te zijn.


#### Stap 3 (optioneel): Een ander JWT genereren

U kunt altijd een nieuw JWT genereren met andere autorisaties.

1. Ga naar: https://ref.tst.vng.cloud/tokens/generate-jwt/

2. Indien u recent stap 1 heeft gevolgd zijn de **Client ID** en **secret**
   reeds voor ingevuld. Zo niet, dan moet u deze zelf invullen met de gegevens
   uit stap 1.

3. Vink de **scopes** en/of **zaaktypes** aan die van toepassing zijn.

4. Klik op **Submit**.

5. Bewaar de waarde die staat achter **Authorization**. Dit is het gegenereerde
   JWT.


#### Stap 4: Gebruik het JWT

Het gegenereerde JWT moet worden meegegeven aan elk API-verzoek in de 
`Authorization` header: `Authorization: Bearer <JWT>`. Ter illustratie:

```bash
$ curl \
    -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImNsaWVudF9pZGVudGlmaWVyIjoiam9lcmktUnVBSmlVcjRzVVFwIn0.eyJpc3MiOiJtaWpuLWNvbnN1bWVyLVJ1QUppVXI0c1VRcCIsImlhdCI6MTU0MzIzNjU5NSwiemRzIjp7InNjb3BlcyI6WyJ6ZHMuc2NvcGVzLnN0YXR1c3Nlbi50b2V2b2VnZW4iLCJ6ZHMuc2NvcGVzLnpha2VuLmFhbm1ha2VuIiwiemRzLnNjb3Blcy56YWtlbi5sZXplbiJdLCJ6YWFrdHlwZXMiOlsiaHR0cHM6Ly9yZWYudHN0LnZuZy5jbG91ZC96dGMvYXBpL3YxL2NhdGFsb2d1c3Nlbi9mN2FmZDE1Ni1jOGY1LTQ2NjYtYjhiNS0yOGE0YTliNWRmYzcvemFha3R5cGVuLzAxMTlkZDRlLTdiZTktNDc3ZS1iY2NmLTc1MDIzYjE0NTNjMSJdfX0.RO_1PpH9DEvWIvwN2SyPQDBvJlgNc-EMVJaX6AHkfP8" \
    -H "Accept-Crs: EPSG:4326" \
    https://ref.tst.vng.cloud/zrc/api/v1/zaken
```

   
Benieuwd hoe het JWT er ongecodeerd uit ziet? Plak de waarde eens op
[jwt.io][jwt].

[jwt]: https://jwt.io/


## Gebruik maken van de APIs

Er zijn vele manieren om verzoeken te doen naar de APIs maar dit kan 
bijvoorbeeld met [cURL][curl-download] of [Postman][postman-download]. De 
voorbeelden maken gebruik van cURL omdat de commando's eenvoudig zijn weer te
geven.

[curl-download]: https://curl.haxx.se/download
[postman-download]: https://www.getpostman.com/apps


### Catalogussen ophalen

Een `GET`-verzoek op de [catalogus_list][catalogus_list] resource van het ZTC:

[catalogus_list]: https://ref.tst.vng.cloud/ztc/api/v1/schema/#operation/catalogus_list 

```bash
$ curl \
    -H "Authorization: Bearer <JWT>" \
    https://ref.tst.vng.cloud/ztc/api/v1/catalogussen
```

### Zaaktype ophalen

Een `GET`-verzoek op de [zaaktype_read][zaaktype_read] resource van het ZTC:

[zaaktype_read]: https://ref.tst.vng.cloud/ztc/api/v1/schema/#operation/zaaktype_read

```bash
$ curl 
    -H "Authorization: Bearer <JWT>" \
    https://ref.tst.vng.cloud/ztc/api/v1/catalogussen/f7afd156-c8f5-4666-b8b5-28a4a9b5dfc7/zaaktypen/0119dd4e-7be9-477e-bccf-75023b1453c1
```

### Zaken ophalen

Een `GET`-verzoek op de [zaak_read][zaak_read] resource van het ZRC. Hiervoor
dient de header `Accept-Crs` te worden meegegeven.

[zaak_read]: https://ref.tst.vng.cloud/zrc/api/v1/schema/#operation/zaak_read

```bash
$ curl \
    -H "Authorization: Bearer <JWT>" \
    -H "Accept-Crs: EPSG:4326" \
    https://ref.tst.vng.cloud/zrc/api/v1/zaken
```

### Zaak aanmaken

Een `POST`-verzoek op de [zaak_create][zaak_create] resource van het ZRC:

[zaak_create]: https://ref.tst.vng.cloud/zrc/api/v1/schema/#operation/zaak_create

#### Stap 1: Gegevens opstellen

Maak een bestand aan met de naam `zaak_aanmaken.json`, met de volgende inhoud:

```json
{
  "bronorganisatie": "291073475",
  "omschrijving": "string",
  "zaaktype": "https://ref.tst.vng.cloud/ztc/api/v1/catalogussen/f7afd156-c8f5-4666-b8b5-28a4a9b5dfc7/zaaktypen/0119dd4e-7be9-477e-bccf-75023b1453c1",
  "verantwoordelijkeOrganisatie": "https://www.example.com/api/v1/organisaties/12345",
  "startdatum": "2018-11-27",
  "uiterlijkeEinddatumAfdoening": "2018-11-27"
}
```

Het `zaaktype` moet daadwerkelijk bestaan. Dat wil zeggen dat de URL 
daadwerkelijk moet werken. Dit geldt (nog) niet voor 
`verantwoordelijkeOrganisatie`.

#### Stap 2: Gegevens versturen

Door het gebruik van `--data` wordt automatisch een `POST`-verzoek gedaan in
plaats van een `GET`-verzoek:

```bash
$ curl \
    -H "Authorization: Bearer <JWT>" \
    -H "Accept-Crs: EPSG:4326" \
    -H "Content-Type: application/json" \
    --data @zaak_aanmaken.json \
    https://ref.tst.vng.cloud/zrc/api/v1/zaken
```
