import asyncio

from action import PollAction
from kafka_hook import KafkaHook

config_consum = {'bootstrap.servers': 'localhost:9092', 'group.id': 'my-group', 'auto.offset.reset': 'earliest'}

async def main():
    kafka_hook = KafkaHook(config_consum)
    consumer = kafka_hook.get_consumer()
    topic = "Topic"
    action = PollAction()
    action.execute(consumer, topic)
    consumer.close()

    await asyncio.sleep(60)


if __name__ == '__main__':
    while True:
        asyncio.run(main())