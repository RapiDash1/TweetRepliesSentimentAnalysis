from transformers import T5ForConditionalGeneration, T5Tokenizer
from collections import Counter
from typing import Iterable, List

from model.tweet import TweetStats


class T5Analyzer:
    tokenizer: T5Tokenizer
    model: T5ForConditionalGeneration

    def __init__(self) -> None:
        self.tokenizer = T5Tokenizer.from_pretrained('t5-base', )
        self.model = T5ForConditionalGeneration.from_pretrained('t5-base')

    def analyze(self, replies: Iterable[str]) -> TweetStats:
        replies = list(map(lambda x: "sst2 sentence: {0}".format(x), replies))
        inputs = self.tokenizer(
            replies, return_tensors='pt', padding=True, max_length=256)
        outputs = self.model.generate(
            input_ids=inputs["input_ids"], attention_mask=inputs["attention_mask"])
        responses = Counter(self.tokenizer.batch_decode(
            outputs, skip_special_tokens=True))
        stats = TweetStats()
        stats.positive_responses = responses.get('positive', 0)
        stats.negative_responses = responses.get('negative', 0)
        stats.neutral_responses = responses.get('neutral', 0)
        return stats
