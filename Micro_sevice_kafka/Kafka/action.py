from generator import Generator


class GenerateAndSendAction:

    def execute(self, producer, topic):
        message = Generator.generate_unit()
        producer.send_msg(topic, message)


