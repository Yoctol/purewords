# purewords

Purewords is a package used to clean raw texts for all languages. 

## Install

   `python setup.py install`

## Test

   `python setup.py test`

## Usage

  ### Module usage:

  ```
  import purewords
  
  # raw sentence
  sentence = "ha hi!!hello I\'m at http:www.google.com.tw\n\n" 
             + "you know yahoo? my_computer is great. My phone number"
             + "is 02-3366-5678. <br>的啦<br> my password: 123-abc$99&^%Y)\'_\'(Y "
  
  # clean sentence and use white space to split word tokens
  # result: string
  # 'ha hi hello i am at you know yahoo my computer is great my phone number is 的 my password 123 abc 99 y y'
  purewords.clean_sentence(sentence)
  
  
  # clean document and split document into several cleaned sentences
  # result: list of cleaned string
  # ['ha hi', 'hello i am at', 'you know yahoo', 'my computer is great', 
  #  'my phone number is', '的 my password 123 abc 99 y y']
  purewords.clean_document(sentence)
  
  ```

  ### Command line usage:
  
    Preprocess text files into single cleaned document with multithreads.
  
  ```
  usage: python -m purewords input_file_path

  Purewords command line interface
  Clean texts from files.

  positional arguments:
    input_path            data file path

  optional arguments:
    -h, --help            show this help message and exit
    -d, --dir             set it up to process all txt files in the directory
    -j [job_number], --job_number [job_number]
                        the thread number used in preprocessing
    -max [max_len], --max_len [max_len]
                        the maximun length of a sentence
    -min [min_len], --min_len [min_len]
                        the minimun length of a sentence
    -bs [batch_size], --batch_size [batch_size]
                        the average number of processed sentence per thread
    -v [verbose], --verbose [verbose]
                        the verbose level in multiprocessing
    -o [output_file_path], --output [output_file_path]
                        the cleaned output file path
  ```
  #### Clean text files in directory
  
  For example, you can use following command to clean all the txt files in your directory.
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
