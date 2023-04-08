from confluent_kafka import KafkaError



class ConsumerWrapper:

    def __init__(self, consumer):
        self.consumer = consumer

    def poll_msg(self, topic):
        self.consumer.subscribe([topic])
        try:
            while True:
                msg = self.consumer.poll(timeout=1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        print(f"Reached end of partition: {msg.topic()}")
                    else:
                        print(f"Error while consuming message: {msg.error()}")
                else:
                    print(f"Received message: {msg.value().decode()}")
                    self.consumer.commit()
        except KeyboardInterrupt:
            print("Stopping consumer")
