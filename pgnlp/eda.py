from utils import *

class TextEDA(object):
  
  def __init__(self, in_file, text_column=None, target_column=None):
    self.text_column = text_column
    self.target_column = target_column
    self.data = load_dataset(in_file=in_file, edit_columns=[self.text_column, self.target_column], keep=True)
    
  def print_dataset_shape(self):
    print (self.data.shape)
    print (self.data.groupby([self.target_column]).agg({self.text_column: 'count'}))