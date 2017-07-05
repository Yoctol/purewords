'''Stopwords filter'''
from .pattern_replace_filter import PatternReplaceFilter


class StopwordsFilter(PatternReplaceFilter):

    def __init__(self, stopwords_set):
        super(StopwordsFilter, self).__init__(
            list(stopwords_set),
        )
