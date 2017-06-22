import os.path

import jieba

from .base_tokenizer import BaseTokenizer

class JiebaTokenizer(BaseTokenizer):

    def __init__(self):
        file_path = os.path.abspath(__file__)
        file_dir = os.path.dirname(file_path)
        jieba.setLogLevel(0)
        jieba.set_dictionary(os.path.join(file_dir, 'dict.txt.big.txt'))

    def cut(self, sentence):
        splitted_tokens = jieba.lcut(sentence)
        while '_' in splitted_tokens:
            splitted_tokens.remove('_')
        return splitted_tokens

    def add_word(self, word, freq=None, tag=None):
        jieba.add_word(word, freq, tag)
        jieba.suggest_freq(word, tune=True)

    def add_words(self, words, freq=None, tag=None):
        for word in words:
            self.add_word(word, freq, tag)
