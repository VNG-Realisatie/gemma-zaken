---
title: "Informatieobjecten-API"
date: '21-01-2019'
---

# INFORMATIEOBJECTEN API

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
<td>Het kunnen aanspreken van een voorziening voor het onderhouden en raadplegen van enkelvoudige informatieobjecten inclusief relaties naar objecten.</td>
</tr>
<tr class="odd">
<td>Domein</td>
<td>Zaakgericht werken</td>
</tr>
<tr class="even">
<td>Versiedatum documentatie</td>
<td>21 januari 2019</td>
</tr>
<tr class="odd">
<td>Provider</td>
<td><a href="https://www.gemmaonline.nl/index.php/GEMMA2/0.9/id-0e99ec6c-283a-4ec9-8efa-e11468e6b878"><span class="underline">Documentregistratiecomponent</span></a> (GEMMA2)</td>
</tr>
<tr class="even">
<td>Consumer</td>
<td>Componenten waarmee informatieobjecten (in de volksmond documenten) beheerd worden (Documentbeheercomponenten; [DBC’s](https://www.gemmaonline.nl/index.php/GEMMA2/0.9/id-25ee9ea7-be66-4bdd-b40c-191777a88b35)) en (andere) componenten die informatieobjecten raadplegen.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Informatiemodel</td>
<td><a href="https://www.gemmaonline.nl/index.php/RGBZ_2.0_in_ontwikkeling"><span class="underline">RGBZ, versie 2.0</span></a> (in-ontwikkeling)</td>
</tr>
<tr class="odd">
<td>API-specificaties</td>
<td><a href="https://documenten-api.vng.cloud/api/v1/schema/"><span class="underline">https://documenten-api.vng.cloud/api/v1/schema/</span></a></td>
</tr>
<tr class="even">
<td>Bijzonderheden</td>
<td></td>
</tr>
</tbody>
</table>

Deze API omvat de navolgende resources (‘bronnen’) en de daarvan beschreven mogelijkheden.

### Resource: Enkelvoudiginformatieobjecten

<table>
<tbody>
<tr class="odd">
<td><strong>Aspect</strong></td>
<td><strong>Beschrijving</strong></td>
</tr>
<tr class="even">
<td>Doel</td>
<td><ul>
<li><a href="https://documenten-api.vng.cloud/api/v1/schema/#operation/enkelvoudiginformatieobject_list">Opvragen</a> van een overzicht van alle beschikbare enkelvoudiginformatieobjecten.</li>
<li><a href="https://documenten-api.vng.cloud/api/v1/schema/#operation/enkelvoudiginformatieobject_read">Opvragen</a> van de details van een specifiek enkelvoudiginformatieobject.</li>
<li><a href="https://documenten-api.vng.cloud/api/v1/schema/#operation/enkelvoudiginformatieobject_create">Aanmaken</a> van een enkelvoudiginformatieobject.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Gegevens</td>
<td><p>Objecttype ENKELVOUDIGINFORMATIEOBJECT.<br/>https://www.gemmaonline.nl/index.php/Rgbz_2.0/doc/objecttype/enkelvoudig_informatieobject</td>
</tr>
<tr class="even">
<td>OAS-specificaties</td>
<td><a href="https://documenten-api.vng.cloud/api/v1/schema/#tag/enkelvoudiginformatieobjecten">https://documenten-api.vng.cloud/api/v1/schema/#tag/enkelvoudiginformatieobjecten</a></td>
</tr>
<tr class="odd">
<td>Bijzonderheden</td>
<td><ul>
<li>Het verwijderen van Enkelvoudiginformatieobjecten wordt nog niet ondersteund.</li>
<li>Het aanpassen van Enkelvoudiginformatieobjecten wordt nog niet ondersteund.</li>
</ul></td>
</tr>
</tbody>
</table>

### Resource: Objectinformatieobjecten

<table>
<tbody>
<tr class="odd">
<td><strong>Aspect</strong></td>
<td><strong>Beschrijving</strong></td>
</tr>
<tr class="even">
<td>Doel</td>
<td><ul>
<li><a href="https://documenten-api.vng.cloud/api/v1/schema/#operation/objectinformatieobject_list">Opvragen</a> van een overzicht van Objectinformatieobjecten.</li>
<li><a href="https://documenten-api.vng.cloud/api/v1/schema/#operation/objectinformatieobject_read">Opvragen</a> van – de gegevens van - een specifiek Objectinformatieobject.</li>
<li><a href="https://documenten-api.vng.cloud/api/v1/schema/#operation/objectinformatieobject_create">Aanmaken</a> van een Objectinformatieobject</li>
<li><a href="https://documenten-api.vng.cloud/api/v1/schema/#operation/objectinformatieobject_update">Bijwerken</a> van een Objectinformatieobject</li>
<li><a href="https://documenten-api.vng.cloud/api/v1/schema/#operation/objectinformatieobject_partial_update">Gedeeltelijk</a> bijwerken van een Objectinformatieobject</li>
</ul></td>
</tr>
<tr class="odd">
<td>Gegevens</td>
<td>Objecttype OBJECTINFORMATIEOBJECT, inclusief relatie naar OBJECT en ENKELVOUDIGINFORMATIEOBJECT.<br/>
https://www.gemmaonline.nl/index.php/Rgbz_2.0/doc/relatieklasse/zaak-informatieobject</td>
</tr>
<tr class="even">
<td>OAS-specificaties</td>
<td><a href="https://documenten-api.vng.cloud/api/v1/schema/#tag/objectinformatieobjecten">https://documenten-api.vng.cloud/api/v1/schema/#tag/objectinformatieobjecten</a></td>
</tr>
<tr class="odd">
<td>Bijzonderheden</td>
<td>
<ul>
<li>Het verwijderen van Objectinformatieobjecten wordt nog niet ondersteund.</li>
</ul>
</td>
</tr>
</tbody>
</table>
