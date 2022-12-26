from analyzer.t5 import T5Analyzer
from config.model import AppConfig
from database.db import Database
from model.tweet import TweetReply
import json


class App:
    config: AppConfig
    analyzer: T5Analyzer

    def run(self):
        # read config
        config_path = "config.ini"
        self.config = AppConfig.create_from_file(config_path)
        self.analyzer = T5Analyzer()

        # Initialize Database
        Database.initialize(self.config)

        # Read all replies
        updated_tweets = []
        for tweet_reply in TweetReply.collection():
            tweet_reply.stats = self.analyzer.analyze(
                map(lambda reply: reply.text, tweet_reply.replies))
            print(json.dumps(tweet_reply.stats))


if __name__ == '__main__':
    app = App()
    app.run()
