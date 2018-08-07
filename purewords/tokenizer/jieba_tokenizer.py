import os.path

from jieba import Tokenizer, setLogLevel

from .base_tokenizer import BaseTokenizer


class JiebaTokenizer(BaseTokenizer):

    def __init__(self):
        file_path = os.path.abspath(__file__)
        file_dir = os.path.dirname(file_path)
        setLogLevel(0)

        self.tokenizer = Tokenizer()
        self.tokenizer.set_dictionary(
            os.path.join(
                file_dir,
                'dict.txt.big.txt'
            )
        )

        specific_tokens = [
            '_url_',
            '_num_',
            '_phone_',
            '_time_'
        ]
        self.add_words(specific_tokens)

    def cut(self, sentence):
        splitted_tokens = self.tokenizer.lcut(sentence)
        while '_' in splitted_tokens:
            splitted_tokens.remove('_')
        return splitted_tokens

    def add_word(self, word, freq=None, tag=None):
        self.tokenizer.add_word(word, freq, tag)
        self.tokenizer.suggest_freq(word, tune=True)

    def add_words(self, words, freq=None, tag=None):
        for word in words:
            self.add_word(word, freq, tag)
