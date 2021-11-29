#!/usr/bin/python
import cv2
from os import system as s; p = print
import nls_util as nut
import os
import numpy as np
import easyocr
import matplotlib.pyplot as plt
import ctypes

help(nut)
def get_imgs(folder): 
  return os.popen(f"ls {folder}").read().split("\n")

def get_img_text(img):
  reader = easyocr.Reader(['en'])
  return reader.readtext(img)

s("sxiv easypay_assets/easy_rotated.jpg")

info = get_img_text("easypay_assets/easy_rotated.jpg")

from PIL import Image
from pytesseract import pytesseract

with nut.Timer("tesseract"):
  print(pytesseract.image_to_string(Image.open("easypay_assets/easy_rotated.jpg")))
