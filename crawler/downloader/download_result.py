# -*- coding: utf-8 -*-

class DownloadResult:
  def __init__(self, index, url, extracted_content):
    self.index = index
    self.url = url
    self.extracted_content = extracted_content