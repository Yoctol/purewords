'''jieba tokenizer testcases'''
from unittest import TestCase
from unittest.mock import patch

from purewords.tokenizer import JiebaTokenizer


class TestJiebaTokenizerClass(TestCase):

    def setUp(self):
        self.tokenizer = JiebaTokenizer()

    def test_cut(self):
        sentence = "你好嗎？_我很好。"
        result = self.tokenizer.cut(sentence)
        self.assertTrue(len(result) > 0)
        self.assertNotIn('_', result)

    @patch('jieba.Tokenizer.add_word')
    def test_add_word(self, patch_add_word):
        new_word = '哈哈'
        self.tokenizer.add_word(new_word)
        patch_add_word.assert_called_once_with(new_word, None, None)

    @patch('jieba.Tokenizer.add_word')
    def test_add_words(self, patch_add_word):
        new_words = [str(i) for i in range(10)]
        self.tokenizer.add_words(new_words)
        self.assertEqual(
            patch_add_word.call_count,
            10
        )
