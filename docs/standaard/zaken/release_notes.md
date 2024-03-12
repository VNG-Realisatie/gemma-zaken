---
title: "Release Notes Zaken API"
date: '05-10-2023'
weight: 10
layout: page-with-side-nav
---
# Release Notes Zaken API

## Versies 1.5.1 / 1.4.1 / 1.3.1

Versie   | Releasedatum  
-------- | ------------- 
1.5.1    | 26-09-2023    
1.4.1    | 26-09-2023    
1.3.1    | 26-09-2022    

- API documentatie HEAD operatie response body verwijderd (#2328)
- Verplichte velden uit PATCH methode optioneel gemaakt (#2067)
- Expand parameter in _zoek operatie toegevoegd (#2345) 

## ~~Versie 1.2.1~~

Versie   | Releasedatum 
-------- | -------------
~~1.2.1~~    | 30-08-2023

Zaken API verise 1.2.1 teruggetrokken

## Versie 1.5.0

Versie   | Releasedatum 
-------- | -------------
1.5.0    | 22-08-2023   

- expand functionaliteit om met één aanroep een grote hoeveelheid informatie op te kunnen halen en zo de performance te verbeteren

## Versie 1.4.0

Versie   | Releasedatum 
-------- | -------------
1.4.0    | 21-03-2023   

- filtren op zaken die gearchiveerd moeten worden (#2139)
- filtren op zaken op meer dan één zaaktype (#2072)

## Versie 1.2.1

Versie   | Releasedatum 
-------- | -------------
1.2.1    | 21-12-2022 

- Om het aantal aanroepen te verminderen is middels JSON/HAL een expand mechanisme toegevoegd

## Versie 1.3.0

Versie   | Releasedatum 
-------- | -------------
1.3.0    | 19-12-2022  

- KVK nummer toegevoegd aan ROL van type Vestiging (#2125)
- IndicaiteLaatstGezetteStatus berekenen (#2088)
- Zaken met bepaalde actuele Status opvragen (#1642)
- Koppelen Zaakobjecten conform ZaakObjecttype in de ZTC (#1848)
- Opvragen zaken op basis vna een lijst UUID (#1728)
- Verbetering sorteren GET Lijst Zaken (#1892)
- Zaaktypeidentificatie toegevoegd aan Zaak (#1974)
- BUG Referentieimplementatie laat toe dat nieuwe documenten aan een gearchiveerde zaak gekoppeld worden (#1498)

## Versie 1.2.0

Versie   | Releasedatum 
-------- | -------------
1.2.0    | 2021-08-31    

- PUT/PATCH/DELETE operaties toegevoegd voor de resources `ZaakEigenschap` en `ZaakObject`.

## Versies 1.1.0 / 1.0.2 / 1.0.1 / 1.0.0

Versie   | Releasedatum 
-------- | -------------
1.1.0    | 24-05-2021   
1.0.2    | 2020-06-12   
1.0.1    | 2019-12-16   
1.0.0    | 2019-11-18