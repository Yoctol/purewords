# -*- coding: utf-8 -*-

import re

def word_length(sentence):
    return sentence.count(' ') + 1

def tokenize_sentence(text_str, tokenizer):
    tokenized_text_lst = tokenizer.cut(text_str)
    while ' ' in tokenized_text_lst:
        tokenized_text_lst.remove(' ')
    while '' in tokenized_text_lst:
        tokenized_text_lst.remove('')
    return ' '.join(tokenized_text_lst)

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
        sentence = tokenize_sentence(sentence, tokenizer)
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

def replace_url(document):
    url_patterns = [
        "((http|ftp).+?(?=([^a-zA-Z&,\-!\d./?:;#%=]|$)))",
        "([a-zA-Z&,!\d\-./@?;:#%=]+?\.com.*?(?=([^a-zA-Z\d\-!&,./@?;:#%=]|$)))",
        "([a-zA-Z&,!\d\-./@?;:#%=]+?@.*?(?=([^a-zA-Z\d!\-&,./@?;:#%=]|$)))"
    ]
    return re.sub('|'.join(url_patterns), '_url_', document)

def replace_time(document):
    time_patterns = [
        "([0-2]\d:[0-5]\d)", "(20\d\d-{0,1}[0-1]\d-{0,1}[0-3]\d)",
        "1[0-1]\d-{0,1}[0-1]\d-{0,1}[0-3]\d"
    ]
    return re.sub('|'.join(time_patterns), '_time_', document)

def replace_phone_number(document):
    phone_patterns = [
        "(0800-{0,1}\d\d\d-{0,1}\d\d\d)", "(02-{0,1}\d\d\d\d-{0,1}\d\d\d\d)",
        "(0[3-8]-{0,1}\d\d\d-{0,1}\d\d\d\d)", "(09\d\d-{0,1}\d\d\d-{0,1}\d\d\d)"
    ]
    return re.sub('|'.join(phone_patterns), '_phone_', document)

def replace_number(document):
    return re.sub(r'\d+', '_number_', document)

def replace_title(document):
    document = re.sub("Mr. ", "Mr ", document)
    document = re.sub("Mrs. ", "Mrs ", document)
    document = re.sub("Ms. ", "Ms ", document)
    document = re.sub("ma'am", "madam", document)
    return document

def replace_abbreviation(document):
    document = re.sub("I'm ", "I am ", document)
    document = re.sub("(Y|y)ou're ", "you are ", document)
    document = re.sub("'s ", " ", document)
    document = re.sub("'ll |’ll ", " will ", document)
    document = re.sub("'d |’d ", " would ", document)
    return document

def remove_angle_brackets(document):
    while re.search("<[^<>]*?>", document) is not None:
        document = re.sub("<[^<>]*?>", "", document)
    return document

def remove_blank(document):
    return re.sub('_{2,}', '_', document)

def remove_meaning_notation(config, document):
    if config['replace_url']:
        document = replace_url(document)

    if config['remove_blank']:
        document = remove_blank(document)

    if config['replace_time']:
        document = replace_time(document)

    if config['replace_phone_number']:
        document = replace_phone_number(document)

    if config['replace_title']:
        document = replace_title(document)

    if config['replace_abbreviation']:
        document = replace_abbreviation(document)

    if config['remove_angle_brackets']:
        document = remove_angle_brackets(document)

    if config['replace_number']:
        document = replace_number(document)

    return document

def remove_stopwords(sentence, stopwords_set):
    stopwords_pattern = '|'.join(stopwords_set)
    sentence = re.sub(stopwords_pattern, '', sentence)
    sentence = re.sub('^ *$', '', sentence)
    return sentence
