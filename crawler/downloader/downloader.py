# -*- coding: utf-8 -*-
import urllib2

def download(url):
  try:
    return urllib2.urlopen(url)
  except urllib2.HTTPError as e: # assume 404 error
    return ""

