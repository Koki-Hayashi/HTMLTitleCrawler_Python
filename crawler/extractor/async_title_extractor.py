# -*- coding: utf-8 -*-
import threading
import downloader
import os

class AsyncTitleExtractor(threading.Thread):

  def __init__(self, url_list):
    threading.Thread.__init__(self)
    self.url_title_list = []
    self.url_list = url_list

  # append pairs of url and contents of title tag of html files to url_title_list
  # when it is not a html file or in case a html has no title tag, append a pair of url and empty string
  def run(self):
    for url in self.url_list:
      path, ext = os.path.splitext(url)
      if ext and (ext != u".html" or ext != u".htm"):
        self.url_title_list.append((url, u""))
        continue

      html = downloader.download(url)

      title_tag_start = u"<title>"
      title_tag_end = u"</title>"

      title = ""
      for line in html:
        line = line.decode(u"utf-8")
        if title_tag_start and title_tag_end in line:
          title = line.replace(title_tag_start, "").replace(title_tag_end, "").strip()


      self.url_title_list.append((url, title))

  def pop_url_title(self):
    try:
      return self.url_title_list.pop(0)
    except IndexError:
      return []




