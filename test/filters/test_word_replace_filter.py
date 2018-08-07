'''Word replace filter testcases'''
from unittest import TestCase
from unittest.mock import patch

from purewords.filters import WordReplaceFilter


class TestWordReplaceFilterClass(TestCase):

    def setUp(self):
        self.replace_dictionary = {
            'A': 'a',
            'B': 'b'
        }
        self.filter = WordReplaceFilter(self.replace_dictionary)

    def test_add_replacement(self):
        self.filter.add_replacement(
            'C',
            'c'
        )
        self.assertEqual(
            self.filter.replace_dictionary['C'],
            'c'
        )
        self.assertEqual(
            len(self.filter.replace_dictionary),
            3
        )

    @patch('re.sub')
    def test_call(self, patch_sub):
        sentence = 'ABC'
        self.filter(sentence)

        self.assertEqual(
            patch_sub.call_count,
            len(self.replace_dictionary)
        )
