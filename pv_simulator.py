#!/usr/bin/env python3

# PV simulator: It must listen to the broker for the meter values,
# generate a simulated PV power value and
# the last step is to add this value to the meter value and output the result.

import json
import pika
from datetime import datetime


def callback(ch, method, properties, body):
    # print("rx {}".format(body))
    message = json.loads(body)
    message['timestamp'] = datetime.fromtimestamp(message['timestamp'])
    print("rx {}".format(message))

    # meter_object = {'timestamp': datetime.fromtimestamp(message['timestamp']),
    #                 'power_value': float(message['power_value'])}
    # print("rx {}".format(meter_object))

    ch.basic_ack(delivery_tag=method.delivery_tag)


credentials = pika.PlainCredentials('user', 'Munich19')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='meter', durable=True)  # queue declaration is idempotent
channel.basic_consume(queue='meter',
                      on_message_callback=callback)
print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
