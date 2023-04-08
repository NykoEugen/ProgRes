import asyncio

from confluent_kafka import Consumer, KafkaError

kafka_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-group'
}

def consume():
    consumer = Consumer(kafka_config)
    consumer.subscribe(['Topic'])

    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print(f"Reached end of partition: {msg.topic()}")
                else:
                    print(f"Error while consuming message: {msg.error()}")
            else:
                print(f"Received message: {msg.value().decode()}")
    except KeyboardInterrupt:
        print("Stopping consumer")
    finally:
        consumer.close()

async def main():
    consume()

    await asyncio.sleep(1)

if __name__ == '__main__':
    while True:
        asyncio.run(main())