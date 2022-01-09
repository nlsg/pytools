import requests
from bs4 import BeautifulSoup
from PIL import Image
import urllib.request
import nls_util as nut

def find_headlines(response_text):
  soup = BeautifulSoup(response_text, 'lxml')
  headlines = soup.find_all("img")
  # headlines = soup.find_all(attrs={"itemprop": "headline"})
  for headline in headlines:
    print(headline.text)
  return headlines

# url = 'https://inshorts.com/en/read'
url = 'https://www.20min.ch/'
response = requests.get(url)
headlines = find_headlines(response.text)

good_headlines = []
for i in headlines:
  if "https://" in i["src"]:
    good_headlines.append(i["src"])


good_headlines = list(dict.fromkeys(good_headlines))

from io import BytesIO
for i in good_headlines:
  Image.open(BytesIO(requests.get(i).content)).show()

