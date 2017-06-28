'''base filter collection'''
from abc import abstractmethod


class BaseFilterCollection(object):

    def __init__(self):
        self.filter_collection = []

    def add(self, filter_object):
        self.filter_collection.append(filter_object)

    def summary(self):
        for num, filter_object in enumerate(self.filter_collection):
            print('{}: {}'.format(num, str(filter_object)))

    def get_size(self):
        return len(self.filter_collection)

    def __call__(self, sentence):
        if isinstance(sentence, str):
            for num, filter_object in enumerate(self.filter_collection):
                sentence = filter_object(sentence)
            return sentence
        else:
            raise TypeError('sentence must be a string')
