'''Pattern replace base filter'''
import re

from .base_filter import BaseFilter


class PatternReplaceFilter(BaseFilter):

    def __init__(self, patterns=[], replacement=''):
        self.patterns = patterns
        self.replacement = replacement

    def add_pattern(self, pattern):
        self.patterns.append(pattern)

    def __call__(self, sentence):
        return re.sub(
            '|'.join(self.patterns),
            self.replacement,
            sentence
        )
