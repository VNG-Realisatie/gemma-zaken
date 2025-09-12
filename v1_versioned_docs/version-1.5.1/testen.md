---
title: "Test jouw implementatie van de Gemma Zaken API"
date: "2025-09-03"
layout: page-with-side-nav
---

Voor leveranciers hebben wij een automatische teststraat ontwikkelt, waarmee een API implementatie kan worden getest op de OpenAPI specificatie. Dit is gemaakt met [Schemathesis](https://schemathesis.io/).

[Lees hier meer details ](https://schemathesis.readthedocs.io/en/stable/guides/cicd/)over hoe je het in je CI/CD kan opzetten.

Hieronder volgen enkele voorbeelden voor hoe Schemathesis + ZGW is te testen.

## Docker

```sh
docker run --rm schemathesis/schemathesis run https://raw.githubusercontent.com/VNG-Realisatie/gemma-zaken/refs/heads/master/api_specs/v1/autorisaties/openapi.yaml \
# Jouw API URL
--url https://mijndienst.nl/api/v1
```

## Github Actions

```yaml
name: ZWG API Tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: schemathesis/action@v2
        with:
          # API schema location (URL or file path)
          schema: 'https://raw.githubusercontent.com/VNG-Realisatie/gemma-zaken/refs/heads/master/api_specs/v1/autorisaties/openapi.yaml'
          # Jouw API URL
          base-url: 'https://mijndienst.nl/api/v1'
          # Zie alle opties:
          # https://github.com/schemathesis/action?tab=readme-ov-file#configuration
```

## GitLab CI

```yaml
stages:
  - test

api-tests:
  stage: test
  image:
    name: schemathesis/schemathesis:stable
    entrypoint: [""]
  services:
    - name: your-api:latest
      alias: api
  variables:
    API_TOKEN: "jouw-geheime-token"
  script:
    - >
      schemathesis run http://api:8080/openapi.json
      --header "Authorization: Bearer $API_TOKEN"
      --wait-for-schema 60
      --report junit
  artifacts:
    when: always
    reports:
      junit: schemathesis-report/junit.xml
    paths:
      - schemathesis-report/
```
