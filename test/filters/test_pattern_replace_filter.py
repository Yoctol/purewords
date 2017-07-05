'''pattern replace filter testcases'''
from unittest import TestCase
from unittest.mock import patch

from purewords.filters import PatternReplaceFilter


class TestPatternReplaceFilterClass(TestCase):

    def setUp(self):
        self.patterns = ['A']
        self.replacement = 'a'
        self.filter_ = PatternReplaceFilter(
            self.patterns,
            self.replacement
        )

    def test_add_pattern(self):
        pattern = '\d+'
        self.filter_.add_pattern(pattern)
        self.assertEqual(
            self.filter_.patterns[-1],
            pattern
        )

    def test_store_matches_of_pattern(self):
        self.filter_.add_pattern('\d+')
        test_cases = ['我要買10元的飲料', 'Apple真好吃', '某官員A1000萬元', '能A到1億元爽爽derA_A']
        answers = [['10'], ['A'], ['A', '1000'], ['A', '1', 'A', 'A']]
        for test_case, answer in zip(test_cases, answers):
            self.filter_.store_matches_of_pattern(test_case, verbose=False)
            self.assertEqual(self.filter_.matches, answer)

    def test_go_forward(self):
        self.filter_.add_pattern('\d+')
        test_cases = ['我要買10元的飲料', 'Apple真好吃', '某官員A1000萬元', '能A到1億元爽爽derA_A']
        answers = ['我要買a元的飲料', 'apple真好吃', '某官員aa萬元', '能a到a億元爽爽dera_a']
        for test_case, answer in zip(test_cases, answers):
            self.assertEqual(
                self.filter_.go_forward(test_case, verbose=False), answer)

    def test_go_backward(self):
        self.filter_.add_pattern('\d+')
        test_cases = ['我要買10元的飲料', 'Apple真好吃', '某官員A1000萬元', '能A到1億元爽爽derA_A']
        answers = ['我要買a元的飲料', 'apple真好吃', '某官員aa萬元', '能a到a億元爽爽dera_a']
        for test_case, answer in zip(test_cases, answers):
            self.assertEqual(
                self.filter_.go_forward(test_case, verbose=False), answer)
            self.assertEqual(self.filter_.go_backward(
                answer, verbose=False), test_case)

    def test_call(self):
        self.filter_.add_pattern('\d+')
        test_cases = ['我要買10元的飲料', 'Apple真好吃', '某官員A1000萬元', '能A到1億元爽爽derA_A']
        answers = ['我要買a元的飲料', 'apple真好吃', '某官員aa萬元', '能a到a億元爽爽dera_a']
        for test_case, answer in zip(test_cases, answers):
            self.assertEqual(
                self.filter_(test_case), answer)

    # @patch('re.sub')
    # def test_call(self, patch_sub):
    #     sentence = ''
    #     self.filter_(sentence)
    #     patch_sub.assert_called_once_with(
    #         self.patterns[0],
    #         self.replacement,
    #         sentence
    #     )
