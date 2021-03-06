#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):
  filenames=os.listdir(dir)
  special_files=[]
  for filename in filenames:
    match=re.search(r'.*\_\_\w+\_\_.*',filename)
    if match:
      #print match.group()    
      special_files.append(match.group())
  special_file_paths=[]
  for file_name in special_files:
    path=os.path.join(dir,file_name)
    #print os.path.abspath(path)
    special_file_paths.append(os.path.abspath(path))
  return special_file_paths

def copy_to(paths,dir):
  if not os.path.exists(dir):
    os.mkdir(dir)
  for path in paths:
    file_name=os.path.basename(path)
    shutil.copy(path,os.path.join(dir,file_name))

def zip_to(paths,zippath):
  cmd = 'zip -j ' + zippath + ' ' + ' '.join(paths)
  print "Command I'm going to do:" + cmd
  (status, output) = commands.getstatusoutput(cmd)
  # If command had a problem (status is non-zero),
  # print its output to stderr and exit.
  if status:
    sys.stderr.write(output)
    sys.exit(1)



def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]
  
  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)
  
  paths=get_special_paths(args[0])
  if todir:
    copy_to(paths,todir)
  elif tozip:
    zip_to(paths,tozip)  
  else:
    for path in paths:
      print path 
  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
