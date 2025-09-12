#!/bin/bash

cd api_specs/v1
rm -rf autorisaties besluiten documenten notificaties zaken catalogi
mkdir autorisaties besluiten documenten notificaties zaken catalogi
cd ../..

cd tools/zgw_cleaner
poetry run zgw-cleaner ../../api-specificatie/ac/openapi.yaml > ../../api_specs/v1/autorisaties/openapi.yaml
poetry run zgw-cleaner ../../api-specificatie/brc/current_version/openapi.yaml > ../../api_specs/v1/besluiten/openapi.yaml
poetry run zgw-cleaner ../../api-specificatie/drc/current_version/openapi.yaml > ../../api_specs/v1/documenten/openapi.yaml
poetry run zgw-cleaner ../../api-specificatie/zrc/current_version/openapi.yaml > ../../api_specs/v1/zaken/openapi.yaml
poetry run zgw-cleaner ../../api-specificatie/ztc/current_version/openapi.yaml > ../../api_specs/v1/catalogi/openapi.yaml

cd ../..
npx docusaurus clean-api-docs -p v1-apis all
npx docusaurus gen-api-docs -p v1-apis all

