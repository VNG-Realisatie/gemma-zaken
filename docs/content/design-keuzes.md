# Designkeuzes

## API endpoints gebruiken UUID4 voor parameters

De paden van API endpoints bevatten referenties naar de objecten in de
achterliggende datastore. Deze parameters zouden semantisch kunnen ingevuld
worden, zoals gebruikmaken van bronorganisatie en zaakidentificatie voor een
zaak. Echter, na analyse blijkt dat dit lastig consequent toe te passen is
doorheen de API.

Daarom is beslist om gebruik te maken van UUID (type 4) voor deze parameters.
De motivatie is dat deze:

* uniciteit garandeert, ook over meerdere systemen heen
* geen volgordelijkheid/database IDs lekt
* volgt de DSO API-richtlijnen
