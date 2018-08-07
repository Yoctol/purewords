from .pattern_replace_filter import PatternReplaceFilter  # noqa
from .recursive_replace_filter import RecursiveReplaceFilter  # noqa
from .word_replace_filter import WordReplaceFilter  # noqa
from .stopwords_filter import StopwordsFilter  # noqa


url_filter = PatternReplaceFilter(
    patterns=[
        "((http|ftp).+?(?=([^a-zA-Z&,\-!\d./?:;#%=]|$)))",
        "([a-zA-Z&,!\d\-./@?;:#%=]+?\.com.*?(?=([^a-zA-Z\d\-!&,./@?;:#%=]|$)))",
        "([a-zA-Z&,!\d\-./@?;:#%=]+?@.*?(?=([^a-zA-Z\d!\-&,./@?;:#%=]|$)))"
    ],
    replacement='_url_'
)

time_filter = PatternReplaceFilter(
    patterns=[
        "([0-2]\d:[0-5]\d)",
        "(20\d\d-{0,1}[0-1]\d-{0,1}[0-3]\d)",
        "1[0-1]\d-{0,1}[0-1]\d-{0,1}[0-3]\d"
    ],
    replacement='_time_'
)

phone_filter = PatternReplaceFilter(
    patterns=[
        "(0800-{0,1}\d\d\d-{0,1}\d\d\d)",
        "(02-{0,1}\d\d\d\d-{0,1}\d\d\d\d)",
        "(0[3-8]-{0,1}\d\d\d-{0,1}\d\d\d\d)",
        "(09\d\d-{0,1}\d\d\d-{0,1}\d\d\d)"
    ],
    replacement='_phone_'
)

title_filter = WordReplaceFilter(
    replace_dictionary={
        "Mr\. ": "Mr ",
        "Mrs\. ": "Mrs ",
        "Ms\. ": "Ms ",
        "ma'am": "madam"
    }
)

abbreviation_filter = WordReplaceFilter(
    replace_dictionary={
        "I'm ": "I am ",
        "(Y|y)ou're ": "you are ",
        "'s ": " ",
        "'ll |’ll ": " will ",
        "'d |’d ": " would "
    }
)

number_filter = PatternReplaceFilter(
    patterns=['\d+'],
    replacement='_num_'
)

angle_brackets_filter = RecursiveReplaceFilter(
    pattern="<[^<>]*?>",
)

blank_filter = PatternReplaceFilter(
    patterns=['_{2,}'],
    replacement='_'
)

token_number_filter = PatternReplaceFilter(
    patterns=['^\d+$'],
    replacement='_num_'
)
