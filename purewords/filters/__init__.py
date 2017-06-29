from .pattern_replace_filter import PatternReplaceFilter
from .recursive_replace_filter import RecursiveReplaceFilter
from .word_replace_filter import WordReplaceFilter

from .url_filter import UrlFilter
from .time_filter import TimeFilter
from .phone_filter import PhoneFilter
from .stopwords_filter import StopwordsFilter
from .title_filter import TitleFilter
from .abbreviation_filter import AbbreviationFilter

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
