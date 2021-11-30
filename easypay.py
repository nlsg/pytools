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
  c.stdscr.clear()
  c.stdscr.addstr(0, 0, '10 divided by')
  c.stdscr.getkey()


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
# nut.ls("*ass*")
# def test(folder):
#   info = get_img_text("easypay_assets/" + nut.ls(folder))
#   info.sort()
