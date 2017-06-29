'''default document filter collection'''
from .base_filter_collection import BaseFilterCollection

from purewords.filters import url_filter
from purewords.filters import time_filter
from purewords.filters import phone_filter
from purewords.filters import title_filter
from purewords.filters import abbreviation_filter
from purewords.filters import angleBrackets_filter
from purewords.filters import blank_filter
from purewords.filters import number_filter

document_filters = BaseFilterCollection()
document_filters.add(url_filter)
document_filters.add(blank_filter)
document_filters.add(time_filter)
document_filters.add(phone_filter)
document_filters.add(title_filter)
document_filters.add(abbreviation_filter)
document_filters.add(angle_brackets_filter)

token_filters = BaseFilterCollection()
token_filters.add(number_filter)
