import os.path

import jieba

frequent_proper_nouns = [
    "有顆頭", "優拓", "優拓資訊", "機器學習", "人工智慧", "機器人",
    "客服", "推薦系統", "深度學習", "資料科學家", "資料科學",
    "自然語言處理",]

common_proper_nouns = [
    "物連網", "溝通", "橋樑", "部落格", "粉專", "頁面",
]

frequent_eng_proper_nouns = [
    "Yoctol Info", "YoctolInfo", "yoctol", "Yoctol",
    "aloha.ai", "Aloha.AI",
    "machine learning", "Machine Learning",
    "deep learning", "Deep Learning",
    "Neural Network", "Convolutional Neural Network", "Deep Neural Network",
    "data scientist", "Data Scientist", "Natural Language Processing",
    "Computer Vision", "Random Forest", "Gradient Boosting"]

proper_nouns = ["客群", "服務"]

def tune_tokenizer(tokenizer):
    for word in set(frequent_proper_nouns):
        tokenizer.add_word(word, freq=None, tag='nr')
        tokenizer.suggest_freq(word, tune=True)

    for word in set(frequent_eng_proper_nouns):
        tokenizer.add_word(word, freq=None, tag='eng')
        tokenizer.suggest_freq(word, tune=True)

    for word in set(proper_nouns):
        tokenizer.add_word(word, freq=None, tag='nr')
    return tokenizer

class yoctol_jieba(object):

    def __init__(self):
        file_path = os.path.abspath(__file__)
        file_dir = os.path.dirname(file_path)
        jieba.setLogLevel(0)
        jieba.set_dictionary(os.path.join(file_dir, 'dict.txt.big.txt'))
        tune_tokenizer(jieba)

    def cut(self, sentence):
        splitted_tokens = jieba.lcut(sentence)
        while '_' in splitted_tokens:
            splitted_tokens.remove('_')
        return splitted_tokens
