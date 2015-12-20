# -*- coding: utf-8 -*-
import codecs

class WordListReader:

  def __init__(self, word_list_file):
    self.word_list_file = word_list_file

  def read(self):
    word_list = []

    if not self.word_list_file or self.word_list_file is None:
      return word_list

    with codecs.open(self.word_list_file, "r", "utf-8") as word_file:
      for line in word_file:
        word_list.append(line.rstrip())

    return word_list