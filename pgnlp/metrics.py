from .utils import *

def count_words(text:str=''):
    return len(re.findall(r'\w+', text))
