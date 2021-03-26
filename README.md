# Python 3 package for data preprocessing
-----------------------------------------------------
# Installation
###
```bash
git clone https://github.com/porfyriosg/pgnlp.git
cd pgnlp
pip install -r requirements.txt
pip install -U .
```
-----------------------------------------------------
# HOWTO
###
## Import main function
```python
from pgnlp.preprocessing import Pipeline
# You could use list
texts = ['<TEXT1>', '<TEXT2>']
# Or file (csv, xls, xlsx)
texts = '/path/to/file.csv'
# Or even single text
texts = '<TEXT>'

# NOTE! In any case Pipeline will return list of texts
```
-----------------------------------------------------
###
## For simple use
```python
pipe = Pipeline()
pre_texts = pipe.execute(texts=texts, lowercase=True)
```
-----------------------------------------------------
###
## For manual use
```python
# Add your processes in list
template = [
    'remove_urls',
    'remove_user_mentions',
    'remove_hashtags',
    'remove_dates',
    'remove_punctuations']

pipe = Pipeline(template=template)
pre_texts = pipe.execute(texts=texts, lowercase=True)
```
###
## For CLI use
```bash
# Will simply print list of texts with results (Not recommended for big files)
nlpcli -t '<TEXT>' --remove_numbers \
                    --remove_punctuations \
                    --remove_urls \
                    --remove_stopwords
```
-----------------------------------------------------
## TO-DOs:
###
1. **Add word similarity**
2. **Add metrics**
