import os
from pycoingecko import CoinGeckoAPI
import pandas as pd
import plotly.express as px
import nls_util as nut
from os import system as s

from PIL import Image

import urllib.request
# urllib.request.urlretrieve(
  # 'https://media.geeksforgeeks.org/wp-content/uploads/20210318103632/gfg-300x300.png',
  #  "gfg.png")
# img = Image.open("gfg.png")
# img.show()

cg = CoinGeckoAPI()
coins = cg.get_coins()

nut.listing(coins)
type(coins)
type(coins[0])
len(coins)
nut.listing(coins[0].keys())

i = 0
for k in coins[i].keys():
  print(f"{k=}\n{coins[0][k]=}")
  if not input(f"^^ {k} [n]ext \n>") == "n":
    break

print("\n\n")
nut.listing(coins[i]["market_data"].keys())
coins[i]["market_data"].keys()
type(coins[i]["market_data"])

coins[0]["localization"]

cg.get_coin_by_id("bitcoin")
os.system("clear")

