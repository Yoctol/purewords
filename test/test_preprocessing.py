import unittest
from purewords.preprocessing import set_sentence_splitting_token
from purewords.preprocessing import clean_sentence_splitting_token
from purewords.preprocessing import tokenize_sentence_and_filte_tokens
from purewords.preprocessing import split_document
from purewords.preprocessing import split_sentence

from purewords.tokenizer import WhitespaceTokenizer


class TestPreprocessingClass(unittest.TestCase):

    def setUp(self):
        self.tokenizer = WhitespaceTokenizer()

        def token_filters(sentence):
            return sentence

        self.token_filters = token_filters

    def test_clean_notation(self):
        sentence = "@@哈哈!!你看看你。＃＃>''<好棒棒++\n"
        answer = "哈哈 你看看你 好棒棒"
        sentence = set_sentence_splitting_token(sentence)
        sentence = clean_sentence_splitting_token(sentence)
        self.assertEqual(answer, sentence)

    def test_split_document(self):
        document = "周：假裝我們還在一塊 我真的演不出來　　\\n還是不習慣你不在 這身份轉變太快"\
                   + "? 張：畫面裡不需要旁白 卻誰都看得出來　　。是我情緒湧了上來 想哭卻一片空白"
        answers = [
            "周 假裝我們還在一塊 我真的演不出來", "還是不習慣你不在 這身份轉變太快",
            "張 畫面裡不需要旁白 卻誰都看得出來", "是我情緒湧了上來 想哭卻一片空白"
        ]
        self.assertEqual(
            answers,
            split_document(
                document,
                self.tokenizer,
                self.token_filters,
                min_sentence_length=2
            )
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
            split_sentence(
                sentence,
                min_sentence_length=5,
                max_sentence_length=5
            )
        )

    def test_tokenize_sentence(self):
        sentence = "  Hi Hi my_computer is perfect!! _ "
        answers = 'Hi Hi my_computer is perfect!!'
        self.assertEqual(
            answers,
            tokenize_sentence_and_filte_tokens(
                sentence,
                self.tokenizer,
                self.token_filters
            )
        )
