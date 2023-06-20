import os, json
import pika
from dotenv import load_dotenv


# loading .env file
load_dotenv()

class RabbitMQHelper:

    EXCHANGE = "contract"
    EXCHANGE_TYPE = "direct"
    QUEUE_NAME = "contract_queue"
    ROUTING_KEY = "create"

    def __init__(self) -> None:

        url = os.environ["RABBITMQ_URL"]
        ##params = pika.URLParameters(url)

        self.__connection = pika.BlockingConnection(pika.ConnectionParameters(url)) 

    def __create_channel(self) -> pika.BlockingConnection:
        channel = self.__connection.channel()
        return channel
    
    async def __create_exchanges_queues(self) -> None:

        channel = self.__create_channel()

        channel.exchange_declare(
            exchange=self.EXCHANGE, exchange_type=self.EXCHANGE_TYPE
        )

        channel.queue_declare(queue=self.QUEUE_NAME)
                                 
        channel.queue_bind(
            self.QUEUE_NAME,
            self.EXCHANGE,
            self.ROUTING_KEY
        )

    async def publish_message(self, message_body) -> None:

        await self.__create_exchanges_queues()

        channel = self.__create_channel()

        channel.basic_publish(
            exchange = self.EXCHANGE,
            routing_key = self.ROUTING_KEY,
            body=json.dumps(message_body)
        )

        print ("Publishing message")

        self.__connection.close()

rabbitmq: RabbitMQHelper = RabbitMQHelper()