import threading
import pika
import json
from dotenv import load_dotenv
import os
load_dotenv()

from django.core.management.base import BaseCommand


from core.infra.models.mark import Mark, Report
class Command(BaseCommand):
    help = "Consume messages from RabbitMQ queue"

    def handle(self, *args, **kwargs):
        thread = threading.Thread(target=self.start_consuming)
        thread.daemon = True
        thread.start()

        self.stdout.write(self.style.SUCCESS("RabbitMQ consumer started."))
        thread.join()

    def start_consuming(self):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=os.getenv("RABBITMQ_HOST"),
                port=os.getenv("AMQP_PORT"),
                credentials=pika.PlainCredentials(os.getenv('RABBITMQ_USER'), os.getenv('RABBITMQ_PASSWORD')),
            )

        )
        channel = connection.channel()

        # Коллбэк для обработки сообщений
        def callback(ch, method, properties, body):
            print(f"Received {body}")
            self.process_message(body)
            ch.basic_ack(delivery_tag=method.delivery_tag)

        # Начать потреблять сообщения
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue=os.getenv("RABBIT_CONSUME_QUEUE"), on_message_callback=callback)

        channel.start_consuming()

    def process_message(self, body):
        try:
            # Декодируем JSON из тела сообщения
            message = json.loads(body)
            print(f"Processing message: {message}")

            # # Пример использования модели
            # obj, created = YourModel.objects.get_or_create(
            #     field1=message['field1'],
            #     defaults={'field2': message['field2']}
            # )

        except Exception as e:
            print(f"Error processing message: {e}")
