import os
from pycoingecko import CoinGeckoAPI
import pandas as pd
import plotly.express as px
import nls_util as nut
def s(str_):
  os.system(str_)

s("clear")
cg = CoinGeckoAPI()
for c in cg.get_coins(): print(f"id -> {c[id]} \n{c}")

cg.get_coin_by_id("bitcoin")
os.system("clear")







