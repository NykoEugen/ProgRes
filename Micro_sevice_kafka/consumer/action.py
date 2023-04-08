class PollAction:

    def execute(self, consumer, topic):
        consumer.poll_msg(topic)

