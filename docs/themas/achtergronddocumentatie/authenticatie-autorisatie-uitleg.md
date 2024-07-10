# Authenticatie en autorisatie

In de GitHUb repo [ZGW Token Issuer](https://github.com/VNG-Realisatie/token-issuer) is beschreven hoe een JWT-token genereerd kan worden met scopes voor een client applicatie. Hieronder een voorbeeld hoe je een client applicatie met als identificatie "allthescopesarebelongtous222223132532" kunt registreren die alle autorisaties (scopes) heeft.


```http
POST /api/v1/register HTTP/1.1
Host: zaken-auth.test.vng.cloud
Content-Type: application/json
Content-Length: 166

{
  "clientIds": [
    "allthescopesarebelongtous222223132532"
  ],
  "secret": "sosecret",
  "label": "user",
  "heeftAlleAutorisaties": true,
  "autorisaties": []
}
```

Deze POST-operatie geeft in dit geval de volgende respons:

```json
{
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsImNsaWVudF9pZGVudGlmaWVyIjoiYWxsdGhlc2NvcGVzYXJlYmVsb25ndG91czIyMjIyMzEzMjUzMi1idWZtM2haZzV5Z1UiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJhbGx0aGVzY29wZXNhcmViZWxvbmd0b3VzMjIyMjIzMTMyNTMyLWJ1Zm0zaFpnNXlnVSIsImlhdCI6MTcyMDUzNzUwMywiY2xpZW50X2lkIjoiYWxsdGhlc2NvcGVzYXJlYmVsb25ndG91czIyMjIyMzEzMjUzMi1idWZtM2haZzV5Z1UifQ.zORTmHVNMj70zRwc5OeG76kSLAHgrYypTBkVK2MS-Kk",
    "propagated": [
        {
            "endpoint": "http://brc:8000/api/v1",
            "success": true,
            "client_id": "allthescopesarebelongtous222223132532-bufm3hZg5ygU"
        },
        {
            "endpoint": "http://nrc:8000/api/v1",
            "success": true,
            "client_id": "allthescopesarebelongtous222223132532-bufm3hZg5ygU"
        },
        {
            "endpoint": "http://ztc:8000/api/v1",
            "success": true,
            "client_id": "allthescopesarebelongtous222223132532-bufm3hZg5ygU"
        },
        {
            "endpoint": "http://ac:8000/api/v1",
            "success": true,
            "client_id": "allthescopesarebelongtous222223132532-bufm3hZg5ygU"
        },
        {
            "endpoint": "http://zrc:8000/api/v1",
            "success": true,
            "client_id": "allthescopesarebelongtous222223132532-bufm3hZg5ygU"
        },
        {
            "endpoint": "http://drc:8000/api/v1",
            "success": true,
            "client_id": "allthescopesarebelongtous222223132532-bufm3hZg5ygU"
        }
    ]
}
```

Het attribuut "authorization" bevat het JWT-token:

```
Bearer eyJhbGciOiJIUzI1NiIsImNsaWVudF9pZGVudGlmaWVyIjoiYWxsdGhlc2NvcGVzYXJlYmVsb25ndG91czIyMjIyMzEzMjUzMi1idWZtM2haZzV5Z1UiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJhbGx0aGVzY29wZXNhcmViZWxvbmd0b3VzMjIyMjIzMTMyNTMyLWJ1Zm0zaFpnNXlnVSIsImlhdCI6MTcyMDUzNzUwMywiY2xpZW50X2lkIjoiYWxsdGhlc2NvcGVzYXJlYmVsb25ndG91czIyMjIyMzEzMjUzMi1idWZtM2haZzV5Z1UifQ.zORTmHVNMj70zRwc5OeG76kSLAHgrYypTBkVK2MS-K
```

Op de website [jwt.io](https://jwt.io/) kun je dit token decoden en het "client_id" zien:

![alt text](image.png)

Op basis van het client_id kan de betreffende ZGW API de Autorisatie API aanroepen om te zien welke scopes (lees: rechten) de aanroepende client heeft. In dit geval heeft de client alle rechten.

Het JWT-token wordt als header-veld meegenomen zodat de geregistreerde client-applicatie door de ZGW API's geauthenticeerd en geautoriseerd kan worden. Bijvoorbeeld bij het opvragen van alle zaken:

```http
GET /api/v1/zaken HTTP/1.1
Host: zaken-api.test.vng.cloud
Accept: application/json
Content-Type: application/json
Accept-Crs: EPSG:4326
Content-Crs: EPSG:4326
Authorization: Bearer eyJhbGciOiJIUzI1NiIsImNsaWVudF9pZGVudGlmaWVyIjoiYWxsdGhlc2NvcGVzYXJlYmVsb25ndG91czIyMjIyMzEzMjUzMi14ajZleXBjUDN5cDMiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJhbGx0aGVzY29wZXNhcmViZWxvbmd0b3VzMjIyMjIzMTMyNTMyLXhqNmV5cGNQM3lwMyIsImlhdCI6MTcyMDUzMzM1OCwiY2xpZW50X2lkIjoiYWxsdGhlc2NvcGVzYXJlYmVsb25ndG91czIyMjIyMzEzMjUzMi14ajZleXBjUDN5cDMifQ.NMGAQIWrI_ftImTMkww-yKBLK1w1cIKpAdw1Dviqk4s
```
