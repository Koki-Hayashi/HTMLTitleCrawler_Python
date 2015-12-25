# -*- coding: utf-8 -*-
import threading
import time
import re
from async_downloader import AsyncDownloader
from operator import itemgetter

class AsyncTitleExtractor:

  def __init__(self, url_list):
    self.url_title_list = []
    self.url_list = url_list
    self.lock = threading.Lock()

  def extract_title(self, html):
    if html is None:
      return None

    pattern = r"<title>(.*)</title>"

    title = u""
    for line in html:
      matchOB = re.search(pattern , line)

      if matchOB:
        line = line.decode(u"utf-8")
        title = line.replace(u"<title>", "").replace(u"</title>", u"").strip()
        break

    return title

  def process(self):
    download_result_list =  []
    index = 0

    # download contents one by one from url and extract title tagged words asynchronously
    # result will be wrapped in DownloadResult object and appended into download_result_list
    for url in self.url_list:
      downloader = AsyncDownloader(index, url, download_result_list, self.extract_title)
      downloader.start()
      index += 1

    while len(download_result_list) != len(self.url_list): # wait until async download finishes
      time.sleep(1)
      continue

    download_result_list.sort() # sort by DonloadResult.index

    url_title_list = []
    for result in download_result_list:
      url_title_list.append([result.url, result.extracted_content])

    return url_title_list;









