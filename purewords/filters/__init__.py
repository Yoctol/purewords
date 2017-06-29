from .pattern_replace_filter import PatternReplaceFilter
from .recursive_replace_filter import RecursiveReplaceFilter
from .word_replace_filter import WordReplaceFilter

from .stopwords_filter import StopwordsFilter

UrlFilter = PatternReplaceFilter(
    patterns=[
        "((http|ftp).+?(?=([^a-zA-Z&,\-!\d./?:;#%=]|$)))",
        "([a-zA-Z&,!\d\-./@?;:#%=]+?\.com.*?(?=([^a-zA-Z\d\-!&,./@?;:#%=]|$)))",
        "([a-zA-Z&,!\d\-./@?;:#%=]+?@.*?(?=([^a-zA-Z\d!\-&,./@?;:#%=]|$)))"
    ],
    replacement='_url_'
)

TimeFilter = PatternReplaceFilter(
    patterns=[
        "([0-2]\d:[0-5]\d)",
        "(20\d\d-{0,1}[0-1]\d-{0,1}[0-3]\d)",
        "1[0-1]\d-{0,1}[0-1]\d-{0,1}[0-3]\d"
    ],
    replacement='_time_'
)

PhoneFilter = PatternReplaceFilter(
    patterns=[
        "(0800-{0,1}\d\d\d-{0,1}\d\d\d)",
        "(02-{0,1}\d\d\d\d-{0,1}\d\d\d\d)",
        "(0[3-8]-{0,1}\d\d\d-{0,1}\d\d\d\d)",
        "(09\d\d-{0,1}\d\d\d-{0,1}\d\d\d)"
    ],
    replacement='_phone_'
)

TitleFilter = WordReplaceFilter(
    replace_dictionary={
        "Mr\. ":"Mr ",
        "Mrs\. ":"Mrs ",
        "Ms\. ":"Ms ",
        "ma'am":"madam"
    }
)

AbbreviationFilter = WordReplaceFilter(
    replace_dictionary={
        "I'm ":"I am ",
        "(Y|y)ou're ":"you are ",
        "'s ":" ",
        "'ll |’ll ":" will ",
        "'d |’d ":" would "
    }
)

NumberFilter = PatternReplaceFilter(
    patterns=['\d+'],
    replacement='_num_'
)

AngleBracketsFilter = RecursiveReplaceFilter(
    pattern="<[^<>]*?>",
)

BlankFilter = PatternReplaceFilter(
    patterns=['_{2,}'],
    replacement='_'
)
