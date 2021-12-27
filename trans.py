#!/usr/bin/python3
'''
translate a data_file to spanish and english
data taken from: https://preply.com/en/blog/300-most-common-english-words/
'''

import time as t
import nls_util as nut
from deep_translator import PonsTranslator as Translator
import deep_translator
from random import randrange

nut.listing(nut.grep("^[a-zA-Z]", deep_translator.__dir__()))

en_de = Translator(source="en", target="de").translate
en_es = Translator(source="en", target="es").translate
en_it = Translator(source="en", target="it").translate

def translate(word):
  return [en_it(word),en_es(word),word,en_de(word)]

def translate2(word):
  return [en_es(word), word]

def translate_file(from_file, to_file ,func=translate):
  lines = []
  with open(from_file) as f: 
    lines = f.readlines()
  with open(to_file, "w") as f:
    for i in range(len(lines)):
      trans_ = func(lines[i])
      trans = []
      for tr in trans_: trans.append(tr.replace("\n","").replace("\t",""))
      line = str(trans).replace("[", "").replace("]", "").replace("'", "").replace(",", " - ") + "\n"
      f.writelines(line)
      print(f"printed: {i}")

translate_file("trans_data_raw",  "trans_data",translate2)


