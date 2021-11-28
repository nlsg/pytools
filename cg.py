import os
from multiprocessing import Process
from pycoingecko import CoinGeckoAPI
import pandas as pd
import plotly.express as px
import nls_util as nut

def s(str_):
  os.system(str_)
s("clear")
cg = CoinGeckoAPI()

def proc():
  for c in cg.get_coins():
    if c["id"] == "bitcoin":
      print("got target")
      print(c)
    print(f"id -> {c['id']} \n{c}")

p = Process(target=proc) 
p.start
p.join
https://google.com
https://google.com







