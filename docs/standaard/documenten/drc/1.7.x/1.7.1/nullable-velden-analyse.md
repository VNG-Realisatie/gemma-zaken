# Analyse nullable velden in OpenAPI specificatie DRC 1.7.1

**Datum**: 2026-07-29  
**Bestand**: openapi.yaml (DRC 1.7.1)

## Samenvatting

In de OpenAPI specificatie komen **95 keer** `nullable: true` voor. De manier waarop null wordt beschreven is **inconsistent** en valt in verschillende categorieën.

## Categorieën

### 1. ✅ Nullable met expliciete uitleg

Deze velden leggen duidelijk uit wanneer `null` gebruikt wordt:

#### `isGereedVoorPublicatie`
```yaml
description: >-
  Geeft aan of het INFORMATIEOBJECT gereed is voor publicatie. Dit
  veld mag `null` zijn om aan te geven dat de gereedheid voor
  publicatie nog niet bekend is.
type: boolean
nullable: true
```

#### `indicatieGebruiksrecht`
```yaml
description: >-
  Indicatie of er beperkingen gelden aangaande het gebruik van het
  informatieobject anders dan raadpleging. Dit veld mag `null` zijn om
  aan te geven dat de indicatie nog niet bekend is. Als de indicatie
  gezet is, dan kan je de gebruiksrechten die van toepassing zijn
  raadplegen via de GEBRUIKSRECHTen resource.
type: boolean
nullable: true
```

### 2. ❌ Nullable zonder uitleg

Deze velden hebben `nullable: true` maar geven **geen uitleg** over wat null betekent:

| Veld | Type | Beschrijving |
|------|------|--------------|
| `inhoud` | string (uri/byte) | "Download URL van de binaire inhoud." of "Binaire inhoud, in base64 geëncodeerd." |
| `bestandsomvang` | integer | "Aantal bytes dat de inhoud van INFORMATIEOBJECT in beslag neemt." |
| `link` | string (uri) | "De URL waarmee de inhoud van het INFORMATIEOBJECT op te vragen is." |
| `faxnummer` | string | "faxnummer van de ontvanger of afzender." |
| `emailadres` | string | "emailadres van de ontvanger of afzender." |
| `telefoonnummer` | string | "telefoonnummer van de ontvanger of afzender." |
| `einddatum` | string (date-time) | "Einddatum van de periode waarin de gebruiksrechtvoorwaarden van toepassing zijn." |

### 3. ⚠️ Nullable met impliciete uitleg

Deze velden hebben context die suggereert wanneer null gebruikt wordt, maar maken het niet expliciet:

#### `ontvangstdatum` / `verzenddatum` (EnkelvoudigInformatieObject - DEPRECATED)
```yaml
description: >-
  <b>DEPRECATED</b> Dit attribuut is verplaatst naar resource
  Verzending. De datum waarop het INFORMATIEOBJECT ontvangen is.
  Verplicht te registreren voor INFORMATIEOBJECTen die van buiten de
  zaakbehandelende organisatie(s) ontvangen zijn. [...]
nullable: true
```
**Implicatie**: null wanneer niet ontvangen van buiten, maar dit wordt niet expliciet gezegd.

#### `ontvangstdatum` / `verzenddatum` (Verzending)
```yaml
description: >-
  De datum waarop het INFORMATIEOBJECT ontvangen is. Verplicht te
  registreren voor INFORMATIEOBJECTen die van buiten de
  zaakbehandelende organisatie(s) ontvangen zijn. [...]
  Vervangt het gelijknamige attribuut uit Informatieobject.
  Verplicht gevuld wanneer aardRelatie de waarde 'afzender' heeft.
nullable: true
```
**Implicatie**: null in andere gevallen, maar niet expliciet vermeld.

### 4. 📦 Nullable op object-niveau

Complete objecten die nullable zijn:

