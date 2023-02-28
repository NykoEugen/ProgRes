import json


class ProducerWrapper:

    def __init__(self, producer):
        self.producer = producer

    def send_msg(self, topic_name, message):
        serialized_msg = json.dumps(message).encode('utf-8')
        self.producer.poll(1)
        self.producer.produce(topic_name, serialized_msg)
        self.producer.flush()
        return 'Message send'



