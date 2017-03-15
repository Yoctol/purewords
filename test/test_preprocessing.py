import unittest
from purewords.preprocessing import clean_notation
from purewords.preprocessing import cut_sentence
from purewords.preprocessing import remove_angle_brackets
from purewords.preprocessing import remove_phone_number
from purewords.preprocessing import remove_stopwords
from purewords.preprocessing import remove_time
from purewords.preprocessing import remove_url
from purewords.preprocessing import replace_abbreviation
from purewords.preprocessing import replace_title
from purewords.preprocessing import split_document
from purewords.preprocessing import split_sentence

from purewords.tokenizer.whitespace_tokenizer import whitespace_tokenizer

class TestPreprocessingClass(unittest.TestCase):

    def setUp(self):
        self.tokenizer = whitespace_tokenizer()

    def test_clean_notation(self):
        sentence = "@@哈哈!!你看看你。＃＃>''<好棒棒++\n"
        answer = "哈哈 你看看你 好棒棒"
        self.assertEqual(answer, clean_notation(sentence))

    def test_remove_angle_brackets(self):
        sentence = "<br>CPH<<阿阿>GG啦,要被清掉啦<>ob'_'ov>"
        answer = "CPH"
        self.assertEqual(answer, remove_angle_brackets(sentence))

    def test_remove_phone_number(self):
        sentence = "薄餡手機是:0912345678, 家電請打:02-2266-2266或08-449-5978"
        answer = "薄餡手機是:, 家電請打:或"
        self.assertEqual(answer, remove_phone_number(sentence))

    def test_remove_stopwords(self):
        sentence = "我講話很喜歡加的啦，你知道的啦，我家有養一隻狗的啦。"
        answer = "我講話很喜歡加，你知道，我家有養一隻狗。"
        stopwords_set = set(['的', '啦'])
        self.assertEqual(answer, remove_stopwords(sentence, stopwords_set))

    def test_remove_time(self):
        sentence = "今天是2018-02-30日，也是1070230，又是20180230, 早上07:30，全國放假一天"
        answer = "今天是日，也是，又是, 早上，全國放假一天"
        self.assertEqual(answer, remove_time(sentence))

    def test_remove_url(self):
        sentence = "我們的官網是http://www.yoctol.com.tw，有問題可以寄信至service@yoctol.com" \
                   + "或寄信到email@yoctol.edu.tw"
        answer = "我們的官網是，有問題可以寄信至或寄信到"
        self.assertEqual(answer, remove_url(sentence))

    def test_replace_abbreviation(self):
        sentence = "I'm Mr. Qoo. She's Mrs. M. You're great. I'd and I'll like to show you something"
        answer = "I am Mr. Qoo. She Mrs. M. you are great. I would and I will like to show you something"
        self.assertEqual(answer, replace_abbreviation(sentence))

    def test_replace_title(self):
        sentence = "I'm Mr. Qoo. She's Mrs. M. Hello ma'am. I'd and I'll like to show you something"
        answer = "I'm Mr Qoo. She's Mrs M. Hello madam. I'd and I'll like to show you something"
        self.assertEqual(answer, replace_title(sentence))

    def test_split_document(self):
        document = "周：假裝我們還在一塊 我真的演不出來　　\\n還是不習慣你不在 這身份轉變太快"\
                   + "? 張：畫面裡不需要旁白 卻誰都看得出來　　。是我情緒湧了上來 想哭卻一片空白"
        answers = [
            "周 假裝我們還在一塊 我真的演不出來", "還是不習慣你不在 這身份轉變太快",
            "張 畫面裡不需要旁白 卻誰都看得出來", "是我情緒湧了上來 想哭卻一片空白"
        ]
        self.assertEqual(answers, split_document(document, min_sen_len=2))

    def test_split_sentence(self):
        sentence = "周 假裝我們還在一塊 我真的演不出來 還是不習慣你不在 這身份轉變太快 "\
                   + "張 畫面裡不需要旁白 卻誰都看得出來 是我情緒湧了上來 想哭卻一片空白"
        answers = [
            "周 假裝我們還在一塊 我真的演不出來", "還是不習慣你不在 這身份轉變太快",
            "張 畫面裡不需要旁白 卻誰都看得出來", "是我情緒湧了上來 想哭卻一片空白"
        ]
        self.assertEqual(answers, split_sentence(sentence, min_sen_len=10, max_sen_len=15))

    def test_cut_sentence(self):
        sentence = "  Hi Hi my_computer is perfect!! _ "
        answers = 'Hi Hi my_computer is perfect!!'
        self.assertEqual(answers, cut_sentence(sentence, self.tokenizer))
