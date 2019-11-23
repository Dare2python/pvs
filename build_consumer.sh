#!/usr/bin/env bash

VERSION="1.0-dev"
if [[ -n $1 ]]
then
    VERSION=$1
fi

docker rmi -f $(docker images "pvs/*" -aq)

docker build -f ./Dockerfile -t pvs/consumer:latest -t pvs/consumer:"${VERSION}" .
