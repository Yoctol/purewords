import unittest

from purewords.tokenizer import YoctolTokenizer


class TestYoctolJiebaClass(unittest.TestCase):

    def setUp(self):
        self.yoctol_jieba = YoctolTokenizer()

    def test_cut(self):
        sentence = "有顆頭是優拓資訊的好夥伴_"
        answer = ['有顆頭', '是', '優拓資訊', '的', '好', '夥伴']
        self.assertEqual(answer, self.yoctol_jieba.cut(sentence))
