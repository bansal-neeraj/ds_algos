import pika, os, json

# url = os.environ.get('CLOUDAQMP_URL')
url = 'amqp://wfddeskb:m7TAKqipgtvl4miA6K4Z5Yq3Mc8IrcJH@puffin.rmq2.cloudamqp.com/wfddeskb'
print(url)
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.exchange_declare('test_exchange')  # declare exchange
channel.queue_declare(queue='test_queue')  # declare queue
channel.queue_bind('test_queue','test_exchange','tests')  # create binding between queue and exchange

my_dict = {
    'name':"Neeraj",
    'language':'Python',
    'framework':'Django',
    'version':4.0
}

#publish message
channel.basic_publish(
    body=json.dumps(my_dict).encode('utf-8'),  # convert dictionary to bytes
    exchange='test_exchange',
    routing_key='tests'
)

print('message sent')
channel.close()




