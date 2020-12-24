# Python 3 package for data preprocessing (WIP)
-----------------------------------------------------
# Requirements

* pandas
* multiprocessing
* datefinder
* tqdm
* nltk
-----------------------------------------------------
# Installation
###
```bash
git clone https://github.com/porfyriosg/pgnlp.git
cd pgnlp
pip install -U .
```
-----------------------------------------------------
# HOWTO
###
```python
from pgnlp import preprocessing
texts = ['<TEXT1>', '<TEXT2>']

template={'lowercase_text': True,
      'remove_stopwords': False,
      'replace_emoticons': False, 
      'remove_emoji': False,
      'replace_urls': False, 
      'remove_urls': True,
      'replace_user_mentions': False, 
      'remove_user_mentions': True,
      'replace_hashtags': False, 
      'remove_hashtags': True,
      'replace_dates': False, 
      'remove_dates': True,
      'replace_numbers': False, 
      'remove_numbers': False,
      'remove_punctuations': True}

pipe = preprocessing.Pipeline(template=template)
results = pipe.execute(texts=texts)
```
-----------------------------------------------------
## TO-DOs:
###
1. **Add word similarity**
2. **Better examples on README**
3. **Add package description on README** 
4. **Check and update multiprocessing**
