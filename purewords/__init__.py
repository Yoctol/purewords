import re
import os.path
import importlib.util
import yaml

from .preprocessing import remove_meaning_notation
from .preprocessing import remove_stopwords
from .preprocessing import split_document
from .preprocessing import cut_sentence

purewords_path = os.path.abspath(__file__)
purewords_dir = os.path.dirname(purewords_path)

class PureWords(object):

    def __init__(self, config_path=None):
        if config_path is None:
            config_path = os.path.join(purewords_dir, 'configs/default.yml')
        config_file = open(config_path, 'r')

        self.config = yaml.load(config_file.read())
        config_file.close()

        stopwords_file = open(
            os.path.join(purewords_dir, self.config['stopwords_path']), 'r'
        )
        self.stopwords_set = set(stopwords_file.read().splitlines())
        stopwords_file.close()

        module = importlib.import_module('purewords.tokenizer.' + self.config['tokenizer'])
        tokenizer = getattr(module, self.config['tokenizer'])
        self.tokenizer = tokenizer()

    def clean_sentence(self, sentence):
        sentences = self.clean_document(sentence)
        return ' '.join(sentences)

    def clean_document(self, document):
        document = remove_meaning_notation(self.config, document)
        document = remove_stopwords(document, self.stopwords_set)
        sentences = split_document(
            document, self.config['min_len'], self.config['max_len']
        )
        tokenized_sentences = []

        for sentence in sentences:
            tokenized_sentences.append(
                cut_sentence(sentence, self.tokenizer)
            )
        return tokenized_sentences


pure_words = PureWords()

clean_sentence = pure_words.clean_sentence
clean_document = pure_words.clean_document
