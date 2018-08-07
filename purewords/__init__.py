from .preprocessing import split_document
from .tokenizer import YoctolTokenizer

from .filter_collection import document_filters
from .filter_collection import token_filters

yoctol_tokenizer = YoctolTokenizer()


class PureWords(object):

    def __init__(
            self,
            tokenizer=yoctol_tokenizer,
            document_filters=document_filters,
            token_filters=token_filters,
            max_len=200,
            min_len=1,
        ):
        self.max_len = max_len
        self.min_len = min_len

        self.tokenizer = tokenizer
        self.document_filters = document_filters
        self.token_filters = token_filters

    def clean_sentence(self, sentence):
        sentences = self.clean_document(sentence)
        return ' '.join(sentences)

    def clean_document(self, document):
        document = self.document_filters(document)
        sentences = split_document(
            document,
            self.tokenizer,
            self.token_filters,
            self.min_len,
            self.max_len
        )
        while '' in sentences:
            sentences.remove('')
        return sentences


def static_clean_document(
        document,
        document_filters,
        token_filters,
        min_len,
        max_len
    ):
    document = document_filters(document)
    sentences = split_document(
        document,
        yoctol_tokenizer,
        token_filters,
        min_len,
        max_len
    )
    while '' in sentences:
        sentences.remove('')
    return sentences


pure_words = PureWords()

clean_sentence = pure_words.clean_sentence
clean_document = pure_words.clean_document
