import unittest

from purewords.tokenizer.whitespace_tokenizer import whitespace_tokenizer

class TestWhiteSpaceTokenizer(unittest.TestCase):

    def setUp(self):
        self.whitespace_tokenizer = whitespace_tokenizer()

    def test_cut(self):
        sentence = "Hello, my name is cph_cph. cph is _ wonderful."
        answer = [
            'Hello,', 'my', 'name', 'is', 'cph_cph.',
            'cph', 'is', 'wonderful.'
        ]
        self.assertEqual(answer, self.whitespace_tokenizer.cut(sentence))
