#!/usr/bin/env python3

# Meter: This should produce messages to the broker with random
# but continuous values from 0 to 9000 Watts.
# This is to mock a regular home power consumption.
import json
import pika
from datetime import datetime, timedelta
import random


def connect(connection):
    channel = connection.channel()
    channel.queue_declare(queue='meter', durable=True)  # queue declaration is idempotent
    return channel


def generate(today, seconds):
    return {
        'timestamp': datetime.timestamp(today + timedelta(seconds=seconds*2)),  # every couple of seconds
        'power_value': round(random.uniform(0, 9000), 3)  # truncate random power value to 3 decimal digits
        # "random but continuous values" ?? are they must be "smooth"?
    }


def publish(channel, message):
    # JSON format is chosen for debugging and demo visibility purposes
    # I would go for anything binary for production
    body = json.dumps(message)
    channel.basic_publish(exchange='',  # default exchange, no Envs (dev, stage, prod), no other projects yet
                          routing_key='meter',
                          body=body,
                          properties=pika.BasicProperties(
                              delivery_mode=2,  # make message persistent
                          ))
    print("tx {0}".format(body))


credentials = pika.PlainCredentials('user', 'Munich19')  # basic inline config

with pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials)) as connection:
    channel = connect(connection)
    # The period of a day with samples every couple of seconds would be enough.
    today = datetime.now().replace(microsecond=0)  # make timestamp sorter by truncating microseconds
    for seconds in range(24):  # * 60 * 30):
        publish(channel, generate(today, seconds))

# connection.close()  # with must take care of this
