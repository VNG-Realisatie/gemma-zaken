# Gemeente Haarlem - aanvraag ontheffing Straatartiest

In dit hoofdstuk wordt een architectuurschets gegeven voor de user stories voor de aanvraag van een ontheffing voor straatartiesten. Het gaat om de volgende user stories.

## User stories

* [Userstory #171](https://github.com/VNG-Realisatie/gemma-zaken/issues/171): Als behandelaar wil ik een document toevoegen aan de zaak zodat ik mijn dossiervorming op orde heb
* [Userstory #164](https://github.com/VNG-Realisatie/gemma-zaken/issues/164): Als straatartiest wil ik dat mijn aanvraag een uniek volgnummer krijgt zodat ik in mijn communicatie snel kan verwijzen naar mijn aanvraag
* [Userstory #163](https://github.com/VNG-Realisatie/gemma-zaken/issues/163): Als gemeente wil ik dat de aanvraag van een straatoptreden als zaak wordt gecreëerd zodat ik mijn dossiervorming op orde is en de voortgang transparant is
* [Userstory #162](https://github.com/VNG-Realisatie/gemma-zaken/issues/162): Als gemeente wil ik dat een het genomen besluit voor de aanvraag voor een straat optreden wordt toegevoegd aan de zaak zodat het besluit door alle betrokkenen inzichtelijk is
* [Userstory #161](https://github.com/VNG-Realisatie/gemma-zaken/issues/161): Als gemeente wil ik de aanvraag van een straatoptreden kunnen afronden zodat het dossier en status afgesloten kan worden

## Toelichting user stories
Het betreft een proces voor de frontoffice medewerker ter ondersteuning bij de aanvraag van een ontheffing voor straatartiesten. In het formulier worden bepaalde gegevens van de straatartiest gevraagd waarbij automatisch een kwartaal of jaar ontheffing wordt gegenereerd. De ..

## Architectuurschets

## Beknopte Procesbeschrijving

## Generieke architectuurschets (GEMMA-referentiecomponenten)
Architectuurschetsen zijn reeds in termen van GEMMA 2 referentiecomponenten.

## Benodigde APIs per user story

| User story | API | Functionaliteit |
|:------------|:-----|:-----------------|
| [Userstory #171](https://github.com/VNG-Realisatie/gemma-zaken/issues/171): Als behandelaar wil ik een document toevoegen aan de zaak zodat ik mijn dossiervorming op orde heb| ZRC, DRC en ZTC| (GenereerInformatieobject identifcatie) > ... id terug (Informatieobject) zaakid, informatieobjectid, omschrijving, creatiedatum, titel, beschrijving, formaat, taal, versie, status, vertrouwlijkheidsaanduiding, auteur, inhoud.|
[Userstory #164](https://github.com/VNG-Realisatie/gemma-zaken/issues/164): Als straatartiest wil ik dat mijn aanvraag een uniek volgnummer krijgt zodat ik in mijn communicatie snel kan verwijzen naar mijn aanvraag| ZRC | Geen mapping nodig: uniek zaakid ontvangen | 
[Userstory #163](https://github.com/VNG-Realisatie/gemma-zaken/issues/163): Als gemeente wil ik dat de aanvraag van een straatoptreden als zaak wordt gecreëerd zodat ik mijn dossiervorming op orde is en de voortgang transparant is | ZRC, DRC en ZTC | creeerZaak -> (rgbz_zaak) zaakidentificatie, omschrijving, toelichting, startdatum, (rgbz_zaaktype) zaaktypeidentificatie | (rgbz_natuurlijkpersoon) burgerservicenummer, naam_geslachtsnaam, naam_aanschrijving_voorletters_aanschrijving, naam_voorvoegsel_geslachtsnaam_voorvoegsel, geboortedatum_ingeschreven_persoon|
[Userstory #162](https://github.com/VNG-Realisatie/gemma-zaken/issues/162): Als gemeente wil ik dat een het genomen besluit voor de aanvraag voor een straat optreden wordt toegevoegd aan de zaak zodat het besluit door alle betrokkenen inzichtelijk is | ZRC en ZTC | genereerBesluitIdentificatie -> ... voegBesluitToe -> (rgbz_besluittype) besluittypeomschrijving; (rgbz_besluit) besluitdatum, besluittoelichting, ingangsdatum, vervaldatum, vervalreden|
[Userstory #161](https://github.com/VNG-Realisatie/gemma-zaken/issues/161): Als gemeente wil ik de aanvraag van een straatoptreden kunnen afronden zodat het dossier en status afgesloten kan worden | ZRC en ZTC | zaakidentificatie, (rgbz_statustype) statustypevolgnummer, statustypeomschrijving (rgbz_zaak) resultaatomschrijving, resultaattoelichting||
