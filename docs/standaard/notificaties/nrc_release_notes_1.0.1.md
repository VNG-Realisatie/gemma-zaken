---
title: "Notificaties API"
weight: 10
layout: page-with-side-nav
---

# Release notes Notificaties API 1.0.1

## MaxLength restrictie verwijderd van twee velden

De maximale lengte restrictie verwijderd van "auth" en "callbackUrl" omdat deze velden te klein zijn (zie [commit](https://github.com/VNG-Realisatie/gemma-zaken/commit/d074f5f92d19072cde88358f4e4f5f45247cdf7f)).

Gerelateerde issues:

- NRC: grootte van het auth-veld (abonnement_create) met 1000 characters is te klein [#2571](https://github.com/VNG-Realisatie/gemma-zaken/issues/2571)