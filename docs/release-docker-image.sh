#!/bin/bash

set -e # exit on error
set -x # echo commands

CONTAINER_REPO=vngr/gemma-zaken-docs
BRANCH_TO_PUSH=master

git_tag=$(git tag --points-at HEAD) &>/dev/null
git_branch=$(git symbolic-ref HEAD 2>/dev/null) || git_branch="(unnamed branch)"     # detached HEAD


build_image() {
    tag=$1
    docker build \
        -t ${CONTAINER_REPO}:$tag \
        -f Dockerfile .
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
    if [[ -n "$JOB_NAME" && $git_branch = $BRANCH_TO_PUSH ]]; then
        docker push ${CONTAINER_REPO}:${release_tag}
    else
        echo "Not pushing image, set the JOB_NAME envvar to push after building and ensure you're on the master branch"
    fi
}


# always build to verify that the image build is not broken
build_image $(get_release_tag)

# only push to docker hub on master
push_image $(get_release_tag)
