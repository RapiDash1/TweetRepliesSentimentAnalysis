from kafka import KafkaAdminClient, KafkaProducer
from kafka.admin import NewTopic

class KafkaHandler:

    analyseRepliesTopicName = "analyseReplies"
    server = "localhost:9092"

    def __init__(self):
        self.client = KafkaAdminClient(bootstrap_servers=[self.server])
        self.producer = KafkaProducer(bootstrap_servers=[self.server])
        #self.__createAnalyseRepliesTopic()

    def addTweetIdToTopic(self, tweetId):
        self.producer.send(self.analyseRepliesTopicName, tweetId.encode())
        self.producer.flush()
                        
    def __createAnalyseRepliesTopic(self):
        topic = NewTopic(self.analyseRepliesTopicName, 1, 1)
        self.client.create_topics([topic])
