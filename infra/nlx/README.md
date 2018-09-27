# NLx integratie & build tooling

Deze README beschrijft de tooling om de NLx inway en outways op te kunnen
zetten, in samenspel de referentieimplementaties.

## Opmerkingen

De public certificates voor NLx bevinden zich in de `./certificates` map.

De gebruikte organisatie in deze certificaten is `zds-nlx-demo`. Om de
containers uit te voeren heb je ook de private key nodig, die om
veiligheidsredenen NIET in versiecontrole zit.

## Docker images builden & pushen

### Outway

```bash
docker build . -f Dockerfile_outway -t vngr/nlx-outway:latest
docker push vngr/nlx-outway:latest
```

### Inway

```bash
docker build . -f Dockerfile_inway -t vngr/nlx-inway:latest
docker push vngr/nlx-inway:latest
```
