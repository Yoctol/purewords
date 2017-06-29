'''Time filter'''
from .pattern_replace_filter import PatternReplaceFilter

class TimeFilter(PatternReplaceFilter):

    def __init__(self, replacement='_time_'):
        time_patterns = [
            "([0-2]\d:[0-5]\d)",
            "(20\d\d-{0,1}[0-1]\d-{0,1}[0-3]\d)",
            "1[0-1]\d-{0,1}[0-1]\d-{0,1}[0-3]\d"
        ]
        super(TimeFilter, self).__init__(
            time_patterns,
            replacement
        )
