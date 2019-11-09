#!/usr/bin/env python3

# Meter: This should produce messages to the broker with random
# but continuous values from 0 to 9000 Watts.
# This is to mock a regular home power consumption.
import json
import pika
from datetime import datetime
import random

credentials = pika.PlainCredentials('user', 'Munich19')  # basic inline config
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials))  # localhost
channel = connection.channel()
channel.queue_declare(queue='meter', durable=True)  # queue declaration is idempotent

message = {
    'timestamp': datetime.timestamp(datetime.now()),
    'power_value': round(random.uniform(0, 9000), 3)
}
body = json.dumps(message)

channel.basic_publish(exchange='',  # default exchange, no Envs (dev, stage, prod), no other projects yet
                      routing_key='meter',
                      body=body,
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                      ))
print("tx {0}".format(body))
connection.close()
