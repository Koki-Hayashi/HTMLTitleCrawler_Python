# -*- coding: utf-8 -*-
import os
import os.path
import sys

class Validator():

  def __init__(self):
    self.line_break = os.linesep

  def validate(self, word_list_file, url_list_file, output_file):
    errorMessages = []

    # validate one by one of all arguments and return error messages if validate fail
    errorMessages.extend(self.validate_word_list_file(word_list_file))
    errorMessages.extend(self.validate_url_list_file(url_list_file))
    errorMessages.extend(self.validate_output_file(output_file))

    if errorMessages:
      sys.stderr.write(''.join(errorMessages))
      return False

    return True

  # check
  # - file name is not empty/None
  # - existense of file
  # - each line is not empty
  # - each line doesn't contain space
  def validate_word_list_file(self, word_list_file):
    errorMessages = []

    # - file name is not empty/None
    if not word_list_file or word_list_file is None:
      errorMessages.append("%s : file name is empty" % (word_list_file, self.line_break))
      return errorMessages

    # - existense of file
    if not os.path.isfile(word_list_file):
      errorMessages.append("%s : the file is not existing%s" % (word_list_file, self.line_break))
      return errorMessages

    with open(word_list_file, "r") as word_file:
      line_counter = 1;

      for line in word_file:

        # - each line is not empty
        if not line.strip():
          errorMessages.append("%s at line %d : empty string contained%s" % (word_list_file, line_counter, self.line_break))
          continue

        # - each line doesn't contain space
        if " " in line:
          errorMessages.append("%s at line %d : each line should contain only 1 word (space included)%s" % (word_list_file, line_counter, self.line_break))

        line_counter += 1

    return errorMessages

  # check
  # - file name is not empty/None
  # - existense of file
  # - each line is not empty
  # - each line doesn't contain space
  def validate_url_list_file(self, url_list_file):
    errorMessages = []

    # - file name is not empty/None
    if not url_list_file or url_list_file is None:
      errorMessages.append("%s : file name is empty%s" % (url_list_file, self.line_break))
      return errorMessages

    # - existense of file
    if not os.path.isfile(url_list_file):
      errorMessages.append("%s : the file is not existing%s" % (url_list_file, self.line_break))
      return errorMessages

    with open(url_list_file, "r") as url_file:
      line_counter = 1;
      for line in url_file:

        # - each line is not empty
        if not line.strip():
          errorMessages.append("%s at line %d : empty string contained%s" % (url_list_file, line_counter, self.line_break))
          continue

        # - each line doesn't contain space
        if " " in line:
          errorMessages.append("%s at line %d : each line shouldn't contain space%s"  % (url_list_file, line_counter, self.line_break))

        line_counter += 1

    return errorMessages

  # check
  # - file name is not empty/None
  # - existense of output dir
  def validate_output_file(self, output_file):
    errorMessages = []

    # - file name is not empty/None
    if not output_file or output_file is None:
      errorMessages.append("%s : file name is empty%s" % (output_file, self.line_break))
      return errorMessages

    # - existense of output dir
    output_file_dir = os.path.dirname(os.path.abspath(output_file))
    if not os.path.isdir(output_file_dir):
      errorMessages.append("%s : target directory %s is not existing%s" % (output_file, output_file_dir, self.line_break))

    return errorMessages
