import re
import os.path
import importlib

from .preprocessing import remove_meaning_notation
from .preprocessing import remove_stopwords
from .preprocessing import split_document
from .preprocessing import cut_sentence


class PureWords(object):

    def __init__(self, tokenizer='yoctol_jieba',
            remove_url=True, remove_time=True,
            remove_phone_number=True, replace_title=True,
            replace_abbreviation=True, remove_angle_brackets=True,
            stopwords_path='configs/stopwords.txt', max_len=200,
            min_len=1
        ):
        self.config = {}
        self.config['tokenizer'] = tokenizer
        self.config['remove_url'] = remove_url
        self.config['remove_time'] = remove_time
        self.config['remove_phone_number'] = remove_phone_number
        self.config['replace_title'] = replace_title
        self.config['replace_abbreviation'] = replace_abbreviation
        self.config['remove_angle_brackets'] = remove_angle_brackets
        self.config['stopwords_path'] = stopwords_path
        self.config['max_len'] = max_len
        self.config['min_len'] = min_len

        purewords_path = os.path.abspath(__file__)
        purewords_dir = os.path.dirname(purewords_path)

        stopwords_path = os.path.join(
            purewords_dir, self.config['stopwords_path']
        )
        with open(stopwords_path, 'r') as stopwords_file:
            self.stopwords_set = set(stopwords_file.read().splitlines())

        module = importlib.import_module('purewords.tokenizer.' + self.config['tokenizer'])
        tokenizer = getattr(module, self.config['tokenizer'])
        self.tokenizer = tokenizer()

    def clean_sentence(self, sentence):
        sentences = self.clean_document(sentence)
        return ' '.join(sentences)

    def clean_document(self, document):
        document = remove_meaning_notation(self.config, document)
        document = remove_stopwords(document, self.stopwords_set)
        sentences = split_document(
            document, self.config['min_len'], self.config['max_len']
        )
        tokenized_sentences = []

        for sentence in sentences:
            tokenized_sentences.append(
                cut_sentence(sentence, self.tokenizer)
            )
        return tokenized_sentences


pure_words = PureWords()

clean_sentence = pure_words.clean_sentence
clean_document = pure_words.clean_document
