'''Url filter testcases'''
from unittest import TestCase

from purewords.filters import UrlFilter

class TestUrlFilterClass(TestCase):

    def setUp(self):
        self.filter = UrlFilter()

    def test_remove_url(self):
        sentence = "我們的官網是http://www.yoctol.com.tw" \
                   + "，有問題可以寄信至service@yoctol.com" \
                   + "或寄信到email@yoctol.edu.tw"
        answer = "我們的官網是_url_，有問題可以寄信至_url_或寄信到_url_"
        self.assertEqual(
            answer,
            self.filter(sentence)
        )
