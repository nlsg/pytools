#!/usr/bin/env python

HEADER = """
                                       _ _ 
  __ _ _   _  ___ _ __ _   _        __| | |
 / _` | | | |/ _ \ '__| | | |_____ / _` | |
| (_| | |_| |  __/ |  | |_| |_____| (_| | |
 \__, |\__,_|\___|_|   \__, |      \__,_|_|
    |_|                |___/               

$ query-dl.py file | -h
file is a file containing youtube search queries separated by newlines
"""
from sys import argv
from os import popen
from multiprocessing import Pool

def get_youtube_dl_string(query):
  return f"youtube-dl -x --audio-format mp3 \"ytsearch:{query}\""

def download(query):
    link = get_youtube_dl_string(query)
    return tuple(map(lambda x: not "[download]" in x, popen(link).read()))

def downloadIO(query):
  if query[0] == "#":
    return
  print(f"about to download: {query}")
  out = download(query)
  print(f"download complete\n{out}")
  return 

if __name__ == "__main__":
  if argv[1] == "-h":
    print(HEADER)
    exit()
  queries = map(lambda x:x[:-1],open(argv[1],"r").readlines())
  Pool().map(downloadIO,queries)
