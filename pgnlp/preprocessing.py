import pandas as pd
from multiprocessing import Pool

from .norm import Normalizer
from .clean import Cleaner
from .repl import Placeholder

class Pipeline(Normalizer, Cleaner, Placeholder):

  def __init__(self, *args, **kwargs):
    super(Pipeline, self).__init__()
    self.template = kwargs.get('template', {
      'lowercase_text': True,
      'replace_emoticons': False,
      'replace_numbers': False,
      'replace_urls': False,
      'replace_user_mentions': False,
      'replace_hashtags': False,
      'replace_dates': False,
      'remove_numbers': False,
      'remove_punctuations': True,
      'remove_urls': True,
      'remove_user_mentions': True,
      'remove_hashtags': False,
      'remove_dates': True,
      'remove_emoji': False,
      'remove_stopwords': True
    })

  def check_texts(self, texts=None):
    texts = [txt if isinstance(txt, str) else '' for txt in texts]
    self.texts_count = len(texts)
    ids = range(self.texts_count)
    return zip(ids, texts)

  def process(self, txt=()):
    tid, text = txt
    for func in filter(lambda v: self.template[v], self.template):
      text = getattr(self, func)(text)
    return (tid, text)

  def serial(self, txts=None):
    results = []
    for txt in txts:
      results.append(self.process(txt))

    return [text for tid, text in sorted(results)]

  def multi(self, txts=None):
    pool = Pool(processes=4)

    results = pool.imap(self.process, txts)

    return [text for tid, text in sorted(results)]

  def execute(self, texts=None, parallel=True):
    assert (isinstance(texts, list)), 'No texts found.'

    txts = self.check_texts(texts=texts)

    if parallel is True:
      return self.multi(txts)
    
    else:
      return self.serial(txts)