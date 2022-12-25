import sys
sys.path.insert(0, "../RepliesRetriever/")
from dbHandler import DbHandler
from textblob import TextBlob
from tweetAnalysis import TweetAnalysis

class Analyser:

    @classmethod
    def analyse(cls, tweetId):
        dbHandler = DbHandler()
        replies = dbHandler.getRepliesForTweetId(tweetId)
        polarities = []
        for reply in replies["replies"]:
            sentiment = TextBlob(reply["text"]).sentiment
            polarities.append(sentiment.polarity)

        if len(polarities) > 0:
            analysis = sum(polarities)/len(polarities)
            dbHandler.addSentimentAnalysisForTweet(TweetAnalysis(tweetId, analysis))
