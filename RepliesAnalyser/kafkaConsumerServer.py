from kafka import KafkaConsumer
from analyser import Analyser

class KafkaHandler:

    def __init__(self):
        self.consumer = KafkaConsumer("analyseReplies", bootstrap_servers=["localhost:9092"])
        for message in self.consumer:
            Analyser.analyse(message.value.decode("utf-8"))


if __name__ == "__main__":
    KafkaHandler()