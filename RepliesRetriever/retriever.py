import requests
from dbHandler import DbHandler
from tweetReplies import TweetReplies
from envHandler import EnvHandler
import requests
from kafkaHandler import KafkaHandler

class Retriever:

    def _getAuthToken(self):
        envHandler = EnvHandler.instance()
        apiKey = envHandler.getValue("api_key")
        apiSecretKey = envHandler.getValue("api_secret_key")
        bearerToken = envHandler.getValue("bearer_token")


        auth = requests.auth.HTTPBasicAuth(apiKey, apiSecretKey)
        return requests.post(
            "https://api.twitter.com/oauth2/token",
            auth=auth,
            data={"grant_type": "client_credentials"},
            headers={"Authorization": f"Bearer {bearerToken}"},
        ).json()


    def saveReplies(self):
        token = self._getAuthToken()

        tweetsByUser = requests.get(
            "https://api.twitter.com/2/tweets/search/recent",
            params={"query": "from:elonmusk", "max_results": 10},
            headers={"Authorization": f"Bearer {token['access_token']}"},
        ).json()

        latestTweetId = tweetsByUser["data"][0]["id"]

        replies = []
        nextToken = None

        i = 0
        while i < 10:
            searchResults = requests.get(
                "https://api.twitter.com/2/tweets/search/recent",
                params={
                    "query": f"to:elonmusk",
                    "max_results": 10,
                    "next_token": nextToken,
                },
                headers={"Authorization": f"Bearer {token['access_token']}"},
            ).json()

            replies.extend(searchResults["data"])

            nextToken = searchResults["meta"]["next_token"]
            i += 1

        dbHandler = DbHandler()
        dbHandler.addTweetReplies(TweetReplies(latestTweetId, replies)) 

        kafkaHandler = KafkaHandler()
        kafkaHandler.addTweetIdToTopic(latestTweetId)

    
if __name__ == "__main__":
    retriever = Retriever()
    retriever.saveReplies()
