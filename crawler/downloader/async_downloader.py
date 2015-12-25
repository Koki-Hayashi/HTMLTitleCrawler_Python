# -*- coding: utf-8 -*-
import urllib2
import threading
import os
from download_result import DownloadResult

class AsyncDownloader(threading.Thread):

  def __init__(self, index, url, result_list, extract_logic = None):
    threading.Thread.__init__(self)
    self.index = index
    self.url = url
    self.result_list = result_list
    self.lock = threading.Lock();
    self.extract_logic = extract_logic

  # This method does:
  # 1. download html contenct from assigned url
  # 2. extract contents according to passed method
  # 3. create and append DownloadResult into result_list
  # extracted content will be None if url is not pointing html or downloaded html file doesn't have title tag
  def run(self):
    path, ext = os.path.splitext(self.url)
    if ext and (ext != u".html" or ext != u".htm"):
      result = DownloadResult(self.index, self.url, None)
      with self.lock:
        self.result_list.append(result)
      return

    try:
      html = urllib2.urlopen(self.url)
      if self.extract_logic is None:
        result = DownloadResult(self.index, self.url, html)
        with self.lock:
          self.result_list.append(result)
        return

      extracted = self.extract_logic(html)
      result = DownloadResult(self.index, self.url, extracted)
      with self.lock:
        self.result_list.append(result)

    except urllib2.HTTPError as e: # if error
      result = DownloadResult(self.index, self.url, None)
      with self.lock:
        self.result_list.append(result)

