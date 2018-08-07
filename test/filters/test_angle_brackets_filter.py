'''Angle brackets filter testcases'''
from unittest import TestCase

from purewords.filters import angle_brackets_filter


class TestAngleBracketsFilterClass(TestCase):

    def setUp(self):
        self.filter = angle_brackets_filter

    def test_angle_brackets_filter(self):
        sentence = "<br>CPH<<阿阿>GG啦,要被清掉啦<>ob'_'ov>"
        answer = "CPH"
        self.assertEqual(
            answer,
            self.filter(sentence)
        )
