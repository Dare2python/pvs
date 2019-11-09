#!/usr/bin/env bash
set -x
docker ps -a | grep rabbit
docker exec -it some-rabbit rabbitmqctl list_queues
