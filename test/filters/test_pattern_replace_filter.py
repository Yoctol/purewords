'''pattern replace filter testcases'''
from unittest import TestCase
from unittest.mock import patch

from purewords.filters import PatternReplaceFilter


class TestPatternReplaceFilterClass(TestCase):

    def setUp(self):
        self.patterns = ['A']
        self.replacement = 'a'
        self.filter = PatternReplaceFilter(
            self.patterns,
            self.replacement
        )

    def test_add_pattern(self):
        pattern = '\d+'
        self.filter.add_pattern(pattern)
        self.assertEqual(
            self.filter.patterns[-1],
            pattern
        )

    @patch('re.sub')
    def test_call(self, patch_sub):
        sentence = ''
        self.filter(sentence)
        patch_sub.assert_called_once_with(
            self.patterns[0],
            self.replacement,
            sentence
        )
