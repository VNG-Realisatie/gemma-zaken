
# Userstory's Gemeente Utrecht

##Userstory beschrijving  userstory [Als gemeente Utrecht wil ik de documenten die opgeslagen worden via de DRC op kunnen slaan in ons gemeentelijk DMS #506](https://github.com/VNG-Realisatie/gemma-zaken/issues/506)

**Beschrijving**
Als gemeenten willen we functionaliteit 1 keer realiseren en vervolgens hergebruiken. Zo ook DMS functionaliteit. De documentregistratiecomponent moet daarom kunnen aansluiten op bestaande DMS oplossingen. Het aansluiten van de documentregistratiecomponent op een DMS kan via de open internationale standaard CMIS. Onder andere Alfresco (ook open source), wat veel gebruikt wordt bij gemeenten, ondersteunt de CMIS standaard.

**Gewenste aanvulling op de APi:**
De mogelijkheid om documenten/informatieobjecten inclusief de metatada van het document middels CMIS op te slaan en te benaderen in een DMS. In de API moet de mogelijkheid bestaan om aan te geven op welke manier informatieobjecten opgeslagen moeten worden:
- In een standaard database + losse bestandsopslag
- In een DMS op basis van CMIS

**Voorstel voor implementatie in referentie component:**
Implementatie op basis van een Alfresco DMS. Reden: Alfresco wordt al veel gebruikt bij verschillende gemeenten, is ook open source en ondersteunt het CMIS protocol.

**Architectuurbeschrijving**
De DRC slaat de documenten op in een Alfresco DMS. Voor de communicatie tussen DRC en DMS wordt het CMIS protocol gebruikt.
(https://github.com/VNG-Realisatie/gemma-zaken/blob/master/docs/archief/processen/bestanden/Utrecht/DRC-DMS.PNG)
