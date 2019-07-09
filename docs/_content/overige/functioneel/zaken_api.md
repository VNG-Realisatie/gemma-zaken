---
title: "Zaken-API"
date: '1-10-2018'
---

# ZAKEN API

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
<td><a href="https://www.gemmaonline.nl/index.php/GEMMA2/0.9/id-a97b6545-d5a7-485d-9b13-3ce22db5b9cf"><span class="underline">Zaakregistratiecomponent</span></a> (GEMMA2)</td>
</tr>
<tr class="even">
<td>Consumer</td>
<td>Componenten waarmee zaken behandeld worden (Zaakafhandelcomponenten; ZAC’s) en (andere) componenten die zaakgegevens raadplegen.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Informatiemodel</td>
<td><a href="https://www.gemmaonline.nl/images/gemmaonline/a/a4/EgIM_20180621_-_ag_4_-_GEMMA_RGBZ_2.0_-_CONCEPT_20180613.zip"><span class="underline">RGBZ, versie 2.00.02</span></a> (in-ontwikkeling)</td>
</tr>
<tr class="odd">
<td>API-specificaties</td>
<td><a href="https://zaken-api.vng.cloud/api/v1/schema"><span class="underline">https://zaken-api.vng.cloud/api/v1/schema</span></a></td>
</tr>
<tr class="even">
<td>Bijzonderheden</td>
<td>Het RGBZ wordt in meerdere API’s uitgewerkt. Zo wordt bijvoorbeeld de relatie van een Zaak met Informatieobjecten gelegd vanuit een op die Informatieobjecten gerichte API.<b/>
De versie van het RGBZ waarnaar verwezen wordt omvat meer dan hetgeen in deze API is uitgewerkt.<br/>
De hierboven beschreven doelen zijn nog niet volledig in deze versie van de API geimplementeerd.</td>
</tr>
</tbody>
</table>

Deze API omvat de navolgende resources (‘bronnen’) en de daarvan beschreven mogelijkheden.

### Resource: Zaken

<table>
<tbody>
<tr class="odd">
<td><strong>Aspect</strong></td>
<td><strong>Beschrijving</strong></td>
</tr>
<tr class="even">
<td>Doel</td>
<td><ul>
<li>Opvragen van een overzicht van alle beschikbare Zaken of Zaken van een zaaktype.</li>
<li>Opvragen van een overzicht van Zaken binnen een geo-contour (locatie), eventueel van een Zaaktype.</li>
<li>Opvragen van de gegevens van een specifieke Zaak.</li>
<li>Aanmaken van een Zaak en deze relateren aan het van toepassing zijnde Zaaktype.</li>
<li>Wijzigen van alle gegevens van een Zaak.</li>
<li>Wijzigen van enkele gegevens van een Zaak.</li>
<li>Opvragen van een overzicht van informatieobjecten bij een Zaak.</li>
<li>Relateren van een informatieobject aan een Zaak.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Gegevens</td>
<td><p>Objecttype ZAAK, inclusief relatie naar ZAAKTYPE.<br/>https://www.gemmaonline.nl/index.php/rgbz_2.0/doc/objecttype/zaak</td>
</tr>
<tr class="even">
<td>OAS-specificaties</td>
<td><a href="https://zaken-api.vng.cloud/api/v1/schema/#tag/zaken">https://zaken-api.vng.cloud/api/v1/schema/#tag/zaken</a></td>
</tr>
<tr class="odd">
<td>Bijzonderheden</td>
<td><ul>
<li>Het verwijderen van Zaken wordt nog niet ondersteund: Zaken kunnen wel beeindigd maar niet zomaar verwijderd worden, hooguit als ‘correctie’ of na verstrijken van de archiverings-vernietigingstermijn.</li>
<li>De relatie naar Zaaktype (cq. het Zaaktype van de Zaak) kan niet gewijzigd worden. Indien het Zaaktype onjuist blijkt te zijn, dient de Zaak beeindigd te worden en een nieuwe Zaak (met het juiste Zaakype) toegevoegd te worden.</li>
<li>De einddatum van de Zaak kan alleen opgevraagd worden. Muteren hiervan gebeurt in de resource: Statussen.</li>
<li>Het relateren van een Informatieobject aan een Zaak wordt aangestuurd vanuit de Documenten-API.</li>
</ul></td>
</tr>
</tbody>
</table>

### Resource: Zaakobjecten

<table>
<tbody>
<tr class="odd">
<td><strong>Aspect</strong></td>
<td><strong>Beschrijving</strong></td>
</tr>
<tr class="even">
<td>Doel</td>
<td><ul>
<li>Opvragen van een overzicht van Objecten bij een Zaak.</li>
<li>Opvragen van – de gegevens van - een specifiek Zaakobject die de relatie beschijft tussen een Object en een Zaak.</li>
<li>Relateren van een Object aan een Zaak d.m.v. het toevoegen van een Zaakobject.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Gegevens</td>
<td>Relatieklasse ZAAKOBJECT, inclusief relatie ‘ZAAK betreft OBJECT’.<br/>
https://www.gemmaonline.nl/index.php/rgbz_2.0/doc/relatieklasse/zaakobject</td>
</tr>
<tr class="even">
<td>OAS-specificaties</td>
<td><a href="https://zaken-api.vng.cloud/api/v1/schema/#tag/zaakobjecten">https://zaken-api.vng.cloud/api/v1/schema/#tag/zaakobjecten</a></td>
</tr>
<tr class="odd">
<td>Bijzonderheden</td>
<td><ul>
<li>Het verwijderen van Zaakobjecten wordt nog niet ondersteund. Overigens kunnen Zaakobjecten niet zomaar verwijderd worden, hooguit als ‘correctie’ of na verstrijken van de archiverings-vernietigingstermijn.</li>
<li>Het aanpassen van Zaakobjecten wordt nog niet ondersteund.</li>
</ul>
</td>
</tr>
</tbody>
</table>

