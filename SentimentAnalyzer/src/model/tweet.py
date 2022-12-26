from typing import Iterable, List
from pymongo.collection import Collection
from database.db import Database


class TweetStats:
    positive_responses: int = 0
    negative_responses: int = 0
    neutral_responses: int = 0

    @staticmethod
    def from_dict(args: dict) -> "TweetStats":
        stats = TweetStats()
        stats.positive_responses = args.get('positive_responses', 0)
        stats.negative_responses = args.get('negative_responses', 0)
        stats.neutral_responses = args.get('neutral_responses', 0)
        return stats


class TweetResponse:
    id: str = ""
    text: str = ""
    edit_history_tweet_ids: List[str] = []

    def from_dict(args: dict) -> "TweetResponse":
        response = TweetResponse()
        response.id = args.get('id')
        response.text = args.get('text')
        response.edit_history_tweet_ids = args.get(
            'edit_history_tweet_ids', [])
        return response


class TweetReply:
    tweetId: str = ""
    replies: List[TweetResponse] = []
    stats: TweetStats = None

    @staticmethod
    def from_dict(args: dict) -> "TweetReply":
        reply = TweetReply()
        reply.tweetId = args.get('tweetId', "")
        if 'replies' in args:
            reply.replies = map(TweetResponse.from_dict, args['replies'])

        if 'stats' in args:
            reply.stats = map(TweetStats.from_dict, args['stats'])
        return reply

    @staticmethod
    def collection() -> Iterable["TweetReply"]:
        return map(TweetReply.from_dict, Database.instance().db['replies'].find())
