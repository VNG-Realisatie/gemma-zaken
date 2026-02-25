---
title: "Notificaties API"
weight: 10
layout: page-with-side-nav
---

# Release notes Notificaties API 1.0.1

In de Notificaties API 1.0.1 zijn de volgende issues verwerkt:

- [Issuelijst Milestone "ZGW 1.6.0" voor Notificaties API 1.0.1](https://github.com/VNG-Realisatie/gemma-zaken/issues?q=is%3Aissue%20state%3Aopen%20milestone%3A%22ZGW%201.6%22%20label%3Anotificatie-api)

## MaxLength restrictie verwijderd van twee velden

De maximale lengte restrictie is verwijderd van "auth" en "callbackUrl" omdat deze velden te klein zijn (zie [commit](https://github.com/VNG-Realisatie/gemma-zaken/commit/d074f5f92d19072cde88358f4e4f5f45247cdf7f)).

Gerelateerde issues:

- [#2571](https://github.com/VNG-Realisatie/gemma-zaken/issues/2571) NRC: grootte van het auth-veld (abonnement_create) met 1000 characters is te klein.