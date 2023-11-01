---
title: "Productvisie API's voor Zaakgericht Werken"
date: '1-11-2023'
weight: 100
layout: page-with-side-nav
---
#Productvisie

## Doel van de productvisie
De productvisie beschrijft het toepassingsgebied van de standaard en het onderliggende informatiemanagementsarchitectuur. Het beschrijven van de werkwijze van ontwikkelteams, de transitiemogelijkheden om van oud naar nieuw te komen etc. vallen buiten scope van de productvisie.

## Wat is Zaakgericht werken?
In het katern [zaakgericht werken](https://www.gemmaonline.nl/index.php/GEMMA_2_Katern_Zaakgericht_Werken) staat de volgende definitie van zaakgericht werken beschreven:

> Zaakgericht werken is een verbijzondering van procesgericht werken.

> Procesgericht werken is het ‘resultaatgericht en structureel besturen, bewaken, uitvoeren en verbeteren van processen’. Dit gebeurt over afdelingsgrenzen heen, in functie van het resultaat van een bedrijfsproces, meestal een product of dienst dat aan een klant wordt geleverd. Procesmatig werken is dus meer dan enkel processen identificeren en beschrijven; het impliceert ook dat deze processen de basis vormen van de sturing van de organisatie; met onder meer als doel om efficiency en effectiviteit te verhogen.

> Er is veel literatuur over procesgericht werken en procesmanagement. Een populaire methodiek binnen gemeenten is de LEAN-methodiek, waarbij activiteiten in processen worden bekeken naar hun bijdrage in de waarde voor de klant. Activiteiten zonder toegevoegde waarde worden geschrapt.

> In de context van BPM zijn er verschillende standaarden voor het modelleren en/of uitvoeren van processen.[7]. Deze definiëren hoe processtappen, keuzemomenten en flows gemodelleerd moeten worden. Ze beschrijven echter geen uniform formaat[8] –zoals ‘zaak’- om de informatie betreffende en betrokken in het proces te modelleren. Dit wordt overgelaten aan de informatiesystemen zelf, bijvoorbeeld dmv globale variabelen, applicatiespecifieke tabellen, etc.


> Zaakgericht werken gedefinieerd

> Zaakgericht werken gaat dus over het uitvoeren van bedrijfsprocessen waarbij informatie die tijdens het proces is ontvangen of gecreëerd, 'zaakinformatie', tijdens het proces wordt gebundeld bij een zaak. Deze zaakinformatie tesamen vormt dus een 'zaakdossier'[9]. Dit bevat meer dan enkel documenten. Ook andere informatieobjecten als statussen, betrokkenen etc. maken deel uit van het zaakdossier. Een zaakdossier is dus een gestandaardiseerd informatieobject waarin, ongeacht het bijbehorende proces, inhoudelijke informatie en procesinformatie op een gestandaardiseerde manier kan worden geregistreerd en ontsloten.

## Wat is zaakgericht werken niet?
Zaakgericht werken is ieder geval niet:
- Verplicht werken in een generiek zaaksysteem
- Alles op dezelfde manier afhandelen met één generiek bedrijfsproces
- Een strak keurslijf waar geen ruimte is voor keuzemomenten

Taken 

## Doel van de API standaard
Bedrijfsprocessen worden afgehandeld in afhandelapplicaties. Dit kunnen hooggespecialiseerde taakspecifieke afhandelapplicaties zijn maar ook generieke afhandelapplicaties waarin releatief eenvoudige processen ingericht zijn. Om de zaakinformatie, het zaakdossier, zoals hierboven beschreven te kunnen ontsluiten wordt deze verzameld in een zaakregistratie en documentregistratie.

In de klassieke silo-gebaseerde software vormt het zaaksysteem een afslag van de zaakinformatie zoals deze in de afhandelapplicaties leeft. Door de verschillende manieren van omgaan met deze afslag en het synchroniseren van zaakinformatie kan deze zaakinformatie per bedrijfsproces verschillen qua actualiteit en compleetheid. Door zaakinformatie als gezamelijke bron te ontsluiten kan deze actualiteit en compleetheid wel geboden worden.

De API standaard voor Zaakgericht werken heeft als doel deze registratie en het ontsluiten van de gegevens mogelijk te maken op een leveranciersonafhankelijke manier. Afhandelapplicaties van verschillende leveranciers kunnen met de API standaard zaakinformatie opslaan in registraties van dezelfde of andere leveranciers. 

## Opzet van de API standaard
Het is niet noodzakelijk dat de verschillende registraties door hetzelfde systeem ingevuld worden. Daarom is de API standaard voor Zaakgericht werken opgesplitst in vier "domeinen", aparte registraties met elk een eigen API standaard. Deze vier domeinen zijn:

- Zaken
- Documenten
- Besluiten
- Zaaktype Catalogus

De interactie tussen deze vier domeinen is beschreven in de standaard. 

## Toepassing van de API standaard
Zoals hierboven geschetst dient de API standaard om zaakinformatie in de betrokken registraties op te kunnen slaan en op te kunnen vragen. In die zin moet de API standaard voor Zaakgericht werken gezien worden als API standaard voor Zaakgericht registreren. De standaard schrijft niet voor hoe bedrijfsprocessen moeten verlopen maar maakt mogelijk dat zaakinformatie op een eenduidige manier procesonafhankelijk opgeslagen en geraadpleegd kan worden.
