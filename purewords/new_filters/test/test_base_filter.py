# -*- coding: utf-8 -*-
import re
from unittest import TestCase

from ..base_pattern_filter import BaseFilter


class TestBaseFilter(TestCase):

    def test_created_base_filter(self):
        base_filter = BaseFilter()
        self.assertEqual({'record': None}, base_filter.__dict__)

    def test_is_sentence_to_be_retrieved(self):
        def replace(sentence):
            return re.sub('A', '@', sentence)
        BaseFilter.is_sentence_to_be_retrieved(
            sentence_to_be_filtered='PPAV真厲害',
            sentence_to_be_retrieved='PP@V真厲害',
            func_replace=replace,
        )
        with self.assertRaises(KeyError):
            BaseFilter.is_sentence_to_be_retrieved(
                sentence_to_be_filtered='PPBV真厲害',
                sentence_to_be_retrieved='PP@V真厲害',
                func_replace=replace,
            )
