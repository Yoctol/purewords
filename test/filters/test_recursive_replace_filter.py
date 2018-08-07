'''recursive replace filter testcase'''
from unittest import TestCase

from purewords.filters import RecursiveReplaceFilter


class TestRecursiveReplaceFilterClass(TestCase):

    def setUp(self):
        self.pattern = 'AA'
        self.replacement = 'A'
        self.filter = RecursiveReplaceFilter(
            self.pattern,
            self.replacement
        )

    def test_call(self):
        sentence = 'AAAA'
        result = self.filter(sentence)
        self.assertEqual(
            result,
            'A'
        )
