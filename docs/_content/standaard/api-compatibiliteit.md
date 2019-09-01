---
title: "API-compatibiliteit"
date: '19-06-2019'
---

Elke API-specificatie heeft zijn eigen versie, wat voor
compatibiliteitsproblemen kan zorgen bij het combineren van APIs.

We vatten hier samen welke versies van APIs compatibel zijn met welke versies
van andere APIs. Indien er in een cel geen range (`x.y.z` - `u.w.v`) opgegeven is 
maar een enkele waarde (`x.y.z`), dan betreft het de minimale versie van een API. 
Een lege cel betekent dat de waarde gelijk is aan de daarboven gelegen cel.


## Autorisaties API (AC)

| Eigen versie      | NRC     | ZRC | DRC | ZTC | BRC |
|-------------------|---------|-----|-----|-----|-----|
| `0.2.x` - `0.3.x` | `0.5.x` | -   | -   | -   | -   |
| `0.4.x`           | `0.8.1` |     |     |     |     |
| `1.0.0`           | `1.0.0` |     |     |     |     |


## Notificaties API (NRC)

| Eigen versie      | AC      | ZRC | DRC | ZTC | BRC |
|-------------------|---------|-----|-----|-----|-----|
| `0.6.0` - `0.7.x` | `0.2.3` | -   | -   | -   | -   |
| `0.8.1`           | `0.4.0` |     |     |     |     |
| `1.0.0`           | `1.0.0` |     |     |     |     |


## Zaken API (ZRC)

| Eigen versie | AC      | NRC     | DRC      | ZTC      | BRC      |
|--------------|---------|---------|----------|----------|----------|
| `0.17.0`     | `0.2.3` | `0.6.0` | `0.13.0` | `0.11.1` | `0.11.1` |
| `0.18.0`     |         |         | `0.15.0` |          |          |
| `0.21.0`     | `0.4.0` | `0.8.1` | `0.17.0` | `0.16.1` | `0.12.1` |
| `1.0.0`      | `1.0.0` | `1.0.0` | `1.0.0`  | `1.0.0`  | `1.0.0`  |


## Documenten API (DRC)

| Eigen versie | AC       | NRC      | ZRC       | ZTC       | BRC       |
|--------------|----------|----------|-----------|-----------|-----------|
| `0.14.0`     | `0.2.3`  | `0.6.0`  | `0.17.0`  | `0.10.0`  | `0.11.3`  |
| `0.17.0`     | `0.4.0`  | `0.8.1`  | `0.21.0`  | `0.16.1`  | `0.12.1`  |
| `1.0.0`      | `1.0.0`  | `1.0.0`  | `1.0.0`   | `1.0.0`   | `1.0.0`   |


## Catalogi API (ZTC)

| Eigen versie | AC       | NRC      | ZRC | DRC | BRC |
|--------------|----------|----------|-----|-----|-----|
| `0.14.0`     | `0.2.3`  | `0.6.0`  | -   | -   | -   |
| `0.16.1`     | `0.4.0`  | `0.8.1`  |     |     |     |
| `1.0.0`      | `1.0.0`  | `1.0.0`  |     |     |     |


## Besluiten API (BRC)

| Eigen versie | AC       | NRC      | ZRC       | DRC       | ZTC      |
|--------------|----------|----------|-----------|-----------|----------|
| `0.11.1`     | `0.2.3`  | `0.6.0`  | `0.16.0`  | `0.14.0`  | `0.2.0`  |
| `0.12.1`     | `0.4.0`  | `0.8.1`  | `0.21.0`  | `0.17.0`  | `0.16.1` |
| `1.0.0`      | `1.0.0`  | `1.0.0`  | `1.0.0`   | `1.0.0`   | `1.0.0`  |