#### `Ondertekening`
```yaml
description: >-
  Aanduiding van de rechtskracht van een informatieobject. Mag niet
  van een waarde zijn voorzien als de `status` de waarde 'in
  bewerking' of 'ter vaststelling' heeft.
nullable: true
```
**Uitleg aanwezig**: Beschrijft wanneer het object NIET aanwezig mag zijn (dus impliciet wanneer het null is).

#### `Integriteit`
```yaml
description: >-
  Uitdrukking van mate van volledigheid en onbeschadigd zijn van
  digitaal bestand.
nullable: true
```
**Geen null-uitleg**: Onduidelijk wanneer null vs. aanwezig.

#### Adres-objecten (`binnenlandsCorrespondentieadres`, `buitenlandsCorrespondentieadres`, `correspondentiePostadres`)
```yaml
description: >-
  Het correspondentieadres, betreffende een adresseerbaar object, van
  de BETROKKENE, zijnde afzender of geadresseerde, zoals vermeld in
  het ontvangen of verzonden INFORMATIEOBJECT indien dat afwijkt van
  het reguliere binnenlandse correspondentieadres van BETROKKENE.
nullable: true
```
**Implicatie**: null = niet afwijkend van regulier adres.

### 5. 🤔 Speciale gevallen

#### `inhoudIsVervallen` - Tegenstrijdigheid
```yaml
description: >-
  Geeft aan of de inhoud van het INFORMATIEOBJECT al dan niet 
  vervallen, dus niet langer geldig is.
  
  * `true` De inhoud van het INFORMATIEOBJECT is vervallen.
  * `false` De inhoud van het INFORMATIEOBJECT is niet vervallen.
type: boolean
nullable: true
```

**Probleem**: Legt `true` en `false` uit met bullet points, maar **zegt niets over `null`** terwijl het wel nullable is! Dit is een inconsistentie.

## Conclusie

**De null waarde wordt NIET consistent beschreven:**

- ✅ **2 velden** hebben expliciete null-documentatie
- ❌ **~70+ velden** hebben helemaal geen uitleg over null
- ⚠️ **~10 velden** hebben impliciete hints over null
- 🤔 **1 veld** (`inhoudIsVervallen`) heeft een tegenstrijdigheid

## Aanbevelingen voor verbetering

Voor consistentie zou elk nullable veld een van deze patronen moeten volgen:

### Patroon A: Expliciete null-uitleg (aanbevolen voor de meeste velden)

```yaml
description: >-
  [Beschrijving van het veld]. Dit veld mag `null` zijn om aan te geven 
  dat [specifieke situatie waarin null voorkomt].
nullable: true
```

**Voorbeeld voor `bestandsomvang`:**
```yaml
description: >-
  Aantal bytes dat de inhoud van INFORMATIEOBJECT in beslag neemt.
  Dit veld mag `null` zijn als de bestandsomvang nog niet bekend is
  of als het INFORMATIEOBJECT via een `link` wordt ontsloten.
nullable: true
```

### Patroon B: Tri-state boolean met volledige uitleg

```yaml
description: >-
  [Beschrijving van het veld].
  
  * `true` - [Betekenis van true]
  * `false` - [Betekenis van false]  
  * `null` - [Betekenis van null, bijv. "nog niet bekend" of "niet van toepassing"]
nullable: true
```

**Voorbeeld voor `inhoudIsVervallen`:**
```yaml
description: >-
  Geeft aan of de inhoud van het INFORMATIEOBJECT al dan niet 
  vervallen, dus niet langer geldig is.
  
  * `true` - De inhoud van het INFORMATIEOBJECT is vervallen.
  * `false` - De inhoud van het INFORMATIEOBJECT is niet vervallen.
  * `null` - Het is (nog) niet bekend of de inhoud vervallen is.
nullable: true
```

### Patroon C: Voor nested objecten

```yaml
description: >-
  [Beschrijving van het object]. Dit veld is `null` wanneer 
  [specifieke situatie, bijv. "er geen ondertekening heeft plaatsgevonden"].
nullable: true
```

## Prioriteit voor verbetering

