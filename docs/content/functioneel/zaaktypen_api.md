---
title: "Zaaktypen-API"
date: '19-01-2019'
---

# ZAAKTYPEN API

FUNCTIONELE BESCHRIJVING

Hieronder lichten we de gebruiksmogelijkheden van deze API toe. Voor de
werking van deze API verwijzen wij u naar de OAS-specificatie (zie
‘link’ hieronder).

<table>
<tbody>
<tr class="odd">
<td><strong>Aspect</strong></td>
<td><strong>Beschrijving</strong></td>
</tr>
<tr class="even">
<td>Doel</td>
<td>Het kunnen aanspreken van een voorziening voor het onderhouden en raadplegen van zaken inclusief bijbehorende statussen, rollen en relaties naar betrokkenen, objecten, zaaktypen en statustypen.</td>
</tr>
<tr class="odd">
<td>Domein</td>
<td>Zaakgericht werken</td>
</tr>
<tr class="even">
<td>Versiedatum documentatie</td>
<td>19 november 2018</td>
</tr>
<tr class="odd">
<td>Provider</td>
<td><a href="https://www.gemmaonline.nl/index.php/GEMMA2/0.9/id-3ef9cdd9-631c-4d3e-88c3-f756423d6314"><span class="underline">Zaaktypecataloguscomponent</span></a> (GEMMA2)</td>
</tr>
<tr class="even">
<td>Consumer</td>
<td>Componenten waarmee zaken behandeld worden (Zaakafhandelcomponenten; ZAC’s) en (andere) componenten die zaaktypegegevens raadplegen.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Informatiemodel</td>
<td><a href="https://www.gemmaonline.nl/index.php/ImZTC_2.2_in_ontwikkeling"><span class="underline">ImZTC, versie 2.2</span></a> (in-ontwikkeling)</td>
</tr>
<tr class="odd">
<td>API-specificaties</td>
<td><a href="https://ref.tst.vng.cloud/ztc/api/v1/schema/"><span class="underline">https://ref.tst.vng.cloud/ztc/api/v1/schema/</span></a></td>
</tr>
<tr class="even">
<td>Bijzonderheden</td>
<td></td>
</tr>
</tbody>
</table>

Deze API omvat de navolgende resources (‘bronnen’) en de daarvan beschreven mogelijkheden.

### Resource: Catalogussen

<table>
<tbody>
<tr class="odd">
<td><strong>Aspect</strong></td>
<td><strong>Beschrijving</strong></td>
</tr>
<tr class="even">
<td>Doel</td>
<td><ul>
<li>Opvragen van een overzicht van alle beschikbare Catalogussen.</li>
<li>Opvragen van de gegevens van een specifieke Catalogus.</li>
<li>Opvragen van een overzicht van alle beschikbare Zaaktypen.</li>
<li>Opvragen van de gegevens van een specifiek Zaaktype.</li>
<li>Opvragen van een overzicht van alle beschikbare Besluittypen.</li>
<li>Opvragen van de gegevens van een specifiek Besluittype.</li>
<li>Opvragen van een overzicht van alle beschikbare Informatieobjecttypen.</li>
<li>Opvragen van de gegevens van een specifiek Informatieobjecttype.</li>
<li>Opvragen van een overzicht van alle beschikbare Eigenschap.</li>
<li>Opvragen van de gegevens van een specifieke Eigenschap.</li>
<li>Opvragen van een overzicht van alle beschikbare Roltypen.</li>
<li>Opvragen van de gegevens van een specifiek Roltype.</li>
<li>Opvragen van een overzicht van alle beschikbare Statustypen.</li>
<li>Opvragen van de gegevens van een specifiek Statustype.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Gegevens</td>
<td><p>Objecttype Catalogus, inclusief relatie naar ZAAKTYPE, BESLUITTYPE, INFORMATIEOBJECTTYPE.<br/>https://www.gemmaonline.nl/index.php/Imztc_2.2/doc/objecttype/catalogus</td>
</tr>
<tr class="even">
<td>OAS-specificaties</td>
<td><a href="https://ref.tst.vng.cloud/ztc/api/v1/schema/#operation/catalogus_list">https://ref.tst.vng.cloud/ztc/api/v1/schema/#operation/catalogus_list</a></td>
</tr>
<tr class="odd">
<td>Bijzonderheden</td>
<td><ul>
<li>Het aanmaken van Catalogussen wordt nog niet ondersteund.</li>
<li>Het verwijderen van Catalogussen wordt nog niet ondersteund.</li>
<li>Het aanpassen van Catalogussen wordt nog niet ondersteund.</li>
</ul></td>
</tr>
</tbody>
</table>

