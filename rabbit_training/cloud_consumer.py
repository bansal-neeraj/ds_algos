import pika, os, json, ast


url = 'amqp://wfddeskb:m7TAKqipgtvl4miA6K4Z5Yq3Mc8IrcJH@puffin.rmq2.cloudamqp.com/wfddeskb'
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='test_queue')


def callback(ch,method,properties,body):
    # print(' [x] Received ', str(body))
    x = ast.literal_eval(body.decode('utf-8'))  # convert bytes to dictionary
    print(x)
    # print(type(x))

channel.basic_consume(
    'test_queue',
    callback,
    auto_ack=True
)

print(' [x] waiting for message')
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.start_consuming()

connection.close()

