#!/usr/bin/python3
import sys, os
def get_url(args):
  url = "+".join(args)
  url = url.replace(" ","+")
  if "://" not in url:
    url = "https://duckduckgo.com/?q=" + url 
  else:
    url = args[0]
  return url

if __name__ == "__main__":
  url = get_url(sys.argv[1:])
  print(f"links {url}")
