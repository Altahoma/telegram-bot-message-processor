import os

import pika
import requests
from dotenv import load_dotenv

load_dotenv()

amqp_user = os.getenv("AMQP_USER")
amqp_password = os.getenv("AMQP_PASSWORD")
amqp_address = os.getenv("AMQP_ADDRESS")
amqp_vhost = os.getenv("AMQP_VHOST")
amqp_port = int(os.getenv("AMQP_PORT"))
queue_name = "0"
api_url = os.getenv("EXTERNAL_API_URL")


class Consumer:
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

    def get_last_message(self):
        file_path = "messages.txt"

        if os.path.exists(file_path):
            with open(file_path) as file:
                return file.read()
        else:
            return "Message does not exist"

    def print_message(self):
        print(f"Received command 'print': {self.get_last_message()}")

    def send_message(self):
        last_message = self.get_last_message()
        requests.post(api_url, json={"message": last_message})

        print(f"Received command 'send': {last_message}")

    def handle_message(self, body):
        if body == "print":
            self.print_message()
        elif body == "send":
            self.send_message()

    def callback(self, ch, method, properties, body):
        self.handle_message(body.decode("utf-8"))

    def start_consuming(self):
        self.channel.basic_consume(
            queue=queue_name, on_message_callback=self.callback, auto_ack=True
        )

        print("Waiting for commands...")
        self.channel.start_consuming()


if __name__ == "__main__":
    consumer = Consumer()
    consumer.start_consuming()
