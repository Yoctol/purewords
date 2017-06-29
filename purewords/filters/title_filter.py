'''Title filter'''
from .word_replace_filter import WordReplaceFilter

class TitleFilter(WordReplaceFilter):

    def __init__(self):
        title_dict = {
            r"Mr. ":"Mr ",
            r"Mrs. ":"Mrs ",
            r"Ms. ":"Ms ",
            r"ma'am":"madam"
        }
        super(TitleFilter, self).__init__(
            title_dict
        )
