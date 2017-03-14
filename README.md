# purewords
Purewords is a package used to clean raw texts for all languages. 

* Usage

  * module usage:

  ```
  >>> import purewords
  >>> sentence = "ha ha hi hi!!hello I\'m at http:www.google.com.tw\n\n" 
                 + "you know yahoo? my_computer is great. My phone number"
                 + "is 02-3366-5678. <br>的啦<br> my password: 123-abc$99&^%Y)\'_\'(Y "
  
  >>> purewords.clean_sentence(sentence)
  'ha ha hi hi hello i am at you know yahoo my computer is great my phone number is 的 my password 123 abc 99 y y'
  
  >>> purewords.clean_document(sentence)
  ['ha ha hi hi', 'hello i am at', 'you know yahoo', 'my computer is great', 'my phone number is', '的 my password 123 abc 99 y y']
  ```

  * command line usage:
  
    preprocess several text files with multithreads.
  
  ```
  usage: python -m purewords input_file_path

  Purewords command line interface
  Clean text from files.

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
