'''Phone filter_ testcases'''
from unittest import TestCase

from purewords.filters import phone_filter


class TestPhoneFilterClass(TestCase):

    def setUp(self):
        self.filter_ = phone_filter

    def test_phone_filter_(self):
        sentence = "薄餡手機是:0912345678, " \
                   + "家電請打:02-2266-2266或08-449-5978"
        answer = "薄餡手機是:_phone_, 家電請打:_phone_或_phone_"
        self.assertEqual(
            answer,
            self.filter_(sentence)
        )

    # def test_invertible(self):
    #     sentence = "薄餡手機是:0912345678, " \
    #                + "家電請打:02-2266-2266或08-449-5978"
    #     answer = "薄餡手機是:_phone_, 家電請打:_phone_或_phone_"
    #     self.assertEqual(
    #         answer,
    #         self.filter_.go_forward(sentence, False)
    #     )
    #     self.assertEqual(
    #         sentence,
    #         self.filter_.go_backward(answer, False)
    #     )
