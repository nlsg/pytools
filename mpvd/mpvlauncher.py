#!/usr/bin/env python
'''
is a tool for firefox to open a link - pionted by the mouse - in mpv.
this script is ment to be triggered via a shortcut.
sxhkd is a great tool for that.
'''

import pyautogui as pag
from os import system, popen

CMD_STR = "mpv {0} --input-ipc-server=/tmp/mpv.socket"

def get_link():
  pag.click(button="right")
  pag.write("l")
  return popen("xclip -o").read()

def fire_mpv(link):
  link = "ytdl://" + link.split("://")[1]
  print(link)
  system(CMD_STR.format(link))

def main():
  fire_mpv(get_link())
  
if name == "__main__":
  main()

