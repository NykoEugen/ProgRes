import asyncio
from action import GenerateAndSendAction
from generator import Generator
from kafka_hook import KafkaHook

kafka_config = {'bootstrap.servers': 'broker:29092'}


async def main():
    kafka_hook = KafkaHook(kafka_config)
    producer = kafka_hook.get_producer()
    topic = Generator.topic_name()
    action = GenerateAndSendAction()
    action.execute(producer, topic)

    await asyncio.sleep(20)


if __name__ == '__main__':
    while True:
        asyncio.run(main())
