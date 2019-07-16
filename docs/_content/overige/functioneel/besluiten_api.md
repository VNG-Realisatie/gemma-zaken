---
title: "Besluiten-API"
date: '21-01-2019'
---

# BESLUITEN API

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
<td>Het kunnen aanspreken van een voorziening voor het onderhouden en raadplegen van Besluiten inclusief relaties naar informatieobjecten.</td>
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
<td><a href=""><span class="underline">Besluitregistratiecomponent</span></a> (GEMMA2)</td>
</tr>
<tr class="even">
<td>Consumer</td>
<td>Componenten waarmee Besluiten beheerd worden en (andere) componenten die besluiten raadplegen.</td>
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
<td><a href="https://besluiten-api.vng.cloud/api/v1/schema/"><span class="underline">https://besluiten-api.vng.cloud/api/v1/schema/</span></a></td>
</tr>
<tr class="even">
<td>Bijzonderheden</td>
<td></td>
</tr>
</tbody>
</table>

Deze API omvat de navolgende resources (‘bronnen’) en de daarvan beschreven mogelijkheden.

### Resource: Besluiten

<table>
<tbody>
<tr class="odd">
<td><strong>Aspect</strong></td>
<td><strong>Beschrijving</strong></td>
</tr>
<tr class="even">
<td>Doel</td>
<td><ul>
<li><a href="https://besluiten-api.vng.cloud/api/v1/schema/#operation/besluit_list">Opvragen</a> van een overzicht van alle beschikbare besluiten.</li>
<li><a href="https://besluiten-api.vng.cloud/api/v1/schema/#operation/besluit_read">Opvragen</a> van de details van een specifiek besluit.</li>
<li><a href="https://besluiten-api.vng.cloud/api/v1/schema/#operation/besluit_create">Aanmaken</a> van een besluit.</li>
<li><a href="https://besluiten-api.vng.cloud/api/v1/schema/#operation/besluit_update">Bijwerken</a> van een besluit.</li>
<li><a href="https://besluiten-api.vng.cloud/api/v1/schema/#operation/besluit_partial_update">Gedeeltelijk bijwerken</a> van een besluit.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Gegevens</td>
<td><p>Objecttype BESLUIT.<br/>https://www.gemmaonline.nl/index.php/Rgbz_2.0/doc/objecttype/besluit</td>
</tr>
<tr class="even">
<td>OAS-specificaties</td>
<td><a href="https://besluiten-api.vng.cloud/api/v1/schema/#tag/besluiten">https://besluiten-api.vng.cloud/api/v1/schema/#tag/besluiten</a></td>
</tr>
<tr class="odd">
<td>Bijzonderheden</td>
<td><ul>
<li>Het verwijderen van Besluiten wordt nog niet ondersteund.</li>
</ul></td>
</tr>
</tbody>
</table>

### Resource: Besluitinformatieobjecten

<table>
<tbody>
<tr class="odd">
<td><strong>Aspect</strong></td>
<td><strong>Beschrijving</strong></td>
</tr>
<tr class="even">
<td>Doel</td>
<td><ul>
<li><a href="https://besluiten-api.vng.cloud/api/v1/schema/#operation/besluitinformatieobject_list">Opvragen</a> van een overzicht van alle beschikbare besluiteninformatieobjecten.</li>
<li><a href="https://besluiten-api.vng.cloud/api/v1/schema/#operation/besluitinformatieobject_read">Opvragen</a> van de details van een specifiek besluitinformatieobject.</li>
<li><a href="https://besluiten-api.vng.cloud/api/v1/schema/#operation/besluitinformatieobject_create">Aanmaken</a> van een besluitinformatieobject.</li>
<li><a href="https://besluiten-api.vng.cloud/api/v1/schema/#operation/besluitinformatieobject_update">Bijwerken</a> van een besluitinformatieobject.</li>
<li><a href="https://besluiten-api.vng.cloud/api/v1/schema/#operation/besluitinformatieobject_partial_update">Gedeeltelijk bijwerken</a> van een besluitinformatieobject.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Gegevens</td>
<td><p>Relatiesoort BESLUIT kan vastgelegd zijn als INFORMATIEOBJECT.<br/>https://www.gemmaonline.nl/index.php/Rgbz_2.0/doc/relatiesoort/besluit.kan_vastgelegd_zijn_als_informatieobject</td>
</tr>
<tr class="even">
<td>OAS-specificaties</td>
<td><a href="https://besluiten-api.vng.cloud/api/v1/schema/#tag/besluiten">https://besluiten-api.vng.cloud/api/v1/schema/#tag/besluiten</a></td>
</tr>
<tr class="odd">
<td>Bijzonderheden</td>
<td><ul>
<li>Het verwijderen van Besluitinformatieobjecten wordt nog niet ondersteund.</li>
</ul></td>
</tr>
</tbody>
</table>