### Resource: Zaaktype

<table>
<tbody>
<tr class="odd">
<td><strong>Aspect</strong></td>
<td><strong>Beschrijving</strong></td>
</tr>
<tr class="even">
<td>Doel</td>
<td><ul>
<li>Opvragen van een overzicht van Zaaktypen in een Catalogus.</li>
<li>Opvragen van – de gegevens van - een specifiek Zaaktype uit een Catalogus.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Gegevens</td>
<td>Objecttype ZAAKTYPE, inclusief relatie naar STAUSTYPE, EIGENSCHAP, ROLTYPE en BESLUITTYPE.<br/>
https://www.gemmaonline.nl/index.php/Imztc_2.2/doc/objecttype/zaaktype</td>
</tr>
<tr class="even">
<td>OAS-specificaties</td>
<td><a href="https://ref.tst.vng.cloud/ztc/api/v1/schema/#operation/zaaktype_list">https://ref.tst.vng.cloud/ztc/api/v1/schema/#operation/zaaktype_list</a></td>
</tr>
<tr class="odd">
<td>Bijzonderheden</td>
<td><ul>
<li>Het aanmaken van Zaaktypen wordt nog niet ondersteund.</li>
<li>Het verwijderen van Zaaktypen wordt nog niet ondersteund.</li>
<li>Het aanpassen van Zaaktypen wordt nog niet ondersteund.</li>
</ul>
</td>
</tr>
</tbody>
</table>

### Besluittype

<table>
<tbody>
<tr class="odd">
<td><strong>Aspect</strong></td>
<td><strong>Beschrijving</strong></td>
</tr>
<tr class="even">
<td>Doel</td>
<td><ul>
<li>Opvragen van een overzicht van alle Besluittypen met relaties naar Catalogus en Zaaktypes.</li>
<li>Opvragen van – de gegevens van - een specifiek Besluittype.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Gegevens</td>
<td>https://www.gemmaonline.nl/index.php/Imztc_2.2/doc/objecttype/besluittype</td>
</tr>
<tr class="even">
<td>OAS-specificaties</td>
<td><a href="https://ref.tst.vng.cloud/ztc/api/v1/schema/#operation/besluittype_list">https://ref.tst.vng.cloud/ztc/api/v1/schema/#operation/besluittype_list</a></td>
</tr>
<tr class="odd">
<td>Bijzonderheden</td>
<td><ul>
<li>Het aanmaken van Besluittypen wordt nog niet ondersteund. </li>
<li>Het verwijderen van Besluittypen wordt nog niet ondersteund. </li>
<li>Het aanpassen van Besluittypen wordt nog niet ondersteund.</li>
</ul></td>
</tr>
</tbody>
</table>

### Resource: Informatieobjectype

<table>
<tbody>
<tr class="odd">
<td><strong>Aspect</strong></td>
<td><strong>Beschrijving</strong></td>
</tr>
<tr class="even">
<td>Doel</td>
<td><ul>
<li>Opvragen van een overzicht van alle Informatieobjectypen inclusief relatie naar de Catalogus waarin het Informatieobjecttype staat beschreven</li>
<li>Opvragen van – de gegevens van - een specifiek Informatieobjectypen.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Gegevens</td>
<td>Objecttype INFORMATIEOBJECTYPE. https://www.gemmaonline.nl/index.php/Imztc_2.2/doc/objecttype/informatieobjecttype</td>
</tr>
<tr class="even">
<td>OAS-specificaties</td>
<td><a href="https://ref.tst.vng.cloud/ztc/api/v1/schema/#operation/informatieobjecttype_list">https://ref.tst.vng.cloud/ztc/api/v1/schema/#operation/informatieobjecttype_list</a></td>
</tr>
<tr class="odd">
<td>Bijzonderheden</td>
<td><ul>
<li>Het aanmaken van Informatieobjectype wordt nog niet ondersteund.</li>
<li>Het verwijderen van Informatieobjectype wordt nog niet ondersteund.</li>
<li>Het aanpassen van Informatieobjectype wordt nog niet ondersteund.</li>
</ul></td>
</tr>
</tbody>
</table>

