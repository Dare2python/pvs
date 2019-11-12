#!/usr/bin/env python3

# PV simulator: It must listen to the broker for the meter values,
# generate a simulated PV power value and
# the last step is to add this value to the meter value and output the result.

import json
import pika
from datetime import datetime
import numpy as np


def simulate(x):
    mu = 14
    sigma = 3
    return 3300*1/(sigma * np.sqrt(2 * np.pi)*0.13) * np.exp(- (x - mu)**2 / (2 * sigma**2))


def callback(ch, method, properties, body):
    # JSON format is chosen for debugging and demo visibility purposes
    # I would go for anything binary for production
    message = json.loads(body)
    message['timestamp'] = datetime.fromtimestamp(message['timestamp'])
    print("rx {}".format(message))

    d = message['timestamp']
    x = d.hour + d.minute/60 + d.second/60/60 + d.microsecond/60/60/60

    pv_power_value = simulate(x)
    print("x={} y={}".format(x, pv_power_value))

    with open('results.csv', 'a+') as the_file:
        the_file.write('{},{},{},{}\n'.format(message['timestamp'],
                                              message['power_value'],
                                              pv_power_value,
                                              pv_power_value+message['power_value']))

    ch.basic_ack(delivery_tag=method.delivery_tag)


credentials = pika.PlainCredentials('user', 'Munich19')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='meter', durable=True)  # queue declaration is idempotent
channel.basic_consume(queue='meter',
                      on_message_callback=callback)
print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
