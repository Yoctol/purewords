'''base tokenizer'''
from abc import abstractmethod


class BaseTokenizer(object):

    @abstractmethod
    def cut(self, sentence):
        pass
