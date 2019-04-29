#!/bin/bash

set -e
set -x

BRANCH_TO_DEPLOY=master

git_branches=($(git branch --contains HEAD | cut -c 3-)) 2>/dev/null

if [[ " ${git_branches[@]} " =~ " ${BRANCH_TO_PUSH} " ]]; then
    deploy=true
else
    deploy=false
fi

release_image() {
    if [[ -f "docs/release-docker-image.sh" ]]; then
        cd docs
        ./release-docker-image.sh $deploy
        cd ..
    fi
}

test_docker_compose() {
    if [[ -d "infra" ]]; then
        # test if all the services can be brought up
        cd infra

        rm -f docker-compose.override.yml

        docker-compose pull
        docker-compose up -d
        docker-compose down
        cd ..
    fi
}

write_deploy_params() {
    # if on jenkins AND it's a tagged release -> prepare deployment
    if [[ -n "$JENKINS_URL" ]]; then
        echo "
DO_DEPLOY=${deploy}
" > deployment-parameters
    fi
}

release_image
test_docker_compose
write_deploy_params
