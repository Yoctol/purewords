class BaseFilter(object):

    def __init__(self):
        self.record = None

    def replace(self, sentence: str)-> str:
        raise NotImplementedError

    def find(self, sentence: str)-> str:
        raise NotImplementedError

    def find_n_save(self, sentence: str)-> str:
        raise NotImplementedError

    def retrieve(self, sentence: str)-> str:
        raise NotImplementedError

    def lretrieve(self, tokenized_sentence: list) -> list:
        raise NotImplementedError

    @classmethod
    def is_sentence_to_be_retrieved(cls, sentence_to_be_filtered: str,
                                    sentence_to_be_retrieved: str,
                                    func_replace: object)-> None:
        filtered_sentence = func_replace(
            sentence=sentence_to_be_filtered,
        )
        if filtered_sentence != sentence_to_be_retrieved:
            raise KeyError(
                'The sentence to be retrieved is not the original sentence after filter.'
                'The sentence to be retrieved is "{},"'.format(
                    sentence_to_be_retrieved
                ),
                'but the sentence before filter is "{}".'.format(
                    sentence_to_be_filtered
                )
            )
