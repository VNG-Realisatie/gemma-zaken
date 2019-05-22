---
title: ZGW API guides
weight: 90
---

In onderstaande voorbeelden wordt gebruik gemaakt van de door VNG gehoste
referentie implementaties van de verschillende componenten.

## Voorbereidingen


### Authorization

To access the ZGW APIs you must be authorized. This could be done through 
a JSON Web Token ([JWT][jwt]) and the Autorisatiecomponent ([AC][ac]). 
The JWT includes authentication part (Client ID and Secret), AC specifies
the rights for certain APIs and / or API resources. 

The JWT must be included to every request to the APIs.

#### Step 1: Create Client ID and Secret

All components must know who you are. This process has been added for testing 
purposes to make all components know your **Client ID** and **Secret**.

1. Go to https://ref.tst.vng.cloud/tokens/

2. Enter the **Clientlabel** (_for example `mijn-consumer`_) and click on **Bevestig**.

3. Save the generated **Client ID** and **Secret**
   
They has now been immediately added to all available components listed in the left 
part of the page.

#### Step 2: Generate JWT

In the step below, the actual JWT is generated based on the **Client ID** and 
the **Secret** that both you and the components are aware of.

1. Click on **Genereer een JWT** button below **Client ID** and **Secret** generated 
   in step 1.

   If everything goes well, the Client ID and Secret are already pre-filled and JWT 
   is generated. If you have other credentials fill them in the relevant fields and 
   click on **Bevestig** button.
         
2. Save the value of **Authorization** field. This is the generated JWT.

You can generate a different JWT with different authorizations at any time. In 
production environments, the authorizations must be as minimal as possible.

#### Step 3: Configure authorization

After the basic authentication is set up you need to specify your access for API's  
resources. This is made via adding rights to Autorisatiecomponent (AC).

1. Navigate to **Configure auth** section.
   **Client ID** should be already pre-filled. Fill in the rest authorization properties:
   
   a. Choose **Component**, which you want to request. 
   
   b. Tick the **Scopes** that apply. For testing purposes, all scopes can be checked.
   
   c. Specify **Zaaktype** to access for **ZRC** component.
   
   d. Specify **Informatieobjecttype** to access for **DRC** component.
   
   e. Specify **Besluittype** to access for **DRC** component.
   
   f. Choose **Maximale vertrouwelijkheidaanduiding** for **ZRC** and **DRC** components.
   
2. Click on **Add authorization**.

Repeat this step to create authorization for all components you want to have an access. 

#### Step 4: Use the JWT

The generated JWT should be given to each API request in the `Authorization` header:  
`Authorization: Bearer <JWT>`. For a example:

```bash
$ curl \
    -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImNsaWVudF9pZGVudGlmaWVyIjoiam9lcmktUnVBSmlVcjRzVVFwIn0.eyJpc3MiOiJtaWpuLWNvbnN1bWVyLVJ1QUppVXI0c1VRcCIsImlhdCI6MTU0MzIzNjU5NSwiemRzIjp7InNjb3BlcyI6WyJ6ZHMuc2NvcGVzLnN0YXR1c3Nlbi50b2V2b2VnZW4iLCJ6ZHMuc2NvcGVzLnpha2VuLmFhbm1ha2VuIiwiemRzLnNjb3Blcy56YWtlbi5sZXplbiJdLCJ6YWFrdHlwZXMiOlsiaHR0cHM6Ly9yZWYudHN0LnZuZy5jbG91ZC96dGMvYXBpL3YxL2NhdGFsb2d1c3Nlbi9mN2FmZDE1Ni1jOGY1LTQ2NjYtYjhiNS0yOGE0YTliNWRmYzcvemFha3R5cGVuLzAxMTlkZDRlLTdiZTktNDc3ZS1iY2NmLTc1MDIzYjE0NTNjMSJdfX0.RO_1PpH9DEvWIvwN2SyPQDBvJlgNc-EMVJaX6AHkfP8" \
    -H "Accept-Crs: EPSG:4326" \
    https://ref.tst.vng.cloud/zrc/api/v1/zaken
```

Curious as to what the decoded JWT looks like? Paste its value at [jwt.io][jwt].

[jwt]: https://jwt.io/
[ac]: https://ref.tst.vng.cloud/ac/api/v1/schema/


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
  "verantwoordelijkeOrganisatie": "291073475",
  "startdatum": "2018-11-27",
  "uiterlijkeEinddatumAfdoening": "2018-11-27"
}
```

Het `zaaktype` moet daadwerkelijk bestaan. 

#### Stap 2: Gegevens versturen

Door het gebruik van `--data` wordt automatisch een `POST`-verzoek gedaan in
plaats van een `GET`-verzoek:

```bash
$ curl \
    -H "Authorization: Bearer <JWT>" \
    -H "Accept-Crs: EPSG:4326" \
    -H "Content-Crs: EPSG:4326" \
    -H "Content-Type: application/json" \
    --data @zaak_aanmaken.json \
    https://ref.tst.vng.cloud/zrc/api/v1/zaken
```
