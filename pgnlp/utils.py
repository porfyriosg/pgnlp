import os, re, csv, datefinder, emoji, string
import pandas as pd
from tqdm import tqdm,trange
from nltk.corpus import stopwords

URLREGEX = re.compile(r"(((https?\:\/\/)|(www.))+((\w+\.)*((com)|(gr)|(int)|(ru)|(edu)|(gov)|(net)|(org))))\S*[\r\n\s\ ]*", re.IGNORECASE)
URLREGEX2 = re.compile(r"(((https?\:\/\/)|(www.))+((\w+\.)*))\S*[\r\n\s\ ]*", re.IGNORECASE)
URLREGEX3 = re.compile(r"bit.ly+([^\s]+)", re.IGNORECASE)
USERMENTIONREGEX = re.compile(r'[@+]\s{0,1}\w+(\.\w+)*\s*', re.MULTILINE)
HASHTAGREGEX = re.compile(r'[#+]\s{0,1}\w+(\.\w+)*\s*', re.MULTILINE)
STOPWORDS = set(stopwords.words('english'))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def load_dataset(in_file, edit_columns=[], keep=True):
  """Function to load dataset CSV files.

  Args:
      in_file (str): Full file path. Defaults to None.
      edit_columns (list, optional): Pass columns to keep or drop. Defaults to [].
      keep (bool, optional): If False will drop edit_columns. Defaults to False.

  Raises:
      AssertionError: Path doesnt exist.
      AssertionError: Wrong file

  Returns:
      pandas.DataFrame: Loaded DataFrame
  """
  
  if isinstance(in_file, str) and in_file.endswith('.csv'):
    if os.path.exists(in_file):
      data = pd.read_csv(in_file, low_memory=False)
    
    else:
      raise AssertionError ('File "{}" doesnt exist.'.format(in_file))
  
  else:
    raise AssertionError ('No CSV file passed.')
  
  if edit_columns:
    assert (isinstance(edit_columns, list)), '"edit_columns" should be list.'
    
    if keep:
      edit_columns = [c for c in data.columns.tolist() if c not in edit_columns[:]]
      
    data.drop(columns=edit_columns, inplace=True)
  
  return data

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~