from utils import *

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
  
  def lowercase_text(self, text=''):
    return text.lower()
  
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
  def replace_emoticons(self, text=''):
    text = emoji.demojize(text)
    
    for emoticon, word in self.emoticons:
      text = text.replace(emoticon, word)
    return text