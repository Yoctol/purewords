'''abbreviation filter'''
from .word_replace_filter import WordReplaceFilter

class AbbreviationFilter(WordReplaceFilter):

    def __init__(self):
        abbreviation_dict = {
            "I'm ":"I am ",
            "(Y|y)ou're ":"you are ",
            "'s ":" ",
            "'ll |’ll ":" will ",
            "'d |’d ":" would "
        }
        super(AbbreviationFilter, self).__init__(
            abbreviation_dict
        )
