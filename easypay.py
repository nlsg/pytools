#!/usr/bin/python
import cv2
from os import system as s; p = print
import nls_util as nut
import os
import numpy as np
import easyocr
import matplotlib.pyplot as plt
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

s("clear")
from PIL import Image
import nls_util as nut
import logging 
logging.basicConfig(**nut.log_config)
log = logging.warning
import time as t

results = []
times = []

def ocr_func(img_path):
  log(f"entered {img_path=}")
  t1 = t.time()
  res =  results.append(easyocr.Reader(['en']).readtext(img_path))
  times.append(t.time()-t1)
  log(f"executed in {t.time()-t1:.2f}s")
  return res

nut.listing((imgs := nut.ls("easypay_assets/*test0*").read().split("\n")))
imgs.pop()
nut.listing(imgs)

from multiprocessing import Pool
nut.listing(nut.grep("*", nut.ls("easypay_assets/*").read().split("\n")))
def f(x):
  return x*x

s("clear")
result = it = res = None
with Pool(processes=4) as pool:         # start 4 worker processes
  result = pool.apply_async(f, (10,)) # evaluate "f(10)" asynchronously in a single process
  print(result.get())        # prints "100" unless your computer is *very* slow
  res = pool.map(f, range(10))       # prints "[0, 1, 4,..., 81]"
  it = pool.imap(f, range(10))
  print(next(it))                     # prints "0"
  print(next(it))                     # prints "1"
  print(it.next(timeout=1))           # prints "4" unless your computer is *very* slow

# t_start = t.time()
# for img_path in nut.ls("easypay_assets/test/*bill*").read().split("\n"):
#   t1 = t.time()
#   thread.start_new_thread(ocr_func, (img_path,))
#   log(f"thread started in {t.time()-t1:.2f}s")

#log(f"all thread joined in {t.time()-t_start:.2f}s")
# for img_path in nut.ls("easypay_assets/test/*bill*").read().split("\n"):
#   results.append(easyocr.Reader(['en']).readtext(img_path))


