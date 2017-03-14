
class whitespace_tokenizer(object):

    def cut(self, sentence):
        splitted_tokens =  sentence.split(' ')
        while '_' in splitted_tokens:
            splitted_tokens.remove('_')
        return splitted_tokens
