# ADR-validatieresultaten samenvatten

Maak eerst de ADR-uitvoer met `tools/validate-don-adr.sh`. Het volgende commando
maakt daarvan een Markdown-overzicht met aantallen per API en per regel:

```sh
python3 tools/summarize_adr_output.py -o tools/adr-output-summary.md
```

Dit vereist Python 3.9 of nieuwer en geen aanvullende packages. Een ander
invoerbestand kan als argument worden opgegeven:

```sh
python3 tools/summarize_adr_output.py pad/naar/adr-output.txt -o overzicht.md
```

Zonder `-o` schrijft het script naar de standaarduitvoer. Het controleert of
de aantallen meldingen overeenkomen met de diagnostiektotalen in de invoer
en rapporteert een fout als een API-sectie onvolledig is. Bestaande
uitvoerbestanden worden overschreven na succesvolle verwerking van de invoer.

De resultaten zijn gegroepeerd op foutniveau en regel, met een voorbeeld en
het aantal verschillende meldingsteksten per regel. Info-meldingen en hints
worden indien aanwezig apart vermeld, maar niet verder uitgesplitst.
