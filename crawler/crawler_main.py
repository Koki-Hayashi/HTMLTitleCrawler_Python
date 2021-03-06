# -*- coding: utf-8 -*-
import sys
sys.path.append(u"reader")
sys.path.append(u"writer")
sys.path.append(u"downloader")
sys.path.append(u"parser")
sys.path.append(u"model")
sys.path.append(u"extractor")
sys.path.append(u"validator")

import time
import os
import threading

from word_list_reader import WordListReader
from url_list_reader import UrlListReader
from async_title_extractor import AsyncTitleExtractor
from tsv_writer import TsvWriter
from result import Result
from validator import Validator

def main(word_list_file, url_list_file, output_file):

  print u"validation check"
  validator = Validator()
  if not validator.validate(word_list_file, url_list_file, output_file):
    sys.stderr.write(u"validation error")
    exit(1)

  word_list = gen_word_list(word_list_file)

  # read url list and start crawling asynchronously and extract title tag content
  url_list = gen_url_list(url_list_file)
  print u"crawling start"
  extractor = AsyncTitleExtractor(url_list);
  url_title_list = extractor.process() # AsyncTitleExtractor.process() download files in listed in url_list
                                # and store pairs of contents of title tags and urls

  result_list = []
  print u"counting..."
  for url_title in url_title_list:

    url = url_title[0]
    title = url_title[1]

    # store appearance count of each word
    word_list_len = len(word_list)
    count_list = [0] * word_list_len
    if title is None: # when title is not extracted then set 0s
      result = Result(url, count_list)
      result_list.append(result)
      continue

    for i in range(0, word_list_len):
      count_list[i] = title.count(word_list[i])

    result = Result(url, count_list)
    result_list.append(result)

  # output result
  print u"writing output..."
  writer = TsvWriter(output_file)
  writer.write(result_list)

  print u"done"

def gen_url_list(url_list_file):
  url_list_reader = UrlListReader(url_list_file)
  return url_list_reader.read();

def gen_word_list(word_list_file):
  word_list_reader = WordListReader(word_list_file)
  return word_list_reader.read()

def print_usage():
  line_break = os.linesep
  error_message = []
  error_message.append(u"This crawler requires 3 arguments. ")
  error_message.append(u"1:file path/name of word list. ")
  error_message.append(u"2:file path/name of target url list. ")
  error_message.append(u"3:file path/name of output file. ")
  sys.stderr.write(u"".join(error_message))
  exit(1)

if __name__ == u"__main__":
  param = sys.argv

  # check arguments number and
  if len(param) != 4:
    print_usage();

  word_list_file = param[1]
  url_list_file = param[2]
  output_file = param[3]

  print u"start processing..."
  main(word_list_file, url_list_file, output_file)






