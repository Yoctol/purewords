'''url filter'''
from .pattern_replace_filter import PatternReplaceFilter

class UrlFilter(PatternReplaceFilter):

    def __init__(self, replacement='_url_'):
        url_patterns = [
            "((http|ftp).+?(?=([^a-zA-Z&,\-!\d./?:;#%=]|$)))",
            "([a-zA-Z&,!\d\-./@?;:#%=]+?\.com.*?(?=([^a-zA-Z\d\-!&,./@?;:#%=]|$)))",
            "([a-zA-Z&,!\d\-./@?;:#%=]+?@.*?(?=([^a-zA-Z\d!\-&,./@?;:#%=]|$)))"
        ]
        super(UrlFilter, self).__init__(
            url_patterns,
            replacement
        )
