'''Title filter testcases'''
from unittest import TestCase

from purewords.filters import TitleFilter

class TestTitleFilterClass(TestCase):

    def setUp(self):
        self.filter = TitleFilter()

    def test_title_filter(self):
        sentence = "I'm Mr. Qoo. She's Mrs. M. " \
                   + "Hello ma'am. I'd and I'll " \
                   + "like to show you something"
        answer = "I'm Mr Qoo. She's Mrs M. Hello madam. " \
                 + "I'd and I'll like to show you something"
        self.assertEqual(
            answer,
            self.filter(sentence)
        )
