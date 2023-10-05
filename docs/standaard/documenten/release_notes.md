---
title: "Release Notes Documenten API"
date: '05-10--2023'
weight: 10
layout: page-with-side-nav
---
# Release Notes Documenten API

Versie   | Release datum 
-------- | ------------- 
1.4.2    | 26-09-2023    
1.3.2    | 26-09-2023    
1.2.5    | 26-09-2023    

- Ontbrekende query parameters toegevoegd aan `documenten_zoek` operatie (#2294)
- `expand` parameter toegevoegd aan `documenten_zoek` operatie (#2345)
- Versienummers in documentatie specifiek gemaakt (#2301)
- Parameternaam `UUID__IN` in `documenten_zoek` operatie correct gespeld in OAS yaml (#2300)
- Response bodies verwijderd uit `HEAD` operaties (#2328)

Versie   | Release datum 
-------- | ------------- 
1.4.1    | 29-08-2023    
1.3.1    | 29-08-2023    
1.2.4    | 29-08-2023    

- `lock` attribuut weer toegevoegd aan groepsattribuut `bestandsdelen` aan responses GET/GET List /Informatieobjecten (#2293)


Versie   | Release datum 
-------- | ------------- 
1.4.0    | 22-08-2023    

- Expand mogelijkheid toegevoegd teneinde met één aanroep meer informatie op te halen en zo de performance te verbeteren. (#2235)
- `trefwoorden` toegevoegd aan resource `Informatieobject`. (#2057)
- Validatie op `informatieobjecttype` bij wijzigen `Informatieobject` vervallen (#2241) 

Versie   | Release datum 
-------- | ------------- 
1.3.0    | 29-03-2023    

- Gelockte documenten kunnen niet verwijderd worden (#1956)
- Telefoonnummer aan relatieklasse `Verzendingen` toegevoegd (#2113)
- Informatieobjecttype aanpasbaar gemaakt (#1777)

Versie   | Release datum 
-------- | ------------- 
1.2.0    | 19-12-2022    

- Ontbrekende attributen RGBZ 2 toegevoegd tbh voldoen aan TMLO (#1884)
- Scope `geforceerd-bijwerken` toegevoegd om Informatieobjecten met status `definitief` te kunnen bewerken (#1859)
- Relatieklasse `Verzendingen` toegevoegd (#1785)
- Voorbeeldwaarde attribuut `taal` aangepast naar correcte waarde (#1775)
- `documenten_zoek` endpoint toegevoegd (#1881)
  

Versie   | Release datum 
-------- | ------------- 
1.1.0    | 24-05-2021    
1.0.1    | 2019-12-16    
1.0.0    | 2019-11-18    
