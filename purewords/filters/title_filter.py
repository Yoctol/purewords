'''Title filter'''
from .word_replace_filter import WordReplaceFilter

class TitleFilter(WordReplaceFilter):

    def __init__(self):
        title_dict = {
            "Mr. ":"Mr ",
            "Mrs. ":"Mrs ",
            "Ms. ":"Ms ",
            "ma'am":"madam"
        }
        super(TitleFilter, self).__init__(
            title_dict
        )
