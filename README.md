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
pipe = preprocessing.Pipeline()
results = pipe.execute(texts=texts)
```
-----------------------------------------------------
## TO-DOs:
###
1. **Add word similarity**
2. **Better examples on README**
3. **Add package description on README** 
4. **Check and update multiprocessing**
