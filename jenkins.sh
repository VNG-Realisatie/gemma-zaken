#!/bin/bash

set -e
set -x

if [[ -f "docs/release-docker-image.sh" ]]; then
    cd docs
    ./release-docker-image.sh
    cd ..
fi

if [[ -d "infra" ]]; then
    # test if all the services can be brought up
    cd infra

    # no port-binding
    rm docker-compose.override.yml

    docker-compose pull
    docker-compose up -d
    docker-compose down
fi
