import os

import pika
from dotenv import load_dotenv

load_dotenv()

amqp_user = os.getenv("AMQP_USER")
amqp_password = os.getenv("AMQP_PASSWORD")
amqp_address = "localhost"
amqp_vhost = os.getenv("AMQP_VHOST")
amqp_port = int(os.getenv("AMQP_PORT"))
queue_name = "0"


class MessagePublisher:
    def __init__(self):
        connection_params = pika.ConnectionParameters(
            host=amqp_address,
            port=amqp_port,
            virtual_host=amqp_vhost,
            credentials=pika.PlainCredentials(amqp_user, amqp_password),
        )

        self.connection = pika.BlockingConnection(connection_params)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name)

    def publish_message(self, message):
        self.channel.basic_publish(exchange="", routing_key=queue_name, body=message)

        print("Message sent")

    def close_connection(self):
        self.connection.close()


if __name__ == "__main__":
    publisher = MessagePublisher()
    command = input("Enter the command 'print' or 'send': ").lower()

    publisher.publish_message(command)
    publisher.close_connection()
