import cv2, pytesseract
import nls_util as nut
from sys import path; path.insert(1, "/home/nls/py/cnav");from cnav import Nav

def read_imgs(img_paths):
  img_texts = []
  for path in img_paths: 
    try:
      img = cv2.imread(path)
      img_texts.append(pytesseract.image_to_string(img, config="outputbase digits"))
      print(f"read {path}")
    except TypeError:
      print("got a type error")
  return img_texts

def show_imgs(img_paths):
  from os import system
  for path in img_paths:
    system(f"sxiv {path}")
    input()

def check_imgs(img_texts):
  pass

paths = nut.ls("easypay_assets/test/*")
show_imgs(paths)
# txts = read_imgs(paths)
# Nav().navigate(txts)
