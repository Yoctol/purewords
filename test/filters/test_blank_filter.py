'''Blank filter testcase'''
from unittest import TestCase

from purewords.filters import BlankFilter

class TestBlankFilterClass(TestCase):

    def setUp(self):
        self.filter = BlankFilter

    def test_blank_filter(self):
        sentence = 'Hello I am ______ blank!!'
        answer = 'Hello I am _ blank!!'
        self.assertEqual(
            answer,
            self.filter(sentence)
        )
