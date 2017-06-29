'''Phone Filter'''
from .pattern_replace_filter import PatternReplaceFilter

class PhoneFilter(PatternReplaceFilter):

    def __init__(self, replacement='_phone_'):
        phone_patterns = [
            "(0800-{0,1}\d\d\d-{0,1}\d\d\d)",
            "(02-{0,1}\d\d\d\d-{0,1}\d\d\d\d)",
            "(0[3-8]-{0,1}\d\d\d-{0,1}\d\d\d\d)",
            "(09\d\d-{0,1}\d\d\d-{0,1}\d\d\d)"
        ]
        super(PhoneFilter, self).__init__(
            phone_patterns,
            replacement
        )
