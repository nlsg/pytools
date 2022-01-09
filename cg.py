import os
from pycoingecko import CoinGeckoAPI
import pandas as pd
import plotly.express as px
import nls_util as nut
from sys import path; path.insert(1, '/home/nls/py/cnav')
import cnav 
from os import system as s

cg = CoinGeckoAPI()
coins = cg.get_coins()

nav = cnav.Nav()
out = []
for i in coins:
  name = i["id"]
  vs = i["market_data"]["current_price"]["usd"]
  out.append([vs, name])

out_ = []
with open("cg.ass") as f:
  for i in f.readlines():
    out_.append(i)

nut.listing(out_)



s("cat cg.ass")

# nav.navigate(out)
