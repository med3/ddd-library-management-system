import pika

class RabbitMQEventPublisher:
    def __init__(self, connection_params):
        self.connection = pika.BlockingConnection(connection_params)
        self.channel = self.connection.channel()

    def publish(self, event_name, payload):
        self.channel.basic_publish(exchange='', routing_key=event_name, body=payload)
