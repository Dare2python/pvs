#!/usr/bin/env bash

VERSION="1.0-dev"
if [[ -n $1 ]]
then
    VERSION=$1
fi

# clean from previous run
docker stop some-rabbit
docker rm some-rabbit

docker stop pvs-consumer
docker rm pvs-consumer

docker network rm rabbit-net

# docker network ls

# On user-defined networks, containers can not only communicate by IP address,
# but can also resolve a container name to an IP address. This capability is called automatic service discovery.
docker network create --driver bridge rabbit-net

docker run -d --hostname my-rabbit --name some-rabbit \
-e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=Munich19 -p 8080:15672 -p 5672:5672 \
--network rabbit-net rabbitmq:3.8.1-management-alpine


echo "wait for RabbitMQ to start in container…"
sleep 20s
# pvs-consumer will connect to RannitMQ by container name "some-rabbit"
docker run -dit --name pvs-consumer --network rabbit-net pvs/consumer:"${VERSION}"

# check that both containers in the same network "rabbit-net"
docker network inspect rabbit-net

# docker attach pvs-consumer
docker logs -ft pvs-consumer

