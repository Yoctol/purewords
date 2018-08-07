'''Time filter testcase'''
from unittest import TestCase

from purewords.filters import time_filter


class TestTimeFilterClass(TestCase):

    def setUp(self):
        self.filter = time_filter

    def test_time_filter(self):
        sentence = "今天是2018-02-30日，" \
                   + "也是1070230，又是20180230, " \
                   + "早上07:30，全國放假一天"
        answer = "今天是_time_日，也是_time_，" \
                 + "又是_time_, 早上_time_，全國放假一天"
        self.assertEqual(
            answer,
            self.filter(sentence)
        )
