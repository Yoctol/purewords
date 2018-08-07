'''Stopwords filter testcase'''
from unittest import TestCase

from purewords.filters import StopwordsFilter


class TestStopwordsFilter(TestCase):

    def setUp(self):
        stopwords_set = set(['的', '啦'])
        self.filter = StopwordsFilter(stopwords_set)

    def test_stopwords_filter(self):
        sentence = "我講話很喜歡加的啦，" \
                   + "你知道的啦，我家有養一隻狗的啦。"
        answer = "我講話很喜歡加，你知道，我家有養一隻狗。"
        self.assertEqual(
            answer,
            self.filter(sentence)
        )
