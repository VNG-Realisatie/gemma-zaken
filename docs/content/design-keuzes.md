# Designkeuzes
12345678901234567890123456789012345678901234567890123456789012345678901234567890
## API endpoints gebruiken UUID4 als ID-parameter voor het opvragen van een enkel object

De ID-parameter, hieronder aangeduid met `{id}` wordt gebruikt om via de URL 
een enkel object van een bepaald type resource te vinden. Bijvoorbeeld een 
`Zaak`:

|URL|Voorbeeld|
|---|---|
| `https://www.example.com/zaken/{id}/`|`https://www.example.com/zaken/550e8400-e29b-41d4-a716-446655440000/`|

Een [UUID (versie 4)] is in de praktijk altijd uniek, zonder dat deze centraal 
hoeft te worden bijgehouden. Deze keuze laat overlet de mogelijkheid om op
andere manieren bij een enkel object te komen, zoals op een combinatie van 
velden die samen uniek zijn, zoals `bronorganisatie` en `zaakidentificatie`:
`https://www.example.com/zaken/?bronorganisatie=0329&zaakidentificatie=MOR-0000001`

*Achtergrond*

De paden van API endpoints bevatten referenties naar de objecten in de
achterliggende datastore. Deze parameters zouden semantisch kunnen ingevuld
worden, zoals gebruikmaken van `bronorganisatie` en `zaakidentificatie` voor
een zaak. Echter, na analyse blijkt dat dit lastig consequent toe te passen is
door de hele de API heen. Tevens wekt het de indruk dat dat deze parameters 
genoeg zijn om een Zaak te vinden maar dat is niet correct. De volledige URL is
nodig voor het opvragen van een enkele Zaak.

Daarom is beslist om gebruik te maken van [UUID (versie 4)] voor deze 
parameters. De motivatie is verder dat deze:

* uniciteit garandeert, ook over meerdere systemen heen;
* geen volgordelijkheid/database IDs lekt;
* de DSO API-richtlijnen volgt;
* semantisch bevragen niet onmogelijk maakt.

[UUID (versie 4)]: https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)
