from confluent_kafka import Consumer, KafkaError

cfg = {'bootstrap.servers': 'localhost:29092', 'group.id': 'my_group', 'auto.offset.reset': 'earliest'}

consumer = Consumer(cfg)
consumer.subscribe(['Topic'])

while True:
    msg = consumer.poll(50.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print(f'End of partition event received {msg}')
        else:
            print(f'Error while consuming message {msg.error()}')
    else:
        print(f'Received message: {msg.value().decode("utf-8")}')

consumer.close()
