---
title: "Demo Sprint 6"
date: "22-11-2018"
---

Rotterdam, 22 november 2018

## Presentatie

- Opening (@Ehotting)
- Techniek sprint 6 (@sergei-maertens & @joeribekker)

## Slides:

- [Demo Spint 6.pdf](../bestanden/zds2-demo-sprint-6.pdf)

## Feedback en vragen

### Schrijven wij OpenID connect voor?

Op dit moment niet. We hebben (nog) geen behoefte om de identiteit van de eindgebruiker te kennen in
de APIs. Dit kan veranderen en dan bekijken we de OpenID standaard.

### Hoeveel scopes komen er?

Moeilijk te zeggen. Het bepalen van de scopes wordt conservatief aangepakt - we willen de
beheerslast beperken. We inspireren ons ook op bestaande permissiemodellen van leveranciers. Verdere
input van welke rollen/permissies bij leveranciers onderkend worden zijn welkom en waardevol!

We houden er rekening mee dat scopes ook gebundeld kunnen zijn - vb. Gmail kent een `gmail` scope
die alles toelaat, waar een 6-7-tal fijnere scopes onder vallen.

### Shared secret vs Asymmetrische key pair

Shared Secret heeft als nadeel dat de server zelf ook JWT's kan uitgeven alsof deze van de client
zouden komen. Misschien willen we dat als feature als een API met andere APIs moet communiceren (in
plaats van dat APIs bij elkaar bekend zijn).

Shared secret _klinkt_ vooral slecht - dezelfde beheerslast die met shared secret komt, geldt ook
voor assymetrische encryptie.

We houden het in gedachten, voor de techniek maakt het op dit moment niet veel uit, maar het is
low-prio.

### JWK ? als alternatief?

JWK lijkt compatibel met JWT. Moet verder onderzocht worden wat we ermee winnen en wat de tradeoff
is qua complexiteit.

### Toch limiet op (text) velden? Anders is je database de limiet.

Goeie opmerking, theoretisch gezien kan je inderdaad een request construeren die een
database/storage volledig doet vollopen puur met een tekstveld.

Echter, in de praktijk zul je lang daarvoor tegen de limitaties van webservers aanlopen die een
maximale grootte voor de request body opleggen. Voor `nginx` bijvoorbeeld is dit standaard 1MB.

Dit is op dit moment een grijs gebied, goede stof tot nadenken. Standaardiseren op minimaal
ondersteunde body-size lijkt ons beter dan arbitraire tekstlengtes op te leggen.

### Einddatum moet toch weer datumtijd worden? Soms is een hele zaak op 1 dag afgehandeld.

[#659](https://github.com/VNG-Realisatie/gemma-zaken/issues/659) aangemaakt.

### Einddatum leeg maken als status veranderd.

[#660](https://github.com/VNG-Realisatie/gemma-zaken/issues/660) aangemaakt.

### API lab: Wat gaan we doen?

Op het moment van schrijven is het API-lab voorbij, en er werd druk gekoppeld tussen verschillende
clients en providers!

### Cliënt beschikbaar?

Ja - demo applicatie, ook gehost en als Docker container bechikbaar.
