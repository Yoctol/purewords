import unittest

from purewords.tokenizer import WhitespaceTokenizer


class TestWhiteSpaceTokenizer(unittest.TestCase):

    def setUp(self):
        self.whitespace_tokenizer = WhitespaceTokenizer()

    def test_cut(self):
        sentence = "Hello, my name is cph_cph. cph is _ wonderful."
        answer = [
            'Hello,', 'my', 'name', 'is', 'cph_cph.',
            'cph', 'is', 'wonderful.'
        ]
        self.assertEqual(answer, self.whitespace_tokenizer.cut(sentence))
