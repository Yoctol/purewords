# -*- coding: utf-8 -*-
import re

def cut_sentence(text_str, tokenizer):
    tokenized_text_lst = tokenizer.cut(text_str)
    while ' ' in tokenized_text_lst:
        tokenized_text_lst.remove(' ')
    return ' '.join(tokenized_text_lst)

def clean_notation(sentence):
    sentence = re.sub('[^\w\d]', ' ', sentence)
    sentence = re.sub(' +', ' ', sentence)
    sentence = re.sub('^ +| +$', '', sentence)
    return sentence.lower()

def split_sentence(sentence, min_sen_len=30, max_sen_len=200):
    splitted_sentences = []
    sub_sents = sentence.split(' ')
    sub_sent_list = []
    sen_len = 0
    for sub_sent in sub_sents:
        if sen_len + len(sub_sent) < max_sen_len:
            sen_len += len(sub_sent)
            sub_sent_list.append(sub_sent)
        elif sen_len < min_sen_len:
            sub_sent_list.append(sub_sent)
            splitted_sentences.append(' '.join(sub_sent_list))
            sub_sent_list = []
            sen_len = 0
        else:
            splitted_sentences.append(' '.join(sub_sent_list))
            sub_sent_list = [sub_sent]
            sen_len = len(sub_sent)
    if sen_len > 0 and sen_len < min_sen_len:
        splitted_sentences[-1] += ' ' + ' '.join(sub_sent_list)
    elif sen_len >= min_sen_len:
        splitted_sentences.append(' '.join(sub_sent_list))
    return splitted_sentences

def split_document(document, min_sen_len=30, max_sen_len=200):
    confident_splitting_tokens = [
        '。', '\n', '\\\\n',
        '！', '\![^\w\d]',
        '？', '\?[^\w\d]',
        '\.[^\w\d]'
    ]
    sentences = re.split('|'.join(confident_splitting_tokens), document)
    clean_sentences = []
    for sentence in sentences:
        sentence = clean_notation(sentence)
        if len(sentence) < min_sen_len:
            continue
        elif len(sentence) > max_sen_len:
            splitted_sentences = split_sentence(
                sentence, min_sen_len, max_sen_len
            )
            for splitted_sentence in splitted_sentences:
                clean_sentences.append(splitted_sentence)
        else:
            clean_sentences.append(sentence)
    return clean_sentences

def remove_url(document):
    url_patterns = [
        "(http.+?(?=(\n| |$)))", "( [^ ]+?\.com.*?(?=(\n| |$)))"
    ]
    return re.sub('|'.join(url_patterns), '', document)

def remove_time(document):
    time_patterns = [
        "(\d\d:\d\d)", "(\d\d\d\d-\d\d-\d\d)", "(\d{7,8})"
    ]
    return re.sub('|'.join(time_patterns), '', document)

def remove_phone_number(document):
    phone_patterns = [
        "(\d\d\d\d-\d\d\d-\d\d\d)", "(\d\d-\d\d\d\d-\d\d\d\d)",
        "(\d\d-\d\d\d-\d\d\d\d)"
    ]
    return re.sub('|'.join(phone_patterns), '', document)

def replace_title(document):
    document = re.sub("Mr. ", "Mr ", document)
    document = re.sub("Mrs. ", "Mrs ", document)
    document = re.sub("Ms. ", "Ms ", document)
    document = re.sub("ma'am", "madam", document)
    return document

def replace_abbreviation(document):
    document = re.sub("I'm ", "I am ", document)
    document = re.sub("(Y|y)ou're ", "you are ", document)
    document = re.sub("'s ", "", document)
    document = re.sub("'ll ", " will ", document)
    document = re.sub("'d ", " would ", document)
    return document

def remove_angle_brackets(document):
    return re.sub("<.+?>", "", document)

def remove_meaning_notation(config, document):
    if config['remove_url']:
        document = remove_url(document)

    if config['remove_time']:
        document = remove_time(document)

    if config['remove_phone_number']:
        document = remove_phone_number(document)

    if config['replace_title']:
        document = replace_title(document)

    if config['replace_abbreviation']:
        document = replace_abbreviation(document)

    if config['remove_angle_brackets']:
        document = remove_angle_brackets(document)
    return document

def remove_stopwords(sentence, stopwords_set):
    stopwords_pattern = '|'.join(stopwords_set)
    sentence = re.sub(stopwords_pattern, '', sentence)
    sentence = re.sub('^ *$', '', sentence)
    return sentence
