import unittest
from purewords.preprocessing import set_sentence_splitting_token
from purewords.preprocessing import clean_sentence_splitting_token
from purewords.preprocessing import tokenize_sentence
from purewords.preprocessing import remove_angle_brackets
from purewords.preprocessing import replace_phone_number
from purewords.preprocessing import remove_stopwords
from purewords.preprocessing import replace_time
from purewords.preprocessing import replace_url
from purewords.preprocessing import replace_abbreviation
from purewords.preprocessing import replace_title
from purewords.preprocessing import split_document
from purewords.preprocessing import split_sentence
from purewords.preprocessing import remove_blank
from purewords.preprocessing import replace_number

from purewords.tokenizer import WhitespaceTokenizer

class TestPreprocessingClass(unittest.TestCase):

    def setUp(self):
        self.tokenizer = WhitespaceTokenizer()

    def test_clean_notation(self):
        sentence = "@@哈哈!!你看看你。＃＃>''<好棒棒++\n"
        answer = "哈哈 你看看你 好棒棒"
        sentence = set_sentence_splitting_token(sentence)
        sentence = clean_sentence_splitting_token(sentence)
        self.assertEqual(answer, sentence)

    def test_remove_angle_brackets(self):
        sentence = "<br>CPH<<阿阿>GG啦,要被清掉啦<>ob'_'ov>"
        answer = "CPH"
        self.assertEqual(answer, remove_angle_brackets(sentence))

    def test_replace_phone_number(self):
        sentence = "薄餡手機是:0912345678, 家電請打:02-2266-2266或08-449-5978"
        answer = "薄餡手機是:_phone_, 家電請打:_phone_或_phone_"
        self.assertEqual(answer, replace_phone_number(sentence))

    def test_remove_stopwords(self):
        sentence = "我講話很喜歡加的啦，你知道的啦，我家有養一隻狗的啦。"
        answer = "我講話很喜歡加，你知道，我家有養一隻狗。"
        stopwords_set = set(['的', '啦'])
        self.assertEqual(answer, remove_stopwords(sentence, stopwords_set))

    def test_replace_time(self):
        sentence = "今天是2018-02-30日，也是1070230，又是20180230, 早上07:30，全國放假一天"
        answer = "今天是_time_日，也是_time_，又是_time_, 早上_time_，全國放假一天"
        self.assertEqual(answer, replace_time(sentence))

    def test_replace_url(self):
        sentence = "我們的官網是http://www.yoctol.com.tw，有問題可以寄信至service@yoctol.com" \
                   + "或寄信到email@yoctol.edu.tw"
        answer = "我們的官網是_url_，有問題可以寄信至_url_或寄信到_url_"
        self.assertEqual(answer, replace_url(sentence))

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
        self.assertEqual(
            answers,
            split_document(document, self.tokenizer, min_sen_len=2)
        )

    def test_split_sentence(self):
        sentence = "周;假裝 我們 還在 一塊 我 真的 演 不 出來;還是 不 習慣 你 不 在 這 身份 轉變 太快;"\
                   + "張;畫面 裡 不 需要 旁白 卻 誰 都 看得 出來;是 我 情緒 湧 了 上來 想 哭 卻 一片 空白"
        answers = [
            "周 假裝 我們 還在 一塊 我 真的 演 不 出來", "還是 不 習慣 你 不 在 這 身份 轉變 太快",
            "張 畫面 裡 不 需要 旁白 卻 誰 都 看得 出來", "是 我 情緒 湧 了 上來 想 哭 卻 一片 空白"
        ]
        self.assertEqual(
            answers,
            split_sentence(sentence, min_sen_len=5, max_sen_len=5)
        )

    def test_tokenize_sentence(self):
        sentence = "  Hi Hi my_computer is perfect!! _ "
        answers = 'Hi Hi my_computer is perfect!!'
        self.assertEqual(answers, tokenize_sentence(sentence, self.tokenizer))

    def test_remove_blank(self):
        sentence = 'Hello I am ______ blank!!'
        answer = 'Hello I am _ blank!!'
        self.assertEqual(answer, remove_blank(sentence))

    def test_remove_number(self):
        sentence = '我要喝八冰綠，一共25元'
        answer = '我要喝八冰綠，一共_number_元'
        self.assertEqual(answer, replace_number(sentence))