1. **Hoog**: `inhoudIsVervallen` - Fix tegenstrijdigheid tussen bullet points en nullable
2. **Hoog**: Veelgebruikte velden zoals `inhoud`, `bestandsomvang`, `link` - Verduidelijk null-semantiek
3. **Middel**: Contactgegevens (`emailadres`, `telefoonnummer`, `faxnummer`) - Verduidelijk wanneer null
4. **Middel**: `Integriteit` object - Verduidelijk wanneer null vs. aanwezig
5. **Laag**: DEPRECATED velden (`ontvangstdatum`, `verzenddatum` in EnkelvoudigInformatieObject) - Kan blijven zoals het is gezien deprecated status

## Statistieken

- **Totaal nullable velden**: 95
- **Met expliciete null-documentatie**: 2 (2%)
- **Zonder null-uitleg**: ~70 (74%)
- **Met impliciete hints**: ~10 (11%)
- **Tegenstrijdige documentatie**: 1 (1%)
- **Object-level nullable**: ~12 (13%)

---

## Toegepaste oplossing

### Oplossing voor `inhoudIsVervallen` (Categorie 5 - Speciale gevallen)

**Datum uitgevoerd**: 2026-07-29

#### Probleem
Het veld `inhoudIsVervallen` had een tegenstrijdigheid in de documentatie:
- Het veld was gemarkeerd als `nullable: true`
- De beschrijving bevatte bullet points voor `true` en `false`
- Er was **geen bullet point voor `null`**, wat de documentatie onvolledig en tegenstrijdig maakte

Dit kwam voor in **6 schema's**:
1. `EnkelvoudigInformatieObject`
2. `EnkelvoudigInformatieObjectCreateLock`
3. `EnkelvoudigInformatieObjectCreateLockRequest`
4. `EnkelvoudigInformatieObjectWithLock`
5. `EnkelvoudigInformatieObjectWithLockRequest`
6. `PatchedEnkelvoudigInformatieObjectWithLockRequest`

#### Oplossing
De beschrijving is bijgewerkt volgens **Patroon B** (tri-state boolean met volledige uitleg).

**Voor:**
```yaml
inhoudIsVervallen:
  description: >-
    Geeft aan of de inhoud van het INFORMATIEOBJECT al dan niet 
    vervallen, dus niet langer geldig is.

    * `true` De inhoud van het INFORMATIEOBJECT is vervallen.

    * `false` De inhoud van het INFORMATIEOBJECT is niet vervallen.
  title: inhoud is vervallen
  type: boolean
  nullable: true
```

**Na:**
```yaml
inhoudIsVervallen:
  description: >-
    Geeft aan of de inhoud van het INFORMATIEOBJECT al dan niet 
    vervallen, dus niet langer geldig is.

    * `true` - De inhoud van het INFORMATIEOBJECT is vervallen.

    * `false` - De inhoud van het INFORMATIEOBJECT is niet vervallen.

    * `null` - Het is (nog) niet bekend of de inhoud van het INFORMATIEOBJECT vervallen is.
  title: inhoud is vervallen
  type: boolean
  nullable: true
```

#### Wijzigingen
1. **Toegevoegd**: Bullet point voor `null` waarde met uitleg "Het is (nog) niet bekend of de inhoud van het INFORMATIEOBJECT vervallen is."
2. **Gestandaardiseerd**: Toegevoegd streepje (`-`) na de backticks voor consistentie (`* `true` -` i.p.v. `* `true``)
3. **Toegepast**: In alle 6 schema's waar dit veld voorkomt

#### Resultaat
✅ De tegenstrijdigheid is opgelost  
✅ Het veld volgt nu het aanbevolen Patroon B  
✅ API-consumenten hebben nu duidelijke documentatie over alle drie de mogelijke waarden  
✅ Consistentie tussen `nullable: true` en de beschrijving is hersteld

#### Technische implementatie
Gebruikt `sed` om alle 6 voorkomens in één actie bij te werken:
- Bestandslocatie: `docs/standaard/documenten/drc/1.7.x/1.7.1/openapi.yaml`
- Regelnummers: 6071, 6369, 6666, 6929, 7217, 7925
