# -*- coding: utf-8 -*-

import re


def word_length(sentence):
    return sentence.count(' ') + 1


def tokenize_sentence_and_filte_tokens(
        text_str,
        tokenizer,
        token_filters,
    ):
    tokenized_text_lst = tokenizer.cut(text_str)
    filted_tokens = []
    for token in tokenized_text_lst:
        filted_tokens.append(
            token_filters(token)
        )

    while ' ' in filted_tokens:
        filted_tokens.remove(' ')
    while '' in filted_tokens:
        filted_tokens.remove('')
    return ' '.join(filted_tokens)


def set_sentence_splitting_token(sentence):
    sentence = re.sub('[^\w\d ]', ';', sentence)
    sentence = re.sub(';+', ';', sentence)
    sentence = re.sub('^;+|;+$', '', sentence)
    sentence = re.sub(' +', ' ', sentence)
    sentence = re.sub('^ +| +$', '', sentence)
    return sentence.lower()


def clean_sentence_splitting_token(sentence):
    sentence = re.sub(';', ' ', sentence)
    sentence = re.sub(' +', ' ', sentence)
    sentence = re.sub('^ +| +$', '', sentence)
    return sentence.lower()


def split_sentence(
        sentence,
        min_sentence_length=30,
        max_sentence_length=200
):
    splitted_sentences = []
    sentence = re.sub(' ;', ';', sentence)
    short_sentences = sentence.split(';')
    short_sentence_list = []
    sentence_length = 0
    for short_sentence in short_sentences:
        short_sentence_length = word_length(short_sentence)
        if sentence_length + short_sentence_length < max_sentence_length:
            sentence_length += short_sentence_length
            short_sentence_list.append(short_sentence)
        elif sentence_length < min_sentence_length:
            short_sentence_list.append(short_sentence)
            splitted_sentences.append(' '.join(short_sentence_list))
            short_sentence_list = []
            sentence_length = 0
        else:
            splitted_sentences.append(' '.join(short_sentence_list))
            short_sentence_list = [short_sentence]
            sentence_length = short_sentence_length
    if sentence_length > 0 and sentence_length < min_sentence_length:
        splitted_sentences[-1] += ' ' + ' '.join(short_sentence_list)
    elif sentence_length >= min_sentence_length:
        splitted_sentences.append(' '.join(short_sentence_list))
    return splitted_sentences


def split_document(
        document,
        tokenizer,
        token_filters,
        min_sentence_length=30,
        max_sentence_length=200
):
    confident_splitting_tokens = [
        '。', '\n', '\\\\n',
        '！', '\![^\w\d]',
        '？', '\?[^\w\d]',
        '\.[^\w\d]'
    ]
    sentences = re.split('|'.join(confident_splitting_tokens), document)
    clean_sentences = []
    for sentence in sentences:
        sentence = set_sentence_splitting_token(sentence)
        sentence = tokenize_sentence_and_filte_tokens(
            sentence,
            tokenizer,
            token_filters
        )
        sentence = re.sub(' ; ', ' ;', sentence)
        sentence_word_length = word_length(sentence)
        if sentence_word_length < min_sentence_length:
            continue
        elif sentence_word_length > max_sentence_length:
            splitted_sentences = split_sentence(
                sentence,
                min_sentence_length,
                max_sentence_length
            )
            for splitted_sentence in splitted_sentences:
                clean_sentences.append(splitted_sentence)
        else:
            sentence = clean_sentence_splitting_token(sentence)
            clean_sentences.append(sentence)
    return clean_sentences
