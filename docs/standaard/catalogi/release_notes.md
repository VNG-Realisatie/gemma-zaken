---
title: "Release Notes Catalogi API"
weight: 10
layout: page-with-side-nav
---
# Release Notes Catalogi API

## Versie 1.4.0

- Op diverse plekken property Any vervangen door een expliciete lijst van attributen. 
  - Issue [#2644](https://github.com/VNG-Realisatie/gemma-zaken/issues/2644). 
  - Pull request [#2646](https://github.com/VNG-Realisatie/gemma-zaken/pull/2646).
- Attribuut "servicenorm" op default waarde `null` gezet. 
  - Issue [#2625](https://github.com/VNG-Realisatie/gemma-zaken/issues/2625). 
  - Commit [debc040](https://github.com/VNG-Realisatie/gemma-zaken/commit/debc040f185622c6a9c903e51ff5ac60e14c9115).
- DELETE operatie toegevoegd aan endpoint `/catalogussen`. 
  - Issue [#2620](https://github.com/VNG-Realisatie/gemma-zaken/issues/2620).
  - Commit [8b57aec](https://github.com/VNG-Realisatie/gemma-zaken/commit/8b57aec65af7453edd84c78e8f3f2ef4309741be).
- Attribuut `indicatieSpecifiek` is deprecated gemaakt omdat de bedoeling ervan niet duidelijk is. 
  - Issue [#2543](https://github.com/VNG-Realisatie/gemma-zaken/issues/2543).
  - Commit [18c471c](https://github.com/VNG-Realisatie/gemma-zaken/commit/18c471cfc60c8d94b28a0aeace1b98c279a1e8eb).
- Attributen statustypen, resultaattypen en resultaatypeOmschrijving deprecated gemaakt in de respons van zaakobjecttypen. 
  - Issue [#2501](https://github.com/VNG-Realisatie/gemma-zaken/issues/2501).
  - Commit [7fc87da](https://github.com/VNG-Realisatie/gemma-zaken/commit/7fc87da603f25fc98b6c113987f41ec1d4e3a6d2).

## Versie 1.3.3

- Ontbrekende array's met omschrijvingen en identificaties toegevoegd in de responses van besluittypen, zaaktypen en informatieobjecttypen ([#2601](https://github.com/VNG-Realisatie/gemma-zaken/issues/2601)).
- In de POST-operatie van `/zaaktypen` het veld "deelzaaktypen" optioneel gemaakt zodat deze versie weer backwards compatible is met eerdere versies ([#2599](https://github.com/VNG-Realisatie/gemma-zaken/issues/2599)).

## Versie 1.3.2

Klik [hier](./release_notes_1.3.2.md) voor de release notes.

## Versies 1.3.1 / 1.2.1

Versie   | Release datum 
-------- | ------------- 
1.3.1    | 26-09-2023    
1.2.1    | 26-09-2023    

- Open API Specificatie aangepast: scope `geforceerd-schrijven` toegepast in plaats van het foutieve `geforceerd-bijwerken`.(#2302) 
- Relatie tussen Zaakobjecttype, Statustype en Resultaattype opgenomen in POST operatie van Zaakobjecttype (#2334) 

## Versie 1.3.0

Versie   | Release datum 
-------- | ------------- 
1.3.0    | 22-08-2023    

- Historiemodel toegevoegd om beheer Zaaktypen Catalogus te verbeteren

## Versie 1.2.0

Versie   | Release datum 
-------- | ------------- 
1.2.0    | 19-12-2022    

- `Catalogus` toegevoegd als convenience attribuut aan resources (#1855)
- `Categorie` en `Trefwoord` toegevoegd aan `Informatieobjecttype` (#2058)
- Correcties mogelijk op objecttypen die in gebruik zijn (#1924)
- `Informatieobjecttype` te relateren aan `Resultaattype` (#1876)
- `Zaakobjecttype` toegevoegd (#1846)
- `Verantwoordelijk` toevoegd aan `Zaaktype` (#1821)
- `Doorlooptijd` van `Status` toegevoegd (#1988)
- Per resource `beginObject`, `eindObject` toegevoegd (#1971)
- Werking `beginGeldigheid` en `eindGeldigheid` beschreven (#1970)

## Versies 1.1.0 / 1.0.0

Versie   | Release datum 
-------- | ------------- 
1.1.0    | 24-05-2021    
1.0.0    | 2019-11-18
