#!/bin/bash

set -e # exit on error
set -x # echo commands

CONTAINER_REPO=ghcr.io/vng-realisatie/gemma-zaken-docs

git_tag=$(git tag --points-at HEAD) &>/dev/null

push=${1:-false}


build_image() {
    tag=$1
    cp -r ../api-specificatie ./api-specificatie
    docker build \
        -t ${CONTAINER_REPO}:$tag \
        -f Dockerfile .
    rm -rf ./api-specificatie
}

get_release_tag() {
    if [[ -n "$git_tag" ]]; then
        echo "Building image for git tag $git_tag"
        release_tag=$git_tag
    else
        release_tag=${RELEASE_TAG:-latest}
    fi
    echo $release_tag
}

push_image() {
    # JOB_NAME is set by Jenkins
    # only push the image if running in CI
    release_tag=$1
    if [[ -n "$JOB_NAME" ]]; then

        # check if commit is contained in $BRANCH_TO_PUSH
        if [[ $push = true ]]; then
            docker push ${CONTAINER_REPO}:${release_tag}
        fi
    else
        echo "Not pushing image, set the JOB_NAME envvar to push after building and ensure you're on the master branch"
    fi
}


# always build to verify that the image build is not broken
build_image $(get_release_tag)

# only push to docker hub on master
push_image $(get_release_tag)
