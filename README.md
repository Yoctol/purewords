# purewords
Purewords is a package used to clean raw texts for all languages. 

* Usage:

  ```
  >>> import purewords
  >>> sentence = "ha ha hi hi!!hello I'm at http:www.google.com.tw\n\n" 
                 + "you know yahoo? my_computer is great. My phone number"
                 + "is 02-3366-5678. <br>的啦<br> my password: 123@abc$99&^%Y)'_'(Y "
  
  >>> purewords.clean_sentence(sentence)
  'ha ha hi hi hello i m at you know yahoo my computer is great my phone number is 的 my password 123 abc 99 y y'
  
  >>> purewords.clean_document(sentence)
  ['ha ha hi hi', 'hello i m at', 'you know yahoo', 'my computer is great', 'my phone number is', '的 my password 123 abc 99 y y']
  ```

You can set up your configuration in `purewords/configs/default.yml`
