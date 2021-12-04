#!/usr/bin/python
import cv2
from os import system as s; p = print
import nls_util as nut
import os
import numpy as np
import easyocr
import matplotlib.pyplot as plt
import ctypes

nut.ls("./")

x,y = 0,0 
with (c := nut.Curses()):
  c.stdscr.clear()
  choice = 2
  choices = ["aaa","bbb","ccc","ddd","eee"]
  y,x = c.stdscr.getmaxyx()
  c.stdscr.addstr(y-1, 0, f"{x=},{y=}", c.curses.A_BOLD)
  while True:
    in_ = c.stdscr.getkey()
    if in_ == 'k' and choice > 0: choice -= 1
    elif in_ == 'j' and choice < len(choices)-1: choice += 1
    elif in_ =='q': break

    for i in range(len(choices)):
      c.stdscr.addstr(i,0,choices[i], c.curses.A_REVERSE if choice == i else c.curses.A_NORMAL)

# help(nut)
# def get_imgs(folder): 
#   return os.popen(f"ls {folder}").read().split("\n")


# def get_img_text(img):
#   reader = easyocr.Reader(['en'])
#   return reader.readtext(img)

# s("sxiv easypay_assets/easy_rotated.jpg")

# info.__dir__()
# nut.listing(info)
# for i in info: print(i[1])

# s("clear")
# from PIL import Image
# from pytesseract import pytesseract

# with nut.Timer("tesseract"):
#   print(pytesseract.image_to_string(Image.open("easypay_assets/easy_rotated.jpg")))
# import nls_util as nut
# nut.notify("dd","ww")
# nut.ls("*ass*").read().split("\n")a
# def test(folder):
#   info = get_img_text("easypay_assets/" + nut.ls(folder).read().split("\n")a)
#   info.sort()