### Resource: Eigenschappen

<table>
<tbody>
<tr class="odd">
<td><strong>Aspect</strong></td>
<td><strong>Beschrijving</strong></td>
</tr>
<tr class="even">
<td>Doel</td>
<td><ul>
<li>Opvragen van een overzicht van alle Eigenschappen zoals gedefinieerd bij een Zaaktype, met de gegevens per Eigenschap.</li>
<li>Opvragen van – de gegevens van - een specifieke Eigenschap.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Gegevens</td>
<td>Objecttype EIGENSCHAP, inclusief relatie naar ZAAKTYPE. https://www.gemmaonline.nl/index.php/Imztc_2.2/doc/objecttype/eigenschap</td>
</tr>
<tr class="even">
<td>OAS-specificaties</td>
</tr>
<td><a href="https://ref.tst.vng.cloud/ztc/api/v1/schema/#operation/eigenschap_list">https://ref.tst.vng.cloud/ztc/api/v1/schema/#operation/eigenschap_list</a></td>
<tr class="odd">
<td>Bijzonderheden</td>
<td><ul>
<li>Het aanmaken van Eigenschappen wordt nog niet ondersteund.</li>
<li>Het verwijderen van Eigenschappen wordt nog niet ondersteund.</li>
<li>Het aanpassen van Eigenschappen wordt nog niet ondersteund.</li>
</ul></td>
</tr>
</tbody>
</table>

### Resource: Roltypen

<table>
<tbody>
<tr class="odd">
<td><strong>Aspect</strong></td>
<td><strong>Beschrijving</strong></td>
</tr>
<tr class="even">
<td>Doel</td>
<td><ul>
<li>Opvragen van een overzicht van alle Roltypen zoals gedefinieerd bij een Zaaktype, met de gegevens per Eigenschap.</li>
<li>Opvragen van – de gegevens van - een specifieke Eigenschap.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Gegevens</td>
<td>Objecttype ROLTYPE, inclusief relatie naar ZAAKTYPE en mogelijkeBETROKKENEN. https://www.gemmaonline.nl/index.php/Imztc_2.2/doc/objecttype/roltype</td>
</tr>
<tr class="even">
<td>OAS-specificaties</td>
</tr>
<td><a href="https://ref.tst.vng.cloud/ztc/api/v1/schema/#operation/roltype_list">https://ref.tst.vng.cloud/ztc/api/v1/schema/#operation/roltype_list</a></td>
<tr class="odd">
<td>Bijzonderheden</td>
<td><ul>
<li>Het aanmaken van Roltypen wordt nog niet ondersteund.</li>
<li>Het verwijderen van Roltypen wordt nog niet ondersteund.</li>
<li>Het aanpassen van Roltypen wordt nog niet ondersteund.</li>
</ul></td>
</tr>
</tbody>
</table>

### Resource: Statustypen

<table>
<tbody>
<tr class="odd">
<td><strong>Aspect</strong></td>
<td><strong>Beschrijving</strong></td>
</tr>
<tr class="even">
<td>Doel</td>
<td><ul>
<li>Opvragen van een overzicht van alle Statustypen zoals gedefinieerd bij een Zaaktype, met de gegevens per Statustype.</li>
<li>Opvragen van – de gegevens van - een specifieke Statustype.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Gegevens</td>
<td>Objecttype STATUSTYPE, inclusief relatie naar ZAAKTYPE. https://www.gemmaonline.nl/index.php/Imztc_2.2/doc/objecttype/statustype</td>
</tr>
<tr class="even">
<td>OAS-specificaties</td>
</tr>
<td><a href="https://ref.tst.vng.cloud/ztc/api/v1/schema/#operation/statustype_list">https://ref.tst.vng.cloud/ztc/api/v1/schema/#operation/statustype_list</a></td>
<tr class="odd">
<td>Bijzonderheden</td>
<td><ul>
<li>Het aanmaken van Statustypen wordt nog niet ondersteund.</li>
<li>Het verwijderen van Statustypen wordt nog niet ondersteund.</li>
<li>Het aanpassen van Statustypen wordt nog niet ondersteund.</li>
</ul></td>
</tr>
</tbody>
</table>