### Klantcontacten

<table>
<tbody>
<tr class="odd">
<td><strong>Aspect</strong></td>
<td><strong>Beschrijving</strong></td>
</tr>
<tr class="even">
<td>Doel</td>
<td><ul>
<li>Opvragen van een overzicht van alle Klantcontacten met per Klantcontact enkele gegevens.</li>
<li>Opvragen van – de gegevens van - een specifiek Klantcontact.</li>
<li>Aanmaken van een Klantcontact en deze relateren aan een Zaak.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Gegevens</td>
<td>https://www.gemmaonline.nl/index.php/rgbz_2.0/doc/objecttype/klantcontact</td>
</tr>
<tr class="even">
<td>OAS-specificaties</td>
<td><a href="https://zaken-api.vng.cloud/api/v1/schema/#tag/klantcontacten">https://zaken-api.vng.cloud/api/v1/schema/#tag/klantcontacten</a></td>
</tr>
<tr class="odd">
<td>Bijzonderheden</td>
<td><ul>
<li>Het verwijderen van Klantcontacten wordt nog niet ondersteund. Overigens kunnen Klantcontacten niet zomaar verwijderd worden, hooguit als ‘correctie’ of na verstrijken van de archiverings-vernietigingstermijn.</li>
<li>Het aanpassen van Klantcontacten wordt nog niet ondersteund.</li>
</ul></td>
</tr>
</tbody>
</table>

### Resource: Rollen

<table>
<tbody>
<tr class="odd">
<td><strong>Aspect</strong></td>
<td><strong>Beschrijving</strong></td>
</tr>
<tr class="even">
<td>Doel</td>
<td><ul>
<li>Opvragen van een overzicht van alle Rollen, desgewenst bij een Zaak, bij een Betrokkene en/of van een bepaald generiek roltype met per rol enkele gegevens.</li>
<li>Opvragen van – de gegevens van - een specifieke Rol.</li>
<li>Aanmaken van een Rol en deze relateren aan een Zaak en een Betrokkene.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Gegevens</td>
<td>Relatieklasse ROL, inclusief relatie naar ZAAK. https://www.gemmaonline.nl/index.php/rgbz_2.0/doc/relatieklasse/rol</td>
</tr>
<tr class="even">
<td>OAS-specificaties</td>
<td><a href="https://zaken-api.vng.cloud/api/v1/schema/#tag/rollen">https://zaken-api.vng.cloud/api/v1/schema/#tag/rollen</a></td>
</tr>
<tr class="odd">
<td>Bijzonderheden</td>
<td><ul>
<li>Het verwijderen van Rollen wordt nog niet ondersteund. Overigens kunnen Rollen niet zomaar verwijderd worden, hooguit als ‘correctie’ of na verstrijken van de archiverings-vernietigingstermijn.</li>
<li>Het aanpassen van Rollen wordt nog niet ondersteund.</li>
</ul></td>
</tr>
</tbody>
</table>

### Resource: Statussen

<table>
<tbody>
<tr class="odd">
<td><strong>Aspect</strong></td>
<td><strong>Beschrijving</strong></td>
</tr>
<tr class="even">
<td>Doel</td>
<td><ul>
<li>Opvragen van een overzicht van alle Statussen, desgewenst bij een Zaak en/of van een bepaald Statustype, met de gegevens per Status.</li>
<li>Opvragen van – de gegevens van - een specifieke Status.</li>
<li>Aanmaken van een Status en deze relateren aan een Zaak en het Statustype.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Gegevens</td>
<td>Objecttype STATUS, inclusief relatie naar ZAAK en STATUSTYPE. https://www.gemmaonline.nl/index.php/rgbz_2.0/doc/objecttype/status</td>
</tr>
<tr class="even">
<td>OAS-specificaties</td>
<td><a href="https://zaken-api.vng.cloud/api/v1/schema/#tag/statussen">https://zaken-api.vng.cloud/api/v1/schema/#tag/statussen</a></td>
</tr>
<tr class="odd">
<td>Bijzonderheden</td>
<td><ul>
<li>Het verwijderen van Statussen wordt nog niet ondersteund. Overigens kunnen Statussen niet zomaar verwijderd worden, hooguit als ‘correctie’ of na verstrijken van de archiverings-vernietigingstermijn.</li>
<li>Het aanpassen van Statussen wordt nog niet ondersteund.</li>
<li>Wanneer een zaak een nieuwe status krijgt wordt een nieuwe Status aangemaakt en krijgt deze de meest actuele datumStatusGezet (incl. tijd). Tevens wordt het element ‘status’ bij de zaak (Zaken-resource) geupdate.</li>
<li>De huidige status van een zaak is de status met de meest actuele datumStatusGezet. Dit is tevens de waarde van het element ‘status’ in de Zaken-resource.</li>
</ul></td>
</tr>
</tbody>
</table>
