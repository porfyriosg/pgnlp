from .utils import *

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
    text = URLREGEX3.sub("<[URL]>", text)
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