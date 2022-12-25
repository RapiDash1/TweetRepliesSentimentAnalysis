import pymongo
from tweetReplies import TweetReplies

class DbHandler:
    def __init__(self):
        dbClient = pymongo.MongoClient("mongodb://twitteradmin:adminpassword@localhost:27017/")
        self.db = dbClient["tweetanalysis"]
        self.collection = self.db["replies"]

    def add(self, tweetReplies: TweetReplies):
        if not self.collection.find_one({"tweetId": tweetReplies.tweetId}):
            self.collection.insert_one({
                "tweetId": tweetReplies.tweetId,
                "replies": tweetReplies.replies
            })
        else:
            for reply in tweetReplies.replies:
                self.collection.update_one(
                { "tweetId": tweetReplies.tweetId },
                {
                    "$push": {
                        "replies": reply
                    }
                }
            )

    def get(self, tweetId):
        return self.collection.find_one({"tweetId": tweetId})

    def _dropCollection(self):
        self.collection = self.db["replies"]
        self.collection.drop()

# [--Add replies example--]
# dbHandler = DbHandler()

# tweetReplies = TweetReplies("1", [{'edit_history_tweet_ids': ['1606971655057993729'], 'id': '1606971655057993729', 'text': '@elonmusk  today is Christmas 🌲 day . Will you be my Santaclaus 🎅?.\nwill you make me twitter ceo for a day.....😜😜🤣🤣🤣\n#Christmas\n#MerryChristmas2022\n#twitter\n#Xmas'}, {'edit_history_tweet_ids': ['1606971653086449664'], 'id': '1606971653086449664', 'text': '@elonmusk @westcoastbill Twitter for Android also needs $cashtags'}, {'edit_history_tweet_ids': ['1606971640004632578'], 'id': '1606971640004632578', 'text': '@elonmusk @RichardDawkins 😵🙄 https://t.co/ljcJ9UofPZ'}, {'edit_history_tweet_ids': ['1606971631569891328'], 'id': '1606971631569891328', 'text': 'RT @GSJohal85: @elonmusk Christmas gift to the #FreeJaggiNow campaign this morning.\n\nIt is not clear what @Twitter rules have been broken,…', 'withheld': {'copyright': False, 'country_codes': ['IN']}}, {'edit_history_tweet_ids': ['1606971627191046146'], 'id': '1606971627191046146', 'text': "@elonmusk @SeibtNaomi @Spiro_Ghost That's my man! To hell with these @wef MF's! They will never win."}, {'edit_history_tweet_ids': ['1606971626096295936'], 'id': '1606971626096295936', 'text': '@elonmusk https://t.co/O1vvc9Zjbe'}, {'edit_history_tweet_ids': ['1606971570982998017'], 'id': '1606971570982998017', 'text': "RT @ProfessorF: @elonmusk That's what happens when woke interferes with work.\n\nWith such a mess, refactoring can only lead to a more effici…"}, {'edit_history_tweet_ids': ['1606971564808966144'], 'id': '1606971564808966144', 'text': 'RT @jean_gum: @elonmusk when are the fauci files going to be released ?'}, {'edit_history_tweet_ids': ['1606971564037218304'], 'id': '1606971564037218304', 'text': '@elonmusk please buy my house before the bank forecloses on it and me and my family are homeless'}, {'edit_history_tweet_ids': ['1606971559041798144'], 'id': '1606971559041798144', 'text': '@elonmusk The "Heath Robinson philosophy" to bury the truth in layers of complexity, but then isn\'t that like any other brain? Our reality is based on a golden ratio maybe we can\'t escape it any more than our creations can.'}])
# dbHandler.add(tweetReplies)
# dbHandler.add(tweetReplies)
# print(dbHandler.get("1"))

# [--Drop Collection example--]
dbHandler = DbHandler()
dbHandler._dropCollection()