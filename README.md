# purewords

Purewords is a package used to clean raw texts for all languages. 

## Install

   `python setup.py install`

## Test

   `python setup.py test`

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
  'ha hi hello i am at you know yahoo my computer is great my phone number is 的 my password 123 abc 99 y y'
  ```
  
  #### Treat inputs as a document and clean it.
  
  Split document with some confident splitting token such as '.' or '?'.
  ```python
  # result: list of cleaned string
  purewords.clean_document(inputs)
  ['ha hi', 'hello i am at', 'you know yahoo', 'my computer is great', 'my phone number is', '的 my password 123 abc 99 y y']
  ```

  ### Customed your purewords
  
  You can use different setting in purewords.
  
  ```python
  import purewords
  
  pw = purewords.PureWords(
      tokenizer='yoctol_jieba', # select your tokenizer
      remove_url=True, 
      remove_time=True, # remove time such as 20170101
      remove_phone_number=True, 
      replace_title=True, # replace "Mr." with "Mr" for example
      remove_blank=True, # remove blank _____ 
      replace_abbreviation=True, # replace "I'd" with "I would" for example
      remove_angle_brackets=True,
      stopwords_path='configs/stopwords.txt', # setup your customed stopwords 
      max_len=200, # cut long sentence whose length exceed max_len
      min_len=1 # ignore short sentence 
  )
  
  inputs = 'This is a sentence.'
  
  pw.clean_sentence(inputs)
  pw.clean_document(inputs)
  ```
  You can select 'whitespace_tokenizer' tokenizer if you prefer tokenize sentences with whitespace.
  
  ```python
  pw = purewords.PureWords(
      tokenizer='whitespace_tokenizer'
  )
  ```

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
