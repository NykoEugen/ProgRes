from confluent_kafka import Consumer

from consumer_wrapper import ConsumerWrapper


class KafkaHook:

    def __init__(self, config_consum):
        self.config_consum = config_consum

    def get_consumer(self):
        consumer = Consumer(self.config_consum)
        return ConsumerWrapper(consumer)