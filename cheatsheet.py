#!/usr/bin/python3
from os  import system
from sys import exit, argv
from sys import path; path.insert(1, "/home/nls/py/lib");
from nls_func import tee_print 

if __name__ == "__main__":
  usage = f"usage: {argv[0]} language your question ..."
  try:
    lang = argv[1]
    query = []
    for arg in argv[2:]:
      if arg[0] == "/":
        lang = arg
        query = []
      else:
        query.append(arg)

    if len(query) == 0:
      raise IndexError
    url = ("cht.sh/" + lang + "/" + "+".join(query)).replace("//", "/")
  except IndexError:
    print(usage)
    exit(1)
  cmd = f"curl {url}"
  system(tee_print(cmd))


