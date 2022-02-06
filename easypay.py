#!/usr/bin/python
import cv2
from os import system as s; p = print
import nls_util as nut
import os
import numpy as np
import easyocr
import matplotlib.pyplot as plt
import ctypes
import nls_util as nut
import logging 
logging.basicConfig(**nut.log_config)
log = logging.warning
import time as t
import json

def ocr_func(queue, img_path):
  log(f"entered {img_path=}")
  t1 = t.time()
  res =  easyocr.Reader(['en']).readtext(img_path)
  log(f"executed in {t.time()-t1:.2f}s")
  nut.notify("ocr_func", f"executed in {t.time()-t1:.2f}s")
  try:
    queue.put(res)
  except:
    log("queue.put() exception occurred")
    nut.notify("ocr_func_error", "queue.put() exception occurred")
    return res

def standard_handler(arg_list, func=ocr_func):
  res = []
  tms = []
  for arg in arg_list:
    log(f"started func with {arg}")
    nut.notify("standard_hnd", f"started func with {arg}")
    t1 = t.time()
    res.append(func(None, arg))
    tms.append((tt :=t.time()-t1))
    log(f"{arg} took {tt:.2f}")
    nut.notify("standard_hnd", f"{arg} took {tt:.2f}")
  return res, tms

def perform_ocr(paths_to_img_files):
  '''returns two objects: ocr_results, time'''
  with nut.Timer():
    return standard_handler(paths_to_img_files)

def pack_results(raw_results, times, paths):
  essence = []
  for i in range(len(raw_results)):#for testing object
    print(f"{i=}")
    data = ""
    for i_ in range(len(raw_results[i])):#for identified textobject
      print(f"{i_=}")
      data += raw_results[i][i_][1]
      data += ", "
      log(f"({i}){data=}")
    essence.append({
      "time":times[i]
      ,"data":data
      ,"path":paths[i]
      })
    return essence

cont = nut.ls("easypay_assets/test/*")
nut.listing((imgs := nut.grep("bill", cont)))

essence = []
# res, tms = perform_ocr(imgs)
essence = pack_results(res, tms, imgs)
nut.listing(essence)
nut.listing(res)
nut.listing(tms)
input()
essence = []
for i in range(len(res)):#for testing object
  print(f"{i=}")
  data = ""
  for i_ in range(len(res[i])):#for identified textobject
    print(f"{i_=}")
    data += res[i][i_][1]
    data += ", "
    log(f"({i}){data=}")
  essence.append({
    "time":tms[i]
    ,"data":data
    ,"path":imgs[i]
    })

def void_f():
  with open(f"essence.json", "w") as f:
    json.dump(essence, f)
    
    
    void_f()

essence = pack_results(res, tms, imgs)
len(essence)

import pandas as pd
df = pd.DataFrame(essence)

len(res)
def get_test_data(file_path="essence.json"):
  data = []
  with open(file_path) as f:
    data = json.load(f)
  return data

# def test_ocr(packed_data):
#   packed_data["data"]

# python load json file 
# test_ocr((data :=get_test_data()))

# def json_dump_int64(data, file_path):
#   from json import dump
#   def np_encoder(object):
#     if isinstance(object, np.generic):
#       return object.item()
#   with open(file_path, "w") as f:
#     json.dump(data,f, default=np_encoder)

# for i in range(len(res)):
#   json_dump_int64(res[i],f"ocr_data0{i+1}.json")

