'''abbreviation filter testcases'''
from unittest import TestCase

from purewords.filters import abbreviation_filter


class TestAbbreviationFilter(TestCase):

    def setUp(self):
        self.filter = abbreviation_filter

    def test_abbreviation_filter(self):
        sentence = "I'm Mr. Qoo. She's Mrs. M. " \
                   + "You're great. I'd and I'll " \
                   + "like to show you something"
        answer = "I am Mr. Qoo. She Mrs. M. " \
                 + "you are great. I would and " \
                 + "I will like to show you something"
        self.assertEqual(
            answer,
            self.filter(sentence)
        )
