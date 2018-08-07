from .base_tokenizer import BaseTokenizer


class WhitespaceTokenizer(BaseTokenizer):

    def cut(self, sentence):
        splitted_tokens = sentence.split(' ')
        while '_' in splitted_tokens:
            splitted_tokens.remove('_')
        return splitted_tokens
