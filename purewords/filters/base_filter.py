'''base filter'''
from abc import abstractmethod


class BaseFilter(object):

    @abstractmethod
    def __call__(self, sentence):
        pass
