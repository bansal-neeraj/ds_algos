import pika

# create a connection , say cn
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# create a channel in CN , say CH
channel = connection.channel()

# [optional] create an exchange and specify the bindings ,

# if a queue does not exists already , create a queue through the channel
channel.queue_declare(queue="hello")

# Publish the message
channel.basic_publish(exchange="",routing_key="hello",body="hello_world msg #1")
print("[x] Sent Hello World")

# close the connection
# Automatically closes the channel
connection.close()
