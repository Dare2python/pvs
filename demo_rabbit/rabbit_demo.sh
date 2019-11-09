#!/usr/bin/env bash
set -x
./rabbit_clear.sh
./rabbit_start.sh
echo "wait for RabbitMQ to start in container…"
sleep 20s
./rabbit_list.sh
./send.py
./rabbit_list.sh
./receive.py
