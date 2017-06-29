import re
import os.path
import importlib

from .preprocessing import split_document
from .tokenizer import YoctolTokenizer

from .filters import StopwordsFilter
from .filter_collection import document_filters
from .filter_collection import token_filters

class PureWords(object):

    def __init__(
            self,
            tokenizer,
            document_filters=document_filters,
            token_filters=token_filters,
            stopwords_path='configs/stopwords.txt',
            max_len=200,
            min_len=1
        ):
        self.max_len = max_len
        self.min_len = min_len

        purewords_path = os.path.abspath(__file__)
        purewords_dir = os.path.dirname(purewords_path)

        stopwords_path = os.path.join(
            purewords_dir,
            stopwords_path
        )
        with open(stopwords_path, 'r') as stopwords_file:
            self.stopwords_set = set(stopwords_file.read().splitlines())

        self.tokenizer = tokenizer
        self.document_filters = document_filters
        self.document_filters.add(
            StopwordsFilter(self.stopwords_set)
        )
        self.token_filters = token_filters

    def clean_sentence(self, sentence):
        sentences = self.clean_document(sentence)
        return ' '.join(sentences)

    def clean_document(self, document):
        document = self.document_filters(document)
        sentences = split_document(
            document,
            self.tokenizer,
            self.token_filters,
            self.min_len,
            self.max_len
        )
        return sentences


pure_words = PureWords(YoctolTokenizer())

clean_sentence = pure_words.clean_sentence
clean_document = pure_words.clean_document
