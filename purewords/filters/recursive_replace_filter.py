'''recursive replace base filter '''
import re

from .base_filter import BaseFilter


class RecursiveReplaceFilter(BaseFilter):

    def __init__(self, pattern='', replacement=''):
        self.pattern = pattern
        self.replacement = replacement

    def __call__(self, sentence):
        while re.search(self.pattern, sentence) is not None:
            sentence = re.sub(
                self.pattern,
                self.replacement,
                sentence
            )
        return sentence
