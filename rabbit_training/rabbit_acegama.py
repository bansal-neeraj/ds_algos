"""
exp tp connect to remote que on Digital ocean
"""
import json

import pika

credentials = pika.PlainCredentials('ace_bak','options')
parameters = pika.ConnectionParameters(
    host='143.244.139.47',
    port=5672,
    virtual_host='backup',
    credentials=credentials
)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
# channel.queue_declare(queue='test_queue')


def callback(ch,method,properties,body):
    print(' [x] Received ', str(body))
    # print(' [x] Received %r' % json.loads(body))
    # x = json.loads(body)  # convert bytes to dictionary
    # print(x)
    # print(type(x))


channel.basic_consume(
    'daily_backup',
    callback,
    auto_ack=True
)

print(' [x] waiting for message')
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()

connection.close()
