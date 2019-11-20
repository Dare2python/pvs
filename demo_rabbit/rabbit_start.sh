#!/usr/bin/env bash
set -x
docker ps -a
docker run -d --hostname my-rabbit --name some-rabbit -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=Munich19 -p 8080:15672 -p 5672:5672 rabbitmq:3.8.1-management-alpine
docker ps -a | grep rabbit
open http://localhost:8080
# for windows
# start "http://localhost:8080"
