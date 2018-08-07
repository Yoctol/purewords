# purewords

Purewords is a package used to clean raw texts for all languages. 

## Install

   `pip install purewords`


## Usage

  ### Module usage:

  ```python
  import purewords
  
  # raw sentence
  inputs = "ha hi!!hello I\'m at http:www.google.com.tw\n\n" 
           + "you know yahoo? my_computer is great. My phone number"
           + "is 02-3366-5678. <br>的啦<br> my password: 123-abc$99&^%Y)\'_\'(Y "
  ```
  #### Treat inputs as a sentence and clean it. 
  
  Word tokens are splitted with whitespace
  ```python
  # result: string
  purewords.clean_sentence(inputs)
  'ha hi hello i am at _url_ you know yahoo my computer is great my phone number is _phone_ 的 my password _num_ abc _num_ y y'
  ```
  
  #### Treat inputs as a document and clean it.
  
  Split document with some confident splitting token such as '.' or '?'.
  ```python
  # result: list of cleaned string
  purewords.clean_document(inputs)
  ['ha hi', 'hello i am at _url_', 'you know yahoo', 'my computer is great', 'my phone number is _phone_', '的 my password _num_ abc _num_ y y']
  ```

  ### Customed your purewords
  
  You can use different setting in purewords.
  
  ```python
  import purewords
  from purewords.tokenizer import YoctolTokenizer
  from purewords.filter_collection import document_filters
  from purewords.filter_collection import token_filters
  
  tokenizer = YoctolTokenizer()
  pw = purewords.PureWords(
      tokenizer=tokenizer, # select your tokenizer
      document_filters=document_filters, # select your document filters
      token_filters=token_filters, # select your token filters
      max_len=200, # cut long sentence whose length exceed max_len
      min_len=1 # ignore short sentence 
  )
  
  inputs = 'This is a sentence.'
  
  pw.clean_sentence(inputs)
  pw.clean_document(inputs)
  ```

  #### Tokenizer

  ##### Select your tokenizer in purewords

  You can select `WhitespaceTokenizer` tokenizer if you prefer tokenize 
  sentences with whitespace or `JiebaTokenizer` for default jieba setting.
  
  Otherwise, we use yoctol jeiba tokenizer as our default setting.
  
  ```python
  from purewords.tokenizer import WhitespaceTokenizer

  tokenizer = WhitespaceTokenizer()
  pw = purewords.PureWords(
      tokenizer=tokenizer
  )
  ```

  ##### Add new words in JiebaTokenizer

  You can add new word in JiebaTokenizer to customize your tokenizer.

  ```python
  from purewords.tokenizer import JiebaTokenizer

  tokenizer = JiebaTokenizer()
  tokenizer.add_word(new_word, freq, tag) # The setting is same with jieba.add_word
  tokenizer.add_words(new_word_list, freq, tag)

  pw = purewords.PureWords(
      tokenizer=tokenizer
  )
  ```
  
  #### Filter collection
  
  You can customize your preprocesing ways in purewords.
  
  * document_filters: preprocess the raw sentence before sentence splitting
  * token_filters: preprocess tokens after tokenization of each sentence
  
  ##### Organize your filters
  
  You can create your customized filters by adding your filters in our filter collection class.
  
  Filter means a callable object which receives a raw sentence and returns the processed one.
  
  The preprocessing order is consistent with the adding order of filters.
  
  ```python
  from purewords.filter_collection import BaseFilterCollection
  
  custom_filters = BaseFilterCollection()
  custom_filters.add(filter_1)
  custom_filters.add(filter_2)
  ...
  custom_filters.add(filter_n)
  
  pw = purewords.PureWords(
      tokenizer=tokenizer,
      document_filters=custom_filters,
  )
  ```
  
  #### Stopwords
  
  You can add stopwords in `purewords/config/stopwords.txt`.


  ### Command line usage:
  
  Preprocess text files into a single cleaned document from command line.
  
  Usage:
  
  #### Clean single txt files
  ```
  python -m purewords input_file_path
  ```
 
  #### Clean text files in a directory
  
  Or, you can use following command to clean all the txt files in your directory.
  ```
  python -m purewords -d your_raw_text_dir
  ```
  
  #### Ignore short sentences 
  
  If you prefer long sentences and want to ignore short sentences less than 5 words, you can try this.
  ```
  python -m purewords -min 5 your_text_file
  ```
  
  #### Cut long sentences
  
  Or you prefer short sentences less than 30 words and want to cut long sentences into short sentences.
  
  You can set up the maximun sentence length like this.
  ```
  python -m purewords -max 30 your_text_file
  ```
  
  #### Use multi-thread to speed up
  
  You can also use multi-trhead to speed up the cleaning process. 
  
  In the follwoing example, you clean all the text files with 4 threads
  ```
  python -m purewords -j 4 -d your_raw_text_dir
  ```
