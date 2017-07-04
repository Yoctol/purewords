'''Pattern replace base filter'''
import re
from .base_filter import BaseFilter


class PatternReplaceFilter(BaseFilter):

    def __init__(self, patterns=[], replacement=''):
        self.patterns = patterns
        self.replacement = replacement

    def add_pattern(self, pattern):
        self.patterns.append(pattern)

    @staticmethod
    def show_process(from_item, to_item, verbose):
        if verbose:
            print('Replace from {} to {}'.format(from_item, to_item))

    def store_matches_of_pattern(self, sentence, verbose):
        self.matches = re.findall('|'.join(self.patterns), sentence)
        if verbose:
            print('All matches are: {}'.format(self.matches))

    def do_replacement(self, sentence):
        return re.sub(
            '|'.join(self.patterns),
            self.replacement,
            sentence
        )

    def go_forward(self, sentence, verbose):
        self.store_matches_of_pattern(sentence, verbose)
        output_sentence = self.do_replacement(sentence)
        show_process(sentence, output_sentence, verbose)
        self.forward = True
        return output_sentence

    def go_backward(self, sentence, verbose):
        if self.forward is not True:
            raise PermissionError(
                'You should run go_forward before running go_backward.')

        if isinstance(sentence, str):
            sentence_copy = sentence
            shift = 0
            for match in self.matches:
                m = re.search(self.replacement, sentence_copy)
                if m is not None:
                    show_process(
                        sentence[m.start(0) + shift: m.end(0) + shift],
                        match, verbose)
                    sentence[m.start(0) + shift: m.end(0) + shift] = match
                    sentence_copy = sentence_copy[m.end(0):]
                    shift += m.end(0)
                else:
                    raise ValueError('{} not Found in this sentence {}'.format(
                        self.replacement, sentence))
        elif isinstance(sentence, list):
            matches_copy = self.matches
            for idx, token in enumerate(sentence):
                if token == self.replacement:
                    show_process(sentence[idx], matches_copy[0], verbose)
                    sentence[idx] = matches_copy[0]
                    matches_copy = matches_copy[1:]
        return sentence

    def __call__(self, sentence, invertible, mode='forward', verbose=True):
        if invertible is True:
            if mode == 'forward':
                return self.go_forward(sentence, verbose)
            elif mode == 'backward':
                return self.go_backward(sentence, verbose)

        elif invertible is False:
            return self.do_replacement(sentence)
