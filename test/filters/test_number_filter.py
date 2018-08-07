'''Number filter testcase'''
from unittest import TestCase

from purewords.filters import number_filter


class TestNumberFilterClass(TestCase):

    def setUp(self):
        self.filter = number_filter

    def test_number_filter(self):
        sentence = '我要喝八冰綠，一共25元'
        answer = '我要喝八冰綠，一共_num_元'
        self.assertEqual(
            answer,
            self.filter(sentence)
        )
