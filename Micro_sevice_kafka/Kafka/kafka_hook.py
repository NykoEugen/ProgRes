from confluent_kafka import Producer
from producer_wrapper import ProducerWrapper


class KafkaHook:

    def __init__(self, config):
        self.config = config

    def get_producer(self):
        producer = Producer(self.config)
        return ProducerWrapper(producer)

