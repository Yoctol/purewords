import re
import os.path
import importlib

from .preprocessing import remove_meaning_notation
from .preprocessing import remove_stopwords
from .preprocessing import split_document
from .preprocessing import tokenize_sentence
from .tokenizer import YoctolTokenizer

class PureWords(object):

    def __init__(self, tokenizer,
            replace_url=True, replace_time=True,
            replace_phone_number=True, replace_title=True,
            remove_blank=True, replace_abbreviation=True,
            remove_angle_brackets=True, replace_number=True,
            stopwords_path='configs/stopwords.txt', max_len=200,
            min_len=1
        ):
        self.config = {}
        self.config['tokenizer'] = tokenizer.__class__.__name__
        self.config['replace_url'] = replace_url
        self.config['remove_blank'] = remove_blank
        self.config['replace_time'] = replace_time
        self.config['replace_number'] = replace_number
        self.config['replace_phone_number'] = replace_phone_number
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

        self.tokenizer = tokenizer

    def clean_sentence(self, sentence):
        sentences = self.clean_document(sentence)
        return ' '.join(sentences)

    def clean_document(self, document):
        document = remove_meaning_notation(self.config, document)
        document = remove_stopwords(document, self.stopwords_set)
        sentences = split_document(
            document, self.tokenizer, self.config['min_len'], self.config['max_len']
        )
        return sentences


pure_words = PureWords(YoctolTokenizer())

clean_sentence = pure_words.clean_sentence
clean_document = pure_words.clean_document
