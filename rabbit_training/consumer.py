import pika,sys,os


def main():
    # create connection
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

    # create a channel in the connection
    channel = connection.channel()

    # create a queye if it does not exist already and associate it with the channel
    channel.queue_declare(queue="hello")

    def callback(ch,method,properties,body):
        print("[x] received %r" %body)

    # Associate a call back function with the mesage queue
    channel.basic_consume(queue="hello",on_message_callback=callback,auto_ack=True)

    # start consuming the mesages
    print(" [*] waiting for the message. To exit press Ctrl-c")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    