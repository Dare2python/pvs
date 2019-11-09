#!/usr/bin/env bash
set -x
docker ps -a | grep rabbit
docker stop some-rabbit
docker rm some-rabbit
docker ps -a
