# -*- coding: utf-8 -*-
import os
from result import Result

class TsvWriter():
  def __init__(self, output_file):
    self.output_file = output_file

  def write(self, result_list):
    with open(self.output_file, mode = "w") as out:

      for result in result_list:
        url = result.url
        line = []
        line.append(url)
        count_list = result.count_list
        for count in count_list:
          line.append("\t%d" % count)

        line.append(os.linesep)
        out.write("".join(line))