from utils import *

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
    text = URLREGEX3.sub("", text)
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