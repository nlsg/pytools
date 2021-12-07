#!/usr/bin/python
from os import system as s; p = print
import nls_util as nut
import os
import numpy as np
import ctypes


with (c := nut.Curses()):
  choice = 0
  in_ = None
  choices = ["a","bb","ccc","ddd","eee"]
  max_y,max_x = c.stdscr.getmaxyx()
  status_bar = c.stdscr.subwin(3,max_x,max_y-3,0)

  def update_bar(status_bar_str):
    status_bar.clear()
    status_bar.addstr(1, 1, status_bar_str, c.curses.A_BOLD)
    status_bar.box()
    status_bar.refresh()

  keys = {
    "k":["move up"   ]
    ,"j":["move down"]
    ,"?":["show help"]
    ,"h":["show help"]
    ,"q":["quit"]
    }

  def keybindings_help():
    help = c.stdscr.subwin(max_y//2, max_x//2,max_y//4,max_x//4)
    y,x =help.getyx()
    help.box()
    help.addstr(0,1,"<keybindings>")
    i =1
    for key in keys:
      help.addstr(i,1,str(key) + " - " + str(keys[key][0]))
      i += 1

    in_ = help.getch()
    help.clear()  

  while True:
    # str = "print('tr') if False else choices"
    # eval(str)
    if in_ == 'k' and choice > 0                : choice -= 1
    elif in_ == 'j' and choice < len(choices)-1 : choice += 1
    elif in_ == 'q'                             : break
    elif in_ == 'm'                             : keybindings_help()
    elif in_ == '?'                             : keybindings_help()
    elif in_ == 'h'                             : keybindings_help()
    for i in range(len(choices)):
      c.stdscr.addstr(i,0,choices[i], c.curses.A_REVERSE if choice == i else c.curses.A_NORMAL)

    update_bar(f"{in_=} | {max_x=}, {max_y=} | {choice=}, {choices[choice]=}")
    in_ = c.stdscr.getkey()


