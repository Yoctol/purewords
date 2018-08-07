'''Url filter testcases'''
from unittest import TestCase

from purewords.filters import url_filter


class TestUrlFilterClass(TestCase):

    def setUp(self):
        self.filter = url_filter

    def test_url_filter(self):
        sentence = "我們的官網是http://www.yoctol.com.tw" \
                   + "，有問題可以寄信至service@yoctol.com" \
                   + "或寄信到email@yoctol.edu.tw"
        answer = "我們的官網是_url_，有問題可以寄信至_url_或寄信到_url_"
        self.assertEqual(
            answer,
            self.filter(sentence)
        )
