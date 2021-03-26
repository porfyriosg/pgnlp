from string import ascii_lowercase
from .utils import *

_TEMPLATE_ = [
    'remove_urls',
    'remove_user_mentions',
    'remove_hashtags',
    'remove_dates',
    'remove_punctuations']

class Cleaner(object):

    def __init__(self):
        pass

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def remove_numbers(self, text=''):
        text = re.sub(r'\dst', '', text)
        text = re.sub(r'\dnd', '', text)
        text = re.sub(r'\drd', '', text)
        text = re.sub(r'\dth', '', text)
        text = re.sub(r'\d', '', text)
        return text
        
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def remove_punctuations(self, text=''):
        punctuations = set(list(string.punctuation))
        chars = set(list(text))
        rmPuncts = list(punctuations.intersection(chars))
        for punc in rmPuncts:
            text = text.replace(punc, '')
        return text

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def remove_urls(self, text=''):
        text = URLREGEX.sub("", text)
        text = URLREGEX2.sub("", text)
        return text

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def remove_user_mentions(self, text=''):
        text = USERMENTIONREGEX.sub("",  text)
        return text

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def remove_hashtags(self, text=''):
        text = HASHTAGREGEX.sub("",  text)
        return text

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    def remove_dates(self, text=''):
        matches = datefinder.find_dates(text, source=True)
        try:
            for match_datetime_obj, match_value in matches:
                text = text.replace(match_value, '').strip()
        except:
            pass

        return text
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    def remove_emoji(self, text=''):
        emoji_pattern = re.compile("["
                            u"\U0001F600-\U0001F64F"  # emoticons
                            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                            u"\U0001F680-\U0001F6FF"  # transport & map symbols
                            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            u"\U00002702-\U000027B0"
                            u"\U000024C2-\U0001F251"
                            "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', text)
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def remove_stopwords(self, text=''):
        words = [word for word in text.split() if word not in STOPWORDS]
        text = ' '.join(words)
        return text

#==============================================================================

class Placeholder(object):

    def __init__(self):
        pass

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def replace_numbers(self, text=''):
        text = re.sub(r'\dst', '<[ORDINAL]>', text)
        text = re.sub(r'\dnd', '<[ORDINAL]>', text)
        text = re.sub(r'\drd', '<[ORDINAL]>', text)
        text = re.sub(r'\dth', '<[ORDINAL]>', text)
        text = re.sub(r'\d', '<[NUMBER]>', text)
        return text 

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def replace_urls(self, text=''):
        text = URLREGEX.sub("<[URL]>",  text)
        text = URLREGEX2.sub("<[URL]>",  text)
        return text

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def replace_user_mentions(self, text=''):
        text = USERMENTIONREGEX.sub("<[MENTION]>",  text)
        return text

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def replace_hashtags(self, text=''):
        text = USERMENTIONREGEX.sub("<[HASHTAG]>",  text)
        return text

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    def replace_dates(self, text=''):
        matches = datefinder.find_dates(text, source=True)
        
        try:
            for match_datetime_obj, match_value in matches:
                text = text.replace(match_value, '<[DATE]>').strip()
        except:
            pass
        
        return text

#==============================================================================

class Normalizer(object):

    def __init__(self):
        self.emoticons = {
        '<3': 'love',
        ':-)': 'happy',
        ':)': 'happy',
        ':-(': 'sad',
        ':(': 'sad',
        ';D': 'wink',
        ';-D': 'wink'
        }
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def replace_emoticons(self, text=''):
        text = emoji.demojize(text)
        
        for emoticon, word in self.emoticons:
            text = text.replace(emoticon, word)
        return text

#==============================================================================

class Pipeline(Cleaner, Placeholder, Normalizer):

    def __init__(self, template:list=[]):
        super(Pipeline, self).__init__()
        template = template if template else _TEMPLATE_
        self.load_pipeline(template=template)
    
    def load_pipeline(self, template:list=[]):
        self.pipeline = []
        append = self.pipeline.append
        if isinstance(template, list):
            for func in template:
                append(
                    getattr(self, func)
                )
            
    def execute(self, texts:list=[], lowercase:bool=False, text_column:str=None, sheet_name:str=0) -> list:
        pre_texts = []
        append = pre_texts.append
        for text in textiter(data=texts, lowercase=lowercase, 
                            text_column=text_column, sheet_name=sheet_name):
            for process in self.pipeline:
                text = process(text)
            append(
                text
            )
        return pre_texts
