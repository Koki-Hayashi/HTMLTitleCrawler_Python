# -*- coding: utf-8 -*-
import codecs

class UrlListReader:

  def __init__(self, url_list_file):
    self.url_list_file = url_list_file

  def read(self):
    url_list = []

    if not self.url_list_file or self.url_list_file is None:
      return url_list

    with codecs.open(self.url_list_file, u"r", u"utf-8") as url_file:
      for line in url_file:
        url_list.append(line.rstrip())

    return url_list