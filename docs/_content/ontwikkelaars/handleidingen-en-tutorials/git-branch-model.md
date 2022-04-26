---
title: "OneFlow branching model"
date: '22-04-2022'
weight: 20
---

Het ontwikkelen van de ZGW componenten gebeurd aan de hand van het git branching
model "[OneFlow]". In deze tutorial wordt beschreven hoe een je om dient te gaan
met dit type branch model.

## Standaard branch
Voor het aanmaken van nieuwe features of bugfixes dien je gebruik te maken van de 
`master` branch tenzij je een feature of bugfix wilt toevoegen voor een specifieke versie.

## Testomgevingen
Voor testomgevingen wordt gebruikt gemaakt van de `master` branch. Om een nieuwe versie 
te deployen kan je als ontwikkelaar een [git tag] gebruiken of gebruik maken van de sha-256 checksum
van een specifieke commit. Bij het gebruik van een git tag dien je het volgende format te hanteren:
```
1.3.0-alpha1
```

## Productieomgevingen
Productieomgevingen worden alleen gebruikt in combinatie met daadwerkelijke release versies. 
Voor deze versies is altijd een branch aangemaakt met het volgende format: `<major>.<minor>.x`.
Een voorbeeld hiervan zou kunnen zijn: `1.2.x`. Alleen bugfixes kunnen nog toegevoegd worden
aan deze branches. Een nieuwe minor of major versie betekent een nieuwe release en 
daarbij een nieuwe branch (bijvoorbeeld in het geval van een nieuwe minor release `1.3.x`).

## Bugfixes en features
Ook bugfixes en nieuw features zijn idealiter gericht naar de `master` branch tenzij
het gaat om een bugfix of feature voor een specifieke release. Er kan daarnaast
gekozen worden om de bugfix niet alleen naar `master` toe te richten maar ook te backporten
naar specifiek releases. Wanneer het gaat om zogenaamde "breaking changes" dien je
altijd een nieuwe release te doen en hiermee ook de major versie op te hogen (e.g van `1.1.1` naar `2.0.0`).

## Aandachtspunten
Om een versie van een ZGW component op te hogen dienen je rekening te houden met
een aantal punten:
1. Het ophogen van het versienummer gaat normaliter via de `API_VERSION` setting in je Django settings
2. Om de API specificaties up-to-date te brengen dien je het `generate_schema` management commando te draaien welke onder andere de openapi specificatie update
3. Indien je een release of release-candidate uitbrengt dien je ook het `CHANGELOG.rst` bestand uit te breiden met de wijzingingen die zijn gedaan

[OneFlow]: https://www.endoflineblog.com/oneflow-a-git-branching-model-and-workflow
[git tag]: https://git-scm.com/book/en/v2/Git-Basics-Tagging#_lightweight_tags
