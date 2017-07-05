'''Word replace base filter'''
import re

from .base_filter import BaseFilter


class WordReplaceFilter(BaseFilter):

    def __init__(self, replace_dictionary={}):
        self.replace_dictionary = replace_dictionary

    def add_replacement(self, word, replacement=''):
        self.replace_dictionary[word] = replacement

    def __call__(self, sentence):
        for pattern, replacement in self.replace_dictionary.items():
            sentence = re.sub(
                pattern,
                replacement,
                sentence
            )
        return sentence
